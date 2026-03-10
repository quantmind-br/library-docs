---
title: Vertical Position Relative (VPR) - CSI
url: https://ghostty.org/docs/vt/csi/vpr
source: crawler
fetched_at: 2026-03-10T06:35:36.484556-03:00
rendered_js: true
word_count: 134
summary: This document describes the VT sequence VPR, which moves the cursor vertically by a specified relative amount based on the current row position.
tags:
    - vt-sequence
    - cursor-movement
    - vpr
    - terminal-control
    - escape-codes
category: reference
---

Move the cursor to a specific row relative to the current position.

1. 0x1B
   
   ESC
2. 0x5B
   
   [
3. \_\_\__
   
   y
4. 0x65
   
   e

This sequence performs [cursor position (CUP)](https://ghostty.org/docs/vt/csi/cup) with `y` set to the current cursor row plus `y` and `x` set to the current cursor column. There is no additional or different behavior for using `VPR`.

The parameter `y` must be an integer greater than or equal to 1. If `y` is less than or equal to 0, adjust `y` to be 1. If `y` is omitted, `y` defaults to 1.

Because this invokes `CUP`, the cursor column (`x`) can change if it is outside the bounds of the `CUP` operation. For example, if [origin mode](#TODO) is set and the current cursor position is outside of the scroll region, the column will be adjusted.

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/csi/vpr.mdx)