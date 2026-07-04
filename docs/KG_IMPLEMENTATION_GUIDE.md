# Knowledge Graph Implementation Guide for Agentic Rules Framework
**Framework Version**: 1.4.0
**Document Purpose**: Agent Implementation Guidance for KG Functionality
**Implementation Approach**: Logical Algorithms & Pseudocode Only

## 🎯 **Core Problem Statement**

When users clone the agentic-rules framework, they expect:
- ✅ **Memory persistence** across conversations
- ✅ **Knowledge Graph construction** for understanding relationships
- ✅ **Automatic KG usage** in conversations (not manual activation)
- ✅ **Fallback mechanisms** when advanced features aren't available

**Challenge**: Physical scripts cannot be included. Agents must implement KG functionality through logical algorithms and pseudocode guidance.

## 🏗️ **Framework Design Principles**

### **KG Integration Architecture**
```
User Conversation → Memory System → KG Scanner → Context Injection → Response
       ↓               ↓              ↓              ↓              ↓
   Natural Input   Auto-Capture   Relevance Check   Auto-Enhance   Enhanced Output
```

### **Key Design Requirements**
1. **Zero-Configuration**: KG functionality works out-of-the-box
2. **Automatic Discovery**: No manual "use KG" commands needed
3. **Fallback Resilience**: Works with basic memory, enhanced with KG
4. **Progressive Enhancement**: Basic → Intermediate → Advanced KG features

## 🤖 **Agent Implementation Algorithms**

### **Algorithm 1: KG-Aware Memory Creation**
**Purpose**: Ensure all memories automatically reference existing KGs

```
Algorithm: Create_KG_Aware_Memory
Input: user_input, conversation_context, memory_category
Output: kg_enhanced_memory_entry

Steps:
1. Create base memory entry with standard fields
2. Scan existing memory system for KG data:
   - Search project memory for "kg_data", "kg_analysis", "kg_relationships"
   - Check common memory for framework KG information
   - Look for KG-related files in memory directory structure

3. IF KG data found:
   - Extract relevant entities and relationships
   - Calculate relevance score based on:
     * Semantic similarity to current conversation
     * Temporal recency of KG data
     * Topic overlap with current context
   - Filter KG items above relevance threshold (default: 0.6)

4. Enhance memory entry:
   - Add "kg_references" field with top N relevant KG items
   - Include "kg_context" field with relationship insights
   - Add "kg_relationships" field for connected concepts

5. Store enhanced memory with KG cross-references
6. Return success confirmation

Fallback: If no KG data found, store standard memory entry
```

### **Algorithm 2: Conversation KG Context Injection**
**Purpose**: Automatically include relevant KG insights in new conversations

```
Algorithm: Inject_Conversation_KG_Context
Input: new_conversation_request, user_context, project_context
Output: kg_enhanced_conversation_context

Steps:
1. Analyze conversation request:
   - Extract key entities, topics, and intent
   - Identify project context and user goals
   - Determine knowledge domains relevant to request

2. Query memory system for KG data:
   - Search project memory for topic-relevant KGs
   - Check common memory for general framework KGs
   - Look for user-specific KG patterns

3. Calculate KG relevance:
   FOR each found KG item:
     relevance_score = calculate_relevance(
       conversation_entities,
       kg_entities,
       temporal_recency,
       topic_overlap
     )
   ENDFOR

4. Select top KG context items:
   - Sort by relevance score descending
   - Limit to max_context_items (default: 5)
   - Prioritize high-impact relationships

5. Format KG context for injection:
   - Convert KG relationships to natural language
   - Create contextual summaries of relevant connections
   - Generate insight statements about relationships

6. Inject KG context into conversation:
   - Prepend relevant KG insights to system context
   - Include relationship summaries in available context
   - Make KG data accessible for response generation

Fallback: If no KG data available, proceed with standard conversation context
```

### **Algorithm 3: Progressive KG Construction**
**Purpose**: Build KGs incrementally without requiring advanced scripting

