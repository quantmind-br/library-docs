---
title: CLI Quickstart | Reference | Warp
url: https://docs.warp.dev/reference/cli/quickstart
source: sitemap
fetched_at: 2026-04-29T15:04:58.822505059-03:00
rendered_js: false
word_count: 247
summary: This guide provides a foundational walkthrough for installing, authenticating, and running local and cloud-based agents using the Oz CLI.
tags:
    - oz-cli
    - agent-automation
    - command-line-tool
    - mcp-servers
    - getting-started
    - cloud-agents
category: guide
optimized: true
optimized_at: 2026-04-29T18:00:00Z
---
Get started with the Oz CLI in under 5 minutes: install, authenticate, run your first agent, and optionally connect MCP servers.

## 1. Install the CLI

The CLI is included with the [Warp desktop app](https://docs.warp.dev/getting-started/installation-and-setup). If not installed, see [Installing the CLI](https://docs.warp.dev/reference/cli/cli#installing-the-cli) for all platforms.

## 2. Authenticate

Interactive login for local development:

```bash
oz login
```

Opens a sign-in URL in your terminal. Works on local and remote machines without API keys.

> [!tip]
> **CI/headless environments:** Use an API key instead. Create one in **Settings** → **Cloud platform** → **Oz Cloud API Keys**. See [API Keys](https://docs.warp.dev/reference/cli/api-keys) for guidance on personal vs. team keys.

## 3. Run an agent

```bash
oz run
```

Uses the default agent profile, loads MCP servers, and runs locally. The agent executes autonomously with output streamed to your terminal. Sessions are tracked on Warp's backend for observability and collaboration.

## 4. Run a cloud agent (optional)

Cloud agents run in a remote environment with repositories cloned and dependencies installed.

1. Create an environment via `/create-environment` in Warp or follow the [Cloud Agents Quickstart](https://docs.warp.dev/agent-platform/cloud-agents/quickstart).
2. Run with your environment ID (find via `oz environment list`):

```bash
oz run --environment <ENV_ID>
```

## 5. Add MCP context (optional)

Connect MCP servers for external tools (GitHub, Linear, etc.):

```bash
oz run --mcp '{"servers": {"github": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-github"]}}}'
```

See [MCP Servers](https://docs.warp.dev/reference/cli/mcp-servers) for all supported formats including UUID references and multi-server configurations.

## Next steps

- [MCP Servers](https://docs.warp.dev/reference/cli/mcp-servers) — connect agents to external systems
- [API Keys](https://docs.warp.dev/reference/cli/api-keys) — automate authentication
- [`oz help`](https://docs.warp.dev/reference/cli/cli) — CLI reference for all commands
- [Oz CLI reference](https://docs.warp.dev/reference/cli/cli) — platform-specific installation, authentication, and configuration