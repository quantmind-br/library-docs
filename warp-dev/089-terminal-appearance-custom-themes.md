---
title: Custom themes | Warp
url: https://docs.warp.dev/terminal/appearance/custom-themes
source: sitemap
fetched_at: 2026-04-29T15:02:46.932886149-03:00
rendered_js: false
word_count: 395
summary: This document provides instructions on how to install, create, and manage custom terminal themes for Warp using YAML configuration files and the built-in theme repository.
tags:
    - warp-terminal
    - theme-customization
    - yaml-configuration
    - ui-design
    - terminal-styling
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
# Custom Themes

Install, create, and manage custom terminal themes using YAML configuration files and the built-in theme repository.

Browse Warp's [theme repository on GitHub](https://github.com/warpdotdev/themes) for ready-made themes. Each theme has a preview generated in the README.

Two theme types:
- **Standard themes** — typical color setup
- **Base16 themes** — follow the framework suggested by [@chriskempson](https://github.com/chriskempson/base16)

## Installing a Theme

Two ways to install:
1. Download a single file
2. Clone the entire repo into the appropriate location for your OS

## Using a Custom Theme

1. Create the themes directory:
2. Add your custom theme YAML file to this directory

> [!info]
> It may take several minutes for Warp to initially discover new themes. You can restart Warp. Future changes will reflect within seconds.

Your theme will now appear in the list of available themes.

## Creating a Custom Theme (Manually)

Create custom themes using `.yaml` files. Format is subject to change but backward compatibility is maintained.

> [!info]
> Each color is represented in hex and must start with `#`.

| Property | Description |
|----------|-------------|
| `name` | Theme name shown in Theme picker |
| `accent` | Color used for UI highlights |
| `cursor` | Cursor color (optional; defaults to accent if omitted) |
| `background` | Background color |
| `foreground` | Foreground color |
| `details` | Detailing options (`darker` for dark theme, `lighter` for light mode) |
| `terminal_colors` | Collection of normal & bright colors (16 ANSI colors) |

## Creating a Custom Theme (Automatically)

Generate themes from a background image. Click the **+** button in the theme picker (**Settings** > **Appearance** > **Themes**) or search `Open Theme Picker` in the [Command Palette](https://docs.warp.dev/terminal/command-palette).

## Background Images and Gradients

Add a background image using the `background_image:` attribute.

> [!info]
> Warp currently only supports `.jpg` file format (`.jpeg`, `.jpg`, `.JPEG`).

Set up gradients under `accent` with two key-value pairs:
- "left" and "right", or
- "top" and "bottom"

Warp also supports gradients for the background.

## Contributing

Contributions to the [theme repo](https://github.com/warpdotdev/themes) are appreciated:

1. Fork the project
2. Create your branch: `git checkout -b theme/AwesomeTheme`
3. Regenerate thumbnails
4. Commit and open a pull request

> [!info]
> PRs with custom background images cannot be accepted due to licensing restrictions and binary size. Include a comment in the YAML with a download link instead.