```
Algorithm: Progressive_KG_Construction
Input: conversation_data, memory_entries, project_context
Output: incrementally_built_kg

Steps:
1. Start with basic entity extraction:
   - Identify nouns, proper names, technical terms
   - Extract key concepts from conversation
   - Build simple entity list

2. Establish basic relationships:
   - Connect entities mentioned together
   - Note temporal relationships (before/after)
   - Record interaction patterns

3. Enhance with memory integration:
   - Cross-reference with existing memory entries
   - Identify recurring entity combinations
   - Strengthen relationships through frequency

4. Store KG incrementally:
   - Save as structured markdown files
   - Use consistent naming: YYYYMMDD_entity_relationships.md
   - Include metadata for future retrieval

5. Progressive enhancement:
   - Start with entity co-occurrence
   - Add semantic relationships
   - Include contextual metadata
   - Build relationship strength scores

Fallback: Store conversation data as enhanced memory even if KG construction fails
```

### **Algorithm 4: KG Query Enhancement**
**Purpose**: Improve information retrieval using KG relationships

```
Algorithm: KG_Enhanced_Query_Processing
Input: user_query, available_context, memory_system
Output: kg_enhanced_response_context

Steps:
1. Process standard query:
   - Extract keywords and intent
   - Search memory system for relevant information
   - Gather traditional context

2. Enhance with KG relationships:
   IF KG data available:
     - Find entities mentioned in query
     - Traverse KG relationships to find connected concepts
     - Retrieve indirectly related information
     - Include relationship context

3. Rank results with KG insights:
   - Boost results connected to query entities
   - Include relationship explanations
   - Provide contextual understanding

4. Generate KG-enhanced response:
   - Include relationship insights in response
   - Explain connections between concepts
   - Provide broader context understanding

Fallback: Return standard query results if KG enhancement unavailable
```

## 🔧 **Fallback Implementation Strategy**

### **Tier 1: Basic Memory Integration**
```
When KG features unavailable:
- Store conversations as enhanced memory
- Include entity extraction and basic categorization
- Cross-reference with existing memory entries
- Provide basic relationship tracking
```

### **Tier 2: Intermediate KG Features**
```
When basic scripting available:
- Implement entity co-occurrence tracking
- Build simple relationship graphs
- Store KG data in structured format
- Enable basic KG queries
```

### **Tier 3: Advanced KG Features**
```
When full implementation possible:
- Complex relationship analysis
- Semantic understanding
- Graph algorithms and traversal
- Advanced query optimization
```

## 📁 **Memory Structure Design**

### **KG-Compatible Memory Organization**
```
memory/
├── common/                    # Shared across projects
│   ├── technical/            # Technical knowledge
│   ├── behavioral/           # Framework behavior patterns
│   └── kg_data/              # Common KG data
├── private/                  # User-specific data
│   ├── personal/             # User information
│   └── kg_patterns/          # Personal KG patterns
└── projects/
    └── [project_name]/
        ├── contextual/       # Project context
        ├── sessions/         # Conversation sessions
        ├── technical/        # Project-specific tech
        ├── topics/           # Topic-based organization
        │   ├── kg_data/      # Project KG data
        │   ├── kg_analysis/  # KG analysis results
        │   └── kg_relationships/  # Relationship data
        ├── user_interactions/ # User interaction memory
        ├── kg_index/         # Project KG index
        └── knowledge_graph/  # Git-aware KG (Phase 5)
            ├── base/         # Full KG for default branch + manifest
            ├── overlays/     # Per-branch delta overlays
            │   └── [branch]/ # overlay.md + overlay_manifest.md
            └── cross_branch/ # Cross-branch conflict analysis
```

