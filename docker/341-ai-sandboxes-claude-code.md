---
title: Configure Claude Code
url: https://docs.docker.com/ai/sandboxes/claude-code/
source: llms
fetched_at: 2026-01-24T14:14:25.191749344-03:00
rendered_js: false
word_count: 448
summary: This guide explains how to set up, authenticate, and configure Claude Code agents running within a Docker sandboxed environment.
tags:
    - docker-sandbox
    - claude-code
    - anthropic-api
    - containerization
    - cli-configuration
    - docker-desktop
category: guide
---

Availability: Experimental

Requires: Docker Desktop [4.50](https://docs.docker.com/desktop/release-notes/#4500) or later

This guide covers authentication, configuration files, and common options for running Claude Code in a sandboxed environment.

The simplest way to start Claude in a sandbox:

This starts a sandboxed Claude Code agent with the current working directory as its workspace.

Or specify a different workspace:

Claude Code supports various command-line options that you can pass through `docker sandbox run`. Any arguments after the agent name (`claude`) are passed directly to Claude Code inside the sandbox.

### [Continue previous conversation](#continue-previous-conversation)

Resume your most recent conversation:

Or use the long form:

### [Pass a prompt directly](#pass-a-prompt-directly)

Start Claude with a specific prompt:

This starts Claude and immediately processes the prompt.

### [Combine options](#combine-options)

You can combine sandbox options with Claude options:

This creates a sandbox with `DEBUG` set to `1`, enabling debug output for troubleshooting, and continues the previous conversation.

### [Available Claude options](#available-claude-options)

All Claude Code CLI options work through `docker sandbox run`:

- `-c, --continue` - Continue the most recent conversation
- `-p, --prompt` - Read prompt from stdin (useful for piping)
- `--dangerously-skip-permissions` - Skip permission prompts (enabled by default in sandboxes)
- And more - see the [Claude Code documentation](https://docs.claude.com/en/docs/claude-code) for a complete list

Claude sandboxes support the following credential management strategies.

### [Strategy 1: `sandbox` (Default)](#strategy-1-sandbox-default)

On first run, Claude prompts you to enter your Anthropic API key. The credentials are stored in a persistent Docker volume named `docker-claude-sandbox-data`. All future Claude sandboxes automatically use these stored credentials, and they persist across sandbox restarts and deletion.

Sandboxes mount this volume at `/mnt/claude-data` and create symbolic links in the sandbox user's home directory.

> If your workspace contains a `.claude.json` file with a `primaryApiKey` field, you'll receive a warning about potential conflicts. You can choose to remove the `primaryApiKey` field from your `.claude.json` or proceed and ignore the warning.

### [Strategy 2: `none`](#strategy-2-none)

No automatic credential management.

Docker does not discover, inject, or store any credentials. You must authenticate manually inside the container. Credentials are not shared with other sandboxes but persist for the lifetime of the container.

Claude Code can be configured through CLI options. Any arguments you pass after the agent name are passed directly to Claude Code inside the container.

Pass options after the agent name:

For example:

See the [Claude Code CLI reference](https://docs.claude.com/en/docs/claude-code/cli-reference) for a complete list of available options.

For more advanced configurations including environment variables, volume mounts, Docker socket access, and custom templates, see [Advanced configurations](https://docs.docker.com/ai/sandboxes/advanced-config/).

The `docker/sandbox-templates:claude-code` image includes Claude Code with automatic credential management, plus development tools (Docker CLI, GitHub CLI, Node.js, Go, Python 3, Git, ripgrep, jq). It runs as a non-root `agent` user with `sudo` access and launches Claude with `--dangerously-skip-permissions` by default.

- [Advanced configurations](https://docs.docker.com/ai/sandboxes/advanced-config/)
- [Troubleshooting](https://docs.docker.com/ai/sandboxes/troubleshooting/)
- [CLI Reference](https://docs.docker.com/reference/cli/docker/sandbox/)