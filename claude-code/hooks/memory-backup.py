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

Never fails the session: any error results in a clean no-op, same
contract as session-start.py.
"""

import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone


TRUE_VALUES = {"true", "1", "yes", "on"}
SKIP_NAMES = {".DS_Store"}


def opt(key, default=""):
    """Read a plugin userConfig value, tolerating casing variants."""
    for name in (f"CLAUDE_PLUGIN_OPTION_{key}", f"CLAUDE_PLUGIN_OPTION_{key.lower()}"):
        if name in os.environ:
            return os.environ[name]
    return default


def is_true(value, default=False):
    value = (value or "").strip().lower()
    if not value:
        return default
    return value in TRUE_VALUES


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


def mirror(src_dir, dst_dir):
    """Copy every file under src_dir into dst_dir. Additive only — updates
    and adds, never deletes a destination file that source no longer has."""
    copied = 0
    for root, _dirs, files in os.walk(src_dir):
        rel = os.path.relpath(root, src_dir)
        target_root = dst_dir if rel == "." else os.path.join(dst_dir, rel)
        os.makedirs(target_root, exist_ok=True)
        for name in files:
            if name in SKIP_NAMES:
                continue
            shutil.copy2(os.path.join(root, name), os.path.join(target_root, name))
            copied += 1
    return copied


def main():
    if not is_true(opt("ENABLE_MEMORY"), default=True):
        return  # Memory module disabled: nothing to back up.

    memory_path = (opt("MEMORY_PATH") or "").strip()
    if not memory_path:
        return  # No separate framework store configured — native is already canonical.

    try:
        payload = json.load(sys.stdin)
    except Exception:
        return

    transcript_path = payload.get("transcript_path") or ""
    cwd = payload.get("cwd") or ""
    if not transcript_path or not cwd:
        return

    # The native memory dir sits next to the session transcript:
    # ~/.claude/projects/<slug>/memory/ , ~/.claude/projects/<slug>/<session>.jsonl
    src = os.path.join(os.path.dirname(transcript_path), "memory")
    if not os.path.isdir(src):
        return  # Nothing written to native memory yet this project.

    project_id = project_id_for(cwd)
    dst = os.path.join(
        os.path.expanduser(memory_path), "projects", project_id,
        "backup", "claude-code-native",
    )

    try:
        os.makedirs(dst, exist_ok=True)
        count = mirror(src, dst)
        manifest = os.path.join(dst, ".backup_manifest.json")
        with open(manifest, "w", encoding="utf-8") as handle:
            json.dump(
                {
                    "last_backup_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                    "source": src,
                    "files_copied": count,
                    "trigger": payload.get("hook_event_name", "unknown"),
                },
                handle,
                indent=2,
            )
    except OSError:
        return


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
