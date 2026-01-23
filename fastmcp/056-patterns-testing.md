---
title: Testing your FastMCP Server - FastMCP
url: https://gofastmcp.com/patterns/testing
source: crawler
fetched_at: 2026-01-22T22:21:50.85271189-03:00
rendered_js: false
word_count: 206
summary: This document explains how to set up and write tests for FastMCP servers using Pytest and the FastMCP Client, including configuration for async testing and fixture usage.
tags:
    - fastmcp
    - pytest
    - testing
    - python
    - async-testing
    - mcp-server
category: tutorial
---

The best way to ensure a reliable and maintainable FastMCP Server is to test it! The FastMCP Client combined with Pytest provides a simple and powerful way to test your FastMCP servers.

## Prerequisites

Testing FastMCP servers requires `pytest-asyncio` to handle async test functions and fixtures. Install it as a development dependency:

```
pip install pytest-asyncio
```

We recommend configuring pytest to automatically handle async tests by setting the asyncio mode to `auto` in your `pyproject.toml`:

```
[tool.pytest.ini_options]
asyncio_mode = "auto"
```

This eliminates the need to decorate every async test with `@pytest.mark.asyncio`.

## Testing with Pytest Fixtures

Using Pytest Fixtures, you can wrap your FastMCP Server in a Client instance that makes interacting with your server fast and easy. This is especially useful when building your own MCP Servers and enables a tight development loop by allowing you to avoid using a separate tool like MCP Inspector during development:

```
import pytest
from fastmcp.client import Client
from fastmcp.client.transports import FastMCPTransport

from my_project.main import mcp

@pytest.fixture
async def main_mcp_client():
    async with Client(transport=mcp) as mcp_client:
        yield mcp_client

async def test_list_tools(main_mcp_client: Client[FastMCPTransport]):
    list_tools = await main_mcp_client.list_tools()

    assert len(list_tools) == 5
```

We recommend the [inline-snapshot library](https://github.com/15r10nk/inline-snapshot) for asserting complex data structures coming from your MCP Server. This library allows you to write tests that are easy to read and understand, and are also easy to update when the data structure changes.

```
from inline_snapshot import snapshot

async def test_list_tools(main_mcp_client: Client[FastMCPTransport]):
    list_tools = await main_mcp_client.list_tools()

    assert list_tools == snapshot()
```

Simply run `pytest --inline-snapshot=fix,create` to fill in the `snapshot()` with actual data.

Using the pytest `parametrize` decorator, you can easily test your tools with a wide variety of inputs.

```
import pytest
from my_project.main import mcp

from fastmcp.client import Client
from fastmcp.client.transports import FastMCPTransport
@pytest.fixture
async def main_mcp_client():
    async with Client(mcp) as client:
        yield client


@pytest.mark.parametrize(
    "first_number, second_number, expected",
    [
        (1, 2, 3),
        (2, 3, 5),
        (3, 4, 7),
    ],
)
async def test_add(
    first_number: int,
    second_number: int,
    expected: int,
    main_mcp_client: Client[FastMCPTransport],
):
    result = await main_mcp_client.call_tool(
        name="add", arguments={"x": first_number, "y": second_number}
    )
    assert result.data is not None
    assert isinstance(result.data, int)
    assert result.data == expected
```