"""
11 — Simple RAG (Retrieve-then-Generate)
==========================================
Keyword-based retrieval + answer generation.
Interview point: RAG = Retrieval-Augmented Generation.
  Step 1: Retrieve relevant context.  Step 2: Generate using that context.
"""

KNOWLEDGE_BASE = [
    "Python was created by Guido van Rossum in 1991.",
    "RAG combines a retriever with a language model generator.",
    "Agents can use tools, memory, and planning to solve tasks.",
    "Vector databases store embeddings for semantic search.",
]

def retrieve(query: str, top_k: int = 2) -> list[str]:
    """Naive keyword overlap scoring."""
    def score(doc):
        return sum(1 for w in query.lower().split() if w in doc.lower())
    ranked = sorted(KNOWLEDGE_BASE, key=score, reverse=True)
    return ranked[:top_k]

def generate(query: str, context: list[str]) -> str:
    ctx = "\n".join(f"- {c}" for c in context)
    return f"Context:\n{ctx}\n\nAnswer for '{query}': [LLM would generate here]"

if __name__ == "__main__":
    q = "How does RAG work?"
    docs = retrieve(q)
    print(generate(q, docs))
