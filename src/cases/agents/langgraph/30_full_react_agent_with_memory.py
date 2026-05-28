"""Full ReAct agent: model ↔ tools loop with memory checkpointer."""
from typing import Annotated, TypedDict
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver


class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    iteration: int


# ── Simulated LLM that calls a tool twice then answers ──

def llm_node(state: AgentState):
    it = state.get("iteration", 0)
    if it < 2:
        return {
            "messages": [AIMessage(
                content="",
                additional_kwargs={"tool_calls": [
                    {"id": f"call_{it}", "function": {"name": "search", "arguments": '{"q":"langgraph"}'}, "type": "function"}
                ]},
            )],
            "iteration": it,
        }
    return {
        "messages": [AIMessage(content="Based on my research: LangGraph is a stateful orchestration framework.")],
        "iteration": it,
    }


def tool_executor(state: AgentState):
    last = state["messages"][-1]
    tool_calls = last.additional_kwargs.get("tool_calls", [])
    results = []
    for tc in tool_calls:
        results.append(ToolMessage(content=f"Result for {tc['function']['name']}", tool_call_id=tc["id"]))
    return {"messages": results, "iteration": state["iteration"] + 1}


def should_continue(state: AgentState):
    last = state["messages"][-1]
    if hasattr(last, "additional_kwargs") and last.additional_kwargs.get("tool_calls"):
        return "tools"
    return "end"


graph = StateGraph(AgentState)
graph.add_node("llm", llm_node)
graph.add_node("tools", tool_executor)
graph.add_edge(START, "llm")
graph.add_conditional_edges("llm", should_continue, {"tools": "tools", "end": END})
graph.add_edge("tools", "llm")

memory = MemorySaver()
app = graph.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "react-demo"}}

# Turn 1
r = app.invoke({"messages": [HumanMessage(content="What is LangGraph?")], "iteration": 0}, config)
print("=== Final answer ===")
print(r["messages"][-1].content)
print(f"Total messages: {len(r['messages'])}")
print(f"Iterations: {r['iteration']}")
