"""
26 — Map-Reduce RAG
=====================
Process chunks independently (map), then combine (reduce).
Interview point: Map-reduce handles documents that are too large
  for a single context window.
"""
from concurrent.futures import ThreadPoolExecutor

CHUNKS = [
    "Chapter 1: Agents perceive their environment and take actions.",
    "Chapter 2: Tools extend agent capabilities beyond language.",
    "Chapter 3: Memory allows agents to maintain state across turns.",
    "Chapter 4: Planning helps agents break complex tasks into steps.",
]

def map_summarize(chunk: str) -> str:
    """Summarize a single chunk (would call LLM in production)."""
    words = chunk.split()
    return " ".join(words[:5]) + "..."

def reduce_combine(summaries: list[str], query: str) -> str:
    """Combine chunk summaries into a final answer."""
    combined = " | ".join(summaries)
    return f"Final answer for '{query}' based on {len(summaries)} chunks: {combined}"

def map_reduce_rag(query: str) -> str:
    # Map phase (parallel)
    with ThreadPoolExecutor() as ex:
        summaries = list(ex.map(map_summarize, CHUNKS))

    print("Map results:")
    for i, s in enumerate(summaries):
        print(f"  Chunk {i}: {s}")

    # Reduce phase
    return reduce_combine(summaries, query)

if __name__ == "__main__":
    print(map_reduce_rag("What are the key components of agents?"))
