---
title: Broadcast
url: https://github.com/kovidgoyal/kitty/blob/master/docs/kittens/broadcast.rst
source: git
fetched_at: 2026-05-04T15:57:49.42567045-03:00
rendered_js: false
word_count: 97
summary: Send keystrokes to all kitty windows simultaneously using the broadcast kitten.
tags:
    - kitty-terminal
    - keyboard-shortcuts
    - automation
    - window-management
optimized: true
optimized_at: 2026-05-04T18:00:00Z
---
# broadcast

*Type text in all kitty windows simultaneously*

Send keystrokes to multiple kitty windows at once.

## Setup

Add to `~/.config/kitty/kitty.conf`:

```
map f1 launch --allow-remote-control kitty +kitten broadcast
```

Press `F1`; text typed in the new window goes to all kitty windows.

## Options

| Option | Description |
|--------|-------------|
| `--match-tab state:focused` | Broadcast only to other windows in the current tab |
| `--match-env VAR=value` | Broadcast only to windows with matching environment variable |
| `--match-cmd cmdname` | Broadcast only to windows running `cmdname` |
| `--target` | Which windows to target (all, others, os-window, tab, window) |

#kitty-terminal #automation #window-management
