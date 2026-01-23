---
title: Connecting to MCP Servers
url: https://docs.getbifrost.ai/mcp/connecting-to-servers.md
source: llms
fetched_at: 2026-01-21T19:44:06.904082338-03:00
rendered_js: false
word_count: 651
summary: This document explains how to connect Bifrost to external MCP servers using STDIO, HTTP, and SSE protocols to discover and execute tools. It provides detailed setup instructions for both the Web UI and API, including configuration parameters and management of discovered tools.
tags:
    - mcp-server
    - connection-protocols
    - bifrost-gateway
    - stdio-connection
    - http-integration
    - sse-streaming
    - tool-discovery
    - api-configuration
category: guide
---

# Connecting to MCP Servers

> Connect Bifrost to external MCP servers via STDIO, HTTP, or SSE protocols.

## Overview

Bifrost can connect to any MCP-compatible server to discover and execute tools. Each connection is called an **MCP Client** in Bifrost terminology.

## Connection Types

Bifrost supports three connection protocols:

| Type      | Description                                           | Best For                                    |
| --------- | ----------------------------------------------------- | ------------------------------------------- |
| **STDIO** | Spawns a subprocess and communicates via stdin/stdout | Local tools, CLI utilities, scripts         |
| **HTTP**  | Sends requests to an HTTP endpoint                    | Remote APIs, microservices, cloud functions |
| **SSE**   | Server-Sent Events for persistent connections         | Real-time data, streaming tools             |

### STDIO Connections

STDIO connections launch external processes and communicate via standard input/output. Best for local tools and scripts.

```json  theme={null}
{
  "name": "filesystem",
  "connection_type": "stdio",
  "stdio_config": {
    "command": "npx",
    "args": ["-y", "@anthropic/mcp-filesystem"],
    "envs": ["HOME", "PATH"]
  },
  "tools_to_execute": ["*"]
}
```

**Use Cases:**

* Local filesystem operations
* Python/Node.js MCP servers
* CLI utilities and scripts
* Database tools with local credentials

<Warning>
  **Docker Users:** When running Bifrost in Docker, STDIO connections may not work if the required commands (e.g., `npx`, `python`) are not installed in the container. For STDIO-based MCP servers, build a custom Docker image that includes the necessary dependencies, or use HTTP/SSE connections to externally hosted MCP servers.
</Warning>

### HTTP Connections

HTTP connections communicate with MCP servers via HTTP requests. Ideal for remote services and microservices.

```json  theme={null}
{
  "name": "web-search",
  "connection_type": "http",
  "connection_string": "https://mcp-server.example.com/mcp",
  "headers": {
    "Authorization": "Bearer your-api-key",
    "X-Custom-Header": "value"
  },
  "tools_to_execute": ["*"]
}
```

**Use Cases:**

* Remote API integrations
* Cloud-hosted MCP services
* Microservice architectures
* Third-party tool providers

### SSE Connections

Server-Sent Events (SSE) connections provide real-time, persistent connections to MCP servers.

```json  theme={null}
{
  "name": "live-data",
  "connection_type": "sse",
  "connection_string": "https://stream.example.com/mcp/sse",
  "headers": {
    "Authorization": "Bearer your-api-key"
  },
  "tools_to_execute": ["*"]
}
```

**Use Cases:**

* Real-time market data
* Live system monitoring
* Event-driven workflows

***

## Gateway Setup

