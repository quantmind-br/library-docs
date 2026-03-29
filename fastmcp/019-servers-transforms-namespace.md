---
title: Namespace Transform - FastMCP
url: https://gofastmcp.com/servers/transforms/namespace
source: crawler
fetched_at: 2026-01-22T22:21:46.110275161-03:00
rendered_js: false
word_count: 57
summary: Explains how to use the Namespace transform in FastMCP to prefix component names and prevent naming conflicts when composing multiple servers.
tags:
    - fastmcp
    - namespacing
    - server-composition
    - mcp-tools
    - resource-management
category: guide
---

New in version `3.0.0` The `Namespace` transform prefixes all component names, preventing conflicts when composing multiple servers. Tools and prompts receive an underscore-separated prefix. Resources and templates receive a path-segment prefix in their URIs.

ComponentOriginalWith `Namespace("api")`Tool`my_tool``api_my_tool`Prompt`my_prompt``api_my_prompt`Resource`data://info``data://api/info`Template`data://{id}``data://api/{id}`

The most common use is through the `mount()` method’s `namespace` parameter.

```
from fastmcp import FastMCP

weather = FastMCP("Weather")
calendar = FastMCP("Calendar")

@weather.tool
def get_data() -> str:
    return "Weather data"

@calendar.tool
def get_data() -> str:
    return "Calendar data"

# Without namespacing, these would conflict
main = FastMCP("Main")
main.mount(weather, namespace="weather")
main.mount(calendar, namespace="calendar")

# Clients see: weather_get_data, calendar_get_data
```

You can also apply namespacing directly using the `Namespace` transform.

```
from fastmcp import FastMCP
from fastmcp.server.transforms import Namespace

mcp = FastMCP("Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Namespace all components
mcp.add_transform(Namespace("api"))

# Tool is now: api_greet
```