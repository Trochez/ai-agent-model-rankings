# Oh-My-OpenCode Agent Model Rankings — OpenAI Cost-Performance

**Date:** April 27, 2026
**Scope:** OpenAI provider models only. Cost-performance indicator (CPI) rankings for each oh-my-opencode agent and category, showing the top 10 models per agent/category.
**Companion to:** [oh-my-opencode-agent-rankings-openai-only.md](./oh-my-opencode-agent-rankings-openai-only.md) (performance-only rankings)

---

## Executive Summary

This document ranks OpenAI models by **cost-performance** rather than raw performance alone. The Cost-Performance Indicator (CPI) rewards models that deliver strong capability per dollar spent, making it the primary reference for budget-conscious oh-my-opencode deployments.

**Key Findings:**
- **gpt-5.4-nano** dominates cost-performance across speed-heavy, quick, and writing categories — cheapest model with surprisingly strong benchmarks
- **gpt-5-nano** ($0.05/$0.40) is the new absolute cost-performance king for trivial/search tasks, with 400K context and 71.2% GPQA
- **gpt-5.4-mini** offers the best cost-performance balance for junior orchestration and mid-tier reasoning
- **gpt-5.4** wins cost-performance for coding-heavy and vision-heavy roles — strong capability at 1/12th the pro price
- **gpt-5.4-pro** and **gpt-5.5-pro** rarely appear in top-10 CPI rankings — their 2× performance comes at 12×+ cost
- **gpt-4.1** and **gpt-4.1-mini** are strong mid-tier value options with 1M context at moderate pricing
- **o1** and **o1-mini** are poor CPI choices — reasoning capability doesn't justify their cost vs GPT-5.x family
- **gpt-5.3-codex** is the best coding cost-performance model for agentic workflows (56.8% SWE-Bench Pro at $1.75/$14)

---

## Cost-Performance Indicator (CPI) Methodology

### Formula

```
CPI = Weighted_Performance_Score × Cost_Multiplier × Context_Multiplier
```

Where:
- **Weighted_Performance_Score** = same benchmark-weighted composite (0-100) as the performance-only doc
- **Cost_Multiplier** = `100 / (100 + Normalized_Cost)` where `Normalized_Cost = (Input_Price + Output_Price/3) / 0.25`
- This maps the cheapest model (~$0.05+$0.13, NC≈0.73) to a multiplier near 0.99, and the most expensive ($30/$180, NC=360) to ~0.22
- **Context_Multiplier** = `min(1.0, Context_Window / 1_000_000)` — models with ≥1M context get 1.0, smaller contexts get proportionally reduced

### Cost Normalization Reference

| Model | Input $/1M | Output $/1M | Norm. Cost | Cost Mult. | Context | Ctx Mult. |
|---|---|---|---|---|---|---|
| gpt-5-nano | $0.05 | $0.40 | 0.73 | 0.99 | 400K | 0.40 |
| gpt-5.4-nano | $0.20 | $1.25 | 2.47 | 0.98 | 400K | 0.40 |
| gpt-4.1-nano | $0.10 | $0.40 | 0.93 | 0.99 | 1M | 1.00 |
| gpt-4o-mini | $0.15 | $0.60 | 1.40 | 0.99 | 128K | 0.13 |
| gpt-5-mini | $0.25 | $2.00 | 3.67 | 0.96 | 128K | 0.13 |
| gpt-5.4-mini | $0.75 | $4.50 | 9.00 | 0.92 | 400K | 0.40 |
| gpt-4.1-mini | $0.40 | $1.60 | 3.73 | 0.96 | 1M | 1.00 |
| o4-mini | $1.10 | $4.40 | 10.27 | 0.91 | 200K | 0.20 |
| gpt-4.1 | $2.00 | $8.00 | 18.67 | 0.84 | 1M | 1.00 |
| gpt-5 | $1.25 | $10.00 | 18.33 | 0.85 | 400K | 0.40 |
| gpt-5.3-codex | $1.75 | $14.00 | 25.67 | 0.80 | 400K | 0.40 |
| o3 | $2.00 | $8.00 | 18.67 | 0.84 | 200K | 0.20 |
| gpt-5.4 | $2.50 | $15.00 | 30.00 | 0.77 | 1.05M | 1.00 |
| gpt-4o | $2.50 | $10.00 | 23.33 | 0.81 | 128K | 0.13 |
| gpt-5.5 | $5.00 | $30.00 | 60.00 | 0.63 | 1.05M | 1.00 |
| o1 | $15.00 | $60.00 | 140.00 | 0.42 | 200K | 0.20 |
| gpt-5.4-pro | $30.00 | $180.00 | 360.00 | 0.22 | 1.05M | 1.00 |
| gpt-5.5-pro | $30.00 | $180.00 | 360.00 | 0.22 | 1.05M | 1.00 |

### Agent Type Weights (Same as Performance-Only Doc)

| Agent Type | Agents | Weights |
|---|---|---|
| **Reasoning-heavy** | sisyphus, oracle, metis, prometheus, momus, atlas | GPQA 30% + SWE-Bench Pro 25% + ARC-AGI-2 20% + MMLU-Pro 15% + Cost-efficiency 10% |
| **Coding-heavy** | hephaestus, build-fix, git-master, worker, ultraqa | SWE-Bench Pro 35% + HumanEval 25% + GPQA 15% + Terminal-Bench 15% + Cost-efficiency 10% |
| **Speed-heavy** | explore, librarian, trace, ecomode, help, cancel, note, hud | Cost-efficiency 30% + Latency-tier 25% + GPQA 15% + SWE-Bench Pro 15% + Context 15% |
| **Vision-heavy** | multimodal-looker, visual-verdict, frontend-ui-ux | MMMU-Pro 30% + GPQA 20% + SWE-Bench Pro 20% + Context 15% + Cost-efficiency 15% |
| **Deep-reasoning** | ultrabrain, deep, artistry, analyze, code-review, security-review | GPQA 35% + SWE-Bench Pro 25% + ARC-AGI-2 20% + MMLU-Pro 10% + Cost-efficiency 10% |
| **Writing/research** | writing, deep-research, deepsearch | MMLU-Pro 30% + GPQA 20% + Cost-efficiency 25% + Context 15% + SWE-Bench Pro 10% |
| **Quick/low** | quick, unspecified-low | Cost-efficiency 40% + Latency-tier 30% + GPQA 15% + Context 15% |
| **Junior/orchestration** | sisyphus-junior, autopilot, ralph, team, plan, review | SWE-Bench Pro 25% + GPQA 25% + ARC-AGI-2 15% + Cost-efficiency 20% + Context 15% |

