#!/usr/bin/env python3
"""
Updated Model Test for oh-my-opencode.json
Tests ALL unique models from the updated configuration
"""

import json
import os
import time
import requests
from datetime import datetime
from pathlib import Path

TEST_PROMPT = "What is 2 + 2? Reply with ONLY the number."
RESULTS_DIR = Path("/home/trocha/projects/explorer")

# All unique models extracted from the updated oh-my-opencode.json
ALL_MODELS = [
    # Primary models from agents
    {"id": "z-ai/glm-5", "provider": "openrouter", "source": "sisyphus, explore, multimodal-looker, sisyphus-junior, artistry, quick, unspecified-low, unspecified-high"},
    {"id": "openai/gpt-5.4", "provider": "openai", "source": "hephaestus, oracle, prometheus, momus, ultrabrain"},
    {"id": "opencode/qwen3.6-plus-free", "provider": "opencode", "source": "metis, atlas, visual-engineering"},
    {"id": "google/gemini-3.1-flash-lite-preview", "provider": "google", "source": "librarian, writing"},
    {"id": "openai/gpt-5.3-codex", "provider": "openai", "source": "deep"},
    
    # Fallback models
    {"id": "qwen/qwen3-coder-4.08.97b-a35b-instruct", "provider": "openrouter", "source": "hephaestus fallback"},
    {"id": "stepfun-ai/step-3.5-flash", "provider": "openrouter", "source": "explore, quick fallback"},
    {"id": "nvidia/nemotron-3-nano-30b-a3b", "provider": "nvidia", "source": "multimodal-looker, visual-engineering, unspecified-high fallback"},
    {"id": "nvidia/meta/llama-3.3-70b-instruct", "provider": "nvidia", "source": "atlas, sisyphus-junior, artistry, unspecified-low, writing fallback"},
    {"id": "nvidia/meta/llama-3.2-11b-vision-instruct", "provider": "nvidia", "source": "visual-engineering fallback"},
]

def load_api_keys():
    keys = {}
    keys["openai"] = os.getenv("OPENAI_API_KEY", "")
    keys["openrouter"] = os.getenv("OPENROUTER_API_KEY", "")
    keys["google"] = os.getenv("GOOGLE_API_KEY", "") or os.getenv("GEMINI_API_KEY", "")
    keys["nvidia"] = os.getenv("NVIDIA_API_KEY", "")
    keys["opencode"] = os.getenv("OPENCODE_API_KEY", "")
    
    config_path = os.path.expanduser("~/.local/share/opencode/auth.json")
    if os.path.exists(config_path):
        try:
            with open(config_path) as f:
                config = json.load(f)
                if not keys["openai"]:
                    keys["openai"] = config.get("openai", {}).get("access", "") or config.get("openai", {}).get("key", "")
                if not keys["openrouter"]:
                    keys["openrouter"] = config.get("openrouter", {}).get("key", "")
                if not keys["google"]:
                    keys["google"] = config.get("google", {}).get("key", "")
                if not keys["nvidia"]:
                    keys["nvidia"] = config.get("nvidia", {}).get("key", "")
                if not keys["opencode"]:
                    keys["opencode"] = config.get("opencode", {}).get("key", "")
        except:
            pass
    return keys

def call_openai(api_key, model_id, prompt):
    model_name = model_id.replace("openai/", "")
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {"model": model_name, "messages": [{"role": "user", "content": prompt}], "max_tokens": 50, "temperature": 0.3}
    
    start = time.time()
    try:
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload, timeout=45)
        elapsed = (time.time() - start) * 1000
        
        if response.status_code == 200:
            content = response.json()["choices"][0]["message"]["content"]
            return content, elapsed, None
        else:
            return "", elapsed, f"HTTP {response.status_code}: {response.text[:100]}"
    except Exception as e:
        return "", (time.time() - start) * 1000, str(e)

def call_openrouter(api_key, model_id, prompt):
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json", "HTTP-Referer": "https://github.com/oh-my-opencode", "X-Title": "Model Test"}
    payload = {"model": model_id, "messages": [{"role": "user", "content": prompt}], "max_tokens": 50, "temperature": 0.3}
    
    start = time.time()
    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload, timeout=45)
        elapsed = (time.time() - start) * 1000
        
        if response.status_code == 200:
            content = response.json()["choices"][0]["message"]["content"]
            return content, elapsed, None
        else:
            return "", elapsed, f"HTTP {response.status_code}: {response.text[:100]}"
    except Exception as e:
        return "", (time.time() - start) * 1000, str(e)

def call_google(api_key, model_id, prompt):
    model_name = model_id.replace("google/", "")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent"
    params = {"key": api_key}
    payload = {"contents": [{"parts": [{"text": prompt}]}], "generationConfig": {"maxOutputTokens": 50, "temperature": 0.3}}
    
    start = time.time()
    try:
        response = requests.post(url, params=params, json=payload, timeout=45)
        elapsed = (time.time() - start) * 1000
        
        if response.status_code == 200:
            content = response.json()["candidates"][0]["content"]["parts"][0]["text"]
            return content, elapsed, None
        else:
            return "", elapsed, f"HTTP {response.status_code}: {response.text[:100]}"
    except Exception as e:
        return "", (time.time() - start) * 1000, str(e)

