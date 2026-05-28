"""Minimal single-node graph — the 'Hello World' of LangGraph."""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    greeting: str


def say_hello(state: State):
    return {"greeting": "Hello from LangGraph!"}


graph = StateGraph(State)
graph.add_node("say_hello", say_hello)
graph.add_edge(START, "say_hello")
graph.add_edge("say_hello", END)

app = graph.compile()
print(app.invoke({"greeting": ""}))
