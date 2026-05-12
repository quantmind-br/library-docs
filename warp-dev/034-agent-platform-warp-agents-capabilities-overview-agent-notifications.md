---
title: Agent notifications | Agents | Warp
url: https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/agent-notifications
source: sitemap
fetched_at: 2026-04-29T15:03:51.87204962-03:00
rendered_js: false
word_count: 419
summary: This document explains how Warp handles notifications for coding agents, detailing the types of alerts, in-app management tools, system-level integration, and configuration requirements for supported agents.
tags:
    - warp-terminal
    - agent-notifications
    - coding-agents
    - developer-productivity
    - workflow-automation
    - ui-notifications
category: guide
optimized: true
optimized_at: 2026-04-29T18:00:00Z
---
Warp delivers notifications from supported coding agents so you know when an agent finishes, encounters an error, or needs input. Notifications work whether you're in a different tab or app.

## Notification types

| Type | Description |
|------|-------------|
| **Complete** | Agent finished its task. Review output and continue. |
| **Request** | Agent is blocked and needs input (command approval, permissions, idle prompts). |
| **Error** | Agent encountered an error requiring attention. |

## In-app notifications

### Toast notifications

Floating toasts appear in the corner of Warp when an agent in another tab needs attention. Toasts auto-dismiss after a few seconds; hover to pause the timer, click to jump to the agent's session. Up to two toasts visible at a time; additional notifications replace the oldest.

### Notification mailbox

Sidebar panel collecting all agent notifications. Open via the bell icon in the top-right corner.

**Features:**
- **Filter tabs** — All tabs, Unread, Errors
- **Mark all as read** — clear unread indicators
- **Click to navigate** — jump to agent's session

**Keyboard shortcuts:**

| Shortcut | Action |
|----------|--------|
| `↑` / `↓` | Select previous/next notification |
| `Enter` | Open notification's session |
| `Shift-Tab` | Cycle filter tabs |
| `Esc` | Close mailbox |

### Tab status indicators

Tabs display icons reflecting agent state: working, blocked, completed, errored. Unread notifications show an attention badge. Notifications auto-mark as read when you navigate to the tab.

## Desktop notifications

Native system alerts when Warp is in background or minimized.

> [!info]
> Desktop notifications require system permissions. If not receiving them, check OS notification settings for Warp. See [Desktop Notifications](https://docs.warp.dev/terminal/more-features/notifications) for troubleshooting.

## Supported agents

| Agent | Support Level |
|-------|---------------|
| Oz agent | Supported out of the box |
| Claude Code | Full support via notification plugin |
| Codex | Full support via native configuration |
| OpenCode | Full support via notification plugin |

## Setting up notifications

### Oz agent

No setup required.

### Claude Code

One-click auto-install via chip in Warp, or manual setup. See [Claude Code setup](https://docs.warp.dev/agent-platform/third-party-agents/claude-code#setting-up-notifications).

### Codex

Add to `~/.codex/config.toml`:
```toml
[tui]
notification_condition = "always"
```
Then restart Codex. See [Codex setup](https://docs.warp.dev/agent-platform/third-party-agents/codex#setting-up-notifications).

### OpenCode

Add to OpenCode config:
```json
"plugin": ["@warp-dot-dev/opencode-warp"]
```
See [OpenCode setup](https://docs.warp.dev/agent-platform/third-party-agents/opencode#setting-up-notifications).

If auto-install fails or you're running over SSH, Warp displays an installation chip with setup steps.

## Related pages

- [Managing Agents](https://docs.warp.dev/agent-platform/cloud-agents/managing-cloud-agents) — monitor all agent conversations
- [Claude Code](https://docs.warp.dev/agent-platform/third-party-agents/claude-code) — setup and plugin installation
- [Codex](https://docs.warp.dev/agent-platform/third-party-agents/codex) — setup and configuration
- [OpenCode](https://docs.warp.dev/agent-platform/third-party-agents/opencode) — setup and plugin installation