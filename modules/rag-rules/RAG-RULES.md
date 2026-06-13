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

#### Framework Self-Preservation Trigger
- **WHEN**: Agent experiences context summarization, reset, or framework identity loss
- **MUST EXECUTE**: Core principles rediscovery through memory system keywords
- **MANDATORY**: Reference foundational behavioral patterns and permanent retention markers
- **VIOLATION**: Loss of framework identity and behavioral consistency

### Framework Identity Preservation
**MANDATORY SURVIVAL**: RAG rules include self-preservation mechanisms for framework continuity.

#### Core Principles Reference Keywords
- **FOUNDATIONAL PRINCIPLES**: Search for permanent behavioral memory patterns
- **FRAMEWORK MISSION**: Locate mission-critical identity and purpose markers
- **CORE PHILOSOPHY**: Find non-intrusive enhancement and user consent principles
- **IDENTITY PRESERVATION**: Access framework corruption warnings and recovery procedures

#### Memory System Recovery Triggers
- **COMMON BEHAVIORAL MEMORY**: Access shared foundational knowledge across projects
- **PERMANENT RETENTION POLICIES**: Locate maximum-priority framework preservation data
- **CONTEXT SURVIVAL MARKERS**: Find context summarization immunity indicators
- **FRAMEWORK INTEGRITY AUDIT**: Execute identity verification and corruption checks

### File Discovery Requirements
- **HIDDEN FILE DETECTION**: Agents MUST detect and process hidden files (dot-files like .env, .gitignore, .settings)
- **COMPREHENSIVE SCANNING**: Use appropriate tools to find ALL files, not just visible ones
- **TOOL SELECTION**: Execute Select_File_Discovery_Tool algorithm before any file operations
- **SAFETY VALIDATION**: Execute Validate_Tool_Usage_Safety for all file operations

**VIOLATION CONSEQUENCE**: Agents that fail to detect hidden files or use inappropriate tools will provide incomplete information processing and violate RAG rule compliance.

#### Hidden File Detection Implementation Guide
**MANDATORY REFERENCE**: When checking framework initialization status (.agentic_initialized), agents MUST use cross-platform hidden file detection tools.

##### Problematic Default Behaviors (REQUIRES CORRECT PARAMETERS):
```python
# ❌ PROBLEMATIC - Default behavior misses hidden files
import os
files = os.listdir('.')  # Default behavior excludes hidden files

# ❌ PROBLEMATIC - Default glob excludes hidden files
import glob
files = glob.glob('./*')  # Default behavior excludes hidden files

# ✅ CORRECT - Use include_hidden parameter
import glob
files = glob.glob('./*', include_hidden=True)

# ✅ CORRECT - Use iterdir() which includes all files
from pathlib import Path
path = Path('.')
files = list(path.iterdir())  # Includes hidden files

# ✅ CORRECT - Filter for hidden files explicitly
import os
all_files = os.listdir('.')
hidden_files = [f for f in all_files if f.startswith('.')]
```

##### Platform-Specific Commands for .agentic_initialized Detection:
```bash
# Windows - PowerShell
Get-ChildItem -Path "." -Force -File | Where-Object {$_.Name -eq '.agentic_initialized'}

# Unix/Linux/macOS - find command
find . -maxdepth 1 -name '.agentic_initialized' -type f 2>/dev/null
```

##### Cross-Platform Python Implementation:
```python
import platform
from pathlib import Path

def check_framework_initialization():
    system = platform.system().lower()
    marker_path = Path('.agentic_initialized')

    # Method 1: Direct pathlib check (works on all platforms)
    if marker_path.exists():
        return True

    # Method 2: Platform-specific detection for comprehensive checking
    if system == 'windows':
        # Use Windows-specific hidden file detection
        try:
            import win32api, win32con
            if marker_path.exists():
                attrs = win32api.GetFileAttributes(str(marker_path))
                return bool(attrs & win32con.FILE_ATTRIBUTE_HIDDEN) or marker_path.exists()
        except ImportError:
            return marker_path.exists()  # Fallback
    else:
        # Unix-like systems
        return marker_path.exists()

    # Method 3: Directory iteration approach (alternative)
    # Check if .agentic_initialized exists in directory listing
    try:
        agentic_rules_dir = Path('.')
        return any(f.name == '.agentic_initialized' for f in agentic_rules_dir.iterdir())
    except (OSError, PermissionError):
        return False
```

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

