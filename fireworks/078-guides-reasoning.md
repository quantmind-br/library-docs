---
title: Reasoning - Fireworks AI Docs
url: https://docs.fireworks.ai/guides/reasoning
source: sitemap
fetched_at: 2026-04-27T20:18:14.49119451-03:00
rendered_js: false
word_count: 400
summary: This document explains how Fireworks models expose their internal reasoning process through a `reasoning_content` field, detailing various ways to access and control this content via the Python SDK, including setting `reasoning_effort` or using Anthropic-compatible `thinking` parameters.
tags:
    - fireworks-models
    - reasoning-content
    - api-usage
    - controlling-effort
    - streaming
    - interleaved-thinking
category: tutorial
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
For thinking/reasoning models, Fireworks exposes the model's internal reasoning through the `reasoning_content` field. This separates the reasoning process (which would otherwise appear in `` tags within `content`) from the final answer.

> [!note]
> Use the [[094-tools-sdks-python-sdk]] for full Fireworks-specific parameter and response field support.

### Prerequisites

Select a reasoning model from the [serverless model library](https://app.fireworks.ai/models/?filter=Serverless).

### Basic usage

```python
from fireworks import Fireworks

client = Fireworks()

completion = client.chat.completions.create(
    messages=[{"role": "user", "content": "What is 25 * 37?"}],
    model="accounts/fireworks/models/<reasoning-model>",
)

for choice in completion.choices:
    if choice.message.reasoning_content:
        print("Reasoning:", choice.message.reasoning_content)
    print("Answer:", choice.message.content)
```

### Controlling reasoning effort

Two parameters control the reasoning token length:

| Parameter | Values | SDK support |
|---|---|---|
| `reasoning_effort` | `"low"`, `"medium"`, `"high"` | Fireworks / OpenAI-compatible |
| `thinking` | `{"type": "enabled", "budget_tokens": 4096}` | Anthropic-compatible |

#### Using `reasoning_effort`

Pass `reasoning_effort` as a top-level or `extra_body` parameter:

```python
completion = client.chat.completions.create(
    messages=[{"role": "user", "content": "Solve step by step: If a train travels at 60 mph for 2.5 hours, how far does it go?"}],
    model="accounts/fireworks/models/<reasoning-model>",
    reasoning_effort="medium",
)
```

#### Using `thinking` (Anthropic-compatible)

```python
completion = client.chat.completions.create(
    messages=[{"role": "user", "content": "Solve step by step: If a train travels at 60 mph for 2.5 hours, how far does it go?"}],
    model="accounts/fireworks/models/<reasoning-model>",
    thinking={"type": "enabled", "budget_tokens": 4096},  # Must be >= 1024
)
```

See the [`reasoning_effort`](https://docs.fireworks.ai/api-reference/post-chatcompletions) and [`thinking`](https://docs.fireworks.ai/api-reference/post-chatcompletions) parameter references for full details.

### Streaming with reasoning content

Reasoning content is available in each chunk's delta when streaming:

```python
from fireworks import Fireworks

client = Fireworks()

stream = client.chat.completions.create(
    messages=[{"role": "user", "content": "What is the square root of 144?"}],
    model="accounts/fireworks/models/<reasoning-model>",
    reasoning_effort="medium",
    stream=True,
)

reasoning_parts = []
content_parts = []

for chunk in stream:
    delta = chunk.choices[0].delta
    if delta.reasoning_content:
        reasoning_parts.append(delta.reasoning_content)
    if delta.content:
        content_parts.append(delta.content)

print("Reasoning:", "".join(reasoning_parts))
print("Answer:", "".join(content_parts))
```

### Interleaved thinking

When building multi-turn tool-calling agents with models that support interleaved thinking, **you must include the `reasoning_content` from previous assistant turns in subsequent requests**. This allows the model to think between tool calls and after receiving tool results.

Two ways to preserve reasoning context:

1. **Pass the `Message` object directly** (recommended) — the SDK message object already contains `reasoning_content` alongside `content` and `tool_calls`
2. **Manually include `reasoning_content`** — when constructing messages as dictionaries, explicitly add the `reasoning_content` field

> [!warning]
> Forgetting to include `reasoning_content` in multi-turn conversations breaks the model's interleaved thinking capability.

```python
# First turn: Get a response with reasoning_content
first_response = client.chat.completions.create(
    messages=[{"role": "user", "content": "What is 15 + 27?"}],
    model="accounts/fireworks/models/<reasoning-model>",
    tools=tools,
)

assistant_message = first_response.choices[0].message
# assistant_message.reasoning_content -> "The user is asking for addition..."
# assistant_message.tool_calls -> [ToolCall(id="...", function=...)]

# Second turn: Pass the Message object directly
# This automatically includes reasoning_content alongside the message
second_response = client.chat.completions.create(
    messages=[
        {"role": "user", "content": "What is 15 + 27?"},
        assistant_message,  # Pass the complete Message object
        {"role": "tool", "content": "42", "tool_call_id": assistant_message.tool_calls[0].id},
    ],
    model="accounts/fireworks/models/<reasoning-model>",
    tools=tools,
)
```

```python
# First turn: Get a response with reasoning_content
first_response = client.chat.completions.create(
    messages=[{"role": "user", "content": "What is 15 + 27?"}],
    model="accounts/fireworks/models/<reasoning-model>",
    tools=tools,
)

assistant_message = first_response.choices[0].message

# Second turn: Manually construct the assistant message dict
# Include reasoning_content explicitly alongside role, content, and tool_calls
second_response = client.chat.completions.create(
    messages=[
        {"role": "user", "content": "What is 15 + 27?"},
        {
            "role": "assistant",
            "content": assistant_message.content,
            "reasoning_content": assistant_message.reasoning_content,  # Include reasoning
            "tool_calls": assistant_message.tool_calls,
        },
        {"role": "tool", "content": "42", "tool_call_id": assistant_message.tool_calls[0].id},
    ],
    model="accounts/fireworks/models/<reasoning-model>",
    tools=tools,
)
```

The Anthropic SDK uses `thinking` content blocks instead of `reasoning_content`. Pass the full `content` array (including thinking blocks) back as the assistant message, and send tool results as `tool_result` content blocks:

```python
import anthropic

client = anthropic.Anthropic(
    api_key=os.environ.get("FIREWORKS_API_KEY"),
    base_url="https://api.fireworks.ai/inference",
)

tools = [
    {
        "name": "calculator",
        "description": "Perform basic arithmetic operations",
        "input_schema": {
            "type": "object",
            "properties": {
                "operation": {"type": "string", "enum": ["add", "subtract", "multiply", "divide"]},
                "a": {"type": "number"},
                "b": {"type": "number"},
            },
            "required": ["operation", "a", "b"],
        },
    }
]

# First turn: thinking + tool_use
first_response = client.messages.create(
    model="accounts/fireworks/models/<reasoning-model>",
    max_tokens=16000,
    thinking={"type": "enabled", "budget_tokens": 4096},
    messages=[{"role": "user", "content": "What is 15 + 27? Use the calculator."}],
    tools=tools,
)

# Response content includes [thinking_block, tool_use_block]
for block in first_response.content:
    if block.type == "thinking":
        print(f"Thinking: {block.thinking[:100]}...")
    elif block.type == "tool_use":
        print(f"Tool: {block.name}({block.input})")

tool_use = next(b for b in first_response.content if b.type == "tool_use")

# Second turn: pass back the full content array (with thinking blocks) + tool result
second_response = client.messages.create(
    model="accounts/fireworks/models/<reasoning-model>",
    max_tokens=16000,
    thinking={"type": "enabled", "budget_tokens": 4096},
    messages=[
        {"role": "user", "content": "What is 15 + 27? Use the calculator."},
        {"role": "assistant", "content": first_response.content},
        {"role": "user", "content": [{"type": "tool_result", "tool_use_id": tool_use.id, "content": "42"}]},
    ],
    tools=tools,
)

# The model thinks again (interleaved) and produces a text answer
for block in second_response.content:
    if block.type == "thinking":
        print(f"Thinking: {block.thinking[:100]}...")
    elif block.type == "text":
        print(f"Answer: {block.text}")
```

The following script validates that `reasoning_content` from the first turn is included in subsequent requests:

```python
"""Test that reasoning_content is passed in multi-turn conversations.

This test proves that reasoning_content from previous turns is included
in subsequent requests by examining the raw prompt sent to the model.
"""

from fireworks import Fireworks
from dotenv import load_dotenv

load_dotenv()

client = Fireworks()

MODEL = "accounts/fireworks/models/kimi-k2-thinking"

# Define tools to enable interleaved thinking
tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Perform basic arithmetic operations",
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": ["add", "subtract", "multiply", "divide"],
                    },
                    "a": {"type": "number"},
                    "b": {"type": "number"},
                },
                "required": ["operation", "a", "b"],
            },
        },
    }
]


def print_header(title: str, char: str = "═", width: int = 60):
    """Print a formatted section header."""
    print(f"\n{char * width}")
    print(f"  {title}")
    print(f"{char * width}")


def print_field(label: str, value: str, indent: int = 2):
    """Print a labeled field with optional indentation."""
    prefix = " " * indent
    print(f"{prefix}{label}: {value}")


def print_multiline(label: str, content: str, max_preview: int = 200, indent: int = 2):
    """Print multiline content with a label and optional truncation."""
    prefix = " " * indent
    print(f"{prefix}{label}:")
    preview = content[:max_preview] + "..." if len(content) > max_preview else content
    for line in preview.split("\n"):
        print(f"{prefix}  │ {line}")


# First turn - get a response with reasoning_content
print_header("FIRST TURN", "═")
first_response = client.chat.completions.create(
    messages=[{"role": "user", "content": "What is 15 + 27?"}],
    model=MODEL,
    tools=tools,
)

print_field("📝 Content", first_response.choices[0].message.content or "(none)")

reasoning = first_response.choices[0].message.reasoning_content
print_multiline("💭 Reasoning", reasoning)

# Print tool call (verified) from the first response
tool_calls = first_response.choices[0].message.tool_calls
assert tool_calls, "No tool calls in first response!"
print(f"\n  🔧 Tool Calls ({len(tool_calls)}):")
for i, tc in enumerate(tool_calls, 1):
    print(f"    [{i}] id={tc.id}")
    print(f"        function={tc.function.name}")
    print(f"        arguments={tc.function.arguments}")
tool_call_id = first_response.choices[0].message.tool_calls[0].id

# Verify we got reasoning_content
assert reasoning and len(reasoning) > 0, "No reasoning_content in first response!"
print("\n  ✓ First response has reasoning_content")

# Second turn - include the first assistant message
print_header("SECOND TURN", "═")
second_response = client.chat.completions.create(
    messages=[
        {"role": "user", "content": "What is 15 + 27?"},
        first_response.choices[0].message,  # Includes reasoning_content
        {"role": "tool", "content": "42", "tool_call_id": tool_call_id},
    ],
    model=MODEL,
    tools=tools,
    raw_output=True,
)

print_field("📝 Answer", second_response.choices[0].message.content or "(none)")

# Extract and display the raw prompt that was sent to the model
raw_prompt = second_response.choices[0].raw_output.prompt_fragments[0]
print_header("RAW PROMPT SENT TO MODEL", "─")
print(raw_prompt)

# Check if reasoning_content from first turn is in the raw prompt
has_reasoning_content = reasoning[:50] in raw_prompt

print_header("RESULT", "═")
if has_reasoning_content:
    print("  ✅ SUCCESS: reasoning_content IS included in subsequent requests!")
else:
    print("  ❌ FAILED: reasoning_content not found in raw prompt")
print()
```

> [!example]
> Expected output shows `reasoning_content` from the first turn appearing in `<|assistant|>` tags within the raw prompt sent to the model for the second turn.

### Preserved thinking

**Preserved thinking** extends interleaved thinking across multiple user turns, retaining reasoning content from previous assistant turns in the conversation context for more coherent multi-turn reasoning.

#### Controlling reasoning history

Use the [`reasoning_history`](https://docs.fireworks.ai/api-reference/post-chatcompletions) parameter to control how historical reasoning is included:

```python
completion = client.chat.completions.create(
    messages=[
        {"role": "user", "content": "What is 15 + 27?"},
        assistant_message,  # Contains reasoning_content from previous turn
        {"role": "user", "content": "Now multiply that by 2"},
    ],
    model="accounts/fireworks/models/<reasoning-model>",
    reasoning_history="preserved",  # Retain all previous reasoning content
)
```

See the [`reasoning_history`](https://docs.fireworks.ai/api-reference/post-chatcompletions) parameter reference for all accepted values.

The following script demonstrates preserved thinking across multiple turns:

```python
"""Test that reasoning_content is passed in multi-turn conversations.

This test proves that reasoning_content from previous turns is included
in subsequent requests by examining the raw prompt sent to the model.
"""

from fireworks import Fireworks
from dotenv import load_dotenv

load_dotenv()

client = Fireworks()

MODEL = "accounts/fireworks/models/glm-4p7"


# Define tools to enable interleaved thinking
tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Perform basic arithmetic operations",
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": ["add", "subtract", "multiply", "divide"],
                    },
                    "a": {"type": "number"},
                    "b": {"type": "number"},
                },
                "required": ["operation", "a", "b"],
            },
        },
    }
]


def print_header(title: str, char: str = "═", width: int = 60):
    """Print a formatted section header."""
    print(f"\n{char * width}")
    print(f"  {title}")
    print(f"{char * width}")


def print_field(label: str, value: str, indent: int = 2):
    """Print a labeled field with optional indentation."""
    prefix = " " * indent
    print(f"{prefix}{label}: {value}")


def print_multiline(label: str, content: str, max_preview: int = 200, indent: int = 2):
    """Print multiline content with a label and optional truncation."""
    prefix = " " * indent
    print(f"{prefix}{label}:")
    preview = content[:max_preview] + "..." if len(content) > max_preview else content
    for line in preview.split("\n"):
        print(f"{prefix}  │ {line}")


# First turn - get a response with reasoning_content
print_header("FIRST TURN", "═")
first_response = client.chat.completions.create(
    messages=[{"role": "user", "content": "What is 15 + 27?"}],
    model=MODEL,
    tools=tools,
)

print_field("📝 Content", first_response.choices[0].message.content or "(none)")

reasoning = first_response.choices[0].message.reasoning_content
print_multiline("💭 Reasoning", reasoning)

# Print tool call (verified) from the first response
tool_calls = first_response.choices[0].message.tool_calls
assert tool_calls, "No tool calls in first response!"
print(f"\n  🔧 Tool Calls ({len(tool_calls)}):")
for i, tc in enumerate(tool_calls, 1):
    print(f"    [{i}] id={tc.id}")
    print(f"        function={tc.function.name}")
    print(f"        arguments={tc.function.arguments}")
tool_call_id = first_response.choices[0].message.tool_calls[0].id

# Verify we got reasoning_content
assert reasoning and len(reasoning) > 0, "No reasoning_content in first response!"
print("\n  ✓ First response has reasoning_content")

# Second turn - include the first assistant message
print_header("SECOND TURN", "═")
second_response = client.chat.completions.create(
    messages=[
        {"role": "user", "content": "What is 15 + 27?"},
        first_response.choices[0].message,  # Includes reasoning_content
        {"role": "tool", "content": "42", "tool_call_id": tool_call_id},
    ],
    model=MODEL,
    tools=tools,
    raw_output=True,
)

print_field("📝 Answer", second_response.choices[0].message.content or "(none)")

# Extract and display the raw prompt that was sent to the model
raw_prompt = second_response.choices[0].raw_output.prompt_fragments[0]
print_header("RAW PROMPT SENT TO MODEL", "─")
print(raw_prompt)

# Check if reasoning_content from first turn is in the raw prompt
has_reasoning_content = reasoning[:50] in raw_prompt

print_header("RESULT", "═")
if has_reasoning_content:
    print("  ✅ SUCCESS: reasoning_content IS included in subsequent requests!")
else:
    print("  ❌ FAILED: reasoning_content not found in raw prompt")
print()

# Third turn - ask for another calculation
print_header("THIRD TURN", "═")
third_response = client.chat.completions.create(
    messages=[
        {"role": "user", "content": "What is 15 + 27?"},
        first_response.choices[0].message,  # Includes reasoning_content
        {"role": "tool", "content": "42", "tool_call_id": tool_call_id},
        {"role": "user", "content": "What is 20 * 5?"},
    ],
    model=MODEL,
    tools=tools,
)

print_field("📝 Answer", third_response.choices[0].message.content or "(none)")

reasoning_third = third_response.choices[0].message.reasoning_content
print_multiline("💭 Reasoning", reasoning_third)

# Print tool call from the third response
tool_calls_third = third_response.choices[0].message.tool_calls
assert tool_calls_third, "No tool calls in third response!"
print(f"\n  🔧 Tool Calls ({len(tool_calls_third)}):")
for i, tc in enumerate(tool_calls_third, 1):
    print(f"    [{i}] id={tc.id}")
    print(f"        function={tc.function.name}")
    print(f"        arguments={tc.function.arguments}")
tool_call_id_third = third_response.choices[0].message.tool_calls[0].id
print()

# Fourth turn - include the third assistant message and tool response
print_header("FOURTH TURN", "═")
fourth_response = client.chat.completions.create(
    messages=[
        {"role": "user", "content": "What is 15 + 27?"},
        first_response.choices[0].message,  # Includes reasoning_content
        {"role": "tool", "content": "42", "tool_call_id": tool_call_id},
        {"role": "user", "content": "What is 20 * 5?"},
        third_response.choices[0].message,  # Includes reasoning_content from third turn
        {"role": "tool", "content": "100", "tool_call_id": tool_call_id_third},
    ],
    model=MODEL,
    tools=tools,
    raw_output=True,
    reasoning_history="preserved",
)

print_field("📝 Answer", fourth_response.choices[0].message.content or "(none)")

# Extract and display the raw prompt that was sent to the model
raw_prompt_fourth = fourth_response.choices[0].raw_output.prompt_fragments[0]
print_header("RAW PROMPT SENT TO MODEL (FOURTH TURN)", "─")
print(raw_prompt_fourth)

# Check if reasoning_content from both first and third turns are in the raw prompt
has_reasoning_content_first = reasoning[:50] in raw_prompt_fourth
has_reasoning_content_third = reasoning_third[:50] in raw_prompt_fourth

print_header("RESULT (FOURTH TURN)", "═")
if has_reasoning_content_first and has_reasoning_content_third:
    print("  ✅ SUCCESS: reasoning_content from both first and third turns IS included in fourth turn requests!")
elif has_reasoning_content_first:
    print("  ⚠️  PARTIAL: Only first turn reasoning_content found in raw prompt")
elif has_reasoning_content_third:
    print("  ⚠️  PARTIAL: Only third turn reasoning_content found in raw prompt")
else:
    print("  ❌ FAILED: reasoning_content not found in raw prompt")
print()
```

> [!example]
> Expected output for the fourth turn shows both `reasoning_content` strings (from turns 1 and 3) present in the raw prompt, confirming `reasoning_history="preserved"` works across multiple user turns.
