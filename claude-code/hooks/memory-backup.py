#!/usr/bin/env python3
"""Agentic Rules Framework — periodic native-memory backup.

Runs on SessionEnd and PreCompact — a session boundary plus a periodic
mid-session checkpoint, so long sessions get more than one shot at this,
not just a single action at the very end.

Claude Code's own per-project memory directory (under
~/.claude/projects/<slug>/memory/) lives on local disk only, with no
off-machine copy. The RULES.md Write policy asks the model to persist
*durable* knowledge into the framework's memory_path, but that is a
curation judgment, not a backup guarantee — anything the model doesn't
judge durable enough stays local-only. This hook makes no such judgment:
it mirrors the whole native memory folder into memory_path as a raw
backup, unconditionally, so nothing is lost to a dead disk regardless of
what any session decided was "worth" keeping.

Deliberately additive-only: it never removes a file on the destination
side. A wrong `cwd`, an unusual project layout, or any other misfire on
the source side must never be able to erase a previously good backup.

The destination nests one level deeper than other project categories:
memory_path/projects/<project_id>/backup/claude-code-native/<native_slug>/,
where <project_id> is the framework's git-remote-or-directory-name
heuristic (co-locates with curated agent memory for the same project) and
<native_slug> is Claude Code's own per-project directory name — unique per
project path and fixed for the life of a session. Two different native
memory sources that happen to share a heuristic project_id (two clones of
the same repo, two unrelated repos with the same basename) therefore can
never collide or overwrite each other's backup.

Never fails the session: any error results in a clean no-op, same
contract as session-start.py.
"""

import json
import os
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone

from hook_common import is_true, opt


SKIP_NAMES = {".DS_Store"}
LOCK_TIMEOUT_S = 10.0
LOCK_POLL_S = 0.05


def project_id_for(cwd):
    """Best-effort project identifier: git remote name, else directory name.
    Mirrors the Project Identification Algorithm documented in
    modules/memory-rules/MEMORY-RULES.md, so backups land next to any
    curated memory already filed under the same id."""
    try:
        remote = subprocess.run(
            ["git", "-C", cwd, "remote", "get-url", "origin"],
            capture_output=True, text=True, timeout=3,
        )
        if remote.returncode == 0 and remote.stdout.strip():
            name = remote.stdout.strip().rstrip("/").rsplit("/", 1)[-1]
            if name.endswith(".git"):
                name = name[:-4]
            if name:
                return name
    except Exception:
        pass
    return os.path.basename(os.path.normpath(cwd)) or "default-project"


def _safe_segment(name):
    """True if `name` is safe to use as a single path component: non-empty,
    not '.'/'..', and containing no path separator. Both project_id (derived
    from a possibly-attacker-controlled git remote URL) and native_slug are
    validated through this before ever touching os.path.join, so a remote
    URL crafted to make project_id_for() return ".." can't escape the
    destination sandbox."""
    return bool(name) and name not in (".", "..") and "/" not in name and "\\" not in name


def _within(base, path):
    """True if realpath(path) is base or a descendant of realpath(base).
    Defense in depth on top of _safe_segment — catches any future path
    component this hook might add that _safe_segment doesn't anticipate."""
    base = os.path.realpath(base)
    path = os.path.realpath(path)
    try:
        return os.path.commonpath([base, path]) == base
    except ValueError:
        return False


class _Lock:
    """Best-effort exclusive advisory lock so two concurrent sessions backing
    up the same destination don't interleave copy2/manifest writes. Falls
    through UNLOCKED (never blocks or aborts the backup) if fcntl is
    unavailable, the lock file can't be opened, or the wait times out — a
    rare interleave is a smaller problem than a missed backup. Never unlinks
    the lock file: delete-then-relock is its own TOCTOU hazard for a
    concurrent opener."""

    def __init__(self, path, timeout=LOCK_TIMEOUT_S, poll=LOCK_POLL_S):
        self.path = path
        self.timeout = timeout
        self.poll = poll
        self._handle = None
        self._fcntl = None
        self._acquired = False

    def __enter__(self):
        try:
            import fcntl
        except ImportError:
            return self
        try:
            handle = open(self.path, "a")
        except OSError:
            return self
        self._handle = handle
        self._fcntl = fcntl
        deadline = time.monotonic() + self.timeout
        while time.monotonic() < deadline:
            try:
                fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                self._acquired = True
                break
            except OSError:
                time.sleep(self.poll)
        return self

    def __exit__(self, *_exc):
        if self._handle is None:
            return
        if self._acquired:
            try:
                self._fcntl.flock(self._handle.fileno(), self._fcntl.LOCK_UN)
            except OSError:
                pass
        self._handle.close()


