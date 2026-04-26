---
title: Function Calling | Mistral Docs
url: https://docs.mistral.ai/studio-api/agents/agent-tools/function-calling
source: sitemap
fetched_at: 2026-04-26T04:11:52.572548371-03:00
rendered_js: false
word_count: 219
summary: Configure and use tool calling and external connectors within agents to interact with custom functions and workflows.
tags:
    - agent-tools
    - function-calling
    - mcp-servers
    - api-integration
    - tool-execution
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Function Calling

The core of an agent relies on tool usage capabilities, enabling it to call tools and workflows depending on the task.

## Built-in Tools

Mistral provides built-in tools via the API: `websearch`, `code_interpreter`, `image_generation`, and `document_library`.

## Custom Function Calling

Define a JSON schema for your function to use standard function tool calling.

## External Tools via MCP

Register MCP servers as [Connectors](https://docs.mistral.ai/studio-api/knowledge-rag/connectors) to use external tools in conversations and Agents.

For more on function calling, see the [function calling docs](https://docs.mistral.ai/studio-api/conversations/function-calling).

## Usage

Create an Agent with function calling or use the Conversations API directly.

### 1. Define Your Function

```python
def get_payment_status(transaction_id: str) -> str:
    """Retrieve payment status for a transaction."""
    # Your implementation
    return '{"status": "Paid"}'
```

### 2. Define the Schema

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_payment_status",
            "description": "Retrieve payment status for a transaction ID",
            "parameters": {
                "type": "object",
                "properties": {
                    "transaction_id": {
                        "type": "string",
                        "description": "The transaction identifier"
                    }
                },
                "required": ["transaction_id"]
            }
        }
    }
]
```

### 3. Create Agent and Chat

```python
agent = client.agents.create(
    model="mistral-large-latest",
    tools=tools
)

response = client.agents.chat(
    agent_id=agent.id,
    inputs="What's the status of my transaction T1001?"
)
```

The model outputs either an answer or a function call. Detect and return the function result.

#agent-tools #function-calling #mcp-servers #api-integration #tool-execution
