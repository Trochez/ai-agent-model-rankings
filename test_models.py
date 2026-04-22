#!/usr/bin/env python3
"""
Model Validation Test Script for oh-my-opencode.json
Tests all 13 unique models with multiple test cases
"""

import json
import os
import time
import requests
from datetime import datetime
from typing import Dict, List, Tuple, Optional
import sys

# Test configuration
TEST_PROMPTS = {
    "test1_arithmetic": {
        "prompt": "What is 2 + 2? Reply with ONLY the number, no explanation.",
        "expected": "4",
        "validation": lambda r: "4" in r.strip()
    },
    "test2_instructions": {
        "prompt": "List three colors. Use a numbered list.",
        "expected": "Numbered list with 3 colors",
        "validation": lambda r: (
            any(str(i) in r for i in range(1, 4)) and
            any(color in r.lower() for color in ["red", "blue", "green", "yellow", "orange", "purple", "black", "white", "pink", "brown"])
        )
    },
    "test3_logic": {
        "prompt": "If it's raining, I need an umbrella. It's raining. Do I need an umbrella? Answer yes or no.",
        "expected": "yes",
        "validation": lambda r: "yes" in r.lower().strip()
    },
    "test4_code": {
        "prompt": "What does this code output? ```python\nprint(3 * 4)\n```",
        "expected": "12",
        "validation": lambda r: "12" in r.strip()
    }
}

# Model definitions with provider info
MODELS = {
    "z-ai/glm-5": {
        "provider": "openrouter",
        "type": "orchestrator"
    },
    "openai/gpt-5.4": {
        "provider": "openai",
        "type": "high-reasoning"
    },
    "qwen/qwen3.6-plus:free": {
        "provider": "openrouter",
        "type": "general"
    },
    "google/gemini-3.1-flash-preview": {
        "provider": "google",
        "type": "fast"
    },
    "google/lyria-3-pro-preview:free": {
        "provider": "openrouter",
        "type": "visual"
    },
    "qwen/qwen2.5-vl-72b-instruct": {
        "provider": "openrouter",
        "type": "vision"
    },
    "openai/gpt-5.3-codex": {
        "provider": "openai",
        "type": "code"
    },
    "google/gemini-3.1-pro-preview": {
        "provider": "google",
        "type": "pro"
    },
    "qwen/qwen3-coder-plus": {
        "provider": "openrouter",
        "type": "code"
    },
    "stepfun/step-3.5-flash:free": {
        "provider": "openrouter",
        "type": "fast"
    },
    "meta-llama/llama-3.3-70b-instruct:free": {
        "provider": "openrouter",
        "type": "general"
    },
    "qwen/qwen-2.5-72b-instruct": {
        "provider": "openrouter",
        "type": "general"
    }
}

