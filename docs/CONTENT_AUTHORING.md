# Content Authoring Guide

## Source-of-Truth Model

The framework has two parallel content tracks that serve different consumers:

### Track 1: Skeletons (drive the setup generator)

```
modules/*/RULES.md.{en,ja,id}
        ↓  generate_simple_setup.py
web-config.json  (embedded template strings)
        ↓  generate_simple_setup.py
setup.html  (staticWebConfig JS constant)
        ↓  setup.py / setup-launcher.py / setup.html UI
CLAUDE.md / AGENTS.md / GEMINI.md  (what AI editors load)
```

**These are what agents actually read at runtime.** Keep them compact. The first-run procedure, module overview, and key algorithms go here. Implementation detail goes in the full files.

### Track 2: Full Rule Files (drive the KG seed)

```
modules/*/[NAME]-RULES.md  (e.g., MEMORY-RULES.md, RAG-RULES.md)
        ↓  ~/.claude/mcp-servers/kg-server/migrate.py
KG nodes in ~/.claude/memory/kg.db
        ↓  kg_context / kg_query at runtime
Agent receives relevant rules, patterns, gotchas
```

**These are reference documentation + KG seeds.** They contain the full algorithmic specs, filled examples, templates, and implementation details. Currently English-only.

## Editing Rules

### After editing `RULES.md.{en,ja,id}` (skeletons):

1. Run `python generate_simple_setup.py`
2. Commit the regenerated `web-config.json` and `setup.html` together with your edits
3. Existing activated files (CLAUDE.md/AGENTS.md) in user projects won't auto-update — users must re-run setup

### After editing `{NAME}-RULES.md` (full files):

1. Optionally re-run `python ~/.claude/mcp-servers/kg-server/migrate.py` to refresh KG seed
2. No regeneration needed (these files are not embedded in setup.html)

### After editing `localization.json`:

1. Run `python update_localization.py`
2. This updates the embedded localization object in `setup.html`

## Regeneration is a Gate

If you edit a skeleton and forget to regenerate, the published `setup.html` will be stale. The next user who runs setup will get old content.

Verification: run `python3 validate.py`. It checks that every `web-config.json` template matches its `RULES.md.{lang}` source, that `setup.html` embeds the current web-config, that version fields agree across all manifests, and that hardcoded module lists match `plugins.json`. Run it before committing any skeleton or manifest change.

## File Naming Conventions

| File | Purpose | Consumer |
|------|---------|----------|
| `RULES.md.en` | English skeleton template | `generate_simple_setup.py` → editors |
| `RULES.md.ja` | Japanese skeleton template | `generate_simple_setup.py` → editors |
| `RULES.md.id` | Indonesian skeleton template | `generate_simple_setup.py` → editors |
| `MEMORY-RULES.md` | Full memory rules spec | `migrate.py` → KG, humans |
| `RAG-RULES.md` | Full RAG rules spec | `migrate.py` → KG, humans |
| `CRITICAL-THINKING-RULES.md` | Full critical thinking spec | `migrate.py` → KG, humans |
| `CORE-RULES.md` | Full agent-interaction spec | humans |
| `settings.json` | Per-module configuration | agents at runtime |
| `setup.json` | UI config for setup.html | `generate_simple_setup.py` |

## Safety Precaution Blocks

Every `RULES.md.{lang}` skeleton must contain:

```html
<!-- SAFETY_PRECAUTION_START -->
...template protection warning...
<!-- SAFETY_PRECAUTION_END -->
```

`setup.py` strips these blocks when generating CLAUDE.md/AGENTS.md/GEMINI.md. Without them, agents could auto-load template files instead of waiting for activation.

<!-- LICENSE: Copyright (c) 2025-2026 Paulus Ery Wasito Adhi. Licensed under the MIT License (see LICENSE file). -->
