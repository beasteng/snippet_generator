"""Snippet generator package."""
from .config import SNIPPET_COUNT, OUTPUT_DIR, MODEL_NAME
from .models import CodeSnippet, SnippetCollection, SnippetGeneratorDeps
from .agent import snippet_agent
from .main import generate_snippets, main

__all__ = [
    "SNIPPET_COUNT",
    "OUTPUT_DIR",
    "MODEL_NAME",
    "CodeSnippet",
    "SnippetCollection",
    "SnippetGeneratorDeps",
    "snippet_agent",
    "generate_snippets",
    "main",
]
