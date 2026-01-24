---
title: Screenshot | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/cli-screenshot
source: sitemap
fetched_at: 2026-01-24T13:33:36.02662066-03:00
rendered_js: false
word_count: 150
summary: This document provides a comprehensive reference for the dms screenshot command, explaining its various capture modes, output formats, and command-line options for Wayland environments.
tags:
    - dms-screenshot
    - wayland
    - cli-reference
    - image-capture
    - linux-utilities
category: reference
---

```
███████╗ ██████╗██████╗ ███████╗███████╗███╗   ██╗
██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝████╗  ██║
███████╗██║     ██████╔╝█████╗  █████╗  ██╔██╗ ██║
╚════██║██║     ██╔══██╗██╔══╝  ██╔══╝  ██║╚██╗██║
███████║╚██████╗██║  ██║███████╗███████╗██║ ╚████║
╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝
```

The `dms screenshot` command captures screenshots from Wayland displays with support for multiple capture modes, output formats, and clipboard integration.

## Quick Start[​](#quick-start "Direct link to Quick Start")

```
# Region select, save file + clipboard
dms screenshot

# Full screen of focused output
dms screenshot full

# Clipboard only
dms screenshot --no-file
```

Press **Escape** to cancel region selection at any time.

## Capture Modes[​](#capture-modes "Direct link to Capture Modes")

ModeCommandDescription`region``dms screenshot`Select a region interactively (default)`full``dms screenshot full`Capture the focused output`all``dms screenshot all`Capture all outputs combined`output``dms screenshot output -o NAME`Capture a specific output by name`last``dms screenshot last`Capture the last selected region

### List Available Outputs[​](#list-available-outputs "Direct link to List Available Outputs")

## Output Formats[​](#output-formats "Direct link to Output Formats")

Use `--format` or `-f` to specify the output format. Default is `png`.

FormatFlagNotesPNG`-f png`Default, losslessJPEG`-f jpg`Use `-q` to set quality (1-100)PPM`-f ppm`Raw format

```
# JPEG with custom quality
dms screenshot -f jpg -q85
```

## Options[​](#options "Direct link to Options")

FlagShortDescription`--cursor`Include cursor in screenshot`--stdout`Output to stdout (for piping)`--dir``-d`Output directory`--filename`Output filename (auto-generated if empty)`--format``-f`Output format: png, jpg, ppm (default: png)`--quality``-q`JPEG quality 1-100 (default: 90)`--output``-o`Output name for 'output' mode`--no-clipboard`Don't copy to clipboard`--no-file`Don't save to file`--no-notify`Don't show notification`--config``-c`Custom DMS config directory path`--help``-h`Show help

## Examples[​](#examples "Direct link to Examples")

### Region Selection[​](#region-selection "Direct link to Region Selection")

```
# Interactive selection, save file + clipboard
dms screenshot

# File only, no clipboard
dms screenshot --no-clipboard

# Clipboard only, no file
dms screenshot --no-file
```

### Full Screen Capture[​](#full-screen-capture "Direct link to Full Screen Capture")

```
# Focused output
dms screenshot full

# All outputs combined
dms screenshot all

# Specific output
dms screenshot output -o DP-1
```

### Repeat Last Capture[​](#repeat-last-capture "Direct link to Repeat Last Capture")

```
# Capture the same region as before
dms screenshot last
```

### Include Cursor[​](#include-cursor "Direct link to Include Cursor")

```
dms screenshot full --cursor
```

### Pipe to Editor[​](#pipe-to-editor "Direct link to Pipe to Editor")

```
# Send to swappy for annotation
dms screenshot --stdout| swappy -f -
```

### Custom Output Location[​](#custom-output-location "Direct link to Custom Output Location")

```
# Save to specific directory
dms screenshot -d ~/Pictures/screenshots

# Custom filename
dms screenshot --filename my-screenshot.png
```