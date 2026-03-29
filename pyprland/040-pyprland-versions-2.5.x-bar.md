---
title: menubar | Pyprland web
url: https://hyprland-community.github.io/pyprland/versions/2.5.x/bar
source: github_pages
fetched_at: 2026-01-31T15:57:42.305824306-03:00
rendered_js: false
word_count: 117
summary: Provides instructions for configuring and running a menu bar application across multiple monitors with automatic selection and restart functionality.
tags:
    - menu-bar
    - monitor-selection
    - automatic-restart
    - configuration
    - bar-application
category: guide
---

Runs your favorite bar app (gbar, ags / hyprpanel, waybar, ...) with option to pass the "best" monitor from a list of monitors.

- Will take care of starting the command on startup (you must not run it from another source like `hyprland.conf`).
- Automatically restarts the menu bar on crash
- Checks which monitors are on and take the best one from a provided list

## Command [​](#command)

- `bar restart`  Restart/refresh Menu Bar on the "best" monitor.

## Configuration [​](#configuration)

### `command` (REQUIRED) [​](#command-required)

The command which runs the menu bar. The string `[monitor]` will be replaced by the best monitor.

### `monitors` [​](#monitors)

List of monitors to chose from, the first have higher priority over the second one etc...

## Example [​](#example)

sh

```
[gbar]
monitors = ["DP-1", "HDMI-1", "HDMI-1-A"]
```