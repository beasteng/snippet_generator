"""Checkpointer for conversation memory across invocations."""
from typing import Annotated, TypedDict
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver


class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


def bot(state: State):
    count = len(state["messages"])
    return {"messages": [AIMessage(content=f"Reply #{count}")]}


graph = StateGraph(State)
graph.add_node("bot", bot)
graph.add_edge(START, "bot")
graph.add_edge("bot", END)

memory = MemorySaver()
app = graph.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "demo-thread"}}

# Turn 1
r1 = app.invoke({"messages": [HumanMessage(content="Hello")]}, config)
print("Turn 1:", r1["messages"][-1].content)

# Turn 2 — memory carries over
r2 = app.invoke({"messages": [HumanMessage(content="How are you?")]}, config)
print("Turn 2:", r2["messages"][-1].content)
print(f"Total messages in state: {len(r2['messages'])}")
