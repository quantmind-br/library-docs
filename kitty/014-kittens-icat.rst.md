---
title: icat
url: https://github.com/kovidgoyal/kitty/blob/master/docs/kittens/icat.rst
source: git
fetched_at: 2026-05-04T15:58:00.304909758-03:00
rendered_js: false
word_count: 183
summary: Display images directly in the kitty terminal using the icat kitten, with support for ImageMagick, over SSH, and programmatic integration.
tags:
    - kitty-terminal
    - image-display
    - terminal-graphics
    - image-processing
optimized: true
optimized_at: 2026-05-04T18:00:00Z
---
# icat

*Display images in the terminal*

```bash
kitten icat image.jpeg

# Alias
alias icat="kitten icat"
icat image.png
```

Supports all image types via ImageMagick. Works over SSH. See [[049-graphics-protocol|kitty graphics protocol]].

> [!note]
> ImageMagick required for full image type support. Without it: PNG/JPG/GIF/BMP/TIFF/WEBP only.

> [!warning]
> May not work inside screen, tmux, or other multiplexers (depends on multiplexer support).

## Key Options

| Option | Description |
|--------|-------------|
| `--place WxH+x+y` | Place image at specific position/size in terminal |
| `--detect-support` | Detect terminal graphics support |
| `--print-window-size` | Print window dimensions to stdout |

## Programmatic Integration

When integrating into editors/file managers, icat communicates over the TTY device. While running, the host program must not do any TTY I/O — all input is discarded.

For non-interactive backends, use TTY-less mode:

```bash
# icat without TTY access — outputs only escape codes
zsh -c 'setsid kitten icat --stdin=no --use-window-size $COLUMNS,$LINES,3000,2000 --transfer-mode=file myimage.png'
```

Required options for TTY-less mode:
- `--use-window-size` — window dimensions
- `--place` — where to place the image
- `--transfer-mode file` — file transfer (not TTY)
- `--stdin=no` — disable TTY communication

Values `3000,2000` are pixel dimensions when TTY is unavailable. For real programs, implement the [[049-graphics-protocol|kitty graphics protocol]] directly — libraries exist for many languages.

#kitty-terminal #image-display #terminal-graphics
