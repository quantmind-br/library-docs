---
title: xdg-desktop-portal-hyprland
url: https://wiki.hypr.land/Hypr-Ecosystem/xdg-desktop-portal-hyprland/
source: sitemap
fetched_at: 2026-04-26T09:48:20.40559428-03:00
rendered_js: false
word_count: 399
summary: This document provides instructions on installing, configuring, and troubleshooting xdg-desktop-portal-hyprland (XDPH) to enable functionality like screensharing within the Hyprland compositor.
tags:
    - hyprland
    - xdg-desktop-portal
    - screensharing
    - linux-desktop
    - wayland
    - configuration
    - debugging
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

XDG Desktop Portals let applications communicate with the compositor via D-Bus. [xdg-desktop-portal-hyprland](https://github.com/hyprwm/xdg-desktop-portal-hyprland) (XDPH) is Hyprland's implementation, enabling screensharing, global shortcuts, and similar features.

> [!warning]
> XDPH doesn't implement a file picker. Install `xdg-desktop-portal-gtk` alongside XDPH.

> [!note]
> Throughout this document, `xdg-desktop-portal-hyprland` is referred to as XDPH.

## Installing[](#installing)

XDPH is automatically started by D-Bus when Hyprland starts. No manual installation needed.

## Usage[](#usage)

XDPH starts automatically with Hyprland. To verify it is running, screenshare anything or open OBS and select the PipeWire source — a Qt menu will appear asking what to share.

XDPH works on other wlroots compositors, but Hyprland-only features (e.g. window sharing) will not function.

For a nuclear restart option, use `exec-once`:

```sh
#!/bin/sh
sleep 1
killall -e xdg-desktop-portal-hyprland
killall xdg-desktop-portal
/usr/lib/xdg-desktop-portal-hyprland &
sleep 2
/usr/lib/xdg-desktop-portal &
```

Adjust paths if incorrect.

## Share Picker Doesn't Use the System Theme[](#share-picker-doesnt-use-the-system-theme)

Try one or both:

```sh
dbus-update-activation-environment --systemd --all
systemctl --user import-environment QT_QPA_PLATFORMTHEME
```

If it works, add to `exec-once` in your config.

## Using the KDE File Picker With XDPH[](#using-the-kde-file-picker-with-xdph)

XDPH uses GTK as a fallback file picker (see `/usr/share/xdg-desktop-portal/hyprland-portals.conf`). To use the KDE file picker instead, create `~/.config/xdg-desktop-portal/hyprland-portals.conf`:

~/.config/xdg-desktop-portal/hyprland-portals.conf

```ini
[preferred]
default = hyprland;gtk
org.freedesktop.impl.portal.FileChooser = kde
```

See the [xdg-desktop-portal Arch Wiki page](https://wiki.archlinux.org/title/XDG_Desktop_Portal) for details. Firefox and some applications may need additional configuration for the KDE file picker.

## Debugging[](#debugging)

For slow app launches or screensharing issues, check logs:

```sh
systemctl --user status xdg-desktop-portal-hyprland
```

Crashes typically indicate missing `qt6-wayland` or `qt5-wayland`.

If the portal does not autostart, manually starting fails, and no error logs appear, your [[040-configuring-environment-variables#xdg-specifications|XDG env variables]] are likely misconfigured.

## Configuration[](#configuration)

Config file: `~/.config/hypr/xdph.conf`

```ini
screencopy {
    max_fps = 60
}
```

### screencopy[](#category-screencopy)

| Variable | Type | Default | Description |
|---|---|---|---|
| `max_fps` | int | `120` | Maximum fps of a screensharing session. `0` means no limit. |
| `allow_token_by_default` | bool | `false` | If enabled, the "Allow restore token" box is ticked by default. |
| `custom_picker_binary` | string | `"hyprland-share-picker"` | If non-empty, uses that binary as the share picker. Must conform to the stdout selection layout of `hyprland-share-picker`. |
| `force_shm` | bool | `false` | If enabled, skips DMA-BUF and uses SHM for screensharing. Slower than DMA-BUF but works around DMA-BUF allocation failures on multi-GPU systems. |
