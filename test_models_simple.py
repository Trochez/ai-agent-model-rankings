#!/usr/bin/env python3
"""Model validation test using OpenCode CLI"""

import subprocess
import json
import time
from datetime import datetime
from pathlib import Path

TEST_PROMPT = "What is 2 + 2? Reply with ONLY the number."
OPENCODE_CLI = "/home/trocha/.opencode/bin/opencode"
RESULTS_DIR = Path("/home/trocha/projects/explorer")

MODELS = [
    "nvidia/z-ai/glm5",
    "openai/gpt-5.4",
    "openrouter/qwen/qwen3.6-plus:free",
    "google/gemini-3.1-flash-preview",
    "openrouter/google/lyria-3-pro-preview:free",
    "openrouter/qwen/qwen2.5-vl-72b-instruct",
    "openai/gpt-5.3-codex",
    "google/gemini-3.1-pro-preview",
    "openrouter/qwen/qwen3-coder-plus",
    "openrouter/stepfun/step-3.5-flash:free",
    "openrouter/meta-llama/llama-3.3-70b-instruct:free",
    "openrouter/qwen/qwen-2.5-72b-instruct",
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
            timeout=30
        )
        end_time = time.time()
        duration_ms = int((end_time - start_time) * 1000)
        
        response = result.stdout.strip()
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
            "error": "Test timed out after 30 seconds"
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
    
    print(f"Starting model validation tests at {datetime.now()}")
    print(f"Total models to test: {len(MODELS)}")
    print(f"Test prompt: '{TEST_PROMPT}'")
    print("-" * 80)
    
    for model in MODELS:
        result = test_model(model)
        results.append(result)
        print(f"  Status: {result['status']} | Time: {result['response_time_ms']}ms")
        
        time.sleep(1)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    results_file = RESULTS_DIR / f"model-test-results-{timestamp}.json"
    report_file = RESULTS_DIR / f"model-test-report-{timestamp}.md"
    
    with open(results_file, 'w') as f:
        json.dump({
            "test_date": datetime.now().isoformat(),
            "test_prompt": TEST_PROMPT,
            "expected_response": "4",
            "results": results
        }, f, indent=2)
    
    passed = sum(1 for r in results if r['status'] == 'PASS')
    failed = len(results) - passed
    
    with open(report_file, 'w') as f:
        f.write("# Model Test Execution Report\n\n")
        f.write(f"**Test Date**: {datetime.now()}\n")
        f.write(f"**Test Prompt**: \"{TEST_PROMPT}\"\n")
        f.write(f"**Expected Response**: \"4\"\n\n")
        f.write("## Summary\n\n")
        f.write(f"- **Total Models Tested**: {len(results)}\n")
        f.write(f"- **Passed**: {passed}\n")
        f.write(f"- **Failed**: {failed}\n")
        f.write(f"- **Pass Rate**: {passed * 100 // len(results)}%\n\n")
        f.write("## Detailed Results\n\n")
        f.write("| Model | Status | Response Time | Response | Pass/Fail |\n")
        f.write("|-------|--------|---------------|----------|----------|\n")
        
        for r in results:
            status_icon = "✅" if r['status'] == 'PASS' else "❌"
            response_preview = r['response'][:50].replace('\n', ' ')
            f.write(f"| `{r['model']}` | {r['status']} | {r['response_time_ms']}ms | {response_preview}... | {status_icon} |\n")
    
    print("-" * 80)
    print(f"\nTest execution complete!")
    print(f"Results saved to: {results_file}")
    print(f"Report saved to: {report_file}")
    print(f"\nSummary: {passed}/{len(results)} models passed ({passed * 100 // len(results)}%)")

if __name__ == "__main__":
    main()
