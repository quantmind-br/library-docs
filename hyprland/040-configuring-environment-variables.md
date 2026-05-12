---
title: Environment variables
url: https://wiki.hypr.land/Configuring/Environment-variables/
source: sitemap
fetched_at: 2026-04-26T09:49:24.561198078-03:00
rendered_js: false
word_count: 639
summary: This document provides instructions and best practices for configuring environment variables within the Hyprland window manager, including specific settings for toolkits, NVIDIA hardware, and session management.
tags:
    - hyprland
    - environment-variables
    - wayland
    - linux-configuration
    - display-server
    - nvidia-setup
category: configuration
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

> [!info]
> [uwsm](https://wiki.hypr.land/Useful-Utilities/Systemd-start) users should avoid placing environment variables in `hyprland.conf`. Use `~/.config/uwsm/env` for theming, xcursor, Nvidia and toolkit variables, and `~/.config/uwsm/env-hyprland` for `HYPR*` and `AQ_*` variables. Format: `export KEY=VAL`. See the [uwsm readme](https://github.com/Vladimir-csp/uwsm?tab=readme-ov-file#4-environments-and-shell-profile) for details.

Use the `env` keyword to set environment variables prior to Display Server initialization.

> [!warning]
> Hyprland reads `env` values as **raw strings** and puts them into the environment as-is. Do NOT add quotes around values.

Examples:

```py
# WRONG — quotes around values
env = QT_AUTO_SCREEN_SCALE_FACTOR,"1"
env = QT_QPA_PLATFORM,"wayland"
env = QT_QPA_PLATFORM,"wayland;xcb"
env = AQ_DRM_DEVICES=,"/dev/dri/card1:/dev/dri/card0"
```

```py
# CORRECT — no quotes
env = QT_AUTO_SCREEN_SCALE_FACTOR,1
env = QT_QPA_PLATFORM,wayland
env = QT_QPA_PLATFORM,wayland;xcb
env = AQ_DRM_DEVICES=,/dev/dri/card1:/dev/dri/card0
```

> [!warning]
> Avoid putting environment variables in `/etc/environment` — that will cause all sessions (including Xorg ones) to inherit Wayland-specific environment on traditional Linux distros.

## Hyprland Environment Variables

| Variable | Description |
|---|---|
| `HYPRLAND_TRACE=1` | Enables more verbose logging |
| `HYPRLAND_NO_RT=1` | Disables realtime priority setting |
| `HYPRLAND_NO_SD_NOTIFY=1` | If systemd, disables `sd_notify` calls |
| `HYPRLAND_NO_SD_VARS=1` | Disables management of variables in systemd/dbus activation |
| `HYPRLAND_CONFIG` | Specifies custom Hyprland config path |

## Aquamarine Environment Variables

| Variable | Description |
|---|---|
| `AQ_TRACE=1` | Enables more verbose logging |
| `AQ_DRM_DEVICES=` | Colon-separated list of DRM devices (GPUs), first is primary. E.g.: `/dev/dri/card1:/dev/dri/card0` |
| `AQ_FORCE_LINEAR_BLIT=0` | Disables forcing linear explicit modifiers on Multi-GPU buffers (Nvidia workaround) |
| `AQ_MGPU_NO_EXPLICIT=1` | Disables explicit syncing on Multi-GPU buffers |
| `AQ_NO_MODIFIERS=1` | Disables modifiers for DRM buffers |

## Toolkit Backend Variables

| Variable | Purpose |
|---|---|
| `env = GDK_BACKEND,wayland,x11,*` | GTK: use Wayland, fall back to X11, then any other GDK backend |
| `env = QT_QPA_PLATFORM,wayland;xcb` | Qt: use Wayland, fall back to X11 |
| `env = SDL_VIDEODRIVER,wayland` | Run SDL2 apps on Wayland (set `x11` if games have compatibility issues) |
| `env = CLUTTER_BACKEND,wayland` | Force Clutter applications to use Wayland backend |

## XDG Specifications

```ini
env = XDG_CURRENT_DESKTOP,Hyprland
env = XDG_SESSION_TYPE,wayland
env = XDG_SESSION_DESKTOP,Hyprland
```

XDG env vars are often detected through portals, but setting them explicitly is recommended. If your desktop portal is malfunctioning with no errors, the XDG env is likely misconfigured.

> [!info]
> [uwsm](https://wiki.hypr.land/Useful-Utilities/Systemd-start) users don't need to set XDG env vars — uwsm sets them automatically.

## Qt Variables

| Variable | Purpose |
|---|---|
| `env = QT_AUTO_SCREEN_SCALE_FACTOR,1` | Enables automatic scaling based on monitor pixel density |
| `env = QT_QPA_PLATFORM,wayland;xcb` | Tell Qt apps to use Wayland, fall back to X11 |
| `env = QT_WAYLAND_DISABLE_WINDOWDECORATION,1` | Disables window decorations on Qt apps |
| `env = QT_QPA_PLATFORMTHEME,qt5ct` | Use qt5ct theme with Kvantum |

## NVIDIA Specific

Force GBM backend:

```ini
env = GBM_BACKEND,nvidia-drm
env = __GLX_VENDOR_LIBRARY_NAME,nvidia
```

> [!note]
> See [Archwiki Wayland Page](https://wiki.archlinux.org/title/Wayland#Requirements) for details on those variables.

Other NVIDIA variables:

| Variable | Purpose |
|---|---|
| `env = LIBVA_DRIVER_NAME,nvidia` | Hardware acceleration on NVIDIA GPUs |
| `__GL_GSYNC_ALLOWED` | Controls if G-Sync capable monitors use Variable Refresh Rate (VRR) |
| `__GL_VRR_ALLOWED` | Controls if Adaptive Sync is used. Set as `0` to avoid problems in some games |
| `env = AQ_NO_ATOMIC,1` | Use legacy DRM interface instead of atomic mode setting (**not recommended**) |

> [!note]
> See [Archwiki Hardware Acceleration Page](https://wiki.archlinux.org/title/Hardware_video_acceleration) for valid values before setting `LIBVA_DRIVER_NAME`.
> See [Nvidia Documentation](https://download.nvidia.com/XFree86/Linux-32bit-ARM/375.26/README/openglenvvariables.html) for `__GL_GSYNC_ALLOWED` details.

## Theming Related Variables

| Variable | Purpose |
|---|---|
| `GTK_THEME` | Set GTK theme manually (avoid appearance tools like lxappearance or nwg-look) |
| `XCURSOR_THEME` | Set cursor theme (must be installed and readable by user) |
| `XCURSOR_SIZE` | Set cursor size |

Last updated on April 20, 2026

[[050-configuring-xwayland|XWayland]] [[044-configuring-multi-gpu|Multi-GPU]]