---
title: ForgeCode
url: https://forgecode.dev/docs/shortcuts/
source: sitemap
fetched_at: 2026-03-29T14:52:22.449903316-03:00
rendered_js: false
word_count: 186
summary: This document provides a reference guide for ZSH keyboard shortcuts and line editing commands, including movement, deletion, history, and utility shortcuts available in any ZSH session.
tags:
    - zsh
    - keyboard-shortcuts
    - line-editor
    - command-line
    - terminal
    - emac keybindings
    - history-search
category: reference
---

These shortcuts are built into ZSH — ForgeCode doesn't add or modify them. They work in any ZSH session, not just when using ForgeCode.

ZSH uses **Emacs keybindings by default**. If you prefer Vi mode, add `bindkey -v` to your `~/.zshrc`.

Run `forge zsh keyboard` at any time to print this reference in your terminal. For the full reference, see the [official ZSH Line Editor documentation](https://linux.die.net/man/1/zshzle).

ShortcutAction`Ctrl+A`Move to beginning of line`Ctrl+E`Move to end of line`Option+F`Move forward one word`Option+B`Move backward one word

ShortcutAction`Ctrl+U`Kill line before cursor`Ctrl+K`Kill line after cursor`Ctrl+W`Kill word before cursor`Option+D`Kill word after cursor`Ctrl+Y`Yank (paste) killed text`Ctrl+_`Undo last edit

## History[​](#history "Direct link to History")

ShortcutAction`Ctrl+R`Search command history backward`Ctrl+S`Search command history forward`Ctrl+P` / `↑`Previous command`Ctrl+N` / `↓`Next command`Option+<`Move to first history entry`Option+>`Move to last history entry

ShortcutAction`Ctrl+L`Clear screen`Ctrl+C`Cancel current command`Ctrl+Z`Suspend current command`Tab`Complete command/path

If `Option` key shortcuts aren't working, run `forge zsh doctor` — the most common cause is a terminal that isn't passing the Option key through correctly.

ZSH exposes the full set of bindings and editor actions directly from the shell.

List all current key bindings:

List all available editor actions:

List bindings for a specific keymap (e.g. Emacs):