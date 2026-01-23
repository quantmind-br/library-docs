---
title: MCP Sampling Extensions | goose
url: https://block.github.io/goose/docs/guides/mcp-sampling
source: github_pages
fetched_at: 2026-01-22T22:14:10.286304959-03:00
rendered_js: true
word_count: 322
summary: This document explains how MCP Sampling allows goose extensions to leverage the host's AI capabilities for contextual analysis and intelligent decision-making. It details the mechanism of sampling requests and provides use cases for creating more sophisticated AI-driven tools.
tags:
    - mcp-sampling
    - model-context-protocol
    - goose-ai
    - extension-development
    - agentic-capabilities
category: concept
---

MCP Sampling can transform extensions from simple data providers into intelligent agents. Instead of just returning raw information for goose to interpret, extensions can leverage goose's AI capabilities to provide expert-level guidance, perform contextual analysis, and create entirely new interaction patterns.

This feature is automatically enabled in goose, no configuration required! Any MCP server extension that supports sampling will automatically have access to the LLM that goose is using. This means:

- goose users can get more targeted responses tailored to the extension's specific capabilities
- developers can add sampling support to their MCP servers to provide enhanced capabilities in goose

Try out the [Council of Mine](https://block.github.io/goose/docs/mcp/council-of-mine-mcp) extension to see MCP sampling in action!

info

[MCP Sampling](https://modelcontextprotocol.io/specification/draft/client/sampling) is a feature in the Model Context Protocol.

## How MCP Sampling Works[​](#how-mcp-sampling-works "Direct link to How MCP Sampling Works")

MCP Sampling enables extensions to ask goose's AI for help with their tasks. When an extension needs to analyze data, make intelligent decisions, or understand natural language, it can send a "sampling" request to ask for AI assistance. goose processes the request using its AI capabilities and returns the response to the extension.

This feature allows extensions to provide more specialized contextual responses or novel interaction patterns. The following example shows how a database extension could provide expert-level diagnostics by combining its domain knowledge with goose's AI analysis:

- Without Sampling
- With Sampling

<!--THE END-->

1. You ask goose: "What's wrong with my database performance?"
2. goose calls the database tool
3. The database tool returns raw metrics to goose:
   
   ```
   Query times: 2.3s, 1.8s, 5.2s, 0.3s, 8.1s
   Table sizes: users (1M rows), orders (5M rows)
   Indexes: 3 on users, 1 on orders
   ```
4. goose responds to you with general recommendations:
   
   ```
   Your database seems slow. Some queries are taking over 5 seconds. You might need more indexes.
   ```

### Use Cases[​](#use-cases "Direct link to Use Cases")

MCP Sampling enables powerful capabilities like:

- **Smart documentation tools** that explain code in context
- **Intelligent search** that filters and ranks results
- **Database analyzers** that provide specific optimization recommendations
- **Multi-perspective analysis** where extensions generate and synthesize multiple AI viewpoints

## For Extension Developers[​](#for-extension-developers "Direct link to For Extension Developers")

Want to add MCP Sampling to your own extensions? See our [Building Custom Extensions](https://block.github.io/goose/docs/tutorials/custom-extensions) tutorial to learn more about how MCP servers can leverage goose's AI capabilities.

## Additional Resources[​](#additional-resources "Direct link to Additional Resources")