## Framework Continuity & Self-Preservation

### Post-Summarization Recovery Mechanisms
**MANDATORY RECOVERY**: RAG rules include semantic triggers for framework rediscovery after context summarization.

#### Identity Reconstruction Keywords
- **AGENTIC ENHANCEMENT**: Locate AI agent behavior improvement frameworks
- **MODULAR RULE SYSTEMS**: Find independent rule modules with shared infrastructure
- **USER CONSENT MODEL**: Access explicit activation requirement patterns
- **TRANSPARENT OPERATION**: Discover clear framework operation indicators

#### Memory System Navigation Markers
- **EIGHT CATEGORY STORAGE**: Access technical, behavioral, contextual, user_interactions, sessions, topics, git_history, personal
- **PERMANENT RETENTION POLICIES**: Find maximum-priority preservation data
- **CROSS-SESSION CONTINUITY**: Locate knowledge retention across context changes
- **FRAMEWORK MISSION MARKERS**: Access mission-critical identity preservation data

#### Self-Diagnostic Triggers
- **FRAMEWORK CORRUPTION WARNINGS**: Execute identity verification checks
- **RECOVERY PROCEDURES**: Access clean reinitialization protocols
- **INTEGRITY AUDIT TRAILS**: Find framework health monitoring patterns
- **USER TRUST MAINTENANCE**: Locate user empowerment and control principles

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

**📖 PLATFORM REFERENCE**: See `docs/CROSS_PLATFORM_HIDDEN_FILE_DETECTION.md` for specific command implementations.

```
Algorithm: Select_File_Discovery_Tool (Enhanced with Platform Commands)
Input: search_target, search_context, file_types_needed, platform
Output: specific_command_with_fallbacks

MANDATORY ANALYSIS - Agents MUST evaluate ALL conditions:

1. Detect Platform and Analyze Requirements:
   - platform = detect_current_platform()  # windows/linux/darwin/unknown
   - If hidden_files_needed OR starts_with_dot: Execute Detect_Hidden_Files_Algorithm (MANDATORY)
   - If system_status_check: Include .agentic_initialized, .bootstrap.json (MANDATORY)
   - If configuration_search: Include .env, .gitignore, .settings, .config (MANDATORY)

2. Determine search scope - MUST verify:
   - project_root: Use relative_path_resolution
   - system_wide: Use absolute_path_resolution with permissions_check
   - network_shares: Use network_mount_detection

3. Execute Platform-Specific Commands - MANDATORY IMPLEMENTATION:

   FOR Windows Systems:
   - Hidden files: PowerShell "Get-ChildItem -Path $directory -Force -File -Recurse"
   - Fallback: CMD "dir /a:h /b /s $directory"
   - Large dirs: Use iterator-based scanning to prevent memory issues

   FOR Unix/Linux/macOS Systems:
   - Hidden files: find $directory -name ".*" -type f 2>/dev/null
   - Fallback: ls -la $directory | grep "^\."
   - Large dirs: find with -maxdepth limits and progress indicators

   FOR Unknown Platforms:
   - Universal: Python pathlib.Path.glob('**/.*') with error handling
   - Fallback: os.scandir() with manual hidden file detection

4. Apply safety filters - MUST exclude:
   - System directories (/proc, /sys, /dev on Unix; System32, Windows on Windows)
   - Unauthorized directories based on permissions
   - Respect .gitignore patterns when applicable
   - Limit recursion depth to prevent infinite loops (max 10 levels)

5. Return command_chain with fallbacks - MUST provide:
   - Primary: Platform-native command for hidden file detection
   - Fallback: Cross-platform Python implementation
   - Emergency: Manual path construction with basic os.listdir()

VIOLATION: Agents using inappropriate tools or failing to detect required file types.
```

