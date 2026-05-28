"""Two agents run in parallel on the same state, then merge."""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    topic: str
    analysis: str
    critique: str
    final: str


def analyst(state: State):
    return {"analysis": f"Deep analysis of '{state['topic']}'"}

def critic(state: State):
    return {"critique": f"Critical review of '{state['topic']}'"}

def synthesize(state: State):
    return {"final": f"SYNTHESIS:\n  {state['analysis']}\n  {state['critique']}"}


graph = StateGraph(State)
graph.add_node("analyst", analyst)
graph.add_node("critic", critic)
graph.add_node("synthesize", synthesize)

# Fan-out from START
graph.add_edge(START, "analyst")
graph.add_edge(START, "critic")

# Fan-in to synthesize
graph.add_edge("analyst", "synthesize")
graph.add_edge("critic", "synthesize")
graph.add_edge("synthesize", END)

app = graph.compile()
result = app.invoke({"topic": "AI Safety"})
print(result["final"])
