---
title: hyprpaper
url: https://wiki.hypr.land/Hypr-Ecosystem/hyprpaper/
source: sitemap
fetched_at: 2026-04-26T09:47:17.001127187-03:00
rendered_js: false
word_count: 287
summary: This document provides installation, configuration, and usage instructions for hyprpaper, an IPC-controlled wallpaper utility designed for the Hyprland compositor.
tags:
    - hyprland
    - wallpaper-manager
    - linux-desktop
    - ipc-configuration
    - system-customization
category: configuration
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

[hyprpaper](https://github.com/hyprwm/hyprpaper) is a fast, IPC-controlled wallpaper utility for Hyprland.

## Installation

**Arch**

**openSUSE**

**Fedora**

## Configuration

Config file: `~/.config/hypr/hyprpaper.conf`. Optional.

### Setting wallpapers

Wallpapers are anonymous special categories. Monitor can be empty for a fallback.

| variable | description | type | default |
|----------|-------------|------|---------|
| `monitor` | Monitor for this wallpaper. Empty = fallback. | monitor ID | |
| `path` | Path to image file or directory of image files | path | |
| `fit_mode` | How to display the image | `contain` \| `cover` \| `tile` \| `fill` | `cover` |
| `timeout` | Seconds between wallpaper changes (for directories) | int | `30` |
| `order` | Order to display images from directory. Only `random` currently. | `random` | |
| `recursive` | Scan subdirectories recursively | bool | `false` |

```ini
wallpaper {
    monitor = DP-3
    path = ~/myFile.jxl
    fit_mode = cover
}
wallpaper {
    monitor = DP-2
    path = ~/myFile2.jxl
    fit_mode = cover
}
wallpaper {
    monitor =     path = ~/fallback.jxl
    fit_mode = cover
}
```

### Run at Startup

Add `exec-once = hyprpaper` to `hyprland.conf`. With [uwsm](https://wiki.hypr.land/Useful-Utilities/Systemd-start), use `systemctl --user enable --now hyprpaper.service`.

### Misc Options

Set outside `wallpaper{...}` sections.

| variable | description | type | default |
|----------|-------------|------|---------|
| `splash` | enable rendering of the hyprland splash over the wallpaper | bool | `true` |
| `splash_offset` | how far up the splash is displayed | float | `20` |
| `splash_opacity` | how opaque the splash is | float | `0.8` |
| `ipc` | whether to enable IPC | bool | `true` |

### Sourcing

```ini
source = ~/.config/hypr/hyprpaper.d/*.conf
```

> [!note]
> Parsing is LINEAR. Lines above `source =` parsed first, then sourced files, then lines below.

## IPC

Set wallpapers via `hyprctl`:

```sh
hyprctl hyprpaper wallpaper '[mon], [path], [fit_mode]'
```

`fit_mode` is optional. `mon` can be empty for a fallback (fallback applies to monitors never assigned a specific target).

Last updated on April 20, 2026

[[072-hypr-ecosystem-hyprpicker|hyprpicker]]