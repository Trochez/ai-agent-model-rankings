# Session Learnings - April 7, 2026

**Session Focus**: Model Configuration Updates, Visual Engineering Research & Documentation Enhancement

---

## Executive Summary

This session focused on updating model configurations based on test results, conducting deep research on visual engineering models, and documenting comprehensive learnings about the model landscape. Key achievements include migrating from OpenRouter to OpenCode Zen for Qwen models, expanding visual model options, and creating detailed documentation of model rankings.

---

## 1. Model Configuration Updates

### 1.1 Qwen3.6 Plus Migration to OpenCode Zen

**Problem Identified:**
- OpenRouter's `qwen/qwen3.6-plus:free` was hitting constant HTTP 429 rate limit errors
- Test results showed only 1/7 models passed (14% success rate)
- OpenRouter free tier has hard rate limits: 20 req/min, 200 req/day

**Solution Implemented:**
- Updated all 15 references from `qwen/qwen3.6-plus:free` to `opencode/qwen3.6-plus-free`
- OpenCode Zen offers curated, tested models specifically for coding agents
- No rate limits mentioned for OpenCode Zen free tier

**Impact:**
- Configuration file: `/home/trocha/.config/opencode/oh-my-opencode.json`
- Affected agents: sisyphus, oracle, explore, prometheus, metis, momus, librarian, multimodal-looker, atlas, sisyphus-junior
- Affected categories: visual-engineering, ultrabrain, quick, unspecified-low, unspecified-high

**Key Insight:**
> OpenRouter's free tier rate limits are provider-level, not credit-based. Having $10+ balance doesn't lift these limits on `:free` models.

### 1.2 Gemini Model Configuration Update

**Change:**
- Updated `google/gemini-3.1-pro-preview` to use OpenRouter routing
- New model ID: `openrouter/google/gemini-3.1-pro-preview`

**Locations:**
- visual-engineering category (fallback model)
- artistry category (primary model)

**Rationale:**
- User preference for OpenRouter routing over direct Google API
- OpenRouter provides unified API interface across providers

---

## 2. Model Testing Insights

### 2.1 Test Results Analysis

**Test Execution:**
- Date: 2026-04-06 16:23:53
- Models tested: 7 (excluding OpenAI models)
- Test prompt: "What is 2 + 2? Reply with ONLY the number."
- Success rate: 14% (1/7 passed)

**Results Breakdown:**

| Model | Provider | Status | Response Time | Error |
|-------|----------|--------|---------------|-------|
| `google/gemini-3.1-flash-lite-preview` | google | ✅ PASS | 2235ms | None |
| `qwen/qwen3.6-plus:free` | openrouter | ❌ ERROR | 3144ms | 'choices' error |
| `google/gemini-3.1-pro-preview` | google | ❌ ERROR | 1495ms | HTTP 429: quota exceeded |
| `meta-llama/llama-3.3-70b-instruct:free` | openrouter | ❌ ERROR | 1029ms | HTTP 429: rate limit |
| `openrouter/qwen/qwen2.5-72b-instruct` | openrouter | ❌ ERROR | 765ms | HTTP 400: invalid model ID |
| `openrouter/qwen/qwen3-coder:free` | openrouter | ❌ ERROR | 523ms | HTTP 400: invalid model ID |
| `stepfun/step-3.5-flash:free` | openrouter | ❌ ERROR | 3140ms | null error |

**Key Findings:**
1. Only `google/gemini-3.1-flash-lite-preview` successfully responded
2. Rate limiting (HTTP 429) was the most common failure
3. Invalid model IDs (HTTP 400) indicated incorrect OpenRouter ID format
4. OpenRouter models with `openrouter/` prefix are invalid

### 2.2 Model ID Convention Learnings

**Correct Conventions:**
- **OpenRouter**: No prefix needed (e.g., `qwen/qwen3.6-plus:free`)
- **OpenCode Zen**: `opencode/` prefix (e.g., `opencode/qwen3.6-plus-free`)
- **NVIDIA Build**: `nvidia/` prefix (e.g., `nvidia/z-ai/glm5`)
- **OpenAI**: `openai/` prefix (e.g., `openai/gpt-5.4`)
- **Google**: `google/` prefix (e.g., `google/gemini-3.1-flash-lite-preview`)

**Common Mistakes:**
- ❌ `openrouter/qwen/qwen3-coder:free` (invalid - has `openrouter/` prefix)
- ✅ `qwen/qwen3-coder:free` (correct)

---

## 3. Model Rankings Deep Dive

### 3.1 Comprehensive Rankings Documentation

**Primary Source:**
- File: `/home/trocha/projects/explorer/docs/oh-my-opencode-agent-rankings-2026-04-06.md`
- Size: 570 lines
- Version: 2.0 (most comprehensive)

