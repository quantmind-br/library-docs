---
title: layout_center | Pyprland web
url: https://hyprland-community.github.io/pyprland/layout/center
source: github_pages
fetched_at: 2026-01-31T15:58:59.094038554-03:00
rendered_js: true
word_count: 157
summary: This document provides configuration options and commands for managing a centered window layout, including margin, offset, and window behavior settings.
tags:
    - window-management
    - layout-config
    - centered-window
    - margin
    - offset
    - focus-behavior
category: configuration
---

- `layout_centertoggle|next|prev|next2|prev2`turn on/off or change the active window.

## Configuration [​](#configuration)

Basic (3)

OptionDescription[`margin`i](#config-margin "More details below")int

=`60`

Margin around the centered window in pixels[`offset`i](#config-offset "More details below")str or list or tuple

=`[0,0]`

Offset of the centered window as 'X Y' or \[X, Y][`style`i](#config-style "More details below")listWindow rules to apply to the centered window

Behavior (2)

OptionDescription`captive_focus`bool

=`false`

Keep focus on the centered window[`on_new_client`i](#config-on-new-client "More details below")str

=`"focus"`

Behavior when a new window opens

Commands (4)

OptionDescription[`next`i](#config-next "More details below")strCommand to run when 'next' is called and layout is disabled[`prev`i](#config-next "More details below")strCommand to run when 'prev' is called and layout is disabled[`next2`i](#config-next2 "More details below")strAlternative command for 'next'[`prev2`i](#config-next2 "More details below")strAlternative command for 'prev'

### `style` list [​](#config-style)

### `on_new_client` str=`"focus"` [​](#config-on-new-client)

Behavior when a new window opens while layout is active:

- `"focus"` (or `"foreground"`) - make the new window the main window
- `"background"` - make the new window appear in the background
- `"close"` - stop the centered layout when a new window opens

### `next` / `prev` str [​](#config-next)

### `next2` / `prev2` str [​](#config-next2)

### `offset` str or list or tuple=`[0,0]` [​](#config-offset)

### `margin` int=`60` [​](#config-margin)