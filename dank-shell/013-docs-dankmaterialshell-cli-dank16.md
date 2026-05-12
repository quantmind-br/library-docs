---
title: Dank16 | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/cli-dank16
source: sitemap
fetched_at: 2026-04-26T08:38:43.406865056-03:00
rendered_js: false
word_count: 918
summary: Dank16 is a command-line tool that generates complete, accessible 16-color Base16 terminal palettes from a single hex color using advanced contrast algorithms.
tags:
    - cli-tool
    - base16
    - color-palette
    - terminal-theme
    - accessibility
    - contrast-algorithm
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Version: 1.4

`dms dank16` generates complete Base16 color palettes from a single hex input color, producing harmonious 16-color terminal themes with proper contrast for both light and dark modes.

## Overview

**Key Features:**

- Generate complete 16-color palettes from one color
- Support for both dark and light themes
- Advanced contrast algorithms (Delta Phi Star or WCAG)
- Multiple output formats (terminal configs, JSON, VSCode)
- Custom background color support

![Dank16 color palette example showing 16 ANSI colors](https://danklinux.com/img/dank16_light.png)![Dank16 color palette example showing 16 ANSI colors](https://danklinux.com/img/dank16.png)

## Quick Start

Generate a dark theme palette:

```bash
dms dank16 "#8b5cf6"
```

**Output:**

```text
palette = 0=#1a1a1a
palette = 1=#e25443
palette = 2=#6ed675
palette = 3=#dbd97b
palette = 4=#9a65fd
palette = 5=#9173d2
palette = 6=#9565ff
palette = 7=#abb2bf
palette = 8=#5c6370
palette = 9=#e06a5f
palette = 10=#86e08b
palette = 11=#e8e697
palette = 12=#e5c7ff
palette = 13=#8269d9
palette = 14=#9069c0
palette = 15=#ffffff
```

Generate a light theme palette:

```bash
dms dank16 "#8b5cf6" --light
```

## Base16 Color Mapping

| Index | Purpose | Dark Theme | Light Theme |
|-------|---------|------------|-------------|
| 0 | Background | Dark gray | Light gray |
| 1 | Red | Saturated red | Dark red |
| 2 | Green | Saturated green | Dark green |
| 3 | Yellow | Saturated yellow | Dark yellow |
| 4 | Blue | Derived from input | Derived from input |
| 5 | Magenta | Derived from input | Derived from input |
| 6 | Cyan | Derived from input | Derived from input |
| 7 | Foreground | Light gray | Dark gray |
| 8 | Bright Black | Medium gray | Dark gray |
| 9 | Bright Red | Lighter red | Medium red |
| 10 | Bright Green | Lighter green | Medium green |
| 11 | Bright Yellow | Lighter yellow | Medium yellow |
| 12 | Bright Blue | Lighter variant | Lighter variant |
| 13 | Bright Magenta | Lighter variant | Lighter variant |
| 14 | Bright Cyan | Lighter variant | Lighter variant |
| 15 | Bright White | White | Black |

## Output Formats

### Default Format

The default output is a simple palette format.

### Kitty Terminal

```bash
dms dank16 "#8b5cf6" --kitty
```

**Output:**

```text
color0   #1a1a1a
color1   #e25443
color2   #6ed675
color3   #dbd97b
...
```

Copy the output directly to `~/.config/kitty/kitty.conf`.

### Foot Terminal

```bash
dms dank16 "#8b5cf6" --foot
```

Generates color configuration for the Foot terminal emulator.

### Alacritty Terminal

```bash
dms dank16 "#8b5cf6" --alacritty
```

Generates YAML configuration for Alacritty's color scheme.

### Ghostty Terminal

```bash
dms dank16 "#8b5cf6" --ghostty
```

Generates configuration for the Ghostty terminal emulator.

### JSON Format

```bash
dms dank16 "#8b5cf6" --json
```

Outputs the palette as a JSON object with detailed color information.

### Variants Format

```bash
dms dank16 "#8b5cf6" --variants [--light] [--background <color>]
```

Outputs all color variants in a single call:

```json
{
  "color0": {
    "dark": {"hex": "#1a1a1a", "hex_stripped": "1a1a1a"},
    "light": {"hex": "#f8f8f8", "hex_stripped": "f8f8f8"},
    "default": {"hex": "#1a1a1a", "hex_stripped": "1a1a1a"}
  },
  ...
}
```

| Variant | Description |
|---------|-------------|
| `dark` | Always dark mode colors |
| `light` | Always light mode colors |
| `default` | Mode-aware (uses `--light` flag to determine which variant) |

Use `--primary-dark` and `--primary-light` to specify different primary colors for each mode:

```bash
dms dank16 --variants --primary-dark "#8b5cf6" --primary-light "#6d28d9"
```

This is the format injected into matugen templates as the `dank16` object.

## Contrast Algorithms

Dank16 supports two contrast algorithms to ensure readability:

### Delta Phi Star (DPS) - Default

The default algorithm uses Delta Phi Star contrast, providing perceptually uniform contrast based on the golden ratio (phi):

- Uses CIELAB color space for perceptual accuracy
- Applies golden ratio (phi ~ 1.618) calculations for harmonious contrast
- Targets minimum Lc (lightness contrast) values of 40 for normal text and 35 for secondary text
- Adjusts for negative polarity in dark themes

```bash
dms dank16 "#8b5cf6" --contrast dps
```

**How it works:**

1. Converts colors to CIELAB space (L*, a*, b*)
2. Calculates lightness contrast using: `Lc = (|Lb^phi - Lf^phi|)^(1/phi) x 1.414 - 40`
3. Adjusts for polarity (+5 for dark mode)
4. Ensures minimum contrast thresholds are met

### WCAG Contrast

Uses the standard WCAG 2.1 contrast ratio algorithm:

- Targets minimum ratios of 4.5:1 for normal text and 3.0:1 for secondary text
- Based on relative luminance calculations
- Industry standard for accessibility compliance

```bash
dms dank16 "#8b5cf6" --contrast wcag
```

## Advanced Options

### Custom Background

```bash
# Dark theme with custom background
dms dank16 "#8b5cf6" --background "#0d1117"
# Light theme with custom background
dms dank16 "#8b5cf6" --light --background "#ffffff"
```

### Combining Options

```bash
dms dank16 "#8b5cf6" \
  --light \
  --background "#fafafa" \
  --contrast wcag \
  --kitty > ~/.config/kitty/dank-light.conf
```

## Algorithm Overview

The palette generation process:

1. **Container Derivation**: Derives a container color from input by adjusting saturation and value based on theme mode
2. **Color Generation**:
   - Red, green, yellow: Generated with hue shifts and saturation adjustments
   - Blue, magenta, cyan: Derived from input color with variations
   - Foreground/background: Set based on theme mode
3. **Contrast Enforcement**: Each color adjusted to meet minimum contrast requirements:
   - Converts to HSV or CIELAB color space
   - Incrementally adjusts lightness/value until contrast threshold is met
   - Preserves hue to maintain color identity
4. **Bright Variants**: Generates brighter versions for colors 9-14:
   - Dark mode: Uses L* retoning for high visibility
   - Light mode: Reduces saturation and adjusts value for subtle contrast

## Use Cases

### Terminal Theming

```bash
# Kitty
dms dank16 "#your-color" --kitty >> ~/.config/kitty/kitty.conf
# Foot
dms dank16 "#your-color" --foot >> ~/.config/foot/foot.ini
# Alacritty
dms dank16 "#your-color" --alacritty >> ~/.config/alacritty/alacritty.yml
```

### Editor Themes

The dank16 palette is available in matugen templates via the `dank16` object. See [[062-docs-dankmaterialshell-application-themes#available-template-variables|Application Theming]] for details.

### Dynamic Theming

```bash
#!/bin/bash
# Extract dominant color from wallpaper
dominant_color=$(your-color-extraction-tool ~/wallpaper.jpg)
# Generate and apply terminal theme
dms dank16 "$dominant_color" --kitty > ~/.config/kitty/auto-theme.conf
kitty @ set-colors -a ~/.config/kitty/auto-theme.conf
```

### Light/Dark Mode Automation

```bash
#!/bin/bash
COLOR="#8b5cf6"
# Generate both variants
dms dank16 "$COLOR" --kitty > ~/.config/kitty/dank-dark.conf
dms dank16 "$COLOR" --light --kitty > ~/.config/kitty/dank-light.conf
# Switch based on time or system setting
if is_dark_mode; then
    kitty @ set-colors -a ~/.config/kitty/dank-dark.conf
else
    kitty @ set-colors -a ~/.config/kitty/dank-light.conf
fi
```

## Tips & Best Practices

### Choosing Input Colors

Choose an input color prominent in your terminal. The input color is most directly represented as blue/cyan colors (palette indices 4, 6, 12, 14), with other colors derived as complementary hues.

### Testing Contrast

```bash
# Generate palette
dms dank16 "#8b5cf6" --kitty > /tmp/test-theme.conf
# Open new kitty window with theme
kitty -o include=/tmp/test-theme.conf
```

### Iterating on Themes

```bash
# Try different shades
dms dank16 "#8b5cf6"    # Original
dms dank16 "#9b6cf6"    # Slightly lighter
dms dank16 "#7b4ce6"    # Slightly darker
```

## Command Reference

```bash
dms dank16 <hex_color> [flags]
```

**Arguments:**

| Argument | Type | Description |
|----------|------|-------------|
| `hex_color` | string | Input color in hex format (e.g., "#8b5cf6" or "8b5cf6") |

**Flags:**

| Flag | Description |
|------|-------------|
| `--light` | Generate light theme variant (default: dark) |
| `--background <hex>` | Custom background color |
| `--contrast <algorithm>` | Contrast algorithm: "dps" or "wcag" (default: "dps") |
| `--kitty` | Output in Kitty terminal format |
| `--foot` | Output in Foot terminal format |
| `--alacritty` | Output in Alacritty terminal format |
| `--ghostty` | Output in Ghostty terminal format |
| `--json` | Output as JSON object with hex, hex_stripped, and RGB values |
| `--variants` | Output all variants (dark/light/default) as JSON |
| `--primary-dark <hex>` | Primary color for dark mode (use with `--variants`) |
| `--primary-light <hex>` | Primary color for light mode (use with `--variants`) |
| `--wezterm` | Output in Wezterm terminal format |
| `-h, --help` | Show help |
