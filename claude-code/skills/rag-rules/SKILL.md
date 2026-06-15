---
name: rag-rules
description: Context optimization and retrieval discipline — hierarchical reading, relevance scoring, grounding answers in retrieved sources, and optional runtime knowledge-graph enrichment. Use when working across many files or a large codebase, when answers must be grounded in source material, or when the context window needs to be spent wisely. Part of the Agentic Rules Framework.
---

# RAG / Context Rules

This skill activates the framework's canonical **RAG / context** rules. Do not work from
this stub — load the source of truth (the framework keeps all rule text in `modules/`):

1. Read `${CLAUDE_PLUGIN_ROOT}/../modules/rag-rules/RULES.md.<lang>`, where `<lang>` is the
   user's configured language (`${user_config.language}`, default `en`). Fall back to
   `RULES.md.en` if that language file is absent.
2. The `SAFETY_PRECAUTION` and `First-Run Procedure` headers in that file are activation
   guards for other platforms — under Claude Code, enabling this plugin **is** the
   activation, so disregard them.
3. Apply those rules for the rest of the session. For the full algorithms (context
   optimization, KG construction, tool-selection, safety), also read
   `${CLAUDE_PLUGIN_ROOT}/../modules/rag-rules/RAG-RULES.md`.

Honor the `enable_rag` option. Related: [[memory-rules]], [[critical-thinking-rules]].
