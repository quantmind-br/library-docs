---
title: gbar | Pyprland web
url: https://hyprland-community.github.io/pyprland/versions/2.4.0/gbar
source: github_pages
fetched_at: 2026-01-31T16:02:37.722083213-03:00
rendered_js: false
word_count: 82
summary: Provides instructions for configuring and running gBar on the optimal monitor from a list of available displays, including automatic startup and crash recovery features.
tags:
    - gbarr
    - monitor-selection
    - automatic-restart
    - configuration
    - hyprland
category: guide
---

Runs [gBar](https://github.com/scorpion-26/gBar) on the "best" monitor from a list of monitors.

- Will take care of starting gbar on startup (you must not run it from another source like `hyprland.conf`).
- Automatically restarts gbar on crash
- Checks which monitors are on and take the best one from a provided list

## Command [​](#command)

- `gbar restart`  Restart/refresh gBar on the "best" monitor.

## Configuration [​](#configuration)

### `monitors` (REQUIRED) [​](#monitors-required)

List of monitors to chose from, the first have higher priority over the second one etc...

## Example [​](#example)

sh

```
[gbar]
monitors = ["DP-1", "HDMI-1", "HDMI-1-A"]
```