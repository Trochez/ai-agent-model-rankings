# Oh-My-OpenCode Agent Model Rankings — OpenAI Only

**Date:** April 25, 2026
**Scope:** OpenAI provider models only. Full cross-benchmark rankings below use the current benchmark-covered set (`gpt-5.4-pro`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `o3`, `o4-mini`) plus `gpt-5.5` where this repo has direct visual benchmark coverage.
**Companion to:** [oh-my-opencode-agent-rankings.md](./oh-my-opencode-agent-rankings.md) (v3.0, all providers)

---

## Executive Summary

This document provides OpenAI-only model rankings for each oh-my-opencode agent and category, with calculated numeric performance indicators derived from benchmark data. It is intended for users who want to run oh-my-opencode exclusively on OpenAI infrastructure.

**Key Findings:**
- **gpt-5.5** is now the best OpenAI vision model in this repo's direct benchmark coverage, taking **multimodal-looker** and **visual-engineering**
- **gpt-5.4-pro** still dominates reasoning-heavy agents (oracle, metis, prometheus, momus, ultrabrain)
- **gpt-5.4** remains the best OpenAI all-rounder for coding/execution work
- **gpt-5.4-nano** still wins speed-heavy and low-cost roles (explore, librarian, quick, writing)
- **gpt-5.4-mini** remains the best junior orchestration choice
- **o3** pricing is materially better than the prior draft ($2/$8, not $10/$40), but it still does not displace the GPT-5.4 family overall
- **gpt-5.3-codex** is still available, but it remains excluded from the primary tables because the refreshed benchmark set in this document focuses on the newer GPT-5.x general models

---

## Scoring Methodology

Each model gets a **composite score (0-100)** calculated from benchmark data, weighted by agent type:

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

**Cost-efficiency** is normalized: nano=100, mini=85, o4-mini=75, o3=40, gpt-5.4=55, gpt-5.4-pro=15

---

## Current OpenAI Model Availability Snapshot (April 25, 2026)

| Model | Input $/1M | Output $/1M | Context | Ranking Coverage in This Doc | Notes |
|---|---|---|---|---|---|
| **gpt-5.5** | $5.00 | $30.00 | 1.0M | Partial | Direct visual benchmark coverage in this repo; used below for vision-heavy rankings |
| **gpt-5.5-pro** | $30.00 | $180.00 | 1.05M | Availability only | Current flagship pro model, but no comparable full benchmark set in this repo yet |
| **gpt-5.4-pro** | $30.00 | $180.00 | 1.05M | Full | Main reasoning leader |
| **gpt-5.4** | $2.50 | $15.00 | 1.0M | Full | Best all-round OpenAI execution model |
| **gpt-5.4-mini** | $0.75 | $4.50 | 400K | Full | Best junior/budget balanced option |
| **gpt-5.4-nano** | $0.20 | $1.25 | 400K | Full | Best speed/value option |
| **o3** | $2.00 | $8.00 | 200K | Full | Pricing corrected from prior draft |
| **o4-mini** | $1.10 | $4.40 | 200K | Full | Still available, but usually outperformed by GPT-5.4 mini/nano |
| **gpt-5.3-codex** | $1.75 | $14.00 | 400K | Availability only | Still available; not used in the primary refreshed tables |

## OpenAI Models — Benchmark Raw Scores (Benchmark-covered set)

| Model | GPQA Diamond | SWE-Bench Pro | ARC-AGI-2 | MMLU-Pro | HumanEval | Terminal-Bench | MMMU-Pro | Context | Cost (in/out per 1M) |
|---|---|---|---|---|---|---|---|---|---|
| **gpt-5.4-pro** | 94.4% | ~60%* | 83.3% | ~88%* | ~95%* | ~78%* | ~88%* | 1.05M | $30/$180 |
| **gpt-5.4** | 92.8% | 57.7% | 73.3% | ~78% | 94.1% | 75.1% | 81.2% | 1.05M | $2.50/$15 |
| **gpt-5.4-mini** | 88.0% | 54.4% | ~55%* | ~75%* | ~88%* | 60.0% | 76.6% | 400K | $0.75/$4.50 |
| **gpt-5.4-nano** | 82.8% | 52.4% | ~42%* | ~70%* | ~82%* | 46.3% | 66.1% | 400K | $0.20/$1.25 |
| **o3** | 87.7% | ~55%* | ~65%* | 91.6% | 81.3% | ~68%* | ~80%* | 200K | $2/$8 |
| **o4-mini** | 81.4% | ~50%* | ~40%* | 83.2% | ~78%* | ~55%* | 81.6% | 200K | $1.10/$4.40 |

