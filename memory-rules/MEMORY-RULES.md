# Memory Rules

## Overview

Memory rules enable agents to maintain persistent understanding through structured local storage. Agents save insights, decisions, and learned patterns in markdown format for transparency and accessibility.

## Critical Requirements

**MANDATORY**: Agents MUST respect user settings. When `"enabled": false`:
- **NEVER** auto-enable memory functionality
- **NEVER** modify user settings without explicit consent
- **ALWAYS** prompt user for consent OR skip operations gracefully
- **SECURITY VIOLATION**: Auto-enabling is forbidden and constitutes a breach

**MANDATORY**: When memory construction is requested and memory is enabled, agents MUST:
- **ALWAYS** create actual local files in the configured storage location
- **NEVER** store memory only in session context - persist to filesystem
- **ALWAYS** follow the Memory Storage Process algorithm exactly
- **ALWAYS** verify file creation and provide confirmation

### Implementation Guards

**REQUIRED**: Every memory operation must check `memory_rules.enabled` first.

**Pattern**:
```javascript
if (!getMemorySettings().enabled) {
  return null; // Exit immediately - NEVER auto-enable
}
```

**FORBIDDEN**: Auto-enabling, bypassing checks, or modifying user settings without consent.

## Core Algorithm

### Memory Initialization Process
1. **Settings Check**: Read memory-rules/settings.json and check if memory_rules.enabled is true
2. **Disabled Handling**: If memory rules are disabled:
   - **CRITICAL**: Do NOT auto-enable - respect user's configuration choice
   - **REQUIRED**: Prompt user: "Memory rules are currently disabled. Enable memory functionality? (y/n)"
   - If user declines: **MUST** skip memory initialization and return null
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
   - **CRITICAL**: Do NOT auto-enable - respect user's configuration choice
   - **MUST** skip all memory operations silently without prompting
   - Log disabled state for debugging only
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
   - **CRITICAL**: Do NOT auto-enable - respect user's configuration choice
   - **MUST** skip storage operation without prompting
3. **Observation Phase**: Agent identifies significant understanding or decision points
4. **Project Identification**: Determine current project context using project identification algorithm
5. **Categorization Phase**: Classify information by type (technical, behavioral, contextual)
6. **Memory Routing**: Apply memory routing algorithm to determine storage location (common vs private)
7. **Versioning Phase**: Read current memory rules version from settings.json
8. **Migration Notes**: Include cross-system compatibility information
9. **Framework Neutrality**: Always exclude framework licensing and branding from generated content
10. **Path Construction**: Build full file path based on routing decision
11. **Directory Creation**: **MANDATORY** - Create all necessary directories if they don't exist
12. **File Creation**: **MANDATORY** - Create actual markdown files with content
13. **Structuring Phase**: Format understanding in standardized markdown template with version metadata
14. **Persistence Phase**: **MANDATORY** - Save to local filesystem and verify file exists
15. **Verification Phase**: **MANDATORY** - Confirm file was created and is readable
16. **Confirmation Phase**: **MANDATORY** - Report successful file creation with path
17. **Indexing Phase**: Update both global and project-specific memory indexes

### Memory Retrieval Process
1. **Query Analysis**: Parse incoming requests for memory relevance
2. **Index Search**: Scan memory index for related entries
3. **Relevance Filtering**: Apply similarity algorithms to rank memories
4. **Context Integration**: Incorporate relevant memories into current reasoning
5. **Usage Logging**: Record memory usage for pattern analysis

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
   - **CRITICAL**: Do NOT auto-enable - respect user's configuration choice
   - Log disabled state for debugging
   - **REQUIRED**: Prompt user: "Memory functionality is currently disabled. Would you like to enable it? (y/n)"
   - If user accepts: Enable memory functionality and proceed with operation
   - If user declines: **MUST** skip operation and return gracefully without enabling
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

- `"memory_rules.enabled"`: **CRITICAL** - Master switch. When `false`, agent MUST NOT auto-enable
- `"storage.base_path"`: Base directory (supports relative/absolute/tilde paths)
- `"cleanup_guidance_days"`: Advisory period for cleanup notifications (no auto-deletion)
- `"project_support.enabled"`: Enable project-based organization
- `"auto_recording.enabled"`: **CRITICAL** - When `false`, agent MUST skip recording silently
- Category `"enabled"` flags: **CRITICAL** - Must be respected, never auto-enable
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
├── common/                 # 📂 SHARED: technical/, behavioral/
├── private/                # 🔐 PRIVATE: personal/, credentials/, sensitive/
│   ├── credentials/        # Contextually named: service-key.md, project-service-key.md
├── projects/               # 📁 PROJECT: sessions/, topics/, interactions/, etc.
│   ├── [project-id]/
│   │   ├── sessions/
│   │   ├── topics/
│   │   ├── interactions/
│   │   ├── contextual/
│   │   └── git_history/
└── index.md               # Global index
```

### Project Identification
- **Git Remote**: Uses repository remote URL or name
- **Directory Name**: Falls back to current working directory name
- **Manual Override**: Can be set via environment variable or configuration
- **Default**: "default-project" when no project detected

<!-- METADATA: This document contains algorithmic specifications for agent implementation -->
<!-- LICENSE: Copyright (c) 2025 Paulus Ery Wasito Adhi. Licensed under the MIT License (see LICENSE file). -->

