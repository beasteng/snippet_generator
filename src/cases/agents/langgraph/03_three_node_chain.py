"""Three-node chain showing data flowing through multiple transforms."""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    text: str


def normalize(state: State):
    return {"text": state["text"].strip().lower()}

def tokenize(state: State):
    return {"text": str(state["text"].split())}

def count(state: State):
    tokens = eval(state["text"])
    return {"text": f"Token count: {len(tokens)}"}


graph = StateGraph(State)
graph.add_node("normalize", normalize)
graph.add_node("tokenize", tokenize)
graph.add_node("count", count)
graph.add_edge(START, "normalize")
graph.add_edge("normalize", "tokenize")
graph.add_edge("tokenize", "count")
graph.add_edge("count", END)

app = graph.compile()
print(app.invoke({"text": "  Hello World From LangGraph  "}))
