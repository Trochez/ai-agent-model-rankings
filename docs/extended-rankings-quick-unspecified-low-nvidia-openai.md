# Extended Rankings — Quick + Unspecified-Low (NVIDIA Build + OpenAI)

**Date:** April 25, 2026
**Scope:** NVIDIA Build + OpenAI models only
**Categories:** `quick` and `unspecified-low`
**Formula:** Cost-eff 40% + Latency-tier 30% + GPQA 15% + Context 15%

---

## Methodology

### Quick/Low Weight Formula

| Component | Weight | Description |
|---|---|---|
| Cost-efficiency | 40% | Normalized pricing score (FREE=100, higher cost=lower) |
| Latency-tier | 30% | Normalized speed score based on active params (<3B=100, 3-8B=95, 8-15B=85, MoE 3-4B act=90, MoE 11B+ act=75, 24B dense=60) |
| GPQA Diamond | 15% | Graduate-level reasoning benchmark, normalized 0-100 |
| Context window | 15% | Normalized context (1M+=100, 256K=90, 131K=80, 128K=75, 33K=40, 32K=38, 8K=15) |

Each component is normalized to 0-100 before weighting. Final Score = component x weight sum.

### Cost/Performance Ratio

- **Paid models:** C/P = (Score x 1,000) / (Input $/1M tokens)
- **Free models:** C/P = Score x 100 (reflects infinite value at zero cost, capped for comparability)

---

## Quick — Performance Ranking (Top 10, NVIDIA Build + OpenAI)

| Rank | Model | Provider | Score | $/1M In | $/1M Out | Ctx | Free |
|---|---|---|---|---|---|---|---|
| 1 | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | NVIDIA Build | **93.5** | $0.05 | $0.20 | 1M | |
| 2 | `nvidia/qwen/qwen3.5-9b` | NVIDIA Build | **92.7** | $0.05 | $0.15 | 256K | |
| 3 | `openai/gpt-5.4-nano` | OpenAI | **92** | $0.20 | $1.25 | 400K | |
| 4 | `nvidia/stepfun-ai/step-3.5-flash` | NVIDIA Build | **91.0** | $0.00 | $0.00 | 256K | Yes |
| 5 | `nvidia/deepseek-ai/deepseek-v4-flash` | NVIDIA Build | **90.4** | $0.00 | $0.00 | 1M | Yes |
| 6 | `nvidia/nvidia/nvidia-nemotron-nano-9b-v2` | NVIDIA Build | **88.3** | $0.00 | $0.00 | 128K | Yes |
| 7 | `nvidia/microsoft/phi-4-multimodal-instruct` | NVIDIA Build | **88.1** | $0.00 | $0.00 | 128K | Yes |
| 8 | `nvidia/google/gemma-4-26b-a4b-it` | NVIDIA Build | **87.4** | $0.08 | $0.35 | 256K | |
| 9 | `nvidia/mistralai/mistral-nemo-minitron-8b-base` | NVIDIA Build | **87.0** | $0.00 | $0.00 | 128K | Yes |
| 10 | `openai/gpt-5.4-mini` | OpenAI | **80** | $0.75 | $4.50 | 400K | |

## Unspecified-Low — Performance Ranking (Top 10, NVIDIA Build + OpenAI)

| Rank | Model | Provider | Score | $/1M In | $/1M Out | Ctx | Free |
|---|---|---|---|---|---|---|---|
| 1 | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | NVIDIA Build | **93.5** | $0.05 | $0.20 | 1M | |
| 2 | `nvidia/qwen/qwen3.5-9b` | NVIDIA Build | **92.7** | $0.05 | $0.15 | 256K | |
| 3 | `openai/gpt-5.4-nano` | OpenAI | **91** | $0.20 | $1.25 | 400K | |
| 4 | `nvidia/stepfun-ai/step-3.5-flash` | NVIDIA Build | **91.0** | $0.00 | $0.00 | 256K | Yes |
| 5 | `nvidia/deepseek-ai/deepseek-v4-flash` | NVIDIA Build | **90.4** | $0.00 | $0.00 | 1M | Yes |
| 6 | `nvidia/nvidia/nvidia-nemotron-nano-9b-v2` | NVIDIA Build | **88.3** | $0.00 | $0.00 | 128K | Yes |
| 7 | `nvidia/microsoft/phi-4-multimodal-instruct` | NVIDIA Build | **88.1** | $0.00 | $0.00 | 128K | Yes |
| 8 | `nvidia/google/gemma-4-26b-a4b-it` | NVIDIA Build | **87.4** | $0.08 | $0.35 | 256K | |
| 9 | `nvidia/mistralai/mistral-nemo-minitron-8b-base` | NVIDIA Build | **87.0** | $0.00 | $0.00 | 128K | Yes |
| 10 | `openai/gpt-5.4-mini` | OpenAI | **79** | $0.75 | $4.50 | 400K | |

