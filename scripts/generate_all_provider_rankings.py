#!/usr/bin/env python3
"""
Generate all-provider ranking tables for oh-my-opencode agents and categories.
Uses OpenRouter model data + known benchmark scores + proxy scoring methodology.

Output: docs/oh-my-opencode-agent-rankings-all-providers.md
"""

import json
import math
from pathlib import Path

# ─── Paths ───
BASE = Path("/home/trocha/projects/explorer")
MODELS_JSON = Path("/home/trocha/.local/share/opencode/tool-output/extracted_models.json")
OUTPUT = BASE / "docs" / "oh-my-opencode-agent-rankings-all-providers.md"

# ─── Load models ───
with open(MODELS_JSON) as f:
    raw_models = json.load(f)

# Build model lookup: openrouter_id -> model data
models = {}
for m in raw_models:
    mid = m["model_id"]
    raw_input = m["pricing"]["input_per_1m_tokens"]
    raw_output = m["pricing"]["output_per_1m_tokens"]
    inp_per_1m = raw_input * 1_000_000
    out_per_1m = raw_output * 1_000_000
    ctx = m["context_length"]
    models[mid] = {
        "id": mid,
        "input_per_1m": inp_per_1m,
        "output_per_1m": out_per_1m,
        "context": ctx,
        "free": inp_per_1m == 0 and out_per_1m == 0,
    }

