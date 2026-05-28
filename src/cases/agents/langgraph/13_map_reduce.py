"""Map-reduce pattern: process items then summarize."""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    items: list[str]
    mapped: list[str]
    summary: str


def map_step(state: State):
    return {"mapped": [item.upper() for item in state["items"]]}

def reduce_step(state: State):
    return {"summary": " + ".join(state["mapped"])}


graph = StateGraph(State)
graph.add_node("map", map_step)
graph.add_node("reduce", reduce_step)
graph.add_edge(START, "map")
graph.add_edge("map", "reduce")
graph.add_edge("reduce", END)

app = graph.compile()
print(app.invoke({"items": ["alpha", "beta", "gamma"]}))