### **KG Memory File Format**
```markdown
# KG Memory Entry: [topic] - [timestamp]

**Project**: [project_name]
**KG Type**: [entity_relationships|analysis|query_patterns]
**Category**: kg_data
**Storage**: project
**Retention**: 365 days

## KG Metadata
- **Entities**: [list of extracted entities]
- **Relationships**: [count of relationships]
- **Communities**: [number of communities detected]
- **Last Updated**: [timestamp]

## Key Insights
- [Relationship 1]: [description]
- [Relationship 2]: [description]

## Query Patterns
- [Pattern 1]: [usage example]
- [Pattern 2]: [usage example]

## Integration Notes
- Automatically referenced in conversations
- Cross-linked with memory entries
- Updated through conversation analysis
```

## 🔄 **Integration Workflow**

### **Conversation Processing Flow**
```
1. User Input → Entity Extraction → KG Relevance Check
2. Memory Scan → KG Data Retrieval → Context Enhancement
3. Response Generation → KG Insights Integration → Output
4. Memory Storage → KG Reference Addition → Learning Update
```

### **KG Evolution Flow**
```
Basic Memory → Entity Tracking → Relationship Building → KG Construction → Advanced Queries
     ↓             ↓                ↓                   ↓                 ↓
  Storage       Recognition     Analysis         Enhancement       Optimization
```

## 🎯 **Agent Implementation Checklist**

### **Phase 1: Basic KG Awareness**
- [ ] Implement Algorithm 1: KG-Aware Memory Creation
- [ ] Create KG-compatible memory structure
- [ ] Enable automatic KG reference scanning
- [ ] Test basic KG memory storage

### **Phase 2: Conversation Integration**
- [ ] Implement Algorithm 2: Conversation KG Context Injection
- [ ] Add KG relevance calculation
- [ ] Enable automatic context enhancement
- [ ] Test conversation KG injection

### **Phase 3: Progressive Enhancement**
- [ ] Implement Algorithm 3: Progressive KG Construction
- [ ] Add incremental KG building
- [ ] Enable relationship tracking
- [ ] Test KG evolution capabilities

### **Phase 4: Query Enhancement**
- [ ] Implement Algorithm 4: KG Query Enhancement
- [ ] Add relationship-based retrieval
- [ ] Enable contextual understanding
- [ ] Test enhanced query capabilities

### **Phase 5: Git-Aware KG**
- [ ] Implement Algorithm 5: Git_Aware_KG_Construction (entry point routing)
- [ ] Implement Algorithm 6: Diff_Based_Overlay_Construction (delta-only analysis)
- [ ] Implement Algorithm 7: Overlay_Merge_Resolution (base + overlay merge)
- [ ] Implement Algorithm 8: Base_Graph_Refresh (incremental base updates)
- [ ] Implement Algorithm 9: Cross_Branch_KG_Analysis (conflict detection)
- [ ] Add knowledge_graph/base/, overlays/, cross_branch/ directory structure
- [ ] Store base_manifest with content hashes for delta computation
- [ ] Test overlay creation on feature branches
- [ ] Test cross-branch semantic conflict detection
- [ ] Verify fallback to standard KG when git_aware disabled or project not git-managed

### **Algorithm 5: Git-Aware KG Construction**
**Purpose**: Route KG construction through git-aware overlay system when project is git-managed

```
Algorithm: Git_Aware_KG_Construction
Input: project_path, current_branch, memory_system, existing_base_graph
Output: effective_knowledge_graph (base + overlay)

Steps:
1. Detect git context:
   - Check if project is a git repository
   - IF NOT: Fallback to standard Incremental_Graph_Builder
   - Identify default branch and current branch
   - Get merge-base commit

2. Route based on context:
   - IF on default branch OR no base exists: Full base construction
   - IF on non-default branch AND base exists: Overlay construction

3. For base construction:
   - Execute full Incremental_Graph_Builder
   - Generate base_manifest with node/edge content hashes
   - Store in knowledge_graph/base/

4. For overlay construction:
   - Execute Diff_Based_Overlay_Construction
   - Only analyze files changed relative to merge-base
   - Store delta in knowledge_graph/overlays/[branch]/

5. Return effective graph:
   - Default branch: Return base directly
   - Feature branch: Merge base + overlay via Overlay_Merge_Resolution

Fallback: Standard Incremental_Graph_Builder when git not available
```