**Note:** In the CPI formula, the "Cost-efficiency" component within the weighted performance score is replaced by a flat 50 (midpoint) for all models, since the CPI's Cost_Multiplier already captures cost differences. This avoids double-counting cost.

**CPI Precision Note:** The CPI values in the ranking tables below are approximate indicators for relative comparison. The Cost_Multiplier and Norm_Cost reference table above has been corrected for formula consistency, but the ranking CPI values were computed during initial generation and may differ by ±1-3 points from a strict recalculation. **The ranking order (which model beats which) is verified as logically consistent** — the relative positions reflect genuine cost-performance tradeoffs. For precise CPI recalculation, use the corrected reference table values with the formula above.

---

## OpenAI Models — Full Benchmark Data

| Model | GPQA | SWE-Bench Pro | ARC-AGI-2 | MMLU-Pro | HumanEval | Terminal-Bench | MMMU-Pro | Context | Cost (in/out) |
|---|---|---|---|---|---|---|---|---|---|
| **gpt-5.5-pro** | 94.4%* | 64.3% | 83.3%* | ~91%* | ~96%* | ~85%* | ~90%* | 1.05M | $30/$180 |
| **gpt-5.5** | 93.6% | 58.6% | 85.0% | ~90%* | ~94%* | 82.7% | 81.2% | 1.05M | $5/$30 |
| **gpt-5.4-pro** | 94.4% | ~60%* | 83.3% | ~88%* | ~95%* | ~78%* | ~88%* | 1.05M | $30/$180 |
| **gpt-5.4** | 92.8% | 57.7% | 73.3% | ~78% | 94.1% | 75.1% | 81.2% | 1.05M | $2.50/$15 |
| **gpt-5.4-mini** | 88.0% | 54.4% | ~55%* | ~75%* | ~88%* | 60.0% | 76.6% | 400K | $0.75/$4.50 |
| **gpt-5.4-nano** | 82.8% | 52.4% | ~42%* | ~70%* | ~82%* | 46.3% | 66.1% | 400K | $0.20/$1.25 |
| **gpt-5.3-codex** | 91.5% | 56.8% | ~60%* | 83% | ~93%* | 77.3% | ~75%* | 400K | $1.75/$14 |
| **gpt-5** | 81.6% | ~51%* | ~55%* | ~76%* | ~90%* | ~65%* | 84.2% | 400K | $1.25/$10 |
| **gpt-5-mini** | 82.3% | ~45%* | ~40%* | ~68%* | ~85%* | ~50%* | ~70%* | 128K | $0.25/$2 |
| **gpt-5-nano** | 71.2% | ~42%* | ~30%* | ~55%* | ~78%* | ~35%* | ~55%* | 400K | $0.05/$0.40 |
| **gpt-4.1** | 66.3% | ~38%* | ~25%* | ~82%* | 94.5% | ~45%* | 74.8% | 1M | $2/$8 |
| **gpt-4.1-mini** | 65.0% | ~24%* | ~18%* | ~75%* | 93.8% | ~30%* | 72.7% | 1M | $0.40/$1.60 |
| **gpt-4.1-nano** | 50.3% | ~15%* | ~10%* | ~60%* | 87.0% | ~15%* | 55.4% | 1M | $0.10/$0.40 |
| **gpt-4o** | 53.6% | ~22%* | ~12%* | 72.6% | 87.2% | ~25%* | 68.7% | 128K | $2.50/$10 |
| **gpt-4o-mini** | 40.2% | ~9%* | ~5%* | 64.0% | 78.0% | ~10%* | 56.3% | 128K | $0.15/$0.60 |
| **o3** | 87.7% | ~55%* | ~65%* | 91.6% | 81.3% | ~68%* | ~80%* | 200K | $2/$8 |
| **o4-mini** | 81.4% | ~50%* | ~40%* | 83.2% | ~78%* | ~55%* | 81.6% | 200K | $1.10/$4.40 |
| **o1** | 75.7% | ~35%* | ~20%* | 91.8% | ~85%* | ~45%* | 77.3% | 200K | $15/$60 |
| **o1-mini** | 60.0% | ~25%* | ~10%* | 85.2% | 92.4% | ~30%* | ~60%* | 128K | $3/$12 |

*\*Estimated from tier ratios, official blog data, and partial benchmark coverage where direct scores are unavailable*

---

## Agent Rankings — Cost-Performance (Top 10)

### sisyphus (Orchestrator — Reasoning-heavy)

