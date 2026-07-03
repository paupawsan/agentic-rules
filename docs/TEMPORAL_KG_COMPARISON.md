# Temporal Knowledge Graph — Before/After Comparison

> Companion to the [Time-Aware (Bi-Temporal) Knowledge Model](KG_IMPLEMENTATION_GUIDE.md#-time-aware-bi-temporal-knowledge-model-v150)
> section of the KG Implementation Guide. This document shows the *behavioral*
> difference between a conventional (non-temporal) KG and the v1.5.0 temporal model,
> using a reproducible A/B test and a real production validation.

## Why this exists

A KG that only *adds* facts eventually ranks stale knowledge above its replacement.
The motivating real-world failure: an outdated high-priority rule node kept
surfacing in retrieval, and the only fix was to hand-edit its content to say
"SUPERSEDED" and manually demote its priority — rewriting history to work around
the ranking. The temporal model fixes this at the data layer.

## The A/B test

Both servers were seeded identically, through their own public tools, with the exact
shape of that incident:

- a **stale fact** at priority 9 — `"The deploy target is ALPHA (set up in January)."`
- its **replacement** at priority 7 — `"The deploy target is BETA since June — alpha was decommissioned."`
- a `supersedes` edge from the replacement to the stale fact

Then the same query ran against both.

### A — conventional KG (before)

```
## Results for "… deploy target" (2 matches)

[fact:stale-example] (p:9, scope:project:compare)      ← STALE FACT RANKS FIRST
The deploy target is ALPHA (set up in January).

[fact:current-example] (p:7, scope:project:compare)
The deploy target is BETA since June — alpha was decommissioned.
-> supersedes: stale-example                            (edge exists but is ignored)
```

The superseded fact not only surfaces — its higher priority ranks it **above** its
own replacement. An agent trusting the top result acts on outdated knowledge.

### B — temporal KG (after)

```
## Results for "… deploy target" (1 matches)

[fact:current-example] (p:7, scope:project:compare)     ← ONLY CURRENT KNOWLEDGE
The deploy target is BETA since June — alpha was decommissioned.
-> supersedes: stale-example [invalidated 2026-07-03]
```

The stale fact is hidden from the default view; the `supersedes` edge renders as an
annotated pointer instead of re-injecting hidden content.

### B — history stays queryable (non-lossy)

```
kg_query("… deploy target", include_expired=True)

[fact:stale-example] (p:9) [SUPERSEDED by current-example]
The deploy target is ALPHA (set up in January).

[fact:current-example] (p:7)
The deploy target is BETA since June — alpha was decommissioned.
```

```
kg_get_node("stale-example")

Status: superseded by current-example at 2026-07-03T21:42Z
Valid: 2026-07-03T21:42Z → 2026-07-03T21:42Z
Supersession chain: stale-example -> current-example (newest last)
```

Nothing was deleted. The old fact keeps its full content, carries its validity
interval, and names its successor.

## Production validation

The temporal model was validated against a live, long-lived personal KG (several
hundred nodes) served over MCP:

| Check | Result |
|-------|--------|
| In-place migration (pure `ADD COLUMN`): node/edge/embedding counts unchanged, all rows backfilled `valid_at = created_at` | ✅ |
| The real formerly-hand-demoted node, repaired with one `supersedes` link: hidden from default retrieval, its replacement surfaces instead | ✅ |
| `kg_get_node` on it reports `Status: superseded by … at …` with validity interval and supersession chain | ✅ |
| Time travel: `as_of` set to a date inside its old validity window returns it as then-current, and hides the successor (not yet valid then) | ✅ |
| Backward compatibility: every pre-temporal tool signature works unchanged | ✅ |

## Capability comparison

| Capability | Conventional KG | Temporal KG (v1.5.0) |
|------------|-----------------|----------------------|
| Outdated knowledge in default results | surfaces; can outrank its replacement | hidden automatically on supersession |
| Replacing a fact | hand-edit old text + demote priority (rewrites history) | `kg_add(…, supersedes=old)` — one atomic call |
| "What did we know on date X?" | unanswerable | `as_of=<ISO date>` on query/context |
| History | manual text conventions only | non-lossy: `include_expired`, `[SUPERSEDED by …]` markers, supersession chains |
| Fact ends with no replacement | delete or hand-edit | `kg_retire` (invalid / expired / restore — reversible) |
| Validity windows | — | `valid_from` / `valid_until`, including retroactive facts |
| Contradictions | edge type exists but inert | recorded without hiding either side; resolution advisory |
| Near-duplicate detection at write | — | embedding KNN advisory suggests supersede/contradict |
| Freshness in ranking | — | gentle recency boost (90-day half-life, tie-breaker only) |

## Test coverage behind this comparison

- **59-check local suite** against a scratch copy of a real database: idempotent
  in-place migration, FTS/vector rowid alignment, mixed timestamp-format parsing,
  old-signature compatibility, atomic supersession, as-of window math (five cases),
  retire/restore round-trips, contradiction semantics, retroactive and future
  validity windows, bounded recency boost, and the context-expansion gate (a
  `supersedes` edge must not re-inject hidden content).
- **6-assertion A/B harness**: the conventional baseline (the previous server
  extracted from version control) reproduces the stale-fact incident; the temporal
  server fixes it without losing history.
- Framework gates: plugin static suite and `validate.py` fully green.

## Trade-offs

History accumulates — nothing is deleted (negligible at personal/project scale;
archive superseded chains if a graph grows very large). Agents must follow
*supersede, don't edit*; the v1.5.0 rules and the Claude Code activation preamble
teach exactly that. See
[when (not) to use the temporal model](KG_IMPLEMENTATION_GUIDE.md#why-use-it--and-when-not-to).
