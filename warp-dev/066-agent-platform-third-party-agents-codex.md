---
title: Codex | Agents | Warp
url: https://docs.warp.dev/agent-platform/third-party-agents/codex
source: sitemap
fetched_at: 2026-04-29T15:04:14.213715011-03:00
rendered_js: false
word_count: 223
summary: This document provides an overview of the Codex CLI integration within the Warp terminal, detailing its supported features and configuration requirements for native notifications.
tags:
    - codex-cli
    - warp-terminal
    - agent-integration
    - developer-tools
    - terminal-notifications
    - command-line-interface
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Codex is OpenAI's open-source coding agent that runs in your terminal — it writes/edits code, executes commands, and navigates your codebase through natural language. For full documentation, see the [Codex GitHub repository](https://github.com/openai/codex).

Warp auto-detects Codex and provides rich input controls, code review, and other integrated features. For a product overview, see [Codex in Warp](https://warp.dev/agents/codex). For setup instructions, see [How to set up Codex CLI](https://docs.warp.dev/guides/integrations/how-to-set-up-codex-cli).

## Setting up notifications

Codex supports native notifications surfaced as in-app and desktop alerts — task completion, errors, or input requests.

1. Update Codex to the latest version (see [upgrade instructions](https://developers.openai.com/codex/cli#upgrade)).
2. Add to `~/.codex/config.toml`:

```toml
[notifications]
enabled = true
```

3. Restart Codex. If the config isn't set, Warp displays a setup chip in the terminal with instructions.

## Supported Warp features

| Feature | Description |
|---------|-------------|
| Agent notifications | In-app and desktop alerts when Codex needs attention (one-time config required) |
| Rich input editor | Press `Ctrl-G` for an expanded input editor |
| Code review | Send inline review comments from Warp's code review panel |
| Attach code as context | Select code and send it to the agent |
| Vertical tabs with metadata | Monitor Codex sessions in Warp's tab bar |
| Tab Configs | Save and restore session configurations |
| Remote Control | Share Codex sessions with teammates |

#codex-cli #agent-integration #developer-tools #terminal-notifications
