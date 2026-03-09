---
title: Terminal setup
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/terminal-setup.md
source: git
fetched_at: 2026-03-03T03:41:04.813304-03:00
rendered_js: false
word_count: 201
summary: Instructional guide for setting up a terminal environment, covering configurations, tool installations, and optimizations for seamless computing experience.
tags:
    - development
    - tech
    - linux
    - command_line
    - terminal
category: guide
---

# Terminal Setup

Pi uses the [Kitty keyboard protocol](https://sw.kovidgoyal.net/kitty/keyboard-protocol/) for reliable modifier key detection. Most modern terminals support this protocol, but some require configuration.

## Kitty, iTerm2

Work out of the box.

## Ghostty

Add to your Ghostty config (`~/.config/ghostty/config`):

```
keybind = alt+backspace=text:\x1b\x7f
keybind = shift+enter=text:\n
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
- macOS: `~/Library/Application Support/Code/User/keybindings.json`
- Linux: `~/.config/Code/User/keybindings.json`
- Windows: `%APPDATA%\\Code\\User\\keybindings.json`

Add to `keybindings.json` to enable `Shift+Enter` for multi-line input:

```json
{
  "key": "shift+enter",
  "command": "workbench.action.terminal.sendSequence",
  "args": { "text": "\u001b[13;2u" },
  "when": "terminalFocus"
}
```

## Windows Terminal

Add to `settings.json` (Ctrl+Shift+, or Settings → Open JSON file):

```json
{
  "actions": [
    {
      "command": { "action": "sendInput", "input": "\u001b[13;2u" },
      "keys": "shift+enter"
    }
  ]
}
```

If you already have an `actions` array, add the object to it.

## IntelliJ IDEA (Integrated Terminal)

The built-in terminal has limited escape sequence support. Shift+Enter cannot be distinguished from Enter in IntelliJ's terminal.

If you want the hardware cursor visible, set `PI_HARDWARE_CURSOR=1` before running pi (disabled by default for compatibility).

Consider using a dedicated terminal emulator for the best experience.
