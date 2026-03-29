---
title: MCP | Mistral Docs
url: https://docs.mistral.ai/agents/tools/mcp
source: crawler
fetched_at: 2026-01-29T07:34:17.100662109-03:00
rendered_js: false
word_count: 167
summary: A guide to the Model Context Protocol (MCP) by Mistral AI, detailing how to connect AI models to external data sources and tools through a standardized integration layer.
tags:
    - Mistral AI
    - MCP
    - API
    - LLM
    - Integration
category: guide
---

Here is how to create an agent that uses a local MCP server to fetch weather information based on a user's location, combining MCP integration.

First, we import everything needed. Most of the required modules are available with our `mistralai` package, but you will also need `mcp`. All the MCP Clients will be run asynchronously, so we will create an async main function where the main code will reside.

We can now define the server parameters, which will point to a specific path. For more information, we recommend visiting the Model Context Protocol documentation. Once the server is defined, we can create our agent.

The next step is to create a Run Context where everything will happen between the MCP Client and our Agent. You can also leverage structured outputs!

The next step is to create and register the MCP Client.

You can also leverage the MCP Orchestration to use Function Calling locally directly.

Everything is ready; you can run our Agent and get the output results!