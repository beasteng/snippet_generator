"""Pydantic models for snippet generator."""
from typing import Literal
from pydantic import BaseModel, Field


class CodeSnippet(BaseModel):
    """Structured representation of a code snippet."""
    
    code: str = Field(..., description="The actual code content")
    language: str = Field(..., description="Programming language (e.g., 'python', 'javascript')")
    description: str = Field(..., description="Brief description of what the snippet does")
    dependencies: list[str] = Field(
        default_factory=list,
        description="List of required dependencies/packages"
    )
    use_case: str = Field(
        ...,
        description="Primary use case or pattern this snippet demonstrates"
    )
    complexity: Literal["beginner", "intermediate", "advanced"] = Field(
        default="beginner",
        description="Complexity level of the snippet"
    )


class SnippetCollection(BaseModel):
    """Collection of code snippets with progressive complexity."""
    
    snippets: list[CodeSnippet] = Field(
        ...,
        description="List of code snippets to generate"
    )


class SnippetGeneratorDeps:
    """Dependencies for the snippet generator agent."""
    
    def __init__(self, output_dir: str, snippet_count: int):
        self.output_dir = output_dir
        self.snippet_count = snippet_count
        self.generated_count: int = 0
