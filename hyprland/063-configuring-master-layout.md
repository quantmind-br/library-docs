---
title: Master Layout
url: https://wiki.hypr.land/Configuring/Master-Layout/
source: sitemap
fetched_at: 2026-04-26T09:49:06.615488218-03:00
rendered_js: false
word_count: 802
summary: This document provides a technical reference for the master tiling layout, detailing its configuration options, workspace rules, and dispatcher commands for managing window positioning and focus.
tags:
    - window-manager
    - tiling-layout
    - hyprland
    - desktop-customization
    - configuration-reference
    - layout-management
category: reference
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

The master layout places one or more windows as "master" on the left (by default), tiling the rest on the right. Orientation can be changed per-workspace.

![master1](https://user-images.githubusercontent.com/43317083/179357849-321f042c-f536-44b3-9e6f-371df5321836.gif)

## Config

*category name: `master`*

| Param | Type | Default | Description |
|---|---|---|---|
| allow_small_split | bool | false | Enable additional master windows in horizontal split style |
| special_scale_factor | float | 1 | Scale of special workspace windows. [0.0 - 1.0] |
| mfact | float | 0.55 | Master window size as percentage. `mfact = 0.70` = 70% master, 30% slave. [0.0 - 1.0] |
| new_status | string | `slave` | `master`: new window becomes master. `slave`: added to slave stack. `inherit`: inherit from focused window |
| new_on_top | bool | false | Place newly opened window at top of stack |
| new_on_active | string | `none` | `before`/`after`: place relative to focused window. `none`: use `new_on_top` value |
| orientation | string | `left` | Master area placement: `left`, `right`, `top`, `bottom`, `center` |
| slave_count_for_center_master | int | 2 | Master centered when at least this many slave windows open (0 = always center) |
| center_master_fallback | string | `left` | Fallback for center master when slaves < `slave_count_for_center_master` |
| smart_resizing | bool | true | Resizing direction based on mouse position (nearest corner) |
| drop_at_cursor | bool | true | Drag-drop puts window at cursor position |
| always_keep_position | bool | false | Keep master in configured position when no slave windows |

## Dispatchers

`layoutmsg` commands:

| Command | Description | Params |
|---|---|---|
| swapwithmaster | Swap current window with master | `master`/`child`/`auto` + optional `ignoremaster` |
| focusmaster | Focus master window | `master`/`auto`/`previous` |
| cyclenext | Focus next window respecting layout | `loop`/`noloop` |
| cycleprev | Focus previous window respecting layout | `loop`/`noloop` |
| swapnext | Swap with next window | `loop`/`noloop` |
| swapprev | Swap with previous window | `loop`/`noloop` |
| addmaster | Add master to master side | none |
| removemaster | Remove master from master side | none |
| orientationleft | Set orientation to left | none |
| orientationright | Set orientation to right | none |
| orientationtop | Set orientation to top | none |
| orientationbottom | Set orientation to bottom | none |
| orientationcenter | Set orientation to center | none |
| orientationnext | Cycle to next orientation (clockwise) | none |
| orientationprev | Cycle to previous orientation (counter-clockwise) | none |
| orientationcycle | Cycle to orientation from list | `left`/`top`/`right`/`bottom`/`center` space-separated |
| mfact | Change master split ratio | delta (e.g. `-0.2`, `+0.2`) or `exact` + float [0.0-1.0] |
| rollnext | Rotate next window to master, keep focus on master | none |
| rollprev | Rotate previous window to master, keep focus on master | none |

Parameters separated by single space.

> [!example]
> ```ini
> bind = MOD, KEY, layoutmsg, cyclenext
> bind = MOD, KEY, layoutmsg, swapwithmaster master
> ```

## Workspace Rules

`layoutopt` rules:

| Rule | Description | Type |
|---|---|---|
| orientation:\[o] | Set workspace orientation | string |

```ini
workspace = 2, layoutopt:orientation:top
```

See also: [[062-configuring-dwindle-layout|Dwindle Layout]], [[065-configuring-scrolling-layout|Scrolling Layout]]

#tiling-layout #layout-management #configuration-reference
