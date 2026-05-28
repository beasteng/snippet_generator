"""Tools for snippet generator agent."""
from pathlib import Path
from pydantic_ai import RunContext

from .config import OUTPUT_DIR, LANGUAGE_EXTENSIONS, VALIDATE_SYNTAX
from .models import CodeSnippet, SnippetGeneratorDeps
from .validators import validate_code


def get_file_extension(language: str) -> str:
    """Get file extension for a programming language."""
    return LANGUAGE_EXTENSIONS.get(language.lower(), "txt")


def save_snippet_to_file(snippet: CodeSnippet, index: int, output_dir: Path) -> Path:
    """Save a code snippet to a file.
    
    Args:
        snippet: The code snippet to save
        index: The snippet index (for filename)
        output_dir: Output directory path
        
    Returns:
        Path to the saved file
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    
    ext = get_file_extension(snippet.language)
    filename = f"snippet_{index:02d}_{snippet.language}.{ext}"
    filepath = output_dir / filename
    
    # Add header comment with description
    header = f"# {snippet.description}\n"
    header += f"# Use case: {snippet.use_case}\n"
    header += f"# Complexity: {snippet.complexity}\n"
    if snippet.dependencies:
        header += f"# Dependencies: {', '.join(snippet.dependencies)}\n"
    header += "\n"
    
    # Validate syntax if enabled
    if VALIDATE_SYNTAX:
        is_valid, error = validate_code(snippet.code, snippet.language)
        if not is_valid:
            # Add error comment to file
            header += f"# WARNING: Validation failed - {error}\n\n"
    
    filepath.write_text(header + snippet.code)
    return filepath


async def save_snippet(
    ctx: RunContext[SnippetGeneratorDeps],
    snippet: CodeSnippet,
    index: int
) -> str:
    """Save snippet to file and return filepath.
    
    Args:
        ctx: Run context with dependencies
        snippet: The code snippet to save
        index: The snippet index
        
    Returns:
        Path to the saved file as string
    """
    if VALIDATE_SYNTAX:
        is_valid, error = validate_code(snippet.code, snippet.language)
        if not is_valid:
            return f"Validation failed: {error}"
    
    filepath = save_snippet_to_file(snippet, index, Path(ctx.deps.output_dir))
    return str(filepath)