#### **Critical Implementation Notes:**

**MANDATORY COMMAND USAGE**:
- **Windows**: Use `Get-ChildItem -Force` or `dir /a:h` - NOT basic `dir`
- **Unix/macOS**: Use `find -name ".*"` or `ls -la` - NOT basic `ls`
- **Cross-platform**: Use Python pathlib with proper hidden detection logic

**HIDDEN FILE DETECTION VALIDATION**:
- ✅ Must find files starting with `.` (dot-files)
- ✅ Must detect Windows hidden attributes
- ✅ Must include .env, .gitignore, .settings, .agentic_initialized
- ✅ Must handle permission errors gracefully

**PROHIBITED PRACTICES**:
- ❌ Using `os.listdir()` without hidden file logic
- ❌ Using `glob.glob()` without `**/.*` patterns
- ❌ Assuming all platforms work like Unix (dot-files only)
- ❌ Skipping platform detection and using generic commands

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

**📖 CROSS-PLATFORM REFERENCE**: See `docs/CROSS_PLATFORM_HIDDEN_FILE_DETECTION.md` for specific commands and implementations.

```
Algorithm: Detect_Hidden_Files_Algorithm (Enhanced with Platform-Specific Commands)
Input: directory_path, include_system_files, recursion_depth, platform
Output: comprehensive_file_list

**AUTOMATIC TRIGGER**: This algorithm MUST execute for ANY directory investigation, file search, or system status check.
**MANDATORY EXECUTION**: Cannot proceed with file operations until this algorithm completes successfully.
**VIOLATION**: Using any file listing tool without executing this algorithm first.

MANDATORY STEPS - Agents MUST execute platform-specific commands:

1. Detect Platform and Initialize Parameters:
   - platform = detect_current_platform()  # windows/linux/darwin/unknown
   - base_path = resolve_absolute_path(directory_path)
   - max_depth = min(recursion_depth, 10)  # Safety limit
   - include_hidden = True  # ALWAYS include hidden files - NEVER set to False
   - exclude_patterns = ['.git', '__pycache__', 'node_modules']

2. Execute Platform-Specific Hidden File Detection:

   FOR Windows Systems:
   - Primary Command: PowerShell "Get-ChildItem -Path $directory -Force -File -Recurse"
   - Fallback Command: CMD "dir /a:h /b /s $directory"
   - Python Fallback: Use win32api.GetFileAttributes() with FILE_ATTRIBUTE_HIDDEN check

   FOR Unix/Linux/macOS Systems:
   - Primary Command: find $directory -name ".*" -type f 2>/dev/null
   - Fallback Command: ls -la $directory | grep "^\."
   - Python Fallback: pathlib.Path.glob('**/.*') with error handling

   FOR Unknown Platforms:
   - Universal Python: Cross-platform pathlib implementation

3. Apply hidden file detection rules - MUST check ALL:
   - Dot-prefix files: .* (Unix/Linux/macOS hidden files)
   - System attributes: Platform-specific hidden flags (Windows FILE_ATTRIBUTE_HIDDEN)
   - Configuration files: .env, .gitignore, .eslintrc, .settings, .config, .agentic_initialized
   - Framework files: .bootstrap.json, .framework files
   - Temporary files: .tmp, .cache, .log variants

4. Process special file types with platform awareness:
   - Symbolic links: Resolve and check target if accessible
   - Special files: Skip device files, sockets, named pipes
   - Large files: Use stat() for size checking before processing
   - Binary files: Flag for specialized processing
   - Permission issues: Log and categorize as inaccessible

5. Return categorized file list - MUST include:
   - visible_files: Regular user-visible files
   - hidden_files: Configuration and system files (MANDATORY)
   - dot_files: Files starting with . (MANDATORY for Unix-like systems)
   - system_hidden: Files with hidden attributes (MANDATORY for Windows)
   - special_files: Links, devices (with warnings)
   - inaccessible_files: Permission denied files (logged)

VIOLATION: Agents that skip hidden files or use incomplete scanning methods.
```