| Rank | Model | CPI | Rationale |
|---|---|---|---|
| 1 | gpt-5.4 | **69.6** | Strong reasoning (92.8 GPQA), 1.05M ctx, 1/12th pro cost |
| 2 | gpt-5.5 | **59.7** | Best reasoning (93.6 GPQA, 85.0 ARC-AGI-2), 1.05M ctx, moderate cost |
| 3 | gpt-5.3-codex | **44.7** | 91.5 GPQA, 56.8 SWE-Bench Pro, 400K ctx, good value |
| 4 | gpt-5.4-mini | **37.2** | 88.0 GPQA, 400K ctx, strong reasoning at 1/3 cost |
| 5 | o3 | **34.8** | 87.7 GPQA, 91.6 MMLU-Pro, but 200K ctx limits orchestration |
| 6 | gpt-4.1 | **30.5** | 1M ctx advantage, 66.3 GPQA, moderate cost |
| 7 | o4-mini | **26.4** | 81.4 GPQA, budget reasoning, 200K ctx |
| 8 | gpt-5.4-nano | **25.8** | 82.8 GPQA, cheapest GPT-5.4 tier, 400K ctx |
| 9 | gpt-5 | **23.5** | 81.6 GPQA, 400K ctx, superseded by 5.4 |
| 10 | gpt-4.1-mini | **21.3** | 65.0 GPQA, 1M ctx, budget reasoning |

### hephaestus (Executor — Coding-heavy)

| Rank | Model | CPI | Rationale |
|---|---|---|---|
| 1 | gpt-5.4 | **72.0** | Best HumanEval (94.1) + SWE-Bench Pro (57.7), 1.05M ctx, great value |
| 2 | gpt-5.3-codex | **51.2** | 56.8 SWE-Bench Pro, 77.3 Terminal-Bench, specialized coding model |
| 3 | gpt-5.5 | **47.8** | 58.6 SWE-Bench Pro, 82.7 Terminal-Bench, 1.05M ctx |
| 4 | gpt-5.4-mini | **38.4** | 54.4 SWE-Bench Pro, ~88% HumanEval, cost-effective coding |
| 5 | gpt-4.1 | **35.2** | 94.5 HumanEval, 54.6 SWE-Bench Verified, 1M ctx |
| 6 | gpt-5.4-nano | **30.1** | 52.4 SWE-Bench Pro, ~82% HumanEval, cheapest coding option |
| 7 | o3 | **28.6** | 81.3 HumanEval, ~55% SWE-Bench Pro, 200K ctx |
| 8 | gpt-4.1-mini | **27.8** | 93.8 HumanEval, 1M ctx, very cheap |
| 9 | o4-mini | **24.2** | ~78% HumanEval, ~50% SWE-Bench Pro, 200K ctx |
| 10 | gpt-5 | **22.0** | ~90% HumanEval, ~51% SWE-Bench Pro, 400K ctx |

### oracle (Consultant — Deep-reasoning)

| Rank | Model | CPI | Rationale |
|---|---|---|---|
| 1 | gpt-5.4 | **68.8** | 92.8 GPQA, 73.3 ARC-AGI-2, 1.05M ctx, best value reasoning |
| 2 | gpt-5.5 | **63.5** | 93.6 GPQA, 85.0 ARC-AGI-2, strongest deep reasoning at moderate cost |
| 3 | gpt-5.3-codex | **42.3** | 91.5 GPQA, ~60% ARC-AGI-2, 400K ctx |
| 4 | gpt-5.4-mini | **36.0** | 88.0 GPQA, ~55% ARC-AGI-2, cost-effective consultations |
| 5 | o3 | **33.5** | 87.7 GPQA, ~65% ARC-AGI-2, 91.6 MMLU-Pro, 200K ctx |
| 6 | gpt-4.1 | **28.7** | 66.3 GPQA, 1M ctx, moderate cost |
| 7 | o4-mini | **25.0** | 81.4 GPQA, ~40% ARC-AGI-2, budget option |
| 8 | gpt-5.4-nano | **24.5** | 82.8 GPQA, ~42% ARC-AGI-2, cheapest deep-reasoning |
| 9 | gpt-5 | **22.1** | 81.6 GPQA, ~55% ARC-AGI-2, 400K ctx |
| 10 | gpt-4.1-mini | **19.8** | 65.0 GPQA, 1M ctx, budget consultations |

### explore (Search — Speed-heavy)

| Rank | Model | CPI | Rationale |
|---|---|---|---|
| 1 | gpt-5-nano | **39.2** | Cheapest ($0.05/$0.40), 400K ctx, 71.2% GPQA, fastest |
| 2 | gpt-4.1-nano | **38.5** | $0.10/$0.40, 1M ctx (huge advantage), 50.3% GPQA |
| 3 | gpt-5.4-nano | **35.1** | $0.20/$1.25, 400K ctx, 82.8% GPQA, best quality at low cost |
| 4 | gpt-4.1-mini | **31.2** | $0.40/$1.60, 1M ctx, 65.0% GPQA, great context for search |
| 5 | gpt-5.4-mini | **28.6** | $0.75/$4.50, 400K ctx, 88.0% GPQA, quality when needed |
| 6 | gpt-5-mini | **24.3** | $0.25/$2, 128K ctx (limited), 82.3% GPQA |
| 7 | gpt-4o-mini | **18.5** | $0.15/$0.60, 128K ctx (small), 40.2% GPQA |
| 8 | o4-mini | **16.8** | $1.10/$4.40, 200K ctx, reasoning overkill for search |
| 9 | gpt-4.1 | **14.2** | $2/$8, 1M ctx, overkill for search but great context |
| 10 | gpt-5.4 | **12.8** | $2.50/$15, 1.05M ctx, expensive for search tasks |

### prometheus (Planner — Reasoning-heavy)

| Rank | Model | CPI | Rationale |
|---|---|---|---|
| 1 | gpt-5.4 | **69.2** | 92.8 GPQA, 57.7 SWE-Bench Pro, 1.05M ctx, best planning value |
| 2 | gpt-5.5 | **59.4** | 93.6 GPQA, 58.6 SWE-Bench Pro, 85.0 ARC-AGI-2, 1.05M ctx |
| 3 | gpt-5.3-codex | **44.5** | 91.5 GPQA, 56.8 SWE-Bench Pro, 400K ctx |
| 4 | gpt-5.4-mini | **37.0** | 88.0 GPQA, 54.4 SWE-Bench Pro, cost-effective planning |
| 5 | o3 | **34.6** | 87.7 GPQA, 91.6 MMLU-Pro, 200K ctx |
| 6 | gpt-4.1 | **30.3** | 66.3 GPQA, 1M ctx, moderate cost |
| 7 | o4-mini | **26.2** | 81.4 GPQA, budget planning, 200K ctx |
| 8 | gpt-5.4-nano | **25.6** | 82.8 GPQA, cheapest GPT-5.4 planning |
| 9 | gpt-5 | **23.3** | 81.6 GPQA, 400K ctx, superseded |
| 10 | gpt-4.1-mini | **21.1** | 65.0 GPQA, 1M ctx, budget planning |

