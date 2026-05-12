---
title: Master tutorial
url: https://wiki.hypr.land/Getting-Started/Master-Tutorial/
source: sitemap
fetched_at: 2026-04-26T09:47:24.657838288-03:00
rendered_js: false
word_count: 730
summary: This document serves as an introductory guide for new users to set up, launch, and configure the Hyprland tiling window manager on Linux systems.
tags:
    - hyprland
    - wayland
    - linux-desktop
    - window-manager
    - installation-guide
    - system-configuration
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

This tutorial covers everything needed to get started with Hyprland.

## Install Hyprland

See [[001-getting-started-installation|Installation]] first. Install `kitty` (default terminal emulator) from your distro's repos.

## Nvidia

> [!note]
> Skip if not using Nvidia.

See [[034-nvidia|Nvidia]] for environment setup and tweaks before launching.

## VM

> [!note]
> Skip if not using a VM.

Enable 3D acceleration in `virtio` config or `virt-manager`. Without it, Hyprland **will not work**. GPU passthrough also possible. 3D acceleration in VMs may be slow.

## Launching Hyprland

`start-hyprland` in tty. For systemd users, `uwsm` is available but has issues — Hyprland without it recommended.

> [!warning]
> Do **not** launch with root (`sudo`).

Launch flags: `start-hyprland -- -h`

### Login Managers

| Manager | Compatibility |
|---|---|
| SDDM | Works flawlessly. Install sddm >= 0.20.0 or [git version](https://github.com/sddm/sddm) to avoid [issue 1476](https://github.com/sddm/sddm/issues/1476) (90s shutdowns). |
| plasma-login-manager | Works flawlessly, depends on systemd |
| GDM | Works, crashes Hyprland on first launch |
| greetd | Works flawlessly, especially with [ReGreet](https://github.com/rharish101/ReGreet) |
| ly | Works flawlessly |

## Preconfigured Setups

Want Hyprland pre-configured like a DE? See [[003-getting-started-preconfigured-setups|Preconfigured setups]].

These include their own tutorials. If using one, you can skip most of this guide, but still read for recommended apps, X11 replacement info, and display configuration.

## Default Config

Use `SUPER + Q` to launch kitty. Default terminal configurable in `~/.config/hypr/hyprland.conf` ([example config](https://github.com/hyprwm/Hyprland/blob/main/example/hyprland.conf)).

## Critical Software

See [[060-useful-utilities-must-have|Must-have Software]] for essential Wayland/Hyprland tools.

## Monitors

See [[043-configuring-monitors|Monitors]] for display configuration.

## Apps / X11 Replacements

See [[082-useful-utilities|Useful Utilities]]. Also see [Sway wiki](https://github.com/swaywm/sway/wiki/Useful-add-ons-for-sway) and [Awesome-Hyprland](https://github.com/hyprland-community/awesome-hyprland).

## Configure Hyprland

See [[031-configuring|Configuring]] for full configuration guide.

## Cursors

- Change mouse cursor: see [[083-faq|FAQ#how-do-i-change-me-mouse-cursor]]
- Cursor not rendering: see [[083-faq|FAQ#me-cursor-no-render]]

## Themes

Not a full DE — use `lxappearance` or `nwg-look` (recommended) for GTK, [[057-hypr-ecosystem-hyprqt6engine|hyprqt6engine]] for Qt6 apps.

## Force Apps to Use Wayland

Chromium/Electron browsers need flags:

```
--enable-features=UseOzonePlatform --ozone-platform=wayland
```

Or in `chrome://flags`, search "ozone" and select Wayland. For Electron apps, add to `~/.config/electron-flags.conf`.

> [!note]
> VSCode does **not** work with these flags.

NixOS: set `NIXOS_OZONE_WL=1` environment variable.

Check app is running in XWayland: `hyprctl clients`

More env vars: [[040-configuring-environment-variables|Environment variables]]

#wayland #linux-desktop #installation-guide
