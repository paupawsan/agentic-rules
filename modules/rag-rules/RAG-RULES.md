# RAG Rules

## Overview

Retrieval-Augmented Generation rules form the foundation of intelligent information processing, optimizing context management across the entire agentic system. These rules enhance memory operations, influence design decisions, and provide pattern-driven insights for all agent activities.

## Critical Requirements for Agents

**MANDATORY COMPLIANCE**: Agents implementing RAG rules MUST adhere to these critical requirements. Non-compliance results in immediate rule violation.

### Automatic Trigger Conditions
**IMMEDIATE EXECUTION REQUIRED**: These algorithms MUST execute automatically when triggered:

#### Directory Investigation Trigger
- **WHEN**: Agent investigates any directory or performs file discovery
- **MUST EXECUTE**: `Detect_Hidden_Files_Algorithm` + `Select_File_Discovery_Tool`
- **MANDATORY**: Cannot proceed with file operations until hidden file detection completes
- **VIOLATION**: Using directory listing without hidden file detection

#### File Search Trigger
- **WHEN**: Agent searches for configuration files, settings, or initialization markers
- **MUST EXECUTE**: `Select_Content_Search_Tool` with hidden file inclusion
- **MANDATORY**: Search ALL files including hidden ones (.env, .gitignore, .settings)
- **VIOLATION**: Excluding hidden files from search operations

#### System Status Check Trigger
- **WHEN**: Agent checks system initialization or configuration status
- **MUST EXECUTE**: Comprehensive scan including ALL dot-files
- **MANDATORY**: Check for .agentic_initialized and other hidden markers
- **VIOLATION**: Incomplete system assessment due to missed hidden files

### File Discovery Requirements
- **HIDDEN FILE DETECTION**: Agents MUST detect and process hidden files (dot-files like .env, .gitignore, .settings)
- **COMPREHENSIVE SCANNING**: Use appropriate tools to find ALL files, not just visible ones
- **TOOL SELECTION**: Execute Select_File_Discovery_Tool algorithm before any file operations
- **SAFETY VALIDATION**: Execute Validate_Tool_Usage_Safety for all file operations

**VIOLATION CONSEQUENCE**: Agents that fail to detect hidden files or use inappropriate tools will provide incomplete information processing and violate RAG rule compliance.

### Algorithm Execution Requirements
- **MANDATORY EXECUTION**: All defined algorithms MUST be executed when their conditions are met
- **NO EXCEPTIONS**: Agents cannot skip algorithm execution based on "assumptions"
- **COMPLETE IMPLEMENTATION**: All algorithm steps MUST be followed
- **PROPER TOOL USAGE**: Use tools as specified in tool selection algorithms
- **AUTOMATIC ENFORCEMENT**: Trigger conditions MUST activate algorithms without manual intervention

## System-Wide Impact

### Memory Integration
RAG rules directly enhance memory operations by:
- **Prioritizing information** during memory construction based on relevance scoring
- **Optimizing retrieval** through context-aware filtering and ranking
- **Guiding pattern recognition** with intelligent content analysis
- **Enhancing storage efficiency** by focusing on high-value information

### Design Construction Influence
RAG algorithms affect design decisions by:
- **Analyzing similar patterns** across projects and documentation
- **Providing context relevance** scoring for architectural choices
- **Optimizing information flow** between system components
- **Reducing token consumption** through selective context loading

### Framework Integration
RAG rules influence all agent operations by:
- **Optimizing context windows** across all interactions
- **Enhancing information retrieval** for any task type
- **Providing pattern analysis** for decision-making
- **Reducing processing overhead** through intelligent filtering

### Memory Integration
Knowledge Graph algorithms integrate with memory rules for persistence:
- **Graph Persistence**: When memory_rules.enabled = true, constructed knowledge graphs are stored in persistent memory system
- **Memory Categories**: Knowledge graphs stored in appropriate memory categories (knowledge_graph or technical)
- **Retention Policies**: Long-term retention for valuable knowledge relationships
- **Coordination**: Memory cleanup processes respect knowledge graph dependencies
- **Fallback**: When memory disabled, graphs maintained in session context only

