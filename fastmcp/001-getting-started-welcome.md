---
title: Welcome to FastMCP 3.0! - FastMCP
url: https://gofastmcp.com/getting-started/welcome
source: crawler
fetched_at: 2026-01-22T22:21:31.916421908-03:00
rendered_js: false
word_count: 452
summary: This document introduces FastMCP, a Python framework for building Model Context Protocol (MCP) applications that simplifies connecting LLMs to tools and data through standardized abstractions.
tags:
    - fastmcp
    - model-context-protocol
    - mcp-server
    - python-framework
    - llm-integration
category: concept
---

!['F' logo on a watercolor background](https://mintcdn.com/fastmcp/vP28Y_HI4lA7ZSYM/assets/brand/f-watercolor-waves-2.png?fit=max&auto=format&n=vP28Y_HI4lA7ZSYM&q=85&s=ed5a792b94ca3d10ae2545461c4cc84d) !['F' logo on a watercolor background](https://mintcdn.com/fastmcp/vP28Y_HI4lA7ZSYM/assets/brand/f-watercolor-waves-dark-2.jpeg?fit=max&auto=format&n=vP28Y_HI4lA7ZSYM&q=85&s=722c3437ce47b4eff4e19e0beb7be363) **FastMCP is the standard framework for building MCP applications.** The [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) provides a standardized way to connect LLMs to tools and data, and FastMCP makes it production-ready with clean, Pythonic code:

```
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run()
```

FastMCP is made with 💙 by [Prefect](https://www.prefect.io/).

## Move Fast and Make Things

The [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) lets you give agents access to your tools and data. But building an effective MCP server is harder than it looks. Give your agent too much—hundreds of tools, verbose responses—and it gets overwhelmed. Give it too little and it can’t do its job. The protocol itself is complex, with layers of serialization, validation, and error handling that have nothing to do with your business logic. And the spec keeps evolving; what worked last month might already need updating. The real challenge isn’t implementing the protocol. It’s delivering **the right information at the right time**. That’s the problem FastMCP solves—and why it’s become the standard. FastMCP 1.0 was incorporated into the official MCP SDK in 2024. Today, the actively maintained standalone project is downloaded a million times a day, and some version of FastMCP powers 70% of MCP servers across all languages. The framework is built on three abstractions that map to the decisions you actually need to make:

- [**Components**](https://gofastmcp.com/servers/tools) are what you expose: tools, resources, and prompts. Wrap a Python function, and FastMCP handles the schema, validation, and docs.
- [**Providers**](https://gofastmcp.com/servers/providers/overview) are where components come from: decorated functions, files on disk, OpenAPI specs, remote servers—your logic can live anywhere.
- [**Transforms**](https://gofastmcp.com/servers/transforms/transforms) shape what clients see: namespacing, filtering, authorization, versioning. The same server can present differently to different users.

These compose cleanly, so complex patterns don’t require complex code. And because FastMCP is opinionated about the details, like serialization, error handling, and protocol compliance, **best practices are the path of least resistance**. You focus on your logic; the MCP part just works. Ready to build? Start with the [installation guide](https://gofastmcp.com/getting-started/installation) or jump straight to the [quickstart](https://gofastmcp.com/getting-started/quickstart). When you’re ready to deploy, [Prefect Horizon](https://www.prefect.io/horizon) offers free hosting for FastMCP users.

## LLM-Friendly Docs

The FastMCP documentation is available in multiple LLM-friendly formats:

### MCP Server

The FastMCP docs are accessible via MCP! The server URL is `https://gofastmcp.com/mcp`. In fact, you can use FastMCP to search the FastMCP docs:

```
import asyncio
from fastmcp import Client

async def main():
    async with Client("https://gofastmcp.com/mcp") as client:
        result = await client.call_tool(
            name="SearchFastMcp",
            arguments={"query": "deploy a FastMCP server"}
        )
    print(result)

asyncio.run(main())
```

### Text Formats

The docs are also available in [llms.txt format](https://llmstxt.org/):

- [llms.txt](https://gofastmcp.com/llms.txt) - A sitemap listing all documentation pages
- [llms-full.txt](https://gofastmcp.com/llms-full.txt) - The entire documentation in one file (may exceed context windows)

Any page can be accessed as markdown by appending `.md` to the URL. For example, this page becomes `https://gofastmcp.com/getting-started/welcome.md`. You can also copy any page as markdown by pressing “Cmd+C” (or “Ctrl+C” on Windows) on your keyboard.