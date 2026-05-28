"""12 — Dependency-Injected Service: inject a database/client via deps."""
from dataclasses import dataclass
from pydantic_ai import Agent, RunContext


class DummyDB:
    def get_user(self, user_id: int) -> str:
        return f"user-{user_id}"


@dataclass
class Deps:
    db: DummyDB


agent = Agent("openai:gpt-4o-mini", deps_type=Deps)


@agent.tool
def lookup_user(ctx: RunContext[Deps], user_id: int) -> str:
    """Look up a user by ID."""
    return ctx.deps.db.get_user(user_id)


print(agent.run_sync("Find user 7.", deps=Deps(db=DummyDB())).output)
