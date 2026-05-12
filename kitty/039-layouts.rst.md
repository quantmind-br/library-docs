---
title: Arrange windows
title: Arrange windows
word_count: 307
summary: Configure and manage tiled window layouts in kitty, including Stack, Tall, Fat, Grid, Splits, Horizontal, and Vertical layouts with their options and keyboard controls.
optimized: true
optimized_at: 2026-05-04T20:45:41Z
---
# Arrange windows

kitty tiles windows in arbitrary arrangements using *Layouts*. All layouts are enabled by default; switch layouts with `next_layout` (default) or control availability via `enabled_layouts` (first listed becomes default).

## Stack Layout

Displays a single window using all available space; other windows are hidden behind it. No options.

```
enabled_layouts stack
```

## Tall Layout

Displays one or more full-height windows on the left half of the screen. Remaining windows tile vertically on the right.

**Options:**
| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `bias` | integer (10-90) | 50 | Horizontal split ratio |
| `full_size` | positive integer | 1 | Number of full-height windows |
| `mirrored` | boolean | false | Place full-height windows on right instead of left |

```
enabled_layouts tall:bias=50;full_size=1;mirrored=false

┌──────────────┬───────────────┐
│              │               │
│              │               │
│              ├───────────────┤
│              │               │
│              ├───────────────┤
│              │               │
└──────────────┴───────────────┘
```

**Suggested key mappings:**
```
map ctrl+[ layout_action decrease_num_full_size_windows
map ctrl+] layout_action increase_num_full_size_windows
map ctrl+/ layout_action mirror toggle
map ctrl+y layout_action mirror true
map ctrl+n layout_action mirror false
map ctrl+. layout_action bias 50 62 70
map ctrl+, layout_action bias 62
```

## Fat Layout

Displays one or more full-width windows on the top half of the screen. Remaining windows tile horizontally on the bottom.

**Options:** Same as Tall (`bias`, `full_size`, `mirrored`).

```
enabled_layouts fat:bias=50;full_size=1;mirrored=false

┌──────────────────────────────┐
│                              │
├─────────┬──────────┬─────────┤
│         │          │         │
│         │          │         │
└─────────┴──────────┴─────────┘
```

## Grid Layout

Displays windows in a balanced grid; all windows same size except the last column if the grid is incomplete. No options.

```
enabled_layouts grid

┌─────────┬──────────┬─────────┐
│         │          │         │
├─────────┼──────────┤         │
│         │          │         │
└─────────┴──────────┴─────────┘
```

## Splits Layout

The most flexible layout: create any arrangement by repeatedly splitting existing windows.

### Key bindings

```
# Split vertically (one above the other)
map f5 launch --location=hsplit

# Split horizontally (side by side)
map f6 launch --location=vsplit

# Auto-split (axis chosen by window aspect ratio)
map f4 launch --location=split

# Rotate split axis
map f7 layout_action rotate

# Move active window
map shift+up    move_window up
map shift+left  move_window left
map shift+right move_window right
map shift+down  move_window down

# Move to screen edge
map ctrl+shift+up    layout_action move_to_screen_edge top
map ctrl+shift+left  layout_action move_to_screen_edge left
map ctrl+shift+right layout_action move_to_screen_edge right
map ctrl+shift+down  layout_action move_to_screen_edge bottom

# Switch focus to neighboring window
map ctrl+left  neighboring_window left
map ctrl+right neighboring_window right
map ctrl+up    neighboring_window up
map ctrl+down  neighboring_window down

# Set bias (active window takes specified percent of parent size)
map ctrl+. layout_action bias 80

# Maximize along axis (press again to restore)
map ctrl+shift+right layout_action maximize horizontal
map ctrl+shift+up    layout_action maximize vertical
```

### Options

| Option | Default | Values | Description |
|--------|---------|--------|-------------|
| `split_axis` | horizontal | `horizontal`, `vertical`, `auto` | Axis for new splits when `--location` unspecified |

```
enabled_layouts splits:split_axis=horizontal

┌──────────────┬───────────────┐
│              ├───────┬───────┤
│              │       │       │
│              │       ├───────┤
│              │       │       │
└──────────────┴───────┴───────┘
```

## Horizontal Layout

All windows side by side. No options.

```
enabled_layouts horizontal
```

## Vertical Layout

All windows one below another. No options.

```
enabled_layouts vertical
```

## Resizing windows

**Mouse:** Drag window borders. `window_drag_tolerance` controls precision. Resizes layout slots, not individual windows.

**Keyboard:**
1. Press `start_resizing_window` (or Cmd+R on macOS)
2. Follow on-screen instructions

```
map ctrl+left  resize_window narrower
map ctrl+right resize_window wider
map ctrl+up    resize_window taller
map ctrl+down  resize_window shorter 3
map ctrl+home  resize_window reset
```

`resize_window` accepts an optional positive integer increment (default: 1).

> [!tip]
> A custom layout requires ~200 lines of code. See the [layout package](https://github.com/kovidgoyal/kitty/tree/master/kitty/layout) for reference.

#kitty #terminal-emulator #window-management #tiling-layouts
