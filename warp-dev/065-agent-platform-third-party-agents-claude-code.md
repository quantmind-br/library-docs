---
title: Claude Code | Agents | Warp
url: https://docs.warp.dev/agent-platform/third-party-agents/claude-code
source: sitemap
fetched_at: 2026-04-29T15:04:13.120008599-03:00
rendered_js: false
word_count: 363
summary: This document outlines the integration between Claude Code and the Warp terminal, focusing on installation procedures for agent notifications and an overview of supported productivity features.
tags:
    - claude-code
    - warp-terminal
    - terminal-integration
    - agent-notifications
    - coding-tools
    - developer-productivity
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Claude Code is Anthropic's agentic coding tool that operates directly in your terminal. Warp auto-detects Claude Code, providing rich input controls, code review, agent notifications, and other integrated features.

For full Claude Code documentation, see the [official docs](https://code.claude.com/docs). For installation, authentication, and productivity tips, see the [How to set up Claude Code](https://docs.warp.dev/guides/integrations/how-to-set-up-claude-code) guide.

## Setting up notifications

Warp surfaces in-app and desktop alerts when Claude Code needs your input (command approval, code review, error intervention). A plugin enables this.

### Auto-install

Each time you run Claude Code without the notification plugin, a notification chip offers one-click installation. Click to install — Warp immediately starts receiving notifications.

### Manual install

> [!info]
> The notification plugin requires `jq`. Install with `brew install jq` on macOS if not already available.

From inside Claude Code:

```bash
claude plugin marketplace install claude-code-warp
```

From your terminal (outside of Claude Code):

```bash
claude plugin marketplace add claude-code-warp
```

After installing, restart Claude Code or run `/reload-plugins` to activate.

> [!info]
> If installation fails, remove first with `claude plugin marketplace remove claude-code-warp`, then re-run the install commands.

### Installation instructions banner

If auto-install doesn't work, or when running over SSH or on a remote machine, Warp displays an installation instructions banner directly in the terminal with step-by-step commands.

For plugin source and updates, see the [claude-code-warp GitHub repository](https://github.com/warpdotdev/claude-code-warp).

## Supported Warp features

| Feature | Description |
|---|---|
| Agent notifications | In-app and desktop alerts when Claude Code needs attention, showing current git branch and agent status |
| Rich input editor | Press `Ctrl-G` to open an expanded input editor for longer prompts |
| Code review | Send inline review comments directly to the agent from Warp's code review panel |
| Attach code as context | Select code and send it to the agent as context |
| Vertical tabs with agent metadata | Monitor Claude Code sessions with status indicators in Warp's tab bar |
| Tab Configs | Save and restore Claude Code session configurations |
| Remote Control | Share your Claude Code session with teammates via session sharing |

## Related

- [[133-guides-external-tools-and-integrations-how-to-set-up-claude-code|How to set up Claude Code]] — Installation, authentication, and productivity tips
- [[068-agent-platform-third-party-agents-remote-control|Remote Control]] — Share Claude Code sessions with teammates
