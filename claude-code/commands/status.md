---
description: Show which Agentic Rules modules are active and how the framework is configured.
---

Report the current state of the **Agentic Rules Framework** plugin to the user:

1. **Active rule modules.** For each module, state whether it is enabled (from the plugin's userConfig options) and what it does:
   - `memory-rules` — persistent cross-session memory.
   - `rag-rules` — context optimization and source-grounded retrieval.
   - `critical-thinking-rules` — verification and calibrated-uncertainty heuristics.
   - `agent-interaction-unit-test` — conversation auditing (explicit invocation only).

2. **Delivery mode.** State whether `always_on_injection` is on (rules injected every session via the SessionStart hook) or off (rules load on demand as skills — the default).

3. **Knowledge Graph.** Report whether a KG tool (e.g. `kg_context`) is available this session. If not, note that memory/RAG run without KG enrichment.

4. **Memory path.** If the `memory_path` option is set, show it; otherwise note the memory skill will ask on first use.

5. **How to change it.** Tell the user that configuration is managed with `/plugin` (enable/disable the plugin, edit its options) — not by editing files in an installed plugin.

Keep the report concise — a short labeled list, not prose.
