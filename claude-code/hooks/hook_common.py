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