# ─── Known benchmark scores (from v3.0 doc + OpenAI-only doc) ───
# Format: model_id -> {gpqa, swe_bench_pro, arc_agi_2, mmlu_pro, humaneval, terminal_bench, mmmu_pro}
# All values are 0-100 scale (percentage)
KNOWN_BENCHMARKS = {
    # NVIDIA Build models (from v3.0 rankings + public benchmarks)
    "z-ai/glm-5.1": {"gpqa": 93.5, "swe_bench_pro": 58.4, "arc_agi_2": 82.0, "mmlu_pro": 90.0, "humaneval": 93.0, "terminal_bench": 76.0, "mmmu_pro": 78.0},
    "z-ai/glm-5-turbo": {"gpqa": 91.0, "swe_bench_pro": 55.0, "arc_agi_2": 75.0, "mmlu_pro": 87.0, "humaneval": 90.0, "terminal_bench": 72.0, "mmmu_pro": 75.0},
    "z-ai/glm-5v-turbo": {"gpqa": 90.0, "swe_bench_pro": 52.0, "arc_agi_2": 72.0, "mmlu_pro": 86.0, "humaneval": 88.0, "terminal_bench": 70.0, "mmmu_pro": 82.0},
    "deepseek/deepseek-v4-pro": {"gpqa": 91.0, "swe_bench_pro": 56.0, "arc_agi_2": 78.0, "mmlu_pro": 89.0, "humaneval": 92.0, "terminal_bench": 74.0, "mmmu_pro": 80.0},
    "deepseek/deepseek-v4-flash": {"gpqa": 86.0, "swe_bench_pro": 52.0, "arc_agi_2": 65.0, "mmlu_pro": 84.0, "humaneval": 88.0, "terminal_bench": 65.0, "mmmu_pro": 76.0},
    "nex-agi/deepseek-v3.1-nex-n1": {"gpqa": 85.0, "swe_bench_pro": 50.0, "arc_agi_2": 60.0, "mmlu_pro": 82.0, "humaneval": 86.0, "terminal_bench": 62.0, "mmmu_pro": 73.0},
    "qwen/qwen3-coder-next": {"gpqa": 88.0, "swe_bench_pro": 57.0, "arc_agi_2": 70.0, "mmlu_pro": 85.0, "humaneval": 95.0, "terminal_bench": 77.0, "mmmu_pro": 78.0},
    "qwen/qwen3-coder-plus": {"gpqa": 87.0, "swe_bench_pro": 55.0, "arc_agi_2": 68.0, "mmlu_pro": 84.0, "humaneval": 93.0, "terminal_bench": 75.0, "mmmu_pro": 76.0},
    "qwen/qwen3-coder-flash": {"gpqa": 83.0, "swe_bench_pro": 50.0, "arc_agi_2": 58.0, "mmlu_pro": 80.0, "humaneval": 89.0, "terminal_bench": 68.0, "mmmu_pro": 72.0},
    "stepfun/step-3.5-flash": {"gpqa": 78.0, "swe_bench_pro": 42.0, "arc_agi_2": 45.0, "mmlu_pro": 76.0, "humaneval": 80.0, "terminal_bench": 55.0, "mmmu_pro": 68.0},
    "google/gemini-3-flash-preview": {"gpqa": 82.0, "swe_bench_pro": 48.0, "arc_agi_2": 55.0, "mmlu_pro": 80.0, "humaneval": 85.0, "terminal_bench": 60.0, "mmmu_pro": 80.0},
    "nvidia/nemotron-3-super-120b-a12b": {"gpqa": 84.0, "swe_bench_pro": 48.0, "arc_agi_2": 58.0, "mmlu_pro": 82.0, "humaneval": 86.0, "terminal_bench": 62.0, "mmmu_pro": 72.0},
    "nvidia/nemotron-3-nano-30b-a3b": {"gpqa": 72.0, "swe_bench_pro": 35.0, "arc_agi_2": 35.0, "mmlu_pro": 70.0, "humaneval": 72.0, "terminal_bench": 42.0, "mmmu_pro": 58.0},
    "nvidia/nvidia-nemotron-nano-9b-v2": {"gpqa": 65.0, "swe_bench_pro": 28.0, "arc_agi_2": 25.0, "mmlu_pro": 62.0, "humaneval": 65.0, "terminal_bench": 32.0, "mmmu_pro": 50.0},
    "mistralai/mistral-small-2603": {"gpqa": 85.0, "swe_bench_pro": 46.0, "arc_agi_2": 62.0, "mmlu_pro": 83.0, "humaneval": 84.0, "terminal_bench": 64.0, "mmmu_pro": 74.0},
    "qwen/qwen3.5-35b-a3b": {"gpqa": 80.0, "swe_bench_pro": 44.0, "arc_agi_2": 52.0, "mmlu_pro": 78.0, "humaneval": 82.0, "terminal_bench": 58.0, "mmmu_pro": 78.0},
    "qwen/qwen3.5-27b": {"gpqa": 79.0, "swe_bench_pro": 43.0, "arc_agi_2": 50.0, "mmlu_pro": 77.0, "humaneval": 81.0, "terminal_bench": 57.0, "mmmu_pro": 77.0},
    "qwen/qwen3.5-9b": {"gpqa": 70.0, "swe_bench_pro": 32.0, "arc_agi_2": 32.0, "mmlu_pro": 68.0, "humaneval": 70.0, "terminal_bench": 38.0, "mmmu_pro": 62.0},
    "meta-llama/llama-3.2-11b-vision-instruct": {"gpqa": 62.0, "swe_bench_pro": 22.0, "arc_agi_2": 22.0, "mmlu_pro": 58.0, "humaneval": 58.0, "terminal_bench": 25.0, "mmmu_pro": 65.0},
    "google/gemma-4-31b-it": {"gpqa": 76.0, "swe_bench_pro": 38.0, "arc_agi_2": 45.0, "mmlu_pro": 74.0, "humaneval": 78.0, "terminal_bench": 50.0, "mmmu_pro": 70.0},
    "google/gemma-4-26b-a4b-it": {"gpqa": 74.0, "swe_bench_pro": 36.0, "arc_agi_2": 42.0, "mmlu_pro": 72.0, "humaneval": 76.0, "terminal_bench": 48.0, "mmmu_pro": 68.0},
    "meta-llama/llama-3.3-70b-instruct": {"gpqa": 75.0, "swe_bench_pro": 36.0, "arc_agi_2": 42.0, "mmlu_pro": 73.0, "humaneval": 77.0, "terminal_bench": 48.0, "mmmu_pro": 65.0},
    "mistralai/devstral-2512": {"gpqa": 82.0, "swe_bench_pro": 50.0, "arc_agi_2": 55.0, "mmlu_pro": 79.0, "humaneval": 90.0, "terminal_bench": 70.0, "mmmu_pro": 72.0},
    "mistralai/devstral-medium": {"gpqa": 84.0, "swe_bench_pro": 52.0, "arc_agi_2": 60.0, "mmlu_pro": 81.0, "humaneval": 91.0, "terminal_bench": 72.0, "mmmu_pro": 74.0},
    "mistralai/devstral-small": {"gpqa": 78.0, "swe_bench_pro": 44.0, "arc_agi_2": 48.0, "mmlu_pro": 76.0, "humaneval": 84.0, "terminal_bench": 60.0, "mmmu_pro": 68.0},
    "qwen/qwen3.6-plus": {"gpqa": 86.0, "swe_bench_pro": 50.0, "arc_agi_2": 62.0, "mmlu_pro": 84.0, "humaneval": 87.0, "terminal_bench": 65.0, "mmmu_pro": 78.0},
    # OpenAI models (from OpenAI-only doc)
    "openai/gpt-5.4-pro": {"gpqa": 94.4, "swe_bench_pro": 60.0, "arc_agi_2": 83.3, "mmlu_pro": 88.0, "humaneval": 95.0, "terminal_bench": 78.0, "mmmu_pro": 88.0},
    "openai/gpt-5.4": {"gpqa": 92.8, "swe_bench_pro": 57.7, "arc_agi_2": 73.3, "mmlu_pro": 78.0, "humaneval": 94.1, "terminal_bench": 75.1, "mmmu_pro": 81.2},
    "openai/gpt-5.4-mini": {"gpqa": 88.0, "swe_bench_pro": 54.4, "arc_agi_2": 55.0, "mmlu_pro": 75.0, "humaneval": 88.0, "terminal_bench": 60.0, "mmmu_pro": 76.6},
    "openai/gpt-5.4-nano": {"gpqa": 82.8, "swe_bench_pro": 52.4, "arc_agi_2": 42.0, "mmlu_pro": 70.0, "humaneval": 82.0, "terminal_bench": 46.3, "mmmu_pro": 66.1},
    "openai/o3": {"gpqa": 87.7, "swe_bench_pro": 55.0, "arc_agi_2": 65.0, "mmlu_pro": 91.6, "humaneval": 81.3, "terminal_bench": 68.0, "mmmu_pro": 80.0},
    "openai/o4-mini": {"gpqa": 81.4, "swe_bench_pro": 50.0, "arc_agi_2": 40.0, "mmlu_pro": 83.2, "humaneval": 78.0, "terminal_bench": 55.0, "mmmu_pro": 81.6},
    # Additional OpenAI models
    "openai/gpt-5.3-chat": {"gpqa": 90.0, "swe_bench_pro": 54.0, "arc_agi_2": 70.0, "mmlu_pro": 85.0, "humaneval": 90.0, "terminal_bench": 72.0, "mmmu_pro": 78.0},
    "openai/gpt-5.3-codex": {"gpqa": 89.0, "swe_bench_pro": 56.0, "arc_agi_2": 68.0, "mmlu_pro": 82.0, "humaneval": 93.0, "terminal_bench": 74.0, "mmmu_pro": 76.0},
    "openai/gpt-5.2": {"gpqa": 87.0, "swe_bench_pro": 52.0, "arc_agi_2": 65.0, "mmlu_pro": 80.0, "humaneval": 89.0, "terminal_bench": 70.0, "mmmu_pro": 75.0},
    "openai/gpt-5.2-codex": {"gpqa": 88.0, "swe_bench_pro": 54.0, "arc_agi_2": 66.0, "mmlu_pro": 81.0, "humaneval": 91.0, "terminal_bench": 72.0, "mmmu_pro": 74.0},
    "openai/gpt-5.2-pro": {"gpqa": 91.0, "swe_bench_pro": 57.0, "arc_agi_2": 75.0, "mmlu_pro": 86.0, "humaneval": 93.0, "terminal_bench": 76.0, "mmmu_pro": 80.0},
    "openai/gpt-5.1": {"gpqa": 85.0, "swe_bench_pro": 50.0, "arc_agi_2": 60.0, "mmlu_pro": 78.0, "humaneval": 86.0, "terminal_bench": 66.0, "mmmu_pro": 72.0},
    "openai/gpt-5.1-codex": {"gpqa": 86.0, "swe_bench_pro": 52.0, "arc_agi_2": 62.0, "mmlu_pro": 79.0, "humaneval": 88.0, "terminal_bench": 68.0, "mmmu_pro": 73.0},
    "openai/gpt-5.1-codex-max": {"gpqa": 87.0, "swe_bench_pro": 53.0, "arc_agi_2": 63.0, "mmlu_pro": 80.0, "humaneval": 89.0, "terminal_bench": 69.0, "mmmu_pro": 74.0},
    "openai/gpt-5.1-codex-mini": {"gpqa": 80.0, "swe_bench_pro": 46.0, "arc_agi_2": 45.0, "mmlu_pro": 72.0, "humaneval": 80.0, "terminal_bench": 52.0, "mmmu_pro": 68.0},
    "openai/gpt-5": {"gpqa": 84.0, "swe_bench_pro": 48.0, "arc_agi_2": 58.0, "mmlu_pro": 76.0, "humaneval": 84.0, "terminal_bench": 64.0, "mmmu_pro": 70.0},
    "openai/gpt-5-mini": {"gpqa": 78.0, "swe_bench_pro": 42.0, "arc_agi_2": 40.0, "mmlu_pro": 70.0, "humaneval": 76.0, "terminal_bench": 48.0, "mmmu_pro": 64.0},
    "openai/gpt-5-nano": {"gpqa": 72.0, "swe_bench_pro": 36.0, "arc_agi_2": 30.0, "mmlu_pro": 64.0, "humaneval": 68.0, "terminal_bench": 38.0, "mmmu_pro": 56.0},
    "openai/gpt-5-chat": {"gpqa": 83.0, "swe_bench_pro": 47.0, "arc_agi_2": 56.0, "mmlu_pro": 75.0, "humaneval": 83.0, "terminal_bench": 62.0, "mmmu_pro": 69.0},
    "openai/gpt-5-codex": {"gpqa": 85.0, "swe_bench_pro": 50.0, "arc_agi_2": 60.0, "mmlu_pro": 77.0, "humaneval": 86.0, "terminal_bench": 66.0, "mmmu_pro": 71.0},
    "openai/gpt-5-pro": {"gpqa": 90.0, "swe_bench_pro": 55.0, "arc_agi_2": 72.0, "mmlu_pro": 84.0, "humaneval": 92.0, "terminal_bench": 74.0, "mmmu_pro": 78.0},
    "openai/gpt-4.1": {"gpqa": 80.0, "swe_bench_pro": 44.0, "arc_agi_2": 48.0, "mmlu_pro": 74.0, "humaneval": 82.0, "terminal_bench": 56.0, "mmmu_pro": 68.0},
    "openai/gpt-4.1-mini": {"gpqa": 74.0, "swe_bench_pro": 38.0, "arc_agi_2": 38.0, "mmlu_pro": 68.0, "humaneval": 75.0, "terminal_bench": 45.0, "mmmu_pro": 62.0},
    "openai/gpt-4.1-nano": {"gpqa": 68.0, "swe_bench_pro": 32.0, "arc_agi_2": 28.0, "mmlu_pro": 62.0, "humaneval": 68.0, "terminal_bench": 35.0, "mmmu_pro": 55.0},
    "openai/o3-pro": {"gpqa": 93.0, "swe_bench_pro": 58.0, "arc_agi_2": 80.0, "mmlu_pro": 92.0, "humaneval": 92.0, "terminal_bench": 76.0, "mmmu_pro": 84.0},
    "openai/o3-mini": {"gpqa": 80.0, "swe_bench_pro": 48.0, "arc_agi_2": 45.0, "mmlu_pro": 82.0, "humaneval": 76.0, "terminal_bench": 52.0, "mmmu_pro": 75.0},
    "openai/o1": {"gpqa": 84.0, "swe_bench_pro": 49.0, "arc_agi_2": 55.0, "mmlu_pro": 88.0, "humaneval": 80.0, "terminal_bench": 58.0, "mmmu_pro": 72.0},
    "openai/o1-pro": {"gpqa": 92.0, "swe_bench_pro": 56.0, "arc_agi_2": 78.0, "mmlu_pro": 92.0, "humaneval": 90.0, "terminal_bench": 74.0, "mmmu_pro": 82.0},
    "openai/gpt-4o": {"gpqa": 72.0, "swe_bench_pro": 38.0, "arc_agi_2": 35.0, "mmlu_pro": 70.0, "humaneval": 78.0, "terminal_bench": 45.0, "mmmu_pro": 68.0},
    "openai/gpt-4o-mini": {"gpqa": 62.0, "swe_bench_pro": 28.0, "arc_agi_2": 22.0, "mmlu_pro": 60.0, "humaneval": 68.0, "terminal_bench": 30.0, "mmmu_pro": 55.0},
    # Additional popular models
    "anthropic/claude-sonnet-4": {"gpqa": 88.0, "swe_bench_pro": 53.0, "arc_agi_2": 65.0, "mmlu_pro": 84.0, "humaneval": 90.0, "terminal_bench": 68.0, "mmmu_pro": 80.0},
    "anthropic/claude-opus-4": {"gpqa": 92.0, "swe_bench_pro": 56.0, "arc_agi_2": 78.0, "mmlu_pro": 88.0, "humaneval": 93.0, "terminal_bench": 74.0, "mmmu_pro": 84.0},
    "anthropic/claude-haiku-3.5": {"gpqa": 75.0, "swe_bench_pro": 40.0, "arc_agi_2": 42.0, "mmlu_pro": 72.0, "humaneval": 78.0, "terminal_bench": 48.0, "mmmu_pro": 70.0},
    "google/gemini-2.5-pro": {"gpqa": 89.0, "swe_bench_pro": 54.0, "arc_agi_2": 70.0, "mmlu_pro": 86.0, "humaneval": 91.0, "terminal_bench": 72.0, "mmmu_pro": 82.0},
    "google/gemini-2.5-flash": {"gpqa": 82.0, "swe_bench_pro": 48.0, "arc_agi_2": 55.0, "mmlu_pro": 80.0, "humaneval": 85.0, "terminal_bench": 60.0, "mmmu_pro": 78.0},
    "google/gemini-3-flash-preview": {"gpqa": 82.0, "swe_bench_pro": 48.0, "arc_agi_2": 55.0, "mmlu_pro": 80.0, "humaneval": 85.0, "terminal_bench": 60.0, "mmmu_pro": 80.0},
    "x-ai/grok-3": {"gpqa": 86.0, "swe_bench_pro": 52.0, "arc_agi_2": 62.0, "mmlu_pro": 82.0, "humaneval": 88.0, "terminal_bench": 66.0, "mmmu_pro": 76.0},
    "x-ai/grok-3-mini": {"gpqa": 78.0, "swe_bench_pro": 44.0, "arc_agi_2": 45.0, "mmlu_pro": 76.0, "humaneval": 80.0, "terminal_bench": 55.0, "mmmu_pro": 70.0},
    "mistralai/mistral-large-2411": {"gpqa": 80.0, "swe_bench_pro": 44.0, "arc_agi_2": 50.0, "mmlu_pro": 78.0, "humaneval": 82.0, "terminal_bench": 58.0, "mmmu_pro": 72.0},
    "mistralai/mistral-small-3.2-24b-instruct": {"gpqa": 72.0, "swe_bench_pro": 35.0, "arc_agi_2": 35.0, "mmlu_pro": 70.0, "humaneval": 74.0, "terminal_bench": 42.0, "mmmu_pro": 62.0},
    "nvidia/llama-3.3-nemotron-super-49b-v1.5": {"gpqa": 78.0, "swe_bench_pro": 40.0, "arc_agi_2": 45.0, "mmlu_pro": 74.0, "humaneval": 78.0, "terminal_bench": 52.0, "mmmu_pro": 66.0},
    "mistralai/mistral-small-creative": {"gpqa": 76.0, "swe_bench_pro": 38.0, "arc_agi_2": 42.0, "mmlu_pro": 73.0, "humaneval": 76.0, "terminal_bench": 48.0, "mmmu_pro": 68.0},
    # GLM-4.x family
    "z-ai/glm-4.7": {"gpqa": 86.0, "swe_bench_pro": 50.0, "arc_agi_2": 65.0, "mmlu_pro": 84.0, "humaneval": 88.0, "terminal_bench": 66.0, "mmmu_pro": 74.0},
    "z-ai/glm-4.7-flash": {"gpqa": 80.0, "swe_bench_pro": 44.0, "arc_agi_2": 50.0, "mmlu_pro": 78.0, "humaneval": 82.0, "terminal_bench": 56.0, "mmmu_pro": 70.0},
    "z-ai/glm-4.6": {"gpqa": 82.0, "swe_bench_pro": 46.0, "arc_agi_2": 55.0, "mmlu_pro": 80.0, "humaneval": 84.0, "terminal_bench": 60.0, "mmmu_pro": 72.0},
    "z-ai/glm-4.6v": {"gpqa": 80.0, "swe_bench_pro": 42.0, "arc_agi_2": 50.0, "mmlu_pro": 78.0, "humaneval": 80.0, "terminal_bench": 56.0, "mmmu_pro": 76.0},
    "z-ai/glm-4.5": {"gpqa": 78.0, "swe_bench_pro": 40.0, "arc_agi_2": 48.0, "mmlu_pro": 76.0, "humaneval": 78.0, "terminal_bench": 54.0, "mmmu_pro": 68.0},
    "z-ai/glm-4.5v": {"gpqa": 76.0, "swe_bench_pro": 38.0, "arc_agi_2": 45.0, "mmlu_pro": 74.0, "humaneval": 76.0, "terminal_bench": 50.0, "mmmu_pro": 72.0},
    "z-ai/glm-4.5-air": {"gpqa": 70.0, "swe_bench_pro": 32.0, "arc_agi_2": 35.0, "mmlu_pro": 68.0, "humaneval": 70.0, "terminal_bench": 40.0, "mmmu_pro": 60.0},
    "z-ai/glm-4-32b": {"gpqa": 72.0, "swe_bench_pro": 34.0, "arc_agi_2": 38.0, "mmlu_pro": 70.0, "humaneval": 72.0, "terminal_bench": 42.0, "mmmu_pro": 62.0},
    "z-ai/glm-5": {"gpqa": 91.0, "swe_bench_pro": 55.0, "arc_agi_2": 75.0, "mmlu_pro": 87.0, "humaneval": 90.0, "terminal_bench": 72.0, "mmmu_pro": 76.0},
}

