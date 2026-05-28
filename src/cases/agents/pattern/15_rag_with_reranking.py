"""
15 — RAG with Re-ranking
==========================
Retrieve broadly, then re-rank for precision.
Interview point: Two-stage retrieval (retrieve → re-rank) is standard
  in production RAG systems.
"""

DOCS = [
    "Python lists are ordered, mutable sequences.",
    "Python agents use LLMs as reasoning engines.",
    "A Python decorator is a function that wraps another function.",
    "LLM agents can call external tools and APIs.",
    "List comprehensions provide concise syntax in Python.",
]

def broad_retrieve(query: str, top_k: int = 4) -> list[str]:
    """Stage 1: cast a wide net with keyword matching."""
    q_words = set(query.lower().split())
    scored = [(len(q_words & set(d.lower().split())), d) for d in DOCS]
    scored.sort(reverse=True)
    return [d for _, d in scored[:top_k]]

def rerank(query: str, docs: list[str], top_k: int = 2) -> list[str]:
    """Stage 2: more precise scoring (simulated cross-encoder)."""
    q = query.lower()
    def precision_score(doc):
        d = doc.lower()
        # Reward exact phrase overlap
        return sum(1 for w in q.split() if w in d) * 2 + (
            5 if q[:10] in d else 0
        )
    ranked = sorted(docs, key=precision_score, reverse=True)
    return ranked[:top_k]

if __name__ == "__main__":
    q = "How do LLM agents work?"
    stage1 = broad_retrieve(q)
    print("Stage 1:", stage1)
    stage2 = rerank(q, stage1)
    print("Stage 2:", stage2)
