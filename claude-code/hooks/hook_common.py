"""Shared helpers for the Agentic Rules Claude Code hooks.

Not itself a hook — imported by session-start.py and memory-backup.py, both
invoked as `python3 "<abs-path>/hooks/<script>.py"`. Python auto-adds the
invoked script's own directory to sys.path[0], so the plain
`from hook_common import ...` resolves with no PYTHONPATH setup needed.
"""

import os


TRUE_VALUES = {"true", "1", "yes", "on"}


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


import json
import re
import subprocess

MARKER_FILE = ".agentic-rules.json"
_PROJECT_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$")


def _marker_project_id(cwd):
    """Walk up from cwd looking for .agentic-rules.json; stop at the git
    top-level (if any) or the filesystem root. Invalid ids are ignored."""
    top = None
    try:
        proc = subprocess.run(["git", "-C", cwd, "rev-parse", "--show-toplevel"],
                              capture_output=True, text=True, timeout=3)
        if proc.returncode == 0:
            top = os.path.realpath(proc.stdout.strip())
    except Exception:
        pass
    here = os.path.realpath(cwd)
    while True:
        candidate = os.path.join(here, MARKER_FILE)
        if os.path.isfile(candidate):
            try:
                with open(candidate, "r", encoding="utf-8") as handle:
                    pid = str(json.load(handle).get("project_id", "")).strip()
                if _PROJECT_ID_RE.match(pid):
                    return pid
            except (OSError, ValueError):
                pass
            return ""
        if here == top or os.path.dirname(here) == here:
            return ""
        here = os.path.dirname(here)


def project_id_for(cwd):
    """Project identifier: repo marker, else git remote name, else directory
    name. Mirrors the Project Identification Algorithm in MEMORY-RULES.md."""
    pid = _marker_project_id(cwd)
    if pid:
        return pid
    try:
        remote = subprocess.run(["git", "-C", cwd, "remote", "get-url", "origin"],
                                capture_output=True, text=True, timeout=3)
        if remote.returncode == 0 and remote.stdout.strip():
            name = remote.stdout.strip().rstrip("/").rsplit("/", 1)[-1]
            if name.endswith(".git"):
                name = name[:-4]
            if name:
                return name
    except Exception:
        pass
    return os.path.basename(os.path.normpath(cwd)) or "default-project"


def _nested(a, b):
    a, b = os.path.realpath(a), os.path.realpath(b)
    try:
        return os.path.commonpath([a, b]) in (a, b)
    except ValueError:
        return False


def team_root():
    """team_memory_path, or "" when unset or nested with memory_path."""
    team = os.path.expanduser((opt("TEAM_MEMORY_PATH") or "").strip())
    if not team:
        return ""
    private = os.path.expanduser((opt("MEMORY_PATH") or "").strip())
    if private and _nested(private, team):
        return ""
    return team


def private_kg_configured():
    return bool((opt("KG_PRIVATE_MCP_URL") or "").strip())


def team_tier_active():
    return bool(team_root()) or private_kg_configured()