<Tabs>
  <Tab title="Web UI">
    ### Adding an MCP Client

    1. Navigate to **MCP Gateway** in the sidebar - you'll see a table of all registered servers

    <Frame>
      <img src="https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-mcp-servers-table.png?fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=acc11a832be51d34ea562844ed995101" alt="MCP Servers Table" data-og-width="3492" width="3492" data-og-height="2358" height="2358" data-path="media/ui-mcp-servers-table.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-mcp-servers-table.png?w=280&fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=c6c365cbe803c3789851899f700a18c0 280w, https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-mcp-servers-table.png?w=560&fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=9cba4da9383b12b63a5ece50d369f02c 560w, https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-mcp-servers-table.png?w=840&fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=331fe67fc0c75e5c1c5e1b7257112c74 840w, https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-mcp-servers-table.png?w=1100&fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=4f5af8e607540002b435673de50f4f34 1100w, https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-mcp-servers-table.png?w=1650&fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=b24514143ce34f31002420367b75c028 1650w, https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-mcp-servers-table.png?w=2500&fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=26235882ee830601d06dc62bb296ac6f 2500w" />
    </Frame>

    2. Click **New MCP Server** button to open the creation form

    3. Fill in the connection details:

    <Frame>
      <img src="https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-mcp-new-server.png?fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=0158ff55a228d790c9d77432269a1c2f" alt="Add MCP Client Form" data-og-width="3492" width="3492" data-og-height="2358" height="2358" data-path="media/ui-mcp-new-server.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-mcp-new-server.png?w=280&fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=a6782472147a977ea879947d7a0181fa 280w, https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-mcp-new-server.png?w=560&fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=e2fdbb1c1ca42c6215bf347d6d533cd8 560w, https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-mcp-new-server.png?w=840&fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=df504448f0bacc6543f2a333501cb1f2 840w, https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-mcp-new-server.png?w=1100&fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=3c90fdc62694cf2315b5eb8b9dc38d64 1100w, https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-mcp-new-server.png?w=1650&fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=9fb7e55de3caf4065c45fdbfcee2e210 1650w, https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-mcp-new-server.png?w=2500&fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=eb71b7d958041b133a27e00ae8990708 2500w" />
    </Frame>

    **Fields:**

    * **Name**: Unique identifier (no spaces or hyphens, ASCII only)
    * **Connection Type**: STDIO, HTTP, or SSE
    * **For STDIO**: Command, arguments, and environment variables
    * **For HTTP/SSE**: Connection URL

    4. Click **Create** to connect

    ### Viewing and Managing Connected Tools

    Once connected, click on any client row to open the configuration sheet:

    <Frame>
      <img src="https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-mcp-tool-config.png?fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=e8897d79c05c622c8bee14f56fae51b5" alt="MCP Client Configuration and Tools" data-og-width="3492" width="3492" data-og-height="2358" height="2358" data-path="media/ui-mcp-tool-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-mcp-tool-config.png?w=280&fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=95ddf8683a91b31c4993ed323e433633 280w, https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-mcp-tool-config.png?w=560&fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=13c7ff5aba7f67126de3363482199b7b 560w, https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-mcp-tool-config.png?w=840&fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=e26f440884ddf7c3323c56ac45a83f50 840w, https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-mcp-tool-config.png?w=1100&fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=d4b1cebe62d6123c2795a8df6926b1ee 1100w, https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-mcp-tool-config.png?w=1650&fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=159527dd0b6ce429fb4f76536e4a6e2c 1650w, https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-mcp-tool-config.png?w=2500&fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=979dc60e870c55c7aab87ac11e63a684 2500w" />
    </Frame>

    Here you can:

    * View all discovered tools with their descriptions and parameters
    * Enable/disable individual tools via toggle switches
    * Configure auto-execution for specific tools
    * Edit custom headers for HTTP/SSE connections
    * View the full connection configuration as JSON
  </Tab>

  <Tab title="API">
    ### Add STDIO Client

    ```bash  theme={null}
    curl -X POST http://localhost:8080/api/mcp/client \
      -H "Content-Type: application/json" \
      -d '{
        "name": "filesystem",
        "connection_type": "stdio",
        "stdio_config": {
          "command": "npx",
          "args": ["-y", "@anthropic/mcp-filesystem"],
          "envs": ["HOME", "PATH"]
        },
        "tools_to_execute": ["*"]
      }'
    ```

    ### Add HTTP Client

    ```bash  theme={null}
    curl -X POST http://localhost:8080/api/mcp/client \
      -H "Content-Type: application/json" \
      -d '{
        "name": "web_search",
        "connection_type": "http",
        "connection_string": "http://localhost:3001/mcp",
        "tools_to_execute": ["*"]
      }'
    ```

    ### Add SSE Client

    ```bash  theme={null}
    curl -X POST http://localhost:8080/api/mcp/client \
      -H "Content-Type: application/json" \
      -d '{
        "name": "realtime_data",
        "connection_type": "sse",
        "connection_string": "https://api.example.com/mcp/sse",
        "tools_to_execute": ["*"]
      }'
    ```

    ### List All Clients

    ```bash  theme={null}
    curl http://localhost:8080/api/mcp/clients
    ```

    Response:

    ```json  theme={null}
    [
      {
        "config": {
          "id": "abc123",
          "name": "filesystem",
          "connection_type": "stdio",
          "stdio_config": {
            "command": "npx",
            "args": ["-y", "@anthropic/mcp-filesystem"]
          }
        },
        "tools": [
          {"name": "read_file", "description": "Read contents of a file"},
          {"name": "write_file", "description": "Write contents to a file"},
          {"name": "list_directory", "description": "List directory contents"}
        ],
        "state": "connected"
      }
    ]
    ```
  </Tab>

  <Tab title="config.json">
    Configure MCP clients in your `config.json`:

    ```json  theme={null}
    {
      "mcp": {
        "client_configs": [
          {
            "name": "filesystem",
            "connection_type": "stdio",
            "stdio_config": {
              "command": "npx",
              "args": ["-y", "@anthropic/mcp-filesystem"],
              "envs": ["HOME", "PATH"]
            },
            "tools_to_execute": ["*"]
          },
          {
            "name": "web_search",
            "connection_type": "http",
            "connection_string": "env.WEB_SEARCH_MCP_URL",
            "tools_to_execute": ["search", "fetch_url"]
          },
          {
            "name": "database",
            "connection_type": "sse",
            "connection_string": "https://db-mcp.example.com/sse",
            "tools_to_execute": []
          }
        ]
      }
    }
    ```

    <Note>
      Use `env.VARIABLE_NAME` syntax to reference environment variables for sensitive values like URLs with API keys.
    </Note>
  </Tab>
