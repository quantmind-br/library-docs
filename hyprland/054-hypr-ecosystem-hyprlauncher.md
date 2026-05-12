---
title: hyprlauncher
url: https://wiki.hypr.land/Hypr-Ecosystem/hyprlauncher/
source: sitemap
fetched_at: 2026-04-26T09:47:36.399278945-03:00
rendered_js: false
word_count: 179
summary: This document provides an overview of the Hyprlauncher daemon, including instructions for usage, daemon management, and available configuration options for customizing themes, finders, and UI elements.
tags:
    - hyprland
    - launcher
    - daemon
    - linux-desktop
    - system-configuration
    - application-launcher
category: configuration
optimized: true
optimized_at: 2026-04-26T10:00:00Z
---

# hyprlauncher

[hyprlauncher](https://github.com/hyprwm/hyprlauncher) is a multipurpose, versatile launcher/picker for Hyprland. Fast, simple, provides various modules.

## Usage

Hyprlauncher is always a daemon. Launching it spawns a daemon that listens for requests. Use `hyprlauncher -d` to avoid opening a window on first launch. Bind `hyprlauncher` to a key to open it.

## Configuration

Theme follows your [[073-hypr-ecosystem-hyprtoolkit|hyprtoolkit]] theme.

Config file: `~/.config/hypr/hyprlauncher.conf`

### General

| Option | Description | Type | Default |
|--------|-------------|------|---------|
| `grab_focus` | Force a full keyboard focus grab. | bool | `true` |

### Cache

| Option | Description | Type | Default |
|--------|-------------|------|---------|
| `enabled` | Controls whether modules keep a cache of often used entries. History is stored in plain text at `~/.local/share/hyprlauncher`. | bool | `true` |

### Finders

Available finders: `math`, `desktop`, `unicode`. Prefixes can only be one character.

| Option | Description | Type | Default |
|--------|-------------|------|---------|
| `default_finder` | Default finder. | string | `desktop` |
| `desktop_prefix` | Prefix for desktop finder. | string | empty |
| `unicode_prefix` | Prefix for unicode finder. | string | `.` |
| `math_prefix` | Prefix for math finder. | string | `=` |
| `font_prefix` | Prefix for font finder. | string | `'` |
| `desktop_launch_prefix` | Launch prefix for each desktop app, e.g. `uwsm app --`. | string | empty |
| `desktop_icons` | Enable desktop icons in results. | bool | `true` |

### UI

| Option | Description | Type | Default |
|--------|-------------|------|---------|
| `window_size` | Size of the launcher. | vec2 | `400 260` |

#launcher #daemon #application-launcher