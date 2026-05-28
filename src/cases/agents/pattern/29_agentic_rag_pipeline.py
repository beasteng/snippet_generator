"""
29 — Full Agentic RAG Pipeline
=================================
Combines: routing → query rewrite → retrieve → rerank → generate → verify.
Interview point: This is a production-grade RAG pattern.
"""
from dataclasses import dataclass, field

@dataclass
class PipelineState:
    query: str
    rewritten_query: str = ""
    route: str = ""
    retrieved: list[str] = field(default_factory=list)
    reranked: list[str] = field(default_factory=list)
    answer: str = ""
    confidence: float = 0.0

KNOWLEDGE_BASE = [
    "RAG retrieves then generates.",
    "Agents reason with LLMs.",
    "Vector DBs enable semantic search.",
    "Fine-tuning adapts models.",
    "Prompt engineering guides LLMs.",
]

def step_route(state: PipelineState) -> PipelineState:
    state.route = "rag" if any(
        w in state.query.lower() for w in ["what", "how", "explain"]
    ) else "direct"
    return state

def step_rewrite(state: PipelineState) -> PipelineState:
    state.rewritten_query = state.query.replace("?", "").strip() + " overview"
    return state

def step_retrieve(state: PipelineState, top_k: int = 3) -> PipelineState:
    q_words = set(state.rewritten_query.lower().split())
    scored = [(sum(1 for w in q_words if w in d.lower()), d) for d in KNOWLEDGE_BASE]
    scored.sort(reverse=True)
    state.retrieved = [d for _, d in scored[:top_k]]
    return state

def step_rerank(state: PipelineState, top_k: int = 2) -> PipelineState:
    q = state.query.lower()
    state.reranked = sorted(
        state.retrieved,
        key=lambda d: sum(1 for w in q.split() if w in d.lower()),
        reverse=True,
    )[:top_k]
    return state

def step_generate(state: PipelineState) -> PipelineState:
    ctx = " | ".join(state.reranked)
    state.answer = f"Based on [{ctx}]: [LLM-generated answer to '{state.query}']"
    state.confidence = 0.85
    return state

def step_verify(state: PipelineState) -> PipelineState:
    if state.confidence < 0.5:
        state.answer = "I'm not confident enough. " + state.answer
    return state

def run_pipeline(query: str) -> PipelineState:
    state = PipelineState(query=query)
    steps = [step_route, step_rewrite, step_retrieve, step_rerank,
             step_generate, step_verify]
    for step in steps:
        state = step(state)
        print(f"  [{step.__name__}] done")
    return state

if __name__ == "__main__":
    result = run_pipeline("How does RAG work?")
    print(f"\nRoute: {result.route}")
    print(f"Rewritten: {result.rewritten_query}")
    print(f"Retrieved: {result.retrieved}")
    print(f"Reranked: {result.reranked}")
    print(f"Answer: {result.answer}")
    print(f"Confidence: {result.confidence}")
