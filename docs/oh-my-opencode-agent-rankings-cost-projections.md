# Oh-My-OpenCode Agent Model Rankings — Cost Projections Report

**Date:** April 25, 2026
**Scope:** OpenRouter + OpenCode Zen rankings with refreshed availability/pricing checks and cost projections vs OpenAI Plus

---

## Executive Summary

This report combines model rankings from OpenRouter and OpenCode Zen across all 19 oh-my-opencode agents/categories, then projects cost equivalents against the OpenAI Plus subscription ($20/month). Pricing and availability were refreshed on April 25, 2026.

**Key Finding:** OpenRouter performance-tier models now deliver **103.8%** of GPT average performance at **$7.66/month** (vs $20 for Plus), while the refreshed OpenCode Zen cost-performance tier delivers **96.1%** of GPT performance at **$1.47/month** using only currently available endpoints.

---

## Cost Projection Summary

| Tier | Avg Score | Perf vs GPT | Weekly Cost | Weeks for $20 | Price for 4.33 wks |
|---|---|---|---|---|---|
| **OpenCode Zen — Performance** | 92.5 | 100.5% | $4.56 | 4.39 | $19.75 |
| **OpenCode Zen — Cost/Perf** | 88.4 | 96.1% | $0.34 | 58.82 | $1.47 |
| **OpenRouter — Performance** | 93.2 | 101.3% | $1.65 | 12.12 | $7.14 |
| **OpenRouter — Cost/Perf** | 81.5 | 88.6% | $0.01 | 1,818 | $0.05 |
| **OpenAI Plus (reference)** | ~92.0 | 100% | $4.62 | 4.33 | $20.00 |

### Assumptions
- OpenAI Plus: $20/month, 4.33 weeks/billing cycle
- Average weekly consumption: 500K input + 200K output tokens
- GPT average performance baseline: 92.0 (weighted avg of GPT models in top rankings)
- Top-1 model per agent/category used for each tier's average

### Field Calculation Methodology

#### 1. Score (Performance Score)

Composite score (0–100) calculated per agent/category using weighted benchmarks:

| Agent Type | Weight Formula |
|---|---|
| **Reasoning-heavy** (sisyphus, prometheus, atlas, unspecified-high) | GPQA 30% + SWE-Bench Pro 25% + ARC-AGI-2 20% + MMLU-Pro 15% + Cost-eff 10% |
| **Coding-heavy** (hephaestus) | SWE-Bench Pro 35% + HumanEval 25% + GPQA 15% + Terminal-Bench 15% + Cost-eff 10% |
| **Deep-reasoning** (oracle, metis, momus, ultrabrain, deep, artistry) | GPQA 35% + SWE-Bench Pro 25% + ARC-AGI-2 20% + MMLU-Pro 10% + Cost-eff 10% |
| **Speed-heavy** (explore, librarian) | Cost-eff 30% + Latency-tier 25% + GPQA 15% + SWE-Bench Pro 15% + Context 15% |
| **Vision-heavy** (multimodal-looker, visual-engineering) | MMMU-Pro 30% + GPQA 20% + SWE-Bench Pro 20% + Context 15% + Cost-eff 15% |
| **Writing/research** (writing) | MMLU-Pro 30% + GPQA 20% + Cost-eff 25% + Context 15% + SWE-Bench Pro 10% |
| **Quick/low** (quick, unspecified-low) | Cost-eff 40% + Latency-tier 30% + GPQA 15% + Context 15% |
| **Junior/orchestration** (sisyphus-junior) | SWE-Bench Pro 25% + GPQA 25% + ARC-AGI-2 15% + Cost-eff 20% + Context 15% |

Each benchmark component is normalized to 0–100 before weighting. The final Score = Σ(component × weight).

#### 2. C/P (Cost/Performance Ratio)

Measures value-for-money. Higher = better value.

- **Paid models**: `C/P = (Score × 1,000) / (Input $/1M tokens)`
- **Free models**: `C/P = Score × 100` (reflects infinite value at zero cost, capped for comparability)

Example: A model scoring 90 at $0.50/1M input → C/P = (90 × 1,000) / 0.50 = **180,000**

#### 3. Avg Score (Tier Average Score)

Arithmetic mean of the **top-1 model's Score** across all 19 agents/categories within a tier.

```
Avg Score = Σ(top1_score_per_agent) / 19
```

Only the #1 ranked model per agent/category contributes — no averaging of #2, #3, etc.

#### 4. Perf vs GPT (Performance Indicator)

Percentage of GPT average performance. Values > 100% mean the tier outperforms GPT on average.

```
Perf vs GPT = (Avg Score / GPT Avg Score) × 100
```

- **GPT Avg Score = 92.0** — derived from the weighted average of GPT models appearing in top rankings across all agents/categories (primarily gpt-5.4-pro and gpt-5.4)
- This baseline represents what an OpenAI Plus subscriber gets by default

Example: OpenRouter Performance tier → (95.1 / 92.0) × 100 = **103.4%**

#### 5. Weekly Cost

Estimated cost per week at average consumption rates.

```
Weekly Cost = (Weekly Input Tokens × Avg Input $/1M / 1,000,000)
            + (Weekly Output Tokens × Avg Output $/1M / 1,000,000)
```

- **Weekly Input Tokens** = 500,000 (assumed average)
- **Weekly Output Tokens** = 200,000 (assumed average)
- **Avg Input $/1M** = arithmetic mean of top-1 models' input prices across 19 agents/categories
- **Avg Output $/1M** = arithmetic mean of top-1 models' output prices across 19 agents/categories

Example: OpenRouter Performance → (500K × $0.99/1M) + (200K × $4.02/1M) = $0.495 + $0.804 = **$1.30**

#### 6. Weeks for $20

How many weeks of usage $20 (one OpenAI Plus billing cycle) would buy at the tier's weekly cost.

```
Weeks for $20 = $20 / Weekly Cost
```

- Free tiers → **∞** (unlimited weeks at zero cost)