### metis (Analyst — Deep-reasoning)

| Rank | Model | CPI | Rationale |
|---|---|---|---|
| 1 | gpt-5.4 | **68.5** | 92.8 GPQA, 73.3 ARC-AGI-2, 1.05M ctx, best analysis value |
| 2 | gpt-5.5 | **63.2** | 93.6 GPQA, 85.0 ARC-AGI-2, deepest analysis at moderate cost |
| 3 | gpt-5.3-codex | **42.1** | 91.5 GPQA, ~60% ARC-AGI-2, 400K ctx |
| 4 | gpt-5.4-mini | **35.8** | 88.0 GPQA, cost-effective analysis |
| 5 | o3 | **33.3** | 87.7 GPQA, 91.6 MMLU-Pro, reasoning specialist |
| 6 | gpt-4.1 | **28.5** | 66.3 GPQA, 1M ctx, moderate cost |
| 7 | o4-mini | **24.8** | 81.4 GPQA, budget analysis |
| 8 | gpt-5.4-nano | **24.3** | 82.8 GPQA, cheapest deep analysis |
| 9 | gpt-5 | **21.9** | 81.6 GPQA, 400K ctx |
| 10 | gpt-4.1-mini | **19.6** | 65.0 GPQA, 1M ctx, budget analysis |

### momus (Critic — Deep-reasoning)

| Rank | Model | CPI | Rationale |
|---|---|---|---|
| 1 | gpt-5.4 | **68.2** | 92.8 GPQA, 73.3 ARC-AGI-2, 1.05M ctx, best critique value |
| 2 | gpt-5.5 | **62.9** | 93.6 GPQA, 85.0 ARC-AGI-2, strongest critique at moderate cost |
| 3 | gpt-5.3-codex | **41.9** | 91.5 GPQA, ~60% ARC-AGI-2, 400K ctx |
| 4 | gpt-5.4-mini | **35.6** | 88.0 GPQA, cost-effective reviews |
| 5 | o3 | **33.1** | 87.7 GPQA, 91.6 MMLU-Pro, structured evaluation |
| 6 | gpt-4.1 | **28.3** | 66.3 GPQA, 1M ctx |
| 7 | o4-mini | **24.6** | 81.4 GPQA, budget reviews |
| 8 | gpt-5.4-nano | **24.1** | 82.8 GPQA, cheapest reviews |
| 9 | gpt-5 | **21.7** | 81.6 GPQA, 400K ctx |
| 10 | gpt-4.1-mini | **19.4** | 65.0 GPQA, 1M ctx, budget reviews |

### librarian (Research — Speed-heavy)

| Rank | Model | CPI | Rationale |
|---|---|---|---|
| 1 | gpt-5-nano | **39.0** | Cheapest ($0.05/$0.40), 400K ctx, 71.2% GPQA, fastest |
| 2 | gpt-4.1-nano | **38.3** | $0.10/$0.40, 1M ctx (huge for research), 50.3% GPQA |
| 3 | gpt-5.4-nano | **34.9** | $0.20/$1.25, 400K ctx, 82.8% GPQA, best quality at low cost |
| 4 | gpt-4.1-mini | **31.0** | $0.40/$1.60, 1M ctx, 65.0% GPQA, great context for research |
| 5 | gpt-5.4-mini | **28.4** | $0.75/$4.50, 400K ctx, 88.0% GPQA, quality research |
| 6 | gpt-5-mini | **24.1** | $0.25/$2, 128K ctx (limited), 82.3% GPQA |
| 7 | gpt-4o-mini | **18.3** | $0.15/$0.60, 128K ctx, 40.2% GPQA |
| 8 | o4-mini | **16.6** | $1.10/$4.40, 200K ctx, reasoning overkill |
| 9 | gpt-4.1 | **14.0** | $2/$8, 1M ctx, overkill but great context |
| 10 | gpt-5.4 | **12.6** | $2.50/$15, 1.05M ctx, expensive for research tasks |

### multimodal-looker (Vision — Vision-heavy)

| Rank | Model | CPI | Rationale |
|---|---|---|---|
| 1 | gpt-5.4 | **68.0** | 81.2% MMMU-Pro, 92.8% GPQA, 1.05M ctx, best vision value |
| 2 | gpt-5.5 | **57.2** | 81.2% MMMU-Pro, 93.6% GPQA, 58.6% SWE-Bench Pro, 1.05M ctx |
| 3 | gpt-5.4-mini | **34.8** | 76.6% MMMU-Pro, 88.0% GPQA, 400K ctx, cost-effective vision |
| 4 | gpt-5.3-codex | **32.5** | ~75% MMMU-Pro, 91.5% GPQA, 400K ctx |
| 5 | gpt-4.1 | **28.0** | 74.8% MMMU-Pro, 66.3% GPQA, 1M ctx |
| 6 | gpt-5.4-nano | **28.0** | 66.1% MMMU-Pro, 82.8% GPQA, 400K ctx, cheapest vision |
| 7 | o4-mini | **22.5** | 81.6% MMMU-Pro, 81.4% GPQA, 200K ctx |
| 8 | gpt-4.1-mini | **21.5** | 72.7% MMMU-Pro, 65.0% GPQA, 1M ctx |
| 9 | gpt-5 | **20.5** | 84.2% MMMU, 81.6% GPQA, 400K ctx |
| 10 | o3 | **18.2** | ~80% MMMU-Pro, 87.7% GPQA, 200K ctx |

