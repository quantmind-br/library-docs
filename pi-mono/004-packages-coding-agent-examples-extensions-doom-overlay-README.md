---
title: README
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/examples/extensions/doom-overlay/README.md
source: git
fetched_at: 2026-03-03T03:42:04.614355-03:00
rendered_js: false
word_count: 204
summary: Basic documentation for software project setup, dependencies, installation instructions, and contribution guidelines.
tags:
    - setup
    - instructions
    - guide
    - open-source
category: guide
---

# DOOM Overlay Demo

Play DOOM as an overlay in pi. Demonstrates that the overlay system can handle real-time game rendering at 35 FPS.

## Usage

```bash
pi --extension ./examples/extensions/doom-overlay
```

Then run:
```
/doom-overlay
```

The shareware WAD file (~4MB) is auto-downloaded on first run.

## Controls

| Action | Keys |
|--------|------|
| Move | WASD or Arrow Keys |
| Run | Shift + WASD |
| Fire | F or Ctrl |
| Use/Open | Space |
| Weapons | 1-7 |
| Map | Tab |
| Menu | Escape |
| Pause/Quit | Q |

## How It Works

DOOM runs as WebAssembly compiled from [doomgeneric](https://github.com/ozkl/doomgeneric). Each frame is rendered using half-block characters (▀) with 24-bit color, where the top pixel is the foreground color and the bottom pixel is the background color.

The overlay uses:
- `width: "90%"` - 90% of terminal width
- `maxHeight: "80%"` - Maximum 80% of terminal height
- `anchor: "center"` - Centered in terminal

Height is calculated from width to maintain DOOM's 3.2:1 aspect ratio (accounting for half-block rendering).

## Credits

- [id Software](https://github.com/id-Software/DOOM) for the original DOOM
- [doomgeneric](https://github.com/ozkl/doomgeneric) for the portable DOOM implementation
- [pi-doom](https://github.com/badlogic/pi-doom) for the original pi integration
