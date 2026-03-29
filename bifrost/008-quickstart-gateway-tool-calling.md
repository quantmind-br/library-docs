---
title: Tool Calling
url: https://docs.getbifrost.ai/quickstart/gateway/tool-calling.md
source: llms
fetched_at: 2026-01-21T19:44:55.513575402-03:00
rendered_js: false
word_count: 221
summary: This document explains how to enable AI models to interact with external services through custom function calling schemas and Model Context Protocol (MCP) server integrations.
tags:
    - tool-calling
    - function-calling
    - mcp-server
    - api-integration
    - model-context-protocol
    - ai-tools
category: guide
---

# Tool Calling

> Enable AI models to use external functions and services by defining tool schemas or connecting to Model Context Protocol (MCP) servers. This allows AI to interact with databases, APIs, file systems, and more.

## Function Calling with Custom Tools

Enable AI models to use external functions by defining tool schemas using OpenAI format. Models can then call these functions automatically based on user requests.

```bash  theme={null}
curl --location 'http://localhost:8080/v1/chat/completions' \
--header 'Content-Type: application/json' \
--data '{
    "model": "openai/gpt-4o-mini",
    "messages": [
        {"role": "user", "content": "What is 15 + 27? Use the calculator tool."}
    ],
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "calculator",
                "description": "A calculator tool for basic arithmetic operations",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "operation": {
                            "type": "string",
                            "description": "The operation to perform",
                            "enum": ["add", "subtract", "multiply", "divide"]
                        },
                        "a": {
                            "type": "number",
                            "description": "The first number"
                        },
                        "b": {
                            "type": "number",
                            "description": "The second number"
                        }
                    },
                    "required": ["operation", "a", "b"]
                }
            }
        }
    ],
    "tool_choice": "auto"
}'
```

**Response includes tool calls:**

```json  theme={null}
{
    "choices": [{
        "message": {
            "role": "assistant", 
            "tool_calls": [{
                "id": "call_abc123",
                "type": "function",
                "function": {
                    "name": "calculator",
                    "arguments": "{\"operation\":\"add\",\"a\":15,\"b\":27}"
                }
            }]
        }
    }]
}
```

## Connecting to MCP Servers

Connect to Model Context Protocol (MCP) servers to give AI models access to external tools and services without manually defining each function.

<Tabs group="tool-calling">
  <Tab title="Using Web UI">
        <img src="https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-mcp-config.png?fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=6e9d5cd353f66dc5943e0bdf819a1f95" alt="MCP Configuration Interface" data-og-width="3492" width="3492" data-og-height="2358" height="2358" data-path="media/ui-mcp-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-mcp-config.png?w=280&fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=919f612a70523b48c79dbafef3c9fb5a 280w, https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-mcp-config.png?w=560&fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=fef915c3f015c80fbf2a0a4edefce968 560w, https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-mcp-config.png?w=840&fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=ca1ef4c6e375c46e370cc2570bf8368a 840w, https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-mcp-config.png?w=1100&fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=6187c8241b5830a5678c4c37bae9c64f 1100w, https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-mcp-config.png?w=1650&fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=ba28fbd66781655c0a3f9dc31e14f799 1650w, https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-mcp-config.png?w=2500&fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=e772de71d89b3d79fb102243cc5cab42 2500w" />

    1. Go to **[http://localhost:8080](http://localhost:8080)**
    2. Navigate to **"MCP Clients"** in the sidebar
    3. Click **"Add MCP Client"**
    4. Enter server details and save
  </Tab>

  <Tab title="Using API">
    ```bash  theme={null}
    curl --location 'http://localhost:8080/api/mcp/client' \
    --header 'Content-Type: application/json' \
    --data '{
        "name": "filesystem",
        "connection_type": "stdio",
        "stdio_config": {
            "command": ["npx", "@modelcontextprotocol/server-filesystem", "/tmp"],
            "args": []
        }
    }'
    ```

    **List configured MCP clients:**

    ```bash  theme={null}
    curl --location 'http://localhost:8080/api/mcp/clients'
    ```
  </Tab>

  <Tab title="Using config.json">
    ```json  theme={null}
    {
        "mcp": {
            "client_configs": [
                {
                    "name": "filesystem",
                    "connection_type": "stdio",
                    "stdio_config": {
                        "command": ["npx", "@modelcontextprotocol/server-filesystem", "/tmp"],
                        "args": []
                    }
                },
                {
                    "name": "youtube-search",
                    "connection_type": "http",
                    "connection_string": "http://your-youtube-mcp-url"
                }
            ]
        }
    }
    ```
  </Tab>
</Tabs>

Read more about MCP connections and advanced end to end tool execution in the [MCP Features](../../mcp/overview) section.

## Tool Choice Options

Control how the AI uses tools:

```bash  theme={null}
# Force use of specific tool
"tool_choice": {
    "type": "function",
    "function": {"name": "calculator"}
}

# Let AI decide automatically (default)
"tool_choice": "auto"

# Disable tool usage
"tool_choice": "none"
```

## Next Steps

Now that you understand tool calling, explore these related topics:

### Essential Topics

* **[Multimodal AI](./multimodal)** - Process images, audio, and multimedia content
* **[Streaming Responses](./streaming)** - Real-time response generation with tool calls
* **[Provider Configuration](./provider-configuration)** - Multiple providers for redundancy
* **[Integrations](./integrations)** - Drop-in compatibility with existing SDKs

### Advanced Topics

* **[MCP Features](../../mcp/overview)** - Advanced MCP server management and configuration
* **[Core Features](../../features/drop-in-replacement)** - Advanced Bifrost capabilities
* **[Architecture](../../architecture/core/request-flow)** - How Bifrost works internally


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt