# 🧠 Memory Rules Plugin

## Overview

The **Memory Rules** plugin provides persistent memory capabilities for AI agents, enabling them to retain context, learn from interactions, and build knowledge over time. This plugin implements a sophisticated memory system with multiple categories and intelligent organization.

## 🎯 What It Does

**Memory Rules** creates a structured memory system that goes beyond simple chat history:

- **Persistent Storage**: Information survives across sessions and conversations
- **Intelligent Organization**: Automatically categorizes and links related information
- **Context Awareness**: Remembers user preferences, patterns, and important details
- **Cross-Session Learning**: Builds knowledge from multiple interactions over time

## ✨ Key Capabilities

### Memory Categories

#### 1. 🧠 **Technical Memory**
- Code patterns and programming knowledge
- Technical solutions and troubleshooting steps
- Tool usage patterns and preferences
- Development workflows and best practices

#### 2. 🎭 **Behavioral Memory**
- User interaction patterns and preferences
- Communication styles and expectations
- Response preferences and feedback patterns
- Personality traits and interaction history

#### 3. 📍 **Contextual Memory**
- Project-specific information and constraints
- Environment details and configurations
- Current work context and objectives
- Session-specific requirements

#### 4. 💬 **User Interaction Memory**
- Important user requests and requirements
- Feedback and corrections provided
- Preferences expressed during conversations
- Historical context from previous sessions

#### 5. 📊 **Session Memory**
- Conversation flow and progression
- Topic evolution and transitions
- Decision points and outcomes
- Session goals and achievements

#### 6. 🎯 **Topic Memory**
- Deep dives into specific subjects
- Complex problem-solving sessions
- Research and analysis threads
- Long-term knowledge development

#### 7. 📅 **Git History Memory**
- Project evolution and milestones
- Code changes and development patterns
- Team collaboration history
- Project decision tracking

#### 8. 👤 **Personal Memory**
- Personal preferences and work styles
- Individual goals and motivations
- Personal context and background
- Long-term relationship building

#### 9. 🔐 **Credentials Memory**
- API keys, tokens, and access credentials
- Authentication patterns and preferences
- Security-related information
- Access management preferences

#### 10. 🚨 **Sensitive Memory**
- Confidential information and private data
- Security-sensitive details
- Privacy-protected information
- Restricted access content

## 🚫 Limitations & Constraints

### What It Cannot Do
- **Real-time Collaboration**: Cannot synchronize memory across multiple agent instances in real-time
- **Infinite Storage**: Memory has practical limits based on storage configuration
- **Perfect Recall**: May prioritize recent or frequently accessed information
- **Cross-Agent Sharing**: Memory is typically agent-specific unless explicitly configured
- **Automatic Cleanup**: Requires manual or configured cleanup policies

### Security Boundaries
- **Local Storage Only**: Memory stays within the configured storage paths
- **User Consent Required**: All memory operations require explicit user permission
- **Encryption Available**: Sensitive memory can be encrypted
- **Access Controls**: Different memory categories have different access levels

## 🎯 Use Cases & Applications

### Development Workflow Enhancement
```
Use Case: Code Review Assistant
Memory captures coding patterns, project conventions, and user preferences
Agent remembers specific code style preferences and common issues
Provides consistent feedback based on learned patterns
```

### Technical Support & Troubleshooting
```
Use Case: System Administration Helper
Remembers server configurations, common issues, and resolution patterns
Tracks user-specific troubleshooting preferences and successful solutions
Builds knowledge base of system-specific problems and fixes
```

### Research & Analysis Tasks
```
Use Case: Research Assistant
Maintains research context across multiple sessions
Remembers user interests, preferred sources, and analysis methods
Tracks hypothesis development and evidence gathering
```

### Creative Collaboration
```
Use Case: Content Creation Partner
Remembers writing style preferences and creative patterns
Tracks project themes, character development, and plot elements
Maintains consistency across creative sessions
```

### Learning & Education
```
Use Case: Personalized Tutor
Adapts to learning style and pace based on memory
Remembers progress, challenges, and successful approaches
Provides continuity across learning sessions
```

## 📝 Sample Prompts & Usage

### Basic Memory Activation
```
"I need help with a project. Please remember that I prefer TypeScript over JavaScript and usually work with React."
```
→ Memory Rules will store this preference for future sessions

### Context Building
```
"This is a Node.js backend project. Remember we're using Express, MongoDB, and JWT authentication."
```
→ Memory captures project context and technical stack preferences

