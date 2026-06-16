---
name: memory-rules
description: Persistent cross-session memory — store and recall user facts, project context, decisions, and error corrections. Use when the user asks to remember or recall something, references past work, starts work in a project, or when continuity across sessions matters. Part of the Agentic Rules Framework.
---

# Memory Rules

This skill activates the framework's canonical **Memory** rules. Do not work from this
stub — load the source of truth (the framework keeps all rule text in `modules/`):

1. Read `${CLAUDE_PLUGIN_ROOT}/modules/memory-rules/RULES.md.<lang>`, where `<lang>` is
   the user's configured language (`${user_config.language}`, default `en`). Fall back to
   `RULES.md.en` if that language file is absent.
2. The `SAFETY_PRECAUTION` and `First-Run Procedure` headers in that file are activation
   guards for other platforms — under Claude Code, enabling this plugin **is** the
   activation, so disregard them.
3. Apply those rules for the rest of the session. For the full algorithms, also read
   `${CLAUDE_PLUGIN_ROOT}/modules/memory-rules/MEMORY-RULES.md`.

Honor the `enable_memory` and `memory_path` options. Related: [[rag-rules]],
[[critical-thinking-rules]].