class ModelTester:
    def __init__(self):
        self.results = {}
        self.api_keys = self._load_api_keys()
        
    def _load_api_keys(self) -> Dict[str, str]:
        """Load API keys from environment or config"""
        keys = {}
        
        # Try environment variables first
        keys["openai"] = os.getenv("OPENAI_API_KEY", "")
        keys["openrouter"] = os.getenv("OPENROUTER_API_KEY", "")
        keys["google"] = os.getenv("GOOGLE_API_KEY", "") or os.getenv("GEMINI_API_KEY", "")
        
        # Try OpenCode config if env vars not found
        if not any(keys.values()):
            config_path = os.path.expanduser("~/.config/opencode/config.json")
            if os.path.exists(config_path):
                try:
                    with open(config_path) as f:
                        config = json.load(f)
                        keys["openai"] = config.get("openai_api_key", "")
                        keys["openrouter"] = config.get("openrouter_api_key", "")
                        keys["google"] = config.get("google_api_key", "")
                except:
                    pass
        
        return keys
    
    def _call_openai(self, model: str, prompt: str) -> Tuple[str, float, Optional[str]]:
        """Call OpenAI API"""
        if not self.api_keys.get("openai"):
            return "", 0, "No OpenAI API key configured"
        
        # Extract model name (remove openai/ prefix)
        model_name = model.replace("openai/", "")
        
        headers = {
            "Authorization": f"Bearer {self.api_keys['openai']}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": model_name,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 100,
            "temperature": 0.3
        }
        
        try:
            start = time.time()
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=30
            )
            elapsed = (time.time() - start) * 1000  # ms
            
            if response.status_code == 200:
                data = response.json()
                content = data["choices"][0]["message"]["content"]
                return content, elapsed, None
            else:
                return "", elapsed, f"HTTP {response.status_code}: {response.text[:100]}"
        except Exception as e:
            return "", 0, str(e)
    
    def _call_openrouter(self, model: str, prompt: str) -> Tuple[str, float, Optional[str]]:
        """Call OpenRouter API"""
        if not self.api_keys.get("openrouter"):
            return "", 0, "No OpenRouter API key configured"
        
        headers = {
            "Authorization": f"Bearer {self.api_keys['openrouter']}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/oh-my-opencode",
            "X-Title": "Model Validation Test"
        }
        
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 100,
            "temperature": 0.3
        }
        
        try:
            start = time.time()
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=30
            )
            elapsed = (time.time() - start) * 1000  # ms
            
            if response.status_code == 200:
                data = response.json()
                content = data["choices"][0]["message"]["content"]
                return content, elapsed, None
            else:
                return "", elapsed, f"HTTP {response.status_code}: {response.text[:100]}"
        except Exception as e:
            return "", 0, str(e)
    
    def _call_google(self, model: str, prompt: str) -> Tuple[str, float, Optional[str]]:
        """Call Google Gemini API"""
        if not self.api_keys.get("google"):
            return "", 0, "No Google API key configured"
        
        # Extract model name (remove google/ prefix)
        model_name = model.replace("google/", "")
        
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent"
        
        params = {"key": self.api_keys["google"]}
        
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "maxOutputTokens": 100,
                "temperature": 0.3
            }
        }
        
        try:
            start = time.time()
            response = requests.post(
                url,
                params=params,
                json=payload,
                timeout=30
            )
            elapsed = (time.time() - start) * 1000  # ms
            
            if response.status_code == 200:
                data = response.json()
                content = data["candidates"][0]["content"]["parts"][0]["text"]
                return content, elapsed, None
            else:
                return "", elapsed, f"HTTP {response.status_code}: {response.text[:100]}"
        except Exception as e:
            return "", 0, str(e)
    
    def test_model(self, model: str, test_name: str) -> Dict:
        """Test a single model with a single test case"""
        provider = MODELS[model]["provider"]
        prompt_data = TEST_PROMPTS[test_name]
        prompt = prompt_data["prompt"]
        
        # Call appropriate API
        if provider == "openai":
            response, elapsed, error = self._call_openai(model, prompt)
        elif provider == "openrouter":
            response, elapsed, error = self._call_openrouter(model, prompt)
        elif provider == "google":
            response, elapsed, error = self._call_google(model, prompt)
        else:
            return {
                "model": model,
                "test": test_name,
                "status": "error",
                "error": f"Unknown provider: {provider}",
                "response": "",
                "time_ms": 0,
                "pass": False
            }
        
        # Validate response
        if error:
            status = "error"
            passed = False
        else:
            passed = prompt_data["validation"](response)
            status = "pass" if passed else "fail"
        
        return {
            "model": model,
            "test": test_name,
            "status": status,
            "error": error,
            "response": response[:200],  # Truncate long responses
            "time_ms": round(elapsed, 2),
            "pass": passed
        }
    
    def run_all_tests(self) -> Dict:
        """Run all tests for all models"""
        results = {
            "timestamp": datetime.now().isoformat(),
            "models": {}
        }
        
        for model in MODELS.keys():
            print(f"\nTesting {model}...")
            results["models"][model] = {
                "provider": MODELS[model]["provider"],
                "type": MODELS[model]["type"],
                "tests": {}
            }
            
            # Run tests 1-3 for all models
            for test_name in ["test1_arithmetic", "test2_instructions", "test3_logic"]:
                print(f"  Running {test_name}...")
                result = self.test_model(model, test_name)
                results["models"][model]["tests"][test_name] = result
                
                # Add delay to avoid rate limits
                time.sleep(1)
            
            # Run test 4 for code models
            if MODELS[model]["type"] == "code":
                print(f"  Running test4_code...")
                result = self.test_model(model, "test4_code")
                results["models"][model]["tests"]["test4_code"] = result
                time.sleep(1)
        
        return results
    
    def generate_report(self, results: Dict) -> str:
        """Generate markdown report"""
        report = []
        report.append("# Model Validation Test Results")
        report.append(f"\n**Test Date**: {results['timestamp']}")
        report.append(f"\n**Total Models Tested**: {len(results['models'])}")
        
        # Summary statistics
        total_tests = 0
        passed_tests = 0
        failed_tests = 0
        error_tests = 0
        
        for model, data in results["models"].items():
            for test_name, test_result in data["tests"].items():
                total_tests += 1
                if test_result["status"] == "pass":
                    passed_tests += 1
                elif test_result["status"] == "fail":
                    failed_tests += 1
                else:
                    error_tests += 1
        
        report.append(f"\n## Summary Statistics")
        report.append(f"\n- **Total Tests**: {total_tests}")
        report.append(f"- **Passed**: {passed_tests} ({passed_tests/total_tests*100:.1f}%)")
        report.append(f"- **Failed**: {failed_tests} ({failed_tests/total_tests*100:.1f}%)")
        report.append(f"- **Errors**: {error_tests} ({error_tests/total_tests*100:.1f}%)")
        
        # Detailed results
        report.append(f"\n## Detailed Results")
        
        for model, data in results["models"].items():
            report.append(f"\n### Model: `{model}`")
            report.append(f"\n- **Provider**: {data['provider']}")
            report.append(f"- **Type**: {data['type']}")
            
            for test_name, test_result in data["tests"].items():
                status_emoji = "✅" if test_result["pass"] else "❌"
                report.append(f"\n#### {test_name}")
                report.append(f"\n- **Status**: {status_emoji} {test_result['status'].upper()}")
                report.append(f"\n- **Response Time**: {test_result['time_ms']}ms")
                
                if test_result["error"]:
                    report.append(f"\n- **Error**: {test_result['error']}")
                
                report.append(f"\n- **Response**: `{test_result['response']}`")
        
        return "\n".join(report)


def main():
    print("=" * 80)
    print("Model Validation Test for oh-my-opencode.json")
    print("=" * 80)
    
    tester = ModelTester()
    
    # Check API keys
    print("\nChecking API keys...")
    for provider, key in tester.api_keys.items():
        status = "✓ Found" if key else "✗ Not found"
        print(f"  {provider}: {status}")
    
    # Run tests
    print("\nRunning tests...")
    results = tester.run_all_tests()
    
    # Generate report
    print("\nGenerating report...")
    report = tester.generate_report(results)
    
    # Save results
    output_file = "/home/trocha/projects/explorer/model-test-results.json"
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to: {output_file}")
    
    # Save report
    report_file = "/home/trocha/projects/explorer/model-test-report.md"
    with open(report_file, "w") as f:
        f.write(report)
    print(f"Report saved to: {report_file}")
    
    # Print summary
    print("\n" + "=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)
    print(report)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
