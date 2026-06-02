# ADR: PydanticAI Language Code Snippet Generator Architecture

## Status

Accepted

## Context

We need to build a tool that generates code snippets for any programming language and/or library. The system must:
- Generate 30 (configurable) snippets per run
- Output each snippet as a separate file with structured metadata
- Ensure code quality through validation
- Provide a CLI interface for user input

The key architectural decision is how to structure the generation pipeline: whether to generate snippets one at a time or in a single batch, and how to handle validation, file output, and configuration.

## Decision

We will use a **single-call batch generation** architecture with the following components:

### 1. Single LLM Call for All Snippets

All snippets are generated in a **single LLM call** using PydanticAI's `Agent` with `output_type=SnippetCollection`. The agent returns a structured list of `CodeSnippet` objects in one response.

**Rationale:**
- Efficiency: One LLM call instead of N calls reduces latency and cost
- Consistency: The LLM sees the full context and can distribute complexity levels (40% beginner, 40% intermediate, 20% advanced) across the collection
- Simplicity: No need for orchestration loops or state management between calls

### 2. Pydantic Models for Structured Output

We define two core models:
- `CodeSnippet`: Contains `code`, `language`, `description`, `dependencies`, `use_case`, and `complexity`
- `SnippetCollection`: Wraps a `list[CodeSnippet]` as the agent's output type

**Rationale:**
- Type safety and validation through Pydantic
- Clear contract between the LLM and the application
- Easy serialization and file output

### 3. Configuration Module

All tunable parameters are centralized in `config.py`:
- `SNIPPET_COUNT`: Number of snippets (default: 30)
- `OUTPUT_DIR`: Output directory (default: `output/snippets`)
- `MODEL_NAME`: LLM model (default: `openai:gpt-4o-mini`)
- `VALIDATE_SYNTAX`: Whether to validate code syntax (default: `True`)
- `LANGUAGE_EXTENSIONS`: Mapping of language names to file extensions

**Rationale:**
- Single source of truth for configuration
- Easy to override via environment or code
- Supports future expansion (e.g., loading from YAML/TOML)

### 4. File Output Tool

The `save_snippet_to_file` function handles:
- Creating output directories
- Generating filenames (`snippet_{index:02d}_{language}.{ext}`)
- Adding header comments with metadata (description, use case, complexity, dependencies)
- Optional syntax validation with warning comments

**Rationale:**
- Separation of concerns: file I/O is isolated from agent logic
- Reusable utility that can be called from both the main loop and agent tools
- Validation feedback is preserved in the output file

### 5. CLI Interface

The `main.py` provides an `argparse`-based CLI with arguments:
- `--language` / `-l`: Required programming language
- `--library` / `-lib`: Optional library/framework
- `--count` / `-c`: Number of snippets (default: 30)
- `--tune-prompt` / `-t`: Additional prompt for fine-tuning

**Rationale:**
- Standard Python CLI pattern
- Easy to integrate into scripts and CI/CD
- Clear help messages for discoverability

### 6. Validation Strategy

Syntax validation is performed using language-specific parsers in `validators.py`. Currently supports Python and JavaScript, with extensible design for additional languages.

**Rationale:**
- Catches obvious errors before users copy-paste snippets
- Non-blocking: validation warnings are added to files rather than failing the entire run
- Extensible: new validators can be added without changing core logic

## Consequences

### Positive
- **Fast generation**: Single LLM call means low latency
- **Consistent output**: Structured Pydantic models ensure predictable file format
- **Configurable**: Easy to adjust count, output directory, and model
- **Validated**: Syntax checking improves snippet quality
- **Extensible**: New languages and validators can be added modularly

### Negative
- **Single point of failure**: If the LLM call fails, no snippets are generated (no partial output)
- **Token limits**: Very large snippet counts may hit LLM context limits
- **Validation coverage**: Only Python and JavaScript validators are implemented initially

### Mitigations
- Error handling in `main.py` catches exceptions and reports failures
- `SNIPPET_COUNT` can be reduced if context limits are hit
- Validator module is designed for easy extension

## Alternatives Considered

### Alternative 1: One-Call-Per-Snippet Loop
Generate each snippet in a separate LLM call with a loop in the orchestration code.

**Rejected because:**
- N LLM calls instead of 1 increases latency and cost proportionally
- Harder to maintain consistent complexity distribution
- More complex error handling (partial failures)

### Alternative 2: Template-Based Generation
Use predefined templates for common patterns instead of LLM generation.

**Rejected because:**
- Limited flexibility for arbitrary languages/libraries
- Requires maintaining template library
- Less adaptable to user-specific `tune-prompt` requirements

### Alternative 3: Multi-Agent Pipeline
Use multiple specialized agents (e.g., one for beginner, one for advanced snippets).

**Rejected because:**
- Over-engineering for the current requirements
- Increases complexity and cost
- Single agent with complexity distribution guidance is sufficient

## References

- [PRD: PydanticAI Language Code Snippet Generator](../PRD/PRD_snippet_generator.md)
- [PydanticAI Documentation](https://ai.pydantic.dev/)
