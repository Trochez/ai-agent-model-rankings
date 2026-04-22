#!/usr/bin/env python3
"""
Comprehensive Model Test for oh-my-opencode.json
Tests ALL 11 unique models including primary and fallback models
"""

import subprocess
import json
import time
from datetime import datetime
from pathlib import Path

# Test configuration
TEST_PROMPT = "What is 2 + 2? Reply with ONLY the number."
OPENCODE_CLI = "/home/trocha/.opencode/bin/opencode"
RESULTS_DIR = Path("/home/trocha/projects/explorer")

# All unique models from oh-my-opencode.json (primary + fallbacks)
ALL_MODELS = [
    "z-ai/glm-5",
    "openai/gpt-5.4",
    "qwen/qwen3.6-plus:free",
    "google/gemini-3.1-flash-lite-preview",
    "google/gemini-3.1-pro-preview",
    "meta-llama/llama-3.3-70b-instruct:free",
    "openai/gpt-5.3-codex",
    "openrouter/qwen/qwen2.5-72b-instruct",
    "openrouter/qwen/qwen3-coder:free",
    "qwen/qwen2.5-vl-72b-instruct",
    "stepfun/step-3.5-flash:free",
]

def test_model(model: str) -> dict:
    """Test a single model and return results"""
    print(f"Testing: {model}")
    
    start_time = time.time()
    try:
        result = subprocess.run(
            [OPENCODE_CLI, "run", "-m", model, TEST_PROMPT],
            capture_output=True,
            text=True,
            timeout=60  # Increased timeout for slower models
        )
        end_time = time.time()
        duration_ms = int((end_time - start_time) * 1000)
        
        response = result.stdout.strip()
        # Check if response contains "4" (correct answer)
        passed = "4" in response and result.returncode == 0
        
        return {
            "model": model,
            "status": "PASS" if passed else "FAIL",
            "response_time_ms": duration_ms,
            "response": response[:200],
            "exit_code": result.returncode,
            "error": result.stderr[:200] if result.stderr else None
        }
    except subprocess.TimeoutExpired:
        end_time = time.time()
        duration_ms = int((end_time - start_time) * 1000)
        return {
            "model": model,
            "status": "TIMEOUT",
            "response_time_ms": duration_ms,
            "response": "",
            "exit_code": -1,
            "error": "Test timed out after 60 seconds"
        }
    except Exception as e:
        end_time = time.time()
        duration_ms = int((end_time - start_time) * 1000)
        return {
            "model": model,
            "status": "ERROR",
            "response_time_ms": duration_ms,
            "response": "",
            "exit_code": -1,
            "error": str(e)
        }

