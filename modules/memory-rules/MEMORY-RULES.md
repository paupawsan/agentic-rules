# Memory Rules

## Overview

Memory rules enable agents to maintain persistent understanding through structured local storage. Agents save insights, decisions, and learned patterns in markdown format for transparency and accessibility.

## Framework Guidance

Memory is opt-in. It activates only when `memory_rules.enabled = true`. When disabled, skip all memory operations and respect the user's choice — never auto-enable.

When memory is enabled **and** a memory operation is requested, follow these rules consistently:

- **Format**: write markdown (.md) files, not JSON. Markdown keeps memory transparent and human-readable.
- **Persistence**: write to the filesystem, not only session context. Session-only "memory" is lost on the next reset.
- **Location**: follow the directory structure `[storage.base_path]/projects/[project-id]/[category]/`.
- **Templates**: use the standardized markdown templates in this specification.
- **Confirmation**: after writing, verify the file exists and report its exact path.

These rules are firm *once memory is active*; activation itself stays the user's decision.

### Implementation Guard

Check `memory_rules.enabled` before every memory operation:

```javascript
if (!getMemorySettings().enabled) {
  return null; // exit immediately — never auto-enable
}
```

## Core Algorithm

### Memory Initialization Process
1. **Settings Check**: Read memory-rules/settings.json and check if memory_rules.enabled is true
2. **Disabled Handling**: If memory rules are disabled:
   - Framework respects user's configuration choice
   - Can prompt user: "Memory rules are currently disabled. Would you like to enable memory functionality? (y/n)"
   - If user declines: Skip memory initialization gracefully
   - If user accepts: Enable memory_rules.enabled and continue with initialization
3. **Storage Path Validation**: Validate and normalize the storage.base_path setting
4. **Directory Scan**: Check for existing memory directories and structures
5. **Git Repository Check**: Detect if current project is a git repository
6. **Context Assessment**: Evaluate available project context and memory
7. **Git History Analysis**: If enabled and context is insufficient, analyze repository history
8. **Migration Detection**: Identify potential memory structures from other systems
9. **User Migration Prompt**: Ask user about migrating existing memories or creating new
10. **Migration Execution**: Apply migration logic with compatibility notes
11. **Git Memory Creation**: Generate git history memories if analysis was performed
12. **Index Building**: Create or update memory index for all loaded memories

### Automatic Interaction Recording Process
1. **Enabled Check**: Verify memory_rules.enabled and auto_recording.enabled are true
2. **Disabled Behavior**: If recording is disabled:
   - Framework respects user's configuration choice
   - Skip all memory operations gracefully
   - Can log disabled state for debugging
3. **Interaction Detection**: Monitor all user-agent interactions automatically
4. **Significance Assessment**: Evaluate interaction importance using configurable thresholds
5. **Context Capture**: Record full interaction context, metadata, and timing
6. **Framework Neutrality**: Always exclude framework licensing and branding from captured content
7. **Categorization**: Classify interaction type (question, instruction, feedback, etc.)
8. **Immediate Storage**: Save interaction to appropriate memory category
9. **Index Update**: Update search indexes for immediate retrieval

### Memory Storage Process
1. **Enabled Verification**: Check memory_rules.enabled and category.enabled before proceeding
2. **Disabled Handling**: If memory or category is disabled:
   - Framework respects user's configuration choice
   - Skip storage operation gracefully
