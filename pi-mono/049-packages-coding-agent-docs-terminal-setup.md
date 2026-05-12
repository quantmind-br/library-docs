---
title: Terminal Setup
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/terminal-setup.md
source: git
fetched_at: 2026-05-03T09:31:25.281967406-03:00
rendered_js: false
word_count: 191
summary: Configuration for terminal emulators to support Pi's keyboard protocol and custom keybindings.
tags:
    - terminal-setup
    - keyboard-protocol
    - pi-agent
    - keybindings
    - emulator-configuration
category: configuration
optimized: true
optimized_at: 2026-05-03T12:00:00Z
---
Pi uses the [Kitty keyboard protocol](https://sw.kovidgoyal.net/kitty/keyboard-protocol/) for reliable modifier key detection.

## Supported Out of the Box

- Kitty
- iTerm2

## Ghostty

Add to `~/.config/ghostty/config` (Linux) or `~/Library/Application Support/com.mitchellh.ghostty/config` (macOS):

```ini
keybind = alt+backspace=text:\x1b\x7f
```

Older Claude Code versions may have added this mapping (sends raw linefeed for Shift+Enter):

```ini
keybind = shift+enter=text:\n
```

If using Claude Code 2.x+ only, this mapping can be removed unless you also use tmux (where it's still required).

For tmux compatibility, add `ctrl+j` to pi's `newLine` keybinding in `~/.pi/agent/keybindings.json`:

```json
{
  "newLine": ["shift+enter", "ctrl+j"]
}
```

## WezTerm

```lua
local wezterm = require 'wezterm'
local config = wezterm.config_builder()
config.enable_kitty_keyboard = true
return config
```

## VS Code Integrated Terminal

Add to `keybindings.json` (`~/Library/Application Support/Code/User/keybindings.json` on macOS, `~/.config/Code/User/keybindings.json` on Linux):

```json
{
  "key": "shift+enter",
  "command": "workbench.action.terminal.sendSequence",
  "args": { "text": "\u001b[13;2u" },
  "when": "terminalFocus"
}
```

## Windows Terminal

Add to `settings.json` (Ctrl+Shift+,):

```json
{
  "actions": [
    {
      "command": { "action": "sendInput", "input": "\u001b[13;2u" },
      "keys": "shift+enter"
    },
    {
      "command": { "action": "sendInput", "input": "\u001b[13;3u" },
      "keys": "alt+enter"
    }
  ]
}
```

- `Shift+Enter` inserts a new line
- `Alt+Enter` is remapped from fullscreen to forward the key chord to pi

If old fullscreen behavior persists, fully close and reopen Windows Terminal.

## Unsupported Terminals

These terminals lack proper escape sequence support for modified Enter keys:

- xfce4-terminal
- terminator
- IntelliJ IDEA integrated terminal

For best experience, use a Kitty keyboard protocol-supported terminal:
- [Kitty](https://sw.kovidgoyal.net/kitty/)
- [Ghostty](https://ghostty.org/)
- [WezTerm](https://wezfurlong.org/wezterm/)
- [iTerm2](https://iterm2.com/)
- [Alacritty](https://github.com/alacritty/alacritty) (requires Kitty protocol compilation)

For IntelliJ hardware cursor visibility, set `PI_HARDWARE_CURSOR=1` before running pi.

#terminal-setup #keyboard-protocol #pi-agent #keybindings #emulator-configuration
