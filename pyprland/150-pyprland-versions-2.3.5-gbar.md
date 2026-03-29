---
title: gbar | Pyprland web
url: https://hyprland-community.github.io/pyprland/versions/2.3.5/gbar
source: github_pages
fetched_at: 2026-01-31T16:01:02.95188146-03:00
rendered_js: false
word_count: 66
summary: Provides instructions for configuring and running gBar on the preferred monitor with automatic startup management.
tags:
    - gbar
    - monitor
    - startup
    - configuration
    - hyprland
category: guide
---

Runs [gBar](https://github.com/scorpion-26/gBar) on the "best" monitor from a list of monitors.

Will take care of starting gbar on startup (you must not run it from another source like `hyprland.conf`).

> *Added in 2.2.6*

## Commands [​](#commands)

- `gbar restart` - Restart/refresh gBar on the "best" monitor.

## Configuration [​](#configuration)

### `monitors` [​](#monitors)

List of monitors to chose from, the first have higher priority over the second one etc...

## Example [​](#example)

sh

```
[gbar]
monitors = ["DP-1", "HDMI-1", "HDMI-1-A"]
```