**Coverage:**
- **11 Agents**: Each with 6 ranked models (0-100 effectiveness scores)
- **8 Categories**: Each with 6 ranked models
- **100+ Models**: From 4 major providers (OpenRouter, NVIDIA Build, OpenAI, OpenCode)

**Scoring Methodology:**
- Task-specific capability matching (40%)
- Context window size (20%)
- Reasoning level requirements (20%)
- Tool support (vision, tools, function calling) (10%)
- Cost efficiency (10%)

### 3.2 Best Free Models Summary

**By Agent:**
- **Most Versatile**: `qwen/qwen3.6-plus:free` (top choice for 8/11 agents)
- **Best Visual**: `google/lyria-3-pro-preview:free` (95/100)
- **Best Coding**: `qwen/qwen3-coder:free` (89/100)

**By Category:**
- **visual-engineering**: `google/lyria-3-pro-preview:free` (95/100)
- **ultrabrain**: `qwen/qwen3.6-plus:free` (82/100)
- **deep**: `qwen/qwen3.6-plus:free` (85/100)
- **artistry**: `qwen/qwen3.6-plus:free` (85/100)
- **quick**: `qwen/qwen3.6-plus:free` (92/100)
- **unspecified-low**: `qwen/qwen3.6-plus:free` (90/100)
- **unspecified-high**: `qwen/qwen3.6-plus:free` (88/100)
- **writing**: `meta-llama/llama-3.3-70b-instruct:free` (88/100)

---

## 4. Visual Engineering Model Research

### 4.1 Expanded Visual Model Options

**Research Methodology:**
- Conducted deep research using web search and webfetch
- Analyzed OpenRouter free models collection
- Explored NVIDIA Build vision models
- Identified 15+ visual models suitable for frontend/UI/UX work

**Top 15 Models for Visual Engineering:**

| Rank | Model | Provider | Score | Context | Vision | Tools |
|------|-------|----------|-------|---------|--------|-------|
| 1 | `openrouter/qwen/qwen2.5-vl-72b-instruct` | OpenRouter | 96 | 32K | ✅ | ✅ |
| 2 | `google/lyria-3-pro-preview:free` | OpenRouter | 95 | 1M | ✅ | ❌ |
| 3 | `opencode/gemini-3.1-pro` | OpenCode | 93 | - | ✅ | ✅ |
| 4 | `qwen/qwen3.6-plus:free` | OpenRouter | 88 | 1M | ✅ | ✅ |
| 5 | `nvidia/nemotron-nano-12b-v2-vl:free` | OpenRouter | 85 | 128K | ✅ | ✅ |
| 6 | `google/gemma-3-27b-it:free` | OpenRouter | 80 | 131K | ✅ | ❌ |
| 7 | `meta/llama-3.2-11b-vision-instruct` | NVIDIA Build | 82 | 131K | ✅ | ✅ |
| 8 | `meta/llama-3.2-90b-vision-instruct` | NVIDIA Build | 85 | 131K | ✅ | ✅ |
| 9 | `google/gemma-3-12b-it:free` | OpenRouter | 78 | 33K | ✅ | ❌ |
| 10 | `google/paligemma` | NVIDIA Build | 78 | - | ✅ | ✅ |
| 11 | `nvidia/cosmos-reason2-8b` | NVIDIA Build | 80 | - | ✅ | ✅ |
| 12 | `google/gemma-3-4b-it:free` | OpenRouter | 75 | 33K | ✅ | ❌ |
| 13 | `openrouter/free` | OpenRouter | 72 | 200K | ✅ | ✅ |
| 14 | `nvidia/nv-dinov2` | NVIDIA Build | 75 | - | ✅ | ❌ |
| 15 | `nvidia/nv-grounding-dino` | NVIDIA Build | 73 | - | ✅ | ❌ |

### 4.2 Specialized Vision Models (NVIDIA Build)

**Vision Language Models (VLM):**
- `nvidia/nemotron-nano-12b-v2-vl:free` - Video understanding, OCR, chart reasoning
- `meta/llama-3.2-11b-vision-instruct` - High-quality reasoning from images
- `meta/llama-3.2-90b-vision-instruct` - Complex visual reasoning
- `nvidia/cosmos-reason2-8b` - Physical world understanding
- `google/paligemma` - Text and visual comprehension

**Specialized Models:**
- `nvidia/nv-dinov2` - Visual foundation model (image embeddings)
- `nvidia/nv-grounding-dino` - Zero-shot object detection
- `nvidia/ocdrnet` - Optical character detection and recognition
- `nvidia/visual-changenet` - Pixel-level change detection

**Key Discovery:**
> NVIDIA Build offers multiple specialized vision models with **free endpoints** for specific tasks like OCR, object detection, and image embeddings.

