---
title: Installation - FastMCP
url: https://gofastmcp.com/getting-started/installation
source: crawler
fetched_at: 2026-01-22T22:21:41.279233763-03:00
rendered_js: false
word_count: 283
summary: This document provides comprehensive instructions for installing FastMCP, verifying the setup, and upgrading from previous versions or the official MCP SDK.
tags:
    - fastmcp
    - installation
    - python
    - upgrade-guide
    - dependency-management
    - versioning-policy
category: guide
---

## Install FastMCP

We recommend using [uv](https://docs.astral.sh/uv/getting-started/installation/) to install and manage FastMCP.

```
pip install "fastmcp>=3.0.0b1"
```

Or with uv:

```
uv add "fastmcp>=3.0.0b1"
```

### Optional Dependencies

FastMCP provides optional extras for specific features. For example, to install the background tasks extra:

```
pip install "fastmcp[tasks]==3.0.0b1"
```

See [Background Tasks](https://gofastmcp.com/servers/tasks) for details on the task system.

### Verify Installation

To verify that FastMCP is installed correctly, you can run the following command:

You should see output like the following:

```
$ fastmcp version

FastMCP version:                           3.0.0
MCP version:                               1.25.0
Python version:                            3.12.2
Platform:            macOS-15.3.1-arm64-arm-64bit
FastMCP root path:            ~/Developer/fastmcp
```

### Dependency Licensing

## Upgrading

### From FastMCP 2.x

See the [Upgrade Guide](https://gofastmcp.com/development/upgrade-guide) for a complete list of breaking changes and migration steps.

### From the Official MCP SDK

Upgrading from the official MCP SDK’s FastMCP 1.0 to FastMCP 3.0 is generally straightforward. The core server API is highly compatible, and in many cases, changing your import statement from `from mcp.server.fastmcp import FastMCP` to `from fastmcp import FastMCP` will be sufficient.

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
fastmcp==3.0.0  # Good
fastmcp>=3.0.0  # Bad - may install breaking changes
```

See the full [versioning and release policy](https://gofastmcp.com/development/releases#versioning-policy) for details on our public API, deprecation practices, and breaking change philosophy.

### Looking Ahead: FastMCP 4.0

The MCP Python SDK v2 is expected in early 2026 and will include breaking changes. When released, FastMCP will incorporate these upstream changes in a new major version (FastMCP 4.0). To avoid unexpected breaking changes, we recommend pinning your dependency with an upper bound:

We’ll provide migration guidance when FastMCP 4.0 is released.

## Contributing to FastMCP

Interested in contributing to FastMCP? See the [Contributing Guide](https://gofastmcp.com/development/contributing) for details on:

- Setting up your development environment
- Running tests and pre-commit hooks
- Submitting issues and pull requests
- Code standards and review process