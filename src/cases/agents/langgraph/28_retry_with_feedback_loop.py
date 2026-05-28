"""Retry loop: if quality check fails, regenerate with feedback (max 3 tries)."""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    draft: str
    feedback: str
    attempts: int
    accepted: bool


def generate(state: State):
    attempt = state.get("attempts", 0) + 1
    fb = state.get("feedback", "")
    draft = f"Draft v{attempt}"
    if fb:
        draft += f" (incorporating: {fb})"
    return {"draft": draft, "attempts": attempt}

def quality_check(state: State):
    # Accept on 3rd attempt
    ok = state["attempts"] >= 3
    feedback = "" if ok else f"Needs more detail (attempt {state['attempts']})"
    return {"accepted": ok, "feedback": feedback}

def route(state: State):
    if state["accepted"]:
        return "accept"
    return "retry" if state["attempts"] < 3 else "accept"


graph = StateGraph(State)
graph.add_node("generate", generate)
graph.add_node("check", quality_check)
graph.add_edge(START, "generate")
graph.add_edge("generate", "check")
graph.add_conditional_edges("check", route, {"retry": "generate", "accept": END})

app = graph.compile()
result = app.invoke({"draft": "", "feedback": "", "attempts": 0, "accepted": False})
print(f"Final: {result['draft']} (attempts: {result['attempts']})")
