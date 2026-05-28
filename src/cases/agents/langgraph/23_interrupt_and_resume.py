"""Interrupt before a node, then resume with human input (using checkpointer)."""
from typing import Annotated, TypedDict
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver


class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


def assistant(state: State):
    return {"messages": [AIMessage(content="I need to call a dangerous tool. Approve?")]}

def execute_tool(state: State):
    return {"messages": [AIMessage(content="Tool executed successfully.")]}


graph = StateGraph(State)
graph.add_node("assistant", assistant)
graph.add_node("execute", execute_tool)
graph.add_edge(START, "assistant")
graph.add_edge("assistant", "execute")
graph.add_edge("execute", END)

memory = MemorySaver()
app = graph.compile(checkpointer=memory, interrupt_before=["execute"])

config = {"configurable": {"thread_id": "interrupt-demo"}}

# First invocation stops before 'execute'
result = app.invoke({"messages": [HumanMessage(content="Do the thing")]}, config)
print("Paused. Last msg:", result["messages"][-1].content)

# Resume (human approved) — invoke with None to continue
result = app.invoke(None, config)
print("Resumed. Last msg:", result["messages"][-1].content)
