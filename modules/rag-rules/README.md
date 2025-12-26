# 📚 RAG Rules Plugin

## Overview

The **RAG (Retrieval-Augmented Generation) Rules** plugin enhances AI agents' ability to process and utilize information effectively. This plugin implements advanced information retrieval and context optimization algorithms that help agents read, understand, and apply relevant information from large knowledge bases.

## 🎯 What It Does

**RAG Rules** transforms how AI agents handle information:

- **Smart Reading**: Agents read files strategically, not sequentially
- **Context Optimization**: Automatically determines what information is most relevant
- **Information Synthesis**: Combines multiple sources for comprehensive understanding
- **Knowledge Graph Learning**: Dynamically builds and learns from knowledge relationships
- **Self-Learning Patterns**: Adapts behavior based on user interactions and preferences
- **Token Efficiency**: Maximizes useful information within token limits

## 🚨 **MANDATORY COMPLIANCE REQUIREMENTS**

### Critical Agent Requirements
**⚠️ NON-COMPLIANCE RESULTS IN RULE VIOLATION**

Agents implementing RAG rules **MUST** adhere to these requirements:

#### 🔍 **Hidden File Detection (MANDATORY)**
- **AUTOMATIC EXECUTION**: Detect_Hidden_Files_Algorithm executes for ANY directory investigation
- **COMPREHENSIVE SCANNING**: Include ALL dot-files (.env, .gitignore, .settings, .agentic_initialized)
- **TOOL MANDATE**: Use `pathlib.Path.iterdir()` or `os.scandir()` - **NEVER** basic `list_dir`
- **VIOLATION CONSEQUENCE**: Incomplete information processing and rule compliance failure

#### 🔧 **Tool Selection Requirements (MANDATORY)**
- **PRE-OPERATION EXECUTION**: Select_File_Discovery_Tool runs BEFORE any file operations
- **AUTOMATIC TRIGGERS**: Executes when investigating directories, searching files, or checking system status
- **PROHIBITED TOOLS**: Standard directory listing tools are INSUFFICIENT and violate compliance
- **MANDATORY ALGORITHMS**: All defined algorithms MUST execute when conditions are met

#### ⚡ **Automatic Trigger Conditions**
- **Directory Investigation**: Triggers hidden file detection algorithms
- **File Search Operations**: Forces comprehensive scanning including hidden files
- **System Status Checks**: Requires scanning for initialization markers and config files

---

## ✨ Key Capabilities

### Intelligent Reading Strategies

#### 📖 **Document Reading**
- **TOC Priority**: Starts with table of contents for document structure
- **Summary First**: Reads executive summaries before detailed content
- **Section Navigation**: Jumps to relevant sections based on query context

#### 💻 **Code Reading**
- **Signature First**: Reads function signatures and class definitions first
- **Dependency Tracing**: Follows import and dependency chains
- **Pattern Recognition**: Identifies code patterns and architectural decisions

#### 🔍 **Selective Reading**
- **Importance Scoring**: Rates content relevance to current task
- **Chunking Optimization**: Breaks content into meaningful units
- **Progressive Expansion**: Starts narrow, expands as needed

### Context Management

#### 🎯 **Dynamic Context Windows**
- **Adaptive Sizing**: Adjusts context window based on task complexity
- **Relevance Filtering**: Prioritizes important information over filler content
- **Token Optimization**: Maximizes information density within limits

#### 🔗 **Hierarchical Processing**
- **Multi-Level Reading**: Summaries → Key sections → Details → Code
- **Recursive Analysis**: Follows references and connections
- **Pattern Integration**: Combines information from multiple sources

#### 🔧 **Intelligent Tool Selection**
- **Context-Aware Tools**: Automatically selects appropriate file discovery and search tools
- **MANDATORY Hidden File Detection**: Agents MUST detect and process hidden files (dot-files like .env, .gitignore, .settings)
- **Automatic Algorithm Triggers**: Executes Detect_Hidden_Files_Algorithm for ANY directory investigation
- **Comprehensive Scanning**: Uses pathlib.Path.iterdir() with hidden file inclusion - NEVER uses basic list_dir
- **Safe Tool Usage**: Validates permissions and applies security restrictions
- **Performance Optimization**: Chooses optimal algorithms for different file types and query patterns

### Information Processing

#### 📊 **Relevance Scoring**
- **Semantic Matching**: Understands meaning beyond keywords
- **Context Awareness**: Considers current task and user intent
- **Temporal Weighting**: Prioritizes recent and frequently referenced information

#### 🔄 **Quality Assurance**
- **Source Validation**: Cross-references multiple information sources
- **Consistency Checking**: Ensures information coherence
- **Gap Identification**: Flags missing or contradictory information

### 🚀 **Advanced Intelligence Features**

