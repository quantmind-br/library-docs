---
title: Overview | Agents | Warp
url: https://docs.warp.dev/agent-platform/third-party-agents/overview
source: sitemap
fetched_at: 2026-04-29T15:04:13.098315538-03:00
rendered_js: false
word_count: 368
summary: This document describes Warp's universal agent support, which enhances third-party CLI coding agents with IDE-like features and a customizable toolbelt interface.
tags:
    - warp-terminal
    - cli-agent
    - coding-assistant
    - terminal-enhancement
    - developer-tools
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Warp auto-detects supported CLI agents and enhances them with IDE-level features — a rich input editor, agent notifications, inline code review, remote session control, and more. This feature set is known as **universal agent support**.

## Supported agents

- [**OpenCode**](066-agent-platform-third-party-agents-opencode) — Open-source CLI coding agent
- [**Codex**](066-agent-platform-third-party-agents-codex) — OpenAI's CLI coding agent
- **Amp** — Sourcegraph's CLI coding agent
- **Auggie** — Augment Code's CLI coding agent
- **Copilot CLI** — GitHub's CLI coding agent
- **Cursor CLI** — Cursor's CLI coding agent
- **Gemini CLI** — Google's CLI coding agent
- **Droid** — Factory's CLI coding agent
- **Pi** — Open-source CLI coding agent

Running a supported agent inside Warp automatically displays the **agent toolbelt**.

## Feature support

> [!info]
> Agent notifications require one-time setup. Claude Code and OpenCode use a Warp notification plugin. Codex uses a native config change. See individual agent pages for instructions. Amp, Auggie, Copilot CLI, Cursor, Gemini CLI, Droid, and Pi don't support notifications yet.

| Feature | OpenCode | Codex | Amp, Auggie, Copilot CLI, Cursor, Gemini CLI, Droid, Pi |
|---------|----------|-------|---------------------------------------------------------|
| Agent notifications | ✅ | ✅ | ❌ |
| Rich input editor | ✅ | ✅ | ✅ |
| Code review | ✅ | ✅ | ✅ |
| Attach code as context | ✅ | ✅ | ✅ |
| Vertical tabs with metadata | ✅ | ✅ | ✅ |
| Tab Configs | ✅ | ✅ | ✅ |
| Remote Control | ✅ | ✅ | ✅ |

## Customizing the toolbelt

The toolbelt chips and buttons can be reordered, hidden, or moved between left and right sides. Layout persists across app restarts.

Open **Edit CLI agent toolbelt** via:
- Right-click the input area while a supported agent is running, then select **Edit CLI agent toolbelt**.
- **Settings** > **Agents** > **Third party CLI agents**, then click **Toolbar layout**.

## Getting started

Run a supported agent inside Warp. Warp detects the agent automatically and activates the toolbelt with all available features. For notifications, follow the one-time setup on the individual agent pages.

> [!tip]
> If you don't see the toolbelt, update Warp to the latest version.

#cli-agent #coding-assistant #terminal-enhancement #developer-tools