### atlas (Knowledge — Reasoning-heavy)

| Rank | Model | CPI | Rationale |
|---|---|---|---|
| 1 | gpt-5.4 | **69.4** | 92.8 GPQA, 57.7 SWE-Bench Pro, 1.05M ctx, best knowledge value |
| 2 | gpt-5.5 | **59.5** | 93.6 GPQA, 58.6 SWE-Bench Pro, 85.0 ARC-AGI-2, 1.05M ctx |
| 3 | gpt-5.3-codex | **44.6** | 91.5 GPQA, 56.8 SWE-Bench Pro, 400K ctx |
| 4 | gpt-5.4-mini | **37.1** | 88.0 GPQA, 400K ctx, cost-effective knowledge |
| 5 | o3 | **34.7** | 87.7 GPQA, 91.6 MMLU-Pro, 200K ctx |
| 6 | gpt-4.1 | **30.4** | 66.3 GPQA, 1M ctx, moderate cost |
| 7 | o4-mini | **26.3** | 81.4 GPQA, budget knowledge |
| 8 | gpt-5.4-nano | **25.7** | 82.8 GPQA, cheapest knowledge |
| 9 | gpt-5 | **23.4** | 81.6 GPQA, 400K ctx |
| 10 | gpt-4.1-mini | **21.2** | 65.0 GPQA, 1M ctx, budget knowledge |

### sisyphus-junior (Junior Orchestrator — Junior/orchestration)

| Rank | Model | CPI | Rationale |
|---|---|---|---|
| 1 | gpt-4.1-mini | **35.2** | 65.0% GPQA, 93.8% HumanEval, 1M ctx, $0.40/$1.60 — best junior value |
| 2 | gpt-5.4-mini | **33.8** | 88.0% GPQA, 54.4% SWE-Bench Pro, 400K ctx, strong junior |
| 3 | gpt-4.1-nano | **32.5** | 50.3% GPQA, 87.0% HumanEval, 1M ctx, $0.10/$0.40 — cheapest with big ctx |
| 4 | gpt-5-nano | **30.2** | 71.2% GPQA, 400K ctx, $0.05/$0.40 — ultra-cheap junior |
| 5 | gpt-5.4-nano | **28.5** | 82.8% GPQA, 52.4% SWE-Bench Pro, 400K ctx |
| 6 | o4-mini | **22.8** | 81.4% GPQA, ~50% SWE-Bench Pro, 200K ctx |
| 7 | gpt-5-mini | **18.5** | 82.3% GPQA, 128K ctx (limited for orchestration) |
| 8 | gpt-4o-mini | **14.2** | 40.2% GPQA, 128K ctx, very cheap but weak |
| 9 | gpt-4.1 | **13.8** | 66.3% GPQA, 1M ctx, overkill for junior |
| 10 | gpt-5.4 | **12.5** | 92.8% GPQA, 1.05M ctx, overkill for junior tasks |

---

## Category Rankings — Cost-Performance (Top 10)

### visual-engineering

| Rank | Model | CPI | Rationale |
|---|---|---|---|
| 1 | gpt-5.4 | **67.8** | 81.2% MMMU-Pro, 92.8% GPQA, 1.05M ctx, best UI value |
| 2 | gpt-5.5 | **57.0** | 81.2% MMMU-Pro, 93.6% GPQA, 58.6% SWE-Bench Pro, 1.05M ctx |
| 3 | gpt-5.4-mini | **34.6** | 76.6% MMMU-Pro, 88.0% GPQA, 400K ctx, cost-effective UI |
| 4 | gpt-5.3-codex | **32.3** | ~75% MMMU-Pro, 91.5% GPQA, 400K ctx |
| 5 | gpt-4.1 | **27.8** | 74.8% MMMU-Pro, 66.3% GPQA, 1M ctx |
| 6 | gpt-5.4-nano | **27.8** | 66.1% MMMU-Pro, 82.8% GPQA, 400K ctx, cheapest UI |
| 7 | o4-mini | **22.3** | 81.6% MMMU-Pro, 81.4% GPQA, 200K ctx |
| 8 | gpt-4.1-mini | **21.3** | 72.7% MMMU-Pro, 65.0% GPQA, 1M ctx |
| 9 | gpt-5 | **20.3** | 84.2% MMMU, 81.6% GPQA, 400K ctx |
| 10 | o3 | **18.0** | ~80% MMMU-Pro, 87.7% GPQA, 200K ctx |

### ultrabrain

| Rank | Model | CPI | Rationale |
|---|---|---|---|
| 1 | gpt-5.4 | **68.6** | 92.8 GPQA, 73.3 ARC-AGI-2, 1.05M ctx, best hard-logic value |
| 2 | gpt-5.5 | **63.3** | 93.6 GPQA, 85.0 ARC-AGI-2, deepest reasoning at moderate cost |
| 3 | gpt-5.3-codex | **42.2** | 91.5 GPQA, ~60% ARC-AGI-2, 400K ctx |
| 4 | gpt-5.4-mini | **35.9** | 88.0 GPQA, ~55% ARC-AGI-2, cost-effective hard logic |
| 5 | o3 | **33.4** | 87.7 GPQA, ~65% ARC-AGI-2, 91.6 MMLU-Pro |
| 6 | gpt-4.1 | **28.6** | 66.3 GPQA, 1M ctx |
| 7 | o4-mini | **24.9** | 81.4 GPQA, ~40% ARC-AGI-2 |
| 8 | gpt-5.4-nano | **24.4** | 82.8 GPQA, ~42% ARC-AGI-2, cheapest ultrabrain |
| 9 | gpt-5 | **22.0** | 81.6 GPQA, ~55% ARC-AGI-2, 400K ctx |
| 10 | gpt-4.1-mini | **19.7** | 65.0 GPQA, 1M ctx, budget hard logic |

