"""
24 — Agent Handoff Pattern
=============================
One agent passes context to the next.
Interview point: Handoff = passing state/context between
  specialised agents in a pipeline.
"""
from dataclasses import dataclass, field

@dataclass
class AgentContext:
    query: str
    history: list[str] = field(default_factory=list)
    data: dict = field(default_factory=dict)

def classifier_agent(ctx: AgentContext) -> AgentContext:
    ctx.data["category"] = "technical"
    ctx.history.append("classifier: categorized as technical")
    return ctx

def retriever_agent(ctx: AgentContext) -> AgentContext:
    ctx.data["documents"] = ["doc1: Agents overview", "doc2: RAG patterns"]
    ctx.history.append(f"retriever: found {len(ctx.data['documents'])} docs")
    return ctx

def generator_agent(ctx: AgentContext) -> AgentContext:
    docs = ctx.data.get("documents", [])
    ctx.data["answer"] = f"Based on {len(docs)} documents: [generated answer]"
    ctx.history.append("generator: produced answer")
    return ctx

def run_pipeline(query: str) -> AgentContext:
    ctx = AgentContext(query=query)
    for agent in [classifier_agent, retriever_agent, generator_agent]:
        ctx = agent(ctx)
        print(f"  → {ctx.history[-1]}")
    return ctx

if __name__ == "__main__":
    result = run_pipeline("Explain how agents use tools")
    print(f"\nFinal answer: {result.data['answer']}")
    print(f"Pipeline trace: {result.history}")
