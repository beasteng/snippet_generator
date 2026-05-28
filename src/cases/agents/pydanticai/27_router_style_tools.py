"""27 — Router-Style Tools: multiple tools simulate API endpoints."""
from pydantic_ai import Agent, RunContext

agent = Agent("openai:gpt-4o-mini")


@agent.tool
def create_ticket(ctx: RunContext[None], title: str) -> str:
    """Create a support ticket and return its ID."""
    return f"TICK-{abs(hash(title)) % 10000}"


@agent.tool
def close_ticket(ctx: RunContext[None], ticket_id: str) -> str:
    """Close a support ticket by ID."""
    return f"Closed: {ticket_id}"


print(agent.run_sync("Create a ticket for 'login bug', then close it.").output)
