---
title: hyprshutdown
url: https://wiki.hypr.land/Hypr-Ecosystem/hyprshutdown/
source: sitemap
fetched_at: 2026-01-22T22:16:07.724219769-03:00
rendered_js: false
word_count: 60
summary: This document introduces hyprshutdown, a graceful shutdown utility for Hyprland that allows applications to exit properly before quitting the window manager.
tags:
    - hyprland
    - hyprshutdown
    - window-manager
    - shutdown-utility
    - linux-tools
category: guide
---

[hyprshutdown](https://github.com/hyprwm/hyprshutdown) is a graceful shutdown utility. It opens a GUI and gracefully asks apps to exit, then quits Hyprland. It’s the recommended way to exit hyprland, as otherwise (e.g. `dispatch exit`) apps will die instead of exiting.

## Tips and tricks[](#tips-and-tricks)

If you want to shut the system down, or reboot, instead of logging out, you can do things like this:

```
hyprshutdown -t 'Shutting down...' --post-cmd 'shutdown -P 0'
hyprshutdown -t 'Restarting...' --post-cmd 'reboot'
```