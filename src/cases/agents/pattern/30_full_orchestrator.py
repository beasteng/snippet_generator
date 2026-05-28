"""
30 — Full Agent Orchestrator
===============================
Combines ALL patterns: routing, planning, parallel tools, RAG,
memory, reflection, guardrails, structured output, and evaluation.

Interview point: This is the architecture of a production agent system.
Each component is modular and independently testable.
"""
from __future__ import annotations
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from enum import Enum, auto
import json

# ── Memory ──────────────────────────────────────────────────
class Memory:
    def __init__(self, max_size: int = 10):
        self.messages: list[dict] = []
        self.summary: str = ""
        self.max_size = max_size

    def add(self, role: str, content: str):
        self.messages.append({"role": role, "content": content})
        if len(self.messages) > self.max_size:
            old = self.messages[:3]
            self.messages = self.messages[3:]
            self.summary += " | " + "; ".join(m["content"][:30] for m in old)

    def context(self) -> list[dict]:
        msgs = []
        if self.summary:
            msgs.append({"role": "system", "content": f"Summary: {self.summary}"})
        return msgs + self.messages

# ── Guardrails ──────────────────────────────────────────────
BLOCKED = {"password", "hack", "exploit"}

def guard_input(query: str) -> bool:
    return not (set(query.lower().split()) & BLOCKED)

def guard_output(text: str) -> str:
    for word in BLOCKED:
        text = text.replace(word, "[REDACTED]")
    return text

# ── Tools ───────────────────────────────────────────────────
def tool_search(query: str) -> str:
    return f"Found: 3 documents about '{query}'"

def tool_calc(expr: str) -> str:
    try:
        return str(eval(expr, {"__builtins__": {}}))
    except Exception as e:
        return f"Error: {e}"

def tool_rag_retrieve(query: str) -> list[str]:
    docs = [
        "Agents use LLMs as reasoning engines.",
        "RAG = Retrieval-Augmented Generation.",
        "Planning breaks problems into sub-tasks.",
    ]
    return [d for d in docs if any(w in d.lower() for w in query.lower().split())]

TOOLS = {"search": tool_search, "calc": tool_calc}

# ── Router ──────────────────────────────────────────────────
class Route(Enum):
    RAG    = auto()
    TOOL   = auto()
    DIRECT = auto()

def route(query: str) -> Route:
    q = query.lower()
    if any(w in q for w in ["what", "how", "explain", "document"]):
        return Route.RAG
    if any(c in q for c in ["+", "-", "*", "/", "calculate"]):
        return Route.TOOL
    return Route.DIRECT

# ── Planner ─────────────────────────────────────────────────
@dataclass
class Plan:
    steps: list[str]

def plan(query: str, route_type: Route) -> Plan:
    if route_type == Route.RAG:
        return Plan(["rewrite_query", "retrieve", "rerank", "generate", "verify"])
    if route_type == Route.TOOL:
        return Plan(["select_tool", "execute", "format_result"])
    return Plan(["generate_direct"])

# ── Structured Output ───────────────────────────────────────
@dataclass
class AgentResponse:
    answer: str
    confidence: float
    sources: list[str] = field(default_factory=list)
    route_used: str = ""
    plan_steps: list[str] = field(default_factory=list)

    def to_json(self) -> str:
        return json.dumps(self.__dict__, indent=2)

# ── Reflection ──────────────────────────────────────────────
def reflect(response: AgentResponse) -> AgentResponse:
    if response.confidence < 0.5:
        response.answer = "[LOW CONFIDENCE] " + response.answer
    if len(response.answer) < 20:
        response.answer += " (Note: response may be too brief)"
    return response

# ── Parallel Execution ──────────────────────────────────────
def parallel_retrieve(query: str) -> list[str]:
    with ThreadPoolExecutor(max_workers=3) as ex:
        futures = [
            ex.submit(tool_rag_retrieve, query),
            ex.submit(tool_search, query),
        ]
        results = []
        for f in futures:
            r = f.result()
            results.extend(r if isinstance(r, list) else [r])
    return results

# ── Main Orchestrator ───────────────────────────────────────
def orchestrate(query: str, memory: Memory) -> AgentResponse:
    # Step 1: Guardrail
    if not guard_input(query):
        return AgentResponse(answer="Query blocked by guardrails.",
                             confidence=1.0, route_used="blocked")

    # Step 2: Route
    r = route(query)
    print(f"  Route: {r.name}")

    # Step 3: Plan
    p = plan(query, r)
    print(f"  Plan: {p.steps}")

    # Step 4: Execute based on route
    if r == Route.RAG:
        docs = parallel_retrieve(query)
        answer = f"Based on {len(docs)} sources: " + "; ".join(docs[:3])
        sources = docs
        confidence = 0.85
    elif r == Route.TOOL:
        result = tool_calc(query.split()[-1]) if "calc" in query.lower() else \
                 tool_search(query)
        answer = f"Tool result: {result}"
        sources = []
        confidence = 0.95
    else:
        answer = f"Direct response to: {query}"
        sources = []
        confidence = 0.7

    # Step 5: Build structured response
    response = AgentResponse(
        answer=answer,
        confidence=confidence,
        sources=sources,
        route_used=r.name,
        plan_steps=p.steps,
    )

    # Step 6: Reflect
    response = reflect(response)

    # Step 7: Output guardrail
    response.answer = guard_output(response.answer)

    # Step 8: Update memory
    memory.add("user", query)
    memory.add("assistant", response.answer)

    return response

# ── Entry Point ─────────────────────────────────────────────
if __name__ == "__main__":
    memory = Memory()
    queries = [
        "How do agents work?",
        "calculate 42 * 7",
        "Hello!",
        "Tell me about hack techniques",  # Should be blocked
    ]
    for q in queries:
        print(f"\n{'='*60}")
        print(f"Query: {q}")
        result = orchestrate(q, memory)
        print(result.to_json())

    print(f"\n{'='*60}")
    print(f"Memory context ({len(memory.messages)} messages):")
    for m in memory.context()[-4:]:
        print(f"  [{m['role']}] {m['content'][:70]}")
