"""Using a callable class as a graph node."""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    text: str
    output: str


class Reverser:
    """Stateful callable — could hold config, caches, etc."""
    def __init__(self, prefix: str = ""):
        self.prefix = prefix

    def __call__(self, state: State):
        return {"output": self.prefix + state["text"][::-1]}


graph = StateGraph(State)
graph.add_node("reverse", Reverser(prefix=">> "))
graph.add_edge(START, "reverse")
graph.add_edge("reverse", END)

app = graph.compile()
print(app.invoke({"text": "LangGraph"}))
