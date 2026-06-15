# Using the Agentic Rules Framework with Claude Code

The framework is **platform-neutral** — `modules/<m>/RULES.md.{en,ja,id}` is the single
source of truth for rule text, and it installs on any AI editor via the `setup.html` /
bootstrap flow (see the main [README](../README.md)). Claude Code is supported as **one
adapter among many**, packaged as a native plugin under [`claude-code/`](../claude-code/) so
the repo root stays generic. A future `cursor/` or `windsurf/` adapter would be a sibling.

**The adapter duplicates nothing.** The single source of truth stays `modules/`. The plugin
exposes it through a relative symlink — `claude-code/modules → ../modules` — which Claude Code
materializes into the plugin cache on install. (A `../modules` path that traversed *outside*
the plugin root would not survive packaging — installed plugins can't reference files above
their root, so the symlink is what makes the single-source model ship.) Anything you change
upstream — new rules, new languages, edited heuristics — flows into Claude Code via
`claude plugin update`, with no copy to keep in sync.

## Install

```bash
/plugin marketplace add paupawsan/agentic-rules
/plugin install agentic-rules@agentic-rules
```

The root `.claude-plugin/marketplace.json` points the installer at `./claude-code`. The plugin
reads its rule text from `${CLAUDE_PLUGIN_ROOT}/modules/…`, resolved through the
`claude-code/modules → ../modules` symlink that ships with the plugin and is materialized into
the cache on install. `claude plugin update` re-pulls the latest rules from upstream.

Manage it from within Claude Code:

```bash
/plugin                 # enable/disable, edit options
/agentic-rules:status   # show which modules are active
/agentic-rules:help     # orientation
```

## Repository layout

```
agentic-rules/                     # platform-neutral root (THE source of truth)
├── modules/<m>/RULES.md.{en,ja,id}   # canonical rule text — the only copy
├── .mcp.json                      # INTERNAL dev config (your KG endpoint) — never ships
├── .claude-plugin/
│   └── marketplace.json           # points at ./claude-code
└── claude-code/                   # the Claude Code adapter (no rule text *copied* here)
    ├── modules -> ../modules      # symlink to the single source; ships, materialized in cache
    ├── .claude-plugin/plugin.json
    ├── skills/                     # thin stubs that READ ${CLAUDE_PLUGIN_ROOT}/modules/<m>/RULES.md.<lang>
    ├── commands/                   # status, help
    ├── hooks/                      # SessionStart injector (opt-in) — also reads ${CLAUDE_PLUGIN_ROOT}/modules
    └── .mcp.json                   # parameterized KG server (kg_mcp_url)
```

## Component mapping

| Framework concept | Claude Code component | Location |
|-------------------|-----------------------|----------|
| Plugin manifest | `plugin.json` | `claude-code/.claude-plugin/plugin.json` |
| Distribution | `marketplace.json` | `.claude-plugin/marketplace.json` (repo root) |
| Rule modules | **Skills** (auto-invoked) — reference only | `claude-code/skills/` → read `modules/` (symlink) |
| Always-on injection | **SessionStart hook** — reference only | `claude-code/hooks/` → read `modules/` (symlink) |
| Knowledge Graph | **MCP server** | `claude-code/.mcp.json` |
| User commands | **Slash commands** | `claude-code/commands/` |
| **Rule text (all languages)** | **Source of truth** | `modules/<m>/RULES.md.{en,ja,id}` |

Each skill is a ~10-line stub: a `description` (the invocation trigger) plus an instruction to
read and apply `${CLAUDE_PLUGIN_ROOT}/modules/<m>/RULES.md.<lang>` (resolved via the
`claude-code/modules → ../modules` symlink). No rule text is copied into the plugin. The repo-root `.mcp.json` and [`.claude/`](../.claude/) are this project's
internal dev config and never ship with the plugin.

## How rules are delivered

Two modes, controlled by the `always_on_injection` option — both read the same canonical
`modules/` files:

1. **On-demand skills (default).** Each module is a skill whose `description` tells Claude
   when it's relevant. On invocation it reads the canonical rule file for the user's language
   and applies it. Low always-on token cost (~90 tokens/skill); enabling the plugin is the
   consent.

