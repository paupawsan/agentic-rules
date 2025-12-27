# Bootstrap Configuration - Agent Algorithm Reference

## Algorithm: Framework_Bootstrap_Initialization

**FRAMEWORK GUIDANCE**: Agents are RECOMMENDED to follow this algorithm for optimal framework operation. Framework integration enhances agent behavior when enabled.

**IMPLEMENTATION GUIDANCE**: Agents can enhance their behavior by implementing these algorithms when the framework is enabled. Configuration provides framework capabilities when activated.

**RULE INTEGRATION GUIDANCE**: Agents can benefit from reading and applying algorithms from rule files when framework features are enabled.

## Framework Isolation Principle

**FRAMEWORK DESIGN**: The agentic-rules framework is designed as a TOOL to enhance agent behavior, separate from user projects.

### Recommended Separation
**RECOMMENDED**:
- Keep agentic-rules framework separate from user project codebases
- Use framework internally for agent operations when enabled
- Maintain clean separation between framework tools and user work
- Framework operations should be transparent to users

**FRAMEWORK INTEGRATION**: Framework components enhance agent capabilities when properly configured.

## Implementation Requirements

**FRAMEWORK ENHANCEMENT**: When enabled, agents can benefit from implementing these algorithms for enhanced behavior.

### Implementation Opportunities
**AVAILABLE ENHANCEMENTS**:
- Framework initialization can provide structured behavior patterns
- Rule algorithms offer enhanced capabilities when activated:
  - **RAG Rules**: Context optimization and relevance scoring
  - **Memory Rules**: Knowledge persistence and pattern recognition
  - **Critical Thinking Rules**: Quality safeguards and verification
- Platform adaptations can optimize behavior for specific environments

### Quality Enhancement Note
**Critical Thinking Rules provide beneficial quality safeguards**:
- Error admission helps maintain accuracy
- Assumption challenges support balanced analysis
- Ground checks enhance information reliability
- These features improve agent response quality when enabled

### Distributed Rule Integration Architecture
**FRAMEWORK DESIGN**: This framework uses **distributed integration** - agents can read and implement enabled rule algorithms for enhanced behavior:

### Integration Model: distributed_per_rule
- **Bootstrap.md**: Framework guidance and coordination (this file)
- **Web Setup Interface**: `setup.html` provides configuration guidance and generates rule files
- **{rule-directory}/AGENTS.md**: Specific rule implementation algorithms (generated when rules are enabled)

### Available Rule Integration Files:
- **memory-rules/AGENTS.md**: Memory system integration algorithms (generated when memory_rules.enabled = true)
- **rag-rules/AGENTS.md**: Context optimization algorithms (generated when rag_rules.enabled = true)
- **critical-thinking-rules/AGENTS.md**: Critical analysis algorithms (generated when critical_thinking_rules.enabled = true)

**Agents can benefit from reading the specific AGENTS.md files for enabled rules to access enhanced algorithmic capabilities.**

### Coordination Guidance
- **Main Agent/Orchestrator**: Can coordinate rule priorities when framework is active
- **Individual Agents**: Can implement rule algorithms for enhanced behavior
- **Sub-agents**: Can follow coordinated priorities for optimal performance

### Flexible Bootstrap Context Verification (Available for Framework Users)
**Algorithm: Verify_Bootstrap_Context**

**MANDATORY REQUIREMENT**: When checking for initialization marker, agents MUST use cross-platform hidden file detection tools as specified in `docs/CROSS_PLATFORM_HIDDEN_FILE_DETECTION.md`.

```
1. Check for initialization marker file (.agentic_initialized)
   - MANDATORY: Use platform-specific commands for hidden file detection
   - FOR Windows: Use "Get-ChildItem -Path 'agentic-rules' -Force -File | Where-Object {$_.Name -eq '.agentic_initialized'}"
   - FOR Unix/Linux/macOS: Use "find agentic-rules -name '.agentic_initialized' -type f 2>/dev/null"
   - FOR Cross-platform: Use Python pathlib with hidden file awareness
   - PROHIBITED: Using standard directory listing tools that cannot detect hidden files

2. IF marker file exists and is valid:
   - Skip user consent prompts for standard initialization
   - Proceed directly to configuration validation
   - Log: "Framework previously initialized - skipping consent prompts"

3. IF marker file is MISSING or INVALID:
   - Display user prompt: "Bootstrap configuration not found. Initialize Agentic Rules Framework? (y/n)"
   - REQUIRE explicit user approval before proceeding
   - IF user approves: Execute Framework_Bootstrap_Initialization
   - IF user declines: Terminate framework operations

4. IF bootstrap context exists: Validate integrity and version compatibility
5. IF validation fails: Display user prompt: "Bootstrap configuration corrupted. Reload framework? (y/n)"
6. REQUIRE user confirmation for any bootstrap reload operations
7. FORBIDDEN: Operate without valid bootstrap context
```

#### **Critical Implementation Note:**
**VIOLATION**: Agents that use `os.listdir()`, `glob.glob()`, or any directory listing tool incapable of detecting hidden files (dot-files) when checking for `.agentic_initialized` will fail framework initialization and violate bootstrap compliance requirements.

