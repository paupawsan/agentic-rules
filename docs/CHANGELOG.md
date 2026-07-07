# Changelog

All notable changes to the Agentic Rules Framework.

## [1.5.2] - 2026-07-08

### Changed

- **`kg_retire` is now named in the always-on rule text.** The temporal rules already taught retire-over-delete semantics, but the tool name only appeared in the on-invoke deep doc (`RAG-RULES.md`), leaving models to discover it via the MCP tool list. The retire step in `Runtime_Knowledge_Graph_Generation` (rag-rules `RULES.md.{en,ja,id}`) now names the tool: "use the KG server's `kg_retire` tool when available".

### Fixed

- **README documentation cleanup.** The Japanese and Indonesian README translations had drifted from the root README — missing the Knowledge Graph Integration, Unit Test, and Disclaimers sections, and containing broken relative links to module and cross-language docs (the paths didn't account for the nested localization directory). Both are now synced to the root's current structure with corrected links, and a couple of outdated claims (module count, language coverage) are fixed. The root README also had two conflicting Quick Start sections, now consolidated into one.

## [1.5.1] - 2026-07-05

### Fixed

- **Module content no longer reports a stale framework version.** The First-Run marker JSON in every module's `RULES.md.{en,ja,id}`, the `Framework: Agentic Rules vX.Y.Z` headers in the agent-interaction-unit-test report templates and examples (plus the root README example), and a filled example in `MEMORY-RULES.md` still said `1.4.0` after the 1.5.0 release — so unit-test audit reports printed the wrong framework version on non-Claude-Code platforms. All literal version strings now track the release.
- **`validate.py` gates version drift in module content.** New `check_module_content_versions()` fails the consistency gate whenever a literal version string in module markdown (First-Run marker JSON, `Agentic Rules vX.Y.Z` references, numeric version footers) disagrees with `bootstrap.json`. Deliberate `vX.Y.Z+` compatibility floors are exempt.

## [1.5.0] - 2026-07-04

### Added

- **Time-aware (bi-temporal) Knowledge Graph.** When knowledge changes, the old node is *superseded* — never edited or deleted. Nodes carry event time (`valid_at`/`invalid_at`) alongside transaction time (`created_at`/`expired_at`); default retrieval returns only current knowledge, `as_of=<date>` reconstructs what was true at any moment, and `include_expired` shows full history with `[SUPERSEDED by …]`/`[expired]` markers. An adaptation of bi-temporal database modeling for agent memory, inspired by Zep's Graphiti (concept only — no code reused). Documented in [KG_IMPLEMENTATION_GUIDE.md](KG_IMPLEMENTATION_GUIDE.md), including a database-backed (SQLite) reference schema and guidance on when (not) to adopt the temporal model and when to upgrade the KG to an MCP server.
- **Supersede-over-edit rule** in the root rules (en/ja/id), the rag-rules KG algorithms (`Incremental_Graph_Builder` resolves contradictions by supersession; `Semantic_Graph_Query` gains temporal view resolution; `Adaptive_Graph_Maintenance` is non-lossy), the memory-rules cleanup policy, and the Claude Code activation preamble (KG-configured branch instructs `kg_add` with `supersedes=<old-id>`).
- **`kg_retire` tool** documented in the rag-rules tool table: end a fact with no replacement (`invalid`), retract an erroneous record (`expired`), or undo either (`restore`).
- **`knowledge_graph.temporal` settings block** in rag-rules settings (bi-temporal tracking, supersede-over-edit, current-view default, as-of queries, recency ranking with 90-day half-life).

## [1.4.2] - 2026-06-18

### Fixed

- **Activation preamble no longer contradicts itself in the default (no-KG) install.** 1.4.1's preamble told the model "do not default to native memory; the framework store and KG are canonical" — but with no `kg_mcp_url` and no `memory_path` configured (the default), neither was actually available, so the instruction was unactionable and the model fell back to native memory anyway. The anti-native-memory nudge now lives only in the KG-configured branch (where there is a KG to steer toward); the always-emitted head is store-neutral.
- **The preamble now names the memory store.** The `SessionStart` injector surfaces `memory_path` and names it as the store, falling back to "Claude Code's project memory directory" when unset — so the directive is concrete whether or not a memory root is configured.
- Manual reworked so the Knowledge Graph reads consistently as *optional enrichment* over an always-present memory store (KG recall/write marked "when connected"), instead of clashing with the "KG is canonical" framing.

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
