---
title: hyprpolkitagent
url: https://wiki.hypr.land/Hypr-Ecosystem/hyprpolkitagent/
source: sitemap
fetched_at: 2026-04-26T09:48:46.529110878-03:00
rendered_js: false
word_count: 126
summary: This document provides instructions on installing and configuring the hyprpolkitagent authentication daemon for use within the Hyprland window manager environment.
tags:
    - hyprland
    - polkit
    - authentication-daemon
    - systemd
    - linux-configuration
    - desktop-environment
category: configuration
optimized: true
optimized_at: 2026-04-26T10:00:00Z
---

# hyprpolkitagent

[hyprpolkitagent](https://github.com/hyprwm/hyprpolkitagent) is a polkit authentication daemon required for GUI applications to request elevated privileges.

If unavailable in your distro's repos, build from [source](https://github.com/hyprwm/hyprpolkitagent) or use a different agent (e.g. [KDE's](https://github.com/KDE/polkit-kde-agent-1/)).

## Usage

Add to Hyprland config:

```ini
exec-once = systemctl --user start hyprpolkitagent
```

Restart Hyprland. If using [[026-useful-utilities-systemd-start|uwsm]], autostart with:

```bash
systemctl --user enable --now hyprpolkitagent.service
```

On distributions with a different init system (e.g. Gentoo), use:

```bash
exec-once=/usr/lib64/libexec/hyprpolkitagent
```

Other possible paths: `/usr/lib/hyprpolkitagent` and `/usr/libexec/hyprpolkitagent`.

#polkit #authentication-daemon #systemd