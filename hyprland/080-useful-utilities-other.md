---
title: Other
url: https://wiki.hypr.land/Useful-Utilities/Other/
source: sitemap
fetched_at: 2026-04-26T09:48:48.498964002-03:00
rendered_js: false
word_count: 359
summary: This document provides a curated list of third-party tools, utilities, and applications that enhance the functionality of the Hyprland window manager.
tags:
    - hyprland
    - wayland
    - utilities
    - system-tools
    - desktop-environment
    - software-list
category: reference
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Curated third-party tools that extend Hyprland functionality.

## Workspace management[](#workspace-management)

[split-monitor-workspaces](https://github.com/Duckonaut/split-monitor-workspaces) by *Stanisław Zagórowski* — Awesome-like workspaces for Hyprland.

## Window switchers[](#window-switchers)

[snappy-switcher](https://github.com/OpalAayan/snappy-switcher) by *OpalAayan* — Blazing-fast, animated Alt+Tab window switcher for Hyprland written in C (Pango and Cairo).

## Keyboard layout management[](#keyboard-layout-management)

[hyprland-per-window-layout](https://github.com/coffebar/hyprland-per-window-layout/) by *MahouShoujoMivutilde and coffebar* — Per-window keyboard layouts for Hyprland.

## Editor support for config files[](#editor-support-for-config-files)

[HyprLS](https://github.com/hyprland-community/hyprls) by *gwennlbh* — LSP server for auto-completion in Hyprland config files (Neovim, VS Code, others).

## Keybind management[](#keybind-management)

[hyprKCS](https://github.com/kosa12/hyprKCS) by *kosa12* — Fast, minimal Hyprland keybind manager in Rust/GTK4.

## IPC wrappers[](#ipc-wrappers)

[hyprland-rs](https://github.com/yavko/hyprland-rs) by *yavko* — Rust wrapper for Hyprland IPC.

## Screen shaders/color temperature[](#screen-shaderscolor-temperature)

- [hyprshade](https://github.com/loqusion/hyprshade) by *loqusion* — Swap and schedule screen shaders; also an automatic color temperature shifter like [f.lux](https://en.wikipedia.org/wiki/F.lux).
- [gammastep](https://gitlab.com/chinstrap/gammastep) by *Chinstrap* — Automatic color temperature based on time of day and location.

## Wireless settings[](#wireless-settings)

- [iwgtk](https://github.com/J-Lentz/iwgtk) — WiFi settings frontend for `iwd` in GTK.
- [blueberry](https://github.com/linuxmint/blueberry) — Bluetooth settings frontend in GTK.
- [Overskride](https://github.com/kaii-lb/overskride) by *kaii-lb* — GTK4 Bluetooth client.
- [nm-applet](https://gitlab.gnome.org/GNOME/network-manager-applet) — GTK applet for NetworkManager.

## Automatically mounting with `udiskie`[](#automatically-mounting-using-udiskie)

USB mass storage devices are not mounted automatically. Many DEs handle this via `udisks2` wrappers.

`udiskie` is a udisks2 frontend for managing removable media from userspace.

Install via your package manager or [build manually](https://github.com/coldfix/udiskie/wiki/installation). Add to your `hyprland.conf`:

```ini
exec-once = udiskie &
```

See the [udiskie usage guide](https://github.com/coldfix/udiskie/wiki/Usage) for more.

## Monitor configuration[](#monitor-configuration)

[Monique](https://github.com/ToRvaLDz/monique) by *ToRvaLDz* — Graphical monitor configurator for Hyprland and Sway with drag-and-drop layout, profile system, and hotplug daemon.

## Other useful utilities[](#other-useful-utilities)

[We Are Wayland Now](https://wearewaylandnow.com/) details docks, email clients, compatibility info, and other utilities for Wayland.
