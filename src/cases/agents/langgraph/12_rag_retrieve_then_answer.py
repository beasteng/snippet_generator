"""RAG pattern: retrieve context then generate answer."""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    query: str
    context: str
    answer: str


def retrieve(state: State):
    # Simulated retrieval
    return {"context": f"[Retrieved docs about: {state['query']}]"}

def generate(state: State):
    return {"answer": f"Based on {state['context']}, the answer is 42."}


graph = StateGraph(State)
graph.add_node("retrieve", retrieve)
graph.add_node("generate", generate)
graph.add_edge(START, "retrieve")
graph.add_edge("retrieve", "generate")
graph.add_edge("generate", END)

app = graph.compile()
print(app.invoke({"query": "What is LangGraph?"}))
