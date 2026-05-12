---
title: Monitors
url: https://wiki.hypr.land/Configuring/Monitors/
source: sitemap
fetched_at: 2026-04-26T09:47:52.771895867-03:00
rendered_js: false
word_count: 1282
summary: This document describes the syntax and configuration options for defining monitor settings, including resolution, positioning, scaling, mirroring, and color management in Hyprland.
tags:
    - hyprland
    - monitor-configuration
    - display-settings
    - linux-desktop
    - compositor-config
category: configuration
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## General

Monitor config syntax:

```ini
monitor = name, resolution, position, scale
```

Example:

```ini
monitor = DP-1, 1920x1080@144, 0x0, 1
```

This sets monitor `DP-1` to 1920x1080 at 144Hz, at position `0x0` (top-left), scale 1 (unscaled).

List all monitors: `hyprctl monitors all` (active and inactive).

Monitors are positioned on a virtual layout. `position` is in pixels from the top-left corner.

Examples placing DP-1 left of DP-2:

```ini
monitor = DP-1, 1920x1080, 0x0, 1
monitor = DP-2, 1920x1080, 1920x0, 1
```

Or right:

```ini
monitor = DP-1, 1920x1080, 1920x0, 1
monitor = DP-2, 1920x1080, 0x0, 1
```

Negative values work:

```ini
monitor = DP-1, 1920x1080, 0x0, 1
monitor = DP-2, 1920x1080, -1920x0, 1
```

Hyprland uses an inverse Y cartesian system. Negative y places a monitor higher, positive y places it lower:

```ini
monitor = DP-1, 1920x1080, 0x0, 1
monitor = DP-2, 1920x1080, 0x-1080, 1   # above DP-1
```

> [!note]
> Position is calculated with the scaled (and transformed) resolution. For a 4K monitor with scale 2 to the left of a 1080p, use `1920x0` for the second screen. If rotated 90 degrees, use `1080x0`.

> [!warning]
> No monitors can overlap — overlapping monitors produce a warning.

> [!note]
> "Invalid scale" warnings appear when scale does not produce valid logical pixels. A valid scale must divide the resolution cleanly (without decimals). Example: 1920x1080 / 1.5 = 1280x720 → OK, but / 1.4 → 1371.4286x771.42857 → not OK.

Leaving `name` empty creates a fallback rule for unmatched monitors.

### Special resolution values

- `preferred` — use display's preferred size and refresh rate
- `highres` — use highest supported resolution
- `highrr` — use highest supported refresh rate
- `maxwidth` — use widest supported resolution

### Special position values

- `auto` — Hyprland decides position, placing each new monitor to the right of existing ones using top-left corner as root
- `auto-right/left/up/down` — place monitor to right/left/above/below other monitors using top-left corner as root
- `auto-center-right/left/up/down` — same but calculate from each monitor's center

> [!note]
> For the first monitor, specifying a direction is allowed but has no effect — it positions at (0,0). The direction is always from center out.

### Auto scale

Use `auto` as scale to let Hyprland decide based on monitor PPI.

Recommended for plugging in random monitors:

```ini
monitor = , preferred, auto, 1
```

Any unspecified monitor auto-places to the right with its preferred resolution.

Use the output's `description` (from `hyprctl monitors`) to specify a monitor:

```ini
monitor = desc:Chimei Innolux Corporation 0x150C, preferred, auto, 1.5
```

Remove the `(portname)` from the description.

### Custom modelines

```ini
monitor = DP-1, modeline 1071.101 3840 3848 3880 3920 2160 2263 2271 2277 +hsync -vsync, 0x0, 1
```

### Disabling a monitor

