---
title: Progress Monitoring - FastMCP
url: https://gofastmcp.com/clients/progress
source: crawler
fetched_at: 2026-01-22T22:23:01.849736418-03:00
rendered_js: false
word_count: 55
summary: This document explains how to implement and use progress handlers in MCP clients to track the status of long-running operations. It covers both client-wide and per-call configuration options introduced in version 2.3.5.
tags:
    - mcp-protocol
    - fastmcp
    - progress-tracking
    - python-sdk
    - event-handlers
    - long-running-tasks
category: guide
---

New in version `2.3.5` Use this when you need to track progress of long-running operations. MCP servers can report progress during operations. The client receives these updates through a progress handler.

## Progress Handler

Set a handler when creating the client:

```
from fastmcp import Client

async def progress_handler(
    progress: float,
    total: float | None,
    message: str | None
) -> None:
    if total is not None:
        percentage = (progress / total) * 100
        print(f"Progress: {percentage:.1f}% - {message or ''}")
    else:
        print(f"Progress: {progress} - {message or ''}")

client = Client(
    "my_mcp_server.py",
    progress_handler=progress_handler
)
```

The handler receives three parameters:

## Per-Call Handler

Override the client-level handler for specific tool calls:

```
async with client:
    result = await client.call_tool(
        "long_running_task",
        {"param": "value"},
        progress_handler=my_progress_handler
    )
```