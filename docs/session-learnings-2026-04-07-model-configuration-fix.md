# Session Learnings: Model Configuration Fix and Testing

**Date**: 2026-04-07  
**Session Type**: Model Configuration Verification and Correction  
**Duration**: ~30 minutes  

## Executive Summary

This session focused on testing and fixing model name discrepancies in the `oh-my-opencode.json` configuration file. All non-OpenAI models were tested, discrepancies were identified and corrected, and the working configuration was saved as a reference file.

## Problem Statement

The user requested:
1. Skip all OpenAI models
2. Test each non-OpenAI model mentioned in `~/.config/opencode/oh-my-opencode.json`
3. Verify all models work correctly
4. Fix any discrepancies found

## Key Discoveries

### 1. Model Name Discrepancies

**Critical Finding**: Model names in the configuration file didn't match the actual available models in opencode.

#### Discrepancies Found:

| Config Name | Actual Available Model | Issue |
|-------------|------------------------|-------|
| `z-ai/glm-5` | `nvidia/z-ai/glm5` | Missing provider prefix, wrong hyphen format |
| `nvidia/nemotron-3-nano-30b-a3b` | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | Missing nested provider path |
| `nvidia/nemotron‑3‑nano‑30b‑a3b` | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | Unicode hyphens instead of ASCII |

### 2. Provider Prefix Hierarchy

**Learning**: Models have specific provider prefixes that must be exact.

- `z-ai/glm-5` is provided by NVIDIA → correct name: `nvidia/z-ai/glm5`
- Some models have nested provider paths: `nvidia/nvidia/nemotron-3-nano-30b-a3b`
- Provider prefixes are not optional - they're part of the model identifier

### 3. Unicode vs ASCII Characters

**Issue Found**: Configuration contained unicode hyphens (`‑`, U+2011) instead of ASCII hyphens (`-`, U+002D).

**Impact**: 
- Unicode characters can cause silent failures
- May work in some contexts but fail in others
- Not visible in casual inspection

**Solution**: Always use ASCII hyphens in model names.

## Testing Methodology Evolution

### Initial Approach (Failed)

```bash
opencode --model "z-ai/glm-5" --prompt "Say 'Model working'"
```

**Result**: Timed out after 60 seconds with no output.

### Working Approach (Success)

```bash
timeout 45 opencode run --model "nvidia/z-ai/glm5" "Reply with exactly: 'Model working'"
```

**Result**: Successful response within 30-45 seconds.

### Key Differences:

1. Use `opencode run` instead of `opencode --model`
2. Add `timeout` command to prevent hanging
3. Use simple, direct prompts for testing
4. Allow 30-60 seconds for model response

## Configuration Validation Process

### Step-by-Step Process Developed:

1. **Extract all model references**
   ```bash
   grep -oE '"model": "[^"]*"' ~/.config/opencode/oh-my-opencode.json
   ```

2. **Cross-reference with available models**
   ```bash
   opencode models | grep -i "model-name"
   ```

3. **Validate JSON syntax after edits**
   ```bash
   python3 -m json.tool ~/.config/opencode/oh-my-opencode.json > /dev/null
   ```

4. **Verify file integrity**
   ```bash
   md5sum file1 file2
   ```

## Changes Made

### File: `~/.config/opencode/oh-my-opencode.json`

#### Change 1: Fixed `z-ai/glm-5` → `nvidia/z-ai/glm5`

**Locations**: 18 occurrences across multiple agents and categories

- `sisyphus.model`
- `hephaestus.fallback_models[1]`
- `oracle.fallback_models[0]`
- `explore.model`
- `prometheus.fallback_models[0]`
- `metis.fallback_models[0]`
- `momus.fallback_models[0]`
- `librarian.fallback_models[1]`
- `multimodal-looker.model`
- `atlas.fallback_models[0]`
- `sisyphus-junior.model`
- `ultrabrain.fallback_models[0]`
- `deep.fallback_models[1]`
- `artistry.model`
- `quick.model`
- `unspecified-low.model`
- `unspecified-high.model`

#### Change 2: Fixed `nvidia/nemotron-3-nano-30b-a3b` → `nvidia/nvidia/nemotron-3-nano-30b-a3b`

**Locations**: 1 occurrence
- `visual-engineering.fallback_models[0]`

#### Change 3: Fixed Unicode Hyphens

**Locations**: 2 occurrences
- `multimodal-looker.fallback_models[1]`
- `unspecified-high.fallback_models[2]`

## Test Results

### All Non-OpenAI Models Tested Successfully

| Model | Status | Response |
|-------|--------|----------|
| `nvidia/z-ai/glm5` | ✅ Working | "Model working" |
| `opencode/qwen3.6-plus-free` | ✅ Working | "Model working" |
| `nvidia/qwen/qwen3-coder-480b-a35b-instruct` | ✅ Working | "Model working" |
| `nvidia/stepfun-ai/step-3.5-flash` | ✅ Working | "Model working" |
| `google/gemini-3.1-flash-lite-preview` | ✅ Working | "Model working" |
| `nvidia/nvidia/nemotron-3-nano-30b-a3b` | ✅ Working | "Model working" |
| `nvidia/meta/llama-3.3-70b-instruct` | ✅ Working | "Model working" |
| `nvidia/meta/llama-3.2-11b-vision-instruct` | ✅ Working | "Model working" |