> [!warning]
> Disabling a monitor removes it from the layout, moving all windows/workspaces to remaining monitors. To turn off just the monitor (screensaver style), use the `dpms` [dispatcher](https://wiki.hypr.land/Configuring/Dispatchers).

## Custom reserved area

Reserved area remains unoccupied by tiled windows:

```ini
monitor = name, addreserved, TOP, BOTTOM, LEFT, RIGHT
```

Where values are integers in pixels. Stacks on top of calculated reserved area (e.g. bars). Only one rule per monitor allowed.

## Extra args

Combine extra arguments at the end of the monitor rule:

```ini
monitor = eDP-1, 2880x1800@90, 0x0, 1, transform, 1, mirror, DP-2, bitdepth, 10
```

### Mirrored displays

```ini
monitor = DP-3, 1920x1080@60, 0x0, 1, mirror, DP-2
monitor = , preferred, auto, 1, mirror, DP-1
```

> [!note]
> Mirroring does not re-render at the second monitor's resolution. A 1080p screen mirrored to 4K displays at 1080p with possible squishing/stretching.

### 10 bit support

```ini
monitor = eDP-1, 2880x1800@90, 0x0, 1, bitdepth, 10
```

> [!warning]
> Colors registered in Hyprland do *not* support 10 bit. Some applications do *not* support screen capture with 10 bit enabled.

### Color management presets

```ini
monitor = eDP-1, 2880x1800@90, 0x0, 1, bitdepth, 10, cm, wide
```

| Preset | Description |
|--------|-------------|
| `auto` | sRGB for 8bpc, wide for 10bpc if supported (recommended) |
| `srgb` | sRGB primaries (default) |
| `dcip3` | DCI P3 primaries |
| `dp3` | Apple P3 primaries |
| `adobe` | Adobe RGB primaries |
| `wide` | wide color gamut, BT2020 primaries |
| `edid` | primaries from edid (may be inaccurate) |
| `hdr` | wide color gamut + HDR PQ transfer function (experimental) |
| `hdredid` | same as hdr with edid primaries (experimental) |

Fullscreen HDR is possible without `hdr` if `render:cm_fs_passthrough` is enabled.

Control SDR brightness and saturation in HDR mode with `sdrbrightness, B` and `sdrsaturation, S` (default 1.0, typical range 1.0–2.0):

```ini
monitor = eDP-1, 2880x1800@90, 0x0, 1, bitdepth, 10, cm, hdr, sdrbrightness, 1.2, sdrsaturation, 0.98
```

SDR EOTF (default `0` follows `render:cm_sdr_eotf`): `1` = piecewise sRGB, `2` = Gamma 2.2.

### ICC Profiles

Load via `, icc, /path/to/icc.icm` (or `icc = path` in v2).

> [!note]
> - Path must be absolute
> - ICC applied forces `sdr_eotf` to `sRGB` for color accuracy
> - ICC applied overrides CM preset
> - ICCs are incompatible with HDR gaming

### VRR

Per-display VRR: add `, vrr, X` where X is the mode from the [variables page](https://wiki.hypr.land/Configuring/Variables).

## Rotating

```ini
monitor = eDP-1, 2880x1800@90, 0x0, 1, transform, 1
```

Transform list:

| Value | Transform |
|-------|-----------|
| 0 | normal (no transform) |
| 1 | 90 degrees |
| 2 | 180 degrees |
| 3 | 270 degrees |
| 4 | flipped |
| 5 | flipped + 90 degrees |
| 6 | flipped + 180 degrees |
| 7 | flipped + 270 degrees |

## Monitor v2

Alternative syntax:

```ini
monitorv2 {
  output = DP-1
  mode = 1920x1080@144
  position = 0x0
  scale = 1
  transform = 2
}
```

`monitor = DP-1,1920x1080@144,0x0,1,transform,2` is equivalent.

`disable` flag becomes `disabled = true`. Other named settings use `name = value` syntax (`bitdepth,10` → `bitdepth = 10`).

#### EDID overrides and SDR → HDR settings

| Name | Description | Type |
|------|-------------|------|
| `supports_wide_color` | Force wide color gamut (0 auto, 1 force on, -1 force off) | int |
| `supports_hdr` | Force HDR support. Requires wide color gamut | int |
| `sdr_min_luminance` | SDR minimum luminance for SDR → HDR mapping. Set to 0.005 for true black | float |
| `sdr_max_luminance` | SDR maximum luminance. Typical range 80–400, likely 200–250 | int |
| `min_luminance` | Monitor's minimum luminance | float |
| `max_luminance` | Monitor's maximum possible luminance | float |
| `max_avg_luminance` | Monitor's maximum average luminance for typical frame | int |
| `sdr_eotf` | Transfer function for SDR apps (default: Gamma 2.2, gamma22, sRGB) | string |

> [!warning]
> These values may be passed to the monitor firmware and cause burn-in or damage if firmware lacks safety checks.

## Default workspace

See [Workspace Rules](https://wiki.hypr.land/Configuring/Workspace-Rules).

### Binding workspaces to a monitor

See [Workspace Rules](https://wiki.hypr.land/Configuring/Workspace-Rules).
