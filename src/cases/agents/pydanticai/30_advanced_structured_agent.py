"""30 — Full-Featured Agent: deps + tools + structured output + validation."""
from dataclasses import dataclass
from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext


# ── Dependencies ──────────────────────────────────────────
@dataclass
class Deps:
    locale: str
    max_items: int


# ── Structured Output ────────────────────────────────────
class SearchItem(BaseModel):
    title: str
    score: float = Field(ge=0, le=1)


class SearchResult(BaseModel):
    query: str
    items: list[SearchItem]


# ── Agent ─────────────────────────────────────────────────
agent = Agent("openai:gpt-4o-mini", deps_type=Deps, result_type=SearchResult)


@agent.system_prompt
def sys(ctx: RunContext[Deps]) -> str:
    return (
        f"Locale: {ctx.deps.locale}. "
        f"Return at most {ctx.deps.max_items} items with relevance scores."
    )


@agent.tool
def normalize_query(ctx: RunContext[Deps], q: str) -> str:
    """Normalize a search query: strip whitespace and lowercase."""
    return q.strip().lower()


@agent.result_validator
def check_item_count(ctx: RunContext[Deps], value: SearchResult) -> SearchResult:
    if len(value.items) > ctx.deps.max_items:
        raise ValueError(
            f"Too many items: {len(value.items)} > {ctx.deps.max_items}"
        )
    return value


# ── Run ───────────────────────────────────────────────────
result = agent.run_sync(
    "Find best Python interview resources.",
    deps=Deps(locale="en-US", max_items=3),
)
print(result.output)
print(f"Items returned: {len(result.output.items)}")
