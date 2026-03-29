---
title: Client Roots - FastMCP
url: https://gofastmcp.com/clients/roots
source: crawler
fetched_at: 2026-01-22T22:23:02.884905906-03:00
rendered_js: false
word_count: 67
summary: This document explains how to configure static and dynamic roots in a fastmcp client to inform servers about accessible local resources.
tags:
    - fastmcp
    - roots
    - client-configuration
    - local-resources
    - python-sdk
category: guide
---

New in version `2.0.0` Use this when you need to tell servers what local resources the client has access to. Roots inform servers about resources the client can provide. Servers can use this information to adjust behavior or provide more relevant responses.

## Static Roots

Provide a list of roots when creating the client:

```
from fastmcp import Client

client = Client(
    "my_mcp_server.py",
    roots=["/path/to/root1", "/path/to/root2"]
)
```

## Dynamic Roots

Use a callback to compute roots dynamically when the server requests them:

```
from fastmcp import Client
from fastmcp.client.roots import RequestContext

async def roots_callback(context: RequestContext) -> list[str]:
    print(f"Server requested roots (Request ID: {context.request_id})")
    return ["/path/to/root1", "/path/to/root2"]

client = Client(
    "my_mcp_server.py",
    roots=roots_callback
)
```