### Pattern Learning
```
"When I ask for code reviews, focus on performance, security, and maintainability in that order."
```
→ Memory learns user's priority preferences for code review feedback

### Session Continuity
```
"Continuing from our last session about the authentication system..."
```
→ Memory provides context from previous conversations

## ⚡ Quick Start Memory Setup (5 Minutes)

For users who want to get memory working immediately with minimal setup:

### One-Prompt Setup
```
"Enable memory for this project. Remember: I'm working on a [language/framework] project using [key technologies]. My preferences: [2-3 key preferences]. Use memory to remember project details, my coding style, and common issues we encounter."
```

**That's it!** Memory will start working immediately and learn as you work.

### Quick Validation
**Open a new fresh chat window** and ask:
```
"What do you remember about this project so far?"
```
→ Should show basic project information and your preferences

### When to Use Quick Setup
- ✅ **New to memory features** - Get started without complexity
- ✅ **Small/simple projects** - Basic memory sufficient
- ✅ **Time constraints** - Need memory working immediately
- ✅ **Exploratory work** - Test memory capabilities quickly

### When to Use Comprehensive Setup
- 🔧 **Large/complex projects** - Need detailed context and patterns
- 🔧 **Team collaboration** - Multiple developers with different preferences
- 🔧 **Long-term projects** - Maximum memory effectiveness over time
- 🔧 **Custom workflows** - Specific requirements and edge cases

### Quick Setup Benefits
- ⚡ **Immediate activation** - Memory works in under 1 minute
- 🎯 **Automatic learning** - Improves with each interaction
- 🔄 **Progressive enhancement** - Can upgrade to comprehensive setup later
- 🛡️ **Safe defaults** - Conservative settings prevent issues

### Quick Setup Tips
- **Be specific about technology stack** - Mention languages, frameworks, databases
- **Include 2-3 key preferences** - Focus on most important coding/workflow preferences
- **Mention project type** - "web app", "API", "mobile app", "data analysis", etc.
- **Start simple** - Memory will learn and improve with each conversation
- **Validate regularly** - Ask "what do you remember" to check memory accuracy

### Example Quick Setups
```
# Web Development
"Enable memory for this React/TypeScript web app using Next.js and Tailwind CSS. I prefer functional components and custom hooks."

# Data Science
"Enable memory for this Python data analysis project using pandas, numpy, and matplotlib. I prefer clear variable names and comprehensive documentation."

# Backend API
"Enable memory for this Node.js/Express API using MongoDB. I prefer async/await, input validation, and comprehensive error handling."
```

---

## 🚀 Setting Up Memory for a New Project

For comprehensive memory setup with maximum effectiveness:

### Step 1: Initial Project Context Setup
Start with comprehensive project introduction:

```
"This is a new [Project Type] project called [Project Name]. Key details to remember:

TECHNICAL STACK:
- Language: [Python/Node.js/etc.]
- Framework: [Django/React/etc.]
- Database: [PostgreSQL/MongoDB/etc.]
- Deployment: [Docker/AWS/etc.]

TEAM & WORKFLOW:
- Code style: [PEP8/ESLint/etc.]
- Git workflow: [GitFlow/trunk-based/etc.]
- Testing: [pytest/Jest/etc.]
- Documentation: [Sphinx/JSDoc/etc.]

PROJECT GOALS:
- Primary objective: [main purpose]
- Target users: [user type/demographics]
- Key features: [main functionality]
- Success metrics: [KPIs/goals]

CONSTRAINTS & PREFERENCES:
- Performance requirements: [response times/etc.]
- Security requirements: [compliance standards]
- Budget/timeline: [constraints]
- My preferences: [your coding style, tools, approaches]
```
→ This establishes foundational context across all memory categories

### Step 2: Codebase Familiarization
Guide the agent through understanding your codebase:

```
"Let's explore the project structure. Remember these key directories and their purposes:

CORE DIRECTORIES:
- src/components: React components following [naming convention]
- src/utils: Shared utilities, prefer [functional/programming style]
- tests/: Unit tests using [testing framework]
- docs/: Documentation in [Markdown/reStructuredText]

IMPORTANT PATTERNS:
- Error handling: Always use [try/catch/async-await/etc.]
- State management: [Redux/Context/Zustand/etc.] for global state
- API calls: [Axios/Fetch/etc.] with [error handling pattern]
- File naming: [kebab-case/camelCase/etc.]
```
→ Memory builds technical understanding and coding patterns

### Step 3: Personal Workflow Setup
Establish your working preferences:

