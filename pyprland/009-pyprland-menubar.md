---
title: menubar | Pyprland web
url: https://hyprland-community.github.io/pyprland/menubar
source: github_pages
fetched_at: 2026-01-31T16:02:09.720923049-03:00
rendered_js: false
word_count: 111
summary: Provides instructions for configuring a menubar plugin that automatically manages bar applications across different display environments.
tags:
    - menubar
    - hyprland
    - niri
    - display-management
    - automation
category: configuration
---

Runs your favorite bar app (gbar, ags / hyprpanel, waybar, ...) with option to pass the "best" monitor from a list of monitors.

- Will take care of starting the command on startup (you must not run it from another source like `hyprland.conf`).
- Automatically restarts the menu bar on crash
- Checks which monitors are on and take the best one from a provided list

Example

toml

```
[menubar]
command = "gBar bar [monitor]"
monitors = ["DP-1", "HDMI-1", "HDMI-1-A"]
```

TIP

This plugin supports both Hyprland and Niri. It will automatically detect the environment and use the appropriate IPC commands.

## Commands [​](#commands)

Loading commands...

## Configuration [​](#configuration)

Loading configuration...

### `command` [​](#config-command)

The command to run the bar. Use `[monitor]` as a placeholder for the monitor name:

toml

```
command = "waybar -o [monitor]"
```