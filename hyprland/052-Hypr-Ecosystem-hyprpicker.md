---
title: hyprpicker
url: https://wiki.hypr.land/Hypr-Ecosystem/hyprpicker/
source: sitemap
fetched_at: 2026-01-22T22:14:56.510308827-03:00
rendered_js: false
word_count: 99
summary: This document outlines the command-line flags and configuration options for hyprpicker, a color picker utility specifically built for the Hyprland Wayland compositor.
tags:
    - hyprpicker
    - hyprland
    - wayland
    - color-picker
    - command-line-tool
    - linux
category: reference
---

[hyprpicker](https://github.com/hyprwm/hyprpicker) is a neat utility for picking a color from your screen on Hyprland.

## Configuration[](#configuration)

Doesn’t require configuration, only launch flags:

FlagDescriptionArgs`-a` | `--autocopy`Automatically copies the output to the clipboard (requires wl-clipboard)none`-f` | `--format=`Specifies the output format`cmyk` | `hex` | `rgb` | `hsl` | `hsv``-n` | `--no-fancy`Disables the “fancy” (aka. colored) outputtingnone`-h` | `--help`Shows the help messagenone`-r` | `--render-inactive`Render (freeze) inactive displaysnone`-z` | `--no-zoom`Disable the zoom lensnone`-q` | `--quiet`Disable most logs (leaves errors)none`-v` | `--verbose`Enable more logsnone`-t` | `--no-fractional`Disable fractional scaling supportnone`-d` | `--disable-hex-preview`Disable live preview of Hex codenone`-l` | `--lowercase-hex`Outputs the hexcode in lowercasenone`-V` | `--version`Print version infonone