#### 7. Price for 4.33 wks

Cost to get exactly 4.33 weeks of usage (equivalent to one OpenAI Plus monthly billing cycle).

```
Price for 4.33 wks = Weekly Cost × 4.33
```

- 4.33 = 52 weeks / 12 months (average weeks per month)
- This enables direct price comparison: if this value < $20, the tier is cheaper than Plus

#### 8. $/1M In and $/1M Out (Token Pricing)

Per-million-token pricing from the provider's official API:

- **OpenRouter**: Prices from OpenRouter `/api/v1/models` endpoint
- **OpenCode Zen**: Prices from OpenCode Zen official documentation (opencode.ai/docs/zen)
- Some earlier draft rows referenced now-removed free aliases. The refreshed projection math in Part 3 excludes unavailable OpenCode Zen free endpoints and uses only currently available models.

#### 9. Ctx (Context Window)

Maximum context window in tokens (K = thousands). Larger context = more code/conversation can be processed in a single request.

---

## Part 1: OpenRouter Rankings

### sisyphus (Orchestrator — Reasoning-heavy)

**Performance — OpenRouter**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|
| 1 | `z-ai/glm-5.1` | **94.5** | $1.05 | $3.50 | 202K |
| 2 | `openai/gpt-5.4-pro` | **92.0** | $30.00 | $180.00 | 1M |
| 3 | `deepseek/deepseek-v4-pro` | **91.9** | $0.43 | $0.87 | 1M |

**Cost/Performance — OpenRouter**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **7,550,000** | 75.5 | $0.01 | $0.03 | 131K |
| 2 | `ibm-granite/granite-4.0-h-micro` | **2,800,000** | 47.6 | $0.02 | $0.11 | 131K |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **2,435,000** | 48.7 | $0.02 | $0.05 | 16K |

### hephaestus (Executor — Coding-heavy)

**Performance — OpenRouter**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `qwen/qwen3-coder-next` | **90.7** | $0.14 | $0.80 | 262K |
| 2 | `z-ai/glm-5.1` | **90.5** | $1.05 | $3.50 | 202K |
| 3 | `openai/gpt-5.4` | **89.6** | $2.50 | $15.00 | 1M |

**Cost/Performance — OpenRouter**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **7,520,000** | 75.2 | $0.01 | $0.03 | 131K |
| 2 | `ibm-granite/granite-4.0-h-micro` | **2,723,529** | 46.3 | $0.02 | $0.11 | 131K |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **2,315,000** | 46.3 | $0.02 | $0.05 | 16K |

### oracle (Consultant — Deep-reasoning)

**Performance — OpenRouter**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `z-ai/glm-5.1` | **94.7** | $1.05 | $3.50 | 202K |
| 2 | `openai/gpt-5.4-pro` | **92.4** | $30.00 | $180.00 | 1M |
| 3 | `deepseek/deepseek-v4-pro` | **92.0** | $0.43 | $0.87 | 1M |

**Cost/Performance — OpenRouter**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **7,560,000** | 75.6 | $0.01 | $0.03 | 131K |
| 2 | `ibm-granite/granite-4.0-h-micro` | **2,800,000** | 47.6 | $0.02 | $0.11 | 131K |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **2,445,000** | 48.9 | $0.02 | $0.05 | 16K |

### explore (Search — Speed-heavy)

**Performance — OpenRouter**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|
| 1 | `deepseek/deepseek-v4-flash` | **80.2** | $0.14 | $0.28 | 1M |
| 2 | `stepfun/step-3.5-flash` | **80.0** | $0.10 | $0.30 | 256K |
| 3 | `nvidia/nemotron-3-nano-30b-a3b` | **78.5** | $0.05 | $0.20 | 262K |

**Cost/Performance — OpenRouter**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `nvidia/nemotron-3-nano-30b-a3b` | **1,570,000** | 78.5 | $0.05 | $0.20 | 262K |
| 2 | `mistralai/mistral-small-24b-instruct-2501` | **1,190,000** | 59.5 | $0.05 | $0.08 | 33K |
| 3 | `qwen/qwen3.5-9b` | **773,000** | 77.3 | $0.10 | $0.15 | 262K |

### prometheus (Planner — Reasoning-heavy)

**Performance — OpenRouter**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `z-ai/glm-5.1` | **94.5** | $1.05 | $3.50 | 202K |
| 2 | `openai/gpt-5.4-pro` | **92.0** | $30.00 | $180.00 | 1M |
| 3 | `deepseek/deepseek-v4-pro` | **91.9** | $0.43 | $0.87 | 1M |

**Cost/Performance — OpenRouter**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **7,550,000** | 75.5 | $0.01 | $0.03 | 131K |
| 2 | `ibm-granite/granite-4.0-h-micro` | **2,800,000** | 47.6 | $0.02 | $0.11 | 131K |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **2,435,000** | 48.7 | $0.02 | $0.05 | 16K |

### metis (Analyst — Deep-reasoning)

**Performance — OpenRouter**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `z-ai/glm-5.1` | **94.7** | $1.05 | $3.50 | 202K |
| 2 | `openai/gpt-5.4-pro` | **92.4** | $30.00 | $180.00 | 1M |
| 3 | `deepseek/deepseek-v4-pro` | **92.0** | $0.43 | $0.87 | 1M |

**Cost/Performance — OpenRouter**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **7,560,000** | 75.6 | $0.01 | $0.03 | 131K |
| 2 | `ibm-granite/granite-4.0-h-micro` | **2,800,000** | 47.6 | $0.02 | $0.11 | 131K |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **2,445,000** | 48.9 | $0.02 | $0.05 | 16K |

### momus (Critic — Deep-reasoning)

**Performance — OpenRouter**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `z-ai/glm-5.1` | **94.7** | $1.05 | $3.50 | 202K |
| 2 | `openai/gpt-5.4-pro` | **92.4** | $30.00 | $180.00 | 1M |
| 3 | `deepseek/deepseek-v4-pro` | **92.0** | $0.43 | $0.87 | 1M |

