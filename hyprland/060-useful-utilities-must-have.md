---
title: Must have
url: https://wiki.hypr.land/Useful-Utilities/Must-have/
source: sitemap
fetched_at: 2026-04-26T09:47:17.174468788-03:00
rendered_js: false
word_count: 307
summary: This document outlines the essential software dependencies and system components required to ensure optimal performance and functionality when using the Hyprland compositor.
tags:
    - hyprland
    - desktop-environment
    - system-configuration
    - linux-desktop
    - software-dependencies
category: configuration
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Essential dependencies for a smooth Hyprland experience. DEs like Plasma or GNOME handle these automatically; Hyprland does not.

## Notification daemon[](#notification-daemon)

*Startup:* Auto via D-Bus on notification emit, or `exec-once` in `hyprland.conf`.

Many apps (e.g. Discord) freeze without one. Examples: `dunst`, `mako`, `fnott`, `swaync`.

## Pipewire[](#pipewire)

*Startup:* Auto on systemd, manual otherwise.

Required for screensharing. Install `pipewire` and `wireplumber` (**not** `pipewire-media-session`).

> [!info]
> Non-systemd distros (Gentoo, Artix) provide a launcher (e.g. `<distro>-pipewire-launcher`). If missing, consult your distro's docs.

## XDG Desktop Portal[](#xdg-desktop-portal)

*Startup:* Auto on systemd, manual otherwise.

Handles file pickers, screensharing, and more. See [[011-hypr-ecosystem-xdg-desktop-portal-hyprland|xdg-desktop-portal-hyprland]].

## Authentication Agent[](#authentication-agent)

*Startup:* Manual (`exec-once`).

Pops up password windows for privilege elevation. See [[056-hypr-ecosystem-hyprpolkitagent|hyprpolkitagent]].

## Qt Wayland Support[](#qt-wayland-support)

*Startup:* None (library only).

Install `qt5-wayland` and `qt6-wayland`.

## Fonts[](#fonts)

*Startup:* None (library only).

A `sans-serif` font is required — without one, text renders as squares. Use `noto-fonts` or similar.

For icons, install a Nerd Font or FontAwesome. Hyprland prefers Nerd Font > FontAwesome > text fallback.