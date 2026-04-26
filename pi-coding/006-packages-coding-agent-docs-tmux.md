---
title: Tmux
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/tmux.md
source: git
fetched_at: 2026-04-26T05:48:37.2368685-03:00
rendered_js: false
word_count: 258
summary: Configure tmux extended key support so modified key combinations like Shift+Enter are correctly forwarded to pi.
tags:
    - tmux
    - terminal-configuration
    - key-bindings
    - csi-u
    - extended-keys
category: configuration
optimized: true
optimized_at: 2026-04-26T09:00:00Z
---

# tmux Setup

Pi works inside tmux, but tmux strips modifier information from certain keys by default — `Shift+Enter` and `Ctrl+Enter` become indistinguishable from plain `Enter`.

## Recommended Configuration

Add to `~/.tmux.conf`:

```tmux
set -g extended-keys on
set -g extended-keys-format csi-u
```

Restart tmux fully:

```bash
tmux kill-server
tmux
```

Pi requests extended key reporting automatically when Kitty keyboard protocol is unavailable. With `csi-u`, tmux forwards modified keys in CSI-u format — the most reliable configuration.

## Why `csi-u` Is Recommended

With only `set -g extended-keys on`, tmux defaults to `extended-keys-format xterm`. Modified keys are forwarded in `modifyOtherKeys` format:

- `Ctrl+C` → `\x1b[27;5;99~`
- `Ctrl+D` → `\x1b[27;5;100~`
- `Ctrl+Enter` → `\x1b[27;5;13~`

With `extended-keys-format csi-u`, the same keys become:

- `Ctrl+C` → `\x1b[99;5u`
- `Ctrl+D` → `\x1b[100;5u`
- `Ctrl+Enter` → `\x1b[13;5u`

Pi supports both formats, but `csi-u` is recommended.

## What This Fixes

Without tmux extended keys, modified Enter keys collapse to legacy sequences:

| Key | Without extkeys | With `csi-u` |
|-----|-----------------|--------------|
| Enter | `\r` | `\r` |
| Shift+Enter | `\r` | `\x1b[13;2u` |
| Ctrl+Enter | `\r` | `\x1b[13;5u` |
| Alt/Option+Enter | `\x1b\r` | `\x1b[13;3u` |

Affects default keybindings (`Enter` submit, `Shift+Enter` newline) and any custom modified Enter bindings.

## Requirements

- tmux 3.2+ (`tmux -V`)
- Terminal emulator supporting extended keys: Ghostty, Kitty, iTerm2, WezTerm, Windows Terminal

#tmux #terminal-configuration #extended-keys