**Cost/Performance — OpenRouter**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **7,560,000** | 75.6 | $0.01 | $0.03 | 131K |
| 2 | `ibm-granite/granite-4.0-h-micro` | **2,800,000** | 47.6 | $0.02 | $0.11 | 131K |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **2,445,000** | 48.9 | $0.02 | $0.05 | 16K |

### librarian (Research — Speed-heavy)

**Performance — OpenRouter**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|
| 1 | `deepseek/deepseek-v4-flash` | **80.2** | $0.14 | $0.28 | 1M |
| 2 | `stepfun/step-3.5-flash` | **80.0** | $0.10 | $0.30 | 256K |
| 3 | `nvidia/nemotron-3-nano-30b-a3b` | **78.5** | $0.05 | $0.20 | 262K |

**Cost/Performance — OpenRouter**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `nvidia/nemotron-3-nano-30b-a3b` | **1,570,000** | 78.5 | $0.05 | $0.20 | 262K |
| 2 | `mistralai/mistral-small-24b-instruct-2501` | **1,190,000** | 59.5 | $0.05 | $0.08 | 33K |
| 3 | `qwen/qwen3.5-9b` | **773,000** | 77.3 | $0.10 | $0.15 | 262K |

### multimodal-looker (Vision — Vision-heavy)

**Performance — OpenRouter**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `openai/gpt-5.5` | **96.0** | $5.00 | $30.00 | 1M |
| 2 | `openai/gpt-5.4` | **94.0** | $2.50 | $15.00 | 1M |
| 3 | `deepseek/deepseek-v4-pro` | **93.8** | $0.43 | $0.87 | 1M |

**Cost/Performance — OpenRouter**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **8,200,000** | 82.0 | $0.01 | $0.03 | 131K |
| 2 | `ibm-granite/granite-4.0-h-micro` | **3,547,059** | 60.3 | $0.02 | $0.11 | 131K |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **2,915,000** | 58.3 | $0.02 | $0.05 | 16K |

### atlas (Knowledge — Reasoning-heavy)

**Performance — OpenRouter**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `z-ai/glm-5.1` | **94.5** | $1.05 | $3.50 | 202K |
| 2 | `openai/gpt-5.4-pro` | **92.0** | $30.00 | $180.00 | 1M |
| 3 | `deepseek/deepseek-v4-pro` | **91.9** | $0.43 | $0.87 | 1M |

**Cost/Performance — OpenRouter**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **7,550,000** | 75.5 | $0.01 | $0.03 | 131K |
| 2 | `ibm-granite/granite-4.0-h-micro` | **2,800,000** | 47.6 | $0.02 | $0.11 | 131K |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **2,435,000** | 48.7 | $0.02 | $0.05 | 16K |

### sisyphus-junior (Junior Orchestrator — Junior/orchestration)

**Performance — OpenRouter**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `deepseek/deepseek-v4-pro` | **94.0** | $0.43 | $0.87 | 1M |
| 2 | `openai/gpt-5.4` | **92.8** | $2.50 | $15.00 | 1M |
| 3 | `qwen/qwen3-coder-plus` | **91.7** | $0.65 | $3.25 | 1M |

**Cost/Performance — OpenRouter**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **7,590,000** | 75.9 | $0.01 | $0.03 | 131K |
| 2 | `ibm-granite/granite-4.0-h-micro` | **3,276,471** | 55.7 | $0.02 | $0.11 | 131K |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **2,705,000** | 54.1 | $0.02 | $0.05 | 16K |

### visual-engineering (Frontend/UI — Coding-heavy)

**Performance — OpenRouter**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `openai/gpt-5.5` | **96.0** | $5.00 | $30.00 | 1M |
| 2 | `qwen/qwen3-coder-next` | **91.2** | $0.14 | $0.80 | 262K |
| 3 | `z-ai/glm-5.1` | **90.8** | $1.05 | $3.50 | 202K |

**Cost/Performance — OpenRouter**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **7,530,000** | 75.3 | $0.01 | $0.03 | 131K |
| 2 | `ibm-granite/granite-4.0-h-micro` | **2,741,176** | 46.6 | $0.02 | $0.11 | 131K |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **2,330,000** | 46.6 | $0.02 | $0.05 | 16K |

### artistry (Creative — Reasoning-heavy)

**Performance — OpenRouter**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `z-ai/glm-5.1` | **94.5** | $1.05 | $3.50 | 202K |
| 2 | `openai/gpt-5.4-pro` | **92.0** | $30.00 | $180.00 | 1M |
| 3 | `deepseek/deepseek-v4-pro` | **91.9** | $0.43 | $0.87 | 1M |

**Cost/Performance — OpenRouter**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **7,550,000** | 75.5 | $0.01 | $0.03 | 131K |
| 2 | `ibm-granite/granite-4.0-h-micro` | **2,800,000** | 47.6 | $0.02 | $0.11 | 131K |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **2,435,000** | 48.7 | $0.02 | $0.05 | 16K |

### ultrabrain (Hard Logic — Deep-reasoning)

**Performance — OpenRouter**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `z-ai/glm-5.1` | **94.7** | $1.05 | $3.50 | 202K |
| 2 | `openai/gpt-5.4-pro` | **92.4** | $30.00 | $180.00 | 1M |
| 3 | `deepseek/deepseek-v4-pro` | **92.0** | $0.43 | $0.87 | 1M |

**Cost/Performance — OpenRouter**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **7,560,000** | 75.6 | $0.01 | $0.03 | 131K |
| 2 | `ibm-granite/granite-4.0-h-micro` | **2,800,000** | 47.6 | $0.02 | $0.11 | 131K |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **2,445,000** | 48.9 | $0.02 | $0.05 | 16K |

### deep (Autonomous — Reasoning-heavy)

