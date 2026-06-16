# First-Run Loading Guide

## Two-Level Initialization Model

The framework has two distinct initialization phases:

### Setup-Time (User Action)
The user runs `setup.py`, `setup-launcher.py`, or `setup.html` to generate editor-specific rule files:
- `AGENTS.md` (Cursor 1.x, Antigravity, Cline, Aider, generic)
- `CLAUDE.md` (Claude Code)
- `GEMINI.md` (Google AI editors)

If these files exist, setup has completed. No marker file is written for this phase.

### Runtime (Agent Action)
When an AI editor agent starts a session and reads the rules, it executes the **First-Run Procedure** (defined below). On completion, it writes `.agentic_initialized` in the working directory. Future sessions detect this marker and skip the procedure.

**The marker is runtime-only.** Written by the agent, never by `setup.py`. If the installer wrote it, the agent would think bootstrap is done without ever actually running it.

---

## First-Run Procedure

This is the canonical 5-step procedure embedded at the top of every `RULES.md.{lang}` skeleton. Agents execute it once per project on first session.

### Step 1: Check Marker
Look for `.agentic_initialized` in the current working directory.

**Cross-platform detection** (hidden dot-file):
- Unix/macOS: `find . -maxdepth 1 -name '.agentic_initialized' -type f`
- Windows PowerShell: `Get-ChildItem -Path . -Force -File | Where-Object {$_.Name -eq '.agentic_initialized'}`
- Python: `pathlib.Path('.agentic_initialized').exists()`
- **Avoid**: `os.listdir()` and bare `glob.glob('*')` — these miss dot-files on some platforms.

See `docs/CROSS_PLATFORM_HIDDEN_FILE_DETECTION.md` for full platform reference.

If the marker exists and its `version` field matches the framework version, skip to normal response.

### Step 2: Read Active Rules
The editor loaded one of: `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, or `.cursorrules`. Check `modules/*/settings.json` to determine which rules are enabled:
- `memory_rules.enabled`
- `rag_rules.enabled`
- `critical_thinking_rules.enabled`
- `agent_interaction_unit_test.enabled`

### Step 3: Load KG Context (Optional)
If the `kg_context` MCP tool is available, call:
```
kg_context('starting work in this project')
```
This loads relevant rules, patterns, and gotchas from the Knowledge Graph. If the tool is not available (e.g., editor doesn't support MCP), skip silently — no error, no warning.

### Step 4: Acknowledge
Tell the user in one short sentence which rules are active. Example:
> "Agentic Rules Framework active (memory + RAG + critical thinking)."

Do **not** prompt with "would you like to enable..." questions. Those belong to the setup phase (`setup.html` / `setup.py`), not runtime.

### Step 5: Write Marker
Create `.agentic_initialized` in the current working directory with this JSON:
```json
{
  "version": "1.4.0",
  "initialized_at": "2026-04-12T10:30:00Z",
  "marker_format_version": 1,
  "agent": "claude-code"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `version` | string | Framework version at time of bootstrap |
| `initialized_at` | string | ISO 8601 UTC timestamp |
| `marker_format_version` | integer | Schema version for forward compatibility (currently `1`) |
| `agent` | string | Editor name if known (optional) |

---

## Marker Location

**Location**: `$CWD/.agentic_initialized` (project-local).

**Note**: This is a deliberate change from the `agentic-rules/.agentic_initialized` (framework-local) location referenced in `Bootstrap.md`. Reason: AI editors operate per-project. A framework-local marker would skip bootstrap for every project after the first, which defeats the purpose.

---

## Per-Editor Wiring

The first-run procedure must be **visible to the agent** at session start. Each editor has its own mechanism:

### Claude Code
- The procedure is embedded at the top of `CLAUDE.md` (which Claude Code always loads from `.claude/CLAUDE.md` or project root).
- **Optional enhancement**: Add a `SessionStart` hook in `.claude/settings.json`:
```json
{
  "hooks": {
    "SessionStart": [
      {
        "type": "command",
        "command": "test -f .agentic_initialized && echo 'Framework initialized' || echo 'First run — bootstrap will execute'",
        "statusMessage": "Checking framework status"
      }
    ]
  }
}
```

### Cursor 1.x
- Place the procedure at the top of `.cursorrules` (always-on rules that Cursor injects into every session).

### Cursor 2.0 (Multi-Agent)
- The orchestrator agent (`.cursor/agents/orchestrator.md`) handles bootstrap for all sub-agents.
- The procedure goes in the orchestrator config. Sub-agents (memory-agent, rag-agent, etc.) don't need their own bootstrap — the orchestrator coordinates.
- See `settings/cursor-2.0-multi-agent-adapter.json` for the multi-agent architecture.

### Antigravity / Generic AGENTS.md Consumers
- Place the procedure at the top of `AGENTS.md`. Most generic consumers (Cline, Aider, Continue, etc.) read `AGENTS.md` at session start.

---

## Graceful Degradation

If the agent ignores the first-run procedure entirely:
- Enabled rules still work as configured.
- Memory recording and persistence defer until the user explicitly asks.
- The framework never blocks the user or refuses to respond.

The marker is a **soft signal** that lets the agent know it's a returning session. It is not a hard gate.

---

## Post-Install (Optional, For Project Owner)

After installing or upgrading the framework, the project owner can optionally seed the Knowledge Graph with framework rules:

```bash
python ~/.claude/mcp-servers/kg-server/migrate.py
```

Re-run after framework upgrades to refresh seeded knowledge.

This step is for the **human project owner**, not the AI agent. The agent accesses the KG via `kg_context` / `kg_query` tools at runtime.

---

## Relationship to Bootstrap.md and bootstrap.json

- **`Bootstrap.md`**: The algorithmic specification for framework loading. Still authoritative for Cursor 2.0's `framework_integration: { bootstrap_compliance: true }`. The first-run procedure is a simplified runtime version of Bootstrap.md's algorithms.
- **`bootstrap.json`**: Defines the 7-step loading sequence with proactive user prompts, rule interconnections, and platform adapters. The JSON is consumed by the setup pipeline and Cursor 2.0 multi-agent integration — not by agents at runtime. The first-run procedure replaces the eager prompts in steps 3–6.5 with a single acknowledgment (step 4).
- **`docs/CROSS_PLATFORM_HIDDEN_FILE_DETECTION.md`**: Detailed platform-specific commands for hidden file detection. Referenced from step 1 of the procedure.
- **`docs/PRELOAD-COMMAND.md`**: Manual preload flow for Cursor. Complementary to the first-run procedure.

<!-- LICENSE: Copyright (c) 2025-2026 Paulus Ery Wasito Adhi. Licensed under the MIT License (see LICENSE file). -->
