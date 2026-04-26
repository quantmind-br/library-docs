---
title: Function Calling | Mistral Docs
url: https://docs.mistral.ai/studio-api/conversations/function-calling
source: sitemap
fetched_at: 2026-04-26T04:12:27.154622569-03:00
rendered_js: false
word_count: 1031
summary: Technical guide on implementing function calling with Mistral models, detailing the five-step process for integrating external tools and APIs into chat completions.
tags:
    - function-calling
    - llm-integration
    - mistral-ai
    - api-development
    - agentic-workflows
    - tool-use
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Function Calling

Connect Mistral models to external local tools, user-defined functions, or APIs to build applications for specific use cases.

> [!note] For chat completions basics, see [Chat Completions](https://docs.mistral.ai/studio-api/conversations/chat-completion).

## Available Models

Function calling capable models include: `mistral-large-latest`, `mistral-medium-latest`, `mistral-small-latest`, `codestral-latest`, and more.

[Full model list](https://docs.mistral.ai/models/overview)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/function_calling/function_calling.ipynb)

## Five-Step Process

1. **Developer:** Specify Functions/Tools and System Prompt
2. **User:** Query the Model with Functions/Tools available
3. **Model:** Generates function arguments if applicable
4. **Developer:** Executes functions to obtain tool results
5. **Model:** Generates answer based on tool results

![Function calling steps](https://docs.mistral.ai/img/fc_steps.png)

## Example: Payment Status Tracking

### Functions and System Definitions

```python
from mistralai.client import MistralClient

client = MistralClient(api_key="your-api-key")

# Define tools
tools = [
    {
        "type": "function",
        "function": {
            "name": "retrieve_payment_status",
            "description": "Retrieve payment status given a transaction ID",
            "parameters": {
                "type": "object",
                "properties": {
                    "transaction_id": {"type": "string", "description": "The transaction ID"}
                },
                "required": ["transaction_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "retrieve_payment_date",
            "description": "Retrieve payment date given a transaction ID",
            "parameters": {
                "type": "object",
                "properties": {
                    "transaction_id": {"type": "string", "description": "The transaction ID"}
                },
                "required": ["transaction_id"]
            }
        }
    }
]

# System prompt
messages = [
    {"role": "system", "content": "You are a payment assistant. Use the available tools to answer user queries."},
    {"role": "user", "content": "What's the status of my transaction T1001?"}
]
```

### Generate Function Arguments

```python
response = client.chat(
    model="mistral-large-latest",
    messages=messages,
    tools=tools
)

tool_calls = response.choices[0].message.tool_calls
```

### Tool Choice Control

| Mode | Description |
|------|-------------|
| `"auto"` | Model decides whether to use tool (default) |
| `"any"` | Forces tool use |
| `"none"` | Prevents tool use |

### Parallel Tool Calls

```python
response = client.chat(
    model="mistral-large-latest",
    messages=messages,
    tools=tools,
    parallel_tool_calls=True  # Allow parallel calls (default: True)
)
```

### Execute Functions

```python
# Extract function name and parameters
function_name = tool_calls[0].function.name
function_params = tool_calls[0].function.arguments

# Execute (simulated)
if function_name == "retrieve_payment_status":
    result = {"status": "Paid"}

# Append result to messages
messages.append({"role": "tool", "tool_call_id": tool_calls[0].id, "content": json.dumps(result)})
```

### Generate Final Answer

```python
final_response = client.chat(
    model="mistral-large-latest",
    messages=messages,
    tools=tools
)

# Response: "The status of your transaction with ID T1001 is Paid."
```

> [!tip] Recursively call the model with new tool calls until it generates a final answer.

## Related

- [Agent Tools](https://docs.mistral.ai/studio-api/agents/agent-tools) — Built-in solutions, MCP, and agentic use cases

#function-calling #llm-integration #mistral-ai #api-development #agentic-workflows #tool-use
