"""Conditional branching: route to 'short' or 'long' path based on input length."""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    text: str
    route: str


def classify(state: State):
    return {"route": "short" if len(state["text"]) < 10 else "long"}

def short_path(state: State):
    return {"text": f"SHORT: {state['text']}"}

def long_path(state: State):
    return {"text": f"LONG: {state['text']}"}

def pick_route(state: State):
    return state["route"]


graph = StateGraph(State)
graph.add_node("classify", classify)
graph.add_node("short_path", short_path)
graph.add_node("long_path", long_path)
graph.add_edge(START, "classify")
graph.add_conditional_edges(
    "classify", pick_route,
    {"short": "short_path", "long": "long_path"},
)
graph.add_edge("short_path", END)
graph.add_edge("long_path", END)

app = graph.compile()
print(app.invoke({"text": "hello world foo bar"}))
print(app.invoke({"text": "hi"}))
