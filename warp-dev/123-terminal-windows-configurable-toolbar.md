---
title: Configurable toolbar | Warp
url: https://docs.warp.dev/terminal/windows/configurable-toolbar
source: sitemap
fetched_at: 2026-04-29T15:02:40.562256926-03:00
rendered_js: false
word_count: 411
summary: This document explains how to customize the layout of the Warp terminal header by rearranging, hiding, or moving toolbar buttons to adjust the positioning of associated panels.
tags:
    - warp-terminal
    - ui-customization
    - toolbar-settings
    - workspace-layout
    - productivity-tools
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Rearrange, move, or hide header toolbar buttons to control which side of the window their panels open on. The toolbar works with both [[127-terminal-windows-tabs|tabs]] and [[128-terminal-windows-vertical-tabs|vertical tabs]].

## Key features

- **Reorder within a side** — drag toolbar chips to change left-to-right order.
- **Move across sides** — drag a chip to the other drop zone; the panel opens on that side.
- **Hide items** — remove a chip from both sides to hide the button; chips reappear when dropped back.
- **Side placement drives panel side** — moving a button flips its panel, resize handles, borders, and popups to match.
- **Persistent** — layout survives app restarts.

## Configurable items

| Button | Panel |
|---|---|
| Tools panel | Project explorer, global search, [[warp-drive|Warp Drive]], conversation history |
| Tabs panel | Visible when vertical tabs enabled |
| Agent management | Visible when Agent Mode enabled |
| Code review | Opens on the same side as its button |
| Notifications mailbox | Opens on the same side as its button |

The search bar and profile avatar are fixed.

> [!info]
> A button only appears when its prerequisite is met. If a prerequisite becomes unavailable, the button hides but your layout is preserved.

### Default layout

- **Left** — Tabs panel, tools panel, agent management
- **Right** — Code review, notifications mailbox

## Opening the editor

### From the header

Right-click any toolbar button (or empty space between buttons and the search bar) and select **Rearrange toolbar items**.

### From Settings

1. Navigate to **Settings** > **Appearance** > **Tabs**.
2. Click **Edit toolbar**.

## How side placement affects panels

| Button | Panel behavior |
|---|---|
| Tabs panel | Sidebar on the button's side; hover detail, action buttons, and right-click menu flip toward center |
| Tools panel | Opens on the button's side; Warp Drive previews, menus, and dialogs flip toward center; resize handle and border switch to the edge |
| Code review | Opens on the button's side with matching resize handle |
| Agent management | Replaces main content; button side only affects position |
| Notifications mailbox | Popover anchors under button; toasts appear on same side |

When multiple panels are open on the same side, they render in the toolbar button order.

## Related pages

- [[128-terminal-windows-vertical-tabs|Vertical tabs]] — sidebar toggled by the tabs panel button
- [[warp-drive|Warp Drive]] — one of the tools panel views

#toolbar-settings
