---
title: User Elicitation - FastMCP
url: https://gofastmcp.com/clients/elicitation
source: crawler
fetched_at: 2026-01-22T22:23:00.972739747-03:00
rendered_js: false
word_count: 177
summary: This document explains how to implement elicitation in FastMCP to handle interactive user input requests from servers during tool execution. It details the setup of elicitation handlers, available response actions, and the automatic conversion of JSON schemas to Python dataclasses.
tags:
    - fastmcp
    - mcp-protocol
    - user-elicitation
    - python-sdk
    - interactive-tools
    - input-handling
category: guide
---

New in version `2.10.0` Use this when you need to respond to server requests for user input during tool execution. Elicitation allows MCP servers to request structured input from users during operations. Instead of requiring all inputs upfront, servers can interactively ask for missing parameters, request clarification, or gather additional context.

## Handler Template

```
from fastmcp import Client
from fastmcp.client.elicitation import ElicitResult, ElicitRequestParams, RequestContext

async def elicitation_handler(
    message: str,
    response_type: type | None,
    params: ElicitRequestParams,
    context: RequestContext
) -> ElicitResult | object:
    """
    Handle server requests for user input.

    Args:
        message: The prompt to display to the user
        response_type: Python dataclass type for the response (None if no data expected)
        params: Original MCP elicitation parameters including raw JSON schema
        context: Request context with metadata

    Returns:
        - Data directly (implicitly accepts the elicitation)
        - ElicitResult for explicit control over the action
    """
    # Present the message and collect input
    user_input = input(f"{message}: ")

    if not user_input:
        return ElicitResult(action="decline")

    # Create response using the provided dataclass type
    return response_type(value=user_input)

client = Client(
    "my_mcp_server.py",
    elicitation_handler=elicitation_handler,
)
```

## How It Works

When a server needs user input, it sends an elicitation request with a message prompt and a JSON schema describing the expected response structure. FastMCP automatically converts this schema into a Python dataclass type, making it easy to construct properly typed responses without manually parsing JSON schemas. The handler receives four parameters:

## Response Actions

You can return data directly, which implicitly accepts the elicitation:

```
async def elicitation_handler(message, response_type, params, context):
    user_input = input(f"{message}: ")
    return response_type(value=user_input)  # Implicit accept
```

Or return an `ElicitResult` for explicit control over the action:

```
from fastmcp.client.elicitation import ElicitResult

async def elicitation_handler(message, response_type, params, context):
    user_input = input(f"{message}: ")

    if not user_input:
        return ElicitResult(action="decline")  # User declined

    if user_input == "cancel":
        return ElicitResult(action="cancel")   # Cancel entire operation

    return ElicitResult(
        action="accept",
        content=response_type(value=user_input)
    )
```

**Action types:**

- **`accept`** : User provided valid input. Include the data in the `content` field.
- **`decline`** : User chose not to provide the requested information. Omit `content`.
- **`cancel`** : User cancelled the entire operation. Omit `content`.

## Example

A file management tool might ask which directory to create:

```
from fastmcp import Client
from fastmcp.client.elicitation import ElicitResult

async def elicitation_handler(message, response_type, params, context):
    print(f"Server asks: {message}")

    user_response = input("Your response: ")

    if not user_response:
        return ElicitResult(action="decline")

    # Use the response_type dataclass to create a properly structured response
    return response_type(value=user_response)

client = Client(
    "my_mcp_server.py",
    elicitation_handler=elicitation_handler
)
```