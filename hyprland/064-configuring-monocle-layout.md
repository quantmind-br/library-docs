---
title: Monocle Layout
url: https://wiki.hypr.land/Configuring/Monocle-Layout/
source: sitemap
fetched_at: 2026-04-26T09:49:12.530931002-03:00
rendered_js: false
word_count: 59
summary: This document explains the functionality and configuration quirks of the Monocle window layout in Hyprland.
tags:
    - hyprland
    - window-manager
    - layout-configuration
    - monocle-layout
    - desktop-environment
category: reference
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Monocle layout fills the entire available space with the active window.

> [!warning]
> `cyclenext` does not work with Monocle. Use `layoutmsg cyclenext` or `cyclenext, tiled` to cycle monocle windows.

## Layout messages[](#layout-messages)

| Dispatcher | Description | Params |
|---|---|---|
| `cyclenext` | Cycle to next window | none |
| `cycleprev` | Cycle to previous window | none |

See also: [[065-configuring-scrolling-layout|Scrolling Layout]], [[045-configuring-permissions|Permissions]]