"""
12 — Embedding-Based RAG
==========================
Cosine similarity with simple TF vectors (no external deps).
Interview point: Real RAG uses dense embeddings; this shows the math.
"""
import math
from collections import Counter

DOCS = [
    "Transformers use self-attention mechanisms.",
    "RAG retrieves documents before generating answers.",
    "Fine-tuning adapts a pre-trained model to a specific task.",
    "Prompt engineering designs inputs to guide LLM behavior.",
]

def tf_vector(text: str) -> Counter:
    return Counter(text.lower().split())

def cosine_sim(a: Counter, b: Counter) -> float:
    common = set(a) & set(b)
    dot = sum(a[w] * b[w] for w in common)
    mag_a = math.sqrt(sum(v**2 for v in a.values()))
    mag_b = math.sqrt(sum(v**2 for v in b.values()))
    return dot / (mag_a * mag_b) if mag_a and mag_b else 0.0

def retrieve(query: str, top_k: int = 2) -> list[tuple[float, str]]:
    qv = tf_vector(query)
    scored = [(cosine_sim(qv, tf_vector(d)), d) for d in DOCS]
    scored.sort(reverse=True)
    return scored[:top_k]

if __name__ == "__main__":
    results = retrieve("How does attention work in transformers?")
    for score, doc in results:
        print(f"  [{score:.3f}] {doc}")