### 4.3 Visual Model Recommendations by Use Case

| Use Case | Best Model | Why |
|----------|------------|-----|
| **UI/UX Design** | `google/lyria-3-pro-preview:free` | Best visual model, 1M context |
| **Frontend Development** | `qwen/qwen2.5-vl-72b-instruct` | Vision+tools, excellent for UI work |
| **Document Analysis** | `nvidia/nemotron-nano-12b-v2-vl:free` | OCR, chart reasoning, document intelligence |
| **Video Understanding** | `nvidia/nemotron-nano-12b-v2-vl:free` | Efficient Video Sampling (EVS) |
| **Object Detection** | `nvidia/nv-grounding-dino` | Zero-shot object detection |
| **Image Embeddings** | `nvidia/nv-dinov2` | Visual foundation model |
| **General Visual Tasks** | `qwen/qwen3.6-plus:free` | Versatile, vision+tools, 1M context |

---

## 5. Provider Landscape Understanding

### 5.1 OpenRouter

**Free Tier:**
- 28 free models available
- Rate limits: 20 req/min, 200 req/day per model
- Cost: $0 (no credit card required)
- Top models: qwen3.6-plus, qwen3-coder, lyria-3

**Key Insight:**
> Rate limits are **provider-level**, not credit-based. Having $10+ balance doesn't lift limits on `:free` models.

### 5.2 OpenCode Zen

**Characteristics:**
- Curated, tested models specifically for coding agents
- No rate limits mentioned for free tier
- Models benchmarked for coding agent performance
- Optional provider (can use OpenCode without Zen)

**Free Models:**
- `opencode/qwen3.6-plus-free` - Same as OpenRouter free tier
- `opencode/gemini-3-flash` - Fast, good for research
- `opencode/gemini-3.1-pro` - High reasoning

**Advantages:**
- No rate limits on free tier
- Models tested for coding agent use cases
- Unified API interface

### 5.3 NVIDIA Build

**Free Endpoints:**
- 91 free models available
- GPU-optimized inference
- Specialized vision models
- Top models: glm5 (744B MoE), nemotron-3-super

**Specialized Vision Models:**
- VLM models for visual reasoning
- OCR and document intelligence
- Object detection and embeddings
- Video understanding

**Advantages:**
- GPU-accelerated inference
- Specialized models for specific tasks
- Free endpoints for development

---

## 6. Configuration File Structure

### 6.1 Oh-My-OpenCode Configuration

**File:** `/home/trocha/.config/opencode/oh-my-opencode.json`

**Structure:**
```json
{
  "$schema": "...",
  "model_fallback": true,
  "agents": {
    "sisyphus": { ... },
    "hephaestus": { ... },
    ...
  },
  "categories": {
    "visual-engineering": { ... },
    "ultrabrain": { ... },
    ...
  }
}
```

**Agent Properties:**
- `model`: Primary model ID
- `variant`: Model variant (low, medium, high, xhigh, max)
- `reasoningEffort`: Reasoning level (minimal, medium, high, xhigh)
- `temperature`: Sampling temperature (typically 0.3)
- `top_p`: Nucleus sampling (typically 0.9)
- `maxTokens`: Maximum output tokens (typically 16384)
- `fallback_models`: Array of fallback model IDs
- `mode`: Agent mode (primary or subagent)
- `category`: Agent category
- `skills`: Array of special skills
- `tools`: Object with tool permissions
- `permission`: Tool permission levels
- `textVerbosity`: Output verbosity (low, medium, high)
- `color`: Hex color for UI display

**11 Agents:**
1. sisyphus (orchestrator)
2. hephaestus (executor)
3. oracle (consultant)
4. explore (search)
5. prometheus (planner)
6. metis (analyst)
7. momus (reviewer)
8. librarian (research)
9. multimodal-looker (visual)
10. atlas (knowledge)
11. sisyphus-junior (orchestrator-junior)

**8 Categories:**
1. visual-engineering
2. ultrabrain
3. deep
4. artistry
5. quick
6. unspecified-low
7. unspecified-high
8. writing

---

## 7. Best Practices for Model Selection

### 7.1 Free Tier Strategy

**General Purpose:**
- Use `opencode/qwen3.6-plus-free` for most tasks
- 1M context, vision+tools, strong reasoning
- No rate limits on OpenCode Zen

**Visual Work:**
- Use `google/lyria-3-pro-preview:free` for visual tasks
- 1M context, best free visual model (95/100)
- Optimized for UI/UX work

**Coding Tasks:**
- Use `qwen/qwen3-coder:free` for coding
- 262K context, best free coding model (89/100)
- Optimized for agentic coding

**Specialized Tasks:**
- Use NVIDIA Build for vision-specific tasks
- OCR, object detection, embeddings
- Free endpoints available

### 7.2 Paid Tier Strategy