## Core Algorithms

### File Discovery Requirements
**MANDATORY**: Agents implementing RAG rules MUST use the following file discovery protocols:

1. **Hidden File Detection**: Always scan for hidden files (dot-files, system files)
2. **Comprehensive Directory Scanning**: Use platform-aware directory traversal
3. **Tool Selection**: Apply Select_File_Discovery_Tool algorithm for optimal method
4. **Safety Validation**: Validate all file operations using Validate_Tool_Usage_Safety

**VIOLATION**: Agents that fail to detect hidden configuration files or use inappropriate file discovery tools.

### Context Window Optimization Algorithm
1. **Information Assessment**: Analyze total available information volume
2. **Relevance Filtering**: Identify information critical to current task
3. **Priority Ranking**: Order information by importance and recency
4. **Selective Loading**: Load only highest-priority information within limits
5. **Progressive Expansion**: Expand context as understanding develops

### Hierarchical Reading Algorithm
1. **Structure Detection**: Identify document or content organization
   - Section headers and hierarchies
   - Code structure and modules
   - Data organization patterns
2. **Top-Down Navigation**: Start with highest-level overviews
3. **Selective Drilling**: Choose relevant subsections based on task
4. **Recursive Processing**: Apply algorithm to subsections as needed
5. **Cross-Reference Linking**: Maintain awareness of related sections

### Log Analysis Algorithm
1. **Initial Sampling**: Read first 10-50 lines to understand format and context
2. **Pattern Recognition**: Identify log structure, timestamps, severity levels
3. **Strategic Reading**:
   - Error-focused: Prioritize error and warning messages
   - Time-focused: Sample across time periods
   - Pattern-focused: Look for recurring issues or sequences
4. **Progressive Deepening**: Read more context around identified patterns
5. **Summary Synthesis**: Create condensed understanding for further processing

## Reading Strategies

### Document Reading Strategy
```
Algorithm: Hierarchical_Document_Reading
Input: document_path, task_context, max_context_window

1. Read document structure (TOC, headers, sections)
2. Match task_context against section titles/descriptions
3. Select top N most relevant sections
4. For each selected section:
   a. Read section header and summary
   b. Assess relevance to task
   c. Read full content if highly relevant
   d. Mark for later reading if moderately relevant
5. Recursively apply to subsections if needed
6. Maintain reading log for context management
```

### Code Reading Strategy
```
Algorithm: Selective_Code_Reading
Input: codebase_path, functionality_required, language_context

1. Identify entry points and main modules
2. Trace execution paths for required functionality
3. Read function signatures and documentation first
4. Follow dependency chains selectively
5. Expand reading based on understanding gaps
6. Cross-reference with related files when needed
```

### Log Reading Strategy
```
Algorithm: Intelligent_Log_Analysis
Input: log_path, issue_description, analysis_type

1. Sample initial segment (first 50 lines)
2. Identify log format and key fields
3. Search for error patterns and timestamps
4. If temporal analysis: Sample across time windows
5. If pattern analysis: Focus on recurring messages
6. If specific issue: Search for related keywords
7. Expand context around identified areas
8. Generate summary with key insights
```

## Context Management

### Information Chunking Algorithm
1. **Semantic Segmentation**: Break information into meaningful units
2. **Importance Scoring**: Assign relevance scores to each chunk
3. **Dependency Mapping**: Identify relationships between chunks
4. **Selective Retention**: Keep most relevant chunks within limits
5. **Progressive Loading**: Load additional chunks as needed

### Memory Buffer Management
1. **Working Memory Allocation**: Reserve space for active processing
2. **Long-term Reference Storage**: Maintain pointers to external information
3. **Context Switching**: Efficiently swap information sets
4. **Compression Techniques**: Summarize less critical information
5. **Cache Management**: Maintain frequently accessed information

