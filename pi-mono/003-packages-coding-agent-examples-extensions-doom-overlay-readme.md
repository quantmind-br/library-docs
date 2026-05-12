---
title: DOOM Overlay Demo
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/examples/extensions/doom-overlay/README.md
source: git
fetched_at: 2026-05-03T09:31:38.402375244-03:00
rendered_js: false
word_count: 178
summary: Play DOOM as a terminal overlay at 35 FPS using WebAssembly and half-block character rendering.
tags:
    - terminal-overlay
    - webassembly
    - game-rendering
    - pi-extension
    - doom-port
category: tutorial
optimized: true
optimized_at: 2026-05-03T12:31:00Z
---
# DOOM Overlay Demo

Play DOOM as an overlay in pi. Demonstrates real-time game rendering at 35 FPS via WebAssembly.

## Usage

```bash
pi --extension ./examples/extensions/doom-overlay
/doom-overlay
```

The shareware WAD (~4MB) auto-downloads on first run.

## Controls

| Action | Keys |
|--------|------|
| Move | `WASD` or Arrow Keys |
| Run | `Shift + WASD` |
| Fire | `F` or `Ctrl` |
| Use/Open | `Space` |
| Weapons | `1-7` |
| Map | `Tab` |
| Menu | `Escape` |
| Pause/Quit | `Q` |

## How It Works

DOOM runs as WebAssembly compiled from [doomgeneric](https://github.com/ozkl/doomgeneric). Each frame renders using half-block characters (▀) with 24-bit color — top pixel = foreground, bottom pixel = background.

Overlay configuration:
- `width: "90%"` — 90% of terminal width
- `maxHeight: "80%"` — max 80% of terminal height  
- `anchor: "center"` — centered in terminal

Height calculates from width to maintain DOOM's 3.2:1 aspect ratio (accounting for half-block rendering).

## Credits

- [id Software](https://github.com/id-Software/DOOM) — original DOOM
- [doomgeneric](https://github.com/ozkl/doomgeneric) — portable DOOM implementation
- [pi-doom](https://github.com/badlogic/pi-doom) — original pi integration

#terminal-overlay #webassembly #game-rendering