def main():
    results = []
    
    print("=" * 80)
    print(f"COMPREHENSIVE MODEL VALIDATION TEST")
    print(f"Started at: {datetime.now()}")
    print("=" * 80)
    print(f"\nTotal models to test: {len(ALL_MODELS)}")
    print(f"Test prompt: '{TEST_PROMPT}'")
    print(f"Expected response: '4'")
    print("-" * 80)
    
    for i, model in enumerate(ALL_MODELS, 1):
        print(f"\n[{i}/{len(ALL_MODELS)}] ", end="")
        result = test_model(model)
        results.append(result)
        
        status_icon = "✅" if result['status'] == 'PASS' else "❌"
        print(f"  {status_icon} Status: {result['status']} | Time: {result['response_time_ms']}ms")
        
        if result['error']:
            print(f"  ⚠️  Error: {result['error'][:100]}")
        
        # Small delay between tests to avoid rate limits
        time.sleep(2)
    
    # Generate timestamp for output files
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    results_file = RESULTS_DIR / f"comprehensive-test-results-{timestamp}.json"
    report_file = RESULTS_DIR / f"comprehensive-test-report-{timestamp}.md"
    
    # Save JSON results
    with open(results_file, 'w') as f:
        json.dump({
            "test_date": datetime.now().isoformat(),
            "test_prompt": TEST_PROMPT,
            "expected_response": "4",
            "total_models": len(ALL_MODELS),
            "results": results
        }, f, indent=2)
    
    # Calculate statistics
    passed = sum(1 for r in results if r['status'] == 'PASS')
    failed = sum(1 for r in results if r['status'] == 'FAIL')
    timeout = sum(1 for r in results if r['status'] == 'TIMEOUT')
    error = sum(1 for r in results if r['status'] == 'ERROR')
    
    # Generate markdown report
    report_lines = [
        "# Comprehensive Model Test Report",
        "",
        f"**Test Date**: {datetime.now()}",
        f"**Test Prompt**: \"{TEST_PROMPT}\"",
        f"**Expected Response**: \"4\"",
        "",
        "## Summary",
        "",
        f"- **Total Models Tested**: {len(results)}",
        f"- **Passed**: {passed} ({passed * 100 // len(results)}%)",
        f"- **Failed**: {failed}",
        f"- **Timeout**: {timeout}",
        f"- **Error**: {error}",
        "",
        "## Detailed Results",
        "",
        "| Model | Status | Response Time | Response | Result |",
        "|-------|--------|---------------|----------|--------|",
    ]
    
    for r in results:
        status_icon = "✅" if r['status'] == 'PASS' else "❌"
        response_preview = r['response'][:50].replace('\n', ' ')
        report_lines.append(
            f"| `{r['model']}` | {r['status']} | {r['response_time_ms']}ms | {response_preview}... | {status_icon} |"
        )
    
    # Add performance analysis
    report_lines.extend([
        "",
        "## Performance Analysis",
        "",
        "### Fastest Models",
        "",
    ])
    
    sorted_by_time = sorted([r for r in results if r['status'] == 'PASS'], 
                           key=lambda x: x['response_time_ms'])
    for i, r in enumerate(sorted_by_time[:5], 1):
        report_lines.append(f"{i}. `{r['model']}` - {r['response_time_ms']}ms")
    
    # Add model categorization
    report_lines.extend([
        "",
        "## Model Categories",
        "",
        "### Primary Models (Used by agents)",
        "- `z-ai/glm-5` - Primary for sisyphus, explore, sisyphus-junior, quick, unspecified-low, unspecified-high",
        "- `openai/gpt-5.4` - Primary for hephaestus, oracle, prometheus, momus",
        "- `qwen/qwen3.6-plus:free` - Primary for metis, multimodal-looker, atlas",
        "- `google/gemini-3.1-flash-lite-preview` - Primary for librarian, writing",
        "- `openai/gpt-5.3-codex` - Primary for deep category",
        "- `google/gemini-3.1-pro-preview` - Primary for artistry category",
        "- `qwen/qwen2.5-vl-72b-instruct` - Primary for visual-engineering category",
        "",
        "### Fallback Models",
        "- `meta-llama/llama-3.3-70b-instruct:free` - Fallback for multiple agents",
        "- `openrouter/qwen/qwen2.5-72b-instruct` - Fallback for writing category",
        "- `openrouter/qwen/qwen3-coder:free` - Fallback for hephaestus",
        "- `stepfun/step-3.5-flash:free` - Fallback for explore, quick",
        "",
    ])
    
    with open(report_file, 'w') as f:
        f.write('\n'.join(report_lines))
    
    # Print final summary
    print("\n" + "=" * 80)
    print("TEST EXECUTION COMPLETE")
    print("=" * 80)
    print(f"\nResults saved to:")
    print(f"  - {results_file}")
    print(f"  - {report_file}")
    print(f"\nSummary:")
    print(f"  ✅ Passed: {passed}/{len(results)} ({passed * 100 // len(results)}%)")
    print(f"  ❌ Failed: {failed}")
    print(f"  ⏱️  Timeout: {timeout}")
    print(f"  ⚠️  Error: {error}")
    print("\n" + "=" * 80)

if __name__ == "__main__":
    main()
