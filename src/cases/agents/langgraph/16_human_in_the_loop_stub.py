"""Human-in-the-loop: simulates pausing for human approval."""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    draft: str
    approved: bool
    final: str


def draft_node(state: State):
    return {"draft": "Proposed: delete all files"}

def human_review(state: State):
    # In production, use an interrupt / checkpoint here.
    print(f"  [HUMAN REVIEW] Draft: {state['draft']}")
    return {"approved": True}  # simulate approval

def execute(state: State):
    return {"final": "Executed!" if state["approved"] else "Blocked."}

def route(state: State):
    return "execute" if state["approved"] else "blocked"


graph = StateGraph(State)
graph.add_node("draft", draft_node)
graph.add_node("review", human_review)
graph.add_node("execute", execute)
graph.add_edge(START, "draft")
graph.add_edge("draft", "review")
graph.add_edge("review", "execute")
graph.add_edge("execute", END)

app = graph.compile()
print(app.invoke({}))
