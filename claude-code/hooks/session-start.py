#!/usr/bin/env python3
"""Agentic Rules Framework — SessionStart injector.

Optional "always-on" path for the Claude Code plugin. When the plugin's
``always_on_injection`` userConfig option is enabled, this hook reads the
enabled modules' localized rule snippets and injects them into the session as
additionalContext — the closest equivalent to a CLAUDE.md the plugin can offer.

When the option is off (the default), the script exits silently and rules load
on demand as skills instead. The script never fails the session: any error
results in a clean no-op.

Reads configuration from environment variables that Claude Code populates from
the plugin's userConfig (CLAUDE_PLUGIN_OPTION_<KEY>), and locates bundled rule
files via CLAUDE_PLUGIN_ROOT.
"""

import json
import os
import re
import sys


TRUE_VALUES = {"true", "1", "yes", "on"}

# userConfig option key -> (module directory, default-enabled)
MODULES = [
    ("ENABLE_MEMORY", "memory-rules", True),
    ("ENABLE_RAG", "rag-rules", True),
    ("ENABLE_CRITICAL_THINKING", "critical-thinking-rules", True),
    ("ENABLE_AGENT_UNIT_TEST", "agent-interaction-unit-test", False),
]


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


def clean(text):
    """Strip template-only scaffolding that doesn't apply to an installed plugin."""
    # Remove the SAFETY_PRECAUTION block (template-protection guard).
    text = re.sub(
        r"<!--\s*SAFETY_PRECAUTION_START\s*-->.*?<!--\s*SAFETY_PRECAUTION_END\s*-->",
        "",
        text,
        flags=re.DOTALL,
    )
    # Remove the First-Run Procedure section (references repo-relative paths).
    # Match the heading in any language — skeletons localize it bilingually,
    # e.g. "## 初回実行手順 / First-Run Procedure" — so allow text before the
    # English anchor instead of requiring it immediately after "## ".
    # Bound the section by the next "## " heading OR end-of-text (\Z), so the
    # strip still works if First-Run Procedure is the last section.
    text = re.sub(
        r"\n##\s+[^\n]*First-Run Procedure\b.*?(?=\n##\s|\Z)",
        "\n",
        text,
        flags=re.DOTALL,
    )
    # Drop remaining HTML comments (metadata/license markers).
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    return text.strip()


def main():
    if not is_true(opt("ALWAYS_ON_INJECTION"), default=False):
        return  # Default mode: skills load on demand; inject nothing.

    root = os.environ.get("CLAUDE_PLUGIN_ROOT", "")
    if not root:
        return
    # Reference the canonical rule text via the in-plugin `modules` symlink
    # (claude-code/modules -> ../modules). The symlink — not a copy — is what
    # ships: Claude Code materializes the symlinked tree inside the plugin cache
    # on install, so ${CLAUDE_PLUGIN_ROOT}/modules resolves to the single source
    # in modules/. A path that traversed OUTSIDE the plugin root (../modules)
    # would not survive packaging.
    modules_root = os.path.join(root, "modules")
    if not os.path.isdir(modules_root):
        return

    lang = (opt("LANGUAGE", "en") or "en").strip().lower()
    if lang not in {"en", "ja", "id"}:
        lang = "en"

    sections = []
    for key, module, default_enabled in MODULES:
        if not is_true(opt(key), default=default_enabled):
            continue
        module_dir = os.path.join(modules_root, module)
        path = os.path.join(module_dir, f"RULES.md.{lang}")
        if not os.path.isfile(path):
            path = os.path.join(module_dir, "RULES.md.en")
        if not os.path.isfile(path):
            continue
        try:
            with open(path, "r", encoding="utf-8") as handle:
                body = clean(handle.read())
        except OSError:
            continue
        if body:
            sections.append(body)

    if not sections:
        return

    header = (
        "# Agentic Rules Framework (active)\n\n"
        "The following behavioral rules are active for this session. Apply them "
        "to your work as standing guidance.\n"
    )
    context = header + "\n\n---\n\n".join(sections)

    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "SessionStart",
                    "additionalContext": context,
                }
            }
        )
    )


if __name__ == "__main__":
    try:
        main()
    except Exception:
        # Never break a session because of rule injection.
        sys.exit(0)
