---
title: Mounting Servers - FastMCP
url: https://gofastmcp.com/servers/providers/mounting#mounting-external-servers
source: crawler
fetched_at: 2026-01-22T22:22:04.529431851-03:00
rendered_js: false
word_count: 437
summary: This guide explains how to combine multiple FastMCP servers into a unified parent server using mounting and importing for modular application design. It details namespacing, proxying external servers, and managing component lifecycles to ensure scalable and organized server architectures.
tags:
    - fastmcp
    - server-mounting
    - modular-architecture
    - namespacing
    - proxy-mounting
    - server-composition
    - python-mcp
category: guide
---

New in version `2.2.0` Mounting lets you combine multiple FastMCP servers into one. When you mount a server, all its components become available through the parent. Under the hood, FastMCP uses `FastMCPProvider` (v3.0.0+) to source components from the mounted server.

## Why Mount Servers

Large applications benefit from modular organization. Rather than defining all components in one massive file, create focused servers for specific domains and combine them:

- **Modularity**: Break down applications into smaller, focused servers
- **Reusability**: Create utility servers and mount them wherever needed
- **Teamwork**: Different teams can work on separate servers
- **Organization**: Keep related functionality grouped together

## Basic Mounting

Use `mount()` to add another server’s components to your server:

```
from fastmcp import FastMCP

# Create focused subservers
weather_server = FastMCP("Weather")

@weather_server.tool
def get_forecast(city: str) -> str:
    """Get weather forecast for a city."""
    return f"Sunny in {city}"

@weather_server.resource("data://cities")
def list_cities() -> list[str]:
    """List supported cities."""
    return ["London", "Paris", "Tokyo"]

# Create main server and mount the subserver
main = FastMCP("MainApp")
main.mount(weather_server)

# Now main has access to get_forecast and data://cities
```

## Mounting External Servers

Mount remote HTTP servers or subprocess-based MCP servers using `create_proxy()`:

```
from fastmcp import FastMCP
from fastmcp.server import create_proxy

mcp = FastMCP("Orchestrator")

# Mount a remote HTTP server (URLs work directly)
mcp.mount(create_proxy("http://api.example.com/mcp"), namespace="api")

# Mount local Python scripts (file paths work directly)
mcp.mount(create_proxy("./my_server.py"), namespace="local")
```

### Mounting npm/uvx Packages

For npm packages or Python tools, use the config dict format:

```
from fastmcp import FastMCP
from fastmcp.server import create_proxy

mcp = FastMCP("Orchestrator")

# Mount npm package via config
github_config = {
    "mcpServers": {
        "default": {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-github"]
        }
    }
}
mcp.mount(create_proxy(github_config), namespace="github")

# Mount Python tool via config
sqlite_config = {
    "mcpServers": {
        "default": {
            "command": "uvx",
            "args": ["mcp-server-sqlite", "--db", "data.db"]
        }
    }
}
mcp.mount(create_proxy(sqlite_config), namespace="db")
```

Or use explicit transport classes:

```
from fastmcp import FastMCP
from fastmcp.server import create_proxy
from fastmcp.client.transports import NpxStdioTransport, UvxStdioTransport

mcp = FastMCP("Orchestrator")

mcp.mount(
    create_proxy(NpxStdioTransport(package="@modelcontextprotocol/server-github")),
    namespace="github"
)
mcp.mount(
    create_proxy(UvxStdioTransport(tool_name="mcp-server-sqlite", tool_args=["--db", "data.db"])),
    namespace="db"
)
```

