---
title: Quickstart | Mistral Docs
url: https://docs.mistral.ai/mistral-vibe/terminal/quickstart
source: sitemap
fetched_at: 2026-04-26T04:08:32.87745416-03:00
rendered_js: false
word_count: 807
summary: This document provides a comprehensive introduction to the Mistral Vibe terminal agent, covering installation, API key configuration, interactive usage, programmatic execution, and advanced features like custom skills and agent modes.
tags:
    - cli-tool
    - mistral-vibe
    - ai-agent
    - terminal-productivity
    - workflow-automation
    - api-integration
category: tutorial
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Quick guide to get started with Mistral Vibe. See [Configuration](https://docs.mistral.ai/mistral-vibe/terminal/configuration) for full customization options.

## Prerequisites

Ensure you have [installed Vibe](https://docs.mistral.ai/mistral-vibe/terminal/install).

## First Launch

1. Navigate to your project's root directory.
2. Run `vibe`.

This starts the interactive CLI interface. On first run, Vibe:
- Creates a default config at `~/.vibe/config.toml`
- Prompts you to enter your API key if not configured:
  - **Le Chat Pro subscribers**: [Studio Codestral API keys](https://console.mistral.ai/codestral/cli)
  - **Experiment or Scale plan**: [Studio Organization API keys](https://admin.mistral.ai/organization/api-keys)

![Entering the API key on first launch](https://docs.mistral.ai/img/vibekey.png)

- Saves your API key to `~/.vibe/.env` for future use

Alternatively, configure your API key with `vibe --setup`.

## Default Model

Vibe uses **Devstral 2** by default. You can also use Devstral Small 2 or [custom models](https://docs.mistral.ai/mistral-vibe/terminal/configuration#change-providers).

## Interactive Mode

Run `vibe` to enter the interactive chat loop.

**Input shortcuts:**
- **Multi-line input**: `Ctrl+J` or `Shift+Enter` for newline
- **File paths**: `@` symbol for smart autocompletion (e.g., `> Read @src/agent.py`)
- **Shell commands**: prefix with `!` (e.g., `> !ls -l`)
- **External editor**: `Ctrl+G` to edit input in external editor
- **Tool output toggle**: `Ctrl+O`
- **Todo view toggle**: `Ctrl+T`
- **Auto-approve toggle**: `Shift+Tab`

## Slash Commands

| Command | Description |
|---------|-------------|
| `/h`, `/help` | Show help message |
| `/config`, `/theme`, `/model` | Edit configuration |
| `/clear` | Clear conversation history |

## Custom Skills

Define your own slash commands via the skills system. To create a custom slash command:
1. Create a skill directory with a `SKILL.md` file
2. Set `user-invocable = true` in the skill metadata
3. Define the command logic

Custom slash commands appear in the autocompletion menu alongside built-in commands.

Learn more about [Skills](https://docs.mistral.ai/mistral-vibe/agents-skills#skills).

## Agents

Define agents and switch between them with `Shift+Tab`. Built-in agents:

| Agent | Description |
|-------|-------------|
| `default` | Standard Vibe behavior, requests approval for tool execution |
| `plan` | Read-only agent for exploration and planning |
| `auto approve` | Automatically approves all tool executions |

Learn more about [Agents](https://docs.mistral.ai/mistral-vibe/agents-skills#agents).

## Trust Folder System

Vibe includes a trust folder system to ensure you only run the agent in directories you trust.

## Programmatic Mode

Run Vibe non-interactively by piping input or using `--prompt`. Useful for scripting. Uses `auto-approve` mode by default.

```bash
echo "List the files in this directory" | vibe
vibe --prompt "Explain this function" < code.py
```

### Options

| Option | Description |
|--------|-------------|
| `--max-turns N` | Limit maximum assistant turns |
| `--max-price DOLLARS` | Set maximum cost limit in dollars |
| `--enabled-tools TOOL` | Enable specific tools (exact name, glob pattern `bash*`, or regex `re:^serena_.*$`) |
| `--output FORMAT` | Output format: `text` (default), `json` (all messages as JSON), `streaming` (newline-delimited JSON per message) |

## Step-by-Step Confirmation

For substantial tasks (refactors, multi-file updates, cleanups), Vibe splits work into steps and asks for confirmation before proceeding.

Before editing files or running commands, Vibe shows a full preview and asks for confirmation.

![Preview of changes and asking for confirmation](https://docs.mistral.ai/img/vibepermission.png)

After each step, you see exactly what was executed and the resulting output.

![Generated output and completed steps](https://docs.mistral.ai/img/vibestep.png)

## Getting Help

- Type `/help`
- Check the [README](https://github.com/mistralai/mistral-vibe/blob/main/README.md)
- Reach out on the [Mistral Discord](https://discord.gg/mistralai)
- Contact [support team](https://help.mistral.ai/en/articles/347458-how-do-i-contact-mistral-ai-support)

#cli-tool #mistral-vibe #ai-agent