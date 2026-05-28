"""Dependency injection: external service used inside a node via closure."""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    query: str
    answer: str


class VectorDB:
    def search(self, q: str) -> str:
        return f"[top-3 docs for '{q}']"


def make_search_node(db: VectorDB):
    def search_node(state: State):
        return {"answer": db.search(state["query"])}
    return search_node


db = VectorDB()

graph = StateGraph(State)
graph.add_node("search", make_search_node(db))
graph.add_edge(START, "search")
graph.add_edge("search", END)

app = graph.compile()
print(app.invoke({"query": "LangGraph patterns"}))