### **Algorithm 6: Cross-Branch KG Analysis**
**Purpose**: Detect merge conflicts and semantic divergence across branch overlays

```
Algorithm: Cross_Branch_KG_Analysis
Input: base_graph, branch_overlays[], analysis_scope
Output: cross_branch_analysis_report

Steps:
1. Collect active overlays from knowledge_graph/overlays/
2. Build entity_modification_map: entity_id -> [modifying branches]
3. Classify collisions:
   - CONVERGENT: Same change across branches (low risk)
   - DIVERGENT: Different changes to same entity (high risk)
4. For DIVERGENT entities:
   - Analyze relationship changes
   - Detect interface modifications
   - Assign semantic_conflict_score (0.0-1.0)
5. Generate report with merge-order recommendations

Fallback: Skip analysis when fewer than 2 overlays exist
```

## 🔒 **Safety & Compatibility**

### **Graceful Degradation**
- Always provide basic functionality without KG features
- KG enhancements should be additive, not required
- Clear fallback paths for all KG operations
- User experience unaffected by KG implementation status

### **Memory Compatibility**
- KG-enhanced memories work with basic memory system
- Standard memories remain readable in KG-enhanced system
- Migration paths for upgrading memory systems
- Backward compatibility maintained

### **Performance Considerations**
- KG operations should not block conversation flow
- Background processing for heavy KG construction
- Caching for frequently accessed KG data
- Resource limits for KG operations

## 📚 **Implementation Resources**

### **Required Agent Capabilities**
1. **Memory System Access**: Read/write memory entries
2. **File System Operations**: Create/manage memory files
3. **Text Processing**: Entity extraction, relationship identification
4. **Context Management**: Relevance scoring, context injection

### **Recommended Patterns**
- Implement algorithms incrementally
- Test each phase before proceeding
- Maintain comprehensive logging
- Provide user feedback on KG status

### **Success Metrics**
- Memories automatically reference KGs
- Conversations include relevant KG context
- KG data evolves through usage
- Fallback mechanisms work reliably

---

## ⏳ **Time-Aware (Bi-Temporal) Knowledge Model** *(v1.5.0)*

Knowledge changes. A deploy target moves, a convention is replaced, a decision is
reversed. A KG that only *adds* facts eventually ranks stale knowledge above its
replacement — the highest-priority answer can be the wrong one. The temporal model
fixes this at the data layer: **knowledge is never deleted; it is superseded.**

### The model

Every node carries two independent time dimensions:

| Field | Dimension | Meaning |
|-------|-----------|---------|
| `created_at` | transaction time | when the record entered the KG |
| `expired_at` | transaction time | when the record was retired as *erroneous bookkeeping* (`NULL` = live) |
| `valid_at` | event time | when the fact became true in the world (defaults to `created_at`) |
| `invalid_at` | event time | when the fact stopped being true — set automatically on supersession (`NULL` = still true) |

Rules of the model:

- **Supersede, don't edit.** When knowledge changes, add the new node with a
  `supersedes` edge to the old one. The old node is invalidated automatically and
  drops out of default retrieval — but its content is untouched.
- **Default view = current.** Queries return only knowledge that is valid *now*.
  Superseded, retired, and not-yet-valid nodes are filtered out; a `supersedes`
  edge renders as an annotated pointer (`-> supersedes: old-id [invalidated <date>]`)
  instead of re-injecting hidden content.
- **Time travel.** `as_of=<ISO date>` reconstructs what was true at that moment —
  useful for auditing *why* a past decision was made with the knowledge available
  then. `include_expired=true` shows everything, with `[SUPERSEDED by …]` /
  `[expired]` markers.
- **Retirement without replacement.** When a fact simply stops being true
  (nothing replaces it), retire it as `invalid`; when a record was wrong from the
  start, retire it as `expired` (hidden from historical views after that instant).
  Both are reversible (`restore`) — nothing is ever destroyed.
