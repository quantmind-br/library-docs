---
title: hyprsunset
url: https://wiki.hypr.land/Hypr-Ecosystem/hyprsunset/
source: sitemap
fetched_at: 2026-04-26T09:48:42.534411591-03:00
rendered_js: false
word_count: 393
summary: This document provides an overview and configuration guide for hyprsunset, a utility for Hyprland that enables blue light filtering and gamma adjustments.
tags:
    - hyprland
    - blue-light-filter
    - gamma-adjustment
    - system-utility
    - configuration
    - linux-desktop
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

[hyprsunset](https://github.com/hyprwm/hyprsunset) provides a blue light filter that will *not* be captured in recordings/screenshots (preferred over screen shaders). Also provides a gamma filter to adjust perceived brightness on monitors without software control, or lower than minimum.

> [!warning]
> `hyprsunset` requires Hyprland 0.45.0+.

## Installation

## Configuration

Config file: `~/.config/hypr/hyprsunset.conf` (recommended but not required).

hyprsunset uses profiles activated at specific times. Each profile resets all options set by other profiles. On startup, the current profile is applied.

Example: with config below at 20:00, first profile activates (no change). At 21:00, second profile applies.

```ini
max-gamma = 150
profile {
    time = 7:30
    identity = true
}
profile {
    time = 21:00
    temperature = 5500
    gamma = 0.8
}
```

| Variable | Description | Type | Default |
|---|---|---|---|
| `max-gamma` | Maximum gamma value. Absolute max is `200`%. Useful for IPC control. | int | `100` |

### Profile

| Variable | Description | Type | Default |
|---|---|---|---|
| `time` | Activation time in `{hours}:{minutes}` format | string | `00:00` |
| `temperature` | Screen temperature (lower = warmer) | int | `6000` |
| `gamma` | Perceived screen brightness (can go below monitor's minimum) | float | `1.0` |
| `identity` | Ignore temperature; only gamma affects apparent brightness | bool | `false` |

## Usage

Autostart: add `exec-once = hyprsunset` to `hyprland.conf`, or use `systemctl --user enable --now hyprsunset.service`.

Override current profile's temperature:

```bash
hyprsunset --temperature 5000  # overridden when a new profile activates
```

`hyprsunset --help` for all CLI arguments.

## IPC

hyprsunset supports IPC via `hyprctl`:

```sh
# Enable blue-light filter
hyprctl hyprsunset temperature 2500
# Disable blue-light filter
hyprctl hyprsunset identity
# Set gamma to 50%
hyprctl hyprsunset gamma 50
# Increase gamma by 10%
hyprctl hyprsunset gamma +10
# Reset config to current profile
hyprctl hyprsunset reset
# Reset specific value to current profile
hyprctl hyprsunset reset temperature
hyprctl hyprsunset reset gamma
hyprctl hyprsunset reset identity
# Print current profile
hyprctl hyprsunset profile
```

Example keybinds for gamma control:

```ini
bindel = ,XF86MonBrightnessDown, exec, hyprctl hyprsunset gamma -10
bindel = ,XF86MonBrightnessUp, exec, hyprctl hyprsunset gamma +10
```

> [!warning]
> Gamma control degrades color accuracy. Use monitor's software control if available.

[[036-hypr-ecosystem-hyprsysteminfo|hyprsysteminfo]] [[056-hypr-ecosystem-hyprpolkitagent|hyprpolkitagent]]

Last updated on April 20, 2026