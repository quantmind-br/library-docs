---
title: Color Picker | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/cli-color-picker
source: sitemap
fetched_at: 2026-01-24T13:35:31.108735678-03:00
rendered_js: false
word_count: 213
summary: This document provides a guide and reference for the dms color pick command, an interactive screen color picker for Wayland that supports multiple output formats and custom templates.
tags:
    - wayland
    - color-picker
    - cli-utility
    - screen-capture
    - linux-productivity
    - color-formats
category: reference
---

```
 ██████╗ ██████╗ ██╗      ██████╗ ██████╗ ███████╗
██╔════╝██╔═══██╗██║     ██╔═══██╗██╔══██╗██╔════╝
██║     ██║   ██║██║     ██║   ██║██████╔╝███████╗
██║     ██║   ██║██║     ██║   ██║██╔══██╗╚════██║
╚██████╗╚██████╔╝███████╗╚██████╔╝██║  ██║███████║
╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
```

![Color Picker](https://danklinux.com/img/blog/v1/colorpick_light.png)![Color Picker](https://danklinux.com/img/blog/v1/colorpick_dark.png)

Pick colors from anywhere on your screen

The `dms color pick` command launches an interactive color picker for Wayland. Click any pixel on your screen to capture its color, with support for multiple output formats and custom templates.

## Quick Start[​](#quick-start "Direct link to Quick Start")

```
# Pick a color, output as hex
dms color pick

# Output as RGB
dms color pick --rgb

# Auto-copy to clipboard
dms color pick -a
```

Press **Escape** to cancel the picker at any time.

## Output Formats[​](#output-formats "Direct link to Output Formats")

Only one format flag can be used at a time. Default is `--hex`.

FlagOutputExample`--hex`Hexadecimal`#FF8040``--rgb`RGB values`255 128 64``--hsl`HSL values`24 75% 60%``--hsv`HSV values`24 75% 100%``--cmyk`CMYK values`0% 50% 75% 0%``--json`All formatsSee below

### JSON Output[​](#json-output "Direct link to JSON Output")

Returns all color formats in a single JSON object, useful for scripting.

## Custom Format Templates[​](#custom-format-templates "Direct link to Custom Format Templates")

The `-o` flag lets you define a custom output format using placeholders `{0}`, `{1}`, `{2}` (and `{3}` for CMYK).

### Placeholder Reference[​](#placeholder-reference "Direct link to Placeholder Reference")

Format0123`--hex` (default)R (hex, e.g. FF)G (hex)B (hex)-`--rgb`R (0-255)G (0-255)B (0-255)-`--hsl`H (0-360)S (0-100)L (0-100)-`--hsv`H (0-360)S (0-100)V (0-100)-`--cmyk`C (0-100)M (0-100)Y (0-100)K (0-100)

### Examples[​](#examples "Direct link to Examples")

```
# CSS rgb() function
dms color pick --rgb-o"rgb({0}, {1}, {2})"
# Output: rgb(255, 128, 64)

# CSS hsl() function
dms color pick --hsl-o"hsl({0}, {1}%, {2}%)"
# Output: hsl(24, 75%, 60%)

# Hex without hash
dms color pick -o"{0}{1}{2}"
# Output: FF8040

# Custom CMYK format
dms color pick --cmyk-o"C={0} M={1} Y={2} K={3}"
# Output: C=0 M=50 Y=75 K=0
```

## Options[​](#options "Direct link to Options")

FlagShortDescription`--hex`Output as hexadecimal (#RRGGBB)`--rgb`Output as RGB (R G B)`--hsl`Output as HSL (H S% L%)`--hsv`Output as HSV (H S% V%)`--cmyk`Output as CMYK (C% M% Y% K%)`--json`Output all formats as JSON`--lowercase``-l`Output hex in lowercase`--autocopy``-a`Copy result to clipboard`--output-format``-o`Custom output format template`--config``-c`Custom DMS config directory path`--help``-h`Show help

## Use Cases[​](#use-cases "Direct link to Use Cases")

### Quick Color Reference[​](#quick-color-reference "Direct link to Quick Color Reference")

Grab any color from your screen for use in design work:

```
dms color pick -a
# Picked color is now in your clipboard
```

### CSS Development[​](#css-development "Direct link to CSS Development")

Get colors ready for your stylesheets:

```
# For CSS custom properties
dms color pick --hsl-o"hsl({0}deg {1}% {2}%)"-a

# For rgba with full opacity
dms color pick --rgb-o"rgba({0}, {1}, {2}, 1)"-a
```

Capture colors programmatically:

```
#!/bin/bash
color=$(dms color pick --json)
hex=$(echo"$color"| jq -r'.hex')
echo"Selected: $hex"
```