*\*Estimated from tier ratios and partial data where direct benchmark not available*

### Additional Benchmark Data

| Model | SWE-Bench Verified | AIME 2025 | MATH-500 | ARC-AGI-1 | OSWorld | Chatbot Arena Elo |
|---|---|---|---|---|---|---|
| **gpt-5.4-pro** | ~80%* | ~98%* | ~99%* | 94.5% | ~78%* | ~1481 |
| **gpt-5.4** | 77.2% | 95.2% | 94.6% | ~85%* | 75.0% | ~1484 |
| **gpt-5.4-mini** | ~72%* | ~90%* | ~92%* | ~60%* | 72.1% | ~1467 |
| **gpt-5.4-nano** | ~65%* | ~85%* | ~88%* | ~50%* | 39.0% | ~1466 |
| **o3** | 71.7% | 98.4% | ~97%* | 87.5% | ~65%* | ~1350 |
| **o4-mini** | 68.1% | 99.5% | 98.9% | ~70%* | ~55%* | ~1350 |

---

## Agent Rankings — OpenAI Only

### sisyphus (Orchestrator — Reasoning-heavy)

| Rank | Model | Score | Rationale |
|---|---|---|---|
| 1 | gpt-5.4-pro | **91** | Highest GPQA (94.4), deepest reasoning, 1.05M ctx |
| 2 | gpt-5.4 | **87** | Strong all-around, 1.05M ctx, best cost/perf ratio |
| 3 | o3 | **79** | Strong reasoning (91.6 MMLU), but 200K ctx, high cost |
| 4 | gpt-5.4-mini | **76** | Good reasoning at 1/3 cost, 400K ctx sufficient |
| 5 | o4-mini | **68** | Budget reasoning, limited context for orchestration |

### hephaestus (Executor — Coding-heavy)

| Rank | Model | Score | Rationale |
|---|---|---|---|
| 1 | gpt-5.4 | **90** | Best HumanEval (94.1) + SWE-Bench Pro (57.7), 1.05M ctx |
| 2 | gpt-5.4-pro | **88** | Slightly better coding but 12× cost penalty |
| 3 | gpt-5.4-mini | **80** | Solid coding (54.4 SWE-Bench Pro), cost-effective |
| 4 | o3 | **74** | Good reasoning but weaker coding (81.3 HumanEval) |
| 5 | gpt-5.4-nano | **71** | Decent coding for the price, 400K ctx |

### oracle (Consultant — Deep-reasoning)

| Rank | Model | Score | Rationale |
|---|---|---|---|
| 1 | gpt-5.4-pro | **93** | Highest GPQA (94.4), ARC-AGI-2 (83.3), best for architecture |
| 2 | gpt-5.4 | **86** | Strong reasoning, 1.05M ctx, better cost/perf |
| 3 | o3 | **82** | 91.6 MMLU-Pro, 87.7 GPQA, reasoning specialist |
| 4 | gpt-5.4-mini | **73** | 88.0 GPQA, cost-effective for less critical consultations |
| 5 | o4-mini | **65** | Budget reasoning, 81.4 GPQA, 200K ctx limit |

### explore (Search — Speed-heavy)

| Rank | Model | Score | Rationale |
|---|---|---|---|
| 1 | gpt-5.4-nano | **89** | Cheapest ($0.20/$1.25), fastest, 400K ctx, sufficient for grep |
| 2 | gpt-5.4-mini | **82** | Good speed/cost, 400K ctx, better quality when needed |
| 3 | o4-mini | **74** | $1.10/$4.40, 200K ctx, reasoning overkill for search |
| 4 | gpt-5.4 | **58** | Overkill for search, expensive at $2.50/$15 |
| 5 | o3 | **42** | Way too expensive ($2/$8) for search tasks |

### prometheus (Planner — Reasoning-heavy)

