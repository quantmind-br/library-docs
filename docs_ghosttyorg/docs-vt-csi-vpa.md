---
title: Vertical Position Absolute (VPA) - CSI
url: https://ghostty.org/docs/vt/csi/vpa
source: crawler
fetched_at: 2026-03-03T08:23:38.086479-03:00
rendered_js: true
word_count: 91
summary: This document explains the terminal escape sequence used to move the cursor to a specific row (line) using the Vertical Position Absolute (VPA) sequence, which maps to the Cursor Position (CUP) operation.
tags:
    - terminal
    - escape-sequence
    - cursor-movement
    - vpa
    - cup
    - ansi
category: reference
---

Move the cursor to a specific row.

1. 0x1B
   
   ESC
2. 0x5B
   
   [
3. \_\_\__
   
   y
4. 0x64
   
   d

This sequence performs [cursor position (CUP)](https://ghostty.org/docs/vt/csi/cup) with `y` set to the parameterized value and `x` set to the current cursor position. There is no additional or different behavior for using `VPA`.

Because this invokes `CUP`, the cursor column (`y`) can change if it is outside the bounds of the `CUP` operation. For example, if [origin mode](#TODO) is set and the current cursor position is outside of the scroll region, the column will be adjusted.

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/csi/vpa.mdx)