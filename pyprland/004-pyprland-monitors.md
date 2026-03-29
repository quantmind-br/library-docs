---
title: monitors | Pyprland web
url: https://hyprland-community.github.io/pyprland/monitors
source: github_pages
fetched_at: 2026-01-31T16:03:25.402707659-03:00
rendered_js: false
word_count: 1059
summary: Provides configuration guidelines for relative monitor placement in Hyprland, allowing users to define monitor positions based on descriptions or ports with various alignment options.
tags:
    - monitor-placement
    - hyprland
    - display-configuration
    - relative-positioning
    - multi-monitor-setup
category: guide
---

Allows relative placement of monitors depending on the model ("description" returned by `hyprctl monitors`). Useful if you have multiple monitors connected to a video signal switch or using a laptop and plugging monitors having different relative positions.

TIP

This plugin also supports Niri. It will automatically detect the environment and use `nirictl` to apply the layout. Note that "hotplug\_commands" and "unknown" commands may need adjustment for Niri (e.g. using `sh -c '...'` or Niri specific tools).

Syntax:

toml

```
[monitors.placement]
"description match".placement = "other description match"
```

Example to set a Sony monitor on top of a BenQ monitor

toml

```
[monitors.placement]
Sony.topOf = "BenQ"

## Character case is ignored, "_" can be added
Sony.Top_Of = ["BenQ"]

## Thanks to TOML format, complex configurations can use separate "sections" for clarity, eg:

[monitors.placement."My monitor brand"]
## You can also use "port" names such as *HDMI-A-1*, *DP-1*, etc...
leftOf = "eDP-1"

## lists are possible on the right part of the assignment:
rightOf = ["Sony", "BenQ"]

# When multiple targets are specified, only the first connected monitor
# matching a pattern is used as the reference.

## > 2.3.2: you can also set scale, transform & rate for a given monitor
[monitors.placement.Microstep]
rate = 100
```

Try to keep the rules as simple as possible, but relatively complex scenarios are supported.

NOTE

