---
title: MCP Servers | Reference | Warp
url: https://docs.warp.dev/reference/cli/mcp-servers
source: sitemap
fetched_at: 2026-04-29T15:05:02.076527862-03:00
rendered_js: false
word_count: 191
summary: This document explains how to integrate and configure Model Context Protocol (MCP) servers with Warp agents using the CLI command line interface.
tags:
    - mcp
    - warp-agents
    - cli-commands
    - configuration
    - integration
    - environment-variables
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
MCP servers connect agents to external systems like GitHub, Linear, or Sentry. Use the `--mcp` flag with `oz agent run` or `oz agent run-cloud` to use an [MCP server](https://docs.warp.dev/agent-platform/warp-agents/mcp).

For conceptual overview, configuration schema, full examples, and limitations, see [MCP Servers](https://docs.warp.dev/agent-platform/cloud-agents/mcp) in Cloud Agents docs.

## Using the `--mcp` flag

Accepts three formats:
- **UUID** — reference a Warp-shared MCP server by UUID (find with `oz mcp list`)
- **Inline JSON** — pass full MCP JSON configuration as a string
- **File path** — path to a JSON file containing MCP configuration

Repeat `--mcp` to include multiple servers.

### Passing MCP servers by UUID

1. Locate the UUID using `oz mcp list`:
```
$ oz mcp list
+--------------------------------------+--------+
|UUID                                  |Name    |
+==============================================+
|1deb1b14-b6e5-4996-ae99-233b7555d2d0  |github  |
|--------------------------------------+--------+
|65450c32-9eb1-4c57-8804-0861737acbc4 |linear  |
|--------------------------------------+--------+
|d94ade64-0e73-47a6-b3ee-14e5afec3d90 |Sentry  |
+--------------------------------------+--------+
```
Or copy from **Settings** > **Agents** > **MCP servers** in Warp.

2. Pass the UUID to `--mcp`:
```
$ oz agent run --mcp "1deb1b14-b6e5-4996-ae99-233b7555d2d0" --prompt "who last updated the README?"
```

### Passing MCP servers as inline JSON or a file

```
# Inline JSON
$ oz agent run --mcp '{"github": {"url": "https://api.githubcopilot.com/mcp/"}}' --prompt "list open issues"
# From a file
$ oz agent run --mcp ./my-mcp-config.json --prompt "list open issues"
```

Example file:
```json
{
  "github": {
    "url": "https://api.githubcopilot.com/mcp/"
  },
  "sentry": {
    "command": "npx",
    "args": ["-y", "mcp-remote@latest", "https://mcp.sentry.dev/mcp"]
  }
}
```

### Combining multiple servers

```
$ oz agent run \
  --mcp "1deb1b14-b6e5-4996-ae99-233b7555d2d0" \
  --mcp '{"sentry": {"url": "https://mcp.sentry.dev/sse"}}' \
  --prompt "open a PR that fixes the top Sentry error"
```

## Environment variables on remote machines

Warp syncs MCP server configuration between machines, but **does not sync environment variables**. Set required secrets manually on remote machines:

```bash
export MY_MCP_SERVER_ACCESS_TOKEN="..."
$ oz agent run --mcp "904a8936-fa82-4571-b1d6-166c26197981" --prompt "use my MCP server to check for errors"
```

## Learn more

- [Secrets](https://docs.warp.dev/agent-platform/cloud-agents/secrets) — store credentials so agents access them at runtime without exposing them in config files
