"""
16 — RAG Evaluation Metrics
==============================
Measure retrieval and generation quality.
Interview point: You MUST evaluate RAG; common metrics are
  precision@k, recall@k, and answer faithfulness.
"""

def precision_at_k(retrieved: list[str], relevant: set[str]) -> float:
    if not retrieved:
        return 0.0
    return sum(1 for d in retrieved if d in relevant) / len(retrieved)

def recall_at_k(retrieved: list[str], relevant: set[str]) -> float:
    if not relevant:
        return 0.0
    return sum(1 for d in retrieved if d in relevant) / len(relevant)

def faithfulness_score(answer: str, context: list[str]) -> float:
    """Fraction of answer sentences supported by context (simplified)."""
    ctx_text = " ".join(context).lower()
    sentences = [s.strip() for s in answer.split(".") if s.strip()]
    if not sentences:
        return 0.0
    supported = sum(
        1 for s in sentences
        if any(word in ctx_text for word in s.lower().split() if len(word) > 3)
    )
    return supported / len(sentences)

if __name__ == "__main__":
    retrieved = ["doc_a", "doc_b", "doc_c"]
    relevant = {"doc_a", "doc_c", "doc_d"}
    print(f"Precision@3: {precision_at_k(retrieved, relevant):.2f}")
    print(f"Recall@3:    {recall_at_k(retrieved, relevant):.2f}")

    answer = "Agents use tools. They have memory for context."
    context = ["Agents can use tools and APIs", "Memory stores history"]
    print(f"Faithfulness: {faithfulness_score(answer, context):.2f}")
