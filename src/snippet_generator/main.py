"""Main entry point for snippet generator."""
import argparse
import asyncio
from pathlib import Path

from .config import SNIPPET_COUNT, OUTPUT_DIR
from .models import SnippetGeneratorDeps, SnippetCollection
from .agent import snippet_agent
from .tools import save_snippet_to_file


async def generate_snippets(
    language: str,
    library: str = "",
    count: int = SNIPPET_COUNT,
    tune_prompt: str = ""
) -> list[str]:
    """Generate multiple code snippets for a language/library in a single call.
    
    Args:
        language: Programming language to generate snippets for
        library: Optional library/framework to focus on
        count: Number of snippets to generate
        tune_prompt: Optional additional prompt to fine-tune generation
        
    Returns:
        List of file paths for generated snippets
    """
    deps = SnippetGeneratorDeps(
        output_dir=str(OUTPUT_DIR),
        snippet_count=count
    )
    
    # Create output directory
    Path(deps.output_dir).mkdir(parents=True, exist_ok=True)
    
    # Build the single prompt for all snippets
    prompt = f"Generate {count} practical code snippets for {language}"
    if library:
        prompt += f" using {library}"
    prompt += ". Make each snippet unique, useful, and well-documented."
    
    if tune_prompt:
        prompt += f" {tune_prompt}"
    
    try:
        result = await snippet_agent.run(prompt, deps=deps)
        
        results = []
        for i, snippet in enumerate(result.output.snippets, 1):
            filepath = save_snippet_to_file(snippet, i, Path(deps.output_dir))
            results.append(str(filepath))
            print(f"Saved snippet {i}/{count} ({snippet.complexity}): {filepath}")
        
        return results
        
    except Exception as e:
        print(f"Error generating snippets: {e}")
        return []


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Generate code snippets for a programming language"
    )
    parser.add_argument(
        "--language",
        "-l",
        required=True,
        help="Programming language to generate snippets for (e.g., python, javascript)"
    )
    parser.add_argument(
        "--library",
        "-lib",
        default="",
        help="Optional library/framework to focus on (e.g., pandas, react)"
    )
    parser.add_argument(
        "--count",
        "-c",
        type=int,
        default=SNIPPET_COUNT,
        help=f"Number of snippets to generate (default: {SNIPPET_COUNT})"
    )
    parser.add_argument(
        "--tune-prompt",
        "-t",
        default="",
        help="Additional prompt to fine-tune snippet generation"
    )
    
    args = parser.parse_args()
    
    print(f"Generating {args.count} snippets for {args.language}" + 
          (f" with {args.library}" if args.library else ""))
    if args.tune_prompt:
        print(f"Tune prompt: {args.tune_prompt}")
    
    results = asyncio.run(generate_snippets(
        language=args.language,
        library=args.library,
        count=args.count,
        tune_prompt=args.tune_prompt
    ))
    
    print(f"\nGenerated {len(results)} snippets in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
