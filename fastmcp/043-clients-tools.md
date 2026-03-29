---
title: Calling Tools - FastMCP
url: https://gofastmcp.com/clients/tools
source: crawler
fetched_at: 2026-01-22T22:23:00.852041275-03:00
rendered_js: false
word_count: 205
summary: This document explains how to execute server-side functions using the call_tool method, covering basic execution, structured result handling, and error management within the FastMCP framework.
tags:
    - fastmcp
    - tool-execution
    - mcp-client
    - error-handling
    - structured-data
    - asynchronous-functions
category: guide
---

New in version `2.0.0` Use this when you need to execute server-side functions and process their results. Tools are executable functions exposed by MCP servers. The client’s `call_tool()` method executes a tool by name with arguments and returns structured results.

## Basic Execution

```
async with client:
    result = await client.call_tool("add", {"a": 5, "b": 3})
    # result -> CallToolResult with structured and unstructured data

    # Access structured data (automatically deserialized)
    print(result.data)  # 8

    # Access traditional content blocks
    print(result.content[0].text)  # "8"
```

Arguments are passed as a dictionary. For multi-server clients, tool names are automatically prefixed with the server name (e.g., `weather_get_forecast` for a tool named `get_forecast` on the `weather` server).

## Execution Options

The `call_tool()` method supports timeout control and progress monitoring:

```
async with client:
    # With timeout (aborts if execution takes longer than 2 seconds)
    result = await client.call_tool(
        "long_running_task",
        {"param": "value"},
        timeout=2.0
    )

    # With progress handler
    result = await client.call_tool(
        "long_running_task",
        {"param": "value"},
        progress_handler=my_progress_handler
    )
```

## Structured Results

New in version `2.10.0` Tool execution returns a `CallToolResult` object. The `.data` property provides fully hydrated Python objects including complex types like datetimes and UUIDs, reconstructed from the server’s output schema.

```
from datetime import datetime
from uuid import UUID

async with client:
    result = await client.call_tool("get_weather", {"city": "London"})

    # FastMCP reconstructs complete Python objects
    weather = result.data
    print(f"Temperature: {weather.temperature}C at {weather.timestamp}")

    # Complex types are properly deserialized
    assert isinstance(weather.timestamp, datetime)
    assert isinstance(weather.station_id, UUID)

    # Raw structured JSON is also available
    print(f"Raw JSON: {result.structured_content}")
```

For tools without output schemas or when deserialization fails, `.data` will be `None`. Fall back to content blocks in that case:

```
async with client:
    result = await client.call_tool("legacy_tool", {"param": "value"})

    if result.data is not None:
        print(f"Structured: {result.data}")
    else:
        for content in result.content:
            if hasattr(content, 'text'):
                print(f"Text result: {content.text}")
```

## Error Handling

By default, `call_tool()` raises a `ToolError` if the tool execution fails:

```
from fastmcp.exceptions import ToolError

async with client:
    try:
        result = await client.call_tool("potentially_failing_tool", {"param": "value"})
        print("Tool succeeded:", result.data)
    except ToolError as e:
        print(f"Tool failed: {e}")
```

To handle errors manually instead of catching exceptions, disable automatic error raising:

```
async with client:
    result = await client.call_tool(
        "potentially_failing_tool",
        {"param": "value"},
        raise_on_error=False
    )

    if result.is_error:
        print(f"Tool failed: {result.content[0].text}")
    else:
        print(f"Tool succeeded: {result.data}")
```

New in version `2.13.1` The `meta` parameter sends ancillary information alongside tool calls for observability, debugging, or client identification:

```
async with client:
    result = await client.call_tool(
        name="send_email",
        arguments={
            "to": "[email protected]",
            "subject": "Hello",
            "body": "Welcome!"
        },
        meta={
            "trace_id": "abc-123",
            "request_source": "mobile_app"
        }
    )
```

See [Client Metadata](https://gofastmcp.com/servers/context#client-metadata) to learn how servers access this data.

## Raw Protocol Access

For complete control, use `call_tool_mcp()` which returns the raw MCP protocol object:

```
async with client:
    result = await client.call_tool_mcp("my_tool", {"param": "value"})
    # result -> mcp.types.CallToolResult

    if result.isError:
        print(f"Tool failed: {result.content}")
    else:
        print(f"Tool succeeded: {result.content}")
        # Note: No automatic deserialization with call_tool_mcp()
```