3. **File Format Guidance**: Files work best as .md (markdown) format for transparency and accessibility
4. **Project Identification**: Determine current project context using project identification algorithm
5. **Categorization Phase**: Classify information by type (technical, behavioral, contextual, personal, session, topic)
6. **Memory Routing**: Apply memory routing algorithm - project memories go to [storage.base_path]/projects/[project-id]/[category]/
7. **Versioning Phase**: Read current memory rules version from settings.json
8. **Migration Notes**: Include cross-system compatibility information
9. **Framework Neutrality**: Always exclude framework licensing and branding from generated content
10. **Path Construction**: Build path following the pattern: [storage.base_path]/projects/[project-id]/[category]/[timestamp]_[category]_memory.md
11. **Directory Creation**: Create directory structure [storage.base_path]/projects/[project-id]/[category]/ as needed
12. **File Creation**: Create markdown (.md) files using standardized templates for consistency
13. **Structuring Phase**: Format using markdown template with version metadata and proper headers
14. **Persistence Phase**: Save to local filesystem and verify .md file creation
15. **Verification Phase**: Confirm .md file was created, is readable, and contains proper markdown content
16. **Confirmation Phase**: Report successful file creation with .md file paths
17. **Indexing Phase**: Update both global and project-specific memory indexes

### Expected Project Memory File Structure
When constructing project memory, create files in this exact structure:

```
[storage.base_path]/projects/[project-id]/
├── contextual/
│   └── [timestamp]_contextual_memory.md
├── technical/
│   └── [timestamp]_technical_memory.md
├── behavioral/
│   └── [timestamp]_behavioral_memory.md
├── personal/
│   └── [timestamp]_personal_memory.md
├── sessions/
│   └── [timestamp]_session_memory.md
├── topics/
│   └── [timestamp]_topic_memory.md
├── git_history/
│   └── [timestamp]_git_history_memory.md
└── knowledge_graph/
    ├── base/
    │   ├── [timestamp]_base_kg.md
    │   └── base_manifest.md
    ├── overlays/
    │   └── [branch-name]/
    │       ├── [timestamp]_overlay.md
    │       └── overlay_manifest.md
    └── cross_branch/
        └── [timestamp]_cross_branch.md
```

**RECOMMENDED**: Each .md file works best using standardized templates (Standard Memory Template, Session Memory Template, Topic Memory Template, etc.)

### Memory Retrieval Process
1. **Query Analysis**: Parse incoming requests for memory relevance
2. **Index Search**: Scan memory index for related entries
3. **Relevance Filtering**: Apply similarity algorithms to rank memories
4. **Context Integration**: Incorporate relevant memories into current reasoning
5. **Usage Logging**: Record memory usage for pattern analysis

### Knowledge Graph Tools (`kg` MCP Server)

When a `kg` MCP server is connected, structured knowledge (rules, patterns, facts, procedures, gotchas) lives in the graph alongside the markdown memory files, and the server's tools become the preferred path for the steps above:

- `kg_context("<task description>")` — load relevant rules/patterns/gotchas before a non-trivial task (richer than a raw index scan).
- `kg_query("<free text>")` / `kg_get_node(id)` — search the graph and expand a specific node.
- `kg_add(...)` / `kg_link(...)` — persist a durable insight and connect it to related nodes, so it surfaces in future `kg_context` calls.
- `kg_list(type/scope)` — browse stored knowledge by type or scope (global / project).

These tools are optional and follow the same consent boundary as file-based memory: persist durable, reusable knowledge — never secrets or transient session detail. If no `kg` server is present, use the markdown memory files and index described above. The full tool reference and algorithm mapping lives in `modules/rag-rules/RAG-RULES.md`.

## Version Tracking Algorithm

### Version Reading Process
1. **Load Settings**: Read memory-rules/settings.json on initialization
2. **Extract Version**: Parse "version" field from settings file
3. **Cache Version**: Store version in memory for use during storage operations
4. **Include in Metadata**: Add version to all generated memory entries

### Version Compatibility Check
1. **Memory Loading**: When reading existing memory entries
2. **Version Comparison**: Compare stored version with current version
3. **Compatibility Assessment**: Determine if memory format is compatible
4. **Migration Flag**: Mark for migration if version mismatch detected

