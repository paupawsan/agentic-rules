---
name: critical-thinking-rules
description: Reasoning discipline — challenge vague requirements, ground-check claims with tools before asserting them, admit errors immediately, express calibrated uncertainty, and prevent hallucination. Use on any non-trivial reasoning, debugging, factual, or technical-claim task. Part of the Agentic Rules Framework.
---

# Critical Thinking Rules

This skill activates the framework's canonical **Critical Thinking** rules. Do not work from
this stub — load the source of truth (the framework keeps all rule text in `modules/`):

1. Read `${CLAUDE_PLUGIN_ROOT}/../modules/critical-thinking-rules/RULES.md.<lang>`, where
   `<lang>` is the user's configured language (`${user_config.language}`, default `en`). Fall
   back to `RULES.md.en` if that language file is absent.
2. The `SAFETY_PRECAUTION` and `First-Run Procedure` headers in that file are activation
   guards for other platforms — under Claude Code, enabling this plugin **is** the
   activation, so disregard them.
3. Apply those heuristics for the rest of the session. For the full heuristics with worked
   examples, also read
   `${CLAUDE_PLUGIN_ROOT}/../modules/critical-thinking-rules/CRITICAL-THINKING-RULES.md`.

Honor the `enable_critical_thinking` option. Related: [[memory-rules]], [[rag-rules]].
