"""Configuration settings for snippet generator."""
from pathlib import Path

# Number of snippets to generate
SNIPPET_COUNT: int = 30

# Output directory for generated snippets
OUTPUT_DIR: Path = Path("output/snippets")

# LLM model to use
MODEL_NAME: str = "openai:gpt-4o-mini"

# Whether to validate code syntax
VALIDATE_SYNTAX: bool = True

# File extension mapping for languages
LANGUAGE_EXTENSIONS: dict[str, str] = {
    "python": "py",
    "javascript": "js",
    "typescript": "ts",
    "java": "java",
    "csharp": "cs",
    "cpp": "cpp",
    "c": "c",
    "go": "go",
    "rust": "rs",
    "ruby": "rb",
    "php": "php",
    "swift": "swift",
    "kotlin": "kt",
    "scala": "scala",
    "r": "r",
    "sql": "sql",
    "bash": "sh",
    "html": "html",
    "css": "css",
}
