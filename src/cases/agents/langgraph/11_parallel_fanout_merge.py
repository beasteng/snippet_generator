"""Fan-out / fan-in: two branches run in parallel then merge."""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    text: str
    lower: str
    upper: str
    result: str


def branch_lower(state: State):
    return {"lower": state["text"].lower()}

def branch_upper(state: State):
    return {"upper": state["text"].upper()}

def merge(state: State):
    return {"result": f"{state['lower']} | {state['upper']}"}


graph = StateGraph(State)
graph.add_node("branch_lower", branch_lower)
graph.add_node("branch_upper", branch_upper)
graph.add_node("merge", merge)
graph.add_edge(START, "branch_lower")
graph.add_edge(START, "branch_upper")
graph.add_edge("branch_lower", "merge")
graph.add_edge("branch_upper", "merge")
graph.add_edge("merge", END)

app = graph.compile()
print(app.invoke({"text": "Hello World"}))
