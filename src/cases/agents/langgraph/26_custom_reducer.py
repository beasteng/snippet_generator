"""Custom state reducer: accumulate items in a list across nodes."""
from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END


def list_accumulator(existing: list[str], new: list[str]) -> list[str]:
    return existing + new


class State(TypedDict):
    log: Annotated[list[str], list_accumulator]


def step_a(state: State):
    return {"log": ["step_a executed"]}

def step_b(state: State):
    return {"log": ["step_b executed"]}

def step_c(state: State):
    return {"log": [f"step_c sees {len(state['log'])} prior entries"]}


graph = StateGraph(State)
graph.add_node("a", step_a)
graph.add_node("b", step_b)
graph.add_node("c", step_c)
graph.add_edge(START, "a")
graph.add_edge("a", "b")
graph.add_edge("b", "c")
graph.add_edge("c", END)

app = graph.compile()
result = app.invoke({"log": []})
for entry in result["log"]:
    print(f"  • {entry}")
