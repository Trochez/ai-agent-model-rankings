# Deep Research Report: Best Free Alternative to `google/lyria-3-pro-preview:free`

**Research Date**: April 6, 2026  
**Task**: Find the best free vision/multimodal model alternative across OpenCode, OpenRouter, NVIDIA Build, and OpenAI  
**Status**: ✅ COMPLETE

---

## 🚨 Critical Discovery

**`google/lyria-3-pro-preview` is NOT a vision model** — it's a **music generation model**!

- **Lyria 3** generates audio/music from text or image prompts
- It was **never suitable** for image understanding tasks
- The `:free` suffix doesn't exist for this model (paid only: $0.08/song)
- The `ProviderModelNotFoundError` was correct — this model ID is invalid

**This explains why the test failed**: You were trying to use a music generation model for visual understanding tasks.

---

## 📊 Research Methodology

### Sources Investigated
1. ✅ **OpenRouter Free Models** - Comprehensive catalog of 28+ free models
2. ✅ **OpenCode Models** - 75+ providers including OpenRouter, NVIDIA, Google
3. ✅ **NVIDIA Build** - Free GPU-optimized inference endpoints
4. ✅ **Google Gemini/Gemma** - Free tier vision models
5. ✅ **OpenAI** - Free tier availability (limited)

### Research Approach
- **Phase 1**: Broad exploration of free model catalogs
- **Phase 2**: Deep dive into vision/multimodal capabilities
- **Phase 3**: Validation of model availability and pricing
- **Phase 4**: Cross-reference with OpenCode CLI availability

---

## 🏆 Top Recommendations

### **#1 Best Overall: `qwen/qwen3.6-plus:free`**

**Why it's the best choice:**
- ✅ **1M context window** (largest available)
- ✅ **Explicit "Vision" capability** listed
- ✅ **Tools support** for agentic workflows
- ✅ **State-of-the-art multimodal** performance
- ✅ **Released April 2, 2026** (very recent)
- ✅ **4.9T tokens processed** (well-tested)

**Model ID for oh-my-opencode.json:**
```json
{
  "model": "openrouter/qwen/qwen3.6-plus:free"
}
```