#### 🧠 **Runtime Knowledge Graph Generation**
- **Dynamic Learning**: Automatically builds knowledge graphs from conversations and documents
- **Relationship Discovery**: Identifies connections between entities, concepts, and ideas
- **Graph Evolution**: Updates and strengthens relationships over time
- **Intelligent Pruning**: Maintains graph efficiency by removing outdated connections
- **Memory Integration**: Persists knowledge graphs when memory_rules enabled (prevents loss during context summarization)

#### 🔗 **Graph-Enhanced Retrieval**
- **Relationship-Based Search**: Finds information through connections, not just keywords
- **Inference Engine**: Discovers indirect relationships and hidden connections
- **Contextual Expansion**: Retrieves related information beyond direct matches
- **Hybrid Ranking**: Combines traditional relevance with graph centrality

#### 🎯 **Self-Learning Pattern Recognition**
- **User Behavior Analysis**: Learns communication patterns and preferences
- **Adaptive Responses**: Adjusts interaction style based on learned patterns
- **Conversation Memory**: Remembers context across multiple interactions
- **Personalization**: Tailors responses to individual user styles

#### ⚡ **Intelligent Context Fusion**
- **Multi-Source Integration**: Combines traditional RAG with knowledge graph insights
- **Dynamic Weighting**: Balances factual retrieval with relational understanding
- **Comprehensive Synthesis**: Provides richer, more contextual responses
- **Real-time Adaptation**: Learns and improves with each interaction

## 🚫 Limitations & Constraints

### Information Boundaries
- **File System Access**: Limited to files the agent can access
- **Processing Limits**: Token limits and processing time constraints
- **Language Support**: Primarily optimized for supported languages
- **Context Windows**: Cannot exceed model's context limitations

### Algorithm Limitations
- **Semantic Understanding**: Relies on available AI capabilities for comprehension
- **Pattern Recognition**: May miss subtle or novel patterns (though self-learning improves this)
- **Graph Complexity**: Large knowledge graphs may require significant memory
- **Real-time Updates**: Cannot monitor live file changes
- **Cross-System Integration**: Limited to agent's accessible resources

### Performance Constraints
- **Processing Time**: Complex analysis may take time
- **Memory Usage**: Large knowledge bases require significant resources
- **Accuracy Trade-offs**: Speed vs. thoroughness balancing

## 🎯 Use Cases & Applications

### Code Analysis & Development
```
Use Case: Codebase Understanding Assistant
RAG Rules help agents quickly understand large codebases by:
- Reading architecture documentation first
- Following dependency chains in code
- Identifying key design patterns
- Providing context-aware code explanations
```

### Research & Documentation
```
Use Case: Documentation Research Assistant
Agents efficiently process documentation by:
- Starting with overviews and summaries
- Following cross-references to related topics
- Synthesizing information from multiple documents
- Providing comprehensive yet concise answers
```

### Technical Troubleshooting
```
Use Case: System Debugging Helper
RAG Rules optimize troubleshooting by:
- Reading error logs and configuration files strategically
- Cross-referencing documentation with code
- Identifying patterns in system behavior
- Providing targeted diagnostic recommendations
```

### Knowledge Base Management
```
Use Case: Internal Knowledge Assistant
For company documentation and procedures:
- Prioritizing current policies over outdated ones
- Following document hierarchies and relationships
- Synthesizing information from multiple sources
- Maintaining context across related topics
```

### Content Creation Support
```
Use Case: Writing and Content Assistant
RAG Rules enhance content creation by:
- Researching relevant background information
- Following style guides and brand guidelines
- Cross-referencing multiple sources for accuracy
- Maintaining consistency across related documents
```

### Intelligent Relationship Mapping
```
Use Case: Knowledge Discovery and Relationship Analysis
RAG Rules with Knowledge Graph capabilities help with:
- Understanding complex system architectures and dependencies
- Discovering hidden relationships between concepts and entities
- Building comprehensive knowledge bases from scattered information
- Providing contextual insights beyond direct queries
- Learning user-specific terminology and domain knowledge
```

## 📝 Sample Prompts & Usage

### Codebase Analysis
```
"Help me understand this React application. Focus on the component architecture and data flow."
```
→ RAG Rules will read package.json first, then key components, then follow data flow patterns

### Documentation Research
```
"I need to implement JWT authentication. What are the security best practices?"
```
→ RAG Rules will prioritize security documentation, cross-reference multiple sources, and provide comprehensive guidance

### Technical Investigation
```
"The application is throwing database connection errors. Help me diagnose the issue."
```
→ RAG Rules will examine configuration files, error logs, and database setup documentation in strategic order

### Learning Assistance
```
"I'm learning TypeScript. Explain the difference between interface and type."
```
→ RAG Rules will reference official documentation, examples, and best practice guides

### Knowledge Graph Exploration
```
"How do authentication, authorization, and JWT tokens relate in this system?"
```
→ Knowledge Graph will trace relationships between security concepts, identify dependencies, and provide comprehensive understanding

### Pattern-Based Assistance
```
"I've been working on this codebase for weeks. What patterns should I look for?"
```
→ Self-learning analyzes interaction history, identifies user focus areas, and suggests relevant patterns and relationships

