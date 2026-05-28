"""Dynamic dispatch: choose from N handlers at runtime."""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    intent: str
    result: str


HANDLERS = {
    "greet": lambda s: {"result": "Hello! How can I help?"},
    "farewell": lambda s: {"result": "Goodbye!"},
    "unknown": lambda s: {"result": "I don't understand."},
}

def classify(state: State):
    text = state["intent"].lower()
    if "hi" in text or "hello" in text:
        return {"intent": "greet"}
    elif "bye" in text:
        return {"intent": "farewell"}
    return {"intent": "unknown"}

def dispatch(state: State):
    return state["intent"]


graph = StateGraph(State)
graph.add_node("classify", classify)
for name, fn in HANDLERS.items():
    graph.add_node(name, fn)

graph.add_edge(START, "classify")
graph.add_conditional_edges("classify", dispatch, {k: k for k in HANDLERS})
for name in HANDLERS:
    graph.add_edge(name, END)

app = graph.compile()
print(app.invoke({"intent": "Hello there"}))
print(app.invoke({"intent": "bye bye"}))
print(app.invoke({"intent": "asdfgh"}))
