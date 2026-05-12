---
title: Alias expansion | Warp
url: https://docs.warp.dev/terminal/editor/alias-expansion
source: sitemap
fetched_at: 2026-04-29T15:02:21.036351563-03:00
rendered_js: false
word_count: 110
summary: This document explains how to enable, disable, and use the alias expansion feature within the terminal input editor.
tags:
    - alias-expansion
    - terminal-settings
    - keyboard-shortcuts
    - command-palette
    - input-editor
category: guide
optimized: true
optimized_at: 2026-04-29T19:02:00Z
---
Alias expansion automatically expands shell aliases as you type.

## How to use it

Type an alias and press `SPACE` to expand it. Press `OPT-SPACE` to insert a space without expanding.

> [!note]
> Aliases will not be expanded when the command in the expanded form is the same as the alias itself (e.g., `ls='ls -G'` → `ls` will not be expanded).

## How to access it

Alias expansion is disabled by default. Toggle via:

- **Settings** → **Features** → **Terminal Input** → "Expand aliases as you type"
- [Command Palette](https://docs.warp.dev/terminal/command-palette#windows): search "Enable/disable alias expansion"

## How it works

See [[103-terminal-editor-command-inspector]] for related editor features.

#alias-expansion #terminal-settings #keyboard-shortcuts #command-palette #input-editor
