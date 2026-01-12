# Agent Coordination Guidelines - Multi-Agent Workflows

## Overview

This guide provides detailed guidelines for coordinating multiple agents in Cursor 2.0 using the Agentic Rules Framework. It covers delegation patterns, communication protocols, and best practices for orchestrator-sub-agent workflows.

## Coordination Principles

### Framework-Based Coordination

All agent coordination follows the Agentic Rules Framework:

1. **Bootstrap Compliance**: Respect `bootstrap.json` loading sequence
2. **Rule Priorities**: Follow rule priority hierarchy (high → medium → low)
3. **Rule Interconnections**: Use framework-defined data flows
4. **Settings Respect**: Only use enabled rule modules
5. **Transparency**: Log all coordination decisions

### Task Decomposition Strategy

#### Phase 1: Planning
- **Orchestrator**: Creates technical plan using Plan Mode (`Shift + Tab`)
- **Global Context**: Uses `@Codebase` for full project understanding
- **Framework Check**: Verifies framework initialization and enabled rules

#### Phase 2: Delegation
- **Rule-Based**: Delegates based on framework rule priorities
- **Parallel Execution**: Uses Git Worktrees for independent tasks
- **Context Sharing**: Provides relevant framework context to sub-agents

#### Phase 3: Execution
- **Sub-Agents**: Execute specialized tasks using framework modules
- **Framework Algorithms**: Implement required algorithms from `AGENTS.md` files
- **Quality Assurance**: Critical Thinking validates all outputs

#### Phase 4: Synthesis
- **Result Combination**: Orchestrator combines sub-agent outputs
- **Rule Interconnections**: Applies framework data flow patterns
- **Final Validation**: Critical Thinking validates final results

## Delegation Patterns

### Pattern 1: Information Gathering

**Use Case**: Need comprehensive information about codebase

**Delegation Flow**:
```
Orchestrator
  ├── RAG Specialist: Semantic search and context optimization
  ├── Memory Specialist: Retrieve relevant context from memory
  └── Critical Thinking Specialist: Validate information quality
```

**Framework Rules**:
- RAG Rules: Context optimization (high priority)
- Memory Rules: Context retrieval (medium priority)
- Critical Thinking Rules: Quality validation (high priority)

### Pattern 2: Feature Implementation

**Use Case**: Implement new feature with tests and documentation

**Delegation Flow**:
```
Orchestrator
  ├── RAG Specialist: Analyze similar patterns (parallel)
  ├── Memory Specialist: Retrieve previous work (parallel)
  ├── Implementation Agent: Create feature code (parallel worktree)
  ├── Testing Specialist: Create tests (parallel worktree)
  ├── Critical Thinking Specialist: Validate implementation
  └── Documentation Specialist: Generate documentation
```

**Framework Rules**:
- All rules active
- Parallel execution via Git Worktrees
- Quality assurance before synthesis

### Pattern 3: Code Review

**Use Case**: Review code for quality and potential issues

**Delegation Flow**:
```
Orchestrator
  ├── RAG Specialist: Gather code context
  ├── Memory Specialist: Retrieve review patterns
  ├── Critical Thinking Specialist: Validate quality
  └── Testing Specialist: Verify test coverage
```

**Framework Rules**:
- Critical Thinking Rules: Primary validation (high priority)
- Memory Rules: Pattern matching (medium priority)
- RAG Rules: Context gathering (high priority)

### Pattern 4: Documentation Generation

**Use Case**: Create comprehensive documentation

**Delegation Flow**:
```
Orchestrator
  ├── RAG Specialist: Gather information
  ├── Memory Specialist: Retrieve documentation patterns
  ├── Documentation Specialist: Generate documentation
  └── Critical Thinking Specialist: Validate accuracy
```

**Framework Rules**:
- RAG Rules: Information gathering (high priority)
- Memory Rules: Pattern retrieval (medium priority)
- Critical Thinking Rules: Accuracy validation (high priority)

## Communication Protocols

### Orchestrator → Sub-Agent

**Message Format**:
```
Task: [Clear, specific task description]
Context: [Relevant framework context]
Priority: [High/Medium/Low based on rule priorities]
Framework Module: [Which rule module to use]
Expected Output: [What the orchestrator expects]
```

**Example**:
```
Task: Retrieve all authentication-related code patterns
Context: User implementing new auth system, similar to previous OAuth implementation
Priority: High (RAG Rules)
Framework Module: rag-rules
Expected Output: Ranked list of relevant code sections with context
```

### Sub-Agent → Orchestrator

**Response Format**:
```
Status: [Success/Partial/Failure]
Output: [Task results]
Framework Applied: [Which algorithms were used]
Quality Score: [If Critical Thinking validated]
Next Steps: [Suggestions for follow-up]
```

**Example**:
```
Status: Success
Output: Found 15 relevant code sections, ranked by relevance
Framework Applied: Context_Optimization_Process, Information_Retrieval_Process
Quality Score: 0.92 (validated by Critical Thinking)
Next Steps: Consider Memory storage for future retrieval
```

### Sub-Agent → Sub-Agent

**Via Framework Rules**:
- **Memory → RAG**: Share session context through Memory Rules
- **RAG → Memory**: Provide optimized context chunks
- **Critical Thinking → Memory**: Store error corrections
- **Memory → Critical Thinking**: Provide user patterns

## Rule Interconnection Patterns

### Error Correction Flow

```
Critical Thinking Specialist detects error
  ↓
Error stored in Memory (error_to_memory interconnection)
  ↓
Memory provides correction context to RAG
  ↓
RAG uses correction for future queries
```

