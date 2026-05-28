"""Demonstrates the add_messages reducer: messages accumulate, not replace."""
from typing import Annotated, TypedDict
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages


class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


def first_reply(state: State):
    return {"messages": [AIMessage(content="First reply")]}

def second_reply(state: State):
    return {"messages": [AIMessage(content="Second reply")]}


graph = StateGraph(State)
graph.add_node("first", first_reply)
graph.add_node("second", second_reply)
graph.add_edge(START, "first")
graph.add_edge("first", "second")
graph.add_edge("second", END)

app = graph.compile()
result = app.invoke({"messages": [HumanMessage(content="Start")]})
for m in result["messages"]:
    print(f"  {m.type}: {m.content}")
# All 3 messages are kept thanks to the reducer.
