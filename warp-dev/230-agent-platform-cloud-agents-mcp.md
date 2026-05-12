---
title: MCP servers | Agents | Warp
url: https://docs.warp.dev/agent-platform/cloud-agents/mcp
source: sitemap
fetched_at: 2026-04-29T15:04:41.270247282-03:00
rendered_js: false
word_count: 460
summary: This document explains how to configure and integrate Model Context Protocol (MCP) servers into cloud agents to enable automated interaction with external APIs, local processes, and developer tools.
tags:
    - cloud-agents
    - mcp-servers
    - agent-configuration
    - external-tools
    - api-integration
    - automation
category: configuration
optimized: true
optimized_at: 2026-04-29T15:04:41.270247282-03:00
---
# MCP servers

Cloud agents can call external tools through [Model Context Protocol (MCP) servers](https://modelcontextprotocol.io). This lets agents automatically interact with GitHub, dbt, Sentry, or any custom internal service whenever the workflow requires it.

## When to use MCP servers

Add MCP servers to a cloud agent when it needs to:

- Read from or write to an external API (issue trackers, monitoring tools, cloud services)
- Call local processes that expose MCP endpoints
- Use internal developer tools wrapped in an MCP interface

Agents call MCP tools automatically based on task requirements, without explicit instruction.

## How MCP configuration works

| Method | Syntax |
|--------|--------|
| **At run time** | Pass `--mcp` when calling `oz agent run` or `oz agent run-cloud` |
| **In agent config file** | Define `mcp_servers` in YAML/JSON config file (passed with `-f / --file`) |

The agent config file approach is recommended for repeatable workflows. Full syntax in [[159-reference-cli-mcp-servers]].

## Configuration schema

Each MCP server entry is keyed by a name you choose. A server config must have **exactly one** transport type:

| Transport | Field(s) | When to use |
|----------|----------|-------------|
| `warp_id` | `warp_id` (UUID) | Reference a Warp-shared MCP server |
| `command` | `command`, `args`, `env` | Launch a local executable as an MCP server |
| `url` | `url`, `headers` | Connect to a remote or locally hosted MCP endpoint (SSE) |

### Supported fields

- `warp_id` — UUID of a Warp-shared MCP server (find via `oz mcp list` or **Settings** → **Agents** → **MCP servers**)
- `command` — Executable to launch (stdio transport)
- `args` — Arguments passed to `command` (only valid with `command`)
- `env` — Environment variables passed to the process (only valid with `command`)
- `url` — HTTP or HTTPS endpoint URL (streamable HTTP or SSE transport)
- `headers` — HTTP headers sent with requests (only valid with `url`)

## Example configuration

```json
{
  "github": {
    "url": "https://mcp.example.com/github"
  },
  "dbt": {
    "command": "uvx",
    "args": ["dbt-mcp"],
    "env": {
      "DBT_HOST": "https://example.us1.dbt.com",
      "DBT_SERVICE_TOKEN": "${DBT_SERVICE_TOKEN}"
    }
  }
}
```

## Using in an agent config file

```json
{
  "name": "my-production-agent",
  "model_id": "claude-sonnet-4",
  "system_prompt": "You are a helpful assistant focused on backend development.",
  "environment_id": "SVhg783GBFQHk1OfdPfFU9",
  "mcp_servers": {
    "github": {
      "url": "https://mcp.example.com/github"
    },
    "dbt": {
      "command": "uvx",
      "args": ["dbt-mcp"],
      "env": {
        "DBT_HOST": "https://example.us1.dbt.com",
        "DBT_SERVICE_TOKEN": "${DBT_SERVICE_TOKEN}"
      }
    }
  }
}
```

Run with:
```
oz agent run-cloud --environment <ENV_ID> -f my-agent-config.json --prompt "Check for regressions in the last deploy"
```

## Requirements and defaults

- MCP configuration must be valid JSON (or YAML when embedded in agent config)
- If `mcp_servers` is omitted, the agent runs with no MCP servers enabled
- Each server name must be unique and non-empty
- `warp_id` transport is validated against your Warp account — referenced servers must be accessible to you

## Limitations

> [!warning]
> Warp does not currently support OAuth-based MCP servers for cloud agents. MCP servers requiring browser-based authentication (like some hosted Figma configurations) cannot be used directly.

**Workaround**: Pass Figma mockups as **image context** to the agent, which can then build and test UI against those images.

## Learn more

- [[205-agent-platform-cloud-agents-environments]] — set up runtime context (repo, image, startup commands)
- [[208-agent-platform-cloud-agents-secrets]] — store and inject credentials safely

#tags #mcp-servers #agent-configuration #external-tools
