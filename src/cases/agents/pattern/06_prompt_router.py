"""
06 — Prompt Router
====================
Route queries to specialised system prompts.
Interview point: Routing is the simplest form of "agent decision-making."
"""

SYSTEM_PROMPTS = {
    "code":  "You are an expert Python developer. Write clean, typed code.",
    "sql":   "You are a SQL expert. Write optimised queries.",
    "chat":  "You are a friendly conversational assistant.",
}

def route(query: str) -> str:
    q = query.lower()
    if any(w in q for w in ["python", "code", "function", "class"]):
        return "code"
    if any(w in q for w in ["sql", "query", "database", "table"]):
        return "sql"
    return "chat"

def get_system_prompt(query: str) -> str:
    return SYSTEM_PROMPTS[route(query)]

if __name__ == "__main__":
    queries = [
        "Write a Python function for fibonacci",
        "Optimise this SQL query",
        "How are you today?",
    ]
    for q in queries:
        print(f"{q!r:50s} → {route(q)}")
