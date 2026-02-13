---
title: Insert Character (ICH) - CSI
url: https://ghostty.org/docs/vt/csi/ich
source: crawler
fetched_at: 2026-02-11T01:43:35.133654-03:00
rendered_js: true
word_count: 260
summary: This document defines the ICH (Insert Character) terminal escape sequence, explaining how to insert blank spaces at the cursor while shifting existing content and handling margins.
tags:
    - vt-sequences
    - terminal-emulation
    - escape-codes
    - cursor-management
    - ich-sequence
    - text-rendering
category: reference
---

Insert blank characters at the current cursor position.

1. 0x1B
   
   ESC
2. 0x5B
   
   [
3. \_\_\__
   
   n
4. 0x40
   
   @

Insert `n` blank characters at the current cursor position and shift existing cell contents right.

The parameter `n` must be an integer greater than or equal to 1. If `n` is less than or equal to 0, adjust `n` to be 1. If `n` is omitted, `n` defaults to 1.

This sequence always unsets the pending wrap state.

If the cursor position is outside of the [left and right margins](#TODO), this sequence does not change the screen, but the pending wrap state is still reset.

Existing cells shifted beyond the right margin are deleted. Inserted cells are blank with the background color colored according to the current SGR state.

If a multi-cell character (such as "橋") is shifted so that the cell is split in half, the multi-cell character can either be clipped or erased. Typical behavior is to clip at the right edge of the screen and erase at a right margin, but either behavior is acceptable.

```
printf "ABC"
printf "\033[1G"
printf "\033[2@"
printf "X"
```

```
|XcABC_____|
```

```
printf "ABC"
printf "\033[1G"
printf "\033[41m"
printf "\033[2@"
printf "X"
```

```
|c_ABC_____|
```

The `c_` cells should both have a red background. The `ABC` cells should remain unchanged in style.

```
cols=$(tput cols)
printf "\033[${cols}G"
printf "\033[2D"
printf "ABC"
printf "\033[2D"
printf "\033[2@"
printf "X"
```

```
|_______XcA|
```

```
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "\033[?69h" # enable left/right margins
printf "\033[3;5s" # scroll region left/right
printf "\033[3G"
printf "ABC"
printf "\033[3G"
printf "\033[2@"
printf "X"
```

```
|__XcA_____|
```

```
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "\033[?69h" # enable left/right margins
printf "\033[3;5s" # scroll region left/right
printf "\033[3G"
printf "ABC"
printf "\033[1G"
printf "\033[2@"
printf "X"
```

```
|XcABC_____|
```

```
cols=$(tput cols)
printf "\033[${cols}G"
printf "\033[1D"
printf "橋"
printf "\033[2D"
printf "\033[@"
printf "X"
```

```
|_______Xc_|
```

In this case, it is valid for the last cell to be blank or to clip the multi-cell character. xterm clips the character but many other terminals erase the cell.

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/csi/ich.mdx)

- [Validation](#validation)
- [ICH V-1: No Scroll Region, Fits on Screen](#ich-v-1:-no-scroll-region-fits-on-screen)
- [ICH V-2: SGR State](#ich-v-2:-sgr-state)
- [ICH V-3: Shifting Content Off the Screen](#ich-v-3:-shifting-content-off-the-screen)
- [ICH V-4: Inside Left/Right Scroll Region](#ich-v-4:-inside-leftright-scroll-region)
- [ICH V-5: Outside Left/Right Scroll Region](#ich-v-5:-outside-leftright-scroll-region)
- [ICH V-6: Split Wide Character](#ich-v-6:-split-wide-character)