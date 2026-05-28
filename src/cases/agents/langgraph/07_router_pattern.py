"""Router pattern: classify then dispatch to specialised handler."""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    input: str
    route: str
    output: str


def router(state: State):
    text = state["input"].lower()
    route = "billing" if "invoice" in text else "support"
    return {"route": route}

def billing(state: State):
    return {"output": "Billing team handling: " + state["input"]}

def support(state: State):
    return {"output": "Support team handling: " + state["input"]}

def choose(state: State):
    return state["route"]


graph = StateGraph(State)
graph.add_node("router", router)
graph.add_node("billing", billing)
graph.add_node("support", support)
graph.add_edge(START, "router")
graph.add_conditional_edges("router", choose, {"billing": "billing", "support": "support"})
graph.add_edge("billing", END)
graph.add_edge("support", END)

app = graph.compile()
print(app.invoke({"input": "I need an invoice copy"}))
print(app.invoke({"input": "My app crashed"}))