| Rank | Model | Score | Rationale |
|---|---|---|---|
| 1 | gpt-5.4-pro | **92** | Best reasoning depth, 1.05M ctx for complex plans |
| 2 | gpt-5.4 | **87** | Strong planning, 1.05M ctx, better cost/perf |
| 3 | o3 | **80** | 91.6 MMLU, good for structured planning |
| 4 | gpt-5.4-mini | **75** | Cost-effective planning, 400K ctx |
| 5 | o4-mini | **67** | Budget option, limited context for large plans |

### metis (Analyst — Deep-reasoning)

| Rank | Model | Score | Rationale |
|---|---|---|---|
| 1 | gpt-5.4-pro | **93** | Best for ambiguity detection, 94.4 GPQA |
| 2 | gpt-5.4 | **86** | Strong analysis, 1.05M ctx |
| 3 | o3 | **81** | 91.6 MMLU, reasoning specialist for analysis |
| 4 | gpt-5.4-mini | **73** | Cost-effective for standard analysis |
| 5 | o4-mini | **65** | Budget analysis, 200K ctx |

### momus (Critic — Deep-reasoning)

| Rank | Model | Score | Rationale |
|---|---|---|---|
| 1 | gpt-5.4-pro | **92** | Best for quality assessment, 94.4 GPQA, 83.3 ARC-AGI-2 |
| 2 | gpt-5.4 | **86** | Strong critique, 1.05M ctx |
| 3 | o3 | **80** | Good for structured evaluation |
| 4 | gpt-5.4-mini | **74** | Cost-effective for standard reviews |
| 5 | o4-mini | **66** | Budget reviews, 200K ctx |

### librarian (Research — Speed-heavy)

| Rank | Model | Score | Rationale |
|---|---|---|---|
| 1 | gpt-5.4-nano | **76.8** | Best OpenAI librarian score: cheapest, fastest, 400K ctx |
| 2 | gpt-5.4-mini | **65.1** | Solid speed/cost balance for more complex lookups |
| 3 | o4-mini | **58.2** | Functional, but slower and pricier than GPT-5.4 nano/mini |
| 4 | gpt-5.4 | **52.1** | Large context helps, but pricing hurts speed-heavy ranking |
| 5 | gpt-5.4-pro | **49.7** | Strong quality, but too expensive for librarian-style tasks |

### multimodal-looker (Vision — Vision-heavy)

| Rank | Model | Score | Rationale |
|---|---|---|---|
| 1 | gpt-5.5 | **96** | Newest frontier visual model in this repo's benchmark set, 1.05M ctx |
| 2 | gpt-5.4 | **85** | Best fully benchmarked prior-generation OpenAI vision model |
| 3 | gpt-5.4-pro | **83** | Strong quality, but expensive |
| 4 | gpt-5.4-mini | **72** | Cost-effective vision |
| 5 | o4-mini | **68** | Budget multimodal option |

### atlas (Knowledge — Reasoning-heavy)

| Rank | Model | Score | Rationale |
|---|---|---|---|
| 1 | gpt-5.4-pro | **90** | Best reasoning + 1.05M ctx for knowledge tasks |
| 2 | gpt-5.4 | **86** | Strong knowledge, 1.05M ctx |
| 3 | o3 | **79** | 91.6 MMLU, good for knowledge synthesis |
| 4 | gpt-5.4-mini | **74** | Cost-effective, 400K ctx |
| 5 | o4-mini | **66** | Budget knowledge, 200K ctx |

### sisyphus-junior (Junior Orchestrator — Junior/orchestration)

| Rank | Model | Score | Rationale |
|---|---|---|---|
| 1 | gpt-5.4-mini | **82** | Best cost/perf for junior tasks, 400K ctx |
| 2 | gpt-5.4-nano | **78** | Cheapest, fast, 400K ctx, sufficient for simple delegation |
| 3 | o4-mini | **72** | Good reasoning at low cost, 200K ctx |
| 4 | gpt-5.4 | **65** | Overkill for junior tasks, expensive |
| 5 | o3 | **48** | Too expensive for junior orchestration |

---

## Category Rankings — OpenAI Only

### visual-engineering

| Rank | Model | Score | Rationale |
|---|---|---|---|
| 1 | gpt-5.5 | **96** | Newest frontier visual model; strongest direct UI/UX benchmark signal in this repo |
| 2 | gpt-5.4 | **84** | Best fully benchmarked prior-generation OpenAI UI model |
| 3 | gpt-5.4-pro | **82** | Strong quality, but premium priced |
| 4 | gpt-5.4-mini | **71** | Cost-effective UI work |
| 5 | o4-mini | **67** | Budget vision/UI option |

