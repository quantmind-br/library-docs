---
title: Terminal setup
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/terminal-setup.md
source: git
fetched_at: 2026-04-26T05:48:31.297881912-03:00
rendered_js: false
word_count: 436
summary: This document provides instructions for configuring various terminal emulators to support the Kitty keyboard protocol and specific keybindings required for the Pi tool.
tags:
    - terminal-configuration
    - keyboard-protocol
    - keybindings
    - environment-setup
    - pi-tool
category: configuration
optimized: true
optimized_at: 2026-04-26T09:00:00Z
---

# Terminal Setup

Pi uses the [Kitty keyboard protocol](https://sw.kovidgoyal.net/kitty/keyboard-protocol/) for reliable modifier key detection. Most modern terminals support it; some require configuration.

## Kitty, iTerm2

Work out of the box.

## Ghostty

Config locations: `~/Library/Application Support/com.mitchellh.ghostty/config` (macOS), `~/.config/ghostty/config` (Linux).

Add:

```
keybind = alt+backspace=text:\x1b\x7f
```

Older Claude Code versions may have added:

```
keybind = shift+enter=text:\n
```

That sends a raw linefeed byte, indistinguishable from `Ctrl+J` inside pi, so tmux and pi lose the real `shift+enter` event. If Claude Code 2.x+ was the only reason for that mapping, remove it — unless you use Claude Code in tmux, where it still needs the remap.

> [!tip] To keep `Shift+Enter` working in tmux via the remap, add `ctrl+j` to pi's `newLine` keybinding in `~/.pi/agent/keybindings.json`:

```json
{
  "newLine": ["shift+enter", "ctrl+j"]
}
```

## WezTerm

Create `~/.wezterm.lua`:

```lua
local wezterm = require 'wezterm'
local config = wezterm.config_builder()
config.enable_kitty_keyboard = true
return config
```

## VS Code (Integrated Terminal)

`keybindings.json` locations:

| Platform | Path |
|----------|------|
| macOS | `~/Library/Application Support/Code/User/keybindings.json` |
| Linux | `~/.config/Code/User/keybindings.json` |
| Windows | `%APPDATA%\Code\User\keybindings.json` |

Add to enable `Shift+Enter` for multi-line input:

```json
{
  "key": "shift+enter",
  "command": "workbench.action.terminal.sendSequence",
  "args": { "text": "[13;2u" },
  "when": "terminalFocus"
}
```

## Windows Terminal

Add to `settings.json` (Ctrl+Shift+, or Settings > Open JSON file):

```json
{
  "actions": [
    {
      "command": { "action": "sendInput", "input": "[13;2u" },
      "keys": "shift+enter"
    },
    {
      "command": { "action": "sendInput", "input": "[13;3u" },
      "keys": "alt+enter"
    }
  ]
}
```

- `Shift+Enter` inserts a new line.
- Windows Terminal binds `Alt+Enter` to fullscreen by default, preventing pi from receiving it for follow-up queueing. The remap forwards the real key chord.
- Merge into an existing `actions` array. If old fullscreen behavior persists, fully close and reopen Windows Terminal.

## xfce4-terminal, terminator

Limited escape sequence support — `Ctrl+Enter` and `Shift+Enter` are indistinguishable from plain `Enter`, preventing custom keybindings like `submit: ["ctrl+enter"]`.

Recommended terminals with Kitty keyboard protocol support:

- [Kitty](https://sw.kovidgoyal.net/kitty/)
- [Ghostty](https://ghostty.org/)
- [WezTerm](https://wezfurlong.org/wezterm/)
- [iTerm2](https://iterm2.com/)
- [Alacritty](https://github.com/alacritty/alacritty) (requires compilation with Kitty protocol support)

## IntelliJ IDEA (Integrated Terminal)

Limited escape sequence support — `Shift+Enter` is indistinguishable from `Enter`.

> [!info] For hardware cursor visibility, set `PI_HARDWARE_CURSOR=1` (disabled by default for compatibility).

A dedicated terminal emulator provides the best experience.

#terminal-configuration #keyboard-protocol #keybindings