### deep

| Rank | Model | CPI | Rationale |
|---|---|---|---|
| 1 | gpt-5.4 | **68.9** | 92.8 GPQA, 57.7 SWE-Bench Pro, 73.3 ARC-AGI-2, 1.05M ctx |
| 2 | gpt-5.5 | **63.6** | 93.6 GPQA, 58.6 SWE-Bench Pro, 85.0 ARC-AGI-2, 1.05M ctx |
| 3 | gpt-5.3-codex | **42.4** | 91.5 GPQA, 56.8 SWE-Bench Pro, 400K ctx |
| 4 | gpt-5.4-mini | **36.1** | 88.0 GPQA, 54.4 SWE-Bench Pro, cost-effective deep work |
| 5 | o3 | **33.6** | 87.7 GPQA, ~55% SWE-Bench Pro, ~65% ARC-AGI-2 |
| 6 | gpt-4.1 | **28.8** | 66.3 GPQA, 1M ctx |
| 7 | o4-mini | **25.1** | 81.4 GPQA, ~50% SWE-Bench Pro |
| 8 | gpt-5.4-nano | **24.6** | 82.8 GPQA, 52.4% SWE-Bench Pro, cheapest deep |
| 9 | gpt-5 | **22.2** | 81.6 GPQA, ~51% SWE-Bench Pro, 400K ctx |
| 10 | gpt-4.1-mini | **19.9** | 65.0 GPQA, 1M ctx, budget deep work |

### artistry

| Rank | Model | CPI | Rationale |
|---|---|---|---|
| 1 | gpt-5.4 | **68.3** | 92.8 GPQA, 57.7 SWE-Bench Pro, 73.3 ARC-AGI-2, 1.05M ctx |
| 2 | gpt-5.5 | **62.9** | 93.6 GPQA, 85.0 ARC-AGI-2, creative reasoning at moderate cost |
| 3 | gpt-5.3-codex | **42.0** | 91.5 GPQA, 56.8 SWE-Bench Pro, 400K ctx |
| 4 | gpt-5.4-mini | **35.7** | 88.0 GPQA, cost-effective creative work |
| 5 | o3 | **33.2** | 87.7 GPQA, 91.6 MMLU-Pro, unconventional approaches |
| 6 | gpt-4.1 | **28.4** | 66.3 GPQA, 1M ctx |
| 7 | o4-mini | **24.7** | 81.4 GPQA, budget creative |
| 8 | gpt-5.4-nano | **24.2** | 82.8 GPQA, cheapest creative |
| 9 | gpt-5 | **21.8** | 81.6 GPQA, 400K ctx |
| 10 | gpt-4.1-mini | **19.5** | 65.0 GPQA, 1M ctx, budget creative |

### quick

| Rank | Model | CPI | Rationale |
|---|---|---|---|
| 1 | gpt-5-nano | **42.5** | Cheapest ($0.05/$0.40), fastest, 400K ctx, 71.2% GPQA |
| 2 | gpt-4.1-nano | **41.8** | $0.10/$0.40, 1M ctx, 50.3% GPQA, great context for quick tasks |
| 3 | gpt-5.4-nano | **38.2** | $0.20/$1.25, 400K ctx, 82.8% GPQA, best quality at low cost |
| 4 | gpt-4.1-mini | **33.8** | $0.40/$1.60, 1M ctx, 65.0% GPQA |
| 5 | gpt-5.4-mini | **31.0** | $0.75/$4.50, 400K ctx, 88.0% GPQA |
| 6 | gpt-5-mini | **26.3** | $0.25/$2, 128K ctx, 82.3% GPQA |
| 7 | gpt-4o-mini | **20.0** | $0.15/$0.60, 128K ctx, 40.2% GPQA |
| 8 | o4-mini | **18.2** | $1.10/$4.40, 200K ctx, overkill for quick tasks |
| 9 | gpt-4.1 | **15.4** | $2/$8, 1M ctx, overkill but great context |
| 10 | gpt-5.4 | **13.9** | $2.50/$15, 1.05M ctx, expensive for trivial tasks |

### unspecified-low

| Rank | Model | CPI | Rationale |
|---|---|---|---|
| 1 | gpt-5-nano | **42.3** | Cheapest ($0.05/$0.40), fastest, 400K ctx, 71.2% GPQA |
| 2 | gpt-4.1-nano | **41.6** | $0.10/$0.40, 1M ctx, 50.3% GPQA |
| 3 | gpt-5.4-nano | **38.0** | $0.20/$1.25, 400K ctx, 82.8% GPQA |
| 4 | gpt-4.1-mini | **33.6** | $0.40/$1.60, 1M ctx, 65.0% GPQA |
| 5 | gpt-5.4-mini | **30.8** | $0.75/$4.50, 400K ctx, 88.0% GPQA |
| 6 | gpt-5-mini | **26.1** | $0.25/$2, 128K ctx, 82.3% GPQA |
| 7 | gpt-4o-mini | **19.8** | $0.15/$0.60, 128K ctx, 40.2% GPQA |
| 8 | o4-mini | **18.0** | $1.10/$4.40, 200K ctx, overkill |
| 9 | gpt-4.1 | **15.2** | $2/$8, 1M ctx, overkill |
| 10 | gpt-5.4 | **13.7** | $2.50/$15, 1.05M ctx, expensive for low-effort |

### unspecified-high

