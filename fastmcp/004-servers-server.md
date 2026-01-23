---
title: The FastMCP Server - FastMCP
url: https://gofastmcp.com/servers/server
source: crawler
fetched_at: 2026-01-22T22:21:40.950334335-03:00
rendered_js: false
word_count: 494
summary: This document explains the core FastMCP class used to build Model Context Protocol servers, including how to define tools, resources, and prompts while managing server lifecycle and transports.
tags:
    - fastmcp
    - mcp-server
    - python-api
    - tag-filtering
    - http-transport
    - resource-templates
    - server-orchestration
category: reference
---

The `FastMCP` class is the central piece of every FastMCP application. It acts as the container for your tools, resources, and prompts, managing communication with MCP clients and orchestrating the entire server lifecycle.

## Creating a Server

Instantiate a server by providing a name that identifies it in client applications and logs. You can also provide instructions that help clients understand the server’s purpose.

```
from fastmcp import FastMCP

mcp = FastMCP(name="MyAssistantServer")

# Instructions help clients understand how to interact with the server
mcp_with_instructions = FastMCP(
    name="HelpfulAssistant",
    instructions="""
        This server provides data analysis tools.
        Call get_average() to analyze numerical data.
    """,
)
```

The `FastMCP` constructor accepts several configuration options. The most commonly used parameters control server identity, authentication, and component behavior.

## Components

FastMCP servers expose three types of components to clients. Each type serves a distinct purpose in the MCP protocol.

### Tools

Tools are functions that clients can invoke to perform actions or access external systems. They’re the primary way clients interact with your server’s capabilities.

```
@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    return a * b
```

See [Tools](https://gofastmcp.com/servers/tools) for detailed documentation.

### Resources

Resources expose data that clients can read. Unlike tools, resources are passive data sources that clients pull from rather than invoke.

```
@mcp.resource("data://config")
def get_config() -> dict:
    """Provides the application configuration."""
    return {"theme": "dark", "version": "1.0"}
```

See [Resources](https://gofastmcp.com/servers/resources) for detailed documentation.

### Resource Templates

Resource templates are parameterized resources. The client provides values for template parameters in the URI, and the server returns data specific to those parameters.

```
@mcp.resource("users://{user_id}/profile")
def get_user_profile(user_id: int) -> dict:
    """Retrieves a user's profile by ID."""
    return {"id": user_id, "name": f"User {user_id}", "status": "active"}
```

See [Resource Templates](https://gofastmcp.com/servers/resources#resource-templates) for detailed documentation.

### Prompts

Prompts are reusable message templates that guide LLM interactions. They help establish consistent patterns for how clients should frame requests.

```
@mcp.prompt
def analyze_data(data_points: list[float]) -> str:
    """Creates a prompt asking for analysis of numerical data."""
    formatted_data = ", ".join(str(point) for point in data_points)
    return f"Please analyze these data points: {formatted_data}"
```

See [Prompts](https://gofastmcp.com/servers/prompts) for detailed documentation.

## Tag-Based Filtering

New in version `2.8.0` Tags let you categorize components and selectively expose them based on configurable include/exclude sets. This is useful for creating different views of your server for different environments or user types. Components can be tagged when defined using the `tags` parameter. A component can have multiple tags, and filtering operates on tag membership.

```
@mcp.tool(tags={"public", "utility"})
def public_tool() -> str:
    return "This tool is public"

@mcp.tool(tags={"internal", "admin"})
def admin_tool() -> str:
    return "This tool is for admins only"
```

The filtering logic works as follows:

- **Include tags**: If specified, only components with at least one matching tag are exposed
- **Exclude tags**: Components with any matching tag are filtered out
- **Precedence**: Exclude tags always take priority over include tags

Configure tag-based filtering when creating your server.

```
# Only expose components tagged with "public"
mcp = FastMCP(include_tags={"public"})

# Hide components tagged as "internal" or "deprecated"
mcp = FastMCP(exclude_tags={"internal", "deprecated"})

# Combine both: show admin tools but hide deprecated ones
mcp = FastMCP(include_tags={"admin"}, exclude_tags={"deprecated"})
```

This filtering applies to all component types (tools, resources, resource templates, and prompts) and affects both listing and access.

## Running the Server

FastMCP servers communicate with clients through transport mechanisms. Start your server by calling `mcp.run()`, typically within an `if __name__ == "__main__":` block. This pattern ensures compatibility with various MCP clients.

```
from fastmcp import FastMCP

mcp = FastMCP(name="MyServer")

@mcp.tool
def greet(name: str) -> str:
    """Greet a user by name."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Defaults to STDIO transport
    mcp.run()

    # Or use HTTP transport
    # mcp.run(transport="http", host="127.0.0.1", port=9000)
```

FastMCP supports several transports:

- **STDIO** (default): For local integrations and CLI tools
- **HTTP**: For web services using the Streamable HTTP protocol
- **SSE**: Legacy web transport (deprecated)

The server can also be run using the FastMCP CLI. For detailed information on transports and configuration, see the [Running Your Server](https://gofastmcp.com/deployment/running-server) guide.

## Custom Routes

When running with HTTP transport, you can add custom web routes alongside your MCP endpoint using the `@custom_route` decorator. This is useful for auxiliary endpoints like health checks.

```
from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import PlainTextResponse

mcp = FastMCP("MyServer")

@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request) -> PlainTextResponse:
    return PlainTextResponse("OK")

if __name__ == "__main__":
    mcp.run(transport="http")  # Health check at http://localhost:8000/health
```

Custom routes are served alongside your MCP endpoint and are useful for:

- Health check endpoints for monitoring
- Simple status or info endpoints
- Basic webhooks or callbacks

For more complex web applications, consider [mounting your MCP server into a FastAPI or Starlette app](https://gofastmcp.com/deployment/http#integration-with-web-frameworks).