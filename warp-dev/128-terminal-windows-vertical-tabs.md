---
title: Vertical Tabs | Warp
url: https://docs.warp.dev/terminal/windows/vertical-tabs
source: sitemap
fetched_at: 2026-04-29T15:02:35.998364313-03:00
rendered_js: false
word_count: 764
summary: This document explains the functionality and configuration of the vertical tabs panel in the Warp terminal, focusing on enhanced workspace management, agent status tracking, and metadata visualization.
tags:
    - warp-terminal
    - ui-customization
    - workflow-management
    - tab-management
    - productivity-tools
    - developer-experience
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
The vertical tabs panel replaces the horizontal tab bar with a sidebar showing every tab and pane with contextual metadata — Git branch, working directory, agent conversation status, diff stats, and PR badges.

## Enabling vertical tabs

1. Navigate to **Settings** > **Appearance** > **Tabs**.
2. Toggle **Use vertical tab layout** on.

The vertical tabs panel appears as a resizable sidebar on the left. The horizontal tab bar is hidden.

Toggle via [[command-palette|Command Palette]] → "vertical tab layout."

## Key features

### Rich metadata and status

- **Pane metadata** — working directory, Git branch, agent conversation status, diff stats, PR badges.
- **Agent status badges** — colored badge on pane icons (in progress, done, errored, cancelled, blocked). Third-party CLI agents (Claude Code, Codex, Gemini CLI) display their brand icon and color alongside badges.
- **Notification indicators** — accent-colored dot on pane rows with unread agent activity.

### Display modes

- **View** — **Panes** (every split pane as its own row) or **Tabs** (focused pane per tab only).
- **Density** — **Compact** (default, single-line) or **Expanded** (multi-line with full metadata).
- **Pane titles** — configurable to show last command/conversation, working directory, or Git branch first.
- **Hover detail sidecar** — floating card with full un-clipped metadata on hover.

### Tab management

- Search, drag-and-drop, inline renaming.
- **New tab menu** — agent tabs, terminal tabs, Oz cloud agent sessions, worktree configs, and [[126-terminal-windows-tab-configs|Tab Configs]].

## View modes

### Compact mode

Default. Each pane row shows icon + title on one line with optional configurable subtitle (**Additional metadata** in settings popup).

### Expanded mode

Each pane row shows title, description (directory or file path), and metadata (Git branch, diff stats badge, PR badge when available).

### Switching view modes

Click the settings icon (sliders) in the control bar → **Density** segmented control.

## Customizing vertical tabs

Configure from the settings popup (sliders icon in control bar) or **Settings** > **Appearance** > **Tabs**.

### Automatic metadata

These appear automatically without configuration:

| Metadata | Description |
|---|---|
| Git branch | Currently checked-out branch for the pane's working directory |
| Worktree | Active [[git-worktrees|Git worktree]] path if applicable |
| Agent status | Colored badge on pane icon |
| Notification dot | Accent dot when pane has unread agent activity |

## Agent status badges

Small circular badge on pane icon bottom-right:

| Status | Badge color |
|---|---|
| In progress | — |
| Done | — |
| Errored | — |
| Cancelled | — |
| Blocked | — |

Third-party CLI agents (Claude Code, Codex, Gemini CLI, others) display their brand icon and color inside the pane icon with the same status overlay. Notification dots clear when you focus the pane.

## Managing tabs

### Search

Filter by title, working directory, Git branch, PR label, or diff stats. Only matching tabs remain visible.

### New tab menu

| Option | Description |
|---|---|
| Agent | Open new agent tab |
| Terminal | Open new terminal tab |
| Oz cloud agent | Open Oz cloud agent session |
| Tab Configs | Any created [[126-terminal-windows-tab-configs|Tab Configs]] |
| New worktree config | Create worktree-based Tab Config |
| New tab config | Create from starter template |

### Drag and drop

Drag tab group headers to reorder. Drag a pane header over a different tab group to move it — Warp switches to that tab. Dropping between groups creates a new tab at that position.

### Tab renaming

Double-click a tab row to rename inline. `Enter` confirms, `Esc` cancels.

> [!info]
> Tabs only. Individual panes cannot be renamed.

## Hover detail sidecar

Hover a pane row to open a floating card anchored to the right side of the panel. Shows full un-clipped metadata. Move cursor from row into card to keep it open. Move away from both to dismiss. Disable via **Show details on hover** toggle.

## Keyboard shortcuts

All existing tab shortcuts work. The sidebar only changes display, not interaction. See [[127-terminal-windows-tabs|Terminal tabs]] for the full list.

## Toolbar integration

The vertical tabs panel toggle button is part of the configurable toolbar. See [[123-terminal-windows-configurable-toolbar|Configurable toolbar]] to rearrange it.

## Related pages

- [[127-terminal-windows-tabs|Terminal tabs]] — horizontal tab bar and shortcuts
- [[125-terminal-windows-split-panes|Split panes]] — divide a tab into multiple panes
- [[126-terminal-windows-tab-configs|Tab Configs]] — reusable tab setups in TOML
- [[git-worktrees|Git Worktrees]] — worktree support in vertical tab metadata
- [[tabs-behavior|Tabs behavior]] — tab bar visibility and indicators
- [[cli-agents-overview|Third-party CLI agents]] — Claude Code, Codex, Gemini CLI with brand icons and status badges

#vertical-tabs
