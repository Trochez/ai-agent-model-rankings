# Session Learnings - April 6, 2026 (Session 2)

**Session:** Model ID Investigation & Configuration Fix
**Agent:** Sisyphus (qwen/qwen3.6-plus:free)
**Duration:** ~30 minutes
**Focus:** Failed model re-testing, model ID investigation, configuration fixes

---

## 1. Model ID Investigation Discoveries

### Discovery: OpenRouter Model ID Convention

**Critical Finding:** OpenRouter model IDs do NOT include the `openrouter/` prefix.

```
❌ Wrong: openrouter/qwen/qwen3-coder:free
✅ Correct: qwen/qwen3-coder:free
```

**Evidence:**
- OpenRouter API returns HTTP 400: "invalid model ID" for prefixed IDs
- Official OpenRouter model pages show IDs without `openrouter/` prefix
- Model IDs follow pattern: `{provider}/{model-name}`

**Key Learning:** The `openrouter/` prefix is a common misconception. OpenRouter normalizes requests internally, so the prefix is unnecessary and causes errors.

---

### Discovery: Qwen 2.5 Hyphenation Requirement

**Critical Finding:** All Qwen 2.5 models require a hyphen between "qwen" and "2.5".

```
❌ Wrong: qwen/qwen2.5-72b-instruct (no hyphen)
✅ Correct: qwen/qwen-2.5-72b-instruct (with hyphen)
```

**Evidence:**
- OpenRouter model page: `qwen/qwen-2.5-72b-instruct`
- HTTP 400 errors for non-hyphenated versions
- Multiple instances found in configuration file

**Key Learning:** Model naming conventions are strict. Even a missing hyphen causes complete failure.

---

### Discovery: Error Type Classification

**Not all failures are the same.** Different HTTP status codes indicate different root causes:

| Error Type | HTTP Code | Root Cause | Solution |
|------------|-----------|------------|----------|
| **Invalid Model ID** | 400 | Configuration error | Fix model ID |
| **Rate Limit** | 429 | Too many requests | Wait for reset |
| **Quota Exceeded** | 429 | Billing/usage limit | Set up billing |
| **Service Unavailable** | 503 | Temporary overload | Wait for recovery |
| **Timeout/Null Error** | N/A | Provider issue | Increase timeout |

**Key Learning:** Error classification is essential for determining the right fix. HTTP 400 requires configuration changes, while HTTP 429/503 are temporary.

---

## 2. Test Execution Learnings

### Discovery: Model Recovery Patterns

**Finding:** Some models self-recover between test runs without any configuration changes.

**Evidence:**
- `google/gemini-3.1-flash-lite-preview` recovered from HTTP 503 to PASS
- Response time: 1457ms (normal)
- No configuration changes needed

**Key Learning:** HTTP 503 errors are often temporary. Re-testing after a short delay can resolve them automatically.

---

### Discovery: Rate Limit Persistence

**Finding:** HTTP 429 errors persist across test runs until daily reset.

**Evidence:**
- `qwen/qwen3.6-plus:free` failed with HTTP 429 in both test runs
- `meta-llama/llama-3.3-70b-instruct:free` failed with HTTP 429 in both runs
- OpenRouter free tier limits: 20 req/min, 200 req/day

**Key Learning:** Rate limits are cumulative. Testing multiple models sequentially quickly exhausts daily limits.

---

### Discovery: Test Script Design

**Finding:** A focused re-test script for failed models is more efficient than re-running all tests.

**Implementation:**
```python
# test_failed_models.py
# Re-tests only models that failed in the last execution
# Tracks previous errors for comparison
# Generates separate report for failed models
```

**Key Learning:** Targeted testing saves time and API quota. Always save test results for comparison.

---

## 3. Configuration Fix Learnings

### Discovery: Cascading Configuration Errors

**Finding:** A single incorrect model ID in configuration affects multiple agents/categories.

