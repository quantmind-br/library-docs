---
title: Reading Resources - FastMCP
url: https://gofastmcp.com/clients/resources
source: crawler
fetched_at: 2026-01-22T22:23:01.500875603-03:00
rendered_js: false
word_count: 171
summary: This document explains how to read static and dynamic resources from MCP servers using URIs, covering content types, templates, multi-server access, and versioning.
tags:
    - mcp-client
    - resource-handling
    - uri-templates
    - data-fetching
    - python-sdk
    - binary-data
category: guide
---

New in version `2.0.0` Use this when you need to read data from server-exposed resources like configuration files, generated content, or external data sources. Resources are data sources exposed by MCP servers. They can be static files with fixed content, or dynamic templates that generate content based on parameters in the URI.

Read a resource using its URI:

```
async with client:
    content = await client.read_resource("file:///path/to/README.md")
    # content -> list[TextResourceContents | BlobResourceContents]

    # Access text content
    if hasattr(content[0], 'text'):
        print(content[0].text)

    # Access binary content
    if hasattr(content[0], 'blob'):
        print(f"Binary data: {len(content[0].blob)} bytes")
```

Resource templates generate content based on URI parameters. The template defines a pattern like `weather://{{city}}/current`, and you fill in the parameters when reading:

```
async with client:
    # Read from a resource template
    weather_content = await client.read_resource("weather://london/current")
    print(weather_content[0].text)
```

## Content Types

Resources return different content types depending on what they expose. Text resources include configuration files, JSON data, and other human-readable content:

```
async with client:
    content = await client.read_resource("resource://config/settings.json")

    for item in content:
        if hasattr(item, 'text'):
            print(f"Text content: {item.text}")
            print(f"MIME type: {item.mimeType}")
```

Binary resources include images, PDFs, and other non-text data:

```
async with client:
    content = await client.read_resource("resource://images/logo.png")

    for item in content:
        if hasattr(item, 'blob'):
            print(f"Binary content: {len(item.blob)} bytes")
            print(f"MIME type: {item.mimeType}")

            # Save to file
            with open("downloaded_logo.png", "wb") as f:
                f.write(item.blob)
```

## Multi-Server Clients

When using multi-server clients, resource URIs are prefixed with the server name:

```
async with client:  # Multi-server client
    weather_icons = await client.read_resource("weather://weather/icons/sunny")
    templates = await client.read_resource("resource://assistant/templates/list")
```

## Version Selection

New in version `3.0.0` When a server exposes multiple versions of a resource, you can request a specific version:

```
async with client:
    # Read the highest version (default)
    content = await client.read_resource("data://config")

    # Read a specific version
    content_v1 = await client.read_resource("data://config", version="1.0")
```

See [Metadata](https://gofastmcp.com/servers/versioning#version-discovery) for how to discover available versions.

## Raw Protocol Access

For complete control, use `read_resource_mcp()` which returns the full MCP protocol object:

```
async with client:
    result = await client.read_resource_mcp("resource://example")
    # result -> mcp.types.ReadResourceResult
```