"""Agent loop: model → tool → model → … until model stops calling tools."""
from typing import Annotated, TypedDict
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages


class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    tool_calls_remaining: int


def model(state: State):
    n = state.get("tool_calls_remaining", 2)
    if n > 0:
        return {
            "messages": [AIMessage(content=f"Calling tool (remaining={n})")],
            "tool_calls_remaining": n,
        }
    return {
        "messages": [AIMessage(content="Final answer: 42")],
        "tool_calls_remaining": 0,
    }

def tools(state: State):
    return {
        "messages": [ToolMessage(content="tool output", tool_call_id="x")],
        "tool_calls_remaining": state["tool_calls_remaining"] - 1,
    }

def should_continue(state: State):
    return "tools" if state["tool_calls_remaining"] > 0 else "end"


graph = StateGraph(State)
graph.add_node("model", model)
graph.add_node("tools", tools)
graph.add_edge(START, "model")
graph.add_conditional_edges("model", should_continue, {"tools": "tools", "end": END})
graph.add_edge("tools", "model")

app = graph.compile()
result = app.invoke({"messages": [HumanMessage(content="Solve this")], "tool_calls_remaining": 2})
for m in result["messages"]:
    print(f"  {m.type}: {m.content}")