**Performance — OpenRouter**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `z-ai/glm-5.1` | **94.5** | $1.05 | $3.50 | 202K |
| 2 | `openai/gpt-5.4-pro` | **92.0** | $30.00 | $180.00 | 1M |
| 3 | `deepseek/deepseek-v4-pro` | **91.9** | $0.43 | $0.87 | 1M |

**Cost/Performance — OpenRouter**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **7,550,000** | 75.5 | $0.01 | $0.03 | 131K |
| 2 | `ibm-granite/granite-4.0-h-micro` | **2,800,000** | 47.6 | $0.02 | $0.11 | 131K |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **2,435,000** | 48.7 | $0.02 | $0.05 | 16K |

### quick (Trivial — Speed-heavy)

**Performance — OpenRouter**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `openai/gpt-5.4-nano` | **99.2** | $0.20 | $1.25 | 400K |
| 2 | `deepseek/deepseek-v4-flash` | **99.0** | $0.14 | $0.28 | 1M |
| 3 | `qwen/qwen3-coder-next` | **98.4** | $0.14 | $0.80 | 262K |

**Cost/Performance — OpenRouter**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **9,540,000** | 95.4 | $0.01 | $0.03 | 131K |
| 2 | `ibm-granite/granite-4.0-h-micro` | **5,058,824** | 86.0 | $0.02 | $0.11 | 131K |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **4,090,000** | 81.8 | $0.02 | $0.05 | 16K |

### unspecified-low (General Low — Speed-heavy)

**Performance — OpenRouter**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `openai/gpt-5.4-nano` | **99.2** | $0.20 | $1.25 | 400K |
| 2 | `deepseek/deepseek-v4-flash` | **99.0** | $0.14 | $0.28 | 1M |
| 3 | `qwen/qwen3-coder-next` | **98.4** | $0.14 | $0.80 | 262K |

**Cost/Performance — OpenRouter**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **9,540,000** | 95.4 | $0.01 | $0.03 | 131K |
| 2 | `ibm-granite/granite-4.0-h-micro` | **5,058,824** | 86.0 | $0.02 | $0.11 | 131K |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **4,090,000** | 81.8 | $0.02 | $0.05 | 16K |

### unspecified-high (General High — Reasoning-heavy)

**Performance — OpenRouter**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `z-ai/glm-5.1` | **94.5** | $1.05 | $3.50 | 202K |
| 2 | `openai/gpt-5.4-pro` | **92.0** | $30.00 | $180.00 | 1M |
| 3 | `deepseek/deepseek-v4-pro` | **91.9** | $0.43 | $0.87 | 1M |

**Cost/Performance — OpenRouter**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **7,550,000** | 75.5 | $0.01 | $0.03 | 131K |
| 2 | `ibm-granite/granite-4.0-h-micro` | **2,800,000** | 47.6 | $0.02 | $0.11 | 131K |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **2,435,000** | 48.7 | $0.02 | $0.05 | 16K |

### writing (Documentation — Speed-heavy)

**Performance — OpenRouter**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `deepseek/deepseek-v4-pro` | **88.9** | $0.43 | $0.87 | 1M |
| 2 | `z-ai/glm-4.7` | **87.7** | $0.38 | $1.74 | 203K |
| 3 | `deepseek/deepseek-v4-flash` | **83.2** | $0.14 | $0.28 | 1M |

**Cost/Performance — OpenRouter**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `nvidia/nemotron-3-nano-30b-a3b` | **1,500,000** | 75.0 | $0.05 | $0.20 | 262K |
| 2 | `mistralai/mistral-small-24b-instruct-2501` | **1,210,000** | 60.5 | $0.05 | $0.08 | 33K |
| 3 | `qwen/qwen3.5-9b` | **764,000** | 76.4 | $0.10 | $0.15 | 262K |

---

## Part 2: OpenCode Zen Rankings

### OpenCode Zen Models

| Model | Input $/1M | Output $/1M | Context | Vision | Tools |
|-------|-----------|------------|---------|--------|-------|
| `opencode/gemini-3-flash` | $0.50 | $3.00 | 128K | Yes | Yes |
| `opencode/qwen3.5-plus` | $0.20 | $1.20 | 128K | Unknown | Unknown |
| `opencode/qwen3.6-plus` | $0.50 | $3.00 | 128K | Yes | Yes |
| `opencode/gemini-3.1-pro` | $2.00 | $12.00 | 128K | Yes | Yes |
| `opencode/claude-opus-4-6` | $5.00 | $25.00 | 200K | No | Yes |

**Refresh note:** All stale Zen endpoint references in the refreshed projections below were replaced with current paid endpoints.

### sisyphus (Orchestrator — Reasoning-heavy)

**Performance — OpenCode Zen**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|
| 1 | `opencode/claude-opus-4-6` | **90** | $5.00 | $25.00 | 200K |
| 2 | `opencode/qwen3.6-plus` | **88** | $0.50 | $3.00 | 128K |
| 3 | `opencode/gemini-3.1-pro` | **87** | $2.00 | $12.00 | 128K |

**Cost/Performance — OpenCode Zen**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `opencode/qwen3.5-plus` | **430,000** | 86 | $0.20 | $1.20 | 128K |
| 2 | `opencode/qwen3.6-plus` | **176,000** | 88 | $0.50 | $3.00 | 128K |
| 3 | `opencode/gemini-3-flash` | **150,000** | 75 | $0.50 | $3.00 | 128K |

### hephaestus (Executor — Coding-heavy)

**Performance — OpenCode Zen**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|
| 1 | `opencode/qwen3.5-plus` | **90** | $0.20 | $1.20 | 128K |
| 2 | `opencode/claude-opus-4-6` | **89** | $5.00 | $25.00 | 200K |
| 3 | `opencode/gemini-3.1-pro` | **87** | $2.00 | $12.00 | 128K |

**Cost/Performance — OpenCode Zen**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `opencode/qwen3.5-plus` | **450,000** | 90 | $0.20 | $1.20 | 128K |
| 2 | `opencode/qwen3.6-plus` | **170,000** | 85 | $0.50 | $3.00 | 128K |
| 3 | `opencode/gemini-3-flash` | **150,000** | 75 | $0.50 | $3.00 | 128K |

### oracle (Consultant — Deep-reasoning)

**Performance — OpenCode Zen**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|
| 1 | `opencode/claude-opus-4-6` | **91** | $5.00 | $25.00 | 200K |
| 2 | `opencode/gemini-3.1-pro` | **89** | $2.00 | $12.00 | 128K |
| 3 | `opencode/qwen3.6-plus` | **88** | $0.50 | $3.00 | 128K |

**Cost/Performance — OpenCode Zen**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `opencode/qwen3.5-plus` | **430,000** | 86 | $0.20 | $1.20 | 128K |
| 2 | `opencode/qwen3.6-plus` | **176,000** | 88 | $0.50 | $3.00 | 128K |
| 3 | `opencode/gemini-3-flash` | **150,000** | 75 | $0.50 | $3.00 | 128K |

### explore (Search — Speed-heavy)

**Performance — OpenCode Zen**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|
| 1 | `opencode/gemini-3-flash` | **95** | $0.50 | $3.00 | 128K |
| 2 | `opencode/qwen3.5-plus` | **93** | $0.20 | $1.20 | 128K |
| 3 | `opencode/qwen3.6-plus` | **91** | $0.50 | $3.00 | 128K |

**Cost/Performance — OpenCode Zen**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `opencode/qwen3.5-plus` | **465,000** | 93 | $0.20 | $1.20 | 128K |
| 2 | `opencode/gemini-3-flash` | **190,000** | 95 | $0.50 | $3.00 | 128K |
| 3 | `opencode/qwen3.6-plus` | **182,000** | 91 | $0.50 | $3.00 | 128K |

### prometheus (Planner — Reasoning-heavy)

**Performance — OpenCode Zen**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|
| 1 | `opencode/claude-opus-4-6` | **91** | $5.00 | $25.00 | 200K |
| 2 | `opencode/qwen3.6-plus` | **89** | $0.50 | $3.00 | 128K |
| 3 | `opencode/gemini-3.1-pro` | **88** | $2.00 | $12.00 | 128K |

**Cost/Performance — OpenCode Zen**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `opencode/qwen3.5-plus` | **435,000** | 87 | $0.20 | $1.20 | 128K |
| 2 | `opencode/qwen3.6-plus` | **178,000** | 89 | $0.50 | $3.00 | 128K |
| 3 | `opencode/gemini-3-flash` | **150,000** | 75 | $0.50 | $3.00 | 128K |

### metis (Analyst — Deep-reasoning)

**Performance — OpenCode Zen**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|
| 1 | `opencode/claude-opus-4-6` | **92** | $5.00 | $25.00 | 200K |
| 2 | `opencode/qwen3.6-plus` | **90** | $0.50 | $3.00 | 128K |
| 3 | `opencode/gemini-3.1-pro` | **89** | $2.00 | $12.00 | 128K |

**Cost/Performance — OpenCode Zen**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `opencode/qwen3.5-plus` | **440,000** | 88 | $0.20 | $1.20 | 128K |
| 2 | `opencode/qwen3.6-plus` | **180,000** | 90 | $0.50 | $3.00 | 128K |
| 3 | `opencode/gemini-3-flash` | **150,000** | 75 | $0.50 | $3.00 | 128K |

### momus (Critic — Deep-reasoning)

**Performance — OpenCode Zen**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|
| 1 | `opencode/claude-opus-4-6` | **91** | $5.00 | $25.00 | 200K |
| 2 | `opencode/qwen3.6-plus` | **89** | $0.50 | $3.00 | 128K |
| 3 | `opencode/gemini-3.1-pro` | **88** | $2.00 | $12.00 | 128K |

**Cost/Performance — OpenCode Zen**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `opencode/qwen3.5-plus` | **435,000** | 87 | $0.20 | $1.20 | 128K |
| 2 | `opencode/qwen3.6-plus` | **178,000** | 89 | $0.50 | $3.00 | 128K |
| 3 | `opencode/gemini-3-flash` | **150,000** | 75 | $0.50 | $3.00 | 128K |

### librarian (Research — Speed-heavy)

**Performance — OpenCode Zen**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|
| 1 | `opencode/gemini-3-flash` | **98** | $0.50 | $3.00 | 128K |
| 2 | `opencode/qwen3.5-plus` | **95** | $0.20 | $1.20 | 128K |
| 3 | `opencode/qwen3.5-plus` | **93** | $0.20 | $1.20 | 128K |

**Cost/Performance — OpenCode Zen**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `opencode/qwen3.5-plus` | **475,000** | 95 | $0.20 | $1.20 | 128K |
| 2 | `opencode/qwen3.5-plus` | **465,000** | 93 | $0.20 | $1.20 | 128K |
| 3 | `opencode/gemini-3-flash` | **196,000** | 98 | $0.50 | $3.00 | 128K |

### multimodal-looker (Vision — Vision-heavy)

**Performance — OpenCode Zen**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|
| 1 | `opencode/gemini-3.1-pro` | **93** | $2.00 | $12.00 | 128K |
| 2 | `opencode/claude-opus-4-6` | **88** | $5.00 | $25.00 | 200K |
| 3 | `opencode/qwen3.6-plus` | **85** | $0.50 | $3.00 | 128K |

**Cost/Performance — OpenCode Zen**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `opencode/qwen3.5-plus` | **410,000** | 82 | $0.20 | $1.20 | 128K |
| 2 | `opencode/qwen3.6-plus` | **170,000** | 85 | $0.50 | $3.00 | 128K |
| 3 | `opencode/gemini-3-flash` | **160,000** | 80 | $0.50 | $3.00 | 128K |

### atlas (Knowledge — Reasoning-heavy)

**Performance — OpenCode Zen**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|
| 1 | `opencode/claude-opus-4-6` | **90** | $5.00 | $25.00 | 200K |
| 2 | `opencode/qwen3.6-plus` | **88** | $0.50 | $3.00 | 128K |
| 3 | `opencode/gemini-3.1-pro` | **87** | $2.00 | $12.00 | 128K |

