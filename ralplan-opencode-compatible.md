# Ralplan Skill - Oh-My-OpenCode Compatible Specification

This document defines the requirements for a `/ralplan` skill that is compatible with oh-my-opencode and model-agnostic.

---

## 1. Core Principle: Use Native Task Delegation

### 1.1. Mandatory Tool Usage

**MUST use `task()` tool** for all agent delegation. Never reference MCP tools that may not exist.

```typescript
// ✅ CORRECT: Native task delegation
task(
  subagent_type="oracle",
  load_skills=[],
  run_in_background=false,
  prompt="..."
)

// ❌ WRONG: MCP tool that may not exist
ask_codex(agent_role: "architect", ...)
mcp__x__ask_codex(agent_role: "critic", ...)
```

### 1.2. Available Subagent Types

The skill MUST only reference subagent types that are universally available:

| Subagent Type | Purpose | Category |
|---------------|---------|----------|
| `oracle` | Architecture, debugging, expert consultation | consultant |
| `explore` | Fast codebase search, pattern discovery | search |
| `librarian` | External documentation, web research | research |
| `metis` | Pre-planning analysis, ambiguity detection | analyst |
| `momus` | Plan review, quality verification | reviewer |

### 1.3. Category-Based Delegation (Alternative)

For domain-specific work, use category-based delegation:

```typescript
task(
  category="visual-engineering",  // or: ultrabrain, deep, quick, artistry, writing
  load_skills=[],
  run_in_background=true,
  prompt="..."
)
```

---

## 2. Model Agnosticism

### 2.1. Never Hardcode Model Names

**MUST NOT** reference specific models in skill documentation.

```markdown
<!-- ❌ WRONG -->
Use `gpt-5.4` for architecture review

<!-- ✅ CORRECT -->
Use `oracle` subagent for architecture review (model configured in oh-my-opencode.json)
```

### 2.2. Reference Configuration, Not Models

All model configuration should be externalized to `oh-my-opencode.json`:

```json
{
  "agents": {
    "oracle": {
      "model": "<configured-by-user>",
      "reasoningEffort": "high",
      "mode": "subagent",
      "category": "consultant"
    }
  }
}
```

### 2.3. Reasoning Effort Guidance

Document reasoning effort expectations, not model names:

| Task Type | Recommended Reasoning Effort | How to Achieve |
|-----------|------------------------------|----------------|
| Architecture review | high/xhigh | Use `oracle` subagent |
| Quick search | minimal/low | Use `explore` subagent |
| Complex logic | high | Use `category="ultrabrain"` |
| UI/UX work | medium/high | Use `category="visual-engineering"` |

---

## 3. Consensus Workflow Specification

### 3.1. Sequential Agent Calls (CRITICAL)

**Steps 3 and 4 MUST run sequentially.** Never parallelize Architect and Critic calls.

```
Step 1: Planner creates initial plan
Step 2: (optional) User feedback
Step 3: Architect reviews ← WAIT FOR COMPLETION
Step 4: Critic evaluates ← RUN ONLY AFTER STEP 3
Step 5: Re-review loop (if needed)
Step 6: Apply improvements
Step 7: Final approval
```

### 3.2. Architect Review Implementation

```typescript
// Step 3: Architect review
task(
  subagent_type="oracle",
  load_skills=[],
  run_in_background=false,  // BLOCKING - must wait
  prompt=`Review this plan for architectural soundness:

  **Plan**: {plan_content}

  **Requirements**:
  1. Provide strongest steelman counterargument (antithesis)
  2. Identify at least one meaningful tradeoff tension
  3. If possible, suggest synthesis path
  4. In deliberate mode: flag principle violations

  Return verdict: APPROVE, ITERATE, or REJECT with specific feedback.`
)
```

### 3.3. Critic Evaluation Implementation

```typescript
// Step 4: Critic evaluation (ONLY after step 3 completes)
task(
  subagent_type="oracle",
  load_skills=[],
  run_in_background=false,  // BLOCKING - must wait
  prompt=`Evaluate this plan against quality criteria:

  **Plan**: {plan_content}
  **Architect Feedback**: {architect_feedback}

  **Verify**:
  1. Principle-option consistency
  2. Fair alternative exploration
  3. Risk mitigation clarity
  4. Testable acceptance criteria
  5. Concrete verification steps

  Return verdict: APPROVE, ITERATE, or REJECT with specific feedback.`
)
```

---

## 4. Timeout Configuration

### 4.1. Environment Variables

