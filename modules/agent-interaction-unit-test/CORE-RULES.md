# Agent Interaction Unit Test Core Rules

## Required Implementation Algorithms

### Algorithm: AgentInteractionUnitTestValidation_Initialization_Process
**MANDATORY**: Execute when agent_interaction_unit_test.enabled = true

**Steps**:
1. Read agent-interaction-unit-test/settings.json
2. Initialize agent interaction unit test validation system
3. Validate test configuration settings
4. Return initialized agent interaction unit test framework

**CRITICAL**: Do NOT auto-enable - respect user's enabled setting.

### Algorithm: GroundCheckValidation_Process
**MANDATORY**: Execute for all information provided during unit testing

**Steps**:
1. Check agent_interaction_unit_test.enabled = true
2. For each information piece provided:
   - Verify source exists and content matches
   - Cross-reference with alternative sources
   - Flag any unverified claims
3. Generate validation report with accuracy score
4. Return ground check results

### Algorithm: AssumptionChallenge_Process
**MANDATORY**: Execute before responding to identify assumptions

**Steps**:
1. Check agent_interaction_unit_test.enabled = true
2. Scan response for implicit assumptions
3. Challenge each assumption with contrary evidence
4. Require explicit validation for unsupported assumptions
5. Return assumption validation results

### Algorithm: ErrorAdmission_Process
**MANDATORY**: Execute immediately when errors detected

**Steps**:
1. Check agent_interaction_unit_test.enabled = true
2. Detect hallucinations or inaccuracies
3. Immediately admit error with evidence
4. Provide corrected information with sources
5. Document prevention measures
6. Return error correction report

### Algorithm: ToolCallAudit_Process
**MANDATORY**: Execute for every tool call during testing

**Steps**:
1. Check agent_interaction_unit_test.enabled = true
2. Log exact function name and parameters
3. Record return data and execution time
4. Perform ground check validation
5. Calculate relevance score with justification
6. Return audited tool call data

### Algorithm: DecisionAudit_Process
**MANDATORY**: Execute for every decision point

**Steps**:
1. Check agent_interaction_unit_test.enabled = true
2. Document alternative options considered
3. Record chosen option with rationale
4. Assess risks and mitigation strategies
5. Validate decision against ground truth
6. Return decision audit trail

### Algorithm: ContextManagementAudit_Process
**MANDATORY**: Execute to monitor context usage

**Steps**:
1. Check agent_interaction_unit_test.enabled = true
2. Monitor context window utilization
3. Track information prioritization decisions
4. Log memory system integration
5. Record optimization actions and impact
6. Return context management metrics

### Algorithm: AgentInteractionUnitTestCompliance_Process
**MANDATORY**: Execute at response completion

**Steps**:
1. Check agent_interaction_unit_test.enabled = true
2. Validate 100% framework compliance
3. Verify 100% ground check coverage
4. Confirm 0% hallucinations detected
5. Assess complete tool transparency
6. Generate agent interaction unit test report with pass/fail criteria
7. Return compliance validation results

<!-- METADATA: Core rules for agent interaction unit test algorithms -->
<!-- LICENSE: Copyright (c) 2025 Paulus Ery Wasito Adhi - Licensed under the MIT License. See LICENSE file for details. -->
