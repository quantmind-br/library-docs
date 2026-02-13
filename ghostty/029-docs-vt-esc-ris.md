---
title: Reset to Initial State (RIS) - ESC
url: https://ghostty.org/docs/vt/esc/ris
source: crawler
fetched_at: 2026-02-11T01:43:23.882755-03:00
rendered_js: true
word_count: 137
summary: This document explains the Full Reset (RIS) escape sequence, detailing how it restores a terminal emulator to its initial state by resetting all modes, colors, and configurations.
tags:
    - terminal-emulation
    - escape-sequence
    - ris
    - terminal-reset
    - vt-commands
    - ghostty
category: reference
---

## Full Reset (RIS)

Reset the terminal to its initial state.

1. 0x1B
   
   ESC
2. 0x63
   
   c

The full reset operation does the following:

- Set the cursor shape to the default
- Reset the scroll region to the full screen
- Disable [left and right margin mode (mode 69)](#TODO)
- Disable [origin mode (mode 6)](#TODO)
- Unset cursor foreground and background colors
- Reset charsets to the default
- Reset [cursor key mode (DECCKM)](#TODO)
- Reset [disable keyboard input (KAM)](#TODO)
- Reset [application keypad mode](https://ghostty.org/docs/vt/esc/deckpnm)
- Reset xterm keyboard modifier state to the default
- Disable cursor [protected attribute](#TODO)
- Disable any [protected area](#TODO)
- Reset all [mouse tracking modes](#TODO)
- Reset tabstops to default
- Enable [send-receive mode (mode 12)](#TODO)
- Reset [backspace sends delete (mode 67)](#TODO)
- Return to the primary screen and clear it
- Move the cursor to the top-left corner
- Reset the pending wrap state
- Reset saved cursor state

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/esc/ris.mdx)