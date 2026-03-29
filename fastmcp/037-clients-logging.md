---
title: Server Logging - FastMCP
url: https://gofastmcp.com/clients/logging
source: crawler
fetched_at: 2026-01-22T22:23:02.715709993-03:00
rendered_js: false
word_count: 131
summary: Explains how to capture and process log messages emitted by MCP servers using the FastMCP client's log handler functionality.
tags:
    - mcp-server
    - logging
    - fastmcp
    - log-handler
    - structured-logging
    - python-client
category: guide
---

New in version `2.0.0` Use this when you need to capture or process log messages sent by the server. MCP servers can emit log messages to clients. The client handles these through a log handler callback.

## Log Handler

Provide a `log_handler` function when creating the client:

```
import logging
from fastmcp import Client
from fastmcp.client.logging import LogMessage

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
LOGGING_LEVEL_MAP = logging.getLevelNamesMapping()

async def log_handler(message: LogMessage):
    """Forward MCP server logs to Python's logging system."""
    msg = message.data.get('msg')
    extra = message.data.get('extra')

    level = LOGGING_LEVEL_MAP.get(message.level.upper(), logging.INFO)
    logger.log(level, msg, extra=extra)

client = Client(
    "my_mcp_server.py",
    log_handler=log_handler,
)
```

The handler receives a `LogMessage` object:

## Structured Logs

The `message.data` attribute is a dictionary containing the log payload. This enables structured logging with rich contextual information.

```
async def detailed_log_handler(message: LogMessage):
    msg = message.data.get('msg')
    extra = message.data.get('extra')

    if message.level == "error":
        print(f"ERROR: {msg} | Details: {extra}")
    elif message.level == "warning":
        print(f"WARNING: {msg} | Details: {extra}")
    else:
        print(f"{message.level.upper()}: {msg}")
```

This structure is preserved even when logs are forwarded through a FastMCP proxy, making it useful for debugging multi-server applications.

## Default Behavior

If you do not provide a custom `log_handler`, FastMCP’s default handler routes server logs to Python’s logging system at the appropriate severity level. The MCP levels map as follows: `notice` becomes INFO; `alert` and `emergency` become CRITICAL.

```
client = Client("my_mcp_server.py")

async with client:
    # Server logs are forwarded at proper severity automatically
    await client.call_tool("some_tool")
```