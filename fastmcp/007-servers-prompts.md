---
title: Prompts - FastMCP
url: https://gofastmcp.com/servers/prompts
source: crawler
fetched_at: 2026-01-22T22:21:55.441920573-03:00
rendered_js: false
word_count: 900
summary: This document explains how to define, customize, and manage reusable message templates in FastMCP using the @mcp.prompt decorator. It covers parameter validation, return types like Message and PromptResult, and argument type handling for structured LLM interactions.
tags:
    - fastmcp
    - mcp-prompts
    - python-sdk
    - prompt-engineering
    - message-templates
    - llm-integration
category: guide
---

Prompts are reusable message templates that help LLMs generate structured, purposeful responses. FastMCP simplifies defining these templates, primarily using the `@mcp.prompt` decorator.

## What Are Prompts?

Prompts provide parameterized message templates for LLMs. When a client requests a prompt:

1. FastMCP finds the corresponding prompt definition.
2. If it has parameters, they are validated against your function signature.
3. Your function executes with the validated inputs.
4. The generated message(s) are returned to the LLM to guide its response.

This allows you to define consistent, reusable templates that LLMs can use across different clients and contexts.

### The `@prompt` Decorator

The most common way to define a prompt is by decorating a Python function. The decorator uses the function name as the prompt’s identifier.

```
from fastmcp import FastMCP
from fastmcp.prompts import Message

mcp = FastMCP(name="PromptServer")

# Basic prompt returning a string (converted to user message automatically)
@mcp.prompt
def ask_about_topic(topic: str) -> str:
    """Generates a user message asking for an explanation of a topic."""
    return f"Can you please explain the concept of '{topic}'?"

# Prompt returning multiple messages
@mcp.prompt
def generate_code_request(language: str, task_description: str) -> list[Message]:
    """Generates a conversation for code generation."""
    return [
        Message(f"Write a {language} function that performs the following task: {task_description}"),
        Message("I'll help you write that function.", role="assistant"),
    ]
```

**Key Concepts:**

- **Name:** By default, the prompt name is taken from the function name.
- **Parameters:** The function parameters define the inputs needed to generate the prompt.
- **Inferred Metadata:** By default:
  
  - Prompt Name: Taken from the function name (`ask_about_topic`).
  - Prompt Description: Taken from the function’s docstring.

#### Decorator Arguments

While FastMCP infers the name and description from your function, you can override these and add additional metadata using arguments to the `@mcp.prompt` decorator:

```
@mcp.prompt(
    name="analyze_data_request",          # Custom prompt name
    description="Creates a request to analyze data with specific parameters",  # Custom description
    tags={"analysis", "data"},            # Optional categorization tags
    meta={"version": "1.1", "author": "data-team"}  # Custom metadata
)
def data_analysis_prompt(
    data_uri: str = Field(description="The URI of the resource containing the data."),
    analysis_type: str = Field(default="summary", description="Type of analysis.")
) -> str:
    """This docstring is ignored when description is provided."""
    return f"Please perform a '{analysis_type}' analysis on the data found at {data_uri}."
```

#### Using with Methods

