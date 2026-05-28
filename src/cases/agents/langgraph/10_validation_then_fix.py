"""Validate → fix loop: if input too short, pad it, otherwise pass through."""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    text: str
    valid: bool


def validate(state: State):
    return {"valid": len(state["text"]) >= 5}

def fix(state: State):
    return {"text": state["text"].ljust(5, "_")}

def route(state: State):
    return "ok" if state["valid"] else "fix"


graph = StateGraph(State)
graph.add_node("validate", validate)
graph.add_node("fix", fix)
graph.add_edge(START, "validate")
graph.add_conditional_edges("validate", route, {"ok": END, "fix": "fix"})
graph.add_edge("fix", END)

app = graph.compile()
print(app.invoke({"text": "ab"}))   # gets fixed
print(app.invoke({"text": "hello"}))  # passes through