</Tabs>

***

## Go SDK Setup

Configure MCP in your Bifrost initialization:

```go  theme={null}
package main

import (
    "context"
    bifrost "github.com/maximhq/bifrost/core"
    "github.com/maximhq/bifrost/core/schemas"
)

func main() {
    mcpConfig := &schemas.MCPConfig{
        ClientConfigs: []schemas.MCPClientConfig{
            {
                Name:           "filesystem",
                ConnectionType: schemas.MCPConnectionTypeSTDIO,
                StdioConfig: &schemas.MCPStdioConfig{
                    Command: "npx",
                    Args:    []string{"-y", "@anthropic/mcp-filesystem"},
                    Envs:    []string{"HOME", "PATH"},
                },
                ToolsToExecute: []string{"*"},
            },
            {
                Name:             "web_search",
                ConnectionType:   schemas.MCPConnectionTypeHTTP,
                ConnectionString: bifrost.Ptr("http://localhost:3001/mcp"),
                ToolsToExecute:   []string{"search", "fetch_url"},
            },
        },
    }

    client, err := bifrost.Init(context.Background(), schemas.BifrostConfig{
        Account:   account,
        MCPConfig: mcpConfig,
        Logger:    bifrost.NewDefaultLogger(schemas.LogLevelInfo),
    })
    if err != nil {
        panic(err)
    }
}
```

### Tools To Execute Semantics

The `ToolsToExecute` field controls which tools from the client are available:

| Value                | Behavior                                |
| -------------------- | --------------------------------------- |
| `["*"]`              | All tools from this client are included |
| `[]` or `nil`        | No tools included (deny-by-default)     |
| `["tool1", "tool2"]` | Only specified tools are included       |

### Tools To Auto Execute (Agent Mode)

The `ToolsToAutoExecute` field controls which tools can be automatically executed in [Agent Mode](./agent-mode):

| Value                | Behavior                                              |
| -------------------- | ----------------------------------------------------- |
| `["*"]`              | All tools are auto-executed                           |
| `[]` or `nil`        | No tools are auto-executed (manual approval required) |
| `["tool1", "tool2"]` | Only specified tools are auto-executed                |

<Note>
  A tool must be in **both** `ToolsToExecute` and `ToolsToAutoExecute` to be auto-executed. If a tool is in `ToolsToAutoExecute` but not in `ToolsToExecute`, it will be skipped.
</Note>

**Example configuration:**