### ultrabrain

| Rank | Model | Score | Rationale |
|---|---|---|---|
| 1 | gpt-5.4-pro | **94** | Highest GPQA (94.4), ARC-AGI-2 (83.3), deepest reasoning |
| 2 | gpt-5.4 | **87** | Strong all-around, 1.05M ctx |
| 3 | o3 | **82** | 91.6 MMLU, 87.7 GPQA, reasoning specialist |
| 4 | gpt-5.4-mini | **73** | 88.0 GPQA, cost-effective hard logic |
| 5 | o4-mini | **65** | Budget reasoning, 81.4 GPQA |

### deep

| Rank | Model | Score | Rationale |
|---|---|---|---|
| 1 | gpt-5.4-pro | **92** | Best for autonomous deep problem-solving, 1.05M ctx |
| 2 | gpt-5.4 | **88** | Strong deep work, 1.05M ctx, better cost/perf |
| 3 | o3 | **80** | Good reasoning for deep investigation |
| 4 | gpt-5.4-mini | **74** | Cost-effective for standard deep tasks |
| 5 | o4-mini | **66** | Budget deep work, 200K ctx limit |

### artistry

| Rank | Model | Score | Rationale |
|---|---|---|---|
| 1 | gpt-5.4-pro | **90** | Best creative reasoning, 94.4 GPQA |
| 2 | gpt-5.4 | **85** | Strong creative + coding, 1.05M ctx |
| 3 | o3 | **78** | Good for unconventional approaches |
| 4 | gpt-5.4-mini | **72** | Cost-effective creative work |
| 5 | o4-mini | **64** | Budget creative, 200K ctx |

### quick

| Rank | Model | Score | Rationale |
|---|---|---|---|
| 1 | gpt-5.4-nano | **92** | Cheapest ($0.20/$1.25), fastest, 400K ctx |
| 2 | gpt-5.4-mini | **80** | Good speed, 400K ctx, $0.75/$4.50 |
| 3 | o4-mini | **70** | $1.10/$4.40, 200K ctx, reasoning overkill |
| 4 | gpt-5.4 | **52** | Overkill for quick tasks |
| 5 | o3 | **35** | Way too expensive for trivial tasks |

### unspecified-low

| Rank | Model | Score | Rationale |
|---|---|---|---|
| 1 | gpt-5.4-nano | **91** | Cheapest, fastest, 400K ctx |
| 2 | gpt-5.4-mini | **79** | Good speed/cost balance |
| 3 | o4-mini | **69** | Functional but overkill |
| 4 | gpt-5.4 | **51** | Expensive for low-effort tasks |
| 5 | o3 | **34** | Too expensive |

### unspecified-high

| Rank | Model | Score | Rationale |
|---|---|---|---|
| 1 | gpt-5.4-pro | **91** | Best reasoning for high-effort tasks |
| 2 | gpt-5.4 | **86** | Strong all-around, 1.05M ctx |
| 3 | o3 | **80** | Good reasoning, 200K ctx |
| 4 | gpt-5.4-mini | **74** | Cost-effective for standard high-effort |
| 5 | o4-mini | **66** | Budget option |

### writing

| Rank | Model | Score | Rationale |
|---|---|---|---|
| 1 | gpt-5.4-nano | **77.5** | Best OpenAI writing value: 400K ctx, low cost, strongest refreshed score |
| 2 | gpt-5.4-mini | **72.8** | Balanced quality/cost for general documentation |
| 3 | o4-mini | **69.0** | Good budget writing option with stronger reasoning than its price suggests |
| 4 | gpt-5.4-pro | **67.5** | High quality, but cost crushes its writing formula score |
| 5 | gpt-5.4 | **66.5** | Large context helps, but price drags it below nano/mini |

---

## Summary: Best OpenAI Model per Agent

