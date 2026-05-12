---
title: hyprqt6engine
url: https://wiki.hypr.land/Hypr-Ecosystem/hyprqt6engine/
source: sitemap
fetched_at: 2026-04-26T09:49:04.341371208-03:00
rendered_js: false
word_count: 133
summary: This document describes how to install and configure hyprqt6engine, a theme engine for Qt6 applications designed for compatibility with KDE color schemes.
tags:
    - qt6-theming
    - hyprland
    - desktop-customization
    - linux-gui
    - kde-compatibility
category: configuration
optimized: true
optimized_at: 2026-04-26T10:00:00Z
---

# hyprqt6engine

[hyprqt6engine](https://github.com/hyprwm/hyprqt6engine) provides a theme for QT6 apps. A replacement for qt6ct, compatible with KDE Apps / KColorScheme.

## Usage

Install, then set `QT_QPA_PLATFORMTHEME=hyprqt6engine`. Set as `env=` in Hyprland, or in `/etc/environment` for system-wide.

## Configuration

Config file: `~/.config/hypr/hyprqt6engine.conf`

### Theme (category `theme:`)

| Variable | Description | Type | Default |
|----------|-------------|------|---------|
| `color_scheme` | Full path to a color scheme. Can be a qt6ct theme or a KColorScheme. Leave empty for defaults. | string | empty |
| `icon_theme` | Name of an icon theme to use. | string | empty |
| `style` | Widget style (e.g. Fusion or kvantum-dark). | string | `Fusion` |
| `font_fixed` | Font family for fixed width font. | string | `monospace` |
| `font_fixed_size` | Font size for fixed width font. | int | `11` |
| `font` | Font family for regular font. | string | `Sans Serif` |
| `font_size` | Font size for regular font. | int | `11` |

### Misc (category `misc:`)

| Variable | Description | Type | Default |
|----------|-------------|------|---------|
| `single_click_activate` | Whether single-clicks activate or open. | bool | `true` |
| `menus_have_icons` | Whether context menus include icons. | bool | `true` |
| `shortcuts_for_context_menus` | Whether context menu options show keyboard shortcuts. | bool | `true` |

#qt6-theming #kde-compatibility #desktop-customization