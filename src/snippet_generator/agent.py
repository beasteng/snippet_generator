"""Snippet generator agent definition."""
from pydantic_ai import Agent, RunContext

from .config import MODEL_NAME
from .models import SnippetCollection, SnippetGeneratorDeps


# Create the agent
snippet_agent = Agent(
    MODEL_NAME,
    output_type=SnippetCollection,
    deps_type=SnippetGeneratorDeps,
)


# System prompt for the snippet generator
@snippet_agent.system_prompt
def system_prompt_generator(ctx: RunContext[SnippetGeneratorDeps]) -> str:
    """Dynamic system prompt for snippet generation."""
    return f"""
You are a code snippet generator. Generate {ctx.deps.snippet_count} practical, working code snippets for the requested language/library.

Each snippet should:
1. Be self-contained and runnable (or easily adaptable)
2. Include a clear description of what it does
3. List any required dependencies
4. Specify a use case (e.g., 'file I/O', 'API call', 'data processing')
5. Have an appropriate complexity level (beginner, intermediate, advanced)

Distribute complexity across the collection:
- Beginner: first 40% of snippets
- Intermediate: middle 40% of snippets
- Advanced: last 20% of snippets

Focus on common patterns, best practices, and useful utilities that developers actually need.
Make each snippet unique and cover different use cases.
"""
