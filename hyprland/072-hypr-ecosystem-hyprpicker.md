---
title: hyprpicker
url: https://wiki.hypr.land/Hypr-Ecosystem/hyprpicker/
source: sitemap
fetched_at: 2026-04-26T09:47:22.704601908-03:00
rendered_js: false
word_count: 156
summary: This document provides a reference for the command-line flags and configuration options available for the hyprpicker color selection utility on Hyprland.
tags:
    - hyprland
    - color-picker
    - cli-utility
    - desktop-environment
    - screen-capture
category: reference
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

[hyprpicker](https://github.com/hyprwm/hyprpicker) picks colors from the screen on Hyprland.

## Flags[](#flags)

No config file needed — CLI flags only.

| Flag | Description | Args |
|---|---|---|
| `-a`, `--autocopy` | Auto-copy result to clipboard (requires wl-clipboard) | none |
| `-f`, `--format=` | Output format | `cmyk`, `hex`, `rgb`, `hsl`, `hsv` |
| `-o`, `--output-format=` | Custom format string | e.g. `rgb({0}, {1}, {2})` |
| `-n`, `--notify` | Desktop notification on pick (requires notify-send + daemon) | none |
| `-b`, `--no-fancy` | Disable colored output | none |
| `-h`, `--help` | Show help | none |
| `-r`, `--render-inactive` | Freeze inactive displays | none |
| `-z`, `--no-zoom` | Disable zoom lens | none |
| `-q`, `--quiet` | Disable most logs (errors only) | none |
| `-v`, `--verbose` | Enable verbose logs | none |
| `-t`, `--no-fractional` | Disable fractional scaling support | none |
| `-d`, `--disable-hex-preview` | Disable live hex preview | none |
| `-l`, `--lowercase-hex` | Output hex in lowercase | none |
| `-s`, `--scale=` | Zoom scale | float 1.0–10.0 |
| `-u`, `--radius=` | Circle radius | int 1–1000 |
| `-V`, `--version` | Print version | none |

See also: [[055-hypr-ecosystem-hyprpaper|hyprpaper]], [[054-hypr-ecosystem-hyprlauncher|hyprlauncher]]