**Note**: OpenAI models (`openai/gpt-5.4`, `openai/gpt-5.3-codex`) were skipped per user request.

## Best Practices Established

### 1. Model Configuration

- ✅ Always verify model availability with `opencode models` before configuring
- ✅ Use exact model names from the available list
- ✅ Check for unicode characters that might cause issues
- ✅ Validate JSON syntax after all edits
- ✅ Use `replaceAll` parameter for batch replacements

### 2. Model Testing

- ✅ Use simple test prompts: "Reply with exactly: 'Model working'"
- ✅ Add timeout commands (45-60 seconds recommended)
- ✅ Test models in parallel for efficiency
- ✅ Verify responses match expectations

### 3. Documentation

- ✅ Save reference configurations after successful setups
- ✅ Use MD5 checksums to verify file integrity
- ✅ Document all changes with specific line numbers
- ✅ Create session learnings for future reference

### 4. Problem-Solving

- ✅ Ask for clarification when model naming seems ambiguous
- ✅ Cross-reference multiple sources before making changes
- ✅ Test fixes immediately after implementation
- ✅ Validate changes don't break existing functionality

## Tools and Commands Reference

### Useful Commands Discovered

```bash
# List all available models
opencode models

# Test a specific model
timeout 45 opencode run --model "provider/model-name" "test prompt"

# Extract all model references from config
grep -oE '"model": "[^"]*"' config.json | sort -u

# Validate JSON syntax
python3 -m json.tool config.json > /dev/null

# Compare file integrity
md5sum file1 file2

# Find specific model in available list
opencode models | grep -i "model-name"
```

## Parallel Execution Efficiency

**Performance Gain**: Testing 8 models in parallel vs sequential

- **Parallel approach**: ~45 seconds total (all tests run simultaneously)
- **Sequential approach**: ~360 seconds (45s × 8 models)
- **Time saved**: ~5.25 minutes (87.5% reduction)

**Implementation**:
```bash
# All 8 tests launched simultaneously
timeout 45 opencode run --model "model1" "prompt" &
timeout 45 opencode run --model "model2" "prompt" &
# ... (8 parallel processes)
```

## User Interaction Insights

### Critical Clarification

**Initial Assumption**: Thought `z-ai/glm-5` was from openrouter provider.

**User Correction**: "the provider of z-ai/glm-5 is nvidia"

**Impact**: This clarification was crucial for finding the correct model name (`nvidia/z-ai/glm5`).

**Lesson**: Always verify assumptions with the user when provider information is ambiguous.

## Actionable Takeaways for Future Sessions

### Immediate Actions

1. **Before configuring any model**: Run `opencode models` to verify availability
2. **When model names seem wrong**: Check provider prefixes and nested paths
3. **After editing config**: Always validate JSON and test at least one model
4. **When saving references**: Include MD5 checksums for verification

### Long-term Improvements

1. **Create a model validation script** that:
   - Extracts all model references from config
   - Cross-references with `opencode models`
   - Reports discrepancies automatically

2. **Implement pre-commit hooks** that:
   - Validate JSON syntax
   - Check for unicode characters
   - Verify model names against available list

3. **Build a model testing suite** that:
   - Tests all configured models in parallel
   - Reports response times and success rates
   - Generates test reports automatically

## Files Modified

### Configuration File
- **Path**: `~/.config/opencode/oh-my-opencode.json`
- **Changes**: 21 model name corrections
- **Validation**: JSON syntax valid, all models tested

### Reference File Created
- **Path**: `/home/trocha/projects/explorer/docs/oh-my-opencode-reference.json`
- **Purpose**: Working configuration backup
- **Verification**: MD5 checksums match original

## Metrics

- **Models tested**: 8 non-OpenAI models
- **Discrepancies fixed**: 3 types (21 total occurrences)
- **Test success rate**: 100% (8/8 models working)
- **Time to completion**: ~30 minutes
- **Files modified**: 1 config file
- **Documentation created**: 2 files (reference + learnings)

## Conclusion

This session successfully identified and fixed all model name discrepancies in the configuration file. The systematic approach of:

1. Extracting all model references
2. Cross-referencing with available models
3. Making precise corrections
4. Validating changes
5. Testing all models
6. Documenting results

...ensured a complete and reliable fix. The working configuration is now saved as a reference, and all learnings are documented for future sessions.

## Next Steps

1. Monitor model performance over time
2. Update configuration when new models become available
3. Consider automating model validation in CI/CD pipeline
4. Review and update fallback chains based on actual performance data

---

**Session Completed**: 2026-04-07  
**Status**: ✅ All objectives achieved  
**Documentation**: Complete