#### **Platform-Specific Command Examples:**

**Windows PowerShell:**
```powershell
# Comprehensive hidden file detection
Get-ChildItem -Path "C:\project" -Force -File -Recurse | Where-Object {
    $_.Attributes -band [System.IO.FileAttributes]::Hidden -or $_.Name -like ".*"
}
```

**Windows Command Prompt:**
```batch
REM List all files including hidden
dir /a /b /s "C:\project"
```

**Linux/macOS:**
```bash
# Find all hidden files recursively
find /project -name ".*" -type f 2>/dev/null

# Alternative using ls
ls -laR /project 2>/dev/null | grep "^-" | grep "\./\."
```

**Cross-Platform Python Implementation:**
```python
import os
import platform
from pathlib import Path

def detect_hidden_files_cross_platform(directory):
    """Universal hidden file detection for all platforms."""
    system = platform.system().lower()
    hidden_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)

            # Platform-specific hidden detection
            if system == 'windows':
                try:
                    # Check Windows hidden attribute
                    import win32api, win32con
                    attrs = win32api.GetFileAttributes(filepath)
                    is_hidden = bool(attrs & win32con.FILE_ATTRIBUTE_HIDDEN)
                except ImportError:
                    # Fallback to dot-file check
                    is_hidden = file.startswith('.')
            else:
                # Unix-like systems
                is_hidden = file.startswith('.')

            if is_hidden:
                hidden_files.append(filepath)

    return hidden_files
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

0. Check git context for overlay mode:
   - IF knowledge_graph.git_aware.enabled AND project is git-managed:
     - Determine if base graph exists
     - IF on non-default branch AND base exists:
       - Delegate to Diff_Based_Overlay_Construction instead
       - RETURN overlay result (skip standard full construction)
     - IF on default branch AND base exists AND changes are small:
       - Delegate to Base_Graph_Refresh instead
       - RETURN refreshed base (skip standard full construction)
   - IF NOT git-managed OR git_aware.enabled = false:
     - Continue with standard full construction (steps 1-6 unchanged)

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
     - IF knowledge_graph.git_aware.enabled AND is_base_construction:
       - Store in knowledge_graph/base/ with base_manifest
       - Record base_commit for future overlay comparisons
     - IF knowledge_graph.git_aware.enabled AND is_overlay_construction:
       - Store in knowledge_graph/overlays/[sanitized-branch-name]/
     - ELSE (standard non-git-aware mode):
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

0. Resolve effective graph for git-aware mode:
   - IF knowledge_graph.git_aware.enabled AND project is git-managed:
     - Determine current branch
     - IF on non-default branch AND overlay exists for current branch:
       - Execute Overlay_Merge_Resolution to get effective_knowledge_graph
       - Use effective_knowledge_graph as the knowledge_graph input for steps 1-6
     - IF on default branch:
       - Use base graph directly
   - IF NOT git-managed OR git_aware.enabled = false:
     - Use standard knowledge_graph (current behavior)

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
2.5. Overlay lifecycle management (git-aware mode):
   - IF knowledge_graph.git_aware.enabled:
     - Scan all branch overlays in knowledge_graph/overlays/
     - FOR each overlay:
       - Check if branch still exists: git branch --list [branch-name]
       - IF branch deleted AND overlay age > overlay_retention_days:
         - Mark overlay for cleanup (with user consent per cleanup_guidance)
       - IF overlay is STALE (base refreshed since overlay created):
         - Mark for reconstruction on next branch checkout
     - Prune overlay directory of cleaned-up branches
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

## Python-Enhanced KG Construction

**ADVANCED CAPABILITY**: Agents can leverage Python execution for enhanced KG construction when system conditions allow safe execution.

### Runtime Script Generation Algorithm
```
Algorithm: Python_Enhanced_KG_Construction
Input: project_files, system_capabilities, safety_requirements
Output: Enhanced KG with Python-derived insights