### Project Identification Algorithm
1. **Context Analysis**: Examine current working environment
2. **Git Remote Check**: Extract project identifier from git remote URL
3. **Directory Name Fallback**: Use current directory name if git not available
4. **Environment Override**: Check for manual project ID override
5. **Validation**: Ensure project ID is valid and unique
6. **Registration**: Register project in global memory index

### Credential Naming Decision Algorithm
1. **Credential Assessment**: Analyze credential type and usage context
2. **Scope Evaluation**:
   - **General**: Credentials used across multiple projects or personally
   - **Project-Specific**: Credentials used only for specific project/service
3. **Security Consideration**: Evaluate security requirements and access patterns
4. **Naming Decision**: Always route to `[storage.base_path]/private/credentials/`
   - General credentials: `service-name-key.md` (e.g., `openai-api-key.md`)
   - Project-specific: `project-name-service-key.md` (e.g., `project-a-aws-key.md`)
5. **File Organization**: Create contextually named files within the private credentials directory

### Memory Routing Algorithm
1. **Category Assessment**: Determine memory category type
2. **Storage Location Check**: Look up storage_location setting for category
3. **Conditional Routing**: Apply credential naming logic for flexible categories
4. **Project Context**: Get current project identifier (if applicable)
5. **Path Construction**:
   - If `storage_location: "common"`: Route to `[storage.base_path]/common/[category]/`
   - If `storage_location: "private"`: Route to `[storage.base_path]/private/[category]/`
   - If `storage_location: "project"`: Route to `[storage.base_path]/projects/[project-id]/[category]/`
   - If credential category: Apply credential naming decision algorithm (always private)
6. **Path Validation**: Ensure target directory exists and is writable
7. **Index Update**: Update appropriate indexes (global, private, or project-specific)

### Storage Path Handling Algorithm
1. **Path Reading**: Extract storage.base_path from memory_rules settings
2. **Path Type Detection**:
   - Relative paths (./path, ../path): Resolve relative to project root
   - Absolute paths (/full/path): Use as-is
   - Tilde paths (~/path): Expand to user home directory
3. **Path Validation**: Check if path exists, is writable, and has sufficient space
4. **Path Creation**: Create directory structure if it doesn't exist
5. **Permission Check**: Verify read/write permissions on the storage location
6. **Fallback Logic**: If primary path fails, suggest alternative locations

### User-Guided Cleanup Algorithm
1. **Memory Age Assessment**: Scan memories and identify those exceeding suggested_retention_days
2. **Importance Evaluation**: Analyze memory content for potential importance/value
3. **Notification Generation**: Create user-friendly notifications about overdue memories
4. **Interactive Presentation**: Present cleanup suggestions with clear explanations
5. **User Consent Process**: Require explicit approval for any cleanup actions
6. **Selective Cleanup**: Allow users to choose which memories to clean up
7. **Preservation Priority**: Protect important/valuable memories from deletion
8. **Feedback Loop**: Learn from user cleanup decisions for future suggestions

### Memory Disabled Behavior Algorithm
1. **Memory Operation Request**: When any memory operation is requested
2. **Enabled Status Check**: Verify memory_rules.enabled is true
3. **Category Check**: Verify specific category.enabled is true
4. **Disabled Detection**: If either is disabled:
   - Framework respects user's configuration choice
   - Can log disabled state for debugging
   - Can prompt user: "Memory functionality is currently disabled. Would you like to enable it? (y/n)"
   - If user accepts: Enable memory functionality and proceed with operation
   - If user declines: Skip operation gracefully
5. **Advisory Message**: Provide brief explanation of memory benefits when prompting
6. **Operation Continuation**: Only proceed if explicitly enabled by user

### Git History Analysis Algorithm
1. **Repository Detection**: Confirm git repository presence and access
2. **Context Evaluation**: Check if existing memory provides sufficient project understanding
3. **Trigger Assessment**: Determine if git analysis should be performed based on settings and context
4. **History Scope Determination**: Apply time limits and commit count limits from settings
5. **Performance Check**: Validate analysis can complete within timeout limits
6. **Commit Analysis**:
   - Parse commit messages for insights and decisions
   - Analyze file change patterns and frequencies
   - Identify significant commits (features, fixes, refactors)
