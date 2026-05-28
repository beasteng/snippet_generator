"""
09 — JSON Output Parser with Fallback
=======================================
Extract JSON from LLM text that may contain markdown fences.
Interview point: LLMs often wrap JSON in ```json ... ```; you must handle it.
"""
import json
import re

def extract_json(text: str) -> dict:
    # Try direct parse first
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    # Try extracting from markdown code fences
    match = re.search(r"```(?:json)?\s*([\s\S]*?)```", text)
    if match:
        return json.loads(match.group(1))
    raise ValueError(f"No valid JSON found in: {text[:100]}...")

if __name__ == "__main__":
    examples = [
        '{"answer": "Paris"}',
        'Here is the result:\n```json\n{"answer": "Berlin"}\n```\nDone!',
        'Sure! ```\n{"answer": "Tokyo"}\n```',
    ]
    for ex in examples:
        print(extract_json(ex))
