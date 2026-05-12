---
title: OpenCode | Agents | Warp
url: https://docs.warp.dev/agent-platform/third-party-agents/opencode
source: sitemap
fetched_at: 2026-04-29T15:04:15.690054066-03:00
rendered_js: false
word_count: 213
summary: This document outlines the integration features between the OpenCode terminal agent and the Warp terminal, including how to configure notifications and utilize enhanced development tools.
tags:
    - opencode
    - warp-terminal
    - agent-integration
    - developer-tools
    - terminal-productivity
    - workflow-automation
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
OpenCode is an open-source terminal-based coding agent that connects to multiple LLM providers and supports tool use, file editing, and command execution. For full documentation, see the [OpenCode docs](https://opencode.ai/docs).

Warp auto-detects OpenCode and provides rich input controls, code review, agent notifications, and other integrated features. For a product overview, see [OpenCode in Warp](https://warp.dev/agents/opencode). For setup instructions, see [How to set up OpenCode](https://docs.warp.dev/guides/integrations/how-to-set-up-opencode).

## Setting up notifications

OpenCode uses the `@warp-dot-dev/opencode-warp` plugin. Add it to the `plugin` array in `opencode.json`:

```json
{
  "plugin": ["@warp-dot-dev/opencode-warp"]
}
```

If the plugin isn't installed, Warp displays an installation chip in the terminal with setup steps. For source and updates, see the [opencode-warp GitHub repository](https://github.com/warpdotdev/opencode-warp).

## Supported Warp features

| Feature | Description |
|---------|-------------|
| Agent notifications | In-app and desktop alerts when OpenCode needs attention. Displays current git branch alongside status |
| Rich input editor | Press `Ctrl-G` for an expanded input editor |
| Code review | Send inline review comments from Warp's code review panel |
| Attach code as context | Select code and send it to the agent |
| Vertical tabs with metadata | Monitor OpenCode sessions in Warp's tab bar |
| Tab Configs | Save and restore session configurations |
| Remote Control | Share OpenCode sessions with teammates |

#opencode #agent-integration #developer-tools #terminal-productivity