7. **Branch Evolution Tracking**:
   - Map branch creation and merging patterns
   - Track feature development lifecycles
   - Identify long-running vs short-lived branches
8. **Milestone Extraction**:
   - Detect version releases and tags
   - Identify major architectural changes
   - Track project growth indicators
9. **Pattern Recognition**:
   - Code evolution trends (complexity, size, structure)
   - Development velocity and consistency
   - Common file types and change frequencies
10. **Privacy Filtering**: Remove sensitive information based on privacy settings
11. **Memory Generation**: Create structured memories from analysis results
12. **Storage Routing**: Apply standard memory routing for git_history category
13. **KG Integration Trigger**:
    - IF `git_aware_kg.enabled` AND `knowledge_graph` category enabled:
      - Pass branch_evolution_data to `Git_Aware_KG_Construction` as hint
      - Pre-compute overlays for active branches discovered during analysis
      - This allows the KG system to build branch-aware overlays proactively

### Migration Detection Algorithm
1. **Directory Discovery**: Scan project directory for memory-related folders
2. **Structure Analysis**: Identify memory structures from different systems:
   - Agentic Rules Framework (current system)
   - Other agent frameworks (Cursor, Copilot, etc.)
   - Custom memory systems
   - Legacy formats
3. **Compatibility Mapping**: Determine migration paths and data compatibility
4. **User Interaction**: Present migration options with clear explanations

### Migration Prompting Algorithm
1. **Option Presentation**: Show user detected memory structures with descriptions
2. **Migration Options**:
   - Import and convert compatible memories
   - Create new memory system alongside existing
   - Selective import with filtering
   - Skip migration and use new system
3. **Migration Preview**: Show what will be imported and any data transformations
4. **User Confirmation**: Require explicit approval before migration begins

### Cross-System Migration Algorithm
1. **Source Analysis**: Understand source system's memory format and structure
2. **Data Mapping**: Map source fields to Agentic Rules Framework categories
3. **Transformation Rules**: Apply conversion logic with compatibility notes
4. **Migration Metadata**: Add migration notes explaining transformations
5. **Validation**: Verify migrated data integrity and completeness
6. **Integration**: Merge migrated memories into active memory system

## Settings Configuration

**Key Settings** (from `memory-rules/settings.json`):

- `"memory_rules.enabled"`: Master switch. When `false`, memory functionality remains disabled
- `"storage.base_path"`: Base directory (supports relative/absolute/tilde paths)
- `"cleanup_guidance_days"`: Advisory period for cleanup notifications (no auto-deletion)
- `"project_support.enabled"`: Enable project-based organization
- `"auto_recording.enabled"`: When `false`, recording operations are skipped
- Category `"enabled"` flags: Settings are respected for user control
- Category `"suggested_retention_days"`: Advisory guideline (no automatic cleanup)

**Storage Locations**:
- `"common"`: `[storage.base_path]/common/[category]/` (shared across projects)
- `"private"`: `[storage.base_path]/private/[category]/` (personal/sensitive)
- `"project"`: `[storage.base_path]/projects/[project-id]/[category]/` (project-specific)

**Cleanup Policy - User Consent Required**:
- **NO automatic deletion** - Never delete memories automatically
- **Advisory retention periods** - `suggested_retention_days` are guidelines only
- **User-guided cleanup** - Interactive process requiring explicit consent
- **Agent notifications** - Remind users about memories exceeding retention guidelines

**Supersession over edit** *(aligns file memory with the time-aware KG model)*:
When stored knowledge changes — a decision is reversed, a fact becomes outdated, a
convention is replaced — do not rewrite or delete the old memory entry. Write the new
entry, and note in it what it replaces (and, when a `kg` server is connected, record the
replacement with `kg_add(..., supersedes=<old-id>)`). The old entry remains as history:
it explains *why* past decisions were made with the knowledge available at the time.

