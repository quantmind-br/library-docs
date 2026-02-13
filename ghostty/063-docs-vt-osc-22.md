---
title: Change Pointer Shape (OSC 22) - OSC
url: https://ghostty.org/docs/vt/osc/22
source: crawler
fetched_at: 2026-02-11T01:43:39.606375-03:00
rendered_js: true
word_count: 163
summary: This document explains how to change the mouse pointer shape using the OSC 22 escape sequence, detailing Ghostty's use of CSS cursor standards and compatibility with other terminal emulators.
tags:
    - osc-22
    - cursor-shape
    - terminal-emulator
    - mouse-pointer
    - escape-sequences
    - ghostty
category: reference
---

Change the pointer shape.

1. 0x1B
   
   ESC
2. 0x5D
   
   ]
3. 0x32 0x32
   
   22
4. 0x3B
   
   ;
5. \_\_\__
   
   t
6. 0x1B
   
   ESC
7. 0x5C
   
   \\

Change the pointer shape to `t`.

Unfortunately, there is no consensus on what values `t` is allowed to have. Even xterm, the origin of this OSC, remarks that when one uses a custom cursor theme, "expect it to provide about a third of those names, while adding others."[1](#user-content-fn-xterm)

Ghostty, like some other terminals like [Kitty](https://sw.kovidgoyal.net/kitty/pointer-shapes/) and Foot, uses CSS's list of standardized cursor shapes, used in the [`cursor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cursor#keyword) property. This is by no means perfect, but it at least is an international standard that is unambiguous and platform-independent.

**Avoid** using this sequence unless your program only targets certain terminal emulators, or you can switch between cursor names by detecting the current terminal.

GhosttyKittyVTEAlacrittyFootiTerm2xtermOSC 221.0.00.31.0NoNo1.12.03.5.0367Cursor stylesCSSCSS--CSS + X11 subset[2](#user-content-fn-foot)[Custom X11 subset](https://github.com/gnachman/iTerm2/blob/v3.6.6/sources/PTYSession.m#L15324-L15342)X11

1. [https://invisible-island.net/xterm/manpage/xterm.html#VT100-Widget-Resources:pointerShape](https://invisible-island.net/xterm/manpage/xterm.html#VT100-Widget-Resources:pointerShape) [↩](#user-content-fnref-xterm)
2. Foot maps [both CSS and X11 names](https://codeberg.org/dnkl/foot/src/tag/1.25.0/cursor-shape.c#L62-L102) to [`wp_cursor_shape_device_v1::shape`](https://wayland.app/protocols/cursor-shape-v1#wp_cursor_shape_device_v1:enum:shape) enums, which are also based on the CSS standard. [↩](#user-content-fnref-foot)

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/osc/22.mdx)