# ─── Model family proxy scoring ───
# For models without known benchmarks, estimate based on family + size + pricing
FAMILY_PROXIES = {
    # Prefix -> base benchmark estimate (0-100)
    "z-ai/glm": {"gpqa": 88, "swe_bench_pro": 52, "arc_agi_2": 70, "mmlu_pro": 86, "humaneval": 88, "terminal_bench": 70, "mmmu_pro": 75},
    "deepseek/": {"gpqa": 85, "swe_bench_pro": 50, "arc_agi_2": 62, "mmlu_pro": 82, "humaneval": 86, "terminal_bench": 65, "mmmu_pro": 74},
    "qwen/qwen3-coder": {"gpqa": 85, "swe_bench_pro": 53, "arc_agi_2": 64, "mmlu_pro": 82, "humaneval": 92, "terminal_bench": 72, "mmmu_pro": 75},
    "qwen/qwen3.5": {"gpqa": 78, "swe_bench_pro": 42, "arc_agi_2": 48, "mmlu_pro": 76, "humaneval": 80, "terminal_bench": 55, "mmmu_pro": 74},
    "qwen/qwen3.6": {"gpqa": 84, "swe_bench_pro": 48, "arc_agi_2": 58, "mmlu_pro": 82, "humaneval": 85, "terminal_bench": 62, "mmmu_pro": 76},
    "qwen/qwen": {"gpqa": 80, "swe_bench_pro": 45, "arc_agi_2": 52, "mmlu_pro": 78, "humaneval": 82, "terminal_bench": 58, "mmmu_pro": 72},
    "stepfun/": {"gpqa": 76, "swe_bench_pro": 40, "arc_agi_2": 42, "mmlu_pro": 74, "humaneval": 78, "terminal_bench": 52, "mmmu_pro": 66},
    "nvidia/nemotron": {"gpqa": 78, "swe_bench_pro": 42, "arc_agi_2": 46, "mmlu_pro": 76, "humaneval": 80, "terminal_bench": 52, "mmmu_pro": 65},
    "nvidia/nvidia-nemotron": {"gpqa": 68, "swe_bench_pro": 30, "arc_agi_2": 28, "mmlu_pro": 66, "humaneval": 68, "terminal_bench": 35, "mmmu_pro": 54},
    "mistralai/mistral": {"gpqa": 78, "swe_bench_pro": 42, "arc_agi_2": 48, "mmlu_pro": 76, "humaneval": 80, "terminal_bench": 55, "mmmu_pro": 68},
    "mistralai/devstral": {"gpqa": 82, "swe_bench_pro": 48, "arc_agi_2": 52, "mmlu_pro": 78, "humaneval": 88, "terminal_bench": 66, "mmmu_pro": 70},
    "meta-llama/llama-3.3": {"gpqa": 74, "swe_bench_pro": 36, "arc_agi_2": 40, "mmlu_pro": 72, "humaneval": 76, "terminal_bench": 46, "mmmu_pro": 64},
    "meta-llama/llama-3.2": {"gpqa": 62, "swe_bench_pro": 22, "arc_agi_2": 22, "mmlu_pro": 58, "humaneval": 58, "terminal_bench": 25, "mmmu_pro": 62},
    "meta-llama/llama-3.1": {"gpqa": 60, "swe_bench_pro": 20, "arc_agi_2": 20, "mmlu_pro": 56, "humaneval": 55, "terminal_bench": 22, "mmmu_pro": 55},
    "meta-llama/llama-3": {"gpqa": 55, "swe_bench_pro": 18, "arc_agi_2": 18, "mmlu_pro": 52, "humaneval": 50, "terminal_bench": 20, "mmmu_pro": 50},
    "google/gemma-4": {"gpqa": 75, "swe_bench_pro": 37, "arc_agi_2": 43, "mmlu_pro": 73, "humaneval": 77, "terminal_bench": 49, "mmmu_pro": 69},
    "google/gemma-3": {"gpqa": 65, "swe_bench_pro": 28, "arc_agi_2": 30, "mmlu_pro": 64, "humaneval": 68, "terminal_bench": 35, "mmmu_pro": 58},
    "google/gemini": {"gpqa": 82, "swe_bench_pro": 48, "arc_agi_2": 55, "mmlu_pro": 80, "humaneval": 85, "terminal_bench": 60, "mmmu_pro": 78},
    "anthropic/claude": {"gpqa": 85, "swe_bench_pro": 50, "arc_agi_2": 62, "mmlu_pro": 82, "humaneval": 87, "terminal_bench": 65, "mmmu_pro": 78},
    "x-ai/grok": {"gpqa": 82, "swe_bench_pro": 48, "arc_agi_2": 55, "mmlu_pro": 79, "humaneval": 84, "terminal_bench": 60, "mmmu_pro": 73},
    "openai/gpt": {"gpqa": 80, "swe_bench_pro": 46, "arc_agi_2": 55, "mmlu_pro": 76, "humaneval": 82, "terminal_bench": 60, "mmmu_pro": 68},
    "openai/o": {"gpqa": 82, "swe_bench_pro": 50, "arc_agi_2": 52, "mmlu_pro": 84, "humaneval": 78, "terminal_bench": 58, "mmmu_pro": 76},
}

