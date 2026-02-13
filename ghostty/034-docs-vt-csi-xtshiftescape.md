---
title: Shift-Escape Behavior (XTSHIFTESCAPE) - CSI
url: https://ghostty.org/docs/vt/csi/xtshiftescape
source: crawler
fetched_at: 2026-02-11T01:43:36.903409-03:00
rendered_js: true
word_count: 313
summary: This document explains the XTSHIFTESCAPE control sequence, which configures whether a terminal emulator passes the shift modifier to running programs during mouse reporting or reserves it for native text selection.
tags:
    - terminal-emulator
    - mouse-reporting
    - shift-modifier
    - csi-sequence
    - xtshiftescape
    - text-selection
category: reference
---

Configure whether mouse reports are allowed to capture the \`shift\` modifier.

1. 0x1B
   
   ESC
2. 0x5B
   
   [
3. 0x3E
   
   &gt;
4. \_\_\__
   
   n
5. 0x73
   
   s

The parameter `n` must be an integer equal to 0 or 1. If `n` is omitted, `n` defaults to 0. If `n` is an invalid value, this sequence does nothing.

When a terminal program requests [mouse reporting](#TODO), some mouse reporting modes also report the modifier keys that are pressed (control, shift, etc.). This would disable the ability for a terminal user to natively select text if they typically select text using left-click and drag, since the left-click event is captured by the running program.

To get around this limitation, many terminal emulators (including xterm) use the `shift` modifier to disable mouse reporting temporarily, allowing native text selection to work. In this scenario, however, the running terminal program cannot detect shift-clicks because the terminal emulator captures the event.

This sequence (`XTSHIFTESCAPE`) allows configuring this behavior. If `n` is `0`, the terminal is allowed to override the shift key and not pass it through to the terminal program. If `n` is `1`, the terminal program is requesting that the shift modifier is sent using standard mouse reporting formats.

In either case, the terminal emulator is not forced to respect this request. For example, `xterm` has a `never` and `always` terminal configuration to never allow terminal programs to capture shift or to always allow them, respectively. If either of these configurations are set, `XTSHIFTESCAPE` has zero effect.

`xterm` also has `false` and `true` terminal configurations. In the `false` scenario, the terminal emulator will override `shift` (not allow the terminal program to see it) *unless it is explicitly requested* via `XTSHIFTESCAPE`. The `true` scenario is the exact opposite: pass the shift modifier through to the running terminal program unless the terminal program explicitly states it doesn't need to know about it (`n = 0`).

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/csi/xtshiftescape.mdx)