```go  theme={null}
{
    Name:           "filesystem",
    ConnectionType: schemas.MCPConnectionTypeSTDIO,
    StdioConfig: &schemas.MCPStdioConfig{
        Command: "npx",
        Args:    []string{"-y", "@anthropic/mcp-filesystem"},
    },
    ToolsToExecute:     []string{"*"},                              // All tools available
    ToolsToAutoExecute: []string{"read_file", "list_directory"},    // Only these auto-execute
}
```

***

## Environment Variables

Use environment variables for sensitive configuration values:

**Gateway (config.json):**

```json  theme={null}
{
  "name": "secure_api",
  "connection_type": "http",
  "connection_string": "env.SECURE_MCP_URL"
}
```

**Go SDK:**

```go  theme={null}
{
    Name:             "secure_api",
    ConnectionType:   schemas.MCPConnectionTypeHTTP,
    ConnectionString: bifrost.Ptr(os.Getenv("SECURE_MCP_URL")),
}
```

Environment variables are:

* Automatically resolved during client connection
* Redacted in API responses and UI for security
* Validated at startup to ensure all required variables are set

***

## Client State Management

### Connection States

| State          | Description                                   |
| -------------- | --------------------------------------------- |
| `connected`    | Client is active and tools are available      |
| `connecting`   | Client is establishing connection             |
| `disconnected` | Client lost connection but can be reconnected |
| `error`        | Client configuration or connection failed     |

### Managing Clients at Runtime

<Tabs>
  <Tab title="Gateway API">
    **Reconnect a client:**

    ```bash  theme={null}
    curl -X POST http://localhost:8080/api/mcp/client/{id}/reconnect
    ```

    **Edit client configuration:**

    ```bash  theme={null}
    curl -X PUT http://localhost:8080/api/mcp/client/{id} \
      -H "Content-Type: application/json" \
      -d '{
        "name": "filesystem",
        "connection_type": "stdio",
        "stdio_config": {
          "command": "npx",
          "args": ["-y", "@anthropic/mcp-filesystem"]
        },
        "tools_to_execute": ["read_file", "list_directory"]
      }'
    ```

    **Remove a client:**

    ```bash  theme={null}
    curl -X DELETE http://localhost:8080/api/mcp/client/{id}
    ```
  </Tab>

  <Tab title="Go SDK">
    ```go  theme={null}
    // Get all connected clients
    clients, err := client.GetMCPClients()
    for _, mcpClient := range clients {
        fmt.Printf("Client: %s, State: %s, Tools: %d\n",
            mcpClient.Config.Name,
            mcpClient.State,
            len(mcpClient.Tools))
    }

    // Reconnect a disconnected client
    err = client.ReconnectMCPClient("filesystem")

    // Add new client at runtime
    err = client.AddMCPClient(schemas.MCPClientConfig{
        Name:           "new_client",
        ConnectionType: schemas.MCPConnectionTypeHTTP,
        ConnectionString: bifrost.Ptr("http://localhost:3002/mcp"),
        ToolsToExecute: []string{"*"},
    })

    // Remove a client
    err = client.RemoveMCPClient("old_client")

    // Edit client tools
    err = client.EditMCPClientTools("filesystem", []string{"read_file", "list_directory"})
    ```
  </Tab>
</Tabs>

***

## Health Monitoring

Bifrost automatically monitors MCP client health:

* **Periodic Pings**: Every 10 seconds by default
* **Auto-Detection**: Disconnections are detected automatically
* **State Updates**: Client state changes are reflected in API responses

When a client disconnects:

1. State changes to `disconnected`
2. Tools from that client become unavailable
3. You can reconnect via API or UI

***

## Naming Conventions

MCP client names have specific requirements:

<Warning>
  * Must contain only ASCII characters
  * Cannot contain hyphens (`-`) or spaces
  * Cannot start with a number
  * Must be unique across all clients
</Warning>

**Valid names:** `filesystem`, `web_search`, `myAPI`, `tool123`

**Invalid names:** `my-tools`, `web search`, `123tools`, `datos-api`

***

## Next Steps

<CardGroup cols={2}>
  <Card title="Tool Execution" icon="play" href="./tool-execution">
    Learn how to execute tools from connected MCP servers
  </Card>

  <Card title="Agent Mode" icon="robot" href="./agent-mode">
    Enable autonomous tool execution with auto-approval
  </Card>
</CardGroup>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt