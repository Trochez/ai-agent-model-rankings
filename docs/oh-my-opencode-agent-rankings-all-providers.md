# Oh-My-OpenCode Agent Model Rankings — All OpenRouter Providers

**Date:** April 24, 2026
**Scope:** All models available on OpenRouter (353 models fetched, 294 ranked after filtering)
**Companion to:** [oh-my-opencode-agent-rankings.md](./oh-my-opencode-agent-rankings.md) (v3.0, NVIDIA Build + OpenCode Zen + OpenAI)

---

## Executive Summary

This document provides comprehensive model rankings for every oh-my-opencode agent and category,
covering all models available on OpenRouter. Each agent/category has **two tables**:

1. **Performance Table**: Top 10 models by composite performance score (0-100)
2. **Cost/Performance Table**: Top 10 models by cost-performance ratio (higher = better value)

### Scoring Methodology

Each model receives a **composite performance score (0-100)** calculated from benchmark data,
weighted by agent type:

| Agent Type | Agents/Categories | Weight Formula |
|---|---|---|
| **Reasoning-heavy** | sisyphus, prometheus, atlas, unspecified-high | GPQA 30% + SWE-Bench Pro 25% + ARC-AGI-2 20% + MMLU-Pro 15% + Cost-eff 10% |
| **Coding-heavy** | hephaestus | SWE-Bench Pro 35% + HumanEval 25% + GPQA 15% + Terminal-Bench 15% + Cost-eff 10% |
| **Deep-reasoning** | oracle, metis, momus, ultrabrain, deep, artistry | GPQA 35% + SWE-Bench Pro 25% + ARC-AGI-2 20% + MMLU-Pro 10% + Cost-eff 10% |
| **Speed-heavy** | explore, librarian | Cost-eff 30% + Latency-tier 25% + GPQA 15% + SWE-Bench Pro 15% + Context 15% |
| **Vision-heavy** | multimodal-looker, visual-engineering | MMMU-Pro 30% + GPQA 20% + SWE-Bench Pro 20% + Context 15% + Cost-eff 15% |
| **Writing/research** | writing | MMLU-Pro 30% + GPQA 20% + Cost-eff 25% + Context 15% + SWE-Bench Pro 10% |
| **Quick/low** | quick, unspecified-low | Cost-eff 40% + Latency-tier 30% + GPQA 15% + Context 15% |
| **Junior/orchestration** | sisyphus-junior | SWE-Bench Pro 25% + GPQA 25% + ARC-AGI-2 15% + Cost-eff 20% + Context 15% |

**Cost/Performance Score** = `(Performance Score × 1000) / (Input Cost per 1M tokens)`
- Free models: Score = `Performance Score × 100` (very high, reflecting zero cost)
- Higher cost/performance = better value for money

### Benchmark Data Sources

- Known benchmarks: Models with verified benchmark scores from public leaderboards
- Proxy estimates: Models without public benchmarks are estimated from model family, size hints, and pricing tier
- Cost-efficiency: Normalized from pricing (free=100, $0.05=98, $2.50=55, $30=15, $150=5)
- Latency tier: Estimated from model size/cost (nano=95, mini=88, flash=88, pro=55, 480b=50)

---

## Agent Rankings

### sisyphus (Orchestrator — Reasoning-heavy)

**Performance Ranking — sisyphus**

| Rank | Model | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|
| 1 | `z-ai/glm-5.1` | **94.5** | $1.05 | $3.50 | 202,752 |  |
| 2 | `openai/gpt-5.4-pro` | **92.0** | $30.00 | $180.00 | 1,050,000 |  |
| 3 | `deepseek/deepseek-v4-pro` | **91.9** | $1.74 | $3.48 | 1,048,576 |  |
| 4 | `openai/o3-pro` | **91.8** | $20.00 | $80.00 | 200,000 |  |
| 5 | `z-ai/glm-5` | **91.0** | $0.60 | $2.08 | 202,752 |  |
| 6 | `z-ai/glm-5-turbo` | **90.5** | $1.20 | $4.00 | 202,752 |  |
| 7 | `anthropic/claude-opus-4` | **89.7** | $15.00 | $75.00 | 200,000 |  |
| 8 | `qwen/qwen3-coder-next` | **89.5** | $0.15 | $0.80 | 262,144 |  |
| 9 | `openai/gpt-5.4` | **89.3** | $2.50 | $15.00 | 1,050,000 |  |
| 10 | `openai/o1-pro` | **88.6** | $150.00 | $600.00 | 200,000 |  |

**Cost/Performance Ranking — sisyphus**

| Rank | Model | Cost/Perf | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **7,550,000** | 75.5 | $0.01 | $0.03 | 131,072 |  |
| 2 | `ibm-granite/granite-4.0-h-micro` | **2,800,000** | 47.6 | $0.02 | $0.11 | 131,000 |  |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **2,435,000** | 48.7 | $0.02 | $0.05 | 16,384 |  |
| 4 | `qwen/qwen-turbo` | **2,301,538** | 74.8 | $0.03 | $0.13 | 131,072 |  |
| 5 | `meta-llama/llama-3.2-1b-instruct` | **1,866,667** | 50.4 | $0.03 | $0.20 | 60,000 |  |
| 6 | `qwen/qwen-2.5-7b-instruct` | **1,785,000** | 71.4 | $0.04 | $0.10 | 32,768 |  |
| 7 | `liquid/lfm-2-24b-a2b` | **1,586,667** | 47.6 | $0.03 | $0.12 | 32,768 |  |
| 8 | `qwen/qwen3-8b` | **1,562,000** | 78.1 | $0.05 | $0.40 | 40,960 |  |
| 9 | `meta-llama/llama-3-8b-instruct` | **1,520,000** | 45.6 | $0.03 | $0.04 | 8,192 |  |
| 10 | `google/gemma-3-4b-it` | **1,510,000** | 60.4 | $0.04 | $0.08 | 131,072 |  |

### hephaestus (Executor — Coding-heavy)

**Performance Ranking — hephaestus**

| Rank | Model | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|
| 1 | `qwen/qwen3-coder-next` | **90.7** | $0.15 | $0.80 | 262,144 |  |
| 2 | `z-ai/glm-5.1` | **90.5** | $1.05 | $3.50 | 202,752 |  |
| 3 | `openai/gpt-5.4` | **89.6** | $2.50 | $15.00 | 1,050,000 |  |
| 4 | `openai/gpt-5.4-pro` | **89.0** | $30.00 | $180.00 | 1,050,000 |  |
| 5 | `deepseek/deepseek-v4-pro` | **88.5** | $1.74 | $3.48 | 1,048,576 |  |
| 6 | `qwen/qwen3-coder-plus` | **88.3** | $0.65 | $3.25 | 1,000,000 |  |
| 7 | `openai/gpt-5.3-codex` | **87.7** | $1.75 | $14.00 | 400,000 |  |
| 8 | `openai/o3-pro` | **87.7** | $20.00 | $80.00 | 200,000 |  |
| 9 | `z-ai/glm-5` | **87.6** | $0.60 | $2.08 | 202,752 |  |
| 10 | `z-ai/glm-5-turbo` | **87.2** | $1.20 | $4.00 | 202,752 |  |

**Cost/Performance Ranking — hephaestus**

| Rank | Model | Cost/Perf | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **7,520,000** | 75.2 | $0.01 | $0.03 | 131,072 |  |
| 2 | `ibm-granite/granite-4.0-h-micro` | **2,723,529** | 46.3 | $0.02 | $0.11 | 131,000 |  |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **2,315,000** | 46.3 | $0.02 | $0.05 | 16,384 |  |
| 4 | `qwen/qwen-turbo` | **2,286,154** | 74.3 | $0.03 | $0.13 | 131,072 |  |
| 5 | `meta-llama/llama-3.2-1b-instruct` | **1,788,889** | 48.3 | $0.03 | $0.20 | 60,000 |  |
| 6 | `qwen/qwen-2.5-7b-instruct` | **1,775,000** | 71.0 | $0.04 | $0.10 | 32,768 |  |
| 7 | `qwen/qwen3-8b` | **1,552,000** | 77.6 | $0.05 | $0.40 | 40,960 |  |
| 8 | `liquid/lfm-2-24b-a2b` | **1,543,333** | 46.3 | $0.03 | $0.12 | 32,768 |  |
| 9 | `google/gemma-3-4b-it` | **1,500,000** | 60.0 | $0.04 | $0.08 | 131,072 |  |
| 10 | `google/gemma-3-12b-it` | **1,500,000** | 60.0 | $0.04 | $0.13 | 131,072 |  |

