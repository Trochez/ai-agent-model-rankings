#!/usr/bin/env python3
"""
Test all models mentioned in oh-my-opencode.json configuration.
Tests each model with a simple prompt to verify availability.
"""

import subprocess
import json
import time
from datetime import datetime

# Models extracted from ~/.config/opencode/oh-my-opencode.json
MODELS = [
    # Primary models
    "nvidia/z-ai/glm5",
    "openai/gpt-5.4",
    "google/gemini-3.1-flash-lite-preview",
    
    # Fallback models
    "openai/gpt-5.3-codex",
    "nvidia/nemotron-3-super-120b-a12b",
    "nvidia/qwen/qwen3-coder-480b-a35b-instruct",
    "opencode/qwen3.6-plus-free",
    "nvidia/stepfun-ai/step-3.5-flash",
    "nvidia/nvidia/nemotron-3-nano-30b-a3b",
    "nvidia/nvidia-nemotron-nano-9b-v2",
    "nvidia/meta/llama-3.3-70b-instruct",
    "nvidia/meta/llama-3.2-11b-vision-instruct",
    "nvidia/nemotron-nano-12b-v2-vl:free",
    "nvidia/nemotron-3-nano-30b-a3b",
]

def test_model(model_id):
    prompt = "Say 'Model working' and nothing else."
    
    start_time = time.time()
    
    try:
        result = subprocess.run(
            ["opencode", "run", "-m", model_id, prompt],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        elapsed = time.time() - start_time
        
        if result.returncode == 0:
            output = result.stdout.strip()
            # Check if output contains expected response
            if "working" in output.lower() or "model" in output.lower():
                return {
                    "status": "PASS",
                    "time_ms": int(elapsed * 1000),
                    "output": output[:100]
                }
            else:
                return {
                    "status": "PASS",
                    "time_ms": int(elapsed * 1000),
                    "output": output[:100],
                    "note": "Unexpected output"
                }
        else:
            error = result.stderr.strip()
            if "429" in error or "rate limit" in error.lower():
                return {
                    "status": "RATE_LIMITED",
                    "time_ms": int(elapsed * 1000),
                    "error": error[:200]
                }
            elif "404" in error or "not found" in error.lower():
                return {
                    "status": "NOT_FOUND",
                    "time_ms": int(elapsed * 1000),
                    "error": error[:200]
                }
            elif "400" in error or "invalid" in error.lower():
                return {
                    "status": "INVALID",
                    "time_ms": int(elapsed * 1000),
                    "error": error[:200]
                }
            else:
                return {
                    "status": "ERROR",
                    "time_ms": int(elapsed * 1000),
                    "error": error[:200]
                }
    except subprocess.TimeoutExpired:
        return {
            "status": "TIMEOUT",
            "time_ms": 60000,
            "error": "Request timed out after 60s"
        }
    except Exception as e:
        return {
            "status": "ERROR",
            "time_ms": 0,
            "error": str(e)[:200]
        }

def main():
    print("=" * 80)
    print(f"Model Configuration Test - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    print()
    
    results = {}
    passed = 0
    failed = 0
    
    for model in MODELS:
        print(f"Testing: {model}...", end=" ", flush=True)
        result = test_model(model)
        results[model] = result
        
        status = result["status"]
        time_ms = result["time_ms"]
        
        if status == "PASS":
            print(f"✅ PASS ({time_ms}ms)")
            passed += 1
        elif status == "RATE_LIMITED":
            print(f"⏳ RATE LIMITED ({time_ms}ms)")
            failed += 1
        elif status == "NOT_FOUND":
            print(f"❌ NOT FOUND ({time_ms}ms)")
            failed += 1
        elif status == "INVALID":
            print(f"⚠️  INVALID ({time_ms}ms)")
            failed += 1
        elif status == "TIMEOUT":
            print(f"⏱️  TIMEOUT ({time_ms}ms)")
            failed += 1
        else:
            print(f"❌ ERROR ({time_ms}ms)")
            failed += 1
        
        # Small delay between tests to avoid rate limiting
        time.sleep(1)
    
    print()
    print("=" * 80)
    print(f"Results: {passed} passed, {failed} failed out of {len(MODELS)} models")
    print("=" * 80)
    print()
    
    # Print detailed results
    print("Detailed Results:")
    print("-" * 80)
    
    for model, result in results.items():
        status = result["status"]
        time_ms = result["time_ms"]
        
        if status == "PASS":
            print(f"✅ {model}")
            print(f"   Status: {status}, Time: {time_ms}ms")
            if "output" in result:
                print(f"   Output: {result['output'][:80]}")
        else:
            print(f"❌ {model}")
            print(f"   Status: {status}, Time: {time_ms}ms")
            if "error" in result:
                print(f"   Error: {result['error'][:80]}")
        print()
    
    # Save results to JSON
    output_file = f"model_test_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, "w") as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "summary": {
                "total": len(MODELS),
                "passed": passed,
                "failed": failed
            },
            "results": results
        }, f, indent=2)
    
    print(f"Results saved to: {output_file}")

if __name__ == "__main__":
    main()
