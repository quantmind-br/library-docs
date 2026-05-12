---
title: "ZSH Keyboard Shortcuts Reference"
url: https://forgecode.dev/docs/shortcuts/
source: sitemap
fetched_at: 2026-04-30T14:09:17.382339107-03:00
rendered_js: false
word_count: 262
summary: "Common ZSH shell keyboard shortcuts for line editing, history navigation, and terminal control."
tags:
  - zsh
  - command-line
  - keyboard-shortcuts
  - shell-navigation
  - terminal-productivity
category: reference
optimized: true
---
# ZSH Keyboard Shortcuts Reference

> **TL;DR**
> Built-in ZSH shortcuts for editing, history, and terminal control. Use `forge zsh keyboard` to print this in your terminal.

## Default Mode
- **Emacs keybindings** (use `bindkey -v` in `~/.zshrc` for Vi mode).

## Cursor Movement

| Shortcut | Action |
|----------|--------|
| `Ctrl+A` | Move to beginning of line |
| `Ctrl+E` | Move to end of line |
| `Option+F` | Move forward one word |
| `Option+B` | Move backward one word |

## Editing

| Shortcut | Action |
|----------|--------|
| `Ctrl+U` | Kill line before cursor |
| `Ctrl+K` | Kill line after cursor |
| `Ctrl+W` | Kill word before cursor |
| `Option+D` | Kill word after cursor |
| `Ctrl+Y` | Yank (paste) killed text |
| `Ctrl+_` | Undo last edit |

## History Navigation

| Shortcut | Action |
|----------|--------|
| `Ctrl+R` | Search history backward |
| `Ctrl+S` | Search history forward |
| `Ctrl+P` / `↑` | Previous command |
| `Ctrl+N` / `↓` | Next command |
| `Option+<` | First history entry |
| `Option+>` | Last history entry |

## Terminal Control

| Shortcut | Action |
|----------|--------|
| `Ctrl+L` | Clear screen |
| `Ctrl+C` | Cancel command |
| `Ctrl+Z` | Suspend command |
| `Tab` | Complete command/path |

## Troubleshooting
- **Option key not working**: Run `forge zsh doctor`.

## Advanced
- **List bindings**: `bindkey`
- **List actions**: `zle -la`
- **List keymap bindings**: `bindkey -M emacs`

## Related
- [Official ZSH Line Editor Docs](https://linux.die.net/man/1/zshzle)