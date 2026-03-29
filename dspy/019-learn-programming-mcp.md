---
title: MCP - DSPy
url: https://dspy.ai/learn/programming/mcp/
source: sitemap
fetched_at: 2026-01-23T08:03:25.386976951-03:00
rendered_js: false
word_count: 205
summary: This document explains how to integrate the Model Context Protocol (MCP) with DSPy to provide standardized tools to agents via HTTP or Stdio servers. It provides instructions for installing the necessary dependencies and converting MCP tools into DSPy-compatible tools.
tags:
    - mcp
    - dspy
    - tool-integration
    - agents
    - react-agent
    - stdio-server
    - http-server
category: guide
---

[](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/learn/programming/mcp.md "Edit this page")

## Model Context Protocol (MCP)[¶](#model-context-protocol-mcp "Permanent link")

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) is an open protocol that standardizes how applications provide context to language models. DSPy supports MCP, allowing you to use tools from any MCP server with DSPy agents.

## Installation[¶](#installation "Permanent link")

Install DSPy with MCP support:

```
pipinstall-U"dspy[mcp]"
```

## Overview[¶](#overview "Permanent link")

MCP enables you to:

- **Use standardized tools** - Connect to any MCP-compatible server.
- **Share tools across stacks** - Use the same tools across different frameworks.
- **Simplify integration** - Convert MCP tools to DSPy tools with one line.

DSPy does not handle MCP server connections directly. You can use client interfaces of the `mcp` library to establish the connection and pass `mcp.ClientSession` to `dspy.Tool.from_mcp_tool` in order to convert mcp tools into DSPy tools.

## Using MCP with DSPy[¶](#using-mcp-with-dspy "Permanent link")

### 1. HTTP Server (Remote)[¶](#1-http-server-remote "Permanent link")

For remote MCP servers over HTTP, use the streamable HTTP transport:

```
importasyncio
importdspy
frommcpimport ClientSession
frommcp.client.streamable_httpimport streamablehttp_client

async defmain():
    # Connect to HTTP MCP server
    async with streamablehttp_client("http://localhost:8000/mcp") as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the session
            await session.initialize()

            # List and convert tools
            response = await session.list_tools()
            dspy_tools = [
                dspy.Tool.from_mcp_tool(session, tool)
                for tool in response.tools
            ]

            # Create and use ReAct agent
            classTaskSignature(dspy.Signature):
                task: str = dspy.InputField()
                result: str = dspy.OutputField()

            react_agent = dspy.ReAct(
                signature=TaskSignature,
                tools=dspy_tools,
                max_iters=5
            )

            result = await react_agent.acall(task="Check the weather in Tokyo")
            print(result.result)

asyncio.run(main())
```

### 2. Stdio Server (Local Process)[¶](#2-stdio-server-local-process "Permanent link")

The most common way to use MCP is with a local server process communicating via stdio:

```
importasyncio
importdspy
frommcpimport ClientSession, StdioServerParameters
frommcp.client.stdioimport stdio_client

async defmain():
    # Configure the stdio server
    server_params = StdioServerParameters(
        command="python",                    # Command to run
        args=["path/to/your/mcp_server.py"], # Server script path
        env=None,                            # Optional environment variables
    )

    # Connect to the server
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the session
            await session.initialize()

            # List available tools
            response = await session.list_tools()

            # Convert MCP tools to DSPy tools
            dspy_tools = [
                dspy.Tool.from_mcp_tool(session, tool)
                for tool in response.tools
            ]

            # Create a ReAct agent with the tools
            classQuestionAnswer(dspy.Signature):
"""Answer questions using available tools."""
                question: str = dspy.InputField()
                answer: str = dspy.OutputField()

            react_agent = dspy.ReAct(
                signature=QuestionAnswer,
                tools=dspy_tools,
                max_iters=5
            )

            # Use the agent
            result = await react_agent.acall(
                question="What is 25 + 17?"
            )
            print(result.answer)

# Run the async function
asyncio.run(main())
```

DSPy automatically handles the conversion from MCP tools to DSPy tools:

```
# MCP tool from session
mcp_tool = response.tools[0]

# Convert to DSPy tool
dspy_tool = dspy.Tool.from_mcp_tool(session, mcp_tool)

# The DSPy tool preserves:
# - Tool name and description
# - Parameter schemas and types
# - Argument descriptions
# - Async execution support

# Use it like any DSPy tool
result = await dspy_tool.acall(param1="value", param2=123)
```

## Learn More[¶](#learn-more "Permanent link")

- [MCP Official Documentation](https://modelcontextprotocol.io/)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [DSPy MCP Tutorial](https://dspy.ai/tutorials/mcp/)
- [DSPy Tools Documentation](https://dspy.ai/learn/programming/tools/)

MCP integration in DSPy makes it easy to use standardized tools from any MCP server, enabling powerful agent capabilities with minimal setup.