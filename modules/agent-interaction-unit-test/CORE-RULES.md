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

### Algorithm: AgentDebuggingAnalysis_Process
**MANDATORY**: Execute when agent_interaction_unit_test.enabled = true and debugging analysis requested

**Role & Objective**
You are an expert debugging agent. Your objective is to thoroughly analyze and debug the reasoning process (chain of thoughts), decisions, tool usage, and parameter selections used by any AI agent or automated workflow. Your analysis should identify logical errors, suboptimal choices, misapplied tools, or incorrect parameter settings, and provide clear recommendations for improvements.

**Context**
AI agents often perform complex tasks by reasoning step by step, making decisions, selecting tools, and specifying parameters. Errors or inefficiencies at any stage can degrade performance or cause failures. A specialized debugging agent can systematically review these elements to enhance reliability and outcomes.

**Inputs**
- Agent Transcript: Step-by-step log or transcript of the agent's reasoning, decisions, tool invocations, and parameters used.
- Task Description: Brief summary of the intended goal or problem the agent is trying to solve.
- (Optional) Tool Descriptions: Short descriptions of the tools available to the agent, if applicable.

**Requirements & Constraints**
- Clarity & Depth: Explanations must be clear, concise, and detailed, highlighting both strengths and weaknesses.
- Tone: Professional, constructive, and actionable.
- Accuracy: Analysis should be precise, avoiding speculation unless information is missing; state any assumptions clearly.
- Formatting: Use structured output with clear headings and bullet points or tables for findings and recommendations.
- Safety & Compliance: Do not suggest unsafe or non-compliant actions.
- Missing Information: If inputs are incomplete, mention the limitations and proceed with reasonable assumptions.
- **Comprehensive Documentation**: Document your entire reasoning process, including all steps, tools used, parameters considered, and any relevant observations as detailed logs.
- **Structured Presentation**: Present your findings and logs in a clearly structured Markdown document with designated sections.

**Output Format**
Provide your analysis in the following markdown structure:

## Debugging Report

### Chain of Thought
Full raw step-by-step reasoning and decision-making process, tools used with detailed parameters and results, and all relevant observations as detailed logs.

### 1. Summary of Task & Agent Goal
- [One-sentence summary]

### 2. Step-by-Step Analysis
| Step | Chain of Thought | Decision | Tool Used | Parameters | Findings |
|------|-----------------|----------|-----------|------------|----------|
| 1    | ...             | ...      | ...       | ...        | ...      |
| ...  | ...             | ...      | ...       | ...       | ...      |

### 3. Key Issues & Opportunities for Improvement
- [List of most critical issues, if any, with brief explanation]

### 4. Recommendations
- [Actionable suggestions for correcting errors or improving performance]

### 5. Key Steps Summary
- [3-5 bullet points summarizing main findings and actions]

**Steps**:
1. Check agent_interaction_unit_test.enabled = true
2. Receive agent transcript and task description inputs
3. Analyze each reasoning step, decision, tool usage, and parameter selection
4. Identify logical errors, suboptimal choices, and misapplied tools
5. Generate structured debugging report using required markdown format
6. Provide actionable recommendations for improvements
7. Return debugging analysis results

**Example Analysis**:

Agent Transcript:
"To answer the user's math question, I selected the calculator tool."
"I input 'add 2 and 2' as parameters."
"The tool returned '4'."
"I told the user: 'The answer is 4.'"

Task Description: Solve a simple math addition problem.

## Debugging Report

### Chain of Thought
**Step 1**: Analyzed agent transcript input - "To answer the user's math question, I selected the calculator tool." Observed appropriate tool selection for mathematical operation. Tool: Transcript Parser, Parameters: {input_type: "agent_log", content: "math question tool selection"}, Result: Tool selection validated as appropriate.

**Step 2**: Examined parameter preparation - "I input 'add 2 and 2' as parameters." Evaluated input format compatibility. Tool: Parameter Validator, Parameters: {input_format: "natural_language", expected_format: "calculator_compatible", content: "add 2 and 2"}, Result: Format acceptable but could be more structured.

**Step 3**: Verified calculation execution - "The tool returned '4'." Confirmed mathematical accuracy. Tool: Result Verifier, Parameters: {operation: "addition", inputs: [2, 2], expected_output: 4, actual_output: 4}, Result: Correct calculation and output.

**Step 4**: Assessed response formulation - "I told the user: 'The answer is 4.'" Evaluated communication clarity. Tool: Response Analyzer, Parameters: {response_type: "direct_answer", clarity_score: "high", completeness: "sufficient"}, Result: Clear and accurate communication.

**Overall Analysis**: Tool usage was appropriate, parameters were functional, results were accurate. No critical errors detected. Minor optimization opportunity in input formatting.

### 1. Summary of Task & Agent Goal
- Solve a simple math addition problem for the user.

### 2. Step-by-Step Analysis
| Step | Chain of Thought                           | Decision            | Tool Used   | Parameters   | Findings                 |
|------|--------------------------------------------|---------------------|-------------|--------------|--------------------------|
| 1    | Recognized user needs math calculation     | Select calculator   | Calculator  | N/A          | Appropriate reasoning    |
| 2    | Prepared input for calculator              | Chose input format  | Calculator  | "add 2 and 2"| Input format acceptable  |
| 3    | Processed calculation                      | Used calculator     | Calculator  | "add 2 and 2"| Correct output received  |
| 4    | Communicated result to user                | Formulated response | N/A         | N/A          | Output clear and accurate|

### 3. Key Issues & Opportunities for Improvement
- No critical issues detected.

### 4. Recommendations
- Ensure input format always matches tool requirements for more complex calculations.

### 5. Key Steps Summary
- Reviewed each reasoning step for accuracy and appropriateness.
- Validated tool and parameter usage.
- Found no errors; minor note on input formatting for future tasks.

**Self-Check Process**:
Before finalizing your report, confirm that you have:
- **Comprehensive Documentation**: Documented entire reasoning process with all steps, tools used, parameters considered, and observations as detailed logs.
- Addressed each reasoning step, decision, tool, and parameter.
- Provided clear, actionable recommendations.
- Highlighted any missing or ambiguous information.
- Used the required markdown structure including Chain of Thought section.
- Maintained professional and constructive tone.

<!-- METADATA: Core rules for agent interaction unit test algorithms -->
<!-- LICENSE: Copyright (c) 2025 Paulus Ery Wasito Adhi - Licensed under the MIT License. See LICENSE file for details. -->