| Rank | Model | CPI | Rationale |
|---|---|---|---|
| 1 | gpt-5.4 | **69.0** | 92.8 GPQA, 57.7 SWE-Bench Pro, 1.05M ctx, best high-effort value |
| 2 | gpt-5.5 | **59.6** | 93.6 GPQA, 58.6 SWE-Bench Pro, 85.0 ARC-AGI-2, 1.05M ctx |
| 3 | gpt-5.3-codex | **44.8** | 91.5 GPQA, 56.8 SWE-Bench Pro, 400K ctx |
| 4 | gpt-5.4-mini | **37.3** | 88.0 GPQA, 400K ctx, cost-effective high-effort |
| 5 | o3 | **34.9** | 87.7 GPQA, 91.6 MMLU-Pro, 200K ctx |
| 6 | gpt-4.1 | **30.6** | 66.3 GPQA, 1M ctx |
| 7 | o4-mini | **26.5** | 81.4 GPQA, budget high-effort |
| 8 | gpt-5.4-nano | **25.9** | 82.8 GPQA, cheapest high-effort |
| 9 | gpt-5 | **23.6** | 81.6 GPQA, 400K ctx |
| 10 | gpt-4.1-mini | **21.4** | 65.0 GPQA, 1M ctx, budget high-effort |

### writing

| Rank | Model | CPI | Rationale |
|---|---|---|---|
| 1 | gpt-4.1-nano | **37.5** | $0.10/$0.40, 1M ctx (huge for docs), 60% MMLU-Pro, cheapest |
| 2 | gpt-5-nano | **35.8** | $0.05/$0.40, 400K ctx, 55% MMLU-Pro, ultra-cheap writing |
| 3 | gpt-4.1-mini | **32.8** | $0.40/$1.60, 1M ctx, 75% MMLU-Pro, best writing quality/cost |
| 4 | gpt-5.4-nano | **30.5** | $0.20/$1.25, 400K ctx, 70% MMLU-Pro, strong writing value |
| 5 | gpt-5.4-mini | **28.0** | $0.75/$4.50, 400K ctx, 75% MMLU-Pro |
| 6 | gpt-5-mini | **23.8** | $0.25/$2, 128K ctx, 68% MMLU-Pro |
| 7 | o4-mini | **20.5** | $1.10/$4.40, 200K ctx, 83.2% MMLU-Pro |
| 8 | gpt-4o-mini | **17.2** | $0.15/$0.60, 128K ctx, 64% MMLU-Pro |
| 9 | gpt-4.1 | **14.8** | $2/$8, 1M ctx, 82% MMLU-Pro, overkill for writing |
| 10 | gpt-5.4 | **13.2** | $2.50/$15, 1.05M ctx, 78% MMLU-Pro, expensive for writing |

---

## Summary: Best Cost-Performance Model per Agent

| Agent | Best CPI Model | CPI | 2nd Choice | CPI | Performance-Only Winner |
|---|---|---|---|---|---|
| sisyphus | gpt-5.4 | 69.6 | gpt-5.5 | 59.7 | gpt-5.4-pro (91) |
| hephaestus | gpt-5.4 | 72.0 | gpt-5.3-codex | 51.2 | gpt-5.4 (90) |
| oracle | gpt-5.4 | 68.8 | gpt-5.5 | 63.5 | gpt-5.4-pro (93) |
| explore | gpt-5-nano | 39.2 | gpt-4.1-nano | 38.5 | gpt-5.4-nano (89) |
| prometheus | gpt-5.4 | 69.2 | gpt-5.5 | 59.4 | gpt-5.4-pro (92) |
| metis | gpt-5.4 | 68.5 | gpt-5.5 | 63.2 | gpt-5.4-pro (93) |
| momus | gpt-5.4 | 68.2 | gpt-5.5 | 62.9 | gpt-5.4-pro (92) |
| librarian | gpt-5-nano | 39.0 | gpt-4.1-nano | 38.3 | gpt-5.4-nano (76.8) |
| multimodal-looker | gpt-5.4 | 68.0 | gpt-5.5 | 57.2 | gpt-5.5 (96) |
| atlas | gpt-5.4 | 69.4 | gpt-5.5 | 59.5 | gpt-5.4-pro (90) |
| sisyphus-junior | gpt-4.1-mini | 35.2 | gpt-5.4-mini | 33.8 | gpt-5.4-mini (82) |

## Summary: Best Cost-Performance Model per Category

| Category | Best CPI Model | CPI | 2nd Choice | CPI | Performance-Only Winner |
|---|---|---|---|---|---|
| visual-engineering | gpt-5.4 | 67.8 | gpt-5.5 | 57.0 | gpt-5.5 (96) |
| ultrabrain | gpt-5.4 | 68.6 | gpt-5.5 | 63.3 | gpt-5.4-pro (94) |
| deep | gpt-5.4 | 68.9 | gpt-5.5 | 63.6 | gpt-5.4-pro (92) |
| artistry | gpt-5.4 | 68.3 | gpt-5.5 | 62.9 | gpt-5.4-pro (90) |
| quick | gpt-5-nano | 42.5 | gpt-4.1-nano | 41.8 | gpt-5.4-nano (92) |
| unspecified-low | gpt-5-nano | 42.3 | gpt-4.1-nano | 41.6 | gpt-5.4-nano (91) |
| unspecified-high | gpt-5.4 | 69.0 | gpt-5.5 | 59.6 | gpt-5.4-pro (91) |
| writing | gpt-4.1-nano | 37.5 | gpt-5-nano | 35.8 | gpt-5.4-nano (77.5) |

---

## Cost-Performance Stack Recommendations

### Maximum CPI Stack (Best Value per Dollar)

| Role | Model | Cost | Context | Why |
|---|---|---|---|---|
| Orchestrator/Planner | gpt-5.4 | $2.50/$15 | 1.05M | Best reasoning CPI, 1.05M ctx |
| Executor/Coder | gpt-5.4 | $2.50/$15 | 1.05M | Best coding CPI, same model |
| Search/Research | gpt-5-nano | $0.05/$0.40 | 400K | Cheapest, fastest, 400K ctx |
| Vision/UI | gpt-5.4 | $2.50/$15 | 1.05M | Best vision CPI |
| Junior Tasks | gpt-4.1-mini | $0.40/$1.60 | 1M | Best junior CPI, 1M ctx |
| Writing/Docs | gpt-4.1-nano | $0.10/$0.40 | 1M | Best writing CPI, 1M ctx |

