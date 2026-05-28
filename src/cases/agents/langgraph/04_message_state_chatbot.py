"""Basic chatbot using the built-in message list reducer."""
from typing import Annotated, TypedDict
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages


class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


def chatbot(state: State):
    last = state["messages"][-1].content
    return {"messages": [AIMessage(content=f"Echo: {last}")]}


graph = StateGraph(State)
graph.add_node("chatbot", chatbot)
graph.add_edge(START, "chatbot")
graph.add_edge("chatbot", END)

app = graph.compile()
result = app.invoke({"messages": [HumanMessage(content="Hi there!")]})
for m in result["messages"]:
    print(f"{m.type}: {m.content}")