### oracle (Consultant — Deep-reasoning)

**Performance Ranking — oracle**

| Rank | Model | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|
| 1 | `z-ai/glm-5.1` | **94.7** | $1.05 | $3.50 | 202,752 |  |
| 2 | `openai/gpt-5.4-pro` | **92.4** | $30.00 | $180.00 | 1,050,000 |  |
| 3 | `deepseek/deepseek-v4-pro` | **92.0** | $1.74 | $3.48 | 1,048,576 |  |
| 4 | `openai/o3-pro` | **91.9** | $20.00 | $80.00 | 200,000 |  |
| 5 | `z-ai/glm-5` | **91.2** | $0.60 | $2.08 | 202,752 |  |
| 6 | `z-ai/glm-5-turbo` | **90.8** | $1.20 | $4.00 | 202,752 |  |
| 7 | `openai/gpt-5.4` | **90.1** | $2.50 | $15.00 | 1,050,000 |  |
| 8 | `anthropic/claude-opus-4` | **90.0** | $15.00 | $75.00 | 200,000 |  |
| 9 | `qwen/qwen3-coder-next` | **89.7** | $0.15 | $0.80 | 262,144 |  |
| 10 | `z-ai/glm-5v-turbo` | **88.7** | $1.20 | $4.00 | 202,752 |  |

**Cost/Performance Ranking — oracle**

| Rank | Model | Cost/Perf | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **7,560,000** | 75.6 | $0.01 | $0.03 | 131,072 |  |
| 2 | `ibm-granite/granite-4.0-h-micro` | **2,800,000** | 47.6 | $0.02 | $0.11 | 131,000 |  |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **2,445,000** | 48.9 | $0.02 | $0.05 | 16,384 |  |
| 4 | `qwen/qwen-turbo` | **2,304,615** | 74.9 | $0.03 | $0.13 | 131,072 |  |
| 5 | `meta-llama/llama-3.2-1b-instruct` | **1,874,074** | 50.6 | $0.03 | $0.20 | 60,000 |  |
| 6 | `qwen/qwen-2.5-7b-instruct` | **1,787,500** | 71.5 | $0.04 | $0.10 | 32,768 |  |
| 7 | `liquid/lfm-2-24b-a2b` | **1,586,667** | 47.6 | $0.03 | $0.12 | 32,768 |  |
| 8 | `qwen/qwen3-8b` | **1,564,000** | 78.2 | $0.05 | $0.40 | 40,960 |  |
| 9 | `meta-llama/llama-3-8b-instruct` | **1,526,667** | 45.8 | $0.03 | $0.04 | 8,192 |  |
| 10 | `google/gemma-3-4b-it` | **1,510,000** | 60.4 | $0.04 | $0.08 | 131,072 |  |

### explore (Search — Speed-heavy)

**Performance Ranking — explore**

| Rank | Model | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|
| 1 | `nvidia/deepseek-ai/deepseek-v4-flash` | **80.2** | $0.00 | $0.00 | 1,000,000 | ✓ |
| 2 | `nvidia/stepfun-ai/step-3.5-flash` | **80.0** | $0.00 | $0.00 | 256,000 | ✓ |
| 3 | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | **78.5** | $0.05 | $0.20 | 1,000,000 |  |
| 4 | `nvidia/qwen/qwen3.5-122b-a10b` | **78.3** | $0.00 | $0.00 | 262,000 | ✓ |
| 5 | `nvidia/z-ai/glm-4.7` | **78.0** | $0.00 | $0.00 | 2,540,000 | ✓ |
| 6 | `nvidia/deepseek-ai/deepseek-v4-pro` | **77.7** | $0.00 | $0.00 | 1,000,000 | ✓ |
| 7 | `nvidia/qwen/qwen3.5-9b` | **77.3** | $0.05 | $0.15 | 256,000 |  |
| 8 | `openai/gpt-5.4-nano` | **76.8** | $0.20 | $1.25 | 400,000 |  |
| 9 | `nvidia/nvidia/nemotron-3-super-120b-a12b` | **76.6** | $0.10 | $0.50 | 1,000,000 |  |
| 10 | `nvidia/microsoft/phi-4-multimodal-instruct` | **74.0** | $0.00 | $0.00 | 128,000 | ✓ |

**Cost/Performance Ranking — explore**

| Rank | Model | Cost/Perf | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|---|
| 1 | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | **1,569,000** | 78.5 | $0.05 | $0.20 | 1,000,000 |  |
| 2 | `nvidia/qwen/qwen3.5-9b` | **1,546,100** | 77.3 | $0.05 | $0.15 | 256,000 |  |
| 3 | `nvidia/mistralai/mistral-small-24b-instruct` | **1,191,000** | 59.5 | $0.05 | $0.08 | 33,000 |  |
| 4 | `nvidia/google/gemma-4-26b-a4b-it` | **915,562** | 73.2 | $0.08 | $0.35 | 256,000 |  |
| 5 | `nvidia/microsoft/phi-4-mini-instruct` | **871,067** | 65.3 | $0.075 | $0.30 | 128,000 |  |
| 6 | `nvidia/nvidia/nemotron-3-super-120b-a12b` | **766,050** | 76.6 | $0.10 | $0.50 | 1,000,000 |  |
| 7 | `nvidia/mistral-ai/mistral-small-4-119b-2603` | **679,500** | 68.0 | $0.10 | $0.40 | 256,000 |  |
| 8 | `nvidia/mistralai/mistral-small-3.1-24b-instruct-2503` | **595,500** | 59.6 | $0.10 | $0.30 | 128,000 |  |
| 9 | `nvidia/meta-llama/llama-3.3-nemotron-super-49b-v1.5` | **572,550** | 57.3 | $0.10 | $0.40 | 131,000 |  |
| 10 | `openai/gpt-5.4-nano` | **383,900** | 76.8 | $0.20 | $1.25 | 400,000 |  |

### prometheus (Planner — Reasoning-heavy)

**Performance Ranking — prometheus**

| Rank | Model | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|
| 1 | `z-ai/glm-5.1` | **94.5** | $1.05 | $3.50 | 202,752 |  |
| 2 | `openai/gpt-5.4-pro` | **92.0** | $30.00 | $180.00 | 1,050,000 |  |
| 3 | `deepseek/deepseek-v4-pro` | **91.9** | $1.74 | $3.48 | 1,048,576 |  |
| 4 | `openai/o3-pro` | **91.8** | $20.00 | $80.00 | 200,000 |  |
| 5 | `z-ai/glm-5` | **91.0** | $0.60 | $2.08 | 202,752 |  |
| 6 | `z-ai/glm-5-turbo` | **90.5** | $1.20 | $4.00 | 202,752 |  |
| 7 | `anthropic/claude-opus-4` | **89.7** | $15.00 | $75.00 | 200,000 |  |
| 8 | `qwen/qwen3-coder-next` | **89.5** | $0.15 | $0.80 | 262,144 |  |
| 9 | `openai/gpt-5.4` | **89.3** | $2.50 | $15.00 | 1,050,000 |  |
| 10 | `openai/o1-pro` | **88.6** | $150.00 | $600.00 | 200,000 |  |

**Cost/Performance Ranking — prometheus**

