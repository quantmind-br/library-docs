---
title: Synchronized inputs | Warp
url: https://docs.warp.dev/terminal/entry/synchronized-inputs
source: sitemap
fetched_at: 2026-04-29T15:02:28.47332185-03:00
rendered_js: false
word_count: 110
summary: This document explains how to use the synchronized inputs feature in the Warp terminal, describing its scope, usage modes, and functionality compared to standard broadcast input features.
tags:
    - warp-terminal
    - synchronized-inputs
    - terminal-productivity
    - multi-pane-management
    - workflow-automation
category: guide
optimized: true
optimized_at: 2026-04-29T19:02:00Z
---
Synchronized inputs sync entire commands across sessions, unlike broadcast input which sends individual keystrokes.

## How to access

- macOS menu: **Edit** → **Synchronize Input**

## Synchronization modes

| Mode | Shortcut |
|------|----------|
| Synchronize All Panes in All Tabs | — |
| Synchronize All Panes in Current Tab | `OPT-CMD-I` |
| Stop Synchronizing Any Panes | `OPT-CMD-I` (toggle) |

## Behavior

- Typing in one input editor syncs the entire command to all target panes
- If using alternative editor mode (e.g., vim), synchronization only applies to tabs with the same editor type
- Select "Stop Synchronizing Any Panes" to end synchronization

#synchronized-inputs #terminal-productivity #multi-pane-management #workflow-automation
