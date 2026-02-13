---
title: Horizontal Position Absolute (HPA) - CSI
url: https://ghostty.org/docs/vt/csi/hpa
source: crawler
fetched_at: 2026-02-11T01:43:35.845962-03:00
rendered_js: true
word_count: 91
summary: This document explains the HPA (Horizontal Position Absolute) control sequence used to move the terminal cursor to a specific column while maintaining the current row position.
tags:
    - terminal-emulation
    - control-sequences
    - cursor-movement
    - csi
    - ansi-escape-codes
category: reference
---

Move the cursor to a specific column.

1. 0x1B
   
   ESC
2. 0x5B
   
   [
3. \_\_\__
   
   x
4. 0x60
   
   \`

This sequence performs [cursor position (CUP)](https://ghostty.org/docs/vt/csi/cup) with `x` set to the parameterized value and `y` set to the current cursor position. There is no additional or different behavior for using `HPA`.

Because this invokes `CUP`, the cursor row (`x`) can change if it is outside the bounds of the `CUP` operation. For example, if [origin mode](#TODO) is set and the current cursor position is outside of the scroll region, the row will be adjusted.

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/csi/hpa.mdx)