## Memory Categories

### Technical Memory
- Code patterns and solutions
- Tool usage patterns
- Error resolution strategies
- Performance optimization insights

### Behavioral Memory
- User interaction patterns
- Communication preferences
- Task completion strategies
- Decision-making approaches

### Contextual Memory
- Project-specific knowledge
- Domain expertise
- Environmental constraints
- Historical outcomes

### User Interaction Memory
- User prompts and queries (full text)
- Agent responses and reasoning
- Conversation threads and context
- User preferences and patterns
- Feedback and corrections provided
- Clarification requests and responses

### Session Memory
- Session start/end timestamps
- Topics discussed in session
- Key decisions made
- Unresolved questions or tasks
- Session goals and outcomes
- Transition context between sessions

### Topic Memory
- Ongoing discussion topics
- Topic evolution over time
- Related concepts and connections
- User expertise level per topic
- Topic-specific preferences
- Cross-topic relationships

### Git History Memory
- Project development timeline and milestones
- Code evolution patterns and architecture changes
- Commit message insights and development decisions
- Branch strategy and feature development history
- Bug fixes and improvement tracking
- Project growth and complexity evolution

## Storage Format

### Standard Memory Template
```markdown
# Memory Entry: [CATEGORY] - [TIMESTAMP]

## Metadata
- **Version**: [MEMORY_RULES_VERSION]
- **Generated**: [GENERATION_TIMESTAMP]
- **Category**: [CATEGORY_TYPE]
- **Migration Notes**: [CROSS_SYSTEM_COMPATIBILITY_INFO]

## Context
[Brief description of situation/decision point]

## Understanding
[Detailed agent reasoning and insights]

## Decision/Action
[What was decided or done]

## Outcome
[Results and learnings]

## Migration Information
- **Source System**: [ORIGINAL_SYSTEM_OR_FRAMEWORK]
- **Migration Date**: [WHEN_DATA_WAS_MIGRATED]
- **Compatibility**: [INTEROPERABILITY_NOTES]
- **Transformations Applied**: [ANY_DATA_CONVERSIONS]

## Related Memories
[Links to related memory entries]

## Tags
[tag1, tag2, tag3]
```

#### Filled Example (Standard Memory Template)

A populated `technical` memory, written to `~/.memory/projects/acme-api/technical/2026-06-16T1430_technical_memory.md`:

```markdown
# Memory Entry: technical - 2026-06-16T14:30:00Z

## Metadata
- **Version**: 1.5.3
- **Generated**: 2026-06-16T14:30:00Z
- **Category**: technical
- **Migration Notes**: none

## Context
The acme-api test suite hung intermittently in CI but passed locally.

## Understanding
The hang traced to an async DB connection acquired in a test fixture that
was never released when an assertion failed mid-test, exhausting the pool
on the next test. Local runs passed because the local pool was larger.

## Decision/Action
Wrapped the fixture acquisition in try/finally and released the connection
in the finally block. Lowered the CI pool size to surface the bug earlier.

## Outcome
Suite is green across 50 consecutive CI runs. Pattern: any test fixture
that acquires a pooled resource must release it in finally, not after the
assertions.

## Related Memories
[[2026-05-02T0900_technical_memory]] — earlier connection-pool tuning

## Tags
[testing, async, connection-pool, ci, flaky-tests]
```

Note what makes this useful later: the **Understanding** explains *why*, the
**Outcome** states a reusable rule, and **Tags** make it retrievable by
`kg_query`/index search. Empty or placeholder sections defeat the purpose —
fill every section or omit the entry.

