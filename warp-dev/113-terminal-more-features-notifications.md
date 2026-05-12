---
title: Desktop notifications | Warp
url: https://docs.warp.dev/terminal/more-features/notifications
source: sitemap
fetched_at: 2026-04-29T15:03:07.941505877-03:00
rendered_js: false
word_count: 264
summary: This document explains how to configure and manage desktop notifications in the Warp terminal, including how to trigger custom notifications using OSC escape sequences.
tags:
    - terminal-notifications
    - warp-terminal
    - osc-escape-sequences
    - desktop-alerts
    - configuration-guide
    - troubleshooting
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
## Overview

Notifications trigger after configurable seconds when a command completes, or when a running command needs a password. Warp sends notifications only if you're using a different app.

> [!info]
> For coding agent notifications (Warp Agent, Claude Code, OpenCode), see [[105-terminal-ai-features|Agent Notifications]].

## Custom Notification Hooks (OSC 9 / OSC 777)

Scripts and tools raise desktop notifications via terminal escape sequences.

| Code | Format | Example |
|------|--------|---------|
| OSC 9 | `ESC ] 9 ; <body> BEL` | `printf '\033]9;Build complete\007'` |
| OSC 777 | `ESC ] 777 ; notify ; <title> ; <body> BEL` | `printf '\033]777;notify;Deploy;Success on prod\007'` |

> [!info]
> - Works on macOS, Windows, Linux (with notification permissions).
> - Avoid or escape newlines and semicolons in payloads.
> - Enabled by default in current Warp releases.

## Enabling Notifications

- Enabled by default; requires system permissions.
- Re-enable via **Settings** → **Features** → **Session** or the [[104-terminal-command-palette|Command Palette]].
- Customize triggers at **Settings** → **Features** → **Notifications**.

> [!info]
> On macOS, **Allow** the notification request. If denied, see troubleshooting below.

## Troubleshooting

Two settings must both be enabled: macOS **System Settings** → **Notifications & Focus** AND Warp **Settings** → **Features** → **Session**.

If notifications still don't appear:

- Ensure you're navigated away from Warp.
- Disable **Do Not Disturb** in System Settings.
- Set notification style to Banner or Alert, then quit and restart Warp.
- Reset prompt: `defaults delete dev.warp.Warp-Stable Notifications`, restart Warp, toggle on notifications.
- Restart macOS to apply changes.

Contact [[105-terminal-ai-features|Sending Feedback]] for additional issues.

#terminal-notifications #warp-terminal #osc-escape-sequences
