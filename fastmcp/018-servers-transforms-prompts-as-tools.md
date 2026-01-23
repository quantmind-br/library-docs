---
title: Prompts as Tools - FastMCP
url: https://gofastmcp.com/servers/transforms/prompts-as-tools
source: crawler
fetched_at: 2026-01-22T22:21:44.750000336-03:00
rendered_js: false
word_count: 273
summary: This document explains how to use the PromptsAsTools transform to expose MCP prompts as callable tools for clients that do not natively support the prompt protocol.
tags:
    - fastmcp
    - mcp-server
    - prompts-as-tools
    - python
    - interoperability
    - tool-calling
category: guide
---

New in version `3.0.0` Some MCP clients only support tools. They cannot list or get prompts directly because they lack prompt protocol support. The `PromptsAsTools` transform bridges this gap by generating tools that provide access to your server’s prompts. When you add `PromptsAsTools` to a server, it creates two tools that clients can call instead of using the prompt protocol:

- **`list_prompts`** returns JSON describing all available prompts and their arguments
- **`get_prompt`** renders a specific prompt with provided arguments

This means any client that can call tools can now access prompts, even if the client has no native prompt support.

## Basic Usage

Pass your server to `PromptsAsTools` when adding the transform. The transform queries that server for prompts whenever the generated tools are called.

```
from fastmcp import FastMCP
from fastmcp.server.transforms import PromptsAsTools

mcp = FastMCP("My Server")

@mcp.prompt
def analyze_code(code: str, language: str = "python") -> str:
    """Analyze code for potential issues."""
    return f"Analyze this {language} code:\n{code}"

@mcp.prompt
def explain_concept(concept: str) -> str:
    """Explain a programming concept."""
    return f"Explain: {concept}"

# Add the transform - creates list_prompts and get_prompt tools
mcp.add_transform(PromptsAsTools(mcp))
```

Clients now see three items: whatever tools you defined directly, plus `list_prompts` and `get_prompt`.

## Listing Prompts

The `list_prompts` tool returns JSON with metadata for each prompt, including its arguments.

```
result = await client.call_tool("list_prompts", {})
prompts = json.loads(result.data)
# [
#   {
#     "name": "analyze_code",
#     "description": "Analyze code for potential issues.",
#     "arguments": [
#       {"name": "code", "description": null, "required": true},
#       {"name": "language", "description": null, "required": false}
#     ]
#   },
#   {
#     "name": "explain_concept",
#     "description": "Explain a programming concept.",
#     "arguments": [
#       {"name": "concept", "description": null, "required": true}
#     ]
#   }
#]
```

Each argument includes:

- `name`: The argument name
- `description`: Optional description from type hints or docstrings
- `required`: Whether the argument must be provided

## Getting Prompts

The `get_prompt` tool accepts a prompt name and optional arguments dict. It returns the rendered prompt as JSON with a messages array.

```
# Prompt with required and optional arguments
result = await client.call_tool(
    "get_prompt",
    {
        "name": "analyze_code",
        "arguments": {
            "code": "x = 1\nprint(x)",
            "language": "python"
        }
    }
)

response = json.loads(result.data)
# {
#   "messages": [
#     {
#       "role": "user",
#       "content": "Analyze this python code:\nx = 1\nprint(x)"
#     }
#   ]
# }
```

If a prompt has no arguments, you can omit the `arguments` field or pass an empty dict:

```
result = await client.call_tool(
    "get_prompt",
    {"name": "simple_prompt"}
)
```

## Message Format

Rendered prompts return a messages array following the standard MCP format. Each message includes:

- `role`: The message role (typically “user”, “assistant”, or “system”)
- `content`: The message text content

Multi-message prompts are supported - the array will contain all messages in order.

## Binary Content

Unlike resources, prompts always return text content. There is no binary encoding needed.