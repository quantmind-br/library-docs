---
title: Scrolling Layout
url: https://wiki.hypr.land/Configuring/Scrolling-Layout/
source: sitemap
fetched_at: 2026-04-26T09:49:08.830642503-03:00
rendered_js: false
word_count: 319
summary: This document provides the configuration options, layout messages, and rules for the scrolling layout, which arranges windows along an infinitely expanding linear tape.
tags:
    - hyprland
    - scrolling-layout
    - window-management
    - configuration-settings
    - layout-messages
category: reference
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Scrolling is a layout where windows are positioned on an infinitely growing tape.

## Config

category name: `scrolling`

| name | description | type | default |
|------|-------------|------|---------|
| `fullscreen_on_one_column` | a single column on a workspace will always span the entire screen | bool | `true` |
| `column_width` | default width of a column [0.1 - 1.0] | float | `0.5` |
| `focus_fit_method` | method to bring focused column into view. 0 = center, 1 = fit | int | `1` |
| `follow_focus` | layout moves to bring focused window into view automatically | bool | `true` |
| `follow_min_visible` | when focused, require at least given fraction of window visible for focus to follow [0.0 - 1.0]. Hard input (binds, clicks) always follows. | float | `0.4` |
| `explicit_column_widths` | comma-separated list of preconfigured widths for colresize +conf/-conf | str | `0.333, 0.5, 0.667, 1.0` |
| `wrap_focus` | causes `layoutmsg focus l/r` to wrap around at beginning and end | bool | `true` |
| `wrap_swapcol` | causes `layoutmsg swapcol l/r` to wrap around at beginning and end | bool | `true` |
| `direction` | direction new windows appear and layout scrolls | `left` \| `right` \| `down` \| `up` | `right` |

## Workspace rules

| name | description | type |
|------|-------------|------|
| `direction` | same as scrolling:direction | str |

```ini
workspace = 2, layoutopt:direction:right
```

## Layout messages

Dispatcher `layoutmsg` params:

| name | description | params |
|------|-------------|--------|
| `move` | move layout horizontally by relative logical px (`-200`, `+200`) or columns (`+col`, `-col`) | move data |
| `colresize` | resize current column to value or relative value (`0.5`, `+0.2`, `-0.2`) or cycle preconfigured with `+conf`/`-conf`. Can also be `all (number)` for all columns. | relative float / relative conf |
| `fit` | executes a fit operation based on argument. Available: `active`, `visible`, `all`, `toend`, `tobeg` | fit mode |
| `focus` | moves focus and centers layout, wrapping instead of moving to neighboring monitors | direction |
| `promote` | moves a window to its own new column | none |
| `swapcol` | swaps current column with neighbor (`l` = left, `r` = right). Wraps around (swap first column left moves it to end). | `l` or `r` |

Example key bindings:

```ini
bind = $mainMod, period, layoutmsg, move +col
bind = $mainMod, comma, layoutmsg, swapcol l
```

## Window rules

With the static rule `scrolling_width`, set a starting column width for a window:

```
windowrule {
  name = kitty_starting_width
  match:class = kitty
  scrolling_width = 0.5
}
```

Last updated on April 20, 2026

[[063-configuring-master-layout|Master Layout]] [[064-configuring-monocle-layout|Monocle Layout]]