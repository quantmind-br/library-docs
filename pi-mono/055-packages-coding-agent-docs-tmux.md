---
title: tmux Setup
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/tmux.md
source: git
fetched_at: 2026-05-03T09:31:28.524591973-03:00
rendered_js: false
word_count: 192
summary: Enabling extended key support in tmux for proper modified key detection (Shift+Enter, Ctrl+Enter).
tags:
    - tmux
    - terminal-configuration
    - key-bindings
    - extended-keys
    - csi-u
category: configuration
optimized: true
optimized_at: 2026-05-03T12:00:00Z
---
Pi works inside tmux, but tmux strips modifier information from certain keys by default.

## Recommended Configuration

Add to `~/.tmux.conf`:

```tmux
set -g extended-keys on
set -g extended-keys-format csi-u
```

Restart tmux:

```bash
tmux kill-server
tmux
```

Pi requests extended key reporting automatically when Kitty keyboard protocol is unavailable. With `extended-keys-format csi-u`, tmux forwards modified keys in CSI-u format.

## Why `csi-u`

With only `set -g extended-keys on`, tmux uses `extended-keys-format xterm` (modifyOtherKeys format):

| Key | Sequence |
|-----|----------|
| `Ctrl+C` | `\x1b[27;5;99~` |
| `Ctrl+D` | `\x1b[27;5;100~` |
| `Ctrl+Enter` | `\x1b[27;5;13~` |

With `extended-keys-format csi-u`:

| Key | Sequence |
|-----|----------|
| `Ctrl+C` | `\x1b[99;5u` |
| `Ctrl+D` | `\x1b[100;5u` |
| `Ctrl+Enter` | `\x1b[13;5u` |

Pi supports both formats, but `csi-u` is recommended.

## What This Fixes

Without extended keys, modified Enter keys collapse to legacy sequences:

| Key | Without extkeys | With `csi-u` |
|-----|-----------------|--------------|
| Enter | `\r` | `\r` |
| Shift+Enter | `\r` | `\x1b[13;2u` |
| Ctrl+Enter | `\r` | `\x1b[13;5u` |
| Alt/Option+Enter | `\x1b\r` | `\x1b[13;3u` |

## Requirements

- tmux 3.2 or later (`tmux -V` to check)
- Terminal emulator supporting extended keys (Ghostty, Kitty, iTerm2, WezTerm, Windows Terminal)

#tmux #terminal-configuration #key-bindings #extended-keys #csi-u
