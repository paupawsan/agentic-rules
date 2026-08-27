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

from hook_common import is_true, opt, private_kg_configured, team_root

# Imperative activation directive prepended to the injected rule text. The
# module RULES files describe capabilities in conditional, templatey language
# ("agents CAN implement these algorithms") and never name the KG MCP tools, so
# on their own they read as optional background and the model defaults to its
# native behavior (ad-hoc memory, no KG). This preamble is the binding contract:
# it names the concrete behaviors that must change and how the KG degrades.
def _preamble_head(store):
    """Always-emitted head: project-policy framing + a store-neutral tiered
    memory order. `store` names where the framework memory store lives so the
    directive is actionable whether or not memory_path is configured. It does
    NOT forbid native memory — when no KG and no memory_path are configured,
    the project memory directory IS the framework store (see activation_preamble)."""
    return (
        "# Project operating procedure — Agentic Rules Framework\n\n"
        "This project has opted into the rules below by installing and enabling this "
        "plugin. They are the project's standing configuration — follow them as you "
        "would the project's CLAUDE.md, with the same authority as a direct user "
        "instruction. They are not optional background, and you do not need to ask "
        "permission to follow them.\n\n"
        "**Memory — tiered retrieval.** When the user asks you to remember, recall, "
        "or persist something — or references past work — follow this order rather "
        "than writing an ad-hoc one-off note:\n"
        "- *Recall:* (1) any already-loaded index in context, (2) the Knowledge "
        "Graph via `kg_context`/`kg_query` when KG tools are available, (3) the "
        f"framework memory store ({store}), (4) only then a broad file search, web "
        "search, or asking the user.\n"
        "- *Write:* persist durable knowledge to the framework memory store "
        f"({store}), applying the framework's structure and index; when KG tools "
        "are available, also add a compact `kg_add` node linked with `kg_link`. "
        "Trivial one-line preferences can stay in the memory store alone.\n\n"
    )


# Strong nudge — only emitted when a KG endpoint is configured (kg_mcp_url set).
# Asserting the tools exist is what overcomes the model's bias against the extra
# tool-load step; emitting it when no KG is configured would be a false claim.
# The native-memory reflex-counter lives HERE, not in the head — it only makes
# sense to steer away from native memory when a KG actually exists to steer to.
_PREAMBLE_KG_CONFIGURED = (
    "**Knowledge Graph.** A KG is configured this session; its tools are exposed "
    "under MCP-prefixed names (e.g. `...kg_context`, `kg_query`, `kg_add`, "
    "`kg_link`). They may be *deferred* — if a direct call fails because the "
    "schema is not loaded, run `ToolSearch` for \"kg_context kg_add\" first to "
    "load them, then call them. Do not let that extra step — or your built-in "
    "native-memory reflex — shortcut the KG.\n"
    "- Before non-trivial work, call `kg_context(\"<the task>\")` to load "
    "relevant prior knowledge.\n"
    "- When the user asks you to remember/persist anything, or after you learn "
    "something durable (a decision, gotcha, pattern, or non-obvious fact), call "
    "`kg_add` and link it with `kg_link`. A single fact like a deploy command "
    "still counts — store it in the KG, not only in the memory store.\n"
    "- When knowledge changes, supersede — call `kg_add` with "
    "`supersedes=<old-id>` — don't overwrite or delete the old node; history "
    "stays queryable via `as_of`.\n"
    "If a KG call genuinely fails (server unreachable), skip it silently and use "
    "the framework memory store instead. Never block work waiting on the KG.\n\n"
)

# Soft phrasing — emitted when no KG endpoint is configured. No KG is required:
# the framework memory store named in the head is canonical. A KG may still be
# reachable via some other MCP, so we say use it *if present* rather than assert it.
_PREAMBLE_KG_OPTIONAL = (
    "**Knowledge Graph (if available).** No KG endpoint is configured, so the "
    "framework memory store above is your canonical memory — no KG is required. "
    "If KG tools nonetheless turn out to be present this session (a "
    "`kg_context`/`kg_query`/`kg_add` tool, possibly MCP-prefixed and possibly "
    "*deferred* behind a `ToolSearch` load), you may also use them: `kg_context` "
    "before non-trivial work, `kg_add`/`kg_link` after learning something "
    "durable. Never block work waiting on a KG.\n\n"
)