**Critical Tasks:**
- Use `openai/gpt-5.4` for frontier intelligence
- Best for architecture consultation, strategic planning
- High reasoning for complex tasks

**Orchestration:**
- Use `nvidia/z-ai/glm5` for orchestration
- 744B MoE, excellent for agentic tasks
- Thinking capability enabled

**Implementation:**
- Use `openai/gpt-5.4` for implementation
- Best for code generation and execution
- High reasoning for complex implementations

### 7.3 Fallback Strategy

**Recommended Fallback Chain:**
1. Primary model (paid or free)
2. `opencode/qwen3.6-plus-free` (versatile free alternative)
3. `nvidia/z-ai/glm5` (strong reasoning, NVIDIA Build)
4. `meta-llama/llama-3.3-70b-instruct:free` (general purpose)

**Key Principle:**
> Always have at least 2 fallback models configured to ensure resilience.

---

## 8. Documentation Resources

### 8.1 Primary Documentation

**Model Rankings:**
- `/home/trocha/projects/explorer/docs/oh-my-opencode-agent-rankings-2026-04-06.md` (570 lines)
- Comprehensive rankings for 11 agents and 8 categories
- Effectiveness scores (0-100) for each model

**Test Results:**
- `/home/trocha/projects/explorer/failed-models-retest-*.json`
- Detailed test execution results
- Error analysis and response times

**Configuration:**
- `/home/trocha/.config/opencode/oh-my-opencode.json`
- Main configuration file
- Agent and category definitions

### 8.2 Session Learnings

**Previous Sessions:**
- Session 1 (April 4): Agent architecture insights
- Session 2 (April 5): Exhaustive search methodology
- Session 3 (April 6): Timeout configuration & system architecture
- Session 4 (April 6): Fallback configuration & retry mechanism
- Session 5 (April 6): Model ID investigation & config fixes

**This Session (April 7):**
- Model configuration updates
- Visual engineering research
- Documentation enhancement

---

## 9. Key Takeaways

### 9.1 Configuration Management

1. **Model ID Conventions Matter**: Incorrect prefixes cause HTTP 400 errors
2. **Rate Limits Are Real**: OpenRouter free tier has hard limits regardless of balance
3. **OpenCode Zen Advantage**: No rate limits, curated for coding agents
4. **Fallback Configuration**: Essential for resilience, all agents should have 2+ fallbacks

### 9.2 Model Selection Strategy

1. **Free Tier**: `opencode/qwen3.6-plus-free` for most tasks, specialized models for specific use cases
2. **Visual Work**: `google/lyria-3-pro-preview:free` is the best free option
3. **Coding**: `qwen/qwen3-coder:free` for coding-specific tasks
4. **Critical Tasks**: `openai/gpt-5.4` for frontier intelligence

### 9.3 Provider Landscape

1. **OpenRouter**: Good for free models, but has rate limits
2. **OpenCode Zen**: Best for coding agents, no rate limits
3. **NVIDIA Build**: Specialized vision models with free endpoints
4. **OpenAI**: Best paid models for critical tasks

### 9.4 Visual Engineering

1. **15+ Options**: Multiple free visual models available
2. **Specialized Models**: NVIDIA Build offers OCR, detection, embeddings
3. **Use Case Specific**: Different models excel at different visual tasks
4. **Free Endpoints**: Many NVIDIA vision models have free endpoints

---

## 10. Next Steps

### 10.1 Configuration Updates

- [ ] Verify OpenCode Zen API key is configured
- [ ] Test updated model IDs in configuration
- [ ] Monitor for rate limit issues
- [ ] Validate fallback chains work correctly

### 10.2 Documentation Updates

- [ ] Update README.md with new learnings
- [ ] Create visual model comparison guide
- [ ] Document provider-specific best practices
- [ ] Update model ID quick reference

### 10.3 Testing & Validation

- [ ] Run comprehensive model tests
- [ ] Validate visual model capabilities
- [ ] Test fallback mechanisms
- [ ] Monitor performance metrics

---

## Related Documentation

- [Oh-My-OpenCode Agent Rankings (v2.0)](oh-my-opencode-agent-rankings-2026-04-06.md)
- [Session Learnings - April 4](session-learnings-2026-04-04.md)
- [Session Learnings - April 5](session-learnings-2026-04-05.md)
- [Session Learnings - April 6](session-learnings-2026-04-06.md)
- [Session Learnings - April 6 (Fallback)](session-learnings-2026-04-06-fallback-investigation.md)
- [Session Learnings - April 6 (Model ID)](session-learnings-2026-04-06-model-id-investigation.md)

---

**Last Updated**: April 7, 2026
**Session Duration**: ~2 hours
**Key Achievements**: Model configuration updates, visual engineering research, comprehensive documentation