```
"Remember my development workflow preferences:

CODING STYLE:
- Indentation: [spaces/tabs] with [width]
- Line length: Maximum [80/100/120] characters
- Comments: [JSDoc/docstrings/etc.] for public APIs
- Naming: [descriptive/self-documenting] variable names

REVIEW PREFERENCES:
- Focus areas: [performance > security > maintainability]
- Feedback style: [constructive/direct/balanced]
- Code examples: [always/sometimes/never] include examples
- Priority: [bugs > features > refactoring]

COMMUNICATION:
- Status updates: [regular/as-needed/on-request]
- Question format: [direct/open-ended/structured]
- Documentation: [comprehensive/essential/minimal]
```
→ Memory learns your personal preferences and working style

### Step 4: Problem-Solution Pattern Building
Establish common issues and solutions:

```
"Common issues in this project to remember:

FREQUENT PROBLEMS:
1. Database connection timeouts → Check connection pool settings
2. API rate limiting → Implement exponential backoff
3. Memory leaks → Profile with [tool] and fix [common causes]

SOLUTION PATTERNS:
- Authentication errors → Verify token format and expiration
- Validation failures → Check input sanitization and schema
- Performance issues → Profile with [tool] and optimize [bottlenecks]

DEBUGGING APPROACH:
- Start with [logs/stack traces/error messages]
- Check [configuration/environment variables]
- Verify [dependencies/versions/compatibility]
- Test [isolated components/integration points]
```
→ Memory builds troubleshooting knowledge base

### Step 5: Validation & Testing
Verify memory setup is working:

```
"Let's test that you've remembered the key project information:

1. What programming language and framework are we using?
2. What are the main directories and their purposes?
3. What are my code review priorities?
4. What should you check first when there's a database error?

If you remember these correctly, then memory setup is complete!"
```
→ Validates memory retention and understanding

## 🔧 Troubleshooting Memory Issues

### Symptom: Memory Not Persisting Between Sessions

**Possible Causes & Solutions:**

1. **Storage Path Issues**
   ```
   Symptom: Settings reset every session
   Solution: Check memory storage path permissions and disk space
   Command: Verify write access to configured memory directory
   ```

2. **Configuration Not Saved**
   ```
   Symptom: Memory settings not retained
   Solution: Ensure memory_rules.enabled = true in settings.json
   Check: Verify settings.json contains memory configuration
   ```

3. **Browser Storage Issues**
   ```
   Symptom: Web interface loses memory settings
   Solution: Clear browser cache, try incognito mode, check localStorage
   Alternative: Use setup-launcher.py for persistent server storage
   ```

### Symptom: Memory Not Using Learned Information

**Possible Causes & Solutions:**

1. **Insufficient Context**
   ```
   Symptom: Agent doesn't remember project details
   Solution: Provide more comprehensive initial project setup prompts
   Add: Specific examples, code snippets, and detailed preferences
   ```

2. **Category Mismatch**
   ```
   Symptom: Information stored but not retrieved
   Solution: Check memory category mapping
   Verify: Technical details → technical category
   Personal preferences → behavioral/personal categories
   ```

3. **Query Context Issues**
   ```
   Symptom: Agent has info but doesn't apply it
   Solution: Be more explicit in queries
   Try: "Remembering our project setup..." or "Based on our previous discussion..."
   ```

### Symptom: Memory Conflicts or Inconsistencies

**Possible Causes & Solutions:**

1. **Multiple Project Confusion**
   ```
   Symptom: Agent mixes information from different projects
   Solution: Clearly specify project context in prompts
   Use: "In this [Project Name] project..." prefixes
   ```

2. **Outdated Information**
   ```
   Symptom: Agent uses old patterns after project changes
   Solution: Explicitly update memory with new information
   Command: "Update your memory: we switched from [old] to [new]"
   ```

3. **Retention Policy Issues**
   ```
   Symptom: Important information gets cleaned up
   Solution: Adjust retention settings in memory configuration
   Increase: retention_days for important categories
   ```

### Symptom: Performance Issues with Memory

**Possible Causes & Solutions:**

1. **Memory Size Too Large**
   ```
   Symptom: Slow response times, high memory usage
   Solution: Reduce max_entries_per_category in settings
   Enable: compression and cleanup policies
   ```

2. **Frequent Access Patterns**
   ```
   Symptom: Memory operations slowing down
   Solution: Enable caching and optimize indexing
   Check: memory performance settings in configuration
   ```

