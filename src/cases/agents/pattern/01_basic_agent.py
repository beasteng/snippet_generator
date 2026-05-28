"""
01 — Basic Agent
=================
Simplest possible agent: single LLM call with a system prompt.
Interview point: An "agent" at minimum is an LLM + instructions.
"""
from openai import OpenAI

def run(query: str) -> str:
    client = OpenAI()
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": query},
        ],
    )
    return resp.choices[0].message.content

if __name__ == "__main__":
    print(run("Explain recursion in one sentence."))
