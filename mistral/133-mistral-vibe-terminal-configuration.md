---
title: Configuration | Mistral Docs
url: https://docs.mistral.ai/mistral-vibe/terminal/configuration
source: sitemap
fetched_at: 2026-04-26T04:08:29.624835369-03:00
rendered_js: false
word_count: 826
summary: This document provides a comprehensive guide on configuring and customizing Mistral Vibe, covering API key management, agent setup, MCP server integration, and workspace security.
tags:
    - configuration
    - api-setup
    - customization
    - mcp-servers
    - environment-variables
    - security-settings
category: configuration
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Mistral Vibe configured via `config.toml` — looks first in `./.vibe/config.toml`, then `~/.vibe/config.toml`.

## Mistral API Key

Requires Codestral API key. Create based on your plan:
- **Le Chat Pro**: [Studio › Codestral › API keys](https://console.mistral.ai/codestral/cli)
- **Experiment/Scale (pay-as-you-go)**: [Studio › Organization › API keys](https://admin.mistral.ai/organization/api-keys)

### Configuration Methods

1. **Interactive Setup** (recommended): Prompts for key on first run, saved to `~/.vibe/.env`
2. **Environment Variables**: Set `MISTRAL_API_KEY`
3. **`.env` File**: Create `~/.vibe/.env` with API keys

Environment variables take precedence over `.env` file. `.env` is for API keys; general config goes in `config.toml`.

## Custom System Prompts

Create `~/.vibe/prompts/<name>.md` and set `system_prompt_id` to the filename (without `.md`):
```toml
system_prompt_id = "my_custom_prompt"
```

## Custom Agents

Create `~/.vibe/agents/<name>.toml` files. Use with `--agent <name>` flag.

Example `~/.vibe/agents/redteam.toml`:
```toml
name = "redteam"
safety = "destructive"
# requires ~/.vibe/prompts/redteam.md
```

## Providers and Models

Create presets in `config.toml`:
```toml
[providers.<name>]
...

[models.<alias>]
...

[defaults]
active_model = "<alias>"
```

Models also accessible via `/config` command to change on the fly.

## MCP Servers

Configure under `mcp_servers` section. Supported transports:
- `http`: Standard HTTP
- `streamable-http`: HTTP with streaming
- `stdio`: Standard input/output (local processes)

| Field | Description |
|-------|-------------|
| `name` | Short alias (used in tool names) |
| `transport` | Transport type |
| `url` | Base URL for HTTP |
| `headers` | Additional HTTP headers |
| `api_key_env` | Environment variable for API key |
| `command` | Command for stdio transport |
| `args` | Additional arguments |

MCP tools named `{server_name}_{tool_name}`. Support environment variables, custom timeouts, enhanced security.

Example:
```toml
[mcp_servers.serena]
transport = "stdio"
command = "npx"
args = ["-y", "@serenamcp/serena-mcp"]
```

## Session Continuation

- **`--continue` / `-c`**: Continue from most recent saved session
- **`--resume SESSION_ID`**: Resume specific session (supports partial matching)

Session logging required (enabled by default).

## Tool Control

Control active tools with `enabled_tools` and `disabled_tools` (exact names, glob patterns, regex with `re:` prefix).

> [!warning]
> MCP tool names use underscores (`serena_list`, not `serena.list`). Regex uses fullmatch.

## Environment Variables

- `VIBE_HOME`: Override config directory (default `~/.vibe/`)
- `--workdir`: Specify working directory

## Trust Folders

Safety system prevents accidental execution in sensitive directories. Trusted folders stored in `~/.vibe/trusted_folders.toml`. First run in new directory prompts for confirmation.

## Auto-Update

Enabled by default. Disable in `config.toml`:
```toml
auto_update = false
``` #configuration #api-setup #mcp-servers