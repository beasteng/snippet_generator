"""Self-loop: increment counter until threshold reached."""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    count: int


def increment(state: State):
    return {"count": state["count"] + 1}


def should_continue(state: State):
    return "loop" if state["count"] < 5 else "exit"


graph = StateGraph(State)
graph.add_node("increment", increment)
graph.add_edge(START, "increment")
graph.add_conditional_edges(
    "increment", should_continue,
    {"loop": "increment", "exit": END},
)

app = graph.compile()
print(app.invoke({"count": 0}))  # → {"count": 5}
