---
title: Syntax & error highlighting | Warp
url: https://docs.warp.dev/terminal/editor/syntax-error-highlighting
source: sitemap
fetched_at: 2026-04-29T15:02:23.216842769-03:00
rendered_js: false
word_count: 141
summary: This document explains how to manage syntax highlighting and error underlining features within the Warp terminal input editor to improve command readability and error detection.
tags:
    - warp-terminal
    - syntax-highlighting
    - error-underlining
    - command-line-interface
    - terminal-settings
    - input-editor
category: guide
optimized: true
optimized_at: 2026-04-29T19:02:00Z
---
Warp colors command parts and underlines invalid commands in the input editor.

## Syntax highlighting

Colors each part of a command (sub-commands, options/flags, arguments, variables) to improve readability.

> [!warning]
> Newly installed apps or aliases require a new Warp session (window, tab, or pane) to trigger syntax highlighting, even after `source`-ing RC files.

**Enable/disable:**
- [Command Palette](https://docs.warp.dev/terminal/command-palette): search "Syntax Highlighting"
- **Settings** → **Features** → **Terminal Input** → toggle "Syntax highlighting for commands"

## Error underlining

Underlines invalid commands with a dashed red underline (e.g., binary doesn't exist).

> [!warning]
> Same session delay applies — requires new Warp session after installing apps.

**Enable/disable:**
- [Command Palette](https://docs.warp.dev/terminal/command-palette): search "Syntax Highlighting"
- **Settings** → **Features** → **Terminal Input** → toggle "Error underlining for commands"

## Related

See [[105-terminal-editor-vim]] for Vim keybinding support in the input editor.

#syntax-highlighting #error-underlining #command-line-interface #terminal-settings #input-editor
