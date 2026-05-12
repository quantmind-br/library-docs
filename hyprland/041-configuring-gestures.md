---
title: Gestures
url: https://wiki.hypr.land/Configuring/Gestures/
source: sitemap
fetched_at: 2026-04-26T09:48:40.523871716-03:00
rendered_js: false
word_count: 209
summary: This document outlines the configuration syntax and supported parameters for trackpad gestures in Hyprland, including available actions, directions, and modification flags.
tags:
    - hyprland
    - configuration
    - gestures
    - trackpad-support
    - input-mapping
    - window-management
category: configuration
optimized: true
optimized_at: 2026-04-26T10:00:00Z
---

# Gestures

Hyprland supports 1:1 trackpad gestures. Basic syntax:

```ini
gesture = fingers, direction, action, options
```

Drop the options arg entirely if the action takes none. Add `, mod: [MODMASK]` after `direction` to restrict gestures to a modifier. Add `scale: [SCALE]` (float) to adjust animation speed.

Examples:

```ini
gesture = 3, horizontal, workspace
gesture = 3, down, mod: ALT, close
gesture = 3, up, mod: SUPER, scale: 1.5, fullscreen
gesture = 3, left, scale: 1.5, float
```

## Directions

| Direction | Description |
|-----------|-------------|
| `swipe` | any swipe |
| `horizontal` | horizontal swipe |
| `vertical` | vertical swipe |
| `left`, `right`, `up`, `down` | swipe directions |
| `pinch` | any pinch |
| `pinchin`, `pinchout` | directional pinch |

## Actions

Use `unset` as the action to remove a previously set gesture — must exactly match the original including direction, mods, fingers, and scale.

| Action | Description | Arguments |
|--------|-------------|-----------|
| `dispatcher` | executes a dispatcher once the gesture ends | `dispatcher, params` |
| `workspace` | workspace swipe gesture, for switching workspaces | none |
| `move` | moves the active window | none |
| `resize` | resizes the active window | none |
| `special` | toggles a special workspace | special workspace without `special:`, e.g. `mySpecialWorkspace` |
| `close` | closes the active window | none |
| `fullscreen` | fullscreens the active window | none for fullscreen, `maximize` for maximize |
| `float` | floats the active window | none for toggle, `float` or `tile` for one-way |
| `cursorZoom` | zooms into the cursor | zoom factor, toggles by default, add `mult` for a multiplier instead |

## Flags

> [!note]
> Gestures support flags via the syntax: `gesture = ..., flag: [FLAG]`

| Flag | Name | Description |
|------|------|-------------|
| `p` | bypass | Allows the gesture to bypass shortcut inhibitors. |

#gestures #trackpad-support #input-mapping