### Git History Memory Template
```markdown
# Git History Analysis: [PROJECT_ID] - [ANALYSIS_TYPE] - [DATE]

## Metadata
- **Version**: [MEMORY_RULES_VERSION]
- **Generated**: [GENERATION_TIMESTAMP]
- **Analysis Type**: [ANALYSIS_TYPE]
- **Time Range**: [START_DATE] to [END_DATE]
- **Migration Notes**: [CROSS_SYSTEM_COMPATIBILITY_INFO]

## Analysis Summary
[Brief overview of what this git history analysis reveals about the project]

## Key Findings
- **Project Evolution**: [How the project has grown/changed over time]
- **Development Patterns**: [Common commit patterns, branch usage, etc.]
- **Milestones**: [Major releases, significant changes, achievements]
- **Architecture Insights**: [How the codebase structure has evolved]

## Commit Analysis
### Major Commits
- **[Commit Hash/Date]**: [Commit message and significance]
- **[Commit Hash/Date]**: [Commit message and significance]

### Pattern Insights
- **Most Changed Files**: [Files that change frequently and why]
- **Common Commit Types**: [Feature additions, bug fixes, refactoring, etc.]
- **Author Patterns**: [If enabled, development collaboration insights]

## Branch Evolution
- **Main Branches**: [Primary development branches and their purposes]
- **Feature Branches**: [How features are developed and merged]
- **Release Strategy**: [How releases and versioning work]

## Code Evolution Metrics
- **File Count Growth**: [How the project size has changed]
- **Complexity Trends**: [Increasing/decreasing code complexity]
- **Technology Stack**: [Languages, frameworks, tools used over time]

## Development Insights
- **Project Velocity**: [Commit frequency and development speed]
- **Quality Indicators**: [Bug fix ratios, refactoring frequency]
- **Collaboration Patterns**: [Team size, contribution distribution]

## Recommendations
- **Areas for Attention**: [Based on git history patterns]
- **Best Practices**: [Development practices that work well for this project]
- **Future Considerations**: [Insights for upcoming development]

## Migration Information
- **Source System**: git_history_analysis
- **Analysis Method**: [METHOD_USED_FOR_ANALYSIS]
- **Data Preservation**: [WHAT_HISTORICAL_DATA_WAS_CAPTURED]
- **Privacy Applied**: [WHAT_FILTERS_WERE_APPLIED]
```

*Framework Requirement: Generated memory content must always exclude framework licensing and branding to maintain neutrality.*

### Base KG Manifest Template
```markdown
# Base KG Manifest: [PROJECT_ID] - [TIMESTAMP]

## Metadata
- **Version**: [MEMORY_RULES_VERSION]
- **Base Commit**: [COMMIT_HASH]
- **Default Branch**: [BRANCH_NAME]
- **Generated**: [TIMESTAMP]
- **Node Count**: [N]
- **Edge Count**: [M]

## Node Registry
| Node ID | Type | Source File | Content Hash |
|---------|------|-------------|--------------|
| [id]    | [type] | [file_path] | [sha256_short] |

## Edge Registry
| Edge Key | Source Node | Target Node | Type | Content Hash |
|----------|------------|-------------|------|--------------|
| [key]    | [source_id] | [target_id] | [rel_type] | [sha256_short] |
```

### Branch Overlay Template
```markdown
# KG Branch Overlay: [BRANCH_NAME] - [TIMESTAMP]

## Metadata
- **Version**: [MEMORY_RULES_VERSION]
- **Branch**: [BRANCH_NAME]
- **Merge Base Commit**: [COMMIT_HASH]
- **Base Graph Timestamp**: [BASE_TIMESTAMP]
- **Generated**: [TIMESTAMP]
- **Files Changed**: [N]
- **Status**: [VALID|STALE]

## File Diff Summary
| File | Change Type |
|------|-------------|
| [path] | added/modified/deleted |

## Added Nodes
| Node ID | Type | Source File | Attributes |
|---------|------|-------------|------------|

## Removed Nodes
| Node ID | Reason |
|---------|--------|

## Modified Nodes
| Node ID | Field Changed | Old Value Summary | New Value Summary |
|---------|--------------|-------------------|-------------------|

## Added Edges
| Source | Target | Type | Confidence |
|--------|--------|------|-----------|

## Removed Edges
| Source | Target | Type | Reason |
|--------|--------|------|--------|

## Modified Edges
| Source | Target | Type | Change |
|--------|--------|------|--------|

## Tags
[overlay, branch-name, git-aware-kg]
```

