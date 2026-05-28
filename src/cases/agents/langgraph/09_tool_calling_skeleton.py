"""Tool-calling agent skeleton (no real LLM needed)."""
from typing import Annotated, TypedDict
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages


class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


def model_node(state: State):
    return {"messages": [AIMessage(content="I'll use the search tool.", additional_kwargs={})]}

def tool_node(state: State):
    return {"messages": [ToolMessage(content="tool result: 42", tool_call_id="tc_1")]}


graph = StateGraph(State)
graph.add_node("model", model_node)
graph.add_node("tools", tool_node)
graph.add_edge(START, "model")
graph.add_edge("model", "tools")
graph.add_edge("tools", END)

app = graph.compile()
result = app.invoke({"messages": [HumanMessage(content="What is 6*7?")]})
for m in result["messages"]:
    print(f"  {m.type}: {m.content}")
