# Model Configuration Update Documentation - CORRECTED

## Summary
Updated all references to the unavailable `opencode/qwen3.6-plus-free` model to use the working free model `nvidia/z-ai/glm5` instead.

## Issue Identified
The initial update used `qwen/qwen3.6-plus:free` which was listed in the documentation as a free model, but this model was NOT tested and may not be available or free. The test results showed that the following models are actually working and free:
1. `nvidia/z-ai/glm5` - 744B MoE, excellent for agentic tasks
2. `google/gemini-3.1-flash-lite-preview` - Good for research and quick tasks
3. `nvidia/meta/llama-3.3-70b-instruct` - Best general purpose, multilingual

## Changes Made

### Primary Model Updates
1. **Metis agent**: Changed model from `opencode/qwen3.6-plus-free` to `nvidia/z-ai/glm5`
2. **Atlas agent**: Changed model from `opencode/qwen3.6-plus-free` to `nvidia/z-ai/glm5`
3. **Visual-engineering category**: Changed model from `opencode/qwen3.6-plus-free` to `nvidia/z-ai/glm5`

### Fallback Model Updates
Updated all fallback model references for the following agents/categories:
- Sisyphus
- Hephaestus
- Oracle
- Explore
- Prometheus
- Momus
- Librarian
- Multimodal-looker
- Atlas
- Sisyphus-junior
- Ultrabrain
- Artistry
- Quick
- Unspecified-low
- Unspecified-high
- Writing

## Reason for Update
The `opencode/qwen3.6-plus-free` model was unavailable with the error "Expecting value: line 1 column 1 (char 0)", which indicates that the model is no longer accessible through the OpenCode provider.

## Replacement Model
The replacement model `nvidia/z-ai/glm5` from NVIDIA Build provides excellent functionality with the following characteristics:
- 744B MoE (Mixture of Experts) architecture
- Excellent for agentic tasks and orchestration
- Strong reasoning capabilities
- Proven to work in test results

## Verification
The updated configuration has been verified to ensure:
1. All references to the unavailable model have been replaced
2. JSON syntax is valid
3. All agents and categories now use the working free model `nvidia/z-ai/glm5`
4. The configuration maintains the same functionality as before

## Affected Agents and Categories
The following agents and categories were affected by this update:
- Metis agent
- Atlas agent
- Visual-engineering category
- All agents with fallback models that included the unavailable model

## Files Updated
- `/home/trocha/projects/explorer/docs/oh-my-opencode-reference.json`

## Date
April 12, 2026

## Author
Hephaestus

## Note
This is a CORRECTED version of the initial update. The initial update incorrectly used `qwen/qwen3.6-plus:free` which may not be available or free. This version uses the tested and working `nvidia/z-ai/glm5` model instead.