---
title: Installation - FastMCP
url: https://gofastmcp.com/v2/getting-started/installation
source: crawler
fetched_at: 2026-01-22T22:22:06.975348706-03:00
rendered_js: false
word_count: 208
summary: This document provides instructions for installing, verifying, and upgrading FastMCP, along with details on its semantic versioning policy and contribution guidelines.
tags:
    - fastmcp
    - installation
    - python-sdk
    - versioning-policy
    - mcp-protocol
    - migration-guide
category: guide
---

## Install FastMCP

We recommend using [uv](https://docs.astral.sh/uv/getting-started/installation/) to install and manage FastMCP. If you plan to use FastMCP in your project, you can add it as a dependency with:

Alternatively, you can install it directly with `pip` or `uv pip`:

### Verify Installation

To verify that FastMCP is installed correctly, you can run the following command:

You should see output like the following:

```
$ fastmcp version

FastMCP version:                           2.11.3
MCP version:                               1.12.4
Python version:                            3.12.2
Platform:            macOS-15.3.1-arm64-arm-64bit
FastMCP root path:            ~/Developer/fastmcp
```

### Dependency Licensing

## Upgrading from the Official MCP SDK

Upgrading from the official MCP SDK’s FastMCP 1.0 to FastMCP 2.0 is generally straightforward. The core server API is highly compatible, and in many cases, changing your import statement from `from mcp.server.fastmcp import FastMCP` to `from fastmcp import FastMCP` will be sufficient.

```
# Before
# from mcp.server.fastmcp import FastMCP

# After
from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")
```

## Versioning Policy

FastMCP follows semantic versioning with pragmatic adaptations for the rapidly evolving MCP ecosystem. Breaking changes may occur in minor versions (e.g., 2.3.x to 2.4.0) when necessary to stay current with the MCP Protocol. For production use, always pin to exact versions:

```
fastmcp==2.11.0  # Good
fastmcp>=2.11.0  # Bad - will install breaking changes
```

See the full [versioning and release policy](https://gofastmcp.com/v2/development/releases#versioning-policy) for details on our public API, deprecation practices, and breaking change philosophy.

## Contributing to FastMCP

Interested in contributing to FastMCP? See the [Contributing Guide](https://gofastmcp.com/v2/development/contributing) for details on:

- Setting up your development environment
- Running tests and pre-commit hooks
- Submitting issues and pull requests
- Code standards and review process