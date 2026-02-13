---
title: Colors - Concepts
url: https://ghostty.org/docs/vt/concepts/colors#special-colors
source: crawler
fetched_at: 2026-02-11T01:43:45.567951-03:00
rendered_js: true
word_count: 408
summary: This document explains how Ghostty handles terminal colors, including the 256-color palette, special and dynamic colors, and various color specification formats. It details the OSC sequences used for color manipulation and the supported syntax for RGB and named colors.
tags:
    - terminal-emulation
    - ghostty
    - color-schemes
    - rgb-specification
    - osc-codes
    - terminal-colors
category: concept
---

All sorts of information regarding colors in terminal emulation.

Ghostty emulates a full 256-color palette, as well as 5 **special colors** and 3 **dynamic colors**.

The special colors, when specified, are used to color cells with particular styles — bold, underline, blink, reversed and italic. They can be queried or changed either with [OSC 4](https://ghostty.org/docs/vt/osc/4-5) using indices from 256 to 260 inclusive, or [OSC 5](https://ghostty.org/docs/vt/osc/4-5) with indices from 0 to 4 inclusive respectively. The ordinary palette colors are used instead of special colors when not specified.

The dynamic colors are used by the terminal to color cells independent of their own styles, when they are selected, highlighted, etc. They are also supposed to be *dynamically updated* by programs after the terminal has been initialized, hence their name. Ghostty currently supports three of these colors: the foreground color, the background color and the cursor color, which are queried or modified with [OSCs 10 to 12](https://ghostty.org/docs/vt/osc/1x) respectively.

Each color in the terminal is specified with a **color specification**. These originated from xterm, which allows any string that can be parsed by X11's standard [`XParseColor`](https://linux.die.net/man/3/xparsecolor) function to serve as a color. However, since Ghostty supports platforms other than X11, we have our own color parser that is compatible but not guaranteed to be the same as xterm, which is documented below.

1. 0x72 0x67 0x62 0x3A
   
   rgb:
2. \_\_\__
   
   r
3. 0x2F
   
   /
4. \_\_\__
   
   g
5. 0x2F
   
   /
6. \_\_\__
   
   b

<!--THE END-->

1. 0x23
   
   \#
2. \_\_\__
   
   r
3. \_\_\__
   
   g
4. \_\_\__
   
   b

Where each of `r`, `g` and `b` can be one to four hexadecimal digits, corresponding to 4, 8, 12 or 16 bit color channels respectively.

> When using the `#` syntax, each channel **must have the same number of digits**.
> 
> Additionally, Ghostty does not yet recognize 16-bit color channels when using the `#` syntax. This is a limitation that may be resolved in the future.

Another format uses the numerical *intensity* of each channel, as follows:

1. 0x72 0x67 0x62 0x69 0x3A
   
   rgbi:
2. \_\_\__
   
   r
3. 0x2F
   
   /
4. \_\_\__
   
   g
5. 0x2F
   
   /
6. \_\_\__
   
   b

Where each of `r`, `g` and `b` is a decimal number between `0` and `1`.

Certain colors can also be specified with their names. The exact list of accepted color names are implementation-defined, but Ghostty uses the [X color name database](https://gitlab.freedesktop.org/xorg/app/rgb) as used by X11 itself. The colors are ASCII case-insensitive, meaning `red` and `RED` correspond to the same color.

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/concepts/colors.mdx)

- [Special Colors](#special-colors)
- [Dynamic Colors](#dynamic-colors)
- [Color Specifications](#color-specifications)
- [Hexadecimal RGB](#hexadecimal-rgb)
- [Intensity RGB](#intensity-rgb)
- [Named](#named)