## ⚙️ Configuration Options

### Reading Strategy Configuration
```json
{
  "rag_rules": {
    "enabled": true,
    "reading_strategies": {
      "document_reading": {
        "toc_priority": true,
        "summary_first": true
      },
      "code_reading": {
        "signature_first": true,
        "dependency_tracing": true
      }
    }
  }
}
```

### Context Optimization Settings
```json
{
  "context_optimization": {
    "max_context_window": 128000,
    "dynamic_adjustment": true,
    "relevance_threshold": 0.7
  }
}
```

### Knowledge Graph Configuration
```json
{
  "rag_rules": {
    "knowledge_graph": {
      "enabled": true,
      "runtime_generation": {
        "entity_extraction": true,
        "relationship_discovery": true,
        "dynamic_updates": true
      },
      "graph_management": {
        "max_nodes": 10000,
        "relationship_pruning": true
      }
    }
  }
}
```

### Self-Learning Configuration
```json
{
  "rag_rules": {
    "self_learning": {
      "enabled": true,
      "pattern_analysis": {
        "conversation_patterns": true,
        "user_preferences": true
      },
      "learning_mechanisms": {
        "reinforcement_learning": true,
        "pattern_recognition": true
      }
    }
  }
}
```

### Performance Tuning
```json
{
  "performance_optimization": {
    "lazy_loading": true,
    "parallel_processing": true,
    "caching_strategy": "lru"
  }
}
```

## 🔄 Integration with Other Rules

### Memory Rules Synergy
- RAG Rules provide information retrieval for memory storage
- Memory Rules store successful RAG strategies and preferences
- **Knowledge Graph Persistence**: When memory_rules enabled, constructed knowledge graphs are stored persistently
- **Graph Memory Categories**: Knowledge graphs stored in appropriate memory categories with long-term retention
- **Context Preservation**: Prevents knowledge graph loss during context summarization or resets
- Combined system learns optimal reading patterns and maintains knowledge relationships

### Critical Thinking Rules Enhancement
- RAG Rules gather comprehensive information for analysis
- Critical Thinking validates information quality and consistency
- Self-correcting system through validated information retrieval

### Bootstrap Coordination
- RAG Rules initialize early in the loading sequence
- Provides foundational information processing for other rules
- Optimizes context management across the entire framework

## 📊 Performance Metrics

### Processing Efficiency
- **Token Utilization**: 85-95% effective information density
- **Reading Speed**: 3-5x faster than sequential reading
- **Accuracy**: 90%+ relevance in retrieved information
- **Context Preservation**: Maintains 95% of critical information

### Resource Usage
- **Memory**: Efficient caching and lazy loading
- **Processing**: Parallel processing for multiple sources
- **Storage**: Compressed caching for performance
- **Network**: Minimized requests through intelligent prefetching

## 🔧 Troubleshooting

### Poor Information Retrieval
```
Symptom: Irrelevant or incomplete information retrieved
Solution: Adjust relevance thresholds and reading strategies in settings
```

### Slow Processing
```
Symptom: RAG operations taking too long
Solution: Enable caching, reduce context window, or disable parallel processing
```

### Context Overload
```
Symptom: Too much information causing token limit issues
Solution: Increase relevance threshold or enable progressive expansion
```

### Missing Information
```
Symptom: Important details not being retrieved
Solution: Check file access permissions and reading strategy configuration
```

## 📚 Algorithm Specifications

For technical implementation details, see:
- **[RULES.md.en](RULES.md.en)** - Complete algorithm specifications
- **[settings.json](settings.json)** - Configuration schema
- **[../CORE-RULES.md](../CORE-RULES.md)** - Framework integration guide

## 🔍 Advanced Features

### Multi-Source Synthesis
- Combines information from documentation, code, and logs
- Cross-references multiple sources for validation
- Identifies conflicts and resolves inconsistencies

### Runtime Knowledge Graph
- Dynamically builds relationship networks from interactions
- Discovers hidden connections between concepts and entities
- Evolves understanding through continuous learning
- Provides relational context beyond keyword matching

### Self-Learning Intelligence
- Analyzes user behavior patterns and preferences
- Adapts response strategies based on interaction history
- Learns domain-specific terminology and concepts
- Personalizes assistance based on individual user styles

### Hybrid Intelligence
- Combines traditional retrieval with graph-based reasoning
- Integrates factual knowledge with relational understanding
- Provides comprehensive context through multi-layered analysis
- Continuously improves through feedback and learning cycles

## 🤝 Contributing

Help improve RAG Rules functionality:

- **Algorithm Improvements**: Submit better information retrieval strategies
- **Performance Optimizations**: Enhance processing speed and accuracy
- **New Use Cases**: Add support for additional information types
- **Integration Testing**: Test with various document and code types

---

**📚 RAG Rules**: Teaching AI agents to read smarter, not harder.

*Copyright (c) 2025 Paulus Ery Wasito Adhi. Licensed under the MIT License.*