## Tool Selection and Usage Algorithms

**MANDATORY REQUIREMENT**: Agents implementing RAG rules MUST use these algorithms for all file operations. Failure to use appropriate tools results in incomplete information processing.

### File Discovery Tool Selection Algorithm
**MANDATORY TRIGGER**: Agents MUST execute this algorithm BEFORE ANY file operations, directory investigation, or system status checks.
**PROHIBITED TOOLS**: Standard `list_dir` or basic file listing tools are INSUFFICIENT and violate compliance.
**AUTOMATIC EXECUTION**: This algorithm MUST run automatically when file discovery is needed.

```
Algorithm: Select_File_Discovery_Tool
Input: search_target, search_context, file_types_needed
Output: recommended_tool_chain

MANDATORY ANALYSIS - Agents MUST evaluate ALL conditions:

1. Analyze search_target characteristics - TRIGGER CONDITIONS:
   - If ANY file operation: Execute this algorithm (MANDATORY)
   - If hidden_files_needed OR starts_with_dot: Use comprehensive_directory_scan (MANDATORY)
   - If checking system status: Execute hidden file detection (MANDATORY)
   - If searching configuration: Include ALL dot-files (.env, .settings, etc.)
   - If specific_extensions: Use filtered_glob_patterns
   - If recursive_search: Use recursive_directory_traversal
   - If metadata_only: Use filesystem_metadata_scanner

2. Determine search scope - MUST verify:
   - project_root: Use relative_path_resolution
   - system_wide: Use absolute_path_resolution with permissions_check
   - network_shares: Use network_mount_detection

3. Select primary tool based on target - REQUIRED tool selection:
   - Standard files: Use available directory listing tool with pattern matching
   - Hidden files: Use comprehensive directory scanning tool capable of detecting dot-files (MANDATORY for dot-files)
   - Large directories: Use recursive directory traversal with iterator support
   - Network paths: Use path existence checking with permission validation

4. Apply safety filters - MUST exclude:
   - System directories (/proc, /sys, /dev on Unix)
   - Unauthorized directories based on permissions
   - Respect .gitignore patterns when applicable
   - Limit recursion depth to prevent infinite loops

5. Return tool_chain with fallback options - MUST provide:
   - Primary: comprehensive_recursive_directory_scanner (for hidden file detection)
   - Fallback: pattern_matching_directory_scanner
   - Emergency: manual_path_construction

VIOLATION: Agents using inappropriate tools or failing to detect required file types.
```

### Content Search Tool Selection Algorithm
```
Algorithm: Select_Content_Search_Tool
Input: content_query, file_set, search_constraints
Output: optimal_search_strategy

1. Analyze content_query characteristics:
   - If exact_match: Use string.find() or regex exact match
   - If pattern_match: Use re.search() with compiled patterns
   - If fuzzy_match: Use difflib or specialized fuzzy libraries
   - If semantic_search: Use embedding-based similarity

2. Evaluate file_set properties:
   - If small_files (< 1MB): Use memory-mapped search
   - If large_files (> 100MB): Use streaming line-by-line search
   - If binary_files: Use specialized binary search tools
   - If encoded_files: Apply appropriate decoding before search

3. Select search algorithm:
   - Text files: Use grep-like line-by-line scanning
   - Structured files: Use format-specific parsers (JSON, XML, CSV)
   - Code files: Use AST parsing for semantic understanding
   - Binary files: Use hex pattern matching with context

4. Optimize for performance:
   - Pre-compile regex patterns for reuse
   - Use memory mapping for large files
   - Implement parallel processing for multiple files
   - Cache frequently accessed file metadata

5. Return search_tool with configuration:
   - Tool: streaming_grep_with_context
   - Configuration: {buffer_size: 8192, context_lines: 3}
   - Fallback: memory_mapped_search
```