def call_nvidia(api_key, model_id, prompt):
    # NVIDIA Build API uses OpenAI-compatible endpoint
    model_name = model_id.replace("nvidia/", "")
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {"model": model_name, "messages": [{"role": "user", "content": prompt}], "max_tokens": 50, "temperature": 0.3}
    
    start = time.time()
    try:
        response = requests.post("https://integrate.api.nvidia.com/v1/chat/completions", headers=headers, json=payload, timeout=45)
        elapsed = (time.time() - start) * 1000
        
        if response.status_code == 200:
            content = response.json()["choices"][0]["message"]["content"]
            return content, elapsed, None
        else:
            return "", elapsed, f"HTTP {response.status_code}: {response.text[:100]}"
    except Exception as e:
        return "", (time.time() - start) * 1000, str(e)

def call_opencode(api_key, model_id, prompt):
    # OpenCode uses OpenRouter-style API
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {"model": model_id, "messages": [{"role": "user", "content": prompt}], "max_tokens": 50, "temperature": 0.3}
    
    start = time.time()
    try:
        # OpenCode Zen API endpoint (assumed)
        response = requests.post("https://api.opencode.ai/v1/chat/completions", headers=headers, json=payload, timeout=45)
        elapsed = (time.time() - start) * 1000
        
        if response.status_code == 200:
            content = response.json()["choices"][0]["message"]["content"]
            return content, elapsed, None
        else:
            return "", elapsed, f"HTTP {response.status_code}: {response.text[:100]}"
    except Exception as e:
        return "", (time.time() - start) * 1000, str(e)

def test_model(model_info, api_keys):
    model_id = model_info["id"]
    provider = model_info["provider"]
    source = model_info.get("source", "")
    
    print(f"[{model_id}] Testing... ", end="", flush=True)
    
    if provider == "openai":
        response, elapsed, error = call_openai(api_keys.get("openai", ""), model_id, TEST_PROMPT)
    elif provider == "openrouter":
        response, elapsed, error = call_openrouter(api_keys.get("openrouter", ""), model_id, TEST_PROMPT)
    elif provider == "google":
        response, elapsed, error = call_google(api_keys.get("google", ""), model_id, TEST_PROMPT)
    elif provider == "nvidia":
        response, elapsed, error = call_nvidia(api_keys.get("nvidia", ""), model_id, TEST_PROMPT)
    elif provider == "opencode":
        response, elapsed, error = call_opencode(api_keys.get("opencode", ""), model_id, TEST_PROMPT)
    else:
        return {"model": model_id, "status": "ERROR", "response_time_ms": 0, "response": "", "error": f"Unknown provider: {provider}"}
    
    passed = response and "4" in response and not error
    status = "PASS" if passed else "FAIL" if response and not error else "ERROR"
    
    status_icon = "✅" if passed else "❌"
    print(f"{status_icon} {status} ({int(elapsed)}ms)")
    
    return {
        "model": model_id,
        "provider": provider,
        "source": source,
        "status": status,
        "response_time_ms": int(elapsed),
        "response": response[:200] if response else "",
        "error": error,
        "passed": passed
    }

def main():
    print("=" * 80)
    print("COMPREHENSIVE MODEL TEST - UPDATED oh-my-opencode.json")
    print(f"Started: {datetime.now()}")
    print("=" * 80)
    
    api_keys = load_api_keys()
    print(f"\nAPI Keys loaded: {', '.join(k for k, v in api_keys.items() if v)}")
    
    results = []
    for model_info in ALL_MODELS:
        result = test_model(model_info, api_keys)
        results.append(result)
        time.sleep(1)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    results_file = RESULTS_DIR / f"updated-model-test-results-{timestamp}.json"
    report_file = RESULTS_DIR / f"updated-model-test-report-{timestamp}.md"
    
    with open(results_file, 'w') as f:
        json.dump({"test_date": datetime.now().isoformat(), "test_prompt": TEST_PROMPT, "results": results}, f, indent=2)
    
    passed = sum(1 for r in results if r['passed'])
    total = len(results)
    
    report_lines = [
        f"# Updated Model Test Report",
        f"**Date**: {datetime.now()}",
        f"**Test**: '{TEST_PROMPT}' → Expected: '4'",
        f"",
        f"## Summary: {passed}/{total} passed ({passed*100//total}%)",
        f"",
        f"| Model | Provider | Source | Status | Time | Response |",
        f"|-------|----------|--------|--------|------|----------|",
    ]
    
    for r in results:
        icon = "✅" if r['passed'] else "❌"
        resp = r['response'][:30].replace('\n', ' ')
        source_short = r['source'][:40] if r.get('source') else ""
        report_lines.append(f"| `{r['model']}` | {r['provider']} | {source_short} | {icon} {r['status']} | {r['response_time_ms']}ms | {resp}... |")
    
    with open(report_file, 'w') as f:
        f.write('\n'.join(report_lines))
    
    print("\n" + "=" * 80)
    print(f"Results: {passed}/{total} passed ({passed*100//total}%)")
    print(f"Saved: {results_file}")
    print(f"Report: {report_file}")
    print("=" * 80)

if __name__ == "__main__":
    main()
