---
title: Launch Configurations (Legacy) | Warp
url: https://docs.warp.dev/terminal/windows/launch-configurations
source: sitemap
fetched_at: 2026-04-29T15:02:41.640593719-03:00
rendered_js: false
word_count: 291
summary: This document provides instructions on how to create and manage terminal window, tab, and pane layouts in the Warp terminal using Launch Configurations.
tags:
    - warp-terminal
    - launch-configurations
    - yaml-config
    - workflow-automation
    - terminal-setup
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
> [!warning]
> Launch Configurations have been replaced by [[126-terminal-windows-tab-configs|Tab Configs]]. Existing configs continue to work, but new features are not being added.

Launch Configurations save terminal window, tab, and pane layouts as YAML files stored in `$HOME/.warp/launch_configurations/`.

## Creating a Launch Configuration

### From the UI

1. Set up your desired windows, tabs, and panes.
2. Open the [[command-palette|Command Palette]] and type `Save New Launch Configuration`.
3. Name the configuration.
4. Click **Save configuration**.

### With a YAML file

Files can be created or modified manually in `$HOME/.warp/launch_configurations/`.

## Using a Launch Configuration

- [[command-palette|Command Palette]] → `Launch Configuration`
- Right-click the **+** button → select a saved Launch Configuration
- macOS menu bar → **File** > **Launch Configurations**

`CMD-ENTER` (macOS) launches single-window configs into the active window.

## YAML Format

> [!warning]
> `cwd:` must be an absolute path or `""`. `~` or empty paths will not appear in the list.

### Windows

```yaml
windows:
  - layout:
      type: ...
```

### Tabs

| Field | Description |
|---|---|
| `title` | Custom tab name |
| `color` | Tab color (ANSI): `Red`, `Green`, `Yellow`, `Blue`, `Magenta`, `Cyan`. Values derive from your Warp theme. |

### Panes

Split panes are supported; nesting is also allowed in launch configuration files.

### Active and Focus

| Field | Description |
|---|---|
| `active_window_index` | Which window is active |
| `active_tab_index` | Which tab is active |
| `is_focused` | Which pane has focus per tab |

> [!warning]
> When using `- active_tab_index:`, the `tabs:` field does not need the `-` prefix to avoid syntax issues.

### Commands

Use `commands` to run commands on launch. Commands on separate lines are chained with `&&`.

> [!warning]
> Double-quote commands with special characters. Commands after `ssh` may not execute.

#launch-configurations