Document configurable timeouts (do not hardcode):

| Variable | Default | Description |
|----------|---------|-------------|
| `OMX_CONSENSUS_AGENT_TIMEOUT_MS` | 120000 | Per-agent call timeout |
| `OMX_CONSENSUS_TOTAL_TIMEOUT_MS` | 600000 | Total workflow timeout |
| `OMX_ASK_USER_TIMEOUT_MS` | 300000 | User response timeout |
| `OMX_CONSENSUS_MAX_REVIEW_ITERATIONS` | 5 | Max re-review loops |
| `OMX_CONSENSUS_CIRCUIT_BREAKER_THRESHOLD` | 3 | Same error recurrence limit |

### 4.2. Timeout Handling

```typescript
// Document fallback behavior, don't implement MCP-specific handling
// If agent call exceeds timeout:
// 1. Log timeout event with agent role and duration
// 2. Fall back to local analysis
// 3. Continue workflow with fallback result
```

---

## 5. Skill File Structure

### 5.1. Required Files

```
.agents/skills/ralplan/
├── SKILL.md          # Main skill documentation
└── (optional supporting files)

.codex/skills/ralplan/
├── SKILL.md          # Symlink or copy of above
└── (optional supporting files)
```

### 5.2. SKILL.md Frontmatter

```yaml
---
name: ralplan
description: Consensus planning with Planner/Architect/Critic loop
---
```

### 5.3. Required Sections in SKILL.md

1. **Purpose** - What the skill does
2. **Usage** - How to invoke it
3. **Flags** - Available options (`--interactive`, `--deliberate`)
4. **Workflow** - Step-by-step process
5. **Tool Usage** - Mandatory `task()` patterns
6. **Timeout Configuration** - Environment variables
7. **Examples** - Concrete usage examples

---

## 6. Tool Usage Section Template

```markdown
<Tool_Usage>
- Use `task(subagent_type="oracle", ...)` with `run_in_background=false` for expert consultation
- Use `task(subagent_type="explore", ...)` with `run_in_background=true` for codebase search
- Use `task(subagent_type="librarian", ...)` with `run_in_background=true` for external research
- Use `task(category="visual-engineering", ...)` for UI/UX work
- Use `task(category="ultrabrain", ...)` for hard logic problems
- Use `task(category="quick", ...)` for trivial changes
- ALWAYS include `load_skills=[]` parameter
- ALWAYS include `run_in_background` parameter (true for parallel, false for blocking)
- **CRITICAL**: Consensus mode agent calls MUST be sequential
- If oracle subagent is unavailable, fall back to local analysis
</Tool_Usage>
```

---

## 7. Anti-Patterns to Avoid

### 7.1. MCP Tool References

```markdown
<!-- ❌ NEVER USE -->
- Use `ask_codex` with `agent_role: "architect"`
- Use `mcp__x__ask_codex` with `agent_role: "critic"`
- Call `ToolSearch("mcp")` to discover MCP tools
```

### 7.2. Model-Specific Instructions

```markdown
<!-- ❌ NEVER USE -->
- Use GPT-5.4 for architecture review
- Use Claude for analysis
- Model X is better for Y task
```

### 7.3. Hardcoded Timeouts

```markdown
<!-- ❌ NEVER USE -->
- Wait 120 seconds for agent response
- Timeout after 2 minutes
```

### 7.4. Parallel Consensus Calls

```typescript
// ❌ NEVER DO THIS
// Running Architect and Critic in parallel
task(subagent_type="oracle", run_in_background=true, ...)  // Architect
task(subagent_type="oracle", run_in_background=true, ...)  // Critic

// ✅ CORRECT: Sequential calls
task(subagent_type="oracle", run_in_background=false, ...)  // Architect
// WAIT for result
task(subagent_type="oracle", run_in_background=false, ...)  // Critic
```

---

## 8. Fallback Strategy

### 8.1. When Subagent Unavailable

```markdown
If `task(subagent_type="oracle", ...)` fails or is unavailable:
1. Log the failure
2. Perform local analysis using available tools (read, grep, glob)
3. Continue workflow with local analysis result
4. Note in output that expert consultation was unavailable
```

### 8.2. Graceful Degradation

```markdown
Consensus workflow degradation path:
1. Try: task(subagent_type="oracle", ...)
2. Fallback: Local analysis with read/grep/glob
3. Fallback: Use category="deep" for autonomous analysis
4. Last resort: Present plan with "expert review unavailable" warning
```