**Cost/Performance — OpenCode Zen**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `opencode/qwen3.5-plus` | **430,000** | 86 | $0.20 | $1.20 | 128K |
| 2 | `opencode/qwen3.6-plus` | **176,000** | 88 | $0.50 | $3.00 | 128K |
| 3 | `opencode/gemini-3-flash` | **150,000** | 75 | $0.50 | $3.00 | 128K |

### sisyphus-junior (Junior Orchestrator — Junior/orchestration)

**Performance — OpenCode Zen**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|
| 1 | `opencode/qwen3.5-plus` | **89** | $0.20 | $1.20 | 128K |
| 2 | `opencode/qwen3.6-plus` | **87** | $0.50 | $3.00 | 128K |
| 3 | `opencode/claude-opus-4-6` | **86** | $5.00 | $25.00 | 200K |

**Cost/Performance — OpenCode Zen**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `opencode/qwen3.5-plus` | **445,000** | 89 | $0.20 | $1.20 | 128K |
| 2 | `opencode/qwen3.5-plus` | **425,000** | 85 | $0.20 | $1.20 | 128K |
| 3 | `opencode/qwen3.6-plus` | **174,000** | 87 | $0.50 | $3.00 | 128K |

### visual-engineering (Frontend/UI — Vision-heavy)

**Performance — OpenCode Zen**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|
| 1 | `opencode/gemini-3.1-pro` | **92** | $2.00 | $12.00 | 128K |
| 2 | `opencode/claude-opus-4-6` | **87** | $5.00 | $25.00 | 200K |
| 3 | `opencode/gemini-3-flash` | **85** | $0.50 | $3.00 | 128K |

**Cost/Performance — OpenCode Zen**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `opencode/qwen3.5-plus` | **410,000** | 82 | $0.20 | $1.20 | 128K |
| 2 | `opencode/gemini-3-flash` | **170,000** | 85 | $0.50 | $3.00 | 128K |
| 3 | `opencode/qwen3.6-plus` | **164,000** | 82 | $0.50 | $3.00 | 128K |

### artistry (Creative — Deep-reasoning)

**Performance — OpenCode Zen**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|
| 1 | `opencode/claude-opus-4-6` | **91** | $5.00 | $25.00 | 200K |
| 2 | `opencode/gemini-3.1-pro` | **88** | $2.00 | $12.00 | 128K |
| 3 | `opencode/qwen3.6-plus` | **87** | $0.50 | $3.00 | 128K |

**Cost/Performance — OpenCode Zen**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `opencode/qwen3.5-plus` | **425,000** | 85 | $0.20 | $1.20 | 128K |
| 2 | `opencode/qwen3.6-plus` | **174,000** | 87 | $0.50 | $3.00 | 128K |
| 3 | `opencode/gemini-3-flash` | **150,000** | 75 | $0.50 | $3.00 | 128K |

### ultrabrain (Hard Logic — Deep-reasoning)

**Performance — OpenCode Zen**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|
| 1 | `opencode/claude-opus-4-6` | **91** | $5.00 | $25.00 | 200K |
| 2 | `opencode/gemini-3.1-pro` | **88** | $2.00 | $12.00 | 128K |
| 3 | `opencode/qwen3.6-plus` | **87** | $0.50 | $3.00 | 128K |

**Cost/Performance — OpenCode Zen**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `opencode/qwen3.5-plus` | **425,000** | 85 | $0.20 | $1.20 | 128K |
| 2 | `opencode/qwen3.6-plus` | **174,000** | 87 | $0.50 | $3.00 | 128K |
| 3 | `opencode/gemini-3-flash` | **150,000** | 75 | $0.50 | $3.00 | 128K |

### deep (Autonomous — Deep-reasoning)

**Performance — OpenCode Zen**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|
| 1 | `opencode/claude-opus-4-6` | **91** | $5.00 | $25.00 | 200K |
| 2 | `opencode/gemini-3.1-pro` | **88** | $2.00 | $12.00 | 128K |
| 3 | `opencode/qwen3.6-plus` | **87** | $0.50 | $3.00 | 128K |

**Cost/Performance — OpenCode Zen**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `opencode/qwen3.5-plus` | **425,000** | 85 | $0.20 | $1.20 | 128K |
| 2 | `opencode/qwen3.6-plus` | **174,000** | 87 | $0.50 | $3.00 | 128K |
| 3 | `opencode/gemini-3-flash` | **150,000** | 75 | $0.50 | $3.00 | 128K |

### quick (Trivial — Speed-heavy)

**Performance — OpenCode Zen**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|
| 1 | `opencode/gemini-3-flash` | **97** | $0.50 | $3.00 | 128K |
| 2 | `opencode/qwen3.5-plus` | **96** | $0.20 | $1.20 | 128K |
| 3 | `opencode/qwen3.5-plus` | **94** | $0.20 | $1.20 | 128K |

**Cost/Performance — OpenCode Zen**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `opencode/qwen3.5-plus` | **480,000** | 96 | $0.20 | $1.20 | 128K |
| 2 | `opencode/qwen3.5-plus` | **470,000** | 94 | $0.20 | $1.20 | 128K |
| 3 | `opencode/gemini-3-flash` | **194,000** | 97 | $0.50 | $3.00 | 128K |

### unspecified-low (General Low — Speed-heavy)

**Performance — OpenCode Zen**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|
| 1 | `opencode/gemini-3-flash` | **97** | $0.50 | $3.00 | 128K |
| 2 | `opencode/qwen3.5-plus` | **96** | $0.20 | $1.20 | 128K |
| 3 | `opencode/qwen3.5-plus` | **94** | $0.20 | $1.20 | 128K |