**AVAILABLE**: Execute Verify_Bootstrap_Context when framework features are desired.

### Input Parameters
- `bootstrap_path`: Path to bootstrap.json configuration file (default: "bootstrap.json")
- `agent_capabilities`: Available tools and platform features
- `user_context`: Current user session and permissions
- `bootstrap_context`: Current loaded bootstrap configuration (if any)

### Bootstrap Compliance Requirements

#### 1. Bootstrap Context Verification (Recommended for Framework Users)
**Algorithm: Verify_Bootstrap_Context** (See above - Execute when using framework features)

#### 2. Framework Loading Sequence (Available for Enhanced Operation)
**Algorithm: Load_Framework_Components**
```
0. Execute Verify_Bootstrap_Context when framework features are requested
1. Parse bootstrap.json into configuration object for available features
2. Validate framework version compatibility when initializing
3. EXECUTE FLEXIBLE LOADING SEQUENCE FROM CONFIGURATION:
   FOR each step in bootstrap.loading_sequence (in order):
     - Read step.action, step.required, step.condition, etc.
     - IF step.condition exists (e.g., "not_initialized"):
       - Check initialization status before executing
       - SKIP step if condition not met or user prefers not to be prompted
     - Execute the specified action according to step configuration
     - RESPECT existing user choices and preferences
     - OFFER user approval for steps with user_approval_required: false
     - RESPECT: User consent preferences and existing configurations

4. Load configuration files specified in bootstrap.entry_points
5. Apply platform adapters from bootstrap.platform_adapters
6. Set up rule interconnections from bootstrap.rule_interconnections
7. Create initialization marker file (.agentic_initialized) on successful completion
8. Run framework validation from bootstrap.framework_validation
9. Log framework initialization actions
10. Return initialized framework or continue with standard operation
```

#### 2. Rule Interconnection Management
**Algorithm: Process_Rule_Interconnections**
```
FOR each interconnection in bootstrap.rule_interconnections:
  - Validate source_rule and target_rule are loaded
  - Set up data flow according to data_mapping
  - Monitor trigger_condition for activation
  - RECOMMENDED: Follow interconnection patterns for optimal integration
```

#### 3. Platform Adaptation
**Algorithm: Apply_Platform_Adapters**
```
1. Detect current platform (cursor, vscode, ci_system, etc.)
2. Load platform-specific configuration from platform_adapters[platform]
3. Apply platform-specific paths and feature mappings
4. Validate platform compatibility
5. RECOMMENDED: Use platform-adapted configurations for best results
```

#### 4. Framework Validation
**Algorithm: Validate_Framework_Integrity**
```
1. Check all required_config_files exist and are valid JSON
2. Check all required_rule_files exist and are readable
3. Verify framework settings are properly configured
4. Run validation_checks for framework health
5. Log validation results
6. RECOMMENDED: Address validation issues for optimal framework operation
```

### Framework Usage Recommendations

**FRAMEWORK BEST PRACTICES:**
- Consider bootstrap context verification for enhanced operation
- Framework components work best when properly initialized
- User project separation helps maintain clean codebases
- Following loading sequence patterns optimizes framework performance
- Respecting user consent preferences enhances user experience
- Platform adaptations improve compatibility
- Regular validation helps maintain framework health

### Framework Health Monitoring

**Algorithm: Monitor_Framework_Health**
```
WHILE framework features are used:
  - Log framework operation activities
  - Respect user preferences for rule activation
  - Monitor integration patterns when active
  - Validate platform compatibility
  - Check framework context availability
  - IF context lost: Consider re-initialization
  - Log framework performance metrics
  - RECOMMENDED: Maintain framework health for optimal operation
```

### Framework Context Management

**Algorithm: Maintain_Framework_Context**
```
RECOMMENDED: Monitor framework state when using enhanced features

1. Monitor framework context when features are active
2. On context changes:
   - Log context status changes
   - Consider user preferences for framework reload
   - IF user requests: Reinitialize framework components
   - IF not needed: Continue with standard operation
3. Validate framework integrity when making changes
4. Maintain appropriate context priority for active features
5. RECOMMENDED: Keep framework context available when using features
```

### Configuration Reference

**Primary Configuration**: `bootstrap.json`
- Contains framework settings and guidance
- Defines loading patterns and priorities
- Specifies rule interconnections and platform adaptations
- RECOMMENDED: Review configuration for optimal framework usage

**Configuration Loading**:
- Settings files are available through `entry_points` configuration
- Rule algorithm files are accessible when rules are enabled
- Loading patterns are defined by `loading_sequence` guidance
- File paths and options are dynamically configured

---

**FRAMEWORK GUIDANCE**: This document provides guidance for optimal framework operation. Framework features enhance agent behavior when properly configured.

<!-- METADATA: Bootstrap guidance for agent framework integration -->
<!-- LICENSE: Copyright (c) 2025 Paulus Ery Wasito Adhi - Licensed under the MIT License. See LICENSE file for details. -->