For decorating instance or class methods, use the standalone `@prompt` decorator and register the bound method. See [Tools: Using with Methods](https://gofastmcp.com/servers/tools#using-with-methods) for the pattern.

### Argument Types

New in version `2.9.0` The MCP specification requires that all prompt arguments be passed as strings, but FastMCP allows you to use typed annotations for better developer experience. When you use complex types like `list[int]` or `dict[str, str]`, FastMCP:

1. **Automatically converts** string arguments from MCP clients to the expected types
2. **Generates helpful descriptions** showing the exact JSON string format needed
3. **Preserves direct usage** - you can still call prompts with properly typed arguments

Since the MCP specification only allows string arguments, clients need to know what string format to use for complex types. FastMCP solves this by automatically enhancing the argument descriptions with JSON schema information, making it clear to both humans and LLMs how to format their arguments.

**MCP clients will call this prompt with string arguments:**

```
{
  "numbers": "[1, 2, 3, 4, 5]",
  "metadata": "{\"source\": \"api\", \"version\": \"1.0\"}",
  "threshold": "2.5"
}
```

**But you can still call it directly with proper types:**

```
# This also works for direct calls
result = await prompt.render({
    "numbers": [1, 2, 3, 4, 5],
    "metadata": {"source": "api", "version": "1.0"},
    "threshold": 2.5
})
```

### Return Values

Prompt functions must return one of these types:

- **`str`** : Sent as a single user message.
- **`list[Message | str]`** : A sequence of messages (a conversation). Strings are auto-converted to user Messages.
- **`PromptResult`** : Full control over messages, description, and metadata. See [PromptResult](#promptresult) below.

```
from fastmcp.prompts import Message

@mcp.prompt
def roleplay_scenario(character: str, situation: str) -> list[Message]:
    """Sets up a roleplaying scenario with initial messages."""
    return [
        Message(f"Let's roleplay. You are {character}. The situation is: {situation}"),
        Message("Okay, I understand. I am ready. What happens next?", role="assistant")
    ]
```

#### Message

New in version `3.0.0` `Message` provides a user-friendly wrapper for prompt messages with automatic serialization.

```
from fastmcp.prompts import Message

# String content (user role by default)
Message("Hello, world!")

# Explicit role
Message("I can help with that.", role="assistant")

# Auto-serialized to JSON text
Message({"key": "value"})
Message(["item1", "item2"])
```

`Message` accepts two fields: **`content`** - The message content. Strings pass through directly. Other types (dict, list, BaseModel) are automatically JSON-serialized to text. **`role`** - The message role, either `"user"` (default) or `"assistant"`.

#### PromptResult

New in version `3.0.0` `PromptResult` gives you explicit control over prompt responses: multiple messages, roles, and metadata at both the message and result level.

````
from fastmcp import FastMCP
from fastmcp.prompts import PromptResult, Message

mcp = FastMCP(name="PromptServer")

@mcp.prompt
def code_review(code: str) -> PromptResult:
    """Returns a code review prompt with metadata."""
    return PromptResult(
        messages=[
            Message(f"Please review this code:\n\n```\n{code}\n```"),
            Message("I'll analyze this code for issues.", role="assistant"),
        ],
        description="Code review prompt",
        meta={"review_type": "security", "priority": "high"}
    )
````

For simple cases, you can pass a string directly to `PromptResult`:

```
return PromptResult("Please help me with this task")  # auto-converts to single Message
```

You can still return plain `str` or `list[Message | str]` from your prompt functions—`PromptResult` is opt-in for when you need to include metadata.

### Required vs. Optional Parameters

Parameters in your function signature are considered **required** unless they have a default value.

```
@mcp.prompt
def data_analysis_prompt(
    data_uri: str,                        # Required - no default value
    analysis_type: str = "summary",       # Optional - has default value
    include_charts: bool = False          # Optional - has default value
) -> str:
    """Creates a request to analyze data with specific parameters."""
    prompt = f"Please perform a '{analysis_type}' analysis on the data found at {data_uri}."
    if include_charts:
        prompt += " Include relevant charts and visualizations."
    return prompt
```

In this example, the client *must* provide `data_uri`. If `analysis_type` or `include_charts` are omitted, their default values will be used.

### Component Visibility

New in version `3.0.0` You can control which prompts are enabled for clients using server-level enabled control. Disabled prompts don’t appear in `list_prompts` and can’t be called.

```
from fastmcp import FastMCP

mcp = FastMCP("MyServer")

@mcp.prompt(tags={"public"})
def public_prompt(topic: str) -> str:
    return f"Discuss: {topic}"

@mcp.prompt(tags={"internal"})
def internal_prompt() -> str:
    return "Internal system prompt"

# Disable specific prompts by key
mcp.disable(keys={"prompt:internal_prompt"})

# Disable prompts by tag
mcp.disable(tags={"internal"})

# Or use allowlist mode - only enable prompts with specific tags
mcp.enable(tags={"public"}, only=True)
```

See [Visibility](https://gofastmcp.com/servers/visibility) for the complete visibility control API including key formats, tag-based filtering, and provider-level control.

### Async Prompts

FastMCP supports both standard (`def`) and asynchronous (`async def`) functions as prompts. Synchronous functions automatically run in a threadpool to avoid blocking the event loop.

```
# Synchronous prompt (runs in threadpool)
@mcp.prompt
def simple_question(question: str) -> str:
    """Generates a simple question to ask the LLM."""
    return f"Question: {question}"

# Asynchronous prompt
@mcp.prompt
async def data_based_prompt(data_id: str) -> str:
    """Generates a prompt based on data that needs to be fetched."""
    # In a real scenario, you might fetch data from a database or API
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.example.com/data/{data_id}") as response:
            data = await response.json()
            return f"Analyze this data: {data['content']}"
```

Use `async def` when your prompt function performs I/O operations like network requests or database queries, since async is more efficient than threadpool dispatch.

### Accessing MCP Context

New in version `2.2.5` Prompts can access additional MCP information and features through the `Context` object. To access it, add a parameter to your prompt function with a type annotation of `Context`:

```
from fastmcp import FastMCP, Context

mcp = FastMCP(name="PromptServer")

@mcp.prompt
async def generate_report_request(report_type: str, ctx: Context) -> str:
    """Generates a request for a report."""
    return f"Please create a {report_type} report. Request ID: {ctx.request_id}"
```

For full documentation on the Context object and all its capabilities, see the [Context documentation](https://gofastmcp.com/servers/context).

### Notifications

New in version `2.9.1` FastMCP automatically sends `notifications/prompts/list_changed` notifications to connected clients when prompts are added, enabled, or disabled. This allows clients to stay up-to-date with the current prompt set without manually polling for changes.

```
@mcp.prompt
def example_prompt() -> str:
    return "Hello!"

# These operations trigger notifications:
mcp.add_prompt(example_prompt)               # Sends prompts/list_changed notification
mcp.disable(keys={"prompt:example_prompt"})  # Sends prompts/list_changed notification
mcp.enable(keys={"prompt:example_prompt"})   # Sends prompts/list_changed notification
```

Notifications are only sent when these operations occur within an active MCP request context (e.g., when called from within a tool or other MCP operation). Operations performed during server initialization do not trigger notifications. Clients can handle these notifications using a [message handler](https://gofastmcp.com/clients/notifications) to automatically refresh their prompt lists or update their interfaces.

## Server Behavior

### Duplicate Prompts

New in version `2.1.0` You can configure how the FastMCP server handles attempts to register multiple prompts with the same name. Use the `on_duplicate_prompts` setting during `FastMCP` initialization.

```
from fastmcp import FastMCP

mcp = FastMCP(
    name="PromptServer",
    on_duplicate_prompts="error"  # Raise an error if a prompt name is duplicated
)

@mcp.prompt
def greeting(): return "Hello, how can I help you today?"

# This registration attempt will raise a ValueError because
# "greeting" is already registered and the behavior is "error".
# @mcp.prompt
# def greeting(): return "Hi there! What can I do for you?"
```

The duplicate behavior options are:

- `"warn"` (default): Logs a warning, and the new prompt replaces the old one.
- `"error"`: Raises a `ValueError`, preventing the duplicate registration.
- `"replace"`: Silently replaces the existing prompt with the new one.
- `"ignore"`: Keeps the original prompt and ignores the new registration attempt.

## Versioning

New in version `3.0.0` Prompts support versioning, allowing you to maintain multiple implementations under the same name while clients automatically receive the highest version. See [Versioning](https://gofastmcp.com/servers/versioning) for complete documentation on version comparison, retrieval, and migration patterns.