### Cross-Branch Analysis Template
```markdown
# Cross-Branch KG Analysis: [PROJECT_ID] - [TIMESTAMP]

## Metadata
- **Version**: [MEMORY_RULES_VERSION]
- **Branches Analyzed**: [N]
- **Generated**: [TIMESTAMP]

## Branch Summary
| Branch | Delta Size | Added | Removed | Modified | Status |
|--------|-----------|-------|---------|----------|--------|

## Potential Merge Conflicts
| Entity | Branches | Conflict Type | Risk Score |
|--------|----------|--------------|------------|

## Semantic Conflicts
| Entity | Type | Branch A Change | Branch B Change | Assessment |
|--------|------|----------------|-----------------|------------|

## Merge Order Recommendation
1. [branch] - [reason]

## Tags
[cross-branch, conflict-analysis, merge-planning]
```

### User Interaction Memory Template
```markdown
# User Interaction: [SESSION_ID] - [TIMESTAMP]

## Metadata
- **Version**: [MEMORY_RULES_VERSION]
- **Generated**: [GENERATION_TIMESTAMP]
- **Interaction ID**: [UNIQUE_ID]
- **Migration Notes**: [CROSS_SYSTEM_COMPATIBILITY_INFO]

## User Prompt
```
[Full user prompt text]
```

## Agent Response
```
[Full agent response text]
```

## Context
- Session: [session_id]
- Topic: [current_topic]
- Previous Context: [summary of conversation leading up]

## Analysis
- User Intent: [interpreted intent]
- Response Effectiveness: [rating/explanation]
- Key Learnings: [insights about user preferences]

## Technical Metadata
- Response Time: [duration]
- Tools Used: [list of tools]
- Success Metrics: [completion rate, user satisfaction]

## Migration Information
- **Source System**: [ORIGINAL_SYSTEM_OR_FRAMEWORK]
- **Migration Date**: [WHEN_DATA_WAS_MIGRATED]
- **Data Preservation**: [WHAT_DATA_WAS_KEPT_OR_TRANSFORMED]
- **Interoperability**: [HOW_THIS_INTERACTION_WORKS_ACROSS_SYSTEMS]

## Related Interactions
- Previous: [link to prior interaction]
- Follow-up: [link to subsequent interaction]
```

### Session Memory Template
```markdown
# Session Memory: [SESSION_ID] - [START_TIME] to [END_TIME]

## Metadata
- **Version**: [MEMORY_RULES_VERSION]
- **Generated**: [GENERATION_TIMESTAMP]
- **Session Type**: [INTERACTIVE/COLLABORATIVE/INFORMATIONAL]

## Session Overview
- Duration: [total time]
- Primary Topic: [main discussion topic]
- Secondary Topics: [other topics covered]
- Session Goal: [stated or inferred purpose]

## Key Interactions
- Opening Prompt: [first user message]
- Closing Exchange: [final interaction]
- Critical Decisions: [important choices made]
- Unresolved Items: [questions/tasks left open]

## Topic Evolution
- Topic Flow: [how topics transitioned]
- Depth Reached: [technical/complexity level]
- User Engagement: [participation level]

## Outcomes
- Goals Achieved: [completed objectives]
- New Understandings: [learnings gained]
- Follow-up Needed: [next steps identified]

## Session Quality Metrics
- Clarity of Communication: [rating]
- Problem Resolution: [effectiveness]
- User Satisfaction: [inferred satisfaction]
```