---

## 9. Configuration Requirements

### 9.1. oh-my-opencode.json Requirements

The skill expects these agents to be configured:

```json
{
  "agents": {
    "oracle": {
      "mode": "subagent",
      "category": "consultant",
      "tools": { "read": true, "grep": true, "glob": true }
    },
    "explore": {
      "mode": "subagent",
      "category": "search",
      "tools": { "read": true, "grep": true, "glob": true }
    },
    "librarian": {
      "mode": "subagent",
      "category": "research",
      "tools": { "webfetch": true, "websearch": true, "read": true }
    }
  }
}
```

### 9.2. Category Requirements

```json
{
  "categories": {
    "visual-engineering": { ... },
    "ultrabrain": { ... },
    "deep": { ... },
    "quick": { ... },
    "artistry": { ... },
    "writing": { ... }
  }
}
```

---

## 10. Testing Checklist

Before deploying a ralplan skill, verify:

- [ ] No `ask_codex` or `mcp__x__ask_codex` references
- [ ] No hardcoded model names
- [ ] All agent calls use `task()` tool
- [ ] All `task()` calls include `load_skills=[]`
- [ ] All `task()` calls include `run_in_background` parameter
- [ ] Architect and Critic calls are documented as sequential
- [ ] Timeout configuration references environment variables
- [ ] Fallback strategy documented for unavailable subagents
- [ ] No parallel execution of consensus steps 3 and 4
- [ ] Configuration requirements documented

---

## 11. Example: Complete Consensus Workflow

```typescript
// Step 1: Planner creates initial plan (local)
const plan = generateInitialPlan(task, context);

// Step 2: (optional) User feedback
if (interactive) {
  const feedback = await askUserQuestion(plan);
  if (feedback === "request_changes") {
    return step1(); // Loop back
  }
}

// Step 3: Architect review (BLOCKING)
const architectResult = await task({
  subagent_type: "oracle",
  load_skills: [],
  run_in_background: false,
  prompt: `Review plan for architectural soundness: ${plan}`
});

// Step 4: Critic evaluation (BLOCKING, after step 3)
const criticResult = await task({
  subagent_type: "oracle",
  load_skills: [],
  run_in_background: false,
  prompt: `Evaluate plan quality: ${plan}\nArchitect feedback: ${architectResult}`
});

// Step 5: Re-review loop (if needed)
let iterations = 0;
while (criticResult.verdict !== "APPROVE" && iterations < 5) {
  iterations++;
  // Revise plan based on feedback
  plan = revisePlan(plan, architectResult, criticResult);
  
  // Sequential re-review
  const archResult = await task({ subagent_type: "oracle", ... });
  const critResult = await task({ subagent_type: "oracle", ... });
}

// Step 6: Apply improvements
const finalPlan = applyImprovements(plan, architectResult, criticResult);

// Step 7: Output or handoff
if (interactive) {
  const choice = await askUserQuestion(finalPlan);
  if (choice === "approve_ralph") {
    invokeSkill("ralph", finalPlan);
  } else if (choice === "approve_team") {
    invokeSkill("team", finalPlan);
  }
} else {
  output(finalPlan);
}
```

---

## 12. Migration Guide

### From Codex CLI to Oh-My-OpenCode

| Before (Codex CLI) | After (Oh-My-OpenCode) |
|--------------------|------------------------|
| `ask_codex(agent_role: "architect")` | `task(subagent_type="oracle", ...)` |
| `ask_codex(agent_role: "critic")` | `task(subagent_type="oracle", ...)` |
| `ask_codex(agent_role: "analyst")` | `task(subagent_type="metis", ...)` |
| `ToolSearch("mcp")` | Remove - not needed |
| `mcp__x__ask_codex` | `task(subagent_type="oracle", ...)` |
| Hardcoded timeouts | Environment variables |
| Model references | Configuration references |

---

## Summary

A ralplan skill compatible with oh-my-opencode must:

1. **Use native `task()` delegation** - Never reference MCP tools
2. **Be model-agnostic** - Reference configuration, not models
3. **Follow sequential consensus** - Architect before Critic, never parallel
4. **Include mandatory parameters** - `load_skills=[]`, `run_in_background`
5. **Document timeouts** - Use environment variables, not hardcoded values
6. **Provide fallback** - Local analysis when subagents unavailable
7. **Specify configuration requirements** - Document expected agents/categories

This ensures the skill works across different oh-my-opencode configurations regardless of the underlying models.