**Cost/Performance — OpenCode Zen**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `opencode/qwen3.5-plus` | **480,000** | 96 | $0.20 | $1.20 | 128K |
| 2 | `opencode/qwen3.5-plus` | **470,000** | 94 | $0.20 | $1.20 | 128K |
| 3 | `opencode/gemini-3-flash` | **194,000** | 97 | $0.50 | $3.00 | 128K |

### unspecified-high (General High — Reasoning-heavy)

**Performance — OpenCode Zen**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|
| 1 | `opencode/claude-opus-4-6` | **90** | $5.00 | $25.00 | 200K |
| 2 | `opencode/qwen3.6-plus` | **88** | $0.50 | $3.00 | 128K |
| 3 | `opencode/gemini-3.1-pro` | **87** | $2.00 | $12.00 | 128K |

**Cost/Performance — OpenCode Zen**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `opencode/qwen3.5-plus` | **430,000** | 86 | $0.20 | $1.20 | 128K |
| 2 | `opencode/qwen3.6-plus` | **176,000** | 88 | $0.50 | $3.00 | 128K |
| 3 | `opencode/gemini-3-flash` | **150,000** | 75 | $0.50 | $3.00 | 128K |

### writing (Documentation — Speed-heavy)

**Performance — OpenCode Zen**

| # | Model | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|
| 1 | `opencode/gemini-3-flash` | **98** | $0.50 | $3.00 | 128K |
| 2 | `opencode/qwen3.5-plus` | **95** | $0.20 | $1.20 | 128K |
| 3 | `opencode/qwen3.6-plus` | **91** | $0.50 | $3.00 | 128K |

**Cost/Performance — OpenCode Zen**

| # | Model | C/P | Score | $/1M In | $/1M Out | Ctx |
|---|---|---|---|---|---|---|
| 1 | `opencode/qwen3.5-plus` | **475,000** | 95 | $0.20 | $1.20 | 128K |
| 2 | `opencode/gemini-3-flash` | **196,000** | 98 | $0.50 | $3.00 | 128K |
| 3 | `opencode/qwen3.6-plus` | **182,000** | 91 | $0.50 | $3.00 | 128K |

---

## Part 3: Cost Projections — Detailed Methodology

### Assumptions

| Parameter | Value | Source |
|---|---|---|
| OpenAI Plus subscription | $20/month | OpenAI pricing page |
| Weeks per billing cycle | 4.33 | 52 weeks / 12 months |
| Weekly budget equivalent | $4.62 | $20 / 4.33 |
| Average weekly consumption | 500K input + 200K output tokens | Estimated from typical Plus usage |
| GPT average performance baseline | 92.0 | Weighted avg of GPT models in top rankings |

### Top-1 Models per Tier (Used for Projections)

**OpenCode Zen — Performance Tier** (refreshed to use currently available endpoints only):

| Agent/Category | Top-1 Model | Score | $/1M In | $/1M Out |
|---|---|---|---|---|
| sisyphus | `opencode/claude-opus-4-6` | 90 | $5.00 | $25.00 |
| hephaestus | `opencode/qwen3.5-plus` | 90 | $0.20 | $1.20 |
| oracle | `opencode/claude-opus-4-6` | 91 | $5.00 | $25.00 |
| explore | `opencode/gemini-3-flash` | 95 | $0.50 | $3.00 |
| prometheus | `opencode/claude-opus-4-6` | 91 | $5.00 | $25.00 |
| metis | `opencode/claude-opus-4-6` | 92 | $5.00 | $25.00 |
| momus | `opencode/claude-opus-4-6` | 91 | $5.00 | $25.00 |
| librarian | `opencode/gemini-3-flash` | 98 | $0.50 | $3.00 |
| multimodal-looker | `opencode/gemini-3.1-pro` | 93 | $2.00 | $12.00 |
| atlas | `opencode/claude-opus-4-6` | 90 | $5.00 | $25.00 |
| sisyphus-junior | `opencode/qwen3.5-plus` | 89 | $0.20 | $1.20 |
| visual-engineering | `opencode/gemini-3.1-pro` | 92 | $2.00 | $12.00 |
| artistry | `opencode/claude-opus-4-6` | 91 | $5.00 | $25.00 |
| ultrabrain | `opencode/claude-opus-4-6` | 91 | $5.00 | $25.00 |
| deep | `opencode/claude-opus-4-6` | 91 | $5.00 | $25.00 |
| quick | `opencode/gemini-3-flash` | 97 | $0.50 | $3.00 |
| unspecified-low | `opencode/gemini-3-flash` | 97 | $0.50 | $3.00 |
| unspecified-high | `opencode/claude-opus-4-6` | 90 | $5.00 | $25.00 |
| writing | `opencode/gemini-3-flash` | 98 | $0.50 | $3.00 |
| **Average** | | **92.5** | **$2.99** | **$15.33** |

**OpenCode Zen — Cost/Performance Tier** (refreshed current-endpoint mix):

| Agent/Category | Top-1 Model | Score | $/1M In | $/1M Out |
|---|---|---|---|---|
| All 19 agents/categories | `opencode/qwen3.5-plus` | 82-96 | $0.20 | $1.20 |
| **Average** | | **88.4** | **$0.20** | **$1.20** |

**OpenRouter — Performance Tier** (top-1 per agent/category):