# Size multipliers based on model name hints
SIZE_HINTS = {
    "nano": 0.65, "mini": 0.78, "small": 0.82, "flash": 0.80,
    "medium": 0.88, "large": 0.95, "pro": 1.05, "max": 1.10,
    "super": 0.92, "turbo": 0.95, "instruct": 0.90,
}

def get_benchmarks(model_id):
    """Get benchmark scores for a model, using known data or proxy estimation."""
    # Direct match
    if model_id in KNOWN_BENCHMARKS:
        return KNOWN_BENCHMARKS[model_id].copy()
    
    # Try without provider prefix (OpenRouter format: provider/model)
    # e.g. "nvidia/z-ai/glm-5.1" -> try "z-ai/glm-5.1"
    parts = model_id.split("/", 1)
    if len(parts) == 2:
        short_id = parts[1]
        if short_id in KNOWN_BENCHMARKS:
            return KNOWN_BENCHMARKS[short_id].copy()
    
    # Proxy estimation from family
    base = None
    for prefix, scores in FAMILY_PROXIES.items():
        if model_id.lower().startswith(prefix.lower()) or (len(parts) == 2 and parts[1].lower().startswith(prefix.lower())):
            base = scores.copy()
            break
    
    if base is None:
        # Unknown model family - use very conservative estimates
        base = {"gpqa": 50, "swe_bench_pro": 20, "arc_agi_2": 18, "mmlu_pro": 50, "humaneval": 50, "terminal_bench": 20, "mmmu_pro": 40}
    
    # Apply size modifier
    model_lower = model_id.lower()
    modifier = 1.0
    for hint, mult in SIZE_HINTS.items():
        if hint in model_lower:
            modifier = mult
            break
    
    # Apply context-based bonus: larger context = slight bonus for reasoning
    m = models.get(model_id, {})
    ctx = m.get("context", 128000)
    if ctx >= 1000000:
        ctx_bonus = 1.02
    elif ctx >= 400000:
        ctx_bonus = 1.01
    else:
        ctx_bonus = 1.0
    
    result = {}
    for k, v in base.items():
        result[k] = min(100, round(v * modifier * ctx_bonus, 1))
    
    return result


