"""Supervisor pattern: a supervisor routes tasks to specialist agents."""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    task: str
    next_agent: str
    result: str


def supervisor(state: State):
    route = "coder" if "code" in state["task"].lower() else "writer"
    return {"next_agent": route}

def coder(state: State):
    return {"result": f"Coder produced: def solve(): pass  # for '{state['task']}'"}

def writer(state: State):
    return {"result": f"Writer produced: essay about '{state['task']}'"}

def choose(state: State):
    return state["next_agent"]


graph = StateGraph(State)
graph.add_node("supervisor", supervisor)
graph.add_node("coder", coder)
graph.add_node("writer", writer)
graph.add_edge(START, "supervisor")
graph.add_conditional_edges("supervisor", choose, {"coder": "coder", "writer": "writer"})
graph.add_edge("coder", END)
graph.add_edge("writer", END)

app = graph.compile()
print(app.invoke({"task": "Write code to sort a list"}))
print(app.invoke({"task": "Write a poem about AI"}))