2. **Always-on injection (opt-in).** Turn on `always_on_injection` and a `SessionStart` hook
   ([`claude-code/hooks/session-start.py`](../claude-code/hooks/session-start.py)) reads the
   enabled modules' canonical rule text in the configured language and injects it into every
   session as `additionalContext` — the closest equivalent to a `CLAUDE.md`.

The `SAFETY_PRECAUTION` and `First-Run Procedure` headers in the `RULES.md.*` files are the
file-rename activation guards used on other platforms. Under Claude Code they are inert: the
skills tell Claude to disregard them, and the injector strips both blocks before injecting.

## Localization (Japanese, Indonesian, …)

Localization is **inherited from the source**, with zero adapter-side duplication:

- The `language` option (`en` / `ja` / `id`, invalid → `en`) selects which
  `modules/<m>/RULES.md.<lang>` the skills and the injector read. Always-on injection in
  Japanese is verified by the test harness (the injected text contains Japanese and differs
  from English; an unknown code falls back to English).
- **Add a language once, upstream.** Drop a `modules/<m>/RULES.md.<xx>` (the framework's
  `generate_plugin_scaffold.py` already produces these) and Claude Code can use it
  immediately — no plugin change, because the adapter only references the file.
- Skill *descriptions* (the invocation triggers) are English. That's metadata for the model,
  not user-facing text — Claude still converses with the user in their language regardless.

## Settings reference

All options are set via `/plugin` (or `--config KEY=VALUE` at install) and stored per-install.

| Option | Type | Default | Effect |
|--------|------|---------|--------|
| `language` | string | `en` | Language of the `modules/<m>/RULES.md.<lang>` that skills and the injector read (`en` / `ja` / `id`; invalid → `en`). |
| `memory_path` | directory | — | Root directory for the memory store (read by the memory skill; if blank it asks on first use). |
| `enable_memory` | boolean | `true` | Toggles the memory skill / its injection. |
| `enable_rag` | boolean | `true` | Toggles the RAG/context skill / its injection. |
| `enable_critical_thinking` | boolean | `true` | Toggles the critical-thinking skill / its injection. |
| `enable_agent_unit_test` | boolean | `false` | Toggles the unit-test module's injection. The skill is explicit-invoke only (`disable-model-invocation: true`). |
| `always_on_injection` | boolean | `false` | Off = on-demand skills; on = inject enabled rules every session. |
| `kg_mcp_url` | string | `""` (blank) | HTTP URL of a Knowledge Graph MCP server. Blank = no KG server; memory/RAG run without it. |

## Migration & adoption

**Fresh adoption on Claude Code.** Install the plugin and enable it — that's the whole setup.
You do **not** run `setup.py` or generate a `CLAUDE.md`/`AGENTS.md`; the plugin surfaces the
same canonical rules as skills.

**Migrating from the `setup.py` / generated-file flow.** On other platforms you ran `setup.py`
to copy `modules/<m>/RULES.md.<lang>` into a `CLAUDE.md` / `AGENTS.md` / `GEMINI.md`. To move
that project to the plugin:

1. Install the plugin (above).
2. Map your old settings to plugin options: the `enabled` flags in `modules/<m>/settings.json`
   become `enable_memory` / `enable_rag` / `enable_critical_thinking` /
   `enable_agent_unit_test`; your chosen rule language becomes `language`; your memory root
   becomes `memory_path`. Set them via `/plugin` or `--config`.
3. If the project has a generated rule file from the old flow (`CLAUDE.md` etc.), remove it to
   avoid the same rules loading twice — the plugin now provides them. (Keep it if you also use
   a non–Claude-Code tool on the same project.)

Both paths read the identical `modules/` source, so behavior is consistent across them.

## Knowledge Graph (optional)

The memory and RAG skills use a KG when a `kg_context` / `kg_query` tool is present, and
degrade gracefully when it isn't. To connect one, set `kg_mcp_url` to your server's HTTP
endpoint. Nothing is bundled by default, so no private endpoint ships in the plugin.

## Verifying the install

A full-coverage test harness lives in
[`claude-code/tests/test_plugin.py`](../claude-code/tests/test_plugin.py). It validates every
manifest, checks skill/command frontmatter, **confirms the skills reference `modules/` and
that no rule text is duplicated in the plugin**, exercises the injector across the full
settings matrix (including `language`), and cross-checks that the documented options exactly
match what the code consumes. Run it from the repo root:

```bash
python claude-code/tests/test_plugin.py
```