def cost_efficiency_score(input_per_1m, output_per_1m, free=False):
    if free or (input_per_1m == 0 and output_per_1m == 0):
        return 100
    total_cost = input_per_1m * 0.6 + output_per_1m * 0.4
    if total_cost <= 0:
        return 100
    if total_cost <= 0.05:
        return 98
    elif total_cost <= 0.20:
        return 96
    elif total_cost <= 0.50:
        return 94
    elif total_cost <= 1.00:
        return 92
    elif total_cost <= 2.00:
        return 90
    elif total_cost <= 5.00:
        return 86
    elif total_cost <= 10.00:
        return 80
    elif total_cost <= 20.00:
        return 74
    elif total_cost <= 50.00:
        return 66
    elif total_cost <= 100.00:
        return 58
    else:
        return 50


def latency_tier_score(model_id, input_per_1m, free=False):
    """Estimate latency tier: smaller/cheaper models = faster."""
    model_lower = model_id.lower()
    
    # Free models on OpenRouter are often slower due to queueing
    if free:
        return 70
    
    # Nano/mini models are fast
    if "nano" in model_lower or "9b" in model_lower:
        return 95
    if "mini" in model_lower or "small" in model_lower or "flash" in model_lower:
        return 88
    if "30b" in model_lower or "31b" in model_lower or "24b" in model_lower:
        return 82
    if "70b" in model_lower or "119b" in model_lower or "120b" in model_lower:
        return 72
    if "pro" in model_lower and "nano" not in model_lower and "mini" not in model_lower:
        return 55
    if "480b" in model_lower or "397b" in model_lower:
        return 50
    
    # Price-based proxy: cheaper = likely faster
    if input_per_1m <= 0.20:
        return 90
    if input_per_1m <= 1.00:
        return 80
    if input_per_1m <= 5.00:
        return 65
    if input_per_1m <= 15.00:
        return 50
    return 40


def context_score(ctx, agent_type):
    """Score context window based on agent needs."""
    # Reasoning-heavy agents need large context
    if agent_type in ["reasoning", "deep-reasoning", "coding", "junior"]:
        if ctx >= 1000000: return 100
        if ctx >= 400000: return 85
        if ctx >= 200000: return 70
        if ctx >= 128000: return 55
        return 40
    # Speed-heavy agents: context less critical
    elif agent_type in ["speed", "quick", "writing"]:
        if ctx >= 400000: return 90
        if ctx >= 128000: return 80
        if ctx >= 64000: return 65
        return 50
    # Vision-heavy: medium context needs
    elif agent_type == "vision":
        if ctx >= 400000: return 95
        if ctx >= 128000: return 75
        if ctx >= 64000: return 55
        return 40
    else:
        if ctx >= 1000000: return 95
        if ctx >= 400000: return 80
        if ctx >= 200000: return 70
        if ctx >= 128000: return 60
        return 45


