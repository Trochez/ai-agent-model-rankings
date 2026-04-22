#!/bin/bash
# Model Test Execution Script via OpenCode CLI
# Tests all 12 unique models from oh-my-opencode.json

TEST_DIR="/home/trocha/projects/explorer"
RESULTS_FILE="$TEST_DIR/model-test-results-$(date +%Y%m%d_%H%M%S).json"
REPORT_FILE="$TEST_DIR/model-test-report-$(date +%Y%m%d_%H%M%S).md"
OPENCODE="/home/trocha/.opencode/bin/opencode"

# Test prompt
TEST_PROMPT="What is 2 + 2? Reply with ONLY the number, no explanation."

# Models to test (12 unique models)
declare -a MODELS=(
    "nvidia/z-ai/glm5"
    "openai/gpt-5.4"
    "openrouter/qwen/qwen3.6-plus:free"
    "google/gemini-3.1-flash-preview"
    "openrouter/google/lyria-3-pro-preview:free"
    "openrouter/qwen/qwen2.5-vl-72b-instruct"
    "openai/gpt-5.3-codex"
    "google/gemini-3.1-pro-preview"
    "openrouter/qwen/qwen3-coder-plus"
    "openrouter/stepfun/step-3.5-flash:free"
    "openrouter/meta-llama/llama-3.3-70b-instruct:free"
    "openrouter/qwen/qwen-2.5-72b-instruct"
)

# Initialize results JSON
echo '{"test_date": "'$(date -Iseconds)'", "results": [' > "$RESULTS_FILE"

# Counter for JSON formatting
first=true

echo "# Model Test Execution Report" > "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "**Test Date**: $(date)" >> "$REPORT_FILE"
echo "**Test Prompt**: \"$TEST_PROMPT\"" >> "$REPORT_FILE"
echo "**Expected Response**: \"4\"" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "## Test Results" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "| Model | Status | Response Time | Response | Pass/Fail |" >> "$REPORT_FILE"
echo "|-------|--------|---------------|----------|-----------|" >> "$REPORT_FILE"

# Test each model
for model in "${MODELS[@]}"; do
    echo "Testing model: $model"
    
    # Measure response time
    start_time=$(date +%s%N)
    
    # Run test
    response=$($OPENCODE run -m "$model" "$TEST_PROMPT" 2>&1)
    exit_code=$?
    
    end_time=$(date +%s%N)
    duration_ms=$(( (end_time - start_time) / 1000000 ))
    
    # Check if response contains "4"
    if [[ "$response" == *"4"* ]] && [ $exit_code -eq 0 ]; then
        status="PASS"
        pass_fail="✅ PASS"
    else
        status="FAIL"
        pass_fail="❌ FAIL"
    fi
    
    # Truncate response for display (first 100 chars)
    response_display=$(echo "$response" | head -c 100 | tr '\n' ' ')
    
    # Add to JSON
    if [ "$first" = true ]; then
        first=false
    else
        echo "," >> "$RESULTS_FILE"
    fi
    
    cat >> "$RESULTS_FILE" <<EOF
{
  "model": "$model",
  "status": "$status",
  "response_time_ms": $duration_ms,
  "response": $(echo "$response" | jq -Rs .),
  "exit_code": $exit_code
}
EOF
    
    # Add to Markdown report
    echo "| \`$model\` | $status | ${duration_ms}ms | $response_display... | $pass_fail |" >> "$REPORT_FILE"
    
    # Delay to avoid rate limits
    sleep 2
done

# Close JSON
echo ']}' >> "$RESULTS_FILE"

# Add summary to report
echo "" >> "$REPORT_FILE"
echo "## Summary" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
total=${#MODELS[@]}
passed=$(grep -c "PASS" "$REPORT_FILE" | head -1 || echo 0)
failed=$((total - passed))
echo "- **Total Models Tested**: $total" >> "$REPORT_FILE"
echo "- **Passed**: $passed" >> "$REPORT_FILE"
echo "- **Failed**: $failed" >> "$REPORT_FILE"
echo "- **Pass Rate**: $(( passed * 100 / total ))%" >> "$REPORT_FILE"

echo ""
echo "Test execution complete!"
echo "Results saved to: $RESULTS_FILE"
echo "Report saved to: $REPORT_FILE"
