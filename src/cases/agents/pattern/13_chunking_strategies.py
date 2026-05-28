"""
13 — Text Chunking Strategies
================================
Fixed-size, sentence-based, and overlapping chunks.
Interview point: Chunk size and overlap directly affect retrieval quality.
"""

def fixed_chunks(text: str, size: int = 100, overlap: int = 20) -> list[str]:
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start + size])
        start += size - overlap
    return chunks

def sentence_chunks(text: str, max_sentences: int = 3) -> list[str]:
    import re
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [
        " ".join(sentences[i:i + max_sentences])
        for i in range(0, len(sentences), max_sentences)
    ]

if __name__ == "__main__":
    text = (
        "Agents use tools to interact with the world. "
        "RAG retrieves relevant documents. "
        "Memory stores conversation history. "
        "Planning breaks tasks into steps. "
        "Evaluation checks output quality."
    )
    print("=== Fixed chunks (size=60, overlap=10) ===")
    for c in fixed_chunks(text, 60, 10):
        print(f"  [{len(c):3d}] {c!r}")
    print("\n=== Sentence chunks (max=2) ===")
    for c in sentence_chunks(text, 2):
        print(f"  {c!r}")
