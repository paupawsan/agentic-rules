---
description: Explain the Agentic Rules Framework — what each module does and how to use it in Claude Code.
---

Give the user a brief orientation to the **Agentic Rules Framework** plugin:

- **What it is.** A set of behavioral rules delivered as Claude Code skills that load automatically when relevant. Enabling the plugin is the activation — there is no separate setup step in Claude Code.
- **The modules:**
  - **Memory** — stores and recalls facts, decisions, and corrections across sessions.
  - **RAG / context** — hierarchical reading, relevance scoring, source-grounded answers.
  - **Critical thinking** — challenge vague requirements, ground-check claims, calibrate uncertainty, prevent hallucination.
  - **Agent interaction unit-test** — audit a conversation against compliance criteria (invoke explicitly).
- **How rules load.** By default the skills auto-invoke when the task calls for them. For strict always-on behavior, enable the `always_on_injection` option so rules are injected at session start.
- **Commands.** `/agentic-rules:status` shows what's active. Configure everything with `/plugin`.
- **Knowledge Graph (optional).** Set the `kg_mcp_url` option to connect a KG MCP server; memory and RAG use it when present and degrade gracefully when not.

Point the user to the project README for the full framework (including the non-Claude-Code setup paths) if they want depth.