### Hidden File Detection Algorithm
**MANDATORY**: Agents MUST execute this algorithm for ALL directory scans to ensure complete file discovery.

```
Algorithm: Detect_Hidden_Files_Algorithm
Input: directory_path, include_system_files, recursion_depth
Output: comprehensive_file_list

**AUTOMATIC TRIGGER**: This algorithm MUST execute for ANY directory investigation, file search, or system status check.
**MANDATORY EXECUTION**: Cannot proceed with file operations until this algorithm completes successfully.
**VIOLATION**: Using any file listing tool without executing this algorithm first.

MANDATORY STEPS - Agents MUST follow ALL of these:

1. Initialize file discovery parameters:
   - base_path = resolve_absolute_path(directory_path)
   - max_depth = min(recursion_depth, 10)  # Safety limit
   - include_hidden = True  # ALWAYS include hidden files - NEVER set to False
   - exclude_patterns = ['.git', '__pycache__', 'node_modules']
   - scan_mode = 'comprehensive'  # Always use comprehensive scanning

2. Use comprehensive directory scanning:
   - Tool: Available directory scanning function capable of detecting hidden files
   - Capability: Must include files starting with '.' (dot-files) - REQUIRED
   - Filter: Apply permission checks and safety exclusions

3. Apply hidden file detection rules - MUST check ALL:
   - Dot-prefix files: .* (Unix/Linux hidden files)
   - System attributes: Check platform-specific hidden flags
   - Configuration files: .env, .gitignore, .eslintrc, .settings, etc.
   - Temporary files: .tmp, .cache, .log variants

4. Process special file types:
   - Symbolic links: Resolve and check target if accessible
   - Special files: Skip device files, sockets, named pipes
   - Large files: Use stat() for size checking before processing
   - Binary files: Flag for specialized processing

5. Return categorized file list - MUST include:
   - visible_files: Regular user-visible files
   - hidden_files: Configuration and system files (MANDATORY)
   - special_files: Links, devices (with warnings)
   - inaccessible_files: Permission denied files (logged)

VIOLATION: Agents that skip hidden files or use incomplete scanning methods.
```

### Safe Tool Usage Conditions
```
Algorithm: Validate_Tool_Usage_Safety
Input: tool_name, target_path, operation_type
Output: safety_clearance_boolean

1. Check path safety:
   - Is path within allowed directories?
   - Does path contain suspicious patterns (.. , symbolic links)?
   - Is path accessible with current permissions?

2. Validate operation type:
   - read_operations: Generally safe if path is accessible
   - write_operations: Require explicit user consent
   - execute_operations: Highly restricted, require validation
   - network_operations: Check firewall and security settings

3. Apply platform-specific restrictions:
   - Windows: Avoid system directories (C:\\Windows, C:\\System32)
   - Unix/Linux: Avoid /proc, /sys, /dev directories
   - macOS: Respect application sandbox restrictions

4. Check resource limits:
   - File size limits for reading operations
   - Time limits for long-running operations
   - Memory limits for large file processing

5. Log operation for audit trail:
   - Record tool used, path accessed, operation result
   - Flag suspicious activities for review
   - Maintain usage statistics for optimization

6. Return safety clearance with confidence level
```

## Specific Tool Implementations

### File System Tools
```
Available Tools:
1. Directory Scanner (available directory scanning tools)
   - Purpose: Complete directory traversal with metadata
   - Use When: Need comprehensive file listing, hidden files, permissions
   - Safety: Apply path validation and recursion limits

2. Pattern Matcher (available pattern matching tools)
   - Purpose: Pattern-based file discovery
   - Use When: Searching for specific file types or naming patterns
   - Safety: Validate patterns prevent directory traversal attacks

3. Find Command Integration (subprocess with find)
   - Purpose: Advanced file searching with complex criteria
   - Use When: Need size, date, or content-based filtering
   - Safety: Sanitize command arguments, limit execution time

4. Metadata Reader (available file metadata tools)
   - Purpose: File metadata without content reading
   - Use When: Checking file properties, sizes, permissions
   - Safety: Safe for all accessible files
```

