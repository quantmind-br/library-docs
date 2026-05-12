---
title: "Terminal features"
url: https://docs.warp.dev/terminal/terminal-features
source: sitemap
fetched_at: 2026-04-29T15:03:17-03:00
rendered_js: false
word_count: 289
summary: This document provides a comparative feature matrix for several popular macOS terminal emulators, detailing their support for various text rendering and formatting capabilities.
tags:
    - terminal-emulator
    - macos-terminal
    - feature-comparison
    - text-rendering
    - terminal-compatibility
category: reference
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
# Terminal Features

Feature matrix comparing Warp against other macOS terminal emulators.

| Feature | Warp | Terminal.app | iTerm | Alacritty | Wezterm |
|---|---|---|---|---|---|
| 24-bit (true color) | YES | NO | YES | YES | YES |
| Bold | YES | YES | YES | YES | YES |
| Dim | NO | YES | YES | YES | YES |
| Italic | NO | YES | YES | YES | YES |
| Underline | YES | YES | YES | YES | YES |
| Underline (alt) | YES | NO | YES | YES | YES |
| Double underline | NO | NO | NO | NO | YES |
| Double underline (alt) | YES | NO | YES | YES | YES |
| Curly underline | NO | NO | YES | NO | YES |
| Colored underline | NO | NO | NO | NO | YES |
| Blink | NO | YES | NO | NO | NO |
| Reverse | YES | YES | YES | YES | YES |
| Invisible (copy-paste-able) | NO | YES | NO | YES | NO |
| Strikethrough | YES | NO | YES | YES | YES |
| Overline | NO | NO | NO | NO | YES |
| [Magic string](https://en.wikipedia.org/wiki/Unicode#Web) | YES | YES | YES | YES | YES |
| Emojis | YES | YES | YES | YES | YES |
| Right-to-left | NO | YES | NO | NO | NO |
| Sixel graphics | NO | NO | YES | NO | NO |

Based on [terminal-testdrive.sh](https://gist.github.com/hellricer/e514d9615d02838244d8de74d0ab18b3).

#terminal #feature-comparison
