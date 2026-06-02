# Snippet Generator

A PydanticAI-based agentic pipeline that generates code snippets for a specified programming language and/or library. The system generates 30 (configurable) snippets, one per file, with structured output and validation.

## Features

- Generate 30 code snippets per run (configurable)
- Support any programming language and library
- Output each snippet as a separate file with metadata headers
- Syntax validation for generated code
- Structured metadata (description, dependencies, use case, complexity)
- CLI interface for easy usage

## Installation

```bash
pip install -r src/snippet_generator/requirements.txt
```

## Requirements

- Python 3.10+
- An API key for your chosen LLM provider (OpenAI, Anthropic, or a local LLM server)

## Usage

### OpenAI (GPT) Users

Set your OpenAI API key and use the default model:

```bash
export OPENAI_API_KEY="your-openai-api-key"

# Generate 30 Python snippets
python -m src.snippet_generator.main --language python

# Generate 10 JavaScript snippets with React
python -m src.snippet_generator.main --language javascript --library react --count 10
```

To use a different OpenAI model, edit [`src/snippet_generator/config.py`](src/snippet_generator/config.py) and set `MODEL_NAME` to e.g. `openai:gpt-4o`.

### Claude (Opus) Users

Set your Anthropic API key and update the model in config:

```bash
export ANTHROPIC_API_KEY="your-anthropic-api-key"
```

Edit [`src/snippet_generator/config.py`](src/snippet_generator/config.py):
```python
MODEL_NAME = "anthropic:claude-3-5-sonnet-20240620"
```

Then run:
```bash
python -m src.snippet_generator.main --language python
```

### Local LLM Users

If you are running a local LLM server (e.g., Ollama, LM Studio, or llama.cpp server), configure the endpoint:

Edit [`src/snippet_generator/config.py`](src/snippet_generator/config.py):
```python
MODEL_NAME = "ollama:llama3.1"
```

Or for a generic OpenAI-compatible local server:
```python
MODEL_NAME = "openai:gpt-4o-mini"
# And set the base URL via environment variable if needed
```

Then run:
```bash
python -m src.snippet_generator.main --language python
```

### Generate snippets with custom tuning

```bash
python -m src.snippet_generator.main --language python --tune-prompt "focus on data processing patterns"
```

### CLI Arguments

| Argument | Short | Required | Default | Description |
|----------|-------|----------|---------|-------------|
| `--language` | `-l` | Yes | - | Programming language |
| `--library` | `-lib` | No | "" | Library/framework to use |
| `--count` | `-c` | No | 30 | Number of snippets |
| `--tune-prompt` | `-t` | No | "" | Additional prompt to fine-tune generation |

## Output

Snippets are saved to `output/snippets/` with the naming convention:

```
output/snippets/
├── snippet_01_python.py
├── snippet_02_python.py
└── ...
```

Each file includes a header comment with:
- Description
- Use case
- Complexity level
- Dependencies (if any)

## Configuration

Edit [`src/snippet_generator/config.py`](src/snippet_generator/config.py) to change defaults:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `SNIPPET_COUNT` | 30 | Number of snippets to generate |
| `OUTPUT_DIR` | `output/snippets` | Directory for output files |
| `MODEL_NAME` | `openai:gpt-4o-mini` | LLM model to use |
| `VALIDATE_SYNTAX` | `true` | Whether to validate code syntax |

## Architecture

The system uses a **single-call batch generation** approach:
1. User provides language/library via CLI
2. A single LLM call generates all snippets as a `SnippetCollection`
3. Each snippet is validated and saved to a file with metadata

See [`docs/ARD/ADR_snippet_generator.md`](docs/ARD/ADR_snippet_generator.md) for the full architecture decision record.

## Project Structure

```
src/snippet_generator/
├── __init__.py         # Package exports
├── config.py           # Configuration settings
├── models.py           # Pydantic models
├── agent.py            # Agent definition
├── tools.py            # File output tools
├── main.py             # Entry point
├── validators.py       # Code validation utilities
└── requirements.txt    # Python dependencies
```

## License

See [LICENSE](LICENSE) file for details.