---

## Score Breakdown (Top 10, Quick Category)

| Model | Cost-eff (40%) | Latency (30%) | GPQA (15%) | Context (15%) | Total |
|---|---|---|---|---|---|
| nemotron-3-nano-30b-a3b | 95 -> 38.0 | 90 -> 27.0 | 90 -> 13.5 | 100 -> 15.0 | **93.5** |
| qwen3.5-9b | 90 -> 36.0 | 95 -> 28.5 | 98 -> 14.7 | 90 -> 13.5 | **92.7** |
| gpt-5.4-nano (OpenAI) | 88 -> 35.2 | 88 -> 26.4 | 92 -> 13.8 | 90 -> 13.5 | **~92** |
| step-3.5-flash | 100 -> 40.0 | 75 -> 22.5 | 100 -> 15.0 | 90 -> 13.5 | **91.0** |
| deepseek-v4-flash | 100 -> 40.0 | 70 -> 21.0 | 96 -> 14.4 | 100 -> 15.0 | **90.4** |
| nemotron-nano-9b-v2 | 100 -> 40.0 | 85 -> 25.5 | 77 -> 11.6 | 75 -> 11.3 | **88.3** |
| phi-4-multimodal | 100 -> 40.0 | 95 -> 28.5 | 55 -> 8.3 | 75 -> 11.3 | **88.1** |
| gemma-4-26b-a4b-it | 80 -> 32.0 | 90 -> 27.0 | 99 -> 14.9 | 90 -> 13.5 | **87.4** |
| mistral-nemo-minitron-8b | 100 -> 40.0 | 95 -> 28.5 | 48 -> 7.2 | 75 -> 11.3 | **87.0** |
| gpt-5.4-mini (OpenAI) | 70 -> 28.0 | 85 -> 25.5 | 85 -> 12.8 | 90 -> 13.5 | **~80** |

---

## Key Insights

1. **nemotron-3-nano-30b-a3b** (93.5) — best overall for quick/low tasks: $0.05/$0.20, 1M context, 3.6B active params, GPQA ~75%. The sweet spot.
2. **step-3.5-flash** and **deepseek-v4-flash** are FREE with 90+ scores — unbeatable cost/performance if SLAs are not required.
3. **qwen3.5-9b** (92.7) — remarkable 9B dense model with GPQA 81.7%, only $0.05/$0.15.
4. **gpt-5.4-nano** is the best OpenAI option (92 quick / 91 unspecified-low) — strong but 4x the input cost of nemotron-3-nano.
5. **gpt-5.4-mini** (80/79) drops significantly — too expensive at $0.75/$4.50 for quick/low tasks.
6. Both categories share identical rankings since they use the same weight formula and model pool. The only difference is OpenAI's 1-point scoring gap between quick and unspecified-low.
7. 7 of the top 10 are free on NVIDIA Build, making paid models hard to justify unless you need guaranteed SLAs.

---

*Generated April 25, 2026. Part of the oh-my-opencode agent rankings series.*
*See also: [v3.0 Canonical Rankings](oh-my-opencode-agent-rankings.md) | [All-Providers Rankings](oh-my-opencode-agent-rankings-all-providers.md) | [Quick NVIDIA Build Extended](extended-rankings-quick-nvidia-build.md) | [Librarian + Writing NVIDIA+OpenAI](extended-rankings-librarian-writing-nvidia-openai.md)*
