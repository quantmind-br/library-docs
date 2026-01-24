---
title: Docs MCP
url: https://platform.openai.com/docs/docs-mcp.md
source: llms
fetched_at: 2026-01-24T16:12:39.30344902-03:00
rendered_js: false
word_count: 336
summary: This document provides instructions for connecting to the OpenAI developer documentation MCP server to access and search API documentation directly within IDEs and tools like Codex, VS Code, and Cursor.
tags:
    - openai
    - mcp-server
    - developer-docs
    - model-context-protocol
    - codex
    - vs-code
    - cursor
category: configuration
---

Docs MCP
========

Search and read OpenAI developer docs from your editor.

OpenAI hosts a public Model Context Protocol (MCP) server for developer documentation on developers.openai.com and platform.openai.com.

**Server URL (streamable HTTP):** `https://developers.openai.com/mcp`

What it provides
----------------

*   Read-only access to OpenAI developer documentation (search + page content).
*   A way to pull documentation into your agent's context while you work.

This MCP server is documentation-only. It does not call the OpenAI API on your behalf.

Quickstart
----------

### Codex

You can connect Codex to [MCP servers](https://developers.openai.com/codex/mcp) in the [CLI](https://developers.openai.com/codex/cli) or [IDE extension](https://developers.openai.com/codex/ide). The configuration is shared between both so you only have to set it up once.

Add the server using the Codex CLI:

```bash
codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp
```

Verify it's configured:

```bash
codex mcp list
```

Alternatively, you can add it in `~/.codex/config.toml` directly:

```toml
[mcp_servers.openaiDeveloperDocs]
url = "https://developers.openai.com/mcp"
```

### VS Code (GitHub Copilot Agent mode)

VS Code supports MCP servers when using GitHub Copilot in Agent mode.

Click the following link to add the Docs MCP to VS Code:

[Install in VS Code](/docs/docs-mcp)

Alternatively, you can manually add a `.vscode/mcp.json` in your project root:

```json
{
  "servers": {
    "openaiDeveloperDocs": {
      "type": "http",
      "url": "https://developers.openai.com/mcp"
    }
  }
}
```

To have VS Code reliably use the MCP server, add this snippet to your `AGENTS.md`:

```text
Always use the OpenAI developer documentation MCP server if you need to work with the OpenAI API, ChatGPT Apps SDK, Codex, or related docs without me having to explicitly ask.
```

Open Copilot Chat, switch to **Agent** mode, enable the server in the tools picker, and ask an OpenAI-related question like:

> Look up the request schema for Responses API tools in the OpenAI developer docs and summarize the required fields.

### Cursor

Cursor has native MCP support and reads configuration from `mcp.json`.

Install with Cursor:

[Install in Cursor](https://cursor.com/en-US/install-mcp?name=openaiDeveloperDocs&config=eyJ1cmwiOiAiaHR0cHM6Ly9kZXZlbG9wZXJzLm9wZW5haS5jb20vbWNwIn0%3D)

Alternatively, create a `~/.cursor/mcp.json` (macOS/Linux) and add:

```json
{
  "mcpServers": {
    "openaiDeveloperDocs": {
      "url": "https://developers.openai.com/mcp"
    }
  }
}
```

To have Cursor reliably use the MCP server, add this snippet to your `AGENTS.md`:

```text
Always use the OpenAI developer documentation MCP server if you need to work with the OpenAI API, ChatGPT Apps SDK, Codex, or related docs without me having to explicitly ask.
```

Restart Cursor and ask Cursor's agent an OpenAI-related question like:

> Look up the request schema for Responses API tools in the OpenAI developer docs and summarize the required fields.

Tips
----

*   If you don't have the snippet in the AGENTS.md file, you need to explicitly tell your agent to consult the Docs MCP server for the answer.
*   If you have more than one MCP server, keep server names short and descriptive to aid the agent in selecting the server.