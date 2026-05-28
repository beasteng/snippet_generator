"""Graceful error handling inside a node."""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    x: int
    result: str
    error: str


def safe_divide(state: State):
    try:
        return {"result": str(100 // state["x"])}
    except ZeroDivisionError as e:
        return {"error": str(e)}


graph = StateGraph(State)
graph.add_node("divide", safe_divide)
graph.add_edge(START, "divide")
graph.add_edge("divide", END)

app = graph.compile()
print("OK: ", app.invoke({"x": 4}))
print("ERR:", app.invoke({"x": 0}))
