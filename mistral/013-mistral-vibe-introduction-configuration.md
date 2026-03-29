---
title: Configuration | Mistral Docs
url: https://docs.mistral.ai/mistral-vibe/introduction/configuration#change-providers
source: crawler
fetched_at: 2026-01-29T07:34:23.018547765-03:00
rendered_js: false
word_count: 814
summary: A guide providing instructions and details for configuring Mistral AI models and environment settings.
tags:
    - mistral
    - configuration
    - setup
    - parameters
category: guide
---

Vibe is configured via a `config.toml` file. It looks for this file first in `./.vibe/config.toml` and then falls back to `~/.vibe/config.toml`. For `~/.vibe/config.toml`, you can open the configuration file with, for example:

### Mistral API Key

You can get your Mistral API key from [here](https://console.mistral.ai/codestral/vibe).  
Devstral 2 is currently **free to use**; create an account with either the Experiment or Scale Up (recommended) plan, and you will be free to use it with Mistral Vibe.

Vibe supports multiple ways to configure your API keys:

1. **Interactive Setup (Recommended for first-time users)**: When you run Vibe for the first time or if your API key is missing, Vibe will prompt you to enter it. The key will be securely saved to `~/.vibe/.env` for future sessions.
2. **Environment Variables**: Set your API key as an environment variable:
3. **`.env` File**: Create a `.env` file in `~/.vibe/` and add your API keys: Vibe automatically loads API keys from `~/.vibe/.env` on startup. Environment variables take precedence over the `.env` file if both are set.

The `.env` file is specifically for API keys and other provider credentials. General Vibe configuration should be done in `config.toml`.

### Custom System Prompts and Agent Configurations

You can customize Vibe's behavior by modifying prompts and agent configurations.

You can create custom system prompts to replace the default one (`prompts/cli.md`). Create a markdown file in the `~/.vibe/prompts/` directory with your custom prompt content.

To use a custom system prompt, set the `system_prompt_id` in your configuration to match the filename (without the `.md` extension):

This will load the prompt from `~/.vibe/prompts/my_custom_prompt.md`.

You can create custom agent configurations for specific use cases (e.g., red-teaming, specialized tasks) by adding agent-specific TOML files in the `~/.vibe/agents/` directory. To use a custom agent, run Vibe with the `--agent` flag:

Vibe will look for a file named `my_custom_agent.toml` in the agents directory and apply its configuration.

Example custom agent configuration (`~/.vibe/agents/redteam.toml`):

This implies that you have set up a redteam prompt named `~/.vibe/prompts/redteam.md`.

We allow users to change providers and models behind Vibe, for this you need to edit the `config.toml` file as follows:

- Create a new Provider preset in the config file:
- Create a new Model preset:
- Set the `active_model` in the config file to the alias:

Models created are also accessible via Vibe directly with the `/config` command, allowing you to change the model on the fly.

### Configuring MCP Servers

You can configure MCP (Model Context Protocol) servers to extend Vibe's capabilities. Add MCP server configurations under the `mcp_servers` section:

Supported transports:

- `http`: Standard HTTP transport
- `streamable-http`: HTTP transport with streaming support
- `stdio`: Standard input/output transport (for local processes) Key fields:
- `name`: A short alias for the server (used in tool names)
- `transport`: The transport type
- `url`: Base URL for HTTP transports
- `headers`: Additional HTTP headers
- `api_key_env`: Environment variable containing the API key
- `command`: Command to run for stdio transport
- `args`: Additional arguments for stdio transport

MCP tools are named using the pattern `{server_name}_{tool_name}` and can be configured with permissions like built-in tools:

MCP Servers also support:

- **Environment variables**: Set environment variables for MCP servers (stdio transport)
- **Custom timeouts**: Configure startup and tool execution timeouts
- **Enhanced security**: Better API key handling

Example with environment variables and timeouts:

### Session Continuation and Resumption

Vibe supports continuing from previous sessions:

- **`--continue`** or **`-c`** : Continue from the most recent saved session
- **`--resume SESSION_ID`** : Resume a specific session by ID (supports partial matching)

Session logging is required for these features to work, it's enabled by default.

### Controlling Tool Availability

You can control which tools are active using `enabled_tools` and `disabled_tools`. These fields support exact names, glob patterns, and even regular expressions with a `re:` prefix.

Examples:

- MCP tool names use underscores, e.g., `serena_list` not `serena.list`.
- Regex patterns are matched against the full tool name using fullmatch.

### Customize Home Directory

By default, Vibe stores its configuration in `~/.vibe/`. You can override this by setting the `VIBE_HOME` environment variable:

This affects where Vibe looks for:

- `config.toml` - Main configuration
- `.env` - API keys
- `agents/` - Custom agent configurations
- `prompts/` - Custom system prompts
- `tools/` - Custom tools
- `logs/` - Session logs

To run code, enable code execution and file creation in Settings &gt; Capabilities.

### Define a Working Directory

Use the `--workdir` option to specify a working directory:

This is useful when you want to run Vibe from a different location than your current directory.

### Manage which folders you trust

Vibe includes a trust folder system to ensure you only run the agent in directories you trust. When you first run Vibe in a new directory, it may ask you to confirm whether you trust the folder.

Trusted folders are remembered for future sessions. You can manage trusted folders through its configuration file `~/.vibe/trusted_folders.toml`.

This safety feature helps **prevent accidental execution in sensitive directories**.

### Auto-Update

Vibe includes an automatic update feature that keeps your installation current. This is enabled by default.

To disable auto-updates, add this to your `config.toml`: