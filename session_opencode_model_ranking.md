# OpenCode Model Ranking Session

**Session ID**: ses_2a8f5ef4fffe4j4L3wntR3DQeK  
**Date**: 2026-04-04  
**Agent**: Sisyphus (Ultraworker)

## Executive Summary

Comprehensive analysis mapping **30 OpenCode agents** to optimal models across **4 sources** (OpenRouter free, OpenCode Go free, NVIDIA Build free, and OpenAI).

## Key Findings

### Top Free Models by Use Case

1. **Qwen3 Coder Next (80B-A3B)** - OpenRouter Free
   - Best for: executor, code-reviewer, build-fixer, git-master
   - Score range: 88-95 across coding agents
   - 70.6% SWE-bench, only 3B active params

2. **DeepSeek R1 (671B-A37B)** - OpenRouter Free
   - Best for: architect, security-reviewer, critic, debugger
   - Score range: 88-93 across reasoning agents
   - Exceptional chain-of-thought reasoning

3. **Qwen3.6 Plus** - OpenRouter Free
   - Best for: analyst, researcher, vision, product-manager
   - Score range: 85-92 across analysis agents
   - 1M context window with vision

4. **Nemotron-3-Super-120B-A12B** - NVIDIA Build Free
   - Best for: planner, team-executor
   - Score range: 85-91 across planning agents
   - Optimized for agentic workflows

5. **Qwen3.5-9B** - OpenRouter Free
   - Best for: explore, style-reviewer
   - Score range: 93-94 across fast agents
   - 161 tok/s, best speed-quality ratio

## Model Sources

### OpenRouter Free Models (28 models)
- Rate limits: 20 req/min, 200 req/day
- Cost: $0 (no credit card required)

### OpenCode Go Free Models (6 models)
- Models: GLM-5, Kimi K2.5, MiMo-V2-Pro, MiMo-V2-Omni, MiniMax M2.5, MiniMax M2.7
- Limits: 1,150-20,000 requests per 5 hours
- Cost: $5 first month, then $10/month

### NVIDIA Build Free Models (91 models)
- Free credits: 5,000 + 4,000 on request
- Specializes: GPU-optimized inference, agentic workflows

### OpenAI Models (Paid)
- Flagship: GPT-5.4, GPT-5.3-Codex-Spark
- Efficient: GPT-5.4-mini, GPT-5.4-nano
- Cost: $2.50-$30 per 1M tokens

## Agent Categories

### Frontier Agents (High Reasoning)
- architect, analyst, planner, security-reviewer
- code-reviewer, test-engineer, critic, code-simplifier
- team-executor

### Standard Agents (Balanced)
- executor, debugger, verifier, quality-reviewer
- api-reviewer, performance-reviewer, dependency-expert
- quality-strategist, build-fixer, designer
- git-master, product-manager, ux-researcher
- information-architect, product-analyst

### Fast-Lane Agents (Speed Priority)
- explore, style-reviewer, writer, researcher
- vision, qa-tester

## Configuration Examples

### Free Tier Setup (OpenRouter)
```json
{
  "agent": {
    "executor": {
      "model": "openrouter/qwen/qwen3-coder-next:free"
    },
    "architect": {
      "model": "openrouter/deepseek/deepseek-r1:free"
    },
    "explore": {
      "model": "openrouter/qwen/qwen3.5-9b:free"
    }
  }
}
```

### OpenCode Go Setup ($5-10/month)
```json
{
  "agent": {
    "executor": {
      "model": "opencode/glm-5"
    },
    "architect": {
      "model": "opencode/glm-5"
    }
  }
}
```

### Paid Setup (OpenAI)
```json
{
  "agent": {
    "executor": {
      "model": "openai/gpt-5.4"
    },
    "architect": {
      "model": "openai/gpt-5.4"
    },
    "explore": {
      "model": "openai/gpt-5.3-codex-spark"
    }
  }
}
```

## Sources

1. OpenCode Documentation. "Agents | OpenCode." *opencode.ai*, 2026.
2. CostGoat. "OpenRouter Free Models: All 28 Listed (Apr 2026)." *costgoat.com*, April 3, 2026.
3. NVIDIA. "Try NVIDIA NIM APIs - Models Catalog." *build.nvidia.com*, 2026.
4. OpenCode. "OpenCode Go | Low cost coding models for everyone." *opencode.ai/go*, 2026.
5. OpenCode. "OpenCode Zen | Reliable optimized models for coding agents." *opencode.ai/zen*, 2026.
6. AGENTS.md Model Capability Table. Lines 255-295.
7. Multiple benchmark sources: SWE-bench, HumanEval, MMLU, LiveCodeBench.

## Conclusion

The open-source ecosystem has matured to the point where free models now compete with or exceed paid alternatives in specific domains. Qwen and DeepSeek lead the charge in coding and reasoning respectively, offering Apache 2.0 licensing for maximum flexibility.

For OpenCode agent workflows, **Qwen3 Coder Next** emerges as the clear winner for free, high-quality coding assistance, while **GPT-5.3-Codex-Spark** leads for speed-critical paid applications.
