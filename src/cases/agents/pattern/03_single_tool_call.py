"""
03 — Single Tool Call
======================
Agent decides whether to use a tool based on the query.
Interview point: Tool use = extending LLM capabilities beyond text.
"""
import datetime

def get_current_time() -> str:
    """Tool: returns current UTC time."""
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def agent(query: str) -> str:
    keywords = ["time", "clock", "hour"]
    if any(k in query.lower() for k in keywords):
        return f"Current time: {get_current_time()}"
    return f"I'll answer directly: {query}"

if __name__ == "__main__":
    print(agent("What time is it?"))
    print(agent("Tell me a joke"))
