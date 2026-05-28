"""Recursion limit: prevent infinite loops with config."""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    n: int

def step(state: State):
    return {"n": state["n"] + 1}

def route(state: State):
    return "loop" if state["n"] < 100 else "done"  # would loop 100 times

graph = StateGraph(State)
graph.add_node("step", step)
graph.add_edge(START, "step")
graph.add_conditional_edges("step", route, {"loop": "step", "done": END})

app = graph.compile()

# The recursion_limit prevents runaway loops (default is 25).
try:
    print(app.invoke({"n": 0}, {"recursion_limit": 10}))
except Exception as e:
    print(f"Caught: {e}")
