"""Composing graphs: an inner subgraph is invoked from an outer graph."""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class InnerState(TypedDict):
    text: str

def shout(state: InnerState):
    return {"text": state["text"].upper() + "!!!"}

inner = StateGraph(InnerState)
inner.add_node("shout", shout)
inner.add_edge(START, "shout")
inner.add_edge("shout", END)
inner_app = inner.compile()


class OuterState(TypedDict):
    text: str

def call_inner(state: OuterState):
    result = inner_app.invoke({"text": state["text"]})
    return {"text": result["text"]}

def post_process(state: OuterState):
    return {"text": f"[Processed] {state['text']}"}

outer = StateGraph(OuterState)
outer.add_node("inner", call_inner)
outer.add_node("post", post_process)
outer.add_edge(START, "inner")
outer.add_edge("inner", "post")
outer.add_edge("post", END)

app = outer.compile()
print(app.invoke({"text": "hello"}))