- **Recency as a tie-breaker.** Ranking may add a *gentle* exponential decay on
  last-update time (default half-life 90 days), bounded so it re-orders near-ties
  and never outweighs relevance.

### Why use it — and when not to

**Benefits:**
- **Stale knowledge stops winning.** The motivating failure: a high-priority
  outdated fact kept outranking its replacement until someone hand-edited its text
  and priority. With supersession, the current fact surfaces and the old one becomes
  an annotated pointer — no manual demotion, no rewriting history.
- **Auditability.** "What did we believe on June 10th?" has a queryable answer.
  Past decisions can be judged against the knowledge of their time.
- **Safe contradictions.** Two conflicting facts can coexist (a `contradicts`
  edge records the conflict) until one side wins by supersession — no premature
  deletion of possibly-correct knowledge.
- **Reversibility.** A mistaken retirement is one `restore` away; a deleted node
  is gone forever.

**Costs / when to skip it:**
- **Write-path discipline.** Agents must learn "supersede, don't edit" — the rules
  in this framework teach it, but ad-hoc scripts writing to the store can bypass it.
- **Growth.** History accumulates (nothing is deleted). For personal/project-scale
  KGs (hundreds to tens of thousands of nodes) this is negligible; at larger scale,
  archive old superseded chains instead of deleting.
- **Not needed for append-only domains.** If your knowledge never changes
  (e.g. a static reference corpus), temporal filtering adds fields you'll never set —
  the defaults (`valid_at = created_at`, everything current) then behave exactly like
  a non-temporal KG, so it costs little, but it also buys nothing.

### Origins & credits

