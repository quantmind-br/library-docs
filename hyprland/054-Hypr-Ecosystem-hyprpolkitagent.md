---
title: hyprpolkitagent
url: https://wiki.hypr.land/Hypr-Ecosystem/hyprpolkitagent/
source: sitemap
fetched_at: 2026-01-22T22:15:49.282619661-03:00
rendered_js: false
word_count: 119
summary: This document explains how to install and configure hyprpolkitagent, an authentication daemon used by GUI applications to request elevated privileges in Hyprland.
tags:
    - hyprland
    - polkit
    - authentication
    - systemd
    - configuration
    - automation
category: guide
---

[hyprpolkitagent](https://github.com/hyprwm/hyprpolkitagent) is a polkit authentication daemon. It is required for GUI applications to be able to request elevated privileges.

If it’s not available in your distro’s repositories, you can either [build it from source](https://github.com/hyprwm/hyprpolkitagent) or use a different agent, e.g. [KDE’s one](https://github.com/KDE/polkit-kde-agent-1/).

## Usage[](#usage)

Add `exec-once = systemctl --user start hyprpolkitagent` to your Hyprland config and restart hyprland. (obviously change that to whatever you are using if you are not using the hypr one)

If Hyprland is started with [uwsm](https://wiki.hypr.land/Useful-Utilities/Systemd-start), you can autostart the polkit agent with the command `systemctl --user enable --now hyprpolkitagent.service`.

On distributions that use a different init system, such as Gentoo, it may be necessary to use `exec-once=/usr/lib64/libexec/hyprpolkitagent` instead.

Other possible paths include `/usr/lib/hyprpolkitagent` and `/usr/libexec/hyprpolkitagent`.