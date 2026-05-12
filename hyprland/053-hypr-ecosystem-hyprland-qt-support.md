---
title: hyprland-qt-support
url: https://wiki.hypr.land/Hypr-Ecosystem/hyprland-qt-support/
source: sitemap
fetched_at: 2026-04-26T09:48:58.266190103-03:00
rendered_js: false
word_count: 51
summary: This document describes the configuration options available for the hyprland-qt-support package, which provides a QML style for Qt6 applications within the Hyprland ecosystem.
tags:
    - hyprland
    - qt6
    - ui-configuration
    - qml-style
    - desktop-customization
category: configuration
optimized: true
optimized_at: 2026-04-26T10:00:00Z
---

# hyprland-qt-support

[hyprland-qt-support](https://github.com/hyprwm/hyprland-qt-support) provides a QML style for hypr* qt6 apps.

## Configuration

Config file: `~/.config/hypr/application-style.conf`

| Variable | Description | Type | Default |
|----------|-------------|------|---------|
| `roundness` | How much to round UI elements. | int [0..3] | `1` |
| `border_width` | Border width around UI elements. | int [0-3] | `1` |
| `reduce_motion` | Reduce motion (transitions, hover effects, etc). | bool | `false` |

#qt6 #qml-style #ui-configuration