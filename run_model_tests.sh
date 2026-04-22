#!/bin/bash
# Model Validation Test Runner
# This script runs model tests with API keys from environment or prompts user

set -e

echo "========================================"
echo "Model Validation Test Runner"
echo "========================================"
echo ""

# Check if API keys are set
if [ -z "$OPENROUTER_API_KEY" ] && [ -z "$OPENAI_API_KEY" ] && [ -z "$GOOGLE_API_KEY" ]; then
    echo "No API keys found in environment."
    echo ""
    echo "Please set at least one of the following:"
    echo "  export OPENROUTER_API_KEY='your-key-here'"
    echo "  export OPENAI_API_KEY='your-key-here'"
    echo "  export GOOGLE_API_KEY='your-key-here'"
    echo ""
    echo "Or run the interactive version:"
    echo "  python3 test_models_interactive.py"
    echo ""
    exit 1
fi

# Run the test script
python3 test_models.py

echo ""
echo "Test complete! Check results in:"
echo "  - model-test-results.json"
echo "  - model-test-report.md"