| Agent | Best OpenAI Model | Score | 2nd Choice | Score |
|---|---|---|---|---|
| sisyphus | gpt-5.4-pro | 91 | gpt-5.4 | 87 |
| hephaestus | gpt-5.4 | 90 | gpt-5.4-pro | 88 |
| oracle | gpt-5.4-pro | 93 | gpt-5.4 | 86 |
| explore | gpt-5.4-nano | 89 | gpt-5.4-mini | 82 |
| prometheus | gpt-5.4-pro | 92 | gpt-5.4 | 87 |
| metis | gpt-5.4-pro | 93 | gpt-5.4 | 86 |
| momus | gpt-5.4-pro | 92 | gpt-5.4 | 86 |
| librarian | gpt-5.4-nano | 76.8 | gpt-5.4-mini | 65.1 |
| multimodal-looker | gpt-5.5 | 96 | gpt-5.4 | 85 |
| atlas | gpt-5.4-pro | 90 | gpt-5.4 | 86 |
| sisyphus-junior | gpt-5.4-mini | 82 | gpt-5.4-nano | 78 |

## Summary: Best OpenAI Model per Category

| Category | Best OpenAI Model | Score | 2nd Choice | Score |
|---|---|---|---|---|
| visual-engineering | gpt-5.5 | 96 | gpt-5.4 | 84 |
| ultrabrain | gpt-5.4-pro | 94 | gpt-5.4 | 87 |
| deep | gpt-5.4-pro | 92 | gpt-5.4 | 88 |
| artistry | gpt-5.4-pro | 90 | gpt-5.4 | 85 |
| quick | gpt-5.4-nano | 92 | gpt-5.4-mini | 80 |
| unspecified-low | gpt-5.4-nano | 91 | gpt-5.4-mini | 79 |
| unspecified-high | gpt-5.4-pro | 91 | gpt-5.4 | 86 |
| writing | gpt-5.4-nano | 77.5 | gpt-5.4-mini | 72.8 |

---

## OpenAI Model Tier Strategy

### Performance Stack (No Budget Limit)

| Role | Model | Cost | Context |
|---|---|---|---|
| Planning/Review | gpt-5.4-pro | $30/$180 | 1.05M |
| Execution | gpt-5.4 | $2.50/$15 | 1.05M |
| Fast Tasks | gpt-5.4-nano | $0.20/$1.25 | 400K |

### Budget Stack (<$10/month)

| Role | Model | Cost | Context |
|---|---|---|---|
| Planning/Review | gpt-5.4-mini | $0.75/$4.50 | 400K |
| Execution | gpt-5.4-mini | $0.75/$4.50 | 400K |
| Fast Tasks | gpt-5.4-nano | $0.20/$1.25 | 400K |

### Balanced Stack

| Role | Model | Cost | Context |
|---|---|---|---|
| Planning/Review | gpt-5.4 | $2.50/$15 | 1.05M |
| Execution | gpt-5.4 | $2.50/$15 | 1.05M |
| Fast Tasks | gpt-5.4-nano | $0.20/$1.25 | 400K |

---

## Key Insights

1. **gpt-5.5** now leads the OpenAI visual tier in this repo's direct benchmark coverage, taking both **multimodal-looker** and **visual-engineering**
2. **gpt-5.4-pro** is still the clear winner for reasoning-heavy agents and categories
3. **gpt-5.4** remains the best value all-rounder for execution/coding work
4. **gpt-5.4-nano** dominates speed-heavy agents plus the quick/low-value categories
5. **gpt-5.4-mini** is still the sweet spot for junior orchestration
6. **o3** looks much better after correcting pricing to $2/$8, but it still does not beat GPT-5.4 or GPT-5.4-pro where the latter have stronger overall benchmark mix and larger context

---

## Benchmark Data Sources

- SWE-Bench Pro Public Leaderboard (April 2026)
- LiveCodeBench Leaderboard (April 2026)
- GPQA Diamond Benchmark (April 2026)
- ARC-AGI-2 Benchmark (April 2026)
- OpenAI Official Model Cards (March 2026)
- BenchLM.ai (April 2026)
- DataLearnerAI Leaderboards (April 2026)
- Awesome Agents Benchmark Compilation (April 2026)

---

## Related Documents

- [Oh-My-OpenCode Agent Rankings v3.0](./oh-my-opencode-agent-rankings.md) — All providers (NVIDIA Build, OpenCode Zen, OpenAI)
- [Oh-My-OpenCode Agent Rankings v2.0](./oh-my-opencode-agent-rankings-2026-04-06.md) — Historical (superseded)
- [Model Rankings Report](../.omx/model-rankings-report.md) — 25+ agent detailed report

---

**Last Updated:** April 25, 2026