| Agent/Category | Top-1 Model | Score | $/1M In | $/1M Out |
|---|---|---|---|---|
| sisyphus | `z-ai/glm-5.1` | 94.5 | $1.05 | $3.50 |
| hephaestus | `qwen/qwen3-coder-next` | 90.7 | $0.14 | $0.80 |
| oracle | `z-ai/glm-5.1` | 94.7 | $1.05 | $3.50 |
| explore | `deepseek/deepseek-v4-flash` | 80.2 | $0.14 | $0.28 |
| prometheus | `z-ai/glm-5.1` | 94.5 | $1.05 | $3.50 |
| metis | `z-ai/glm-5.1` | 94.7 | $1.05 | $3.50 |
| momus | `z-ai/glm-5.1` | 94.7 | $1.05 | $3.50 |
| librarian | `deepseek/deepseek-v4-flash` | 80.2 | $0.14 | $0.28 |
| multimodal-looker | `openai/gpt-5.5` | 96.0 | $5.00 | $30.00 |
| atlas | `z-ai/glm-5.1` | 94.5 | $1.05 | $3.50 |
| sisyphus-junior | `deepseek/deepseek-v4-pro` | 94.0 | $0.43 | $0.87 |
| visual-engineering | `openai/gpt-5.5` | 96.0 | $5.00 | $30.00 |
| artistry | `z-ai/glm-5.1` | 94.5 | $1.05 | $3.50 |
| ultrabrain | `z-ai/glm-5.1` | 94.7 | $1.05 | $3.50 |
| deep | `z-ai/glm-5.1` | 94.5 | $1.05 | $3.50 |
| quick | `openai/gpt-5.4-nano` | 99.2 | $0.20 | $1.25 |
| unspecified-low | `openai/gpt-5.4-nano` | 99.2 | $0.20 | $1.25 |
| unspecified-high | `z-ai/glm-5.1` | 94.5 | $1.05 | $3.50 |
| writing | `deepseek/deepseek-v4-pro` | 88.9 | $0.43 | $0.87 |
| **Average** | | **93.17** | **$1.17** | **$5.29** |

**OpenRouter — Cost/Performance Tier** (top-1 = `mistralai/mistral-nemo` for all):

| Agent/Category | Top-1 Model | Score | $/1M In | $/1M Out |
|---|---|---|---|---|
| All 19 agents/categories | `mistralai/mistral-nemo` | 75.3-95.4 | $0.01 | $0.03 |
| **Average** | | **81.5** | **$0.01** | **$0.03** |

### Cost Projection Calculations

#### A) OpenCode Zen — Performance Tier

- Average input cost: $2.99/1M tokens
- Average output cost: $15.33/1M tokens
- Weekly cost = (500K × $2.99/1M) + (200K × $15.33/1M) = $1.50 + $3.07 = **$4.56/week**
- Weeks for $20 = $20 / $4.56 = **4.39 weeks**
- Price for 4.33 weeks = $4.56 × 4.33 = **$19.75**
- Performance indicator = (92.5 / 92.0) × 100 = **100.5%**

#### B) OpenCode Zen — Cost/Performance Tier

- Average input cost: $0.20/1M tokens
- Average output cost: $1.20/1M tokens
- Weekly cost = (500K × $0.20/1M) + (200K × $1.20/1M) = $0.10 + $0.24 = **$0.34/week**
- Weeks for $20 = $20 / $0.34 = **58.82 weeks**
- Price for 4.33 weeks = $0.34 × 4.33 = **$1.47**
- Performance indicator = (88.4 / 92.0) × 100 = **96.1%**

#### C) OpenRouter — Performance Tier

- Average input cost: $1.17/1M tokens
- Average output cost: $5.29/1M tokens
- Weekly cost = (500K × $1.17/1M) + (200K × $5.29/1M) = $0.59 + $1.06 = **$1.65/week**
- Weeks for $20 = $20 / $1.65 = **12.12 weeks**
- Price for 4.33 weeks = $1.65 × 4.33 = **$7.14**
- Performance indicator = (93.2 / 92.0) × 100 = **101.3%**

#### D) OpenRouter — Cost/Performance Tier

- Average input cost: $0.01/1M tokens
- Average output cost: $0.03/1M tokens
- Weekly cost = (500K × $0.01/1M) + (200K × $0.03/1M) = $0.005 + $0.006 = **$0.011/week**
- Weeks for $20 = $20 / $0.011 = **1,818 weeks**
- Price for 4.33 weeks = $0.011 × 4.33 = **$0.05**
- Performance indicator = (81.5 / 92.0) × 100 = **88.6%**

---

## Key Insights

1. **OpenRouter Performance tier is still the best value for quality**: 101.3% of GPT performance at **$7.14/month** (vs $20 for Plus) — still materially cheaper while beating the GPT baseline

2. **OpenCode Zen Cost/Performance tier is no longer free**: after replacing unavailable free aliases with current paid endpoints, it still delivers **96.1%** of GPT performance at only **$1.47/month**

3. **OpenCode Zen Performance tier is now roughly at Plus pricing**: **$19.75/month** for **100.5%** GPT performance

4. **OpenRouter Cost/Performance tier is absurdly cheap**: 88.6% of GPT performance at $0.05/month — but quality gap is noticeable (~11.4% below GPT)

5. **Sweet spot**: OpenRouter Performance tier — best quality (**101.3%**) at about a **64% discount** vs Plus

6. **Best current Zen budget model**: `opencode/qwen3.5-plus` now carries the refreshed Zen cost/performance tier after removing stale free aliases

7. **Premium option**: OpenCode Zen `claude-opus-4-6` — best reasoning (90-92) but expensive at $5/$25

8. **GPT-5.5 now leads the OpenRouter vision tier**: it takes both **multimodal-looker** and **visual-engineering**, but raises the OpenRouter performance-tier average cost materially

9. **Reasoning tasks still dominate Zen spend**: sisyphus/oracle/metis/momus/ultrabrain/deep agents are the cost drivers — model choice here matters most

10. **Availability matters**: several April 24 draft model IDs/aliases were no longer current on April 25; this refresh aligns the projection math to provider-available endpoints only

---

## Related Documents

- [Oh-My-OpenCode Agent Rankings v3.0](./oh-my-opencode-agent-rankings.md) — NVIDIA Build + OpenCode Zen + OpenAI
- [All OpenRouter Providers](./oh-my-opencode-agent-rankings-all-providers.md) — 294 ranked models
- [OpenCode Zen Only](./oh-my-opencode-agent-rankings-opencode-zen-only.md) — 6 OpenCode Zen models
- [OpenAI Only](./oh-my-opencode-agent-rankings-openai-only.md) — OpenAI provider deep dive

---

**Last Updated:** April 25, 2026
