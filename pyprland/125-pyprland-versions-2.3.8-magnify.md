---
title: magnify | Pyprland web
url: https://hyprland-community.github.io/pyprland/versions/2.3.8/magnify
source: github_pages
fetched_at: 2026-01-31T16:00:20.590647114-03:00
rendered_js: false
word_count: 236
summary: Provides instructions for using the pypr zoom command to adjust display zoom levels with optional animation effects in Hyprland.
tags:
    - zoom
    - hyprland
    - display
    - animation
    - configuration
category: reference
---

Zooms in and out with an optional animation.

Example

sh

```
pypr zoom  # sets zoom to `factor` (2 by default)
pypr zoom +1  # will set zoom to 3x
pypr zoom  # will set zoom to 1x
pypr zoom 1 # will (also) set zoom to 1x - effectively doing nothing
```

Sample `hyprland.conf`:

sh

```
bind = $mainMod , Z, exec, pypr zoom ++0.5
bind = $mainMod SHIFT, Z, exec, pypr zoom
```

## Command [​](#command)

- `zoom [value]`  Set the current zoom level (absolute or relative) - toggle zooming if no value is provided

### `[value]` [​](#value)

#### unset / not specified [​](#unset-not-specified)

Will zoom to [factor](#factor) if not zoomed, else will set the zoom to 1x.

#### floating or integer value [​](#floating-or-integer-value)

Will set the zoom to the provided value.

#### +value / -value [​](#value-value)

Update (increment or decrement) the current zoom level by the provided value.

#### ++value / --value [​](#value-value-1)

Update (increment or decrement) the current zoom level by a non-linear scale. It *looks* more linear changes than using a single + or -.

NOTE

The non-linear scale is calculated as powers of two, eg:

- `zoom ++1` → 2x, 4x, 8x, 16x...
- `zoom ++0.7` → 1.6x, 2.6x, 4.3x, 7.0x, 11.3x, 18.4x...
- `zoom ++0.5` → 1.4x, 2x, 2.8x, 4x, 5.7x, 8x, 11.3x, 16x...

## Configuration [​](#configuration)

### `factor` (optional) [​](#factor-optional)

default value is `2`

Scaling factor to be used when no value is provided.

### `duration` (optional) [​](#duration-optional)

Default value is `15`

Duration in tenths of a second for the zoom animation to last, set to `0` to disable animations.