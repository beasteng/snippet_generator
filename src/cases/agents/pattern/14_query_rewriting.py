"""
14 — Query Rewriting for RAG
===============================
Transform ambiguous queries into better retrieval queries.
Interview point: "How does it work?" is useless for retrieval;
  rewriting adds context from conversation history.
"""

def rewrite_with_history(query: str, history: list[str]) -> str:
    """Replace pronouns/vague refs using recent history."""
    if not history:
        return query
    recent = history[-1]
    replacements = {
        "it": f"'{recent}'",
        "this": f"'{recent}'",
        "that": f"'{recent}'",
    }
    result = query
    for pronoun, replacement in replacements.items():
        result = result.replace(f" {pronoun} ", f" {replacement} ")
        if result.lower().endswith(f" {pronoun}"):
            result = result[:-len(pronoun)] + replacement
    return result

def multi_query_expansion(query: str) -> list[str]:
    """Generate multiple search queries for better recall."""
    return [
        query,
        f"{query} definition",
        f"{query} example",
        f"how does {query} work",
    ]

if __name__ == "__main__":
    history = ["vector databases"]
    print(rewrite_with_history("How does it work?", history))
    print(multi_query_expansion("RAG pipeline"))