Check [wlr layout UI](https://github.com/fdev31/wlr-layout-ui) which is a nice complement to configure your monitor settings.

## Commands [​](#commands)

Loading commands...

## Configuration [​](#configuration)

Loading configuration...

### `placement` [​](#config-placement)

Configure monitor settings and relative positioning. Each monitor is identified by a [pattern](#monitor-patterns) (port name or description substring) and can have both display settings and positioning rules.

toml

```
[monitors.placement."My monitor"]
# Display settings
scale = 1.25
transform = 1
rate = 144
resolution = "2560x1440"

# Positioning
leftOf = "eDP-1"
```

#### Monitor Settings [​](#monitor-settings)

These settings control the display properties of a monitor.

##### `scale` [​](#placement-scale)

Controls UI element size. Higher values make the UI larger (zoomed in), showing less content.

Scale ValueContent Visible`0.666667`More (zoomed out)`0.833333`More`1.0`Native`1.25`Less`1.6`Less`2.0`25% (zoomed in)

TIP

For HiDPI displays, use values like `1.5` or `2.0` to make UI elements larger and more readable at the cost of screen real estate.

##### `transform` [​](#placement-transform)

Rotates and optionally flips the monitor.

ValueRotationDescription0NormalNo rotation (landscape)190°Portrait (rotated right)2180°Upside down3270°Portrait (rotated left)4FlippedMirrored horizontally5Flipped 90°Mirrored + 90°6Flipped 180°Mirrored + 180°7Flipped 270°Mirrored + 270°

##### `rate` [​](#placement-rate)

Refresh rate in Hz.

TIP

Run `hyprctl monitors` to see available refresh rates for each monitor.

##### `resolution` [​](#placement-resolution)

Display resolution. Can be specified as a string or array.

toml

```
resolution = "2560x1440"
# or
resolution = [2560, 1440]
```

TIP

Run `hyprctl monitors` to see available resolutions for each monitor.

##### `disables` [​](#placement-disables)

List of monitors to disable when this monitor is connected. This is useful for automatically turning off a laptop's built-in display when an external monitor is plugged in.

toml

```
[monitors.placement."External Monitor"]
disables = ["eDP-1"]  # Disable laptop screen when this monitor is connected
```

You can disable multiple monitors and combine with positioning rules:

toml

```
[monitors.placement."DELL U2722D"]
leftOf = "DP-2"
disables = ["eDP-1", "HDMI-A-2"]
```

NOTE

Monitors specified in `disables` are excluded from layout calculations. They will be re-enabled on the next relayout if the disabling monitor is disconnected.

#### Positioning Rules [​](#positioning-rules)

Position monitors relative to each other using directional keywords.

**Directions:**

- `leftOf` / `rightOf` — horizontal placement
- `topOf` / `bottomOf` — vertical placement

**Alignment modifiers** (for different-sized monitors):

- `start` (default) — align at top/left edge
- `center` / `middle` — center alignment
- `end` — align at bottom/right edge

Combine direction + alignment: `topCenterOf`, `leftEndOf`, `right_middle_of`, etc.

Everything is case insensitive; use `_` for readability (e.g., `top_center_of`).

IMPORTANT

At least one monitor must have **no placement rule** to serve as the anchor/reference point. Other monitors are positioned relative to this anchor.

See [Placement Examples](#placement-examples) for visual diagrams.

#### Monitor Patterns [​](#monitor-patterns)

Both the monitor being configured and the target monitor can be specified using:

1. **Port name** (exact match) — e.g., `eDP-1`, `HDMI-A-1`, `DP-1`
2. **Description substring** (partial match) — e.g., `Hisense`, `BenQ`, `DELL P2417H`

The plugin first checks for an exact port name match, then searches monitor descriptions for a substring match. Descriptions typically contain the manufacturer, model, and serial number.

toml

```
# Target by port name
[monitors.placement.Sony]
topOf = "eDP-1"

# Target by brand/model name
[monitors.placement.Hisense]
top_middle_of = "BenQ"

# Mix both approaches
[monitors.placement."DELL P2417H"]
right_end_of = "HDMI-A-1"
```

TIP

Run `hyprctl monitors` (or `nirictl outputs` for Niri) to see the full description of each connected monitor.

### `startup_relayout` [​](#config-startup-relayout)

When set to `false`, do not initialize the monitor layout on startup or when configuration is reloaded.

### `relayout_on_config_change` [​](#config-relayout-on-config-change)

When set to `false`, do not relayout when Hyprland config is reloaded.

### `new_monitor_delay` [​](#config-new-monitor-delay)

The layout computation happens after this delay when a new monitor is detected, to let time for things to settle.

### `hotplug_command` [​](#config-hotplug-command)

Allows to run a command when any monitor is plugged.

toml

```
[monitors]
hotplug_command = "wlrlui -m"
```

### `hotplug_commands` [​](#config-hotplug-commands)

Allows to run a command when a specific monitor is plugged.

Example to load a specific profile using [wlr layout ui](https://github.com/fdev31/wlr-layout-ui):

toml

```
[monitors.hotplug_commands]
"DELL P2417H CJFH277Q3HCB" = "wlrlui rotated"
```

### `unknown` [​](#config-unknown)

Allows to run a command when no monitor layout has been changed (no rule applied).

toml

```
[monitors]
unknown = "wlrlui"
```

## Placement Examples [​](#placement-examples)

This section provides visual diagrams to help understand monitor placement rules.

### Basic Positions [​](#basic-positions)

The four basic placement directions position a monitor relative to another:

#### `topOf` - Monitor above another [​](#topof-monitor-above-another)

![Monitor A placed on top of Monitor B](https://hyprland-community.github.io/pyprland/images/monitors/basic-top-of.svg)

toml

```
[monitors.placement.A]
topOf = "B"
```

#### `bottomOf` - Monitor below another [​](#bottomof-monitor-below-another)

![Monitor A placed below Monitor B](https://hyprland-community.github.io/pyprland/images/monitors/basic-bottom-of.svg)

toml

```
[monitors.placement.A]
bottomOf = "B"
```

#### `leftOf` - Monitor to the left [​](#leftof-monitor-to-the-left)

![Monitor A placed to the left of Monitor B](https://hyprland-community.github.io/pyprland/images/monitors/basic-left-of.svg)

toml

```
[monitors.placement.A]
leftOf = "B"
```

#### `rightOf` - Monitor to the right [​](#rightof-monitor-to-the-right)

![Monitor A placed to the right of Monitor B](https://hyprland-community.github.io/pyprland/images/monitors/basic-right-of.svg)

toml

```
[monitors.placement.A]
rightOf = "B"
```

### Alignment Modifiers [​](#alignment-modifiers)

When monitors have different sizes, alignment modifiers control where the smaller monitor aligns along the edge.

#### Horizontal placement (`leftOf` / `rightOf`) [​](#horizontal-placement-leftof-rightof)

**Start (default)** - Top edges align:

![Monitor A to the left of B, top edges aligned](https://hyprland-community.github.io/pyprland/images/monitors/align-left-start.svg)

toml

```
[monitors.placement.A]
leftOf = "B"  # same as leftStartOf
```

**Center / Middle** - Vertically centered:

![Monitor A to the left of B, vertically centered](https://hyprland-community.github.io/pyprland/images/monitors/align-left-center.svg)

toml

```
[monitors.placement.A]
leftCenterOf = "B"  # or leftMiddleOf
```

**End** - Bottom edges align:

![Monitor A to the left of B, bottom edges aligned](https://hyprland-community.github.io/pyprland/images/monitors/align-left-end.svg)

toml

```
[monitors.placement.A]
leftEndOf = "B"
```

#### Vertical placement (`topOf` / `bottomOf`) [​](#vertical-placement-topof-bottomof)

**Start (default)** - Left edges align:

![Monitor A on top of B, left edges aligned](https://hyprland-community.github.io/pyprland/images/monitors/align-top-start.svg)

toml

```
[monitors.placement.A]
topOf = "B"  # same as topStartOf
```

**Center / Middle** - Horizontally centered:

![Monitor A on top of B, horizontally centered](https://hyprland-community.github.io/pyprland/images/monitors/align-top-center.svg)

toml

```
[monitors.placement.A]
topCenterOf = "B"  # or topMiddleOf
```

**End** - Right edges align:

![Monitor A on top of B, right edges aligned](https://hyprland-community.github.io/pyprland/images/monitors/align-top-end.svg)

toml

```
[monitors.placement.A]
topEndOf = "B"
```

### Common Setups [​](#common-setups)

#### Dual side-by-side [​](#dual-side-by-side)

![Dual monitor setup: A and B side by side](https://hyprland-community.github.io/pyprland/images/monitors/setup-dual.svg)

toml

```
[monitors.placement.A]
leftOf = "B"
```

#### Triple horizontal [​](#triple-horizontal)

![Triple monitor setup: A, B, C in a row](https://hyprland-community.github.io/pyprland/images/monitors/setup-triple.svg)

toml

```
[monitors.placement.A]
leftOf = "B"

[monitors.placement.C]
rightOf = "B"
```

#### Stacked (vertical) [​](#stacked-vertical)

![Stacked monitor setup: A on top, B in middle, C at bottom](https://hyprland-community.github.io/pyprland/images/monitors/setup-stacked.svg)

toml

```
[monitors.placement.A]
topOf = "B"

[monitors.placement.C]
bottomOf = "B"
```

### Real-World Example: L-Shape with Portrait Monitor [​](#real-world-example-l-shape-with-portrait-monitor)

This example shows a complex 3-monitor setup combining portrait mode, corner alignment, and different-sized displays.

**Layout:**

![L-shape monitor setup with portrait monitor A, anchor B, and landscape C](https://hyprland-community.github.io/pyprland/images/monitors/real-world-l-shape.svg)

Where:

- **A** (HDMI-A-1) = Portrait monitor (transform=1), directly on top of B (blue)
- **B** (eDP-1) = Main anchor monitor, landscape (green)
- **C** = Landscape monitor, positioned at the bottom-right corner of A (orange)

**Configuration:**

toml

```
[monitors.placement.CJFH277Q3HCB]
top_of = "eDP-1"
transform = 1
scale = 0.83

[monitors.placement.CJFH27888CUB]
right_end_of = "HDMI-A-1"
```

**Explanation:**

1. **B (eDP-1)** has no placement rule, making it the anchor/reference point
2. **A (CJFH277Q3HCB)** is placed on top of B with `top_of = "eDP-1"`, rotated to portrait with `transform = 1`, and scaled to 83%
3. **C (CJFH27888CUB)** uses `right_end_of = "HDMI-A-1"` to position itself to the right of A with bottom edges aligned, creating the L-shape

The `right_end_of` placement is key here: it aligns C's bottom edge with A's bottom edge, tucking C into the corner rather than aligning at the top (which `rightOf` would do).