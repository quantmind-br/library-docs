---
title: Dwindle Layout
url: https://wiki.hypr.land/Configuring/Dwindle-Layout/
source: sitemap
fetched_at: 2026-04-26T09:48:54.591480868-03:00
rendered_js: false
word_count: 438
summary: This document provides configuration options, layout behavior, and dispatchers for the Dwindle tiling window management layout.
tags:
    - window-management
    - dwindle-layout
    - tiling-window-manager
    - config-reference
    - layout-dispatchers
category: reference
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Dwindle is a BSPWM-like layout where every window on a workspace is a member of a binary tree.

## Quirks

Dwindle splits are **NOT PERMANENT**. The split is determined dynamically by the parent node's W/H ratio — side-by-side if W > H, top-and-bottom if H > W. Enable `preserve_split` for permanent splits.

## Config

category name: `dwindle`

| name | description | type | default |
|------|-------------|------|---------|
| `pseudotile` | enable pseudotiling. Pseudotiled windows retain their floating size when tiled. | bool | `false` |
| `force_split` | 0 = split follows mouse, 1 = always split to the left (new = left or top), 2 = always split to the right (new = right or bottom) | int | `0` |
| `preserve_split` | if enabled, the split (side/top) will not change regardless of what happens to the container. | bool | `false` |
| `smart_split` | enables precise control over window split direction based on cursor position. The window is divided into four triangles; cursor's triangle determines split direction. Automatically enables `preserve_split`. | bool | `false` |
| `smart_resizing` | resizing direction is determined by mouse position on the window (nearest corner). Else, based on window's tiling position. | bool | `true` |
| `permanent_direction_override` | makes the preselect direction persist until mode is turned off, another direction is specified, or a non-direction is specified (anything other than l, r, u/t, d/b). | bool | `false` |
| `special_scale_factor` | scale factor of windows on the special workspace [0 - 1]. | float | `1` |
| `split_width_multiplier` | auto-split width multiplier. Useful on widescreen monitors where window W > H even after several splits. | float | `1.0` |
| `use_active_for_splits` | prefer the active window or the mouse position for splits. | bool | `true` |
| `default_split_ratio` | default split ratio on window open. 1 means even 50/50 split. [0.1 - 1.9] | float | `1.0` |
| `split_bias` | which window receives the split ratio. 0 = directional (top or left window), 1 = current window. | int | `0` |
| `precise_mouse_movebindm` | movewindow drops the window more precisely depending on mouse position. | bool | `false` |

## Bind Dispatchers

| dispatcher | description | params |
|------------|-------------|--------|
| `pseudo` | toggles the given window's pseudo mode. | empty for current, `active` for current, or `window` for specific window |

## Layout messages

Dispatcher `layoutmsg` params:

| param | description | args |
|-------|-------------|------|
| `splitratio` | changes the split ratio. | float value |
| `togglesplit` | toggles the split (top/side) of the current window. `preserve_split` must be enabled. | none |
| `swapsplit` | swaps the two halves of the split of the current window. | none |
| `preselect` | one-time override for split direction (valid for next window to be opened, only works on tiled windows). | direction |
| `movetoroot` | moves selected window to the root of its workspace tree. Default maximizes in current subtree; `unstable` as second arg swaps subtrees instead. Cannot provide only second arg — use `movetoroot active unstable`. | `[window, [ string ]]` |

Example:

```ini
bind = SUPER, A, layoutmsg, preselect l
```

Last updated on April 20, 2026

[[064-configuring-tearing|Tearing]] [[063-configuring-master-layout|Master Layout]]