3. **Storage I/O Bottlenecks**
   ```
   Symptom: Memory operations cause delays
   Solution: Move memory storage to faster storage medium
   Check: SSD vs HDD, network vs local storage
   ```

### Symptom: Memory Not Learning from Corrections

**Possible Causes & Solutions:**

1. **Correction Format Issues**
   ```
   Symptom: Agent repeats same mistakes
   Solution: Be explicit about corrections
   Use: "Remember for future reference: [mistake] should be [correction]"
   ```

2. **Feedback Loop Disabled**
   ```
   Symptom: Corrections not retained
   Solution: Enable error learning in memory settings
   Check: error_correction_learning = true
   ```

### Advanced Troubleshooting

#### Memory Inspection
```
To check what's in memory, ask the agent:
"What do you remember about this project's technical stack?"
"What are my preferences for code reviews?"
"Can you list the common issues we've encountered?"
```

#### Memory Reset
```
If memory needs to be reset:
1. Stop the agent/session
2. Delete memory storage directory
3. Restart with fresh memory setup
4. Re-run initial project setup prompts
```

#### Configuration Validation
```
Check memory configuration:
- settings.json exists and is valid JSON
- memory_rules.enabled = true
- storage paths are writable
- retention policies are reasonable
- category limits are appropriate for project size
```

### Getting Help

If troubleshooting doesn't resolve issues:

1. **Check Logs**: Look for memory-related error messages
2. **Verify Configuration**: Ensure all settings are properly set
3. **Test Isolation**: Try memory setup in a clean environment
4. **Community Support**: Check GitHub issues for similar problems
5. **Detailed Bug Reports**: Include configuration, logs, and reproduction steps

## ⚙️ Configuration Options

### Storage Configuration
```json
{
  "memory_rules": {
    "enabled": true,
    "max_entries_per_category": 100,
    "retention_days": 90,
    "auto_cleanup": true
  }
}
```

### Category-Specific Settings
```json
{
  "categories": {
    "technical": {
      "enabled": true,
      "retention_days": 180,
      "priority": "high"
    },
    "personal": {
      "enabled": true,
      "retention_days": 365,
      "encryption": true
    }
  }
}
```

## 🔄 Integration with Other Rules

### RAG Rules Synergy
- Memory provides personalized context for information retrieval
- RAG optimizes memory search and relevance scoring
- Combined system creates intelligent knowledge retrieval

### Critical Thinking Rules Enhancement
- Memory stores error corrections and learning insights
- Critical thinking validates memory accuracy and consistency
- Self-improving system through validated memory updates

### Bootstrap Coordination
- Memory initialization follows bootstrap loading sequence
- Interconnects with other rules through shared context
- Maintains system-wide consistency and coherence

## 📊 Performance & Storage

### Storage Requirements
- **Base Memory**: ~10MB for typical usage
- **Extended Usage**: Scales with conversation volume
- **Compression**: Automatic compression for large memories
- **Backup**: Automatic backup before cleanup operations

### Performance Characteristics
- **Access Speed**: Sub-second retrieval for recent memories
- **Search Performance**: Fast full-text search across all categories
- **Indexing**: Automatic indexing for quick lookups
- **Cleanup**: Background cleanup doesn't impact performance

## 🔧 Troubleshooting

### Memory Not Persisting
```
Symptom: Information forgotten between sessions
Solution: Check storage path permissions and available disk space
```

### Slow Performance
```
Symptom: Memory operations taking too long
Solution: Reduce max_entries_per_category or enable compression
```

### Memory Conflicts
```
Symptom: Inconsistent or conflicting information
Solution: Review retention policies and cleanup frequency
```

## 📚 Related Documentation

- **[RULES.md.en](RULES.md.en)** - Technical algorithm specifications
- **[settings.json](settings.json)** - Configuration options reference
- **[../CORE-RULES.md](../CORE-RULES.md)** - Framework architecture overview
- **[../docs/USER-GUIDE.md](../docs/USER-GUIDE.md)** - Basic setup instructions

## 🤝 Contributing

Found issues or have suggestions for memory functionality?

- **Bug Reports**: [GitHub Issues](../../issues)
- **Feature Requests**: [GitHub Discussions](../../discussions)
- **Code Contributions**: Submit pull requests with memory improvements

---

**🧠 Memory Rules**: Giving AI agents the gift of remembering, learning, and growing with each interaction.

*Copyright (c) 2025 Paulus Ery Wasito Adhi. Licensed under the MIT License.*
