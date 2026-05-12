---
title: Text, fonts, & cursor | Warp
url: https://docs.warp.dev/terminal/appearance/text-fonts-cursor
source: sitemap
fetched_at: 2026-04-29T15:02:51.193382315-03:00
rendered_js: false
word_count: 200
summary: This document provides instructions on how to customize text, font styles, and cursor behavior within the Warp terminal settings.
tags:
    - warp-terminal
    - appearance-settings
    - font-customization
    - cursor-configuration
    - terminal-ui
    - accessibility-settings
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
# Text, Fonts, & Cursor

Customize text, font styles, and cursor behavior in Warp terminal settings.

> [!info]
> After installing a new font, restart Warp for it to appear in the list. Check "View all available system fonts" if needed.

## Text and Fonts

Access via **Settings** > **Appearance** > **Text**.

| Setting | Description |
|---------|-------------|
| Font type | Select preferred font |
| Font weight | Adjust weight |
| Font size | Adjust size |
| Line height | Adjust spacing |
| Use thin strokes | Prevents blur on low-DPI displays (default: on; Linux: not supported) |
| Enforce minimum contrast | Tweaks named colors to meet accessibility standards (default: on) |
| Show ligatures | Enable ligatures (may reduce performance; Warp's default font Hack doesn't support ligatures) |

> [!tip]
> For ligatures, use a font with ligature support like [Fira Code](https://github.com/tonsky/FiraCode).

## Cursor

Access via **Settings** > **Appearance** > **Cursor**.

| Setting | Options |
|---------|---------|
| Cursor type | Bar, Block, or Underline |
| Blinking cursor | Toggle on/off (via Command Palette: "Cursor blink") |

> [!info]
> Cursor type preference is disabled while [Vim keybindings](https://docs.warp.dev/terminal/editor/vim) (vim mode) is active.