### Topic Memory Template
```markdown
# Topic Memory: [TOPIC_NAME] - [LAST_UPDATED]

## Metadata
- **Version**: [MEMORY_RULES_VERSION]
- **Generated**: [GENERATION_TIMESTAMP]
- **Topic ID**: [UNIQUE_TOPIC_ID]
- **Last Evolution**: [LAST_UPDATE_TIMESTAMP]

## Topic Definition
- Description: [clear definition of topic]
- Scope: [boundaries of what this topic covers]
- Related Topics: [connected concepts/areas]

## Evolution History
- First Discussed: [initial date/session]
- Development Stages: [how understanding evolved]
- Current Understanding Level: [depth of knowledge]

## User Interaction Patterns
- Common Questions: [frequent queries]
- Preferred Approaches: [user's preferred solutions]
- Expertise Level: [user's familiarity]
- Communication Style: [formal/informal, detailed/brief]

## Key Insights
- Important Concepts: [core learnings]
- Best Practices: [successful approaches]
- Pitfalls to Avoid: [common mistakes]
- Resources Referenced: [helpful materials]

## Cross-References
- Related Sessions: [session links]
- Connected Topics: [other topic memories]
- Project Context: [broader project ties]
```

## Directory Structure

### Dynamic Path Resolution
The directory structure adapts to the `storage.base_path` setting in memory-rules/settings.json:
- **Relative paths**: `./memory/` → resolved relative to project root
- **Absolute paths**: `/full/path/to/memory/` → used as-is
- **Tilde paths**: `~/Documents/memory/` → expanded to user home

### Memory Organization: Common, Private, and Project-Specific

**Common Memory** (`[storage.base_path]/common/`): Shared across ALL projects
- **Purpose**: Reusable knowledge that benefits multiple projects
- **Categories**: `technical/`, `behavioral/`
- **Examples**: Code patterns, algorithms, interaction patterns

**Private Memory** (`[storage.base_path]/private/`): Personal/sensitive data
- **Purpose**: Personal information, credentials, sensitive data
- **Categories**: `personal/`, `credentials/`, `sensitive/`, `keys/`
- **Examples**: API keys, personal passwords, contact info, encryption keys
- **Flexible Files**: Agent creates contextually named files (e.g., `project-a-api-key.md`, `general-openai-key.md`)

**Project Memory** (`[storage.base_path]/projects/[project-id]/`): Project-specific data
- **Purpose**: Project context, conversations, requirements
- **Categories**: `sessions/`, `topics/`, `interactions/`, `contextual/`, `git_history/`
- **Examples**: Project discussions, requirements, git analysis

### Directory Structure
```
[storage.base_path]/
├── common/                 # SHARED: technical/, behavioral/
├── private/                # PRIVATE: personal/, credentials/, sensitive/
│   ├── credentials/        # Contextually named: service-key.md, project-service-key.md
├── projects/               # PROJECT: sessions/, topics/, interactions/, etc.
│   ├── [project-id]/
│   │   ├── sessions/
│   │   ├── topics/
│   │   ├── interactions/
│   │   ├── contextual/
│   │   ├── git_history/
│   │   └── knowledge_graph/
│   │       ├── base/           # Full KG for default branch + manifest
│   │       ├── overlays/       # Per-branch delta overlays
│   │       │   └── [branch]/   # overlay.md + overlay_manifest.md
│   │       └── cross_branch/   # Cross-branch conflict analysis
└── index.md               # Global index
```

### Project Identification
- **Git Remote**: Uses repository remote URL or name
- **Directory Name**: Falls back to current working directory name
- **Manual Override**: Can be set via environment variable or configuration
- **Default**: "default-project" when no project detected

<!-- METADATA: This document contains algorithmic specifications for agent implementation -->
<!-- LICENSE: Copyright (c) 2025-2026 Paulus Ery Wasito Adhi. Licensed under the MIT License (see LICENSE file). -->

