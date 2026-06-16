---
name: agent-interaction-unit-test
description: Validate and audit agent conversations against explicit compliance criteria — framework compliance, ground-check coverage, hallucination detection, tool-call transparency, and decision documentation. Use only when the user explicitly asks to test, audit, or validate agent interaction behavior. Off by default; invoke deliberately.
disable-model-invocation: true
---

# Agent Interaction Unit Test

This skill activates the framework's canonical **Agent Interaction Unit Test** rules — an
explicit, opt-in audit mode. Do not work from this stub — load the source of truth (the
framework keeps all rule text in `modules/`):

1. Read `${CLAUDE_PLUGIN_ROOT}/modules/agent-interaction-unit-test/RULES.md.<lang>`, where
   `<lang>` is the user's configured language (`${user_config.language}`, default `en`). Fall
   back to `RULES.md.en` if that language file is absent.
2. The `SAFETY_PRECAUTION` and `First-Run Procedure` headers in that file are activation
   guards for other platforms — under Claude Code, enabling this plugin **is** the
   activation, so disregard them.
3. Run the audit and produce the compliance report. For the full algorithm specifications,
   also read `${CLAUDE_PLUGIN_ROOT}/modules/agent-interaction-unit-test/CORE-RULES.md`.

Never enable testing mode automatically — it runs only on explicit request. Honor the
`enable_agent_unit_test` option. Related: [[memory-rules]], [[critical-thinking-rules]].