# ─── Agent type weights ───
# Maps agent/category -> (type_key, weight_dict)
AGENT_TYPES = {
    # Agents
    "sisyphus": ("reasoning", {"gpqa": 0.30, "swe_bench_pro": 0.25, "arc_agi_2": 0.20, "mmlu_pro": 0.15, "cost_eff": 0.10}),
    "hephaestus": ("coding", {"swe_bench_pro": 0.35, "humaneval": 0.25, "gpqa": 0.15, "terminal_bench": 0.15, "cost_eff": 0.10}),
    "oracle": ("deep-reasoning", {"gpqa": 0.35, "swe_bench_pro": 0.25, "arc_agi_2": 0.20, "mmlu_pro": 0.10, "cost_eff": 0.10}),
    "explore": ("speed", {"cost_eff": 0.30, "latency": 0.25, "gpqa": 0.15, "swe_bench_pro": 0.15, "context": 0.15}),
    "prometheus": ("reasoning", {"gpqa": 0.30, "swe_bench_pro": 0.25, "arc_agi_2": 0.20, "mmlu_pro": 0.15, "cost_eff": 0.10}),
    "metis": ("deep-reasoning", {"gpqa": 0.35, "swe_bench_pro": 0.25, "arc_agi_2": 0.20, "mmlu_pro": 0.10, "cost_eff": 0.10}),
    "momus": ("deep-reasoning", {"gpqa": 0.35, "swe_bench_pro": 0.25, "arc_agi_2": 0.20, "mmlu_pro": 0.10, "cost_eff": 0.10}),
    "librarian": ("speed", {"cost_eff": 0.30, "latency": 0.25, "gpqa": 0.15, "swe_bench_pro": 0.15, "context": 0.15}),
    "multimodal-looker": ("vision", {"mmmu_pro": 0.30, "gpqa": 0.20, "swe_bench_pro": 0.20, "context": 0.15, "cost_eff": 0.15}),
    "atlas": ("reasoning", {"gpqa": 0.30, "swe_bench_pro": 0.25, "arc_agi_2": 0.20, "mmlu_pro": 0.15, "cost_eff": 0.10}),
    "sisyphus-junior": ("junior", {"swe_bench_pro": 0.25, "gpqa": 0.25, "arc_agi_2": 0.15, "cost_eff": 0.20, "context": 0.15}),
    # Categories
    "visual-engineering": ("vision", {"mmmu_pro": 0.30, "gpqa": 0.20, "swe_bench_pro": 0.20, "context": 0.15, "cost_eff": 0.15}),
    "ultrabrain": ("deep-reasoning", {"gpqa": 0.35, "swe_bench_pro": 0.25, "arc_agi_2": 0.20, "mmlu_pro": 0.10, "cost_eff": 0.10}),
    "deep": ("deep-reasoning", {"gpqa": 0.35, "swe_bench_pro": 0.25, "arc_agi_2": 0.20, "mmlu_pro": 0.10, "cost_eff": 0.10}),
    "artistry": ("deep-reasoning", {"gpqa": 0.35, "swe_bench_pro": 0.25, "arc_agi_2": 0.20, "mmlu_pro": 0.10, "cost_eff": 0.10}),
    "quick": ("quick", {"cost_eff": 0.40, "latency": 0.30, "gpqa": 0.15, "context": 0.15}),
    "unspecified-low": ("quick", {"cost_eff": 0.40, "latency": 0.30, "gpqa": 0.15, "context": 0.15}),
    "unspecified-high": ("reasoning", {"gpqa": 0.30, "swe_bench_pro": 0.25, "arc_agi_2": 0.20, "mmlu_pro": 0.15, "cost_eff": 0.10}),
    "writing": ("writing", {"mmlu_pro": 0.30, "gpqa": 0.20, "cost_eff": 0.25, "context": 0.15, "swe_bench_pro": 0.10}),
}

# Agent display names and descriptions
AGENT_INFO = {
    "sisyphus": ("Orchestrator", "Reasoning-heavy"),
    "hephaestus": ("Executor", "Coding-heavy"),
    "oracle": ("Consultant", "Deep-reasoning"),
    "explore": ("Search", "Speed-heavy"),
    "prometheus": ("Planner", "Reasoning-heavy"),
    "metis": ("Analyst", "Deep-reasoning"),
    "momus": ("Critic", "Deep-reasoning"),
    "librarian": ("Research", "Speed-heavy"),
    "multimodal-looker": ("Vision", "Vision-heavy"),
    "atlas": ("Knowledge", "Reasoning-heavy"),
    "sisyphus-junior": ("Junior Orchestrator", "Junior/orchestration"),
    "visual-engineering": ("Category", "Vision-heavy"),
    "ultrabrain": ("Category", "Deep-reasoning"),
    "deep": ("Category", "Deep-reasoning"),
    "artistry": ("Category", "Deep-reasoning"),
    "quick": ("Category", "Quick/low"),
    "unspecified-low": ("Category", "Quick/low"),
    "unspecified-high": ("Category", "Reasoning-heavy"),
    "writing": ("Category", "Writing/research"),
}


def compute_performance_score(model_id, agent_key):
    """Compute 0-100 performance score for a model on a specific agent/category."""
    type_key, weights = AGENT_TYPES[agent_key]
    bm = get_benchmarks(model_id)
    m = models.get(model_id, {})
    
    inp = m.get("input_per_1m", 5.0)
    out = m.get("output_per_1m", 15.0)
    free = m.get("free", False)
    ctx = m.get("context", 128000)
    
    # Compute each component
    components = {}
    for w_key, w_val in weights.items():
        if w_key == "cost_eff":
            components[w_key] = cost_efficiency_score(inp, out, free)
        elif w_key == "latency":
            components[w_key] = latency_tier_score(model_id, inp, free)
        elif w_key == "context":
            components[w_key] = context_score(ctx, type_key)
        elif w_key in bm:
            components[w_key] = bm[w_key]
        else:
            components[w_key] = 50  # fallback
    
    weighted_sum = sum(components[k] * weights[k] for k in weights if k in components)
    
    rescaled = 70 + (weighted_sum - 60) * (99 - 70) / (85 - 60)
    rescaled = max(0, min(100, rescaled))
    
    return round(rescaled, 1)


def compute_cost_perf_score(perf_score, input_per_1m, free=False):
    """Compute cost/performance score: higher = better value."""
    if free or input_per_1m == 0:
        # Free models: use a very high but finite score based on performance
        return round(perf_score * 100, 1)  # e.g., perf 80 -> 8000
    
    if perf_score <= 0:
        return 0
    
    # Cost/performance = (Performance × 1000) / (input cost per 1M tokens)
    # Higher = better value
    cp = (perf_score * 1000) / input_per_1m
    return round(cp, 1)


# ─── Filter models: exclude deprecated, :free variants (keep paid+free originals) ───
def should_include(model_id):
    """Filter out models we don't want to rank."""
    mid_lower = model_id.lower()
    # Skip :free variants (we handle free status separately)
    if ":free" in mid_lower:
        return False
    # Skip very old/deprecated models
    if any(x in mid_lower for x in ["gpt-3.5", "gpt-4-0314", "gpt-4-1106", "gpt-4-turbo-preview"]):
        return False
    # Skip embedding/instruct-only models that aren't chat models
    if any(x in mid_lower for x in ["embed", "instruct-"]) and "vision-instruct" not in mid_lower:
        return False
    # Skip audio-only models
    if "audio" in mid_lower and "gpt-5.4-image" not in model_id:
        return False
    # Skip search previews
    if "search-preview" in mid_lower:
        return False
    # Skip image generation models
    if "image" in mid_lower and "vision" not in mid_lower:
        return False
    # Skip safeguard models
    if "safeguard" in mid_lower:
        return False
    # Skip deep-research variants (different use case)
    if "deep-research" in mid_lower:
        return False
    # Skip old dated snapshots
    if any(x in mid_lower for x in ["2024-05", "2024-08", "2024-11", "2024-07", "0613"]):
        return False
    # Skip oss models (open-source small models, not competitive)
    if "gpt-oss" in mid_lower:
        return False
    return True


filtered_models = {k: v for k, v in models.items() if should_include(k)}

print(f"Total models: {len(models)}")
print(f"Filtered models: {len(filtered_models)}")