### Context Enhancement Flow

```
RAG Specialist optimizes context
  ↓
Optimized chunks stored in Memory (rag_to_memory_design)
  ↓
Memory provides enhanced context to RAG queries
  ↓
RAG uses enhanced context for better retrieval
```

### Quality Assurance Flow

```
RAG Specialist retrieves information
  ↓
Critical Thinking validates quality (ground_check_to_rag)
  ↓
Quality scores stored in Memory
  ↓
Memory uses quality scores for future retrieval
```

## Best Practices

### Orchestrator Best Practices

1. **Always Plan First**: Use Plan Mode (`Shift + Tab`) for complex tasks
2. **Global Context**: Use `@Codebase` before delegating
3. **Clear Delegation**: Provide specific, actionable tasks
4. **Monitor Progress**: Check worktree status regularly
5. **Quality Review**: Always validate with Critical Thinking
6. **Framework Compliance**: Follow bootstrap loading sequence
7. **Transparency**: Log all coordination decisions

### Sub-Agent Best Practices

1. **Framework First**: Check framework status before operations
2. **Algorithm Implementation**: Use algorithms from `AGENTS.md` files
3. **Settings Respect**: Only use enabled rule modules
4. **Quality Standards**: Apply Critical Thinking validation
5. **Context Sharing**: Use Memory Rules for context
6. **Error Handling**: Admit errors immediately and correct
7. **Transparency**: Log all operations

### Coordination Best Practices

1. **Parallel Execution**: Use Git Worktrees for independent tasks
2. **Rule Priorities**: Respect framework rule priorities
3. **Rule Interconnections**: Follow framework data flows
4. **Memory Sharing**: Use Memory Rules for context
5. **Quality Assurance**: Validate all outputs
6. **Error Recovery**: Use framework error handling
7. **Transparency**: Log all coordination activities

## Quality Assurance

### Pre-Delegation Checks

- [ ] Framework initialized
- [ ] Required rules enabled
- [ ] Task clearly defined
- [ ] Context provided
- [ ] Priority assigned

### During Execution

- [ ] Sub-agents using framework algorithms
- [ ] Rule interconnections active
- [ ] Quality validation ongoing
- [ ] Progress monitored
- [ ] Errors handled

### Post-Synthesis

- [ ] All outputs validated
- [ ] Framework rules applied
- [ ] Quality scores acceptable
- [ ] Errors corrected
- [ ] Results logged

## Error Handling

### Framework Errors

**Error**: Framework not initialized
- **Action**: Initialize framework first
- **Check**: Verify `.agentic_initialized` marker

**Error**: Required rule not enabled
- **Action**: Enable rule in settings or use alternative
- **Check**: Review `settings/global-settings.json`

**Error**: Invalid configuration
- **Action**: Use default settings, log warning
- **Check**: Validate JSON syntax

### Agent Errors

**Error**: Sub-agent task failure
- **Action**: Retry with different approach or delegate to alternative agent
- **Check**: Review sub-agent logs

**Error**: Quality validation failure
- **Action**: Request Critical Thinking review, correct errors
- **Check**: Review validation scores

**Error**: Memory storage failure
- **Action**: Fall back to session-only memory
- **Check**: Verify storage path permissions

## Monitoring and Logging

### Framework Logs

Location: `logs/rule-applications/` (configurable)

Logs include:
- Agent coordination decisions
- Rule applications
- Quality validation results
- Error corrections
- Memory operations

### Agent Logs

Each agent logs:
- Task received
- Framework algorithms used
- Operations performed
- Results generated
- Quality scores

### Coordination Logs

Orchestrator logs:
- Task decomposition
- Delegation decisions
- Sub-agent coordination
- Result synthesis
- Quality validation

## Examples

### Example 1: Complex Feature Implementation

```
User Request: "Implement user authentication with OAuth, tests, and docs"

Orchestrator Plan:
1. Gather context (RAG + Memory)
2. Implement auth (parallel worktree)
3. Create tests (parallel worktree)
4. Generate docs
5. Validate quality
6. Synthesize results

Delegation:
- RAG: Find OAuth patterns
- Memory: Retrieve previous auth work
- Implementation: Create OAuth code
- Testing: Create test suite
- Docs: Generate documentation
- Critical Thinking: Validate all

Framework Rules:
- RAG: Context optimization
- Memory: Pattern retrieval
- Critical Thinking: Quality validation
- All: Rule interconnections active
```

### Example 2: Code Review

```
User Request: "Review this PR for security and quality"

Orchestrator Plan:
1. Gather PR context
2. Analyze security
3. Validate quality
4. Check tests
5. Generate review

Delegation:
- RAG: Gather PR context
- Memory: Retrieve security patterns
- Critical Thinking: Validate quality
- Testing: Verify test coverage

Framework Rules:
- Critical Thinking: Primary (high priority)
- RAG: Context gathering (high priority)
- Memory: Pattern matching (medium priority)
```

## References

- **Framework Documentation**: `docs/CORE-RULES.md`
- **Cursor 2.0 Integration**: `docs/CURSOR-2.0-INTEGRATION.md`
- **Bootstrap Guide**: `Bootstrap.md`
- **Agent Configuration Generator**: `setup.html` (generates `.cursor/agents/*.md` files)
- **Bootstrap Configuration**: `bootstrap.json`

**Note**: Agent configuration files (`.cursor/agents/*.md`) are auto-generated by `setup.html`. Users should generate them using the installer rather than creating them manually.

---

**Framework Version**: 1.3.0  
**Last Updated**: 2026-01-12