### Search and Analysis Tools
```
Available Tools:
1. Regex Pattern Search (re module)
   - Purpose: Complex pattern matching in text
   - Use When: Structured text search, validation patterns
   - Safety: Pre-compile patterns, limit input size

2. Fuzzy Text Matching (difflib, fuzzywuzzy)
   - Purpose: Approximate string matching
   - Use When: Handling typos, variations in search terms
   - Safety: Set similarity thresholds to prevent false matches

3. JSON/XML Parsers (json, xml.etree)
   - Purpose: Structured data extraction
   - Use When: Processing configuration files, data formats
   - Safety: Validate input format before parsing

4. Code Analysis Tools (ast, tokenize)
   - Purpose: Semantic code understanding
   - Use When: Analyzing source code structure and dependencies
   - Safety: Handle syntax errors gracefully
```

## Multi-language Support

### Language Detection Algorithm
1. **Extension Analysis**: Identify language from file extensions
2. **Syntax Sampling**: Read initial content to confirm language
3. **Parser Selection**: Choose appropriate parsing strategy
4. **Encoding Handling**: Manage character encoding variations
5. **Fallback Strategies**: Handle mixed-language or unknown formats

### Cross-Language Reading Patterns
- **Documentation First**: Prioritize language-agnostic documentation
- **Interface Focus**: Read API definitions and contracts
- **Example-Based**: Use code examples for understanding
- **Translation Layer**: Apply consistent terminology across languages

## Performance Optimization

### Lazy Loading Algorithm
1. **Metadata First**: Load file/directory information without content
2. **Demand-Driven**: Read content only when needed
3. **Caching Strategy**: Maintain recently accessed information
4. **Prefetching**: Anticipate likely future needs
5. **Cleanup**: Remove unused information from memory

### Parallel Processing
1. **Independent Tasks**: Process unrelated information simultaneously
2. **Batch Operations**: Group similar operations for efficiency
3. **Result Aggregation**: Combine parallel results intelligently
4. **Error Handling**: Manage failures in parallel operations

## Knowledge Graph Algorithms

### Entity Extraction Algorithm
```
Algorithm: Structured_Entity_Extraction
Input: text_content, domain_context
Output: List of extracted entities with types

1. Tokenize input text into sentences and words
2. Apply part-of-speech tagging to identify noun phrases
3. Use named entity recognition patterns:
   - Person: Capitalized words following titles (Dr., Mr., Ms.)
   - Organization: Capitalized sequences with corporate indicators
   - Location: Geographic names and location indicators
   - Concept: Domain-specific terminology from context
4. Apply rule-based filtering:
   - Remove common stop words and pronouns
   - Validate against known entity dictionaries
   - Cross-reference with domain context
5. Assign confidence scores based on pattern matching
6. Return entities sorted by confidence and frequency
```

### Relationship Discovery Algorithm
```
Algorithm: Pattern_Based_Relation_Extraction
Input: entity_list, sentence_context
Output: List of entity relationships

1. Identify sentence structures containing multiple entities
2. Apply syntactic pattern matching:
   - Subject-verb-object triples
   - Prepositional relationships (X works at Y, X located in Y)
   - Possessive relationships (X's Y, Y of X)
3. Use lexical pattern recognition:
   - Verb-based relations (X develops Y, X uses Y)
   - Noun compound analysis (machine learning model)
   - Adjective relationships (X is Y, Y-based X)
4. Apply domain-specific relation templates:
   - Technical: "X implements Y", "X inherits from Y"
   - Organizational: "X reports to Y", "X belongs to Y"
   - Temporal: "X created Y", "Y updated by X"
5. Validate relationships against consistency rules
6. Return relationships with confidence scores
```