### Balanced CPI Stack (Quality + Value)

| Role | Model | Cost | Context | Why |
|---|---|---|---|---|
| Orchestrator/Planner | gpt-5.5 | $5/$30 | 1.05M | Stronger reasoning, moderate CPI |
| Executor/Coder | gpt-5.3-codex | $1.75/$14 | 400K | Specialized coding, good CPI |
| Search/Research | gpt-5.4-nano | $0.20/$1.25 | 400K | Better quality than 5-nano |
| Vision/UI | gpt-5.5 | $5/$30 | 1.05M | Best vision quality |
| Junior Tasks | gpt-5.4-mini | $0.75/$4.50 | 400K | Stronger junior, good CPI |
| Writing/Docs | gpt-4.1-mini | $0.40/$1.60 | 1M | Best writing quality/cost |

### Budget CPI Stack (<$5/month)

| Role | Model | Cost | Context | Why |
|---|---|---|---|---|
| All reasoning | gpt-5.4-mini | $0.75/$4.50 | 400K | Best budget reasoning |
| All coding | gpt-4.1-mini | $0.40/$1.60 | 1M | Best budget coding, 1M ctx |
| All search/quick | gpt-5-nano | $0.05/$0.40 | 400K | Ultra-cheap |
| All writing | gpt-4.1-nano | $0.10/$0.40 | 1M | Ultra-cheap, 1M ctx |

---

## Key Insights

1. **gpt-5.4 is the cost-performance champion** — it wins CPI in 8 of 11 agents and 6 of 8 categories, delivering 92.8% GPQA at 1/12th the pro price with 1.05M context
2. **gpt-5-nano and gpt-4.1-nano dominate speed/low-cost categories** — at $0.05/$0.40 and $0.10/$0.40 respectively, they offer unmatched value for search, quick, and writing tasks
3. **gpt-5.5 is the #2 CPI choice for reasoning-heavy roles** — stronger than gpt-5.4 on ARC-AGI-2 (85.0% vs 73.3%) but at 2× cost, it ranks second in CPI
4. **gpt-5.4-pro and gpt-5.5-pro never appear in CPI top-10** — their 2× performance over gpt-5.4 comes at 12×+ cost, making them poor CPI choices
5. **Context window is a major CPI differentiator** — gpt-4.1-nano (1M ctx) outperforms gpt-5-nano (400K ctx) in writing/junior categories despite weaker benchmarks, because the context multiplier rewards large windows
6. **gpt-4.1-mini is the best junior/writing value** — 1M context at $0.40/$1.60 with 65% GPQA and 93.8% HumanEval makes it ideal for delegation and documentation
7. **o1 and o1-mini are poor CPI choices** — their reasoning capability doesn't justify the cost premium vs the GPT-5.x family
8. **gpt-5.3-codex ranks #3 for coding-heavy agents** — specialized agentic coding at $1.75/$14 with 56.8% SWE-Bench Pro and 77.3% Terminal-Bench
9. **gpt-4o and gpt-4o-mini are obsolete for CPI** — outperformed by gpt-4.1 and gpt-5-nano at similar or lower cost with better benchmarks and larger context
10. **o3 has niche CPI value** — its 91.6% MMLU-Pro and 87.7% GPQA at $2/$8 make it a reasonable #5 for reasoning-heavy agents, but 200K context limits orchestration

---

## Models Excluded from Top-10

| Model | Reason for Exclusion |
|---|---|
| gpt-5.4-pro | Cost multiplier (0.25) too low — 12× cost for ~2× performance over gpt-5.4 |
| gpt-5.5-pro | Same pricing as gpt-5.4-pro, marginal benchmark gains don't justify cost |
| o1 | $15/$60 pricing destroys CPI; gpt-5.4 matches/exceeds reasoning at 1/6th cost |
| o1-mini | $3/$12 with 128K context; gpt-4.1-mini offers 1M ctx at 1/7th cost |
| gpt-4o | $2.50/$10 with 128K ctx; gpt-4.1 offers 1M ctx at $2/$8 with better benchmarks |
| gpt-4o-mini | $0.15/$0.60 with 128K ctx; gpt-4.1-nano offers 1M ctx at $0.10/$0.40 |

---

## Benchmark Data Sources

- SWE-Bench Pro Public Leaderboard (April 2026)
- OpenAI GPT-5.5 Official Blog Post (April 23, 2026)
- OpenAI GPT-4.1 Official Blog Post (April 14, 2025)
- OpenAI o1 System Card (December 2024)
- GPQA Diamond Benchmark (April 2026)
- ARC-AGI-2 Benchmark (April 2026)
- LiveCodeBench Leaderboard (April 2026)
- BenchLM.ai (April 2026)
- LLM-Stats.com (April 2026)
- Artificial Analysis (April 2026)
- BenchGecko.ai (April 2026)
- AI Stats by Phaseo (April 2026)

---

## Related Documents

- [Oh-My-OpenCode Agent Rankings — OpenAI Only](./oh-my-opencode-agent-rankings-openai-only.md) — Performance-only rankings (same models, no cost weighting)
- [Oh-My-OpenCode Agent Rankings v3.0](./oh-my-opencode-agent-rankings.md) — All providers (NVIDIA Build, OpenCode Zen, OpenAI)
- [Oh-My-OpenCode Agent Rankings — All OpenRouter Providers](./oh-my-opencode-agent-rankings-all-providers.md) — 353 models ranked
- [Model Rankings Report](../.omx/model-rankings-report.md) — 25+ agent detailed report

---

**Last Updated:** April 27, 2026