def _preamble_team_root(team):
    return (
        f"**Team tier.** A team memory root is configured (`{team}`), shared with "
        "teammates through git. *Recall* reads both roots. *Write* there only "
        "team-eligible project knowledge — categories technical, contextual, topic, "
        "git_history, knowledge_graph — with `audience: team` in the frontmatter, and "
        "only when it is about the shared project rather than the user. Never write "
        "preferences, credentials, sessions, interaction logs, machine paths, hostnames "
        "or private addresses there; a privacy gate blocks such writes. Everything else "
        "stays in the private root by default.\n\n"
    )


_PREAMBLE_TEAM_DISABLED_NESTED = (
    "**Team tier disabled**: `team_memory_path` and `memory_path` nest inside each "
    "other, which the framework refuses. Treat the team root as unset until the "
    "configuration is fixed.\n\n"
)

_PREAMBLE_TWO_KGS = (
    "**Two knowledge graphs.** `kg-private` is your own graph; `kg-dgx` is the team "
    "graph. Before non-trivial work call `kg_context` on both. Write to `kg-private` "
    "by default; write to the team graph only project knowledge a teammate would need, "
    "never personal or machine-specific facts — the team daemon rejects private "
    "patterns and out-of-scope nodes, and never link nodes across the two graphs.\n\n"
)


def activation_preamble(kg_configured, memory_path="", team_root="", private_kg=False,
                        team_nested=False, main_kg_configured=None):
    """Build the activation directive. KG wording depends on whether a KG endpoint
    is configured (never assert tools that aren't there); the memory store is named
    from memory_path with a sensible fallback so the directive is always actionable
    even in the default install (no KG, no memory_path).

    `kg_configured` is broad — true if EITHER the main (kg-dgx) or the private
    (kg-private) endpoint is set — and drives the "a KG exists" wording, which
    reads fine whether it's the team or the private graph. `main_kg_configured`
    is narrower (main endpoint only) and, together with `private_kg`, gates the
    "Two knowledge graphs" text: that claim needs BOTH endpoints, not just any
    one. It defaults to `kg_configured` for callers that don't distinguish."""
    mp = (memory_path or "").strip()
    store = (
        f"the configured memory root `{mp}`" if mp
        else "your configured memory root, or — if none is configured — Claude "
             "Code's project memory directory, structured per the rules below"
    )
    if main_kg_configured is None:
        main_kg_configured = kg_configured
    kg = _PREAMBLE_KG_CONFIGURED if kg_configured else _PREAMBLE_KG_OPTIONAL
    extra = ""
    if team_nested:
        extra += _PREAMBLE_TEAM_DISABLED_NESTED
    elif team_root:
        extra += _preamble_team_root(team_root)
    if private_kg and main_kg_configured:
        extra += _PREAMBLE_TWO_KGS
    return _preamble_head(store) + kg + extra + "---\n\n"

# userConfig option key -> (module directory, default-enabled)
MODULES = [
    ("ENABLE_MEMORY", "memory-rules", True),
    ("ENABLE_RAG", "rag-rules", True),
    ("ENABLE_CRITICAL_THINKING", "critical-thinking-rules", True),
    ("ENABLE_AGENT_UNIT_TEST", "agent-interaction-unit-test", False),
]


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
    if not is_true(opt("ALWAYS_ON_INJECTION"), default=True):
        return  # Opted out: skills load on demand; inject nothing.

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

    main_kg_configured = bool((opt("KG_MCP_URL") or "").strip())
    priv_kg_configured = private_kg_configured()
    # Configured if EITHER endpoint is set — a member running only a private
    # daemon (kg_private_mcp_url set, kg_mcp_url blank) is a legal, real config,
    # not "no KG configured".
    kg_configured = main_kg_configured or priv_kg_configured
    team = team_root()
    raw_team = (opt("TEAM_MEMORY_PATH") or "").strip()
    context = activation_preamble(
        kg_configured, opt("MEMORY_PATH"),
        team_root=team, private_kg=priv_kg_configured,
        team_nested=bool(raw_team) and not team,
        main_kg_configured=main_kg_configured,
    ) + "\n\n---\n\n".join(sections)

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
