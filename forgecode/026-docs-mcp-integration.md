---
title: ForgeCode
url: https://forgecode.dev/docs/mcp-integration/
source: sitemap
fetched_at: 2026-03-29T14:52:02.614124712-03:00
rendered_js: false
word_count: 462
summary: This document provides comprehensive documentation for MCP (Model Context Protocol) integration in ForgeCode, covering how to connect agents to external tools, APIs, and services through command-line interface operations.
tags:
    - mcp
    - forgecode
    - api-integration
    - external-tools
    - command-line
    - agent-configuration
    - tool-connectivity
category: reference
---

MCP lets ForgeCode connect agents to external tools, APIs, and services.

With MCP, your agents can:

- Call external APIs and web services
- Use specialized tools from local or remote servers
- Automate browser workflows
- Connect to internal services and data systems

Start with one command, confirm it loaded, then use the tools.

### `forge mcp import`[​](#forge-mcp-import "Direct link to forge-mcp-import")

Import one or more MCP servers from a JSON string.

**Usage**

**Options**

- `-s, --scope <SCOPE>`: `local` or `user` (default: `local`)
- `--porcelain`: machine-readable output

**Examples**

Add multiple servers to local scope:

Add a server to user scope:

Typical output:

### `forge mcp list`[​](#forge-mcp-list "Direct link to forge-mcp-list")

List configured MCP servers.

**Usage**

**Options**

- `--porcelain`: machine-readable output

### `forge mcp show`[​](#forge-mcp-show "Direct link to forge-mcp-show")

Show full configuration for one server.

**Usage**

**Options**

- `--porcelain`: machine-readable output

Shows command or URL, arguments, environment variables, and final resolved config.

### `forge mcp remove`[​](#forge-mcp-remove "Direct link to forge-mcp-remove")

Remove one MCP server from a selected scope.

**Usage**

**Options**

- `-s, --scope <SCOPE>`: `local` or `user` (default: `local`)
- `--porcelain`: machine-readable output

**Examples**

### `forge mcp reload`[​](#forge-mcp-reload "Direct link to forge-mcp-reload")

Reload MCP servers after configuration changes.

**Usage**

**Options**

- `--porcelain`: machine-readable output

Use this after editing `.mcp.json` manually.

If you prefer direct file editing, create or update `.mcp.json`.

### Server configuration types[​](#server-configuration-types "Direct link to Server configuration types")

#### Command-based server[​](#command-based-server "Direct link to Command-based server")

#### URL-based server[​](#url-based-server "Direct link to URL-based server")

### Scope and precedence[​](#scope-and-precedence "Direct link to Scope and precedence")

MCP configuration can exist in two places:

1. **Local scope**: `.mcp.json` in the current project
2. **User scope**: global ForgeCode config directory

Local scope wins over user scope when both define the same server.

> **Note** Find your resolved configuration path by running `/info` in ForgeCode Shell.

### Disable a server without deleting it[​](#disable-a-server-without-deleting-it "Direct link to Disable a server without deleting it")

Set `"disable": true` on a server entry.

Behavior:

- `"disable": true`: server is ignored and not loaded
- `"disable": false` or omitted: server loads normally

After you add a server, tool registration is automatic.

You do not need per-agent setup.

To verify which MCP tools are available to your current agent, run:

Use this whenever you switch agents and want to confirm the active tool list.

### Browser automation[​](#browser-automation "Direct link to Browser automation")

Use this for UI testing, data extraction, and scripted page interactions.

### External API integration[​](#external-api-integration "Direct link to External API integration")

Use this for real-time data access and API-backed workflows.

### Development tool integration[​](#development-tool-integration "Direct link to Development tool integration")

Use this for database operations, schema work, and migration tooling.

- Store secrets in environment variables, not inline config
- Grant minimum server permissions
- Prefer HTTPS for URL-based servers
- Rotate API keys and access tokens regularly

### Server connection failures[​](#server-connection-failures "Direct link to Server connection failures")

- Verify server URL and port
- Check network reachability
- Confirm required environment variables
- Validate credentials and tokens

### Command execution failures[​](#command-execution-failures "Direct link to Command execution failures")

- Verify command path and arguments
- Check runtime dependencies
- Confirm file permissions
- Re-check environment variables

### Configuration issues[​](#configuration-issues "Direct link to Configuration issues")

- Validate `.mcp.json` syntax
- Confirm local vs user scope expectations
- Check whether the server is disabled
- Run `forge mcp list` to confirm loaded servers

Add one server you need today, verify it with `forge mcp list`, and use it in your next agent session. That gives you the fastest path to a real MCP workflow.