**Evidence:**
- `qwen/qwen2.5-vl-72b-instruct` appeared in 4 locations
- Each location affected a different agent/category
- All instances needed correction

**Key Learning:** Configuration errors cascade. Fixing one ID may require updating multiple locations.

---

### Discovery: JSON Validation Importance

**Finding:** Always validate JSON after manual edits to prevent syntax errors.

**Command:**
```bash
python3 -m json.tool /path/to/config.json > /dev/null
```

**Key Learning:** A single syntax error in JSON configuration can break the entire system.

---

## 4. Research Methodology Learnings

### Discovery: Direct Web Fetch > Background Agents

**Finding:** When background agents fail due to rate limiting, direct web searches are more reliable.

**Evidence:**
- 3 out of 4 background agents failed with "Request rate increased too quickly"
- Direct web searches succeeded and provided accurate information
- Official documentation pages (OpenRouter, Google AI) were authoritative sources

**Key Learning:** Background agents are great for codebase exploration, but direct web searches are better for external documentation when rate limiting is an issue.

---

### Discovery: Official Sources Are Key

**Finding:** Always verify model IDs against official provider documentation.

**Sources Used:**
- OpenRouter model pages: `https://openrouter.ai/{provider}/{model}`
- Google AI documentation: `https://ai.google.dev/gemini-api/docs/models`
- OpenRouter free models collection: `https://openrouter.ai/collections/free-models`

**Key Learning:** Secondary sources (blogs, forums) may have outdated information. Always check official documentation.

---

## 5. Technical Learnings

### Discovery: Google Gemini Model Naming

**Finding:** Current Google Gemini generation is 3.1, not 2.0 or 1.5.

**Evidence:**
- Google AI documentation shows Gemini 3.1 Pro and Gemini 3 Flash
- Model IDs: `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`
- Older generations (2.0, 1.5) are deprecated

**Key Learning:** Model versions evolve rapidly. Always check current documentation for latest generation.

---

### Discovery: OpenRouter Free Model Landscape

**Finding:** OpenRouter offers 28+ free models with varying availability.

**Top Free Models (April 2026):**
- `qwen/qwen3.6-plus:free` - 1M context, best general-purpose
- `qwen/qwen3-coder:free` - 262K context, best for coding
- `meta-llama/llama-3.3-70b-instruct:free` - 65K context
- `stepfun/step-3.5-flash:free` - 256K context, MoE architecture

**Key Learning:** Free models have rate limits but are viable for testing and light usage.

---

## 6. Documentation Learnings

### Discovery: Structured Report Generation

**Finding:** Creating multiple report types provides comprehensive documentation.

**Reports Generated:**
1. `model-id-investigation-report.md` - Comprehensive investigation details
2. `corrected-model-ids.md` - Quick reference with exact fixes
3. `failed-models-retest-report-20260406_153937.md` - Test execution results
4. `config-fix-summary.md` - Configuration change log

**Key Learning:** Different report types serve different purposes. Quick references are valuable for future fixes.

---

## 7. Meta-Learning: Problem-Solving Approach

### Understanding the Real Problem

**User Request:**
> "ignoring all models of openai, investigate the right id of each fail model"

**Initial Assumption:** All failed models have incorrect IDs

**Actual Finding:** Only 2 out of 7 failed models had incorrect IDs. The rest were rate-limited or had temporary issues.

**Key Learning:** Don't assume all failures have the same root cause. Investigate each failure individually.

---

### Solution Evolution

**Attempt 1:** Launch background agents for research
- **Result:** 3 out of 4 failed due to rate limiting

**Attempt 2:** Direct web searches
- **Result:** Found official documentation and correct model IDs

**Attempt 3:** Configuration file analysis
- **Result:** Found 5 instances of incorrect model IDs

**Attempt 4:** Configuration fixes
- **Result:** All instances corrected, JSON validated

**Key Learning:** Iterative approach with fallback strategies (agents → direct search → fix) is effective.

