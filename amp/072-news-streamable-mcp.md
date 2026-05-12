---
title: Streamable Transport for MCP
url: https://ampcode.com/news/streamable-mcp
source: crawler
fetched_at: 2026-02-06T02:08:44.402232609-03:00
rendered_js: false
word_count: 43
summary: This document explains Amp's default adoption of streamable HTTP transport for MCP servers, including support for Server-Sent Events fallback and remote server compatibility.
tags:
    - amp
    - mcp-server
    - streamable-http
    - server-sent-events
    - model-context-protocol
    - transport-layer
category: concept
---

Amp now uses [streamable HTTP transport](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#streamable-http) for MCP servers by default with a fallback to Server-Sent Events.

That allows you to connect to your own MCP servers hosted on [Cloudflare](https://blog.cloudflare.com/streamable-http-mcp-servers-python/) or use other remote servers such as `https://learn.microsoft.com/api/mcp`.

![Streamable HTTP transport in action](https://static.ampcode.com/news/streamable-mcp.png)