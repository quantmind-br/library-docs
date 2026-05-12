---
title: Model Context Protocol (MCP) | Agents | Warp
url: https://docs.warp.dev/agent-platform/warp-agents/agent-context/mcp
source: sitemap
fetched_at: 2026-04-29T15:04:09.751129716-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-29T18:15:00.000Z
tags:
    - mcp-servers
    - warp-agents
    - configuration
    - authentication
    - api-integration
    - plugin-management
    - developer-tools
category: guide
word_count: 546
---
MCP servers extend Warp's local agents by exposing custom tools or data sources through a standardized interface. Warp supports Streamable HTTPS, SSE, custom headers, and environment variables.

> [!info]
> MCP is an open source protocol. See the official [MCP documentation](https://modelcontextprotocol.io/introduction) for details.

> [!note]
> This page covers MCP servers for local agents. For cloud agents, see [[230-agent-platform-cloud-agents-mcp|MCP Servers for cloud agents]].

## Accessing MCP Server settings

**Settings** → **Agents** → **Warp Agent** → **Manage MCP servers**

This shows all configured MCP servers and their running status. Closing Warp with an MCP server running keeps it running on next launch; stopped servers remain stopped.

## Adding an MCP Server

Click **+ Add**. Configurations from most MCP clients can be copied and pasted directly.

| Server Type | Description |
|-------------|-------------|
| CLI Server (Command) | Provide a startup command; Warp launches it on startup and shuts it down on exit |

> [!info]
> Always set `working_directory` explicitly when your MCP server command or args include relative paths.

### Adding multiple MCP servers

Add multiple servers by pasting a JSON snippet under `mcpServers`, keyed by unique names:

```json
{
  "mcpServers": {
    "filesystem": { ... },
    "github": { ... },
    "notes": { ... }
  }
}
```

### File-based MCP servers

Enable file-based servers: **Settings** → **Agents** → **MCP servers** → toggle **File-based MCP Servers**.

| Scope | Behavior |
|-------|----------|
| Global/user-scoped | Spawned on Warp startup; available in any session |
| Project-scoped | Spawned when entering a repo with supported config; available within that project |

**Supported providers:**
- **Codex** — reads `~/.codex/config.toml` (global) and `.codex/config.toml` (project-scoped)

> [!note]
> File-based servers requiring OAuth show an authentication modal on first spawn; credentials are saved for future spawns.

## Managing MCP servers

Start, stop, rename, or delete servers from the MCP servers page. Running servers show available tools and resources.

### Sharing MCP servers

Click the share icon. Sensitive `env` values are automatically scrubbed and replaced with variables.

Teammates find shared servers under **Shared** in their MCP settings and enter their own `env` values.

## Authentication

| Method | Description |
|--------|-------------|
| Environment variables | Pass API key or access token via server's environment variables |
| OAuth login | One-click browser-based authentication; credentials stored securely on device |
| Custom Headers | Pass Authentication Bearer token via headers variable |

> [!tip]
> Some models work better with MCP servers than others. If having trouble, try a different model.

### Debugging authentication issues

To reset auth tokens: `rm -rf ~/.mcp-auth`

> [!warning]
> This deletes all MCP auth tokens stored locally; re-authentication required.

## Debugging MCP

Click **View Logs** on a server to check for errors.

> [!warning]
> Remove sensitive information before sharing logs, as they may contain API keys.

Many SSE-based MCP servers treat the URL like a password.

## Where logs are stored

`~/.warp/mcp-logs/`

## MCP server configuration examples

### Engineering & Ops

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/directory"]
    }
  }
}
```

### Design & Collaboration

**Figma Remote MCP Server (Recommended)**
1. **Warp Drive** → **MCP Servers** → **+ Add**
2. Paste configuration and authenticate via browser

**Figma Local MCP Server**
1. In Figma: **Preferences** → **Enable local MCP Server**
2. Enter configuration in **Warp** → **Warp Drive** → **MCP Servers** → **+ Add**

## MCP server demos

See [Warp Guides](/guides) for demos and walkthroughs:
- [**GitHub MCP**](https://docs.warp.dev/guides/mcp-servers/github-mcp-summarizing-open-prs-and-creating-gh-issues) — access repositories, issues, and pull requests through MCP