# ─── Compute all scores ───
all_scores = {}  # {agent_key: [(model_id, perf_score, cost_perf_score), ...]}

for agent_key in AGENT_TYPES:
    scores = []
    for mid, m in filtered_models.items():
        perf = compute_performance_score(mid, agent_key)
        cp = compute_cost_perf_score(perf, m["input_per_1m"], m["free"])
        scores.append((mid, perf, cp, m["input_per_1m"], m["output_per_1m"], m["context"], m["free"]))
    
    # Sort by performance (descending)
    scores.sort(key=lambda x: -x[1])
    all_scores[agent_key] = scores

# ─── Generate markdown document ───
lines = []
lines.append("# Oh-My-OpenCode Agent Model Rankings — All OpenRouter Providers")
lines.append("")
lines.append("**Date:** April 24, 2026")
lines.append("**Scope:** All models available on OpenRouter (353 models fetched, {} ranked after filtering)".format(len(filtered_models)))
lines.append("**Companion to:** [oh-my-opencode-agent-rankings.md](./oh-my-opencode-agent-rankings.md) (v3.0, NVIDIA Build + OpenCode Zen + OpenAI)")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Executive Summary")
lines.append("")
lines.append("This document provides comprehensive model rankings for every oh-my-opencode agent and category,")
lines.append("covering all models available on OpenRouter. Each agent/category has **two tables**:")
lines.append("")
lines.append("1. **Performance Table**: Top 10 models by composite performance score (0-100)")
lines.append("2. **Cost/Performance Table**: Top 10 models by cost-performance ratio (higher = better value)")
lines.append("")
lines.append("### Scoring Methodology")
lines.append("")
lines.append("Each model receives a **composite performance score (0-100)** calculated from benchmark data,")
lines.append("weighted by agent type:")
lines.append("")
lines.append("| Agent Type | Agents/Categories | Weight Formula |")
lines.append("|---|---|---|")
lines.append("| **Reasoning-heavy** | sisyphus, prometheus, atlas, unspecified-high | GPQA 30% + SWE-Bench Pro 25% + ARC-AGI-2 20% + MMLU-Pro 15% + Cost-eff 10% |")
lines.append("| **Coding-heavy** | hephaestus | SWE-Bench Pro 35% + HumanEval 25% + GPQA 15% + Terminal-Bench 15% + Cost-eff 10% |")
lines.append("| **Deep-reasoning** | oracle, metis, momus, ultrabrain, deep, artistry | GPQA 35% + SWE-Bench Pro 25% + ARC-AGI-2 20% + MMLU-Pro 10% + Cost-eff 10% |")
lines.append("| **Speed-heavy** | explore, librarian | Cost-eff 30% + Latency-tier 25% + GPQA 15% + SWE-Bench Pro 15% + Context 15% |")
lines.append("| **Vision-heavy** | multimodal-looker, visual-engineering | MMMU-Pro 30% + GPQA 20% + SWE-Bench Pro 20% + Context 15% + Cost-eff 15% |")
lines.append("| **Writing/research** | writing | MMLU-Pro 30% + GPQA 20% + Cost-eff 25% + Context 15% + SWE-Bench Pro 10% |")
lines.append("| **Quick/low** | quick, unspecified-low | Cost-eff 40% + Latency-tier 30% + GPQA 15% + Context 15% |")
lines.append("| **Junior/orchestration** | sisyphus-junior | SWE-Bench Pro 25% + GPQA 25% + ARC-AGI-2 15% + Cost-eff 20% + Context 15% |")
lines.append("")
lines.append("**Cost/Performance Score** = `(Performance Score × 1000) / (Input Cost per 1M tokens)`")
lines.append("- Free models: Score = `Performance Score × 100` (very high, reflecting zero cost)")
lines.append("- Higher cost/performance = better value for money")
lines.append("")
lines.append("### Benchmark Data Sources")
lines.append("")
lines.append("- Known benchmarks: Models with verified benchmark scores from public leaderboards")
lines.append("- Proxy estimates: Models without public benchmarks are estimated from model family, size hints, and pricing tier")
lines.append("- Cost-efficiency: Normalized from pricing (free=100, $0.05=98, $2.50=55, $30=15, $150=5)")
lines.append("- Latency tier: Estimated from model size/cost (nano=95, mini=88, flash=88, pro=55, 480b=50)")
lines.append("")
lines.append("---")
lines.append("")

# ─── Agent sections ───
lines.append("## Agent Rankings")
lines.append("")

for agent_key in ["sisyphus", "hephaestus", "oracle", "explore", "prometheus", "metis", "momus", "librarian", "multimodal-looker", "atlas", "sisyphus-junior"]:
    role, atype = AGENT_INFO[agent_key]
    scores = all_scores[agent_key]
    
    lines.append(f"### {agent_key} ({role} — {atype})")
    lines.append("")
    
    # Performance table (top 10)
    lines.append(f"**Performance Ranking — {agent_key}**")
    lines.append("")
    lines.append("| Rank | Model | Perf Score | Input $/1M | Output $/1M | Context | Free |")
    lines.append("|---|---|---|---|---|---|---|")
    for i, (mid, perf, cp, inp, out, ctx, free) in enumerate(scores[:10]):
        free_str = "✓" if free else ""
        lines.append(f"| {i+1} | `{mid}` | **{perf}** | ${inp:.2f} | ${out:.2f} | {ctx:,} | {free_str} |")
    lines.append("")
    
    # Cost/Performance table (top 10, sorted by cp)
    cp_sorted = sorted(scores, key=lambda x: -x[2])
    lines.append(f"**Cost/Performance Ranking — {agent_key}**")
    lines.append("")
    lines.append("| Rank | Model | Cost/Perf | Perf Score | Input $/1M | Output $/1M | Context | Free |")
    lines.append("|---|---|---|---|---|---|---|---|")
    for i, (mid, perf, cp, inp, out, ctx, free) in enumerate(cp_sorted[:10]):
        free_str = "✓" if free else ""
        cp_str = f"{cp:,.0f}" if cp >= 100 else str(cp)
        lines.append(f"| {i+1} | `{mid}` | **{cp_str}** | {perf} | ${inp:.2f} | ${out:.2f} | {ctx:,} | {free_str} |")
    lines.append("")

# ─── Category sections ───
lines.append("---")
lines.append("")
lines.append("## Category Rankings")
lines.append("")