def _unchanged(src_path, dst_path):
    try:
        s = os.stat(src_path)
        d = os.stat(dst_path)
    except OSError:
        return False
    return s.st_size == d.st_size and s.st_mtime_ns == d.st_mtime_ns


def mirror(src_dir, dst_dir):
    """Copy every file under src_dir into dst_dir. Additive only — updates
    and adds, never deletes a destination file that source no longer has.
    Skips a file whose destination already matches size+mtime (shutil.copy2
    preserves mtime, so this is a valid across-runs comparison) — PreCompact
    can fire repeatedly in one session, and re-copying everything every time
    scales with total memory size, not the delta. A single unreadable file
    (dangling symlink, permission error) is skipped, not fatal: mirror()
    never raises, so the manifest write always runs and reflects what
    actually happened instead of going stale on a partial failure.
    Returns (files_copied, errors)."""
    copied = 0
    errors = 0
    for root, _dirs, files in os.walk(src_dir):
        rel = os.path.relpath(root, src_dir)
        target_root = dst_dir if rel == "." else os.path.join(dst_dir, rel)
        try:
            os.makedirs(target_root, exist_ok=True)
        except OSError:
            errors += 1
            continue
        for name in files:
            if name in SKIP_NAMES:
                continue
            src_path = os.path.join(root, name)
            dst_path = os.path.join(target_root, name)
            if _unchanged(src_path, dst_path):
                continue
            try:
                shutil.copy2(src_path, dst_path)
                copied += 1
            except OSError:
                errors += 1
    return copied, errors


def _log(message):
    print(f"memory-backup: {message}", file=sys.stderr)


def main():
    if not is_true(opt("ENABLE_MEMORY"), default=True):
        return  # Memory module disabled: nothing to back up.

    memory_path = (opt("MEMORY_PATH") or "").strip()
    if not memory_path:
        return  # No separate framework store configured — native is already canonical.

    payload = json.load(sys.stdin)

    transcript_path = payload.get("transcript_path") or ""
    cwd = payload.get("cwd") or ""
    if not transcript_path or not cwd:
        return

    # The native memory dir sits next to the session transcript:
    # ~/.claude/projects/<slug>/memory/ , ~/.claude/projects/<slug>/<session>.jsonl
    session_dir = os.path.dirname(transcript_path)
    src = os.path.join(session_dir, "memory")
    if not os.path.isdir(src):
        return  # Nothing written to native memory yet this project.

    project_id = project_id_for(cwd)
    native_slug = os.path.basename(session_dir)
    if not _safe_segment(project_id) or not _safe_segment(native_slug):
        return  # Unsafe path component — refuse rather than guess.

    projects_root = os.path.join(os.path.expanduser(memory_path), "projects")
    dst = os.path.join(
        projects_root, project_id, "backup", "claude-code-native", native_slug,
    )
    if not _within(projects_root, dst):
        return  # Defense in depth: never write outside memory_path/projects/.

    try:
        os.makedirs(dst, exist_ok=True)
    except OSError as exc:
        _log(f"cannot create backup dir {dst}: {exc}")
        return

    with _Lock(dst.rstrip(os.sep) + ".lock"):
        copied, errors = mirror(src, dst)
        manifest = os.path.join(dst, ".backup_manifest.json")
        tmp_manifest = f"{manifest}.{os.getpid()}.tmp"
        try:
            with open(tmp_manifest, "w", encoding="utf-8") as handle:
                json.dump(
                    {
                        "last_backup_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                        "source": src,
                        "files_copied": copied,
                        "files_skipped_errors": errors,
                        "trigger": payload.get("hook_event_name", "unknown"),
                    },
                    handle,
                    indent=2,
                )
            os.replace(tmp_manifest, manifest)
        except OSError as exc:
            _log(f"cannot write backup manifest {manifest}: {exc}")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