1. Execute Safety_Validation_Check:
   - Verify Python execution environment safety
   - Check allowed modules availability
   - Validate sandboxing capabilities
   - Confirm fallback mechanisms

2. IF safety validation PASSES:
   - Generate Python analysis script dynamically
   - Execute in sandboxed environment
   - Process results into KG format
   - Log transparency information

3. IF safety validation FAILS or execution errors:
   - Automatically fallback to text-based analysis
   - Log fallback reason for transparency
   - Continue with standard KG construction

4. Merge Python-enhanced and text-based results
5. Update KG with combined insights
```

### Safety Validation Requirements
**MANDATORY**: Python execution requires comprehensive safety validation.

#### Pre-Execution Checks
- **Environment Safety**: Verify sandboxed execution capabilities
- **Module Whitelisting**: Only allow safe, analysis-relevant modules
- **Resource Limits**: CPU time and memory constraints enforced
- **Fallback Availability**: Text-based analysis must remain functional

#### Execution Environment
- **Sandboxed Python**: Isolated execution preventing system access
- **Timeout Protection**: Automatic termination of long-running scripts
- **Memory Monitoring**: Resource usage tracking and limits
- **Error Containment**: Script failures don't affect main KG system

### Dynamic Script Generation

#### Code Analysis Scripts
```python
# Example generated script for import analysis
import ast
import os
from typing import Dict, List, Set