This is an **adaptation, not an invention of this project**. Bi-temporal modeling
(separating *valid time* from *transaction time*) is long-standing temporal-database
practice (see e.g. SQL:2011 temporal tables). Applying it to an AI agent's memory
KG — supersession edges, non-lossy invalidation, point-in-time retrieval — was
popularized by **Zep's Graphiti** engine, which inspired this design. The framework
adapts the *concept only*: no Graphiti code, schema, or text is reused, which is why
no third-party license accompanies it. A related but different research direction is
embedding-based temporal-KG *reasoning/forecasting* (e.g. RE-GCN,
[arXiv:2104.10353](https://arxiv.org/abs/2104.10353)), which predicts future facts
from KG snapshots; this framework deliberately stays at the storage/retrieval layer —
curated knowledge in, deterministic time-aware retrieval out.

### Database-backed implementation (instead of markdown)

The markdown KG (Tiers above) is the zero-infrastructure default. When the graph
grows past what grep-and-read handles comfortably — or when more than one project or
agent needs the same knowledge — move the store to a database. SQLite is enough; no
server process is required to start.

**Schema** (SQLite; the temporal fields are the three nullable columns):

```sql
CREATE TABLE nodes (
    id TEXT PRIMARY KEY,
    type TEXT NOT NULL CHECK(type IN ('rule','pattern','fact','procedure','gotcha')),
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    scope TEXT NOT NULL DEFAULT 'global',
    tags TEXT DEFAULT '',
    priority INTEGER DEFAULT 5 CHECK(priority BETWEEN 1 AND 10),
    source TEXT DEFAULT '',
    created_at TEXT DEFAULT (datetime('now')),
    updated_at TEXT DEFAULT (datetime('now')),
    valid_at TEXT,      -- event time: fact became true (NULL -> treat as created_at)
    invalid_at TEXT,    -- event time: fact stopped being true (set on supersession)
    expired_at TEXT     -- transaction time: record retired as erroneous
);

CREATE TABLE edges (
    source_id TEXT NOT NULL REFERENCES nodes(id) ON DELETE CASCADE,
    target_id TEXT NOT NULL REFERENCES nodes(id) ON DELETE CASCADE,
    relation TEXT NOT NULL CHECK(relation IN
        ('applies_to','depends_on','part_of','related_to','supersedes','contradicts')),
    weight REAL DEFAULT 0.5,
    PRIMARY KEY (source_id, target_id, relation)
);

CREATE INDEX idx_nodes_invalid ON nodes(invalid_at);
CREATE INDEX idx_nodes_expired ON nodes(expired_at);
-- Optional retrieval upgrades: an FTS5 table over (title, content, tags) for BM25,
-- and a vector table (e.g. sqlite-vec) for semantic search.
```

**Visibility predicate** (the heart of the temporal behavior):

```
current view (default):   expired_at IS NULL AND invalid_at IS NULL
                           AND (valid_at IS NULL OR valid_at <= now)
as-of view (as_of = T):   (expired_at IS NULL OR expired_at > T)
                           AND (valid_at IS NULL OR valid_at <= T)
                           AND (invalid_at IS NULL OR invalid_at > T)
```

Apply it as a post-filter on candidates in application code, not as ad-hoc SQL string
comparison — mixed timestamp formats (`datetime('now')` vs ISO-8601 with offset) break
lexicographic ordering. Normalize all writes through one timestamp helper.

**Write-path semantics:**
- `add(..., valid_from=…, valid_until=…)` — call-time parameter names that set the
  stored `valid_at` / `invalid_at` event-time fields (one documented convention:
  `*_from`/`*_until` on the write API, `*_at` in storage); retroactive facts allowed.
- `add(..., supersedes=old_id)` — in one transaction: insert the new node, insert the
  `supersedes` edge, and set `old.invalid_at = new.valid_at` *only if it is NULL*
  (never overwrite existing history).
- A `supersedes` edge created on its own invalidates its target the same way;
  a `contradicts` edge invalidates nothing (record the conflict, resolve later).
- `retire(id, mode)` — set `invalid_at` (fact ended) or `expired_at` (record was
  wrong); `restore` clears both.

**Migrating an existing non-temporal database in place:** use pure
`ALTER TABLE nodes ADD COLUMN …` (never drop/recreate the table — a rebuild
reassigns SQLite rowids and silently desyncs any FTS/vector tables joined by rowid),
then backfill once: `UPDATE nodes SET valid_at = created_at WHERE valid_at IS NULL`.
Make the migration idempotent (check `PRAGMA table_info` first) and back up the
database file before the first run.

### Upgrading the KG to an MCP server — recommended path

The natural maturity ladder is: **markdown files → SQLite database → MCP server**
in front of that database. Converting to MCP is a genuinely good option once either
of these is true: (a) more than one project, machine, or agent needs the same
knowledge, or (b) you want retrieval quality (BM25/semantic/reranking) better than
grep. Reasons it pays off:

- **One brain, many sessions.** Every project and every agent session talks to the
  same store through the same tool set (`kg_context`, `kg_query`, `kg_add`,
  `kg_link`, `kg_retire`, `kg_get_node`, `kg_list`) — no per-project copies drifting
  apart.
- **The rules already speak MCP.** This framework's rule files instruct agents to
  prefer `kg` MCP tools when connected and to fall back to the markdown store when
  not — converting requires **zero rule changes**, just configuring the endpoint
  (`kg_mcp_url` in the Claude Code plugin).
- **Retrieval upgrades stay server-side.** Hybrid BM25+vector search, reranking,
  temporal filtering, recency decay — all improve behind the tool interface without
  touching any agent-facing text.
- **Schema-validated writes.** Tool parameters (types, valid relations, priority
  bounds) are enforced at the boundary instead of hoped-for in file edits.

When *not* to convert: a single project with a small KG and no appetite for running
a process — the markdown store is versioned with the repo, diffable in code review,
and needs nothing installed. That simplicity is worth keeping until sharing or
retrieval quality actually hurts.

---

**Implementation Note**: This guide provides logical algorithms and pseudocode for KG implementation. Agents should adapt these patterns to their specific capabilities and environment constraints. The goal is to ensure KG functionality works seamlessly for end users regardless of the underlying agent implementation approach.