| Rank | Model | Cost/Perf | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **7,550,000** | 75.5 | $0.01 | $0.03 | 131,072 |  |
| 2 | `ibm-granite/granite-4.0-h-micro` | **2,800,000** | 47.6 | $0.02 | $0.11 | 131,000 |  |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **2,435,000** | 48.7 | $0.02 | $0.05 | 16,384 |  |
| 4 | `qwen/qwen-turbo` | **2,301,538** | 74.8 | $0.03 | $0.13 | 131,072 |  |
| 5 | `meta-llama/llama-3.2-1b-instruct` | **1,866,667** | 50.4 | $0.03 | $0.20 | 60,000 |  |
| 6 | `qwen/qwen-2.5-7b-instruct` | **1,785,000** | 71.4 | $0.04 | $0.10 | 32,768 |  |
| 7 | `liquid/lfm-2-24b-a2b` | **1,586,667** | 47.6 | $0.03 | $0.12 | 32,768 |  |
| 8 | `qwen/qwen3-8b` | **1,562,000** | 78.1 | $0.05 | $0.40 | 40,960 |  |
| 9 | `meta-llama/llama-3-8b-instruct` | **1,520,000** | 45.6 | $0.03 | $0.04 | 8,192 |  |
| 10 | `google/gemma-3-4b-it` | **1,510,000** | 60.4 | $0.04 | $0.08 | 131,072 |  |

### metis (Analyst — Deep-reasoning)

**Performance Ranking — metis**

| Rank | Model | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|
| 1 | `z-ai/glm-5.1` | **94.7** | $1.05 | $3.50 | 202,752 |  |
| 2 | `openai/gpt-5.4-pro` | **92.4** | $30.00 | $180.00 | 1,050,000 |  |
| 3 | `deepseek/deepseek-v4-pro` | **92.0** | $1.74 | $3.48 | 1,048,576 |  |
| 4 | `openai/o3-pro` | **91.9** | $20.00 | $80.00 | 200,000 |  |
| 5 | `z-ai/glm-5` | **91.2** | $0.60 | $2.08 | 202,752 |  |
| 6 | `z-ai/glm-5-turbo` | **90.8** | $1.20 | $4.00 | 202,752 |  |
| 7 | `openai/gpt-5.4` | **90.1** | $2.50 | $15.00 | 1,050,000 |  |
| 8 | `anthropic/claude-opus-4` | **90.0** | $15.00 | $75.00 | 200,000 |  |
| 9 | `qwen/qwen3-coder-next` | **89.7** | $0.15 | $0.80 | 262,144 |  |
| 10 | `z-ai/glm-5v-turbo` | **88.7** | $1.20 | $4.00 | 202,752 |  |

**Cost/Performance Ranking — metis**

| Rank | Model | Cost/Perf | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **7,560,000** | 75.6 | $0.01 | $0.03 | 131,072 |  |
| 2 | `ibm-granite/granite-4.0-h-micro` | **2,800,000** | 47.6 | $0.02 | $0.11 | 131,000 |  |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **2,445,000** | 48.9 | $0.02 | $0.05 | 16,384 |  |
| 4 | `qwen/qwen-turbo` | **2,304,615** | 74.9 | $0.03 | $0.13 | 131,072 |  |
| 5 | `meta-llama/llama-3.2-1b-instruct` | **1,874,074** | 50.6 | $0.03 | $0.20 | 60,000 |  |
| 6 | `qwen/qwen-2.5-7b-instruct` | **1,787,500** | 71.5 | $0.04 | $0.10 | 32,768 |  |
| 7 | `liquid/lfm-2-24b-a2b` | **1,586,667** | 47.6 | $0.03 | $0.12 | 32,768 |  |
| 8 | `qwen/qwen3-8b` | **1,564,000** | 78.2 | $0.05 | $0.40 | 40,960 |  |
| 9 | `meta-llama/llama-3-8b-instruct` | **1,526,667** | 45.8 | $0.03 | $0.04 | 8,192 |  |
| 10 | `google/gemma-3-4b-it` | **1,510,000** | 60.4 | $0.04 | $0.08 | 131,072 |  |

### momus (Critic — Deep-reasoning)

**Performance Ranking — momus**

| Rank | Model | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|
| 1 | `z-ai/glm-5.1` | **94.7** | $1.05 | $3.50 | 202,752 |  |
| 2 | `openai/gpt-5.4-pro` | **92.4** | $30.00 | $180.00 | 1,050,000 |  |
| 3 | `deepseek/deepseek-v4-pro` | **92.0** | $1.74 | $3.48 | 1,048,576 |  |
| 4 | `openai/o3-pro` | **91.9** | $20.00 | $80.00 | 200,000 |  |
| 5 | `z-ai/glm-5` | **91.2** | $0.60 | $2.08 | 202,752 |  |
| 6 | `z-ai/glm-5-turbo` | **90.8** | $1.20 | $4.00 | 202,752 |  |
| 7 | `openai/gpt-5.4` | **90.1** | $2.50 | $15.00 | 1,050,000 |  |
| 8 | `anthropic/claude-opus-4` | **90.0** | $15.00 | $75.00 | 200,000 |  |
| 9 | `qwen/qwen3-coder-next` | **89.7** | $0.15 | $0.80 | 262,144 |  |
| 10 | `z-ai/glm-5v-turbo` | **88.7** | $1.20 | $4.00 | 202,752 |  |

**Cost/Performance Ranking — momus**

| Rank | Model | Cost/Perf | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **7,560,000** | 75.6 | $0.01 | $0.03 | 131,072 |  |
| 2 | `ibm-granite/granite-4.0-h-micro` | **2,800,000** | 47.6 | $0.02 | $0.11 | 131,000 |  |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **2,445,000** | 48.9 | $0.02 | $0.05 | 16,384 |  |
| 4 | `qwen/qwen-turbo` | **2,304,615** | 74.9 | $0.03 | $0.13 | 131,072 |  |
| 5 | `meta-llama/llama-3.2-1b-instruct` | **1,874,074** | 50.6 | $0.03 | $0.20 | 60,000 |  |
| 6 | `qwen/qwen-2.5-7b-instruct` | **1,787,500** | 71.5 | $0.04 | $0.10 | 32,768 |  |
| 7 | `liquid/lfm-2-24b-a2b` | **1,586,667** | 47.6 | $0.03 | $0.12 | 32,768 |  |
| 8 | `qwen/qwen3-8b` | **1,564,000** | 78.2 | $0.05 | $0.40 | 40,960 |  |
| 9 | `meta-llama/llama-3-8b-instruct` | **1,526,667** | 45.8 | $0.03 | $0.04 | 8,192 |  |
| 10 | `google/gemma-3-4b-it` | **1,510,000** | 60.4 | $0.04 | $0.08 | 131,072 |  |

### librarian (Research — Speed-heavy)

**Performance Ranking — librarian**

| Rank | Model | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|
| 1 | `nvidia/deepseek-ai/deepseek-v4-flash` | **80.2** | $0.00 | $0.00 | 1,000,000 | ✓ |
| 2 | `nvidia/stepfun-ai/step-3.5-flash` | **80.0** | $0.00 | $0.00 | 256,000 | ✓ |
| 3 | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | **78.5** | $0.05 | $0.20 | 1,000,000 |  |
| 4 | `nvidia/qwen/qwen3.5-122b-a10b` | **78.3** | $0.00 | $0.00 | 262,000 | ✓ |
| 5 | `nvidia/z-ai/glm-4.7` | **78.0** | $0.00 | $0.00 | 2,540,000 | ✓ |
| 6 | `nvidia/deepseek-ai/deepseek-v4-pro` | **77.7** | $0.00 | $0.00 | 1,000,000 | ✓ |
| 7 | `nvidia/qwen/qwen3.5-9b` | **77.3** | $0.05 | $0.15 | 256,000 |  |
| 8 | `openai/gpt-5.4-nano` | **76.8** | $0.20 | $1.25 | 400,000 |  |
| 9 | `nvidia/nvidia/nemotron-3-super-120b-a12b` | **76.6** | $0.10 | $0.50 | 1,000,000 |  |
| 10 | `nvidia/microsoft/phi-4-multimodal-instruct` | **74.0** | $0.00 | $0.00 | 128,000 | ✓ |