**Evidence**: [OpenRouter Qwen3.6 Plus](https://openrouter.ai/qwen/qwen3.6-plus:free)

---

### **#2 Best Dedicated VL: `nvidia/nemotron-nano-12b-v2-vl:free`**

**Why it's excellent:**
- ✅ **Purpose-built vision-language model** (VL in name)
- ✅ **Specialized for OCR, charts, document intelligence**
- ✅ **128K context window**
- ✅ **Hybrid Transformer-Mamba architecture**
- ✅ **Leading results on OCRBench v2**
- ✅ **Efficient Video Sampling (EVS)** for long videos

**Model ID for oh-my-opencode.json:**
```json
{
  "model": "openrouter/nvidia/nemotron-nano-12b-v2-vl:free"
}
```

**Evidence**: [OpenRouter Nemotron VL](https://openrouter.ai/nvidia/nemotron-nano-12b-v2-vl:free)

---

### **#3 Best Google Model: `google/gemma-3-27b-it:free`**

**Why it's good:**
- ✅ **Strongest free Google vision model**
- ✅ **Vision-language input** (images + text → text)
- ✅ **140+ languages** supported
- ✅ **Function calling** and structured outputs
- ✅ **104M+ tokens usage** (well-tested)
- ✅ **33K context window**

**Model ID for oh-my-opencode.json:**
```json
{
  "model": "openrouter/google/gemma-3-27b-it:free"
}
```

**Evidence**: [OpenRouter Gemma 3 27B](https://openrouter.ai/google/gemma-3-27b-it:free)

---

## 📋 Complete Free Vision Models Catalog

### OpenRouter Free Vision Models (April 2026)

| Rank | Model ID | Context | Capabilities | Best For |
|------|----------|---------|--------------|----------|
| **1** | `qwen/qwen3.6-plus:free` | **1,000K** | Vision, Tools | **Best overall** - SOTA multimodal |
| **2** | `nvidia/nemotron-nano-12b-v2-vl:free` | 128K | Vision, Tools | **Best dedicated VL** - OCR, charts |
| **3** | `google/gemma-3-27b-it:free` | 33K | Vision | **Best Google** - strong general-purpose |
| **4** | `google/gemma-3-12b-it:free` | 33K | Vision | Balanced quality/speed |
| **5** | `google/gemma-3-4b-it:free` | 33K | Vision | Lightweight vision tasks |
| **6** | `google/gemma-3n-e4b-it:free` | 8K | Multimodal | Mobile/low-resource |
| **7** | `google/gemma-3n-e2b-it:free` | 8K | Multimodal | Minimal resource usage |
| **8** | `openrouter/free` | 200K | Vision, Tools | **Auto-router** - smart selection |

### NVIDIA Build Free Vision Models

| Model ID | Context | Capabilities | Notes |
|----------|---------|--------------|-------|
| `nvidia/google/gemma-3-27b-it` | Varies | Vision | Same as OpenRouter, GPU-optimized |
| `nvidia/google/gemma-3-12b-it` | Varies | Vision | GPU-optimized inference |
| `nvidia/google/gemma-3n-e4b-it` | Varies | Multimodal | GPU-optimized |

**Note**: NVIDIA Build offers free GPU-optimized inference for many models. Use `nvidia/` prefix instead of `openrouter/`.

### OpenCode Free Vision Models

Available through OpenCode CLI with various providers:
- `opencode/nemotron-3-super-free` (NVIDIA Nemotron via OpenCode)
- All OpenRouter free models accessible via `openrouter/` prefix
- All NVIDIA Build models accessible via `nvidia/` prefix

---

## 🔍 Detailed Model Analysis

### 1. Qwen3.6 Plus (free) - Top Recommendation

**Architecture**: Hybrid MoE (Mixture of Experts) with linear attention  
**Parameters**: MoE (efficient routing)  
**Context**: 1,000,000 tokens  
**Capabilities**: Vision, Tools, Function Calling  
**Performance**: 78.8 on SWE-bench Verified  

**Strengths:**
- Largest context window among free models
- State-of-the-art multimodal understanding
- Excellent for complex reasoning tasks
- Strong agentic coding capabilities

**Best Use Cases:**
- Document analysis with images
- Multimodal RAG systems
- Complex visual reasoning
- Long-context image understanding

**Rate Limits**: 20 req/min, 200 req/day (OpenRouter free tier)

---

### 2. NVIDIA Nemotron Nano 12B VL - Best Dedicated VL

**Architecture**: Hybrid Transformer-Mamba  
**Parameters**: 12B  
**Context**: 128,000 tokens  
**Capabilities**: Vision, Tools, OCR, Chart Reasoning  

**Strengths:**
- Purpose-built for vision-language tasks
- Excellent OCR and document intelligence
- Efficient Video Sampling (EVS) for videos
- Leading results on OCRBench v2, MMMU, MathVista

**Best Use Cases:**
- OCR and text extraction from images
- Chart and diagram understanding
- Document intelligence
- Video analysis

**Special Features:**
- Handles multi-image documents
- Efficient for long-form videos
- Open weights and training data available

---

### 3. Google Gemma 3 27B - Best Google Option

**Architecture**: Transformer  
**Parameters**: 27B  
**Context**: 33,000 tokens  
**Capabilities**: Vision-language input, Function Calling  

**Strengths:**
- Strongest free Google vision model
- 140+ language support
- Well-tested (104M+ tokens usage)
- Function calling support

**Best Use Cases:**
- General-purpose image understanding
- Multilingual vision tasks
- Structured output generation

---

## 🚫 Models to Avoid

| Model ID | Issue | Reason |
|----------|-------|--------|
| `google/lyria-3-pro-preview:free` | ❌ **Doesn't exist** | Lyria is music generation, not vision |
| `google/lyria-3-clip-preview:free` | ❌ **Doesn't exist** | Same - music generation |
| `qwen/qwen2.5-vl-3b-instruct:free` | ❌ **No free tier** | Only paid version exists |
| `google/gemini-3.1-flash-preview` | ⚠️ **Wrong ID** | Should be `gemini-3.1-flash-lite-preview` |

---

## 💡 Configuration Recommendations

### For oh-my-opencode.json

**Option 1: Best Overall (Recommended)**
```json
{
  "multimodal-looker": {
    "model": "openrouter/qwen/qwen3.6-plus:free",
    "variant": "high",
    "reasoningEffort": "high",
    "temperature": 0.3,
    "maxTokens": 16384,
    "fallback_models": [
      "openrouter/nvidia/nemotron-nano-12b-v2-vl:free",
      "openrouter/google/gemma-3-27b-it:free"
    ]
  }
}
```

**Option 2: Dedicated VL Focus**
```json
{
  "multimodal-looker": {
    "model": "openrouter/nvidia/nemotron-nano-12b-v2-vl:free",
    "variant": "medium",
    "reasoningEffort": "medium",
    "temperature": 0.3,
    "maxTokens": 16384,
    "fallback_models": [
      "openrouter/qwen/qwen3.6-plus:free",
      "openrouter/google/gemma-3-27b-it:free"
    ]
  }
}
```

**Option 3: Auto-Router (Easiest)**
```json
{
  "multimodal-looker": {
    "model": "openrouter/openrouter/free",
    "variant": "medium",
    "reasoningEffort": "medium",
    "temperature": 0.3,
    "maxTokens": 16384
  }
}
```

---

## 📈 Performance Comparison

### Context Window Size
```
qwen/qwen3.6-plus:free          1,000K  ████████████████████ (largest)
nvidia/nemotron-nano-12b-vl:free  128K  ██▌
google/gemma-3-27b-it:free         33K  ▌
openrouter/free                   200K  ████
```

### Multimodal Capability Score (Estimated)
```
qwen/qwen3.6-plus:free           95/100  ███████████████████▌
nvidia/nemotron-nano-12b-vl:free 92/100  ███████████████████▏
google/gemma-3-27b-it:free       85/100  █████████████████▏
```

### Availability & Stability
```
qwen/qwen3.6-plus:free           ✅✅✅✅✅  (4.9T tokens processed)
nvidia/nemotron-nano-12b-vl:free ✅✅✅✅   (12.7B tokens)
google/gemma-3-27b-it:free       ✅✅✅✅✅  (104M+ tokens)
```

---

## 🎯 Decision Matrix

| Criteria | Qwen3.6+ | Nemotron VL | Gemma 3 27B |
|----------|----------|-------------|-------------|
| **Context Length** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **Vision Quality** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **OCR/Charts** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Speed** | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Availability** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Agentic Tools** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

---

## 🔧 Implementation Steps

### Step 1: Update Configuration
Replace the invalid model ID in `oh-my-opencode.json`:

**Before:**
```json
"model": "openrouter/google/lyria-3-pro-preview:free"
```

**After (Recommended):**
```json
"model": "openrouter/qwen/qwen3.6-plus:free"
```

### Step 2: Test the New Model
```bash
/home/trocha/.opencode/bin/opencode run -m "openrouter/qwen/qwen3.6-plus:free" \
  "Describe what you see in this image: [image URL or path]"
```

### Step 3: Validate Fallback Chain
Ensure fallback models are also valid:
```json
"fallback_models": [
  "openrouter/nvidia/nemotron-nano-12b-v2-vl:free",
  "openrouter/google/gemma-3-27b-it:free"
]
```

---

## 📚 Evidence Sources

1. **OpenRouter Free Models Collection**: https://openrouter.ai/collections/free-models
2. **OpenRouter Vision Models**: https://openrouter.ai/collections/vision-models
3. **Qwen3.6 Plus (free)**: https://openrouter.ai/qwen/qwen3.6-plus:free
4. **NVIDIA Nemotron VL**: https://openrouter.ai/nvidia/nemotron-nano-12b-v2-vl:free
5. **Google Gemma 3 27B**: https://openrouter.ai/google/gemma-3-27b-it:free
6. **NVIDIA Build Vision Models**: https://build.nvidia.com/explore/vision
7. **OpenCode Models List**: CLI output from `/home/trocha/.opencode/bin/opencode models`

---

## 🎓 Key Learnings

### What We Discovered
1. **Lyria is for music, not vision** - Critical misunderstanding of model purpose
2. **Free vision models are abundant** - 8+ quality options available
3. **Qwen3.6+ leads in context** - 1M tokens vs 128K for others
4. **NVIDIA VL excels at OCR** - Purpose-built for document intelligence
5. **OpenRouter free tier is generous** - 20 req/min, 200 req/day

### Best Practices
- ✅ Always verify model capabilities before configuration
- ✅ Check if `:free` suffix exists for the model
- ✅ Use fallback chains for reliability
- ✅ Test models with actual vision tasks
- ✅ Monitor rate limits on free tiers

---

## 🏁 Final Recommendation

**Use `qwen/qwen3.6-plus:free` as the primary replacement for `google/lyria-3-pro-preview:free`**

**Rationale:**
1. ✅ Largest context window (1M tokens)
2. ✅ Explicit vision capability
3. ✅ State-of-the-art multimodal performance
4. ✅ Well-tested (4.9T tokens processed)
5. ✅ Tools support for agentic workflows
6. ✅ Recent release (April 2, 2026)

**Alternative for specialized OCR/document tasks:**
- Use `nvidia/nemotron-nano-12b-v2-vl:free` for OCR, charts, and document intelligence

---

**Report Generated**: April 6, 2026  
**Research Method**: Deep Research Skill (Multi-angle systematic investigation)  
**Sources**: OpenRouter, OpenCode, NVIDIA Build, Google AI  
**Status**: ✅ COMPLETE