---

## 8. Session Statistics

| Metric | Value |
|--------|-------|
| Background agents launched | 4 |
| Background agents failed | 3 (rate limiting) |
| Web searches performed | 6 |
| Documentation pages fetched | 4 |
| Test executions | 1 (9 models re-tested) |
| Configuration fixes | 5 model IDs corrected |
| Reports generated | 4 |
| Total research time | ~30 minutes |

---

## 9. Key Takeaways

### For Model ID Management

1. **OpenRouter IDs** do NOT include `openrouter/` prefix
2. **Qwen 2.5** models require hyphen: `qwen-2.5` not `qwen2.5`
3. **Error classification** is essential (400 vs 429 vs 503)
4. **Official documentation** is the authoritative source
5. **Configuration errors cascade** - fix all instances

### For Test Execution

1. **Targeted re-testing** saves time and API quota
2. **Rate limits persist** until daily reset
3. **HTTP 503 errors** often self-recover
4. **Save test results** for comparison
5. **Generate reports** for documentation

### For Research Methodology

1. **Direct web searches** are more reliable than background agents when rate limiting
2. **Official sources** > secondary sources
3. **Multiple report types** serve different purposes
4. **Iterative approach** with fallback strategies works best
5. **Don't assume** all failures have the same root cause

---

## 10. Open Questions for Future Sessions

1. **How to optimize rate limit usage?**
   - Can we stagger model testing across multiple days?
   - Are there alternative free providers for the same models?

2. **What is the impact of the configuration fixes?**
   - Do the corrected model IDs work in practice?
   - Are there other incorrect IDs in the configuration?

3. **How to monitor model availability?**
   - Can we create a dashboard for model status?
   - How to detect when models are deprecated or renamed?

4. **What is the optimal fallback chain?**
   - Which models should be primary vs fallback?
   - How to balance free vs paid models?

5. **How to automate model ID validation?**
   - Can we create a script to validate all model IDs?
   - How to detect incorrect IDs before they cause errors?

---

## 11. Next Steps

### Immediate
- [x] Investigate failed model IDs
- [x] Fix configuration file
- [x] Generate reports
- [ ] Test corrected model IDs in practice
- [ ] Monitor for remaining errors

### Short-term
- [ ] Create model ID validation script
- [ ] Optimize rate limit usage
- [ ] Update all documentation with correct IDs
- [ ] Test fallback chains with corrected IDs

### Long-term
- [ ] Develop model availability monitoring
- [ ] Create automated configuration validation
- [ ] Research alternative free model providers
- [ ] Optimize fallback chain configuration

---

## 12. Related Files

### Generated Reports
- `model-id-investigation-report.md` - Comprehensive investigation
- `corrected-model-ids.md` - Quick reference
- `failed-models-retest-report-20260406_153937.md` - Test results
- `config-fix-summary.md` - Configuration changes

### Configuration Files
- `~/.config/opencode/oh-my-opencode.json` - Fixed model IDs

### Test Scripts
- `test_failed_models.py` - Re-test script for failed models

---

## Conclusion

This session revealed that **not all model failures are equal**. Only 2 out of 7 failed models had incorrect IDs (configuration errors), while the rest were experiencing temporary rate limits or quota issues.

The solution required:
1. **Error classification** - Distinguishing between 400, 429, and 503 errors
2. **Official documentation research** - Verifying correct model IDs
3. **Configuration fixes** - Correcting 5 instances across the config file
4. **Targeted re-testing** - Focusing only on failed models

**Most Important Learning:** Model ID conventions are strict and non-intuitive. The `openrouter/` prefix and hyphenation requirements are common sources of errors that require careful investigation.

**Secondary Learning:** Direct web searches and official documentation are more reliable than background agents when researching external APIs, especially when rate limiting is a concern.

---

**Document Version:** 1.0
**Last Updated:** April 6, 2026
