"""
25 — OpenAI Function Calling Schema
======================================
Define tools as JSON schemas for the OpenAI API.
Interview point: Function calling is how modern LLMs invoke tools
  in a structured, reliable way.
"""
import json

TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "City name"},
                    "units": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "default": "celsius",
                    },
                },
                "required": ["city"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_docs",
            "description": "Search internal documentation",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                    "top_k": {"type": "integer", "default": 3},
                },
                "required": ["query"],
            },
        },
    },
]

def execute_tool_call(name: str, arguments: dict) -> str:
    """Dispatch a tool call from the LLM."""
    if name == "get_weather":
        return json.dumps({"temp": 22, "condition": "sunny",
                           "city": arguments["city"]})
    if name == "search_docs":
        return json.dumps({"results": [f"doc about {arguments['query']}"]})
    return json.dumps({"error": f"Unknown tool: {name}"})

if __name__ == "__main__":
    # Simulate what the LLM returns
    tool_call = {"name": "get_weather", "arguments": {"city": "London"}}
    result = execute_tool_call(tool_call["name"], tool_call["arguments"])
    print(f"Tool: {tool_call['name']}")
    print(f"Args: {tool_call['arguments']}")
    print(f"Result: {result}")
    print(f"\nSchemas sent to API: {json.dumps(TOOL_SCHEMAS, indent=2)[:200]}...")
