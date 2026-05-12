---
title: hyprtoolkit
url: https://wiki.hypr.land/Hypr-Ecosystem/hyprtoolkit/
source: sitemap
fetched_at: 2026-04-26T09:49:36.701512793-03:00
rendered_js: false
word_count: 128
summary: This document provides an overview and configuration reference for hyprtoolkit, a GUI development toolkit designed for Wayland compositors.
tags:
    - wayland
    - gui-toolkit
    - hyprland
    - configuration-reference
    - linux-desktop
category: reference
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

[hyprtoolkit](https://github.com/hyprwm/hyprtoolkit) is a GUI toolkit for native Wayland applications. Built for Hyprland, compatible with any modern Wayland compositor.

For developer docs, see [[010-hypr-ecosystem-hyprtoolkit-development|Development]].

## Configuration[](#configuration)

Config file: `~/.config/hypr/hyprtoolkit.conf`. Supports the same color options as Hyprland.

| Variable | Type | Default | Description |
|---|---|---|---|
| `background` | color | `0xFF181818` | Background color |
| `base` | color | `0xFF202020` | Base color |
| `text` | color | `0xFFDADADA` | Text color |
| `alternate_base` | color | `0xFF272727` | Alternative base color |
| `bright_text` | color | `0xFFFFDEDE` | Bright text color |
| `accent` | color | `0xFF00FFCC` | Accent color |
| `accent_secondary` | color | `0xFF0099F0` | Secondary accent color |
| `h1_size` | int | `19` | H1 font size |
| `h2_size` | int | `15` | H2 font size |
| `h3_size` | int | `13` | H3 font size |
| `font_size` | int | `11` | Regular text font size |
| `small_font_size` | int | `10` | Small text font size |
| `icon_theme` | string | *(empty)* | Icon theme name (empty = first found) |
| `font_family` | string | `Sans Serif` | Font family |
| `font_family_monospace` | string | `monospace` | Monospace font family |
| `rounding_large` | int | `10` | Large rounding (logical px) |
| `rounding_small` | int | `5` | Small rounding (logical px) |