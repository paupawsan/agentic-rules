# RAG Rules

## Overview

Retrieval-Augmented Generation rules form the foundation of intelligent information processing, optimizing context management across the entire agentic system. These rules enhance memory operations, influence design decisions, and provide pattern-driven insights for all agent activities.

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

## Core Algorithms

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

## Tool Integration

### File System Tools
- Use directory listing to understand project structure
- Apply glob patterns for targeted file discovery
- Read file metadata before content analysis
- Implement streaming reads for large files

### Search and Filter Tools
- Apply text search with context expansion
- Use regex patterns for structured data extraction
- Implement fuzzy matching for flexible queries
- Support multi-file search operations

### External Tool Integration
- Leverage code execution for dynamic analysis
- Use external commands for file processing
- Integrate with version control for change tracking
- Connect to databases for structured data retrieval

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

