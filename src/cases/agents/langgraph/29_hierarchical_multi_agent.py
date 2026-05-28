"""Hierarchical agents: top-level routes to team leads, each runs a sub-pipeline."""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


# ── Inner team graphs ──

class TeamState(TypedDict):
    task: str
    result: str

def researcher(state: TeamState):
    return {"result": f"Researched: {state['task']}"}

def writer(state: TeamState):
    return {"result": f"Wrote about: {state['task']}"}

def make_team(worker_fn):
    g = StateGraph(TeamState)
    g.add_node("worker", worker_fn)
    g.add_edge(START, "worker")
    g.add_edge("worker", END)
    return g.compile()

research_team = make_team(researcher)
writing_team = make_team(writer)

# ── Outer orchestrator ──

class OrcState(TypedDict):
    task: str
    category: str
    result: str

def categorize(state: OrcState):
    cat = "research" if "analyze" in state["task"].lower() else "writing"
    return {"category": cat}

def run_research(state: OrcState):
    r = research_team.invoke({"task": state["task"]})
    return {"result": r["result"]}

def run_writing(state: OrcState):
    r = writing_team.invoke({"task": state["task"]})
    return {"result": r["result"]}

def pick(state: OrcState):
    return state["category"]

orc = StateGraph(OrcState)
orc.add_node("categorize", categorize)
orc.add_node("research", run_research)
orc.add_node("writing", run_writing)
orc.add_edge(START, "categorize")
orc.add_conditional_edges("categorize", pick, {"research": "research", "writing": "writing"})
orc.add_edge("research", END)
orc.add_edge("writing", END)

app = orc.compile()
print(app.invoke({"task": "Analyze market trends"}))
print(app.invoke({"task": "Create a blog post"}))
