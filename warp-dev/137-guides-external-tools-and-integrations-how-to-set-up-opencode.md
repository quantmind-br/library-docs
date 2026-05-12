---
title: Set Up OpenCode | Guides | Warp
url: https://docs.warp.dev/guides/external-tools-and-integrations/how-to-set-up-opencode
source: sitemap
fetched_at: 2026-04-29T15:06:41.714750128-03:00
rendered_js: false
word_count: 466
summary: This document provides a comprehensive guide for installing, configuring, and utilizing the OpenCode AI coding agent within the Warp terminal environment.
tags:
    - coding-agent
    - terminal-productivity
    - opencode
    - warp-terminal
    - llm-integration
    - developer-tools
category: guide
optimized: true
optimized_at: 2026-04-29T15:06:41.714750128-03:00
---
OpenCode is an open-source coding agent that runs in your terminal. It supports 75+ LLM providers, features a built-in TUI, and lets you edit code, execute commands, and manage sessions from natural language prompts.

## Prerequisites

- **An LLM provider account** — OpenCode connects to any supported provider (Anthropic, OpenAI, Google, and others) via API key, or use OpenCode Zen for a curated model list
- **macOS, Linux, or Windows (via WSL)** — WSL recommended for best Windows experience

## 1. Install OpenCode

The install script is the fastest method:
```bash
curl -L opencode.ai/install.sh | sh
```

Also available via npm or Homebrew:
```bash
npm install -g opencode-ai
# or
brew install opencode-ai
```

See the [OpenCode docs](https://opencode.ai/docs#install) for additional installation methods including platform-specific binaries and Docker.

When you launch OpenCode inside Warp, Warp auto-detects the agent session and surfaces integrated controls, including rich input, code review, vertical tab metadata, and more.

## 2. Authenticate

OpenCode supports multiple LLM providers. Run the `/connect` command inside OpenCode's TUI to configure a provider, or set API keys as environment variables:

```bash
export OPENAI_API_KEY=your_key_here
export ANTHROPIC_API_KEY=your_key_here
```

Outside the TUI, run `opencode auth login` from the command line for interactive provider setup. Credentials are stored locally in `~/.local/share/opencode/auth.json`.

## 3. Start your first session

Navigate to any project directory and launch OpenCode:
```bash
opencode
```

Try giving it a task:
```
Fix the authentication bug in login.ts
```

OpenCode reads relevant files, proposes changes, and asks for confirmation before modifying anything. Use the `Tab` key to switch between Plan mode (read-only suggestions) and Build mode (applies changes).

## 4. Configure for your project

Initialize OpenCode for your project by running `/init` inside the TUI. This analyzes your codebase and creates an `AGENTS.md` file at your project root:

The `AGENTS.md` file teaches OpenCode your project's structure and conventions. You can also create or edit it manually:

```markdown
# Project Conventions

## Code Style
- Use 2 spaces for indentation
- Prefer const over let

## Testing
- All functions must have unit tests
- Use Vitest for testing
```

Commit the `AGENTS.md` file to Git so your team shares the same project context.

## 5. Set up agent notifications

Warp supports agent notifications for OpenCode through a plugin. If the plugin isn't installed, Warp displays an installation chip in the terminal when you run OpenCode, with setup steps you can follow directly.

> [!tip]
> For manual installation and configuration, see [OpenCode in Warp](https://docs.warp.dev/agent-platform/cli-agents/opencode#setting-up-notifications).

## Productivity Tips

| Feature | How to Use |
|---------|------------|
| **Voice input** | Dictate complex instructions; Warp's voice transcription works with any CLI agent |
| **Images as context** | Paste screenshots of bugs, designs, or error messages into prompts |
| **Visual diffs** | Open Code Review panel (`⌘+Shift++`) after changes to see visual diffs |
| **Run alongside other agents** | Use [vertical tabs](https://docs.warp.dev/warp/terminal/windows/vertical-tabs) to compare outputs |
| **Rich input** | Press `Ctrl+G` for full text editor experience when composing prompts |

## Next Steps

You installed OpenCode, authenticated with a provider, started your first session, and configured it for your project. OpenCode is now set up as a working coding agent in Warp.

#coding-agent #terminal-productivity #opencode #warp-terminal #llm-integration
