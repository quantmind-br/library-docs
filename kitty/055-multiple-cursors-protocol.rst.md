---
title: The multiple cursors protocol
title: The multiple cursors protocol
word_count: 461
summary: Terminal escape code protocol for displaying and managing multiple cursors at specific screen locations with custom shapes and colors.
category: reference
optimized: true
optimized_at: 2026-05-04T20:46:03Z
---
# The multiple cursors protocol

Allows terminal programs to display multiple cursors at specific screen locations. Replaces Unicode glyph hacks with terminal-native cursors supporting smooth animation, auto color adjustment, etc.

## Quickstart

```sh
# Show cursors at y=4, x=5 (same shape as main cursor)
printf "\e[>29;2:4:5 q"
# Various shapes on row 7
printf "\e[>1;2:7:1 q\e[>2;2:7:3 q\e[>3;2:7:5;2:7:7 q"
```

## Escape code structure

```
CSI > SHAPE;CO-ORD TYPE : CO-ORDINATES ; CO-ORD TYPE : CO-ORDINATES ... TRAILER
```

`CSI` = ESC (`0x1b`) + `[` (`0x5b`). `TRAILER` = SPACE (`0x20`) + `q` (`0x71`).

### SHAPE values

| Value | Meaning |
|-------|---------|
| `0` | No cursor |
| `1` | Block cursor |
| `2` | Beam cursor |
| `3` | Underline cursor |
| `29` | Follow main cursor shape |
| `30` | Change text color under extra cursors |
| `40` | Change cursor color |
| `100` | Query currently set cursors |

### Coordinate types

| Type | Format | Description |
|------|--------|-------------|
| `0` | No coords | Refers to main cursor position |
| `2` | `y:x` pairs | Cell positions, origin (1,1) top-left. Any number of pairs. |
| `4` | `top:left:bottom:right` | Rectangle. Sets shape on every cell in range. Empty = full screen. |

> [!warning]
> Terminals must ignore out-of-screen cells. For type 2, odd coordinates ignore last one. For type 4, non-multiple-of-4 coordinates ignore trailing 1-3 values.

Example: `-1;2:3:4;4:5:6:7:8` sets shape `-1` at cell `(3,2)` and rectangle `(6,5)` to `(8,7)`.

## Querying support

Send:
```
CSI > q
```

Supported terminal responds with:
```
CSI > 1;2;3;29;30;40;100;101 q
```

> [!tip]
> Send query immediately followed by primary device attributes request. If DA response arrives without query response, protocol unsupported.

Terminals must respond in FIFO order for multiplexer compatibility.

## Clearing multi-cursors

Set cursor shape to `0` at a cell. Clear all with rectangle across screen:

```
CSI > 0;4 q
```

## Changing cursor colors

All extra cursors share one color pair (cursor + text color).

```
CSI > WHICH ; COLOR_SPACE : COLOR_PARAMETER1 : COLOR_PARAMETER2 : ... q
```

| WHICH | Meaning |
|-------|---------|
| `30` | Set text color under cursor |
| `40` | Set cursor color |

### COLOR_SPACE values

| Value | Meaning | Parameters |
|-------|---------|------------|
| `0` | Same as main cursor | None |
| `1` | Special (reverse video) | None |
| `2` | sRGB | `r,g,b` (0-255 each) |
| `5` | Indexed color | Index 0-255 |

> [!note]
> `40` with special = block cursor uses reverse video. `30` with special = foreground becomes background (partial reverse).

## Querying current state

### Cursors

```
CSI > 100 q
```

Response:
```
CSI > 100; SHAPE:CO-ORD TYPE:CO-ORDINATES ; ... q
```

Empty response if no cursors active.

### Colors

```
CSI > 101 q
```

Response:
```
CSI > 101 ; 30 : COLOR_SPACE : COLOR_PARAMS ; 40 : COLOR_SPACE : COLOR_PARAMS q
```

## Interaction with terminal state

| Event | Effect on cursors |
|-------|-------------------|
| Main cursor | Extra cursors share color, opacity, blink state |
| Clear screen (ED 2/3/22) | Removes all extra cursors |
| Reset | Removes all extra cursors |
| Alternate screen switch | Removes all extra cursors |
| Scroll (IND/RI) | Extra cursors stay fixed position — apps manage positions if needed |

#terminal-emulation #escape-codes #multi-cursor-protocol
