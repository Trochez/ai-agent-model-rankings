# vLLM Flags Addition to Global Configuration

**Date**: April 6, 2026
**File**: `/home/trocha/.config/opencode/oh-my-opencode.json`

---

## Changes Made

Added vLLM server configuration flags to the global configuration file.

### Configuration Added

```json
"providerOptions": {
  "enable-auto-tool-choice": true,
  "tool-call-parser": "auto"
}

**Note**: The `tool-call-parser` should be set to `"auto"` for models like GLM5 that don't have a specific parser version. vLLM will auto-detect the appropriate parser.
```

### Location

- **Line 4-7**: Added `providerOptions` block at the top level of the configuration
- **Position**: After `model_fallback`, before `agents`

---

## Purpose

These flags enable automatic tool calling in vLLM:

1. **`enable-auto-tool-choice`**: Enables automatic tool selection when the model is asked to use tools
2. **`tool-call-parser`**: Specifies the parser to use for tool calls
   - Set to `"auto"` for automatic detection
   - Other options: `"mistral"`, `"hermes"`, `"internlm"`, `"llama3"`, `"qwen2"`

---

## Validation

✅ **JSON syntax validated** - Configuration file is valid JSON
✅ **Schema compliant** - `providerOptions` is a valid field in the schema
✅ **No breaking changes** - Existing configuration preserved

---

## Impact

These settings will:
1. Enable automatic tool calling for all agents using vLLM backends
2. Allow models to automatically select and use tools when appropriate
3. Improve tool integration without manual configuration per agent

---

## Related Documentation

- [vLLM Tool Calling Documentation](https://docs.vllm.ai/en/latest/features/tool_calling.html)
- [oh-my-opencode Schema](https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/dev/assets/oh-my-opencode.schema.json)

---

## Testing Recommendation

After these changes:
1. Restart OpenCode to load new configuration
2. Test tool calling with agents that use vLLM models
3. Verify automatic tool selection works as expected
4. Monitor for any tool calling errors

---

## Last Updated

April 6, 2026
