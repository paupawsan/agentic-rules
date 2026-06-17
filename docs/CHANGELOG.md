# Changelog

All notable changes to the Agentic Rules Framework.

## [1.4.1] - 2026-06-18

### Changed

- **Claude Code plugin: always-on rule injection is now the default.** Verified through the real `/plugins` install path that on-demand skills did not reliably activate — the model's built-in memory won out and the Knowledge Graph was never called, even with a KG connected. The `SessionStart` injector now defaults on (opt out with `always_on_injection: false`) and prepends an imperative activation directive so the rules actually take effect.
- **Tiered memory retrieval** enforced in the activation preamble and documented in [CLAUDE_CODE_PLUGIN.md](CLAUDE_CODE_PLUGIN.md): a recall order (in-context index → KG via `kg_context`/`kg_query` → framework memory files → broad/web/ask) and paired writes (`kg_add` + `kg_link` alongside the memory file).

### Fixed

- The activation preamble no longer asserts that KG tools exist when no `kg_mcp_url` is configured (the default install): the Knowledge Graph section is conditional on a configured endpoint, with graceful "if available" wording otherwise — so it never directs the model to load tools that aren't there.

## [1.4.0] - 2026-06-16

### ⚠️ Breaking Changes

- **`.agentic_initialized` marker is now project-local.** The marker is written to `$CWD/.agentic_initialized` (the project the agent works on) by the agent at runtime, instead of inside the `agentic-rules/` framework directory. A framework-local marker would skip bootstrap for every project after the first; AI editors operate per-project.
  - **Migration**: delete any old `agentic-rules/.agentic_initialized` file. Each project re-initializes once on the agent's next session, automatically.
  - Add `.agentic_initialized` to your project's `.gitignore` — it is runtime state, not configuration.

### Added

- First-run loading model: 12 `RULES.md.{en,ja,id}` skeletons with a 5-step bootstrap procedure executed by the agent on first use ([FIRST_RUN_LOADING.md](FIRST_RUN_LOADING.md))
- Content authoring guide documenting the two-track source-of-truth pipeline ([CONTENT_AUTHORING.md](CONTENT_AUTHORING.md))
- `validate.py` — consistency checks for versions, module lists, and generated-artifact staleness
- This changelog

### Changed

- Critical-thinking-rules fully rewritten: concrete heuristics and 12 worked scenarios replace rhetoric (en/ja/id)
- All version strings aligned to 1.4.0 across manifests, module settings, READMEs, and generated artifacts
- `Bootstrap.md` marker-check commands updated to the project-local location

### Fixed

- `setup-launcher.py`: removed unreachable duplicate `main()`; plugin directory lists are now loaded from `plugins.json` in both file-creation and cleanup paths (the cleanup fallback list was missing `agent-interaction-unit-test`)
- `generate_plugin_scaffold.py`: temp-directory cleanup no longer relies on a bare `except`; fallback removal now actually runs when `git worktree remove` fails

## [1.3.0]

- Cursor 2.0 multi-agent integration (`settings/cursor-2.0-multi-agent-adapter.json`, agent coordination guide)

## [1.2.x and earlier]

- Agent Interaction Unit Test module, Knowledge Graph integration docs, multi-language setup UI (en/ja/id). See git history.