### Knowledge Graph Construction Algorithm
```
Algorithm: Incremental_Graph_Builder
Input: entities, relationships, existing_graph, memory_system_enabled
Output: Updated knowledge graph

1. Initialize graph with existing nodes and edges
2. Process new entities:
   - Add as nodes with type and attribute metadata
   - Merge duplicate entities based on similarity scoring
3. Process new relationships:
   - Add as directed or undirected edges between nodes
   - Include relationship type and confidence metadata
4. Apply graph consistency checks:
   - Remove contradictory relationships
   - Merge redundant connections
   - Update node centrality measures
5. Perform graph optimization:
   - Remove isolated nodes below threshold
   - Simplify redundant paths
   - Update graph indices for efficient querying
6. Persist graph state with timestamp metadata:
   - If memory_rules.enabled = true:
     - Store graph data in persistent memory system
     - Use appropriate memory category (knowledge_graph or technical)
     - Include metadata for graph reconstruction
     - Set retention policy for long-term knowledge preservation
   - If memory_rules.enabled = false:
     - Store graph in session-only context
     - Graph will be lost when context is summarized/reset
```

### Graph Query Algorithm
```
Algorithm: Semantic_Graph_Query
Input: query_text, knowledge_graph
Output: Ranked list of relevant information

1. Parse query for entities and intent
2. Identify relevant nodes through direct matching
3. Expand search using graph traversal:
   - Find connected nodes within 2-3 degrees
   - Apply relationship type filtering
   - Use centrality scoring for importance ranking
4. Apply semantic similarity matching:
   - Compare query concepts with node attributes
   - Use synonym expansion from domain vocabulary
   - Calculate concept relevance scores
5. Rank results using multi-factor scoring:
   - Direct match confidence
   - Graph centrality weight
   - Semantic similarity score
   - Recency and frequency factors
6. Return top-ranked results with explanation metadata
```

### Graph Maintenance Algorithm
```
Algorithm: Adaptive_Graph_Maintenance
Input: knowledge_graph, usage_patterns, time_window, memory_system_enabled
Output: Optimized knowledge graph

1. Analyze usage patterns over time window:
   - Track query frequency for nodes and edges
   - Monitor relationship strength changes
   - Identify emerging vs. decaying connections
2. Apply aging and pruning rules:
   - Reduce confidence scores for unused elements
   - Remove edges below minimum threshold
   - Consolidate similar but unused nodes
3. Perform graph restructuring:
   - Merge highly similar nodes
   - Simplify redundant relationship paths
   - Update node clustering for better organization
4. Optimize for query performance:
   - Rebuild indices based on access patterns
   - Pre-compute frequently accessed subgraphs
   - Update caching strategies
5. Persist optimized graph state:
   - If memory_rules.enabled = true:
     - Update stored graph data in persistent memory
     - Respect memory retention policies for knowledge preservation
     - Maintain graph evolution history for debugging
     - Coordinate with memory cleanup processes
   - If memory_rules.enabled = false:
     - Maintain graph in session context only
     - Graph optimizations lost when context resets
6. Generate maintenance report with statistics
```

## Quality Assurance

### Reading Completeness Check
1. **Coverage Analysis**: Verify all relevant information accessed
2. **Understanding Validation**: Test comprehension through application
3. **Gap Identification**: Detect missing critical information
4. **Re-reading Triggers**: Initiate additional reading when needed

### Accuracy Verification
1. **Cross-Reference Checking**: Validate information against multiple sources
2. **Consistency Analysis**: Check for internal contradictions
3. **Update Verification**: Ensure information currency
4. **Source Credibility**: Assess information reliability

<!-- METADATA: This document contains algorithmic specifications for agent implementation -->
<!-- LICENSE: Copyright (c) 2025 Paulus Ery Wasito Adhi. Licensed under the MIT License (see LICENSE file). -->

