"""Streaming: iterate over node-by-node updates as they happen."""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    text: str

def step_a(state: State):
    return {"text": state["text"] + " → A"}

def step_b(state: State):
    return {"text": state["text"] + " → B"}


graph = StateGraph(State)
graph.add_node("a", step_a)
graph.add_node("b", step_b)
graph.add_edge(START, "a")
graph.add_edge("a", "b")
graph.add_edge("b", END)

app = graph.compile()

print("stream_mode='updates' (default):")
for chunk in app.stream({"text": "START"}):
    print(f"  {chunk}")

print("\nstream_mode='values':")
for snapshot in app.stream({"text": "START"}, stream_mode="values"):
    print(f"  {snapshot}")
