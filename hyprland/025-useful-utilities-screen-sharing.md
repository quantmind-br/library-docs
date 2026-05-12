---
title: Screen sharing
url: https://wiki.hypr.land/Useful-Utilities/Screen-Sharing/
source: sitemap
fetched_at: 2026-04-26T09:47:54.605270406-03:00
rendered_js: false
word_count: 150
summary: This document provides instructions for setting up screensharing in Hyprland using PipeWire and addresses compatibility workarounds for XWayland applications.
tags:
    - hyprland
    - screensharing
    - pipewire
    - wayland
    - xwayland
    - desktop-portal
category: guide
optimized: true
optimized_at: 2026-04-26T12:00:00Z
---

# Screen sharing

Screen sharing on Hyprland uses PipeWire.

## Prerequisites

- `pipewire`, `wireplumber`, [[011-hypr-ecosystem-xdg-desktop-portal-hyprland|xdg-desktop-portal-hyprland]] installed and running
- `bitdepth` in config matches your physical monitor → see [[043-configuring-monitors|Monitors]]

## Tutorial

See [Bruno Ancona Sala's gist](https://gist.github.com/brunoanc/2dea6ddf6974ba4e5d26c3139ffb7580) for a complete tutorial.

## XWayland apps (Discord, Skype, etc.)

XWayland apps can only see other XWayland windows — they cannot share a full screen or Wayland window.

The KDE team created [xwaylandvideobridge](https://invent.kde.org/system/xwaylandvideobridge) as a workaround. On Arch Linux, use the [AUR package](https://aur.archlinux.org/packages/xwaylandvideobridge-git).

> [!note]
> Hyprland doesn't support xwaylandvideobridge's window-hiding mechanism. Use window rules to achieve the same effect:

```ini
windowrule {
    name = xwayland-video-bridge-fixes
    match:class = xwaylandvideobridge
    no_initial_focus = true
    no_focus = true
    no_anim = true
    no_blur = true
    max_size = 1 1
    opacity = 0.0
}
```

See [KDE issue #1](https://invent.kde.org/system/xwaylandvideobridge/-/issues/1) for details.

Last updated on April 20, 2026

[[081-useful-utilities-wallpapers|Wallpapers]] [[078-useful-utilities-app-launchers|App launchers]]