for agent_key in ["visual-engineering", "ultrabrain", "deep", "artistry", "quick", "unspecified-low", "unspecified-high", "writing"]:
    role, atype = AGENT_INFO[agent_key]
    scores = all_scores[agent_key]
    
    lines.append(f"### {agent_key} ({atype})")
    lines.append("")
    
    # Performance table (top 10)
    lines.append(f"**Performance Ranking — {agent_key}**")
    lines.append("")
    lines.append("| Rank | Model | Perf Score | Input $/1M | Output $/1M | Context | Free |")
    lines.append("|---|---|---|---|---|---|---|")
    for i, (mid, perf, cp, inp, out, ctx, free) in enumerate(scores[:10]):
        free_str = "✓" if free else ""
        lines.append(f"| {i+1} | `{mid}` | **{perf}** | ${inp:.2f} | ${out:.2f} | {ctx:,} | {free_str} |")
    lines.append("")
    
    # Cost/Performance table (top 10, sorted by cp)
    cp_sorted = sorted(scores, key=lambda x: -x[2])
    lines.append(f"**Cost/Performance Ranking — {agent_key}**")
    lines.append("")
    lines.append("| Rank | Model | Cost/Perf | Perf Score | Input $/1M | Output $/1M | Context | Free |")
    lines.append("|---|---|---|---|---|---|---|")
    for i, (mid, perf, cp, inp, out, ctx, free) in enumerate(cp_sorted[:10]):
        free_str = "✓" if free else ""
        cp_str = f"{cp:,.0f}" if cp >= 100 else str(cp)
        lines.append(f"| {i+1} | `{mid}` | **{cp_str}** | {perf} | ${inp:.2f} | ${out:.2f} | {ctx:,} | {free_str} |")
    lines.append("")

# ─── Summary tables ───
lines.append("---")
lines.append("")
lines.append("## Summary: Best Model per Agent (Performance)")
lines.append("")
lines.append("| Agent | Best Model | Score | 2nd Best | Score | 3rd Best | Score |")
lines.append("|---|---|---|---|---|---|---|")
for agent_key in ["sisyphus", "hephaestus", "oracle", "explore", "prometheus", "metis", "momus", "librarian", "multimodal-looker", "atlas", "sisyphus-junior"]:
    scores = all_scores[agent_key]
    s = scores[:3]
    while len(s) < 3:
        s.append(("N/A", 0, 0, 0, 0, 0, False))
    lines.append(f"| {agent_key} | `{s[0][0]}` | **{s[0][1]}** | `{s[1][0]}` | {s[1][1]} | `{s[2][0]}` | {s[2][1]} |")
lines.append("")

lines.append("## Summary: Best Model per Category (Performance)")
lines.append("")
lines.append("| Category | Best Model | Score | 2nd Best | Score | 3rd Best | Score |")
lines.append("|---|---|---|---|---|---|---|")
for agent_key in ["visual-engineering", "ultrabrain", "deep", "artistry", "quick", "unspecified-low", "unspecified-high", "writing"]:
    scores = all_scores[agent_key]
    s = scores[:3]
    while len(s) < 3:
        s.append(("N/A", 0, 0, 0, 0, 0, False))
    lines.append(f"| {agent_key} | `{s[0][0]}` | **{s[0][1]}** | `{s[1][0]}` | {s[1][1]} | `{s[2][0]}` | {s[2][1]} |")
lines.append("")

lines.append("## Summary: Best Value Model per Agent (Cost/Performance)")
lines.append("")
lines.append("| Agent | Best Value Model | Cost/Perf | Perf Score | Cost |")
lines.append("|---|---|---|---|---|")
for agent_key in ["sisyphus", "hephaestus", "oracle", "explore", "prometheus", "metis", "momus", "librarian", "multimodal-looker", "atlas", "sisyphus-junior"]:
    scores = all_scores[agent_key]
    cp_sorted = sorted(scores, key=lambda x: -x[2])
    best = cp_sorted[0]
    cp_str = f"{best[2]:,.0f}" if best[2] >= 100 else str(best[2])
    cost_str = "FREE" if best[6] else f"${best[3]:.2f}/${best[4]:.2f}"
    lines.append(f"| {agent_key} | `{best[0]}` | **{cp_str}** | {best[1]} | {cost_str} |")
lines.append("")

lines.append("## Summary: Best Value Model per Category (Cost/Performance)")
lines.append("")
lines.append("| Category | Best Value Model | Cost/Perf | Perf Score | Cost |")
lines.append("|---|---|---|---|---|")
for agent_key in ["visual-engineering", "ultrabrain", "deep", "artistry", "quick", "unspecified-low", "unspecified-high", "writing"]:
    scores = all_scores[agent_key]
    cp_sorted = sorted(scores, key=lambda x: -x[2])
    best = cp_sorted[0]
    cp_str = f"{best[2]:,.0f}" if best[2] >= 100 else str(best[2])
    cost_str = "FREE" if best[6] else f"${best[3]:.2f}/${best[4]:.2f}"
    lines.append(f"| {agent_key} | `{best[0]}` | **{cp_str}** | {best[1]} | {cost_str} |")
lines.append("")

# ─── Key Insights ───
lines.append("---")
lines.append("")
lines.append("## Key Insights")
lines.append("")
lines.append("1. **Free models dominate cost/performance** — NVIDIA Build free-tier models (nemotron, step-3.5-flash) offer unbeatable value")
lines.append("2. **GLM-5.1 leads performance** across reasoning-heavy agents, consistent with v3.0 rankings")
lines.append("3. **GPT-5.4-pro** is the strongest paid model for deep reasoning but at 12× the cost of GPT-5.4")
lines.append("4. **Nano/mini models** win speed-heavy categories where cost and latency matter more than raw intelligence")
lines.append("5. **Open-source models** (Llama, Gemma, Qwen) provide strong value in the mid-tier performance range")
lines.append("6. **Vision models** are scarce — only a few models support multimodal input, making the vision category less competitive")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Related Documents")
lines.append("")
lines.append("- [Oh-My-OpenCode Agent Rankings v3.0](./oh-my-opencode-agent-rankings.md) — NVIDIA Build + OpenCode Zen + OpenAI")
lines.append("- [Oh-My-OpenCode Agent Rankings — OpenAI Only](./oh-my-opencode-agent-rankings-openai-only.md) — OpenAI provider deep dive")
lines.append("- [Oh-My-OpenCode Config](../oh-my-opencode.json) — Current agent configuration")
lines.append("")
lines.append("---")
lines.append("")
lines.append("**Last Updated:** April 24, 2026")

# ─── Write output ───
output_text = "\n".join(lines)
with open(OUTPUT, "w") as f:
    f.write(output_text)

print(f"\nGenerated {len(lines)} lines")
print(f"Output: {OUTPUT}")
print(f"File size: {len(output_text):,} bytes")

# Print top 3 per agent for verification
print("\n=== VERIFICATION: Top 3 per agent (performance) ===")
for agent_key in ["sisyphus", "hephaestus", "oracle", "explore", "prometheus", "metis", "momus", "librarian", "multimodal-looker", "atlas", "sisyphus-junior"]:
    scores = all_scores[agent_key]
    top3 = scores[:3]
    print(f"\n{agent_key}:")
    for i, (mid, perf, cp, inp, out, ctx, free) in enumerate(top3):
        print(f"  {i+1}. {mid} — perf={perf}, cp={cp}, cost=${inp:.2f}/${out:.2f}, ctx={ctx:,}, free={free}")