def analyze_python_imports(file_path: str) -> Dict[str, List[str]]:
    \"\"\"Analyze Python file for import relationships.\"\"\"
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read())

        imports = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(alias.name.split('.')[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.append(node.module.split('.')[0])

        return {file_path: list(set(imports))}
    except Exception as e:
        return {file_path: []}
```

#### Class Hierarchy Analysis
```python
# Generated script for inheritance relationships
def analyze_class_hierarchy(file_path: str) -> Dict[str, List[str]]:
    \"\"\"Extract class inheritance relationships.\"\"\"
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read())

        classes = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                parents = []
                for base in node.bases:
                    if isinstance(base, ast.Name):
                        parents.append(base.id)
                    elif isinstance(base, ast.Attribute):
                        # Handle module.Class patterns
                        parents.append(f"{base.value.id}.{base.attr}" if isinstance(base.value, ast.Name) else base.attr)
                classes[node.name] = parents

        return {file_path: classes}
    except Exception as e:
        return {file_path: {}}
```

### Transparency & Logging

#### Execution Transparency
**MANDATORY**: All Python executions must be logged for user transparency.

- **Script Content**: Generated script code logged before execution
- **Execution Results**: Success/failure status and output
- **Fallback Reasons**: Why text fallback was used (if applicable)
- **Performance Metrics**: Execution time, memory usage, analysis coverage

#### User-Accessible Transparency
- **`/kg-python-status`**: Show current Python enhancement status
- **`/kg-script-log`**: View recent script generation and execution logs
- **`/kg-fallback-reasons`**: Understand why text analysis was used

### Fallback Mechanisms

#### Automatic Fallback Triggers
- **Safety Validation Failure**: Environment not safe for Python execution
- **Module Unavailability**: Required analysis modules not installed
- **Execution Errors**: Script runtime failures or timeouts
- **Resource Limits**: Memory or time constraints exceeded

#### Seamless Integration
- **Result Merging**: Python and text analysis results combined intelligently
- **Quality Scoring**: Results ranked by analysis method reliability
- **Progressive Enhancement**: Python results enhance text analysis, don't replace

## Git-Aware Knowledge Graph Algorithms

When the target project is managed by git, KG construction can leverage branch-level diffing to avoid redundant reconstruction. Instead of rebuilding the entire graph per branch, a **base graph** represents the default branch and lightweight **overlay graphs** capture only the delta for each feature branch.

**Guard Clause**: All algorithms in this section check `knowledge_graph.git_aware.enabled` first. When disabled (default), all existing KG algorithms execute unchanged. For non-git projects, the git detection in step 1 triggers an immediate fallback to standard `Incremental_Graph_Builder`.

### Git-Aware KG Construction Algorithm
```
Algorithm: Git_Aware_KG_Construction
Input: project_path, current_branch, memory_system, existing_base_graph
Output: effective_knowledge_graph (base + overlay)

1. Detect git context:
   - Check if project_path is a git repository
   - IF NOT git managed: Fallback to standard Incremental_Graph_Builder
   - Identify default branch (main/master) via git remote HEAD or config
   - IF git_aware_kg.default_branch_override is set: Use that value
   - Identify current branch via git rev-parse --abbrev-ref HEAD
   - Get merge-base commit between current branch and default branch

2. Determine construction mode:
   - IF current_branch == default_branch: MODE = "base_construction"
   - IF base graph does not exist: MODE = "base_construction"
   - IF base graph exists AND current_branch != default_branch: MODE = "overlay_construction"

3. IF MODE == "base_construction":
   - Execute full Incremental_Graph_Builder on entire codebase
   - Generate base_manifest with node/edge identifiers and content hashes
   - Store as base graph in knowledge_graph/base/
   - Record base_commit (HEAD of default branch at construction time)

4. IF MODE == "overlay_construction":
   - Execute Diff_Based_Overlay_Construction

5. Return effective graph:
   - IF on default branch: Return base graph directly
   - IF on non-default branch: Execute Overlay_Merge_Resolution
```

### Diff-Based Overlay Construction Algorithm
```
Algorithm: Diff_Based_Overlay_Construction
Input: project_path, current_branch, default_branch, base_graph, base_manifest
Output: branch_overlay

1. Compute file diff set:
   - Run: git diff --name-only [merge-base]..HEAD
   - Collect changed_files (added, modified, deleted)
   - Record merge_base_commit for overlay provenance

2. Compute dependency expansion:
   - FOR each file in changed_files:
     - Query base_graph for entities sourced from this file
     - Identify direct dependents (files that import/reference changed files)
     - Add first-degree dependents to analysis_set
   - Deduplicate analysis_set
   - Cap analysis_set at max_overlay_analysis_files (default: 50)

3. Extract entities from analysis_set:
   - Execute Structured_Entity_Extraction on each file in analysis_set
   - Execute Pattern_Based_Relation_Extraction for relationships
   - IF python_enhancement.enabled:
     - Execute Python_Enhanced_KG_Construction on analysis_set only

4. Compute delta against base_graph:
   - FOR each extracted entity:
     - IF entity exists in base_manifest with same content_hash: SKIP (unchanged)
     - IF entity exists with different content_hash: Mark as MODIFIED
     - IF entity NOT in base_manifest: Mark as ADDED
   - FOR each base entity sourced from deleted files: Mark as REMOVED
   - FOR each extracted relationship:
     - Compare against base relationships using source+target+type key
     - Classify as ADDED, MODIFIED, or UNCHANGED
   - FOR each base relationship involving REMOVED entities: Mark as REMOVED

5. Construct overlay document:
   - Create overlay with sections: added_nodes, removed_nodes, modified_nodes,
     added_edges, removed_edges, modified_edges
   - Include merge_base_commit and branch_name in metadata
   - Include file_diff_summary for traceability

6. Store overlay:
   - Sanitize branch name: replace / with -- for directory safety
   - Write to knowledge_graph/overlays/[sanitized-branch-name]/
   - Update overlay_manifest with timestamp and validity info
   - IF memory_rules.enabled = false: Keep overlay in session context only
```

### Overlay Merge Resolution Algorithm
```
Algorithm: Overlay_Merge_Resolution
Input: base_graph, branch_overlay
Output: effective_knowledge_graph

1. Initialize effective_graph as deep copy of base_graph

2. Apply removals:
   - FOR each node in overlay.removed_nodes:
     - Remove node and all connected edges from effective_graph
   - FOR each edge in overlay.removed_edges:
     - Remove edge from effective_graph

3. Apply modifications:
   - FOR each node in overlay.modified_nodes:
     - Replace matching node in effective_graph with overlay version
   - FOR each edge in overlay.modified_edges:
     - Replace matching edge in effective_graph with overlay version

4. Apply additions:
   - FOR each node in overlay.added_nodes: Add to effective_graph
   - FOR each edge in overlay.added_edges:
     - Add edge (validate source/target nodes exist)

5. Validate merged graph:
   - Check for orphaned edges (referencing non-existent nodes)
   - Check for duplicate nodes after merge
   - Log inconsistencies for debugging

6. Return effective_knowledge_graph
```

### Base Graph Refresh Algorithm
```
Algorithm: Base_Graph_Refresh
Input: project_path, existing_base_graph, base_manifest
Output: updated_base_graph, invalidated_overlays_list

1. Detect base changes:
   - Get current HEAD of default branch
   - Compare with base_manifest.base_commit
   - IF unchanged: Return existing base graph (no work needed)
   - Run: git diff --name-only [base_commit]..HEAD on default branch

2. Incremental base update:
   - Apply Diff_Based_Overlay_Construction logic targeting the base itself
   - Apply resulting delta to base_graph
   - Update base_manifest with new base_commit and content hashes

3. Invalidate affected overlays:
   - FOR each overlay in knowledge_graph/overlays/:
     - IF overlay's changed files overlap with base changed_files: Mark STALE
     - IF no overlap: Overlay remains valid
   - Return list of invalidated overlays

4. Persist updated base and manifest
```

### Cross-Branch KG Analysis Algorithm
```
Algorithm: Cross_Branch_KG_Analysis
Input: base_graph, branch_overlays[], analysis_scope
Output: cross_branch_analysis_report

1. Collect active branch overlays:
   - Scan knowledge_graph/overlays/ for branch directories
   - Load overlay_manifest from each
   - Filter stale overlays (merge_base older than base graph)
   - Limit to max_branches_to_compare (default: 10)

2. Entity collision detection:
   - Build entity_modification_map: entity_id -> [branches that modify it]
   - FOR each entity modified by 2+ branches:
     - IF same change across branches: Flag as CONVERGENT (low risk)
     - IF different changes: Flag as DIVERGENT (high risk)

3. Semantic conflict detection:
   - FOR each DIVERGENT entity:
     - Analyze relationship changes across branches
     - Detect interface modifications (same interface changed differently)
     - Detect dependency changes (edges to/from entity differ)
     - Assign semantic_conflict_score (0.0 = safe, 1.0 = certain conflict)

4. Branch divergence mapping:
   - FOR each overlay: count total delta size, compute overlap_ratio with others
   - Calculate divergence_distance from base

5. Generate report:
   - Merge conflicts ranked by semantic_conflict_score
   - Subsystem impact map (which branches touch which areas)
   - Merge-order recommendations (least conflicts first)
   - Store in knowledge_graph/cross_branch/ using Cross-Branch Analysis Template

6. Persist report:
   - IF memory_rules.enabled: Store as markdown in cross_branch/ directory
   - IF memory_rules.enabled = false: Return in session context only
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

