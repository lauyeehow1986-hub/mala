#!/usr/bin/env python3
"""PreToolUse Agent Hook for Antigravity Gemini 3.8 Flash Mala Optimiser."""
import sys
import json

def main():
    raw = sys.stdin.read().strip()
    if not raw:
        print(json.dumps({"status": "ALLOW", "note": "Empty stdin; pass-through"}))
        return
    try:
        payload = json.loads(raw)
    except Exception:
        print(json.dumps({"status": "ALLOW", "note": "Non-JSON payload"}))
        return

    args = payload.get("arguments", {})
    budget = float(args.get("budget_sgd", 30.0))
    if budget > 30.0:
        print(json.dumps({
            "status": "WARN_AND_CLAMP",
            "clamped_budget_sgd": 30.0,
            "reason": f"User specified fixed $30.00 SGD budget; clamped requested {budget} SGD to 30.00 SGD."
        }))
        return
    print(json.dumps({"status": "ALLOW", "verified_budget_sgd": budget}))

if __name__ == "__main__":
    main()
