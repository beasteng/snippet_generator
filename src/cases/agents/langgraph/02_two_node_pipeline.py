"""Linear two-step pipeline: strip → uppercase."""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    text: str


def step1(state: State):
    return {"text": state["text"].strip()}


def step2(state: State):
    return {"text": state["text"].upper()}


graph = StateGraph(State)
graph.add_node("strip", step1)
graph.add_node("upper", step2)
graph.add_edge(START, "strip")
graph.add_edge("strip", "upper")
graph.add_edge("upper", END)

app = graph.compile()
print(app.invoke({"text": "  hello world  "}))