For advanced configuration, see [Proxying](https://gofastmcp.com/servers/providers/proxy).

## Namespacing

New in version `3.0.0` When mounting multiple servers, use namespaces to avoid naming conflicts:

```
weather = FastMCP("Weather")
calendar = FastMCP("Calendar")

@weather.tool
def get_data() -> str:
    return "Weather data"

@calendar.tool
def get_data() -> str:
    return "Calendar data"

main = FastMCP("Main")
main.mount(weather, namespace="weather")
main.mount(calendar, namespace="calendar")

# Tools are now:
# - weather_get_data
# - calendar_get_data
```

### How Namespacing Works

Component TypeWithout NamespaceWith `namespace="api"`Tool`my_tool``api_my_tool`Prompt`my_prompt``api_my_prompt`Resource`data://info``data://api/info`Template`data://{id}``data://api/{id}`

Namespacing uses [transforms](https://gofastmcp.com/servers/transforms/transforms) under the hood.

## Mounting vs Importing

FastMCP offers two ways to combine servers:

Feature`mount()``import_server()`**Link Type**Live (dynamic)One-time copy (static)**Updates**Changes reflected immediatelyChanges not reflected**Performance**Runtime delegationFaster - no delegation**Use Case**Modular runtime compositionBundling finalized components

### Live Mounting

With `mount()`, changes to the subserver are immediately reflected:

```
main = FastMCP("Main")
main.mount(dynamic_server, namespace="dynamic")

# Add a tool AFTER mounting - it's accessible through main
@dynamic_server.tool
def added_later() -> str:
    return "Added after mounting!"

# This works because mount() creates a live link
```

### Static Importing

With `import_server()`, components are copied once at import time:

```
main = FastMCP("Main")

async def setup():
    await main.import_server(static_server, namespace="static")

# Changes to static_server after this point are NOT reflected in main
```

## Direct vs Proxy Mounting

New in version `2.2.7` FastMCP supports two mounting modes:

### Direct Mounting (Default)

The parent server directly accesses the mounted server’s objects in memory:

```
main.mount(subserver, namespace="api")
```

- No client lifecycle events on mounted server
- Mounted server’s lifespan is not executed
- Communication via direct method calls

### Proxy Mounting

Previously, the parent server could treat the mounted server as a separate entity with its own lifecycle. This behavior is now the default for all mounted servers:

- Full client lifecycle events on mounted server
- Mounted server’s lifespan is executed
- Communication via in-memory Client transport

## Tag Filtering

New in version `3.0.0` Parent server tag filters apply recursively to mounted servers:

```
api_server = FastMCP("API")

@api_server.tool(tags={"production"})
def prod_endpoint() -> str:
    return "Production data"

@api_server.tool(tags={"development"})
def dev_endpoint() -> str:
    return "Debug data"

# Mount with production filter
prod_app = FastMCP("Production")
prod_app.mount(api_server, namespace="api")
prod_app.enable(tags={"production"}, only=True)

# Only prod_endpoint (namespaced as api_prod_endpoint) is visible
```

## Performance Considerations

When using live mounting, operations like `list_tools()` on the parent server are affected by the performance of all mounted servers. This is particularly noticeable with:

- HTTP-based mounted servers (300-400ms vs 1-2ms for local tools)
- Mounted servers with slow initialization
- Deep mounting hierarchies

If low latency is critical, consider:

- Using `import_server()` for static composition
- Implementing caching strategies
- Limiting mounting depth

## Custom Routes

New in version `2.4.0` Custom HTTP routes defined with `@server.custom_route()` are also forwarded when mounting:

```
subserver = FastMCP("Sub")

@subserver.custom_route("/health", methods=["GET"])
async def health_check():
    return {"status": "ok"}

main = FastMCP("Main")
main.mount(subserver, namespace="sub")

# /health is now accessible through main's HTTP app
```

## Conflict Resolution

New in version `3.0.0` When mounting multiple servers with the same namespace (or no namespace), the **most recently mounted** server takes precedence for conflicting component names:

```
server_a = FastMCP("A")
server_b = FastMCP("B")

@server_a.tool
def shared_tool() -> str:
    return "From A"

@server_b.tool
def shared_tool() -> str:
    return "From B"

main = FastMCP("Main")
main.mount(server_a)
main.mount(server_b)

# shared_tool returns "From B" (most recently mounted)
```