**Cost/Performance Ranking — librarian**

| Rank | Model | Cost/Perf | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|---|
| 1 | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | **1,569,000** | 78.5 | $0.05 | $0.20 | 1,000,000 |  |
| 2 | `nvidia/qwen/qwen3.5-9b` | **1,546,100** | 77.3 | $0.05 | $0.15 | 256,000 |  |
| 3 | `nvidia/mistralai/mistral-small-24b-instruct` | **1,191,000** | 59.5 | $0.05 | $0.08 | 33,000 |  |
| 4 | `nvidia/google/gemma-4-26b-a4b-it` | **915,562** | 73.2 | $0.08 | $0.35 | 256,000 |  |
| 5 | `nvidia/microsoft/phi-4-mini-instruct` | **871,067** | 65.3 | $0.075 | $0.30 | 128,000 |  |
| 6 | `nvidia/nvidia/nemotron-3-super-120b-a12b` | **766,050** | 76.6 | $0.10 | $0.50 | 1,000,000 |  |
| 7 | `nvidia/mistral-ai/mistral-small-4-119b-2603` | **679,500** | 68.0 | $0.10 | $0.40 | 256,000 |  |
| 8 | `nvidia/mistralai/mistral-small-3.1-24b-instruct-2503` | **595,500** | 59.6 | $0.10 | $0.30 | 128,000 |  |
| 9 | `nvidia/meta-llama/llama-3.3-nemotron-super-49b-v1.5` | **572,550** | 57.3 | $0.10 | $0.40 | 131,000 |  |
| 10 | `openai/gpt-5.4-nano` | **383,900** | 76.8 | $0.20 | $1.25 | 400,000 |  |

### multimodal-looker (Vision — Vision-heavy)

**Performance Ranking — multimodal-looker**

| Rank | Model | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|
| 1 | `openai/gpt-5.4` | **94.0** | $2.50 | $15.00 | 1,050,000 |  |
| 2 | `deepseek/deepseek-v4-pro` | **93.8** | $1.74 | $3.48 | 1,048,576 |  |
| 3 | `google/gemini-2.5-pro` | **93.6** | $1.25 | $10.00 | 1,048,576 |  |
| 4 | `openai/gpt-5.4-pro` | **93.5** | $30.00 | $180.00 | 1,050,000 |  |
| 5 | `deepseek/deepseek-v4-flash` | **92.1** | $0.14 | $0.28 | 1,048,576 |  |
| 6 | `qwen/qwen3-coder-plus` | **92.0** | $0.65 | $3.25 | 1,000,000 |  |
| 7 | `qwen/qwen3.6-plus` | **91.6** | $0.33 | $1.95 | 1,000,000 |  |
| 8 | `openai/gpt-5.4-mini` | **91.6** | $0.75 | $4.50 | 400,000 |  |
| 9 | `anthropic/claude-sonnet-4` | **91.4** | $3.00 | $15.00 | 1,000,000 |  |
| 10 | `openai/gpt-5.3-codex` | **90.9** | $1.75 | $14.00 | 400,000 |  |

**Cost/Performance Ranking — multimodal-looker**

| Rank | Model | Cost/Perf | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **8,200,000** | 82.0 | $0.01 | $0.03 | 131,072 |  |
| 2 | `ibm-granite/granite-4.0-h-micro` | **3,547,059** | 60.3 | $0.02 | $0.11 | 131,000 |  |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **2,915,000** | 58.3 | $0.02 | $0.05 | 16,384 |  |
| 4 | `qwen/qwen-turbo` | **2,507,692** | 81.5 | $0.03 | $0.13 | 131,072 |  |
| 5 | `meta-llama/llama-3.2-1b-instruct` | **2,259,259** | 61.0 | $0.03 | $0.20 | 60,000 |  |
| 6 | `meta-llama/llama-3-8b-instruct` | **1,843,333** | 55.3 | $0.03 | $0.04 | 8,192 |  |
| 7 | `qwen/qwen-2.5-7b-instruct` | **1,817,500** | 72.7 | $0.04 | $0.10 | 32,768 |  |
| 8 | `liquid/lfm-2-24b-a2b` | **1,806,667** | 54.2 | $0.03 | $0.12 | 32,768 |  |
| 9 | `google/gemma-3-4b-it` | **1,797,500** | 71.9 | $0.04 | $0.08 | 131,072 |  |
| 10 | `google/gemma-3-12b-it` | **1,797,500** | 71.9 | $0.04 | $0.13 | 131,072 |  |

### atlas (Knowledge — Reasoning-heavy)

**Performance Ranking — atlas**

| Rank | Model | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|
| 1 | `z-ai/glm-5.1` | **94.5** | $1.05 | $3.50 | 202,752 |  |
| 2 | `openai/gpt-5.4-pro` | **92.0** | $30.00 | $180.00 | 1,050,000 |  |
| 3 | `deepseek/deepseek-v4-pro` | **91.9** | $1.74 | $3.48 | 1,048,576 |  |
| 4 | `openai/o3-pro` | **91.8** | $20.00 | $80.00 | 200,000 |  |
| 5 | `z-ai/glm-5` | **91.0** | $0.60 | $2.08 | 202,752 |  |
| 6 | `z-ai/glm-5-turbo` | **90.5** | $1.20 | $4.00 | 202,752 |  |
| 7 | `anthropic/claude-opus-4` | **89.7** | $15.00 | $75.00 | 200,000 |  |
| 8 | `qwen/qwen3-coder-next` | **89.5** | $0.15 | $0.80 | 262,144 |  |
| 9 | `openai/gpt-5.4` | **89.3** | $2.50 | $15.00 | 1,050,000 |  |
| 10 | `openai/o1-pro` | **88.6** | $150.00 | $600.00 | 200,000 |  |

**Cost/Performance Ranking — atlas**

| Rank | Model | Cost/Perf | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **7,550,000** | 75.5 | $0.01 | $0.03 | 131,072 |  |
| 2 | `ibm-granite/granite-4.0-h-micro` | **2,800,000** | 47.6 | $0.02 | $0.11 | 131,000 |  |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **2,435,000** | 48.7 | $0.02 | $0.05 | 16,384 |  |
| 4 | `qwen/qwen-turbo` | **2,301,538** | 74.8 | $0.03 | $0.13 | 131,072 |  |
| 5 | `meta-llama/llama-3.2-1b-instruct` | **1,866,667** | 50.4 | $0.03 | $0.20 | 60,000 |  |
| 6 | `qwen/qwen-2.5-7b-instruct` | **1,785,000** | 71.4 | $0.04 | $0.10 | 32,768 |  |
| 7 | `liquid/lfm-2-24b-a2b` | **1,586,667** | 47.6 | $0.03 | $0.12 | 32,768 |  |
| 8 | `qwen/qwen3-8b` | **1,562,000** | 78.1 | $0.05 | $0.40 | 40,960 |  |
| 9 | `meta-llama/llama-3-8b-instruct` | **1,520,000** | 45.6 | $0.03 | $0.04 | 8,192 |  |
| 10 | `google/gemma-3-4b-it` | **1,510,000** | 60.4 | $0.04 | $0.08 | 131,072 |  |

### sisyphus-junior (Junior Orchestrator — Junior/orchestration)

**Performance Ranking — sisyphus-junior**

| Rank | Model | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|
| 1 | `deepseek/deepseek-v4-pro` | **94.0** | $1.74 | $3.48 | 1,048,576 |  |
| 2 | `openai/gpt-5.4` | **92.8** | $2.50 | $15.00 | 1,050,000 |  |
| 3 | `qwen/qwen3-coder-plus` | **91.7** | $0.65 | $3.25 | 1,000,000 |  |
| 4 | `deepseek/deepseek-v4-flash` | **91.4** | $0.14 | $0.28 | 1,048,576 |  |
| 5 | `google/gemini-2.5-pro` | **91.4** | $1.25 | $10.00 | 1,048,576 |  |
| 6 | `z-ai/glm-5.1` | **90.9** | $1.05 | $3.50 | 202,752 |  |
| 7 | `openai/gpt-5.4-pro` | **90.5** | $30.00 | $180.00 | 1,050,000 |  |
| 8 | `qwen/qwen3.6-plus` | **89.4** | $0.33 | $1.95 | 1,000,000 |  |
| 9 | `z-ai/glm-5` | **88.8** | $0.60 | $2.08 | 202,752 |  |
| 10 | `qwen/qwen3-coder-next` | **88.6** | $0.15 | $0.80 | 262,144 |  |

**Cost/Performance Ranking — sisyphus-junior**

| Rank | Model | Cost/Perf | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **7,590,000** | 75.9 | $0.01 | $0.03 | 131,072 |  |
| 2 | `ibm-granite/granite-4.0-h-micro` | **3,276,471** | 55.7 | $0.02 | $0.11 | 131,000 |  |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **2,705,000** | 54.1 | $0.02 | $0.05 | 16,384 |  |
| 4 | `qwen/qwen-turbo` | **2,316,923** | 75.3 | $0.03 | $0.13 | 131,072 |  |
| 5 | `meta-llama/llama-3.2-1b-instruct` | **2,037,037** | 55.0 | $0.03 | $0.20 | 60,000 |  |
| 6 | `liquid/lfm-2-24b-a2b` | **1,770,000** | 53.1 | $0.03 | $0.12 | 32,768 |  |
| 7 | `qwen/qwen-2.5-7b-instruct` | **1,760,000** | 70.4 | $0.04 | $0.10 | 32,768 |  |
| 8 | `meta-llama/llama-3-8b-instruct` | **1,733,333** | 52.0 | $0.03 | $0.04 | 8,192 |  |
| 9 | `google/gemma-3-4b-it` | **1,610,000** | 64.4 | $0.04 | $0.08 | 131,072 |  |
| 10 | `google/gemma-3-12b-it` | **1,610,000** | 64.4 | $0.04 | $0.13 | 131,072 |  |

---

## Category Rankings

### visual-engineering (Vision-heavy)

**Performance Ranking — visual-engineering**

| Rank | Model | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|
| 1 | `openai/gpt-5.4` | **94.0** | $2.50 | $15.00 | 1,050,000 |  |
| 2 | `deepseek/deepseek-v4-pro` | **93.8** | $1.74 | $3.48 | 1,048,576 |  |
| 3 | `google/gemini-2.5-pro` | **93.6** | $1.25 | $10.00 | 1,048,576 |  |
| 4 | `openai/gpt-5.4-pro` | **93.5** | $30.00 | $180.00 | 1,050,000 |  |
| 5 | `deepseek/deepseek-v4-flash` | **92.1** | $0.14 | $0.28 | 1,048,576 |  |
| 6 | `qwen/qwen3-coder-plus` | **92.0** | $0.65 | $3.25 | 1,000,000 |  |
| 7 | `qwen/qwen3.6-plus` | **91.6** | $0.33 | $1.95 | 1,000,000 |  |
| 8 | `openai/gpt-5.4-mini` | **91.6** | $0.75 | $4.50 | 400,000 |  |
| 9 | `anthropic/claude-sonnet-4` | **91.4** | $3.00 | $15.00 | 1,000,000 |  |
| 10 | `openai/gpt-5.3-codex` | **90.9** | $1.75 | $14.00 | 400,000 |  |

**Cost/Performance Ranking — visual-engineering**

| Rank | Model | Cost/Perf | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **8,200,000** | 82.0 | $0.01 | $0.03 | 131,072 |  |
| 2 | `ibm-granite/granite-4.0-h-micro` | **3,547,059** | 60.3 | $0.02 | $0.11 | 131,000 |  |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **2,915,000** | 58.3 | $0.02 | $0.05 | 16,384 |  |
| 4 | `qwen/qwen-turbo` | **2,507,692** | 81.5 | $0.03 | $0.13 | 131,072 |  |
| 5 | `meta-llama/llama-3.2-1b-instruct` | **2,259,259** | 61.0 | $0.03 | $0.20 | 60,000 |  |
| 6 | `meta-llama/llama-3-8b-instruct` | **1,843,333** | 55.3 | $0.03 | $0.04 | 8,192 |  |
| 7 | `qwen/qwen-2.5-7b-instruct` | **1,817,500** | 72.7 | $0.04 | $0.10 | 32,768 |  |
| 8 | `liquid/lfm-2-24b-a2b` | **1,806,667** | 54.2 | $0.03 | $0.12 | 32,768 |  |
| 9 | `google/gemma-3-4b-it` | **1,797,500** | 71.9 | $0.04 | $0.08 | 131,072 |  |
| 10 | `google/gemma-3-12b-it` | **1,797,500** | 71.9 | $0.04 | $0.13 | 131,072 |  |

### ultrabrain (Deep-reasoning)

**Performance Ranking — ultrabrain**

| Rank | Model | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|
| 1 | `z-ai/glm-5.1` | **94.7** | $1.05 | $3.50 | 202,752 |  |
| 2 | `openai/gpt-5.4-pro` | **92.4** | $30.00 | $180.00 | 1,050,000 |  |
| 3 | `deepseek/deepseek-v4-pro` | **92.0** | $1.74 | $3.48 | 1,048,576 |  |
| 4 | `openai/o3-pro` | **91.9** | $20.00 | $80.00 | 200,000 |  |
| 5 | `z-ai/glm-5` | **91.2** | $0.60 | $2.08 | 202,752 |  |
| 6 | `z-ai/glm-5-turbo` | **90.8** | $1.20 | $4.00 | 202,752 |  |
| 7 | `openai/gpt-5.4` | **90.1** | $2.50 | $15.00 | 1,050,000 |  |
| 8 | `anthropic/claude-opus-4` | **90.0** | $15.00 | $75.00 | 200,000 |  |
| 9 | `qwen/qwen3-coder-next` | **89.7** | $0.15 | $0.80 | 262,144 |  |
| 10 | `z-ai/glm-5v-turbo` | **88.7** | $1.20 | $4.00 | 202,752 |  |

**Cost/Performance Ranking — ultrabrain**

| Rank | Model | Cost/Perf | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **7,560,000** | 75.6 | $0.01 | $0.03 | 131,072 |  |
| 2 | `ibm-granite/granite-4.0-h-micro` | **2,800,000** | 47.6 | $0.02 | $0.11 | 131,000 |  |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **2,445,000** | 48.9 | $0.02 | $0.05 | 16,384 |  |
| 4 | `qwen/qwen-turbo` | **2,304,615** | 74.9 | $0.03 | $0.13 | 131,072 |  |
| 5 | `meta-llama/llama-3.2-1b-instruct` | **1,874,074** | 50.6 | $0.03 | $0.20 | 60,000 |  |
| 6 | `qwen/qwen-2.5-7b-instruct` | **1,787,500** | 71.5 | $0.04 | $0.10 | 32,768 |  |
| 7 | `liquid/lfm-2-24b-a2b` | **1,586,667** | 47.6 | $0.03 | $0.12 | 32,768 |  |
| 8 | `qwen/qwen3-8b` | **1,564,000** | 78.2 | $0.05 | $0.40 | 40,960 |  |
| 9 | `meta-llama/llama-3-8b-instruct` | **1,526,667** | 45.8 | $0.03 | $0.04 | 8,192 |  |
| 10 | `google/gemma-3-4b-it` | **1,510,000** | 60.4 | $0.04 | $0.08 | 131,072 |  |

### deep (Deep-reasoning)

**Performance Ranking — deep**

| Rank | Model | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|
| 1 | `z-ai/glm-5.1` | **94.7** | $1.05 | $3.50 | 202,752 |  |
| 2 | `openai/gpt-5.4-pro` | **92.4** | $30.00 | $180.00 | 1,050,000 |  |
| 3 | `deepseek/deepseek-v4-pro` | **92.0** | $1.74 | $3.48 | 1,048,576 |  |
| 4 | `openai/o3-pro` | **91.9** | $20.00 | $80.00 | 200,000 |  |
| 5 | `z-ai/glm-5` | **91.2** | $0.60 | $2.08 | 202,752 |  |
| 6 | `z-ai/glm-5-turbo` | **90.8** | $1.20 | $4.00 | 202,752 |  |
| 7 | `openai/gpt-5.4` | **90.1** | $2.50 | $15.00 | 1,050,000 |  |
| 8 | `anthropic/claude-opus-4` | **90.0** | $15.00 | $75.00 | 200,000 |  |
| 9 | `qwen/qwen3-coder-next` | **89.7** | $0.15 | $0.80 | 262,144 |  |
| 10 | `z-ai/glm-5v-turbo` | **88.7** | $1.20 | $4.00 | 202,752 |  |

**Cost/Performance Ranking — deep**

| Rank | Model | Cost/Perf | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **7,560,000** | 75.6 | $0.01 | $0.03 | 131,072 |  |
| 2 | `ibm-granite/granite-4.0-h-micro` | **2,800,000** | 47.6 | $0.02 | $0.11 | 131,000 |  |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **2,445,000** | 48.9 | $0.02 | $0.05 | 16,384 |  |
| 4 | `qwen/qwen-turbo` | **2,304,615** | 74.9 | $0.03 | $0.13 | 131,072 |  |
| 5 | `meta-llama/llama-3.2-1b-instruct` | **1,874,074** | 50.6 | $0.03 | $0.20 | 60,000 |  |
| 6 | `qwen/qwen-2.5-7b-instruct` | **1,787,500** | 71.5 | $0.04 | $0.10 | 32,768 |  |
| 7 | `liquid/lfm-2-24b-a2b` | **1,586,667** | 47.6 | $0.03 | $0.12 | 32,768 |  |
| 8 | `qwen/qwen3-8b` | **1,564,000** | 78.2 | $0.05 | $0.40 | 40,960 |  |
| 9 | `meta-llama/llama-3-8b-instruct` | **1,526,667** | 45.8 | $0.03 | $0.04 | 8,192 |  |
| 10 | `google/gemma-3-4b-it` | **1,510,000** | 60.4 | $0.04 | $0.08 | 131,072 |  |

### artistry (Deep-reasoning)

**Performance Ranking — artistry**

| Rank | Model | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|
| 1 | `z-ai/glm-5.1` | **94.7** | $1.05 | $3.50 | 202,752 |  |
| 2 | `openai/gpt-5.4-pro` | **92.4** | $30.00 | $180.00 | 1,050,000 |  |
| 3 | `deepseek/deepseek-v4-pro` | **92.0** | $1.74 | $3.48 | 1,048,576 |  |
| 4 | `openai/o3-pro` | **91.9** | $20.00 | $80.00 | 200,000 |  |
| 5 | `z-ai/glm-5` | **91.2** | $0.60 | $2.08 | 202,752 |  |
| 6 | `z-ai/glm-5-turbo` | **90.8** | $1.20 | $4.00 | 202,752 |  |
| 7 | `openai/gpt-5.4` | **90.1** | $2.50 | $15.00 | 1,050,000 |  |
| 8 | `anthropic/claude-opus-4` | **90.0** | $15.00 | $75.00 | 200,000 |  |
| 9 | `qwen/qwen3-coder-next` | **89.7** | $0.15 | $0.80 | 262,144 |  |
| 10 | `z-ai/glm-5v-turbo` | **88.7** | $1.20 | $4.00 | 202,752 |  |

**Cost/Performance Ranking — artistry**

| Rank | Model | Cost/Perf | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **7,560,000** | 75.6 | $0.01 | $0.03 | 131,072 |  |
| 2 | `ibm-granite/granite-4.0-h-micro` | **2,800,000** | 47.6 | $0.02 | $0.11 | 131,000 |  |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **2,445,000** | 48.9 | $0.02 | $0.05 | 16,384 |  |
| 4 | `qwen/qwen-turbo` | **2,304,615** | 74.9 | $0.03 | $0.13 | 131,072 |  |
| 5 | `meta-llama/llama-3.2-1b-instruct` | **1,874,074** | 50.6 | $0.03 | $0.20 | 60,000 |  |
| 6 | `qwen/qwen-2.5-7b-instruct` | **1,787,500** | 71.5 | $0.04 | $0.10 | 32,768 |  |
| 7 | `liquid/lfm-2-24b-a2b` | **1,586,667** | 47.6 | $0.03 | $0.12 | 32,768 |  |
| 8 | `qwen/qwen3-8b` | **1,564,000** | 78.2 | $0.05 | $0.40 | 40,960 |  |
| 9 | `meta-llama/llama-3-8b-instruct` | **1,526,667** | 45.8 | $0.03 | $0.04 | 8,192 |  |
| 10 | `google/gemma-3-4b-it` | **1,510,000** | 60.4 | $0.04 | $0.08 | 131,072 |  |

### quick (Quick/low)

**Performance Ranking — quick**

| Rank | Model | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|
| 1 | `deepseek/deepseek-v4-flash` | **100** | $0.14 | $0.28 | 1,048,576 |  |
| 2 | `openrouter/pareto-code` | **100** | $-1000000.00 | $-1000000.00 | 200,000 |  |
| 3 | `google/gemma-4-26b-a4b-it` | **100** | $0.06 | $0.33 | 262,144 |  |
| 4 | `qwen/qwen3.6-plus` | **100** | $0.33 | $1.95 | 1,000,000 |  |
| 5 | `openai/gpt-5.4-nano` | **100** | $0.20 | $1.25 | 400,000 |  |
| 6 | `openai/gpt-5.4-mini` | **100** | $0.75 | $4.50 | 400,000 |  |
| 7 | `mistralai/mistral-small-2603` | **100** | $0.15 | $0.60 | 262,144 |  |
| 8 | `qwen/qwen3.5-9b` | **100** | $0.10 | $0.15 | 262,144 |  |
| 9 | `google/gemini-3.1-flash-lite-preview` | **100** | $0.25 | $1.50 | 1,048,576 |  |
| 10 | `qwen/qwen3.5-35b-a3b` | **100** | $0.16 | $1.30 | 262,144 |  |

**Cost/Performance Ranking — quick**

| Rank | Model | Cost/Perf | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **10,000,000** | 100 | $0.01 | $0.03 | 131,072 |  |
| 2 | `ibm-granite/granite-4.0-h-micro` | **5,817,647** | 98.9 | $0.02 | $0.11 | 131,000 |  |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **4,765,000** | 95.3 | $0.02 | $0.05 | 16,384 |  |
| 4 | `meta-llama/llama-3.2-1b-instruct` | **3,507,407** | 94.7 | $0.03 | $0.20 | 60,000 |  |
| 5 | `meta-llama/llama-3-8b-instruct` | **3,150,000** | 94.5 | $0.03 | $0.04 | 8,192 |  |
| 6 | `qwen/qwen-turbo` | **3,076,923** | 100 | $0.03 | $0.13 | 131,072 |  |
| 7 | `liquid/lfm-2-24b-a2b` | **3,030,000** | 90.9 | $0.03 | $0.12 | 32,768 |  |
| 8 | `amazon/nova-micro-v1` | **2,825,714** | 98.9 | $0.04 | $0.14 | 128,000 |  |
| 9 | `cohere/command-r7b-12-2024` | **2,637,333** | 98.9 | $0.04 | $0.15 | 128,000 |  |
| 10 | `nvidia/nemotron-nano-9b-v2` | **2,500,000** | 100 | $0.04 | $0.16 | 131,072 |  |

### unspecified-low (Quick/low)

**Performance Ranking — unspecified-low**

| Rank | Model | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|
| 1 | `deepseek/deepseek-v4-flash` | **100** | $0.14 | $0.28 | 1,048,576 |  |
| 2 | `openrouter/pareto-code` | **100** | $-1000000.00 | $-1000000.00 | 200,000 |  |
| 3 | `google/gemma-4-26b-a4b-it` | **100** | $0.06 | $0.33 | 262,144 |  |
| 4 | `qwen/qwen3.6-plus` | **100** | $0.33 | $1.95 | 1,000,000 |  |
| 5 | `openai/gpt-5.4-nano` | **100** | $0.20 | $1.25 | 400,000 |  |
| 6 | `openai/gpt-5.4-mini` | **100** | $0.75 | $4.50 | 400,000 |  |
| 7 | `mistralai/mistral-small-2603` | **100** | $0.15 | $0.60 | 262,144 |  |
| 8 | `qwen/qwen3.5-9b` | **100** | $0.10 | $0.15 | 262,144 |  |
| 9 | `google/gemini-3.1-flash-lite-preview` | **100** | $0.25 | $1.50 | 1,048,576 |  |
| 10 | `qwen/qwen3.5-35b-a3b` | **100** | $0.16 | $1.30 | 262,144 |  |

**Cost/Performance Ranking — unspecified-low**

| Rank | Model | Cost/Perf | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **10,000,000** | 100 | $0.01 | $0.03 | 131,072 |  |
| 2 | `ibm-granite/granite-4.0-h-micro` | **5,817,647** | 98.9 | $0.02 | $0.11 | 131,000 |  |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **4,765,000** | 95.3 | $0.02 | $0.05 | 16,384 |  |
| 4 | `meta-llama/llama-3.2-1b-instruct` | **3,507,407** | 94.7 | $0.03 | $0.20 | 60,000 |  |
| 5 | `meta-llama/llama-3-8b-instruct` | **3,150,000** | 94.5 | $0.03 | $0.04 | 8,192 |  |
| 6 | `qwen/qwen-turbo` | **3,076,923** | 100 | $0.03 | $0.13 | 131,072 |  |
| 7 | `liquid/lfm-2-24b-a2b` | **3,030,000** | 90.9 | $0.03 | $0.12 | 32,768 |  |
| 8 | `amazon/nova-micro-v1` | **2,825,714** | 98.9 | $0.04 | $0.14 | 128,000 |  |
| 9 | `cohere/command-r7b-12-2024` | **2,637,333** | 98.9 | $0.04 | $0.15 | 128,000 |  |
| 10 | `nvidia/nemotron-nano-9b-v2` | **2,500,000** | 100 | $0.04 | $0.16 | 131,072 |  |

### unspecified-high (Reasoning-heavy)

**Performance Ranking — unspecified-high**

| Rank | Model | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|
| 1 | `z-ai/glm-5.1` | **94.5** | $1.05 | $3.50 | 202,752 |  |
| 2 | `openai/gpt-5.4-pro` | **92.0** | $30.00 | $180.00 | 1,050,000 |  |
| 3 | `deepseek/deepseek-v4-pro` | **91.9** | $1.74 | $3.48 | 1,048,576 |  |
| 4 | `openai/o3-pro` | **91.8** | $20.00 | $80.00 | 200,000 |  |
| 5 | `z-ai/glm-5` | **91.0** | $0.60 | $2.08 | 202,752 |  |
| 6 | `z-ai/glm-5-turbo` | **90.5** | $1.20 | $4.00 | 202,752 |  |
| 7 | `anthropic/claude-opus-4` | **89.7** | $15.00 | $75.00 | 200,000 |  |
| 8 | `qwen/qwen3-coder-next` | **89.5** | $0.15 | $0.80 | 262,144 |  |
| 9 | `openai/gpt-5.4` | **89.3** | $2.50 | $15.00 | 1,050,000 |  |
| 10 | `openai/o1-pro` | **88.6** | $150.00 | $600.00 | 200,000 |  |

**Cost/Performance Ranking — unspecified-high**

| Rank | Model | Cost/Perf | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|
| 1 | `mistralai/mistral-nemo` | **7,550,000** | 75.5 | $0.01 | $0.03 | 131,072 |  |
| 2 | `ibm-granite/granite-4.0-h-micro` | **2,800,000** | 47.6 | $0.02 | $0.11 | 131,000 |  |
| 3 | `meta-llama/llama-3.1-8b-instruct` | **2,435,000** | 48.7 | $0.02 | $0.05 | 16,384 |  |
| 4 | `qwen/qwen-turbo` | **2,301,538** | 74.8 | $0.03 | $0.13 | 131,072 |  |
| 5 | `meta-llama/llama-3.2-1b-instruct` | **1,866,667** | 50.4 | $0.03 | $0.20 | 60,000 |  |
| 6 | `qwen/qwen-2.5-7b-instruct` | **1,785,000** | 71.4 | $0.04 | $0.10 | 32,768 |  |
| 7 | `liquid/lfm-2-24b-a2b` | **1,586,667** | 47.6 | $0.03 | $0.12 | 32,768 |  |
| 8 | `qwen/qwen3-8b` | **1,562,000** | 78.1 | $0.05 | $0.40 | 40,960 |  |
| 9 | `meta-llama/llama-3-8b-instruct` | **1,520,000** | 45.6 | $0.03 | $0.04 | 8,192 |  |
| 10 | `google/gemma-3-4b-it` | **1,510,000** | 60.4 | $0.04 | $0.08 | 131,072 |  |

### writing (Writing/research)

**Performance Ranking — writing**

| Rank | Model | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|
| 1 | `nvidia/deepseek-ai/deepseek-v4-pro` | **88.9** | $0.00 | $0.00 | 1,000,000 | ✓ |
| 2 | `nvidia/z-ai/glm-4.7` | **87.7** | $0.00 | $0.00 | 2,540,000 | ✓ |
| 3 | `nvidia/deepseek-ai/deepseek-v4-flash` | **83.2** | $0.00 | $0.00 | 1,000,000 | ✓ |
| 4 | `nvidia/stepfun-ai/step-3.5-flash` | **82.7** | $0.00 | $0.00 | 256,000 | ✓ |
| 5 | `nvidia/minimax/minimax-m2.7` | **81.4** | $0.00 | $0.00 | 3,050,000 | ✓ |
| 6 | `nvidia/qwen/qwen3.5-122b-a10b` | **80.8** | $0.00 | $0.00 | 262,000 | ✓ |
| 7 | `nvidia/nvidia/nemotron-3-super-120b-a12b` | **77.7** | $0.10 | $0.50 | 1,000,000 |  |
| 8 | `openai/gpt-5.4-nano` | **77.5** | $0.20 | $1.25 | 400,000 |  |
| 9 | `nvidia/qwen/qwen3.5-9b` | **76.4** | $0.05 | $0.15 | 256,000 |  |
| 10 | `nvidia/mistral-ai/mistral-small-4-119b-2603` | **75.3** | $0.10 | $0.40 | 256,000 |  |

**Cost/Performance Ranking — writing**

| Rank | Model | Cost/Perf | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|
| 1 | `nvidia/qwen/qwen3.5-9b` | **1,527,800** | 76.4 | $0.05 | $0.15 | 256,000 |  |
| 2 | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | **1,499,000** | 75.0 | $0.05 | $0.20 | 1,000,000 |  |
| 3 | `nvidia/mistralai/mistral-small-24b-instruct` | **1,211,000** | 60.5 | $0.05 | $0.08 | 33,000 |  |
| 4 | `nvidia/google/gemma-4-26b-a4b-it` | **909,500** | 72.8 | $0.08 | $0.35 | 256,000 |  |
| 5 | `nvidia/nvidia/nemotron-3-super-120b-a12b` | **776,900** | 77.7 | $0.10 | $0.50 | 1,000,000 |  |
| 6 | `nvidia/mistral-ai/mistral-small-4-119b-2603` | **753,500** | 75.3 | $0.10 | $0.40 | 256,000 |  |
| 7 | `nvidia/microsoft/phi-4-mini-instruct` | **731,867** | 54.9 | $0.075 | $0.30 | 128,000 |  |
| 8 | `nvidia/meta-llama/llama-3.3-nemotron-super-49b-v1.5` | **639,900** | 64.0 | $0.10 | $0.40 | 131,000 |  |
| 9 | `nvidia/mistralai/mistral-small-3.1-24b-instruct-2503` | **625,000** | 62.5 | $0.10 | $0.30 | 128,000 |  |
| 10 | `openai/gpt-5.4-nano` | **387,750** | 77.5 | $0.20 | $1.25 | 400,000 |  |

---

## Summary: Best Model per Agent (Performance)

| Agent | Best Model | Score | 2nd Best | Score | 3rd Best | Score |
|---|---|---|---|---|---|---|
| sisyphus | `z-ai/glm-5.1` | **94.5** | `openai/gpt-5.4-pro` | 92.0 | `deepseek/deepseek-v4-pro` | 91.9 |
| hephaestus | `qwen/qwen3-coder-next` | **90.7** | `z-ai/glm-5.1` | 90.5 | `openai/gpt-5.4` | 89.6 |
| oracle | `z-ai/glm-5.1` | **94.7** | `openai/gpt-5.4-pro` | 92.4 | `deepseek/deepseek-v4-pro` | 92.0 |
| explore | `nvidia/deepseek-ai/deepseek-v4-flash` | **80.2** | `nvidia/stepfun-ai/step-3.5-flash` | 80.0 | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | 78.5 |
| prometheus | `z-ai/glm-5.1` | **94.5** | `openai/gpt-5.4-pro` | 92.0 | `deepseek/deepseek-v4-pro` | 91.9 |
| metis | `z-ai/glm-5.1` | **94.7** | `openai/gpt-5.4-pro` | 92.4 | `deepseek/deepseek-v4-pro` | 92.0 |
| momus | `z-ai/glm-5.1` | **94.7** | `openai/gpt-5.4-pro` | 92.4 | `deepseek/deepseek-v4-pro` | 92.0 |
| librarian | `nvidia/deepseek-ai/deepseek-v4-flash` | **80.2** | `nvidia/stepfun-ai/step-3.5-flash` | 80.0 | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | 78.5 |
| multimodal-looker | `openai/gpt-5.4` | **94.0** | `deepseek/deepseek-v4-pro` | 93.8 | `google/gemini-2.5-pro` | 93.6 |
| atlas | `z-ai/glm-5.1` | **94.5** | `openai/gpt-5.4-pro` | 92.0 | `deepseek/deepseek-v4-pro` | 91.9 |
| sisyphus-junior | `deepseek/deepseek-v4-pro` | **94.0** | `openai/gpt-5.4` | 92.8 | `qwen/qwen3-coder-plus` | 91.7 |

## Summary: Best Model per Category (Performance)

| Category | Best Model | Score | 2nd Best | Score | 3rd Best | Score |
|---|---|---|---|---|---|---|
| visual-engineering | `openai/gpt-5.4` | **94.0** | `deepseek/deepseek-v4-pro` | 93.8 | `google/gemini-2.5-pro` | 93.6 |
| ultrabrain | `z-ai/glm-5.1` | **94.7** | `openai/gpt-5.4-pro` | 92.4 | `deepseek/deepseek-v4-pro` | 92.0 |
| deep | `z-ai/glm-5.1` | **94.7** | `openai/gpt-5.4-pro` | 92.4 | `deepseek/deepseek-v4-pro` | 92.0 |
| artistry | `z-ai/glm-5.1` | **94.7** | `openai/gpt-5.4-pro` | 92.4 | `deepseek/deepseek-v4-pro` | 92.0 |
| quick | `deepseek/deepseek-v4-flash` | **100** | `openrouter/pareto-code` | 100 | `google/gemma-4-26b-a4b-it` | 100 |
| unspecified-low | `deepseek/deepseek-v4-flash` | **100** | `openrouter/pareto-code` | 100 | `google/gemma-4-26b-a4b-it` | 100 |
| unspecified-high | `z-ai/glm-5.1` | **94.5** | `openai/gpt-5.4-pro` | 92.0 | `deepseek/deepseek-v4-pro` | 91.9 |
| writing | `nvidia/deepseek-ai/deepseek-v4-pro` | **88.9** | `nvidia/z-ai/glm-4.7` | 87.7 | `nvidia/deepseek-ai/deepseek-v4-flash` | 83.2 |

## Summary: Best Value Model per Agent (Cost/Performance)

| Agent | Best Value Model | Cost/Perf | Perf Score | Cost |
|---|---|---|---|---|
| sisyphus | `mistralai/mistral-nemo` | **7,550,000** | 75.5 | $0.01/$0.03 |
| hephaestus | `mistralai/mistral-nemo` | **7,520,000** | 75.2 | $0.01/$0.03 |
| oracle | `mistralai/mistral-nemo` | **7,560,000** | 75.6 | $0.01/$0.03 |
| explore | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | **1,569,000** | 78.5 | $0.05/$0.20 |
| prometheus | `mistralai/mistral-nemo` | **7,550,000** | 75.5 | $0.01/$0.03 |
| metis | `mistralai/mistral-nemo` | **7,560,000** | 75.6 | $0.01/$0.03 |
| momus | `mistralai/mistral-nemo` | **7,560,000** | 75.6 | $0.01/$0.03 |
| librarian | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | **1,569,000** | 78.5 | $0.05/$0.20 |
| multimodal-looker | `mistralai/mistral-nemo` | **8,200,000** | 82.0 | $0.01/$0.03 |
| atlas | `mistralai/mistral-nemo` | **7,550,000** | 75.5 | $0.01/$0.03 |
| sisyphus-junior | `mistralai/mistral-nemo` | **7,590,000** | 75.9 | $0.01/$0.03 |

## Summary: Best Value Model per Category (Cost/Performance)

| Category | Best Value Model | Cost/Perf | Perf Score | Cost |
|---|---|---|---|---|
| visual-engineering | `mistralai/mistral-nemo` | **8,200,000** | 82.0 | $0.01/$0.03 |
| ultrabrain | `mistralai/mistral-nemo` | **7,560,000** | 75.6 | $0.01/$0.03 |
| deep | `mistralai/mistral-nemo` | **7,560,000** | 75.6 | $0.01/$0.03 |
| artistry | `mistralai/mistral-nemo` | **7,560,000** | 75.6 | $0.01/$0.03 |
| quick | `mistralai/mistral-nemo` | **10,000,000** | 100 | $0.01/$0.03 |
| unspecified-low | `mistralai/mistral-nemo` | **10,000,000** | 100 | $0.01/$0.03 |
| unspecified-high | `mistralai/mistral-nemo` | **7,550,000** | 75.5 | $0.01/$0.03 |
| writing | `nvidia/qwen/qwen3.5-9b` | **1,527,800** | 76.4 | $0.05/$0.15 |

---

## Key Insights

1. **April 25 refresh shifts speed-heavy leadership toward NVIDIA Build** — `deepseek-v4-flash` and `step-3.5-flash` now lead refreshed explore/librarian rankings.
2. **GLM-5.1 leads performance** across reasoning-heavy agents, consistent with v3.0 rankings
3. **GPT-5.4-pro** is the strongest paid model for deep reasoning but at 12× the cost of GPT-5.4
4. **GPT-5.4-nano stays relevant** as the strongest OpenAI model for refreshed speed-heavy and writing value rankings.
5. **Open-source models** (Llama, Gemma, Qwen) provide strong value in the mid-tier performance range
6. **Writing is now led by free large NVIDIA models** — `deepseek-v4-pro`, `glm-4.7`, and `deepseek-v4-flash` all outrank paid OpenAI frontier models on the refreshed formula.

---

## Related Documents

- [Oh-My-OpenCode Agent Rankings v3.0](./oh-my-opencode-agent-rankings.md) — NVIDIA Build + OpenCode Zen + OpenAI
- [Oh-My-OpenCode Agent Rankings — OpenAI Only](./oh-my-opencode-agent-rankings-openai-only.md) — OpenAI provider deep dive
- [Oh-My-OpenCode Config](../oh-my-opencode.json) — Current agent configuration

---

**Last Updated:** April 25, 2026
