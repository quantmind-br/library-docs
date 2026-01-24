---
title: Custom Themes | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/custom-themes
source: sitemap
fetched_at: 2026-01-24T13:35:41.644673626-03:00
rendered_js: false
word_count: 471
summary: This document provides instructions on creating, structuring, and applying custom color themes for DankMaterialShell using JSON configuration and matugen color keywords.
tags:
    - dankmaterialshell
    - theming
    - color-schemes
    - matugen
    - json-configuration
    - customization
category: guide
---

```
████████╗██╗  ██╗███████╗███╗   ███╗███████╗███████╗
╚══██╔══╝██║  ██║██╔════╝████╗ ████║██╔════╝██╔════╝
   ██║   ███████║█████╗  ██╔████╔██║█████╗  ███████╗
   ██║   ██╔══██║██╔══╝  ██║╚██╔╝██║██╔══╝  ╚════██║
   ██║   ██║  ██║███████╗██║ ╚═╝ ██║███████╗███████║
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝╚══════╝
```

DankMaterialShell supports custom color themes using arbitrary color schemes. You can create your own themes or use pre-made ones.

## Theme Structure[​](#theme-structure "Direct link to Theme Structure")

Custom themes are defined in JSON files that generally map to [matugen color keywords](https://github.com/InioX/matugen/wiki/Configuration#colors). Themes can have separate `dark` and `light` variants, or use a single color scheme for both modes.

### Complete Theme Example[​](#complete-theme-example "Direct link to Complete Theme Example")

```
{
"dark":{
"name":"Cyberpunk Electric Dark",
"primary":"#00FFCC",
"primaryText":"#000000",
"primaryContainer":"#00CC99",
"secondary":"#FF4DFF",
"surface":"#0F0F0F",
"surfaceText":"#E0FFE0",
"surfaceVariant":"#1F2F1F",
"surfaceVariantText":"#CCFFCC",
"surfaceTint":"#00FFCC",
"background":"#000000",
"backgroundText":"#F0FFF0",
"outline":"#80FF80",
"surfaceContainer":"#1A2B1A",
"surfaceContainerHigh":"#264026",
"surfaceContainerHighest":"#33553F",
"error":"#FF0066",
"warning":"#CCFF00",
"info":"#00FFCC",
"matugen_type":"scheme-expressive"
},
"light":{
"name":"Cyberpunk Electric Light",
"primary":"#00B899",
"primaryText":"#FFFFFF",
"primaryContainer":"#66FFDD",
"secondary":"#CC00CC",
"surface":"#F0FFF0",
"surfaceText":"#1F2F1F",
"surfaceVariant":"#E6FFE6",
"surfaceVariantText":"#2D4D2D",
"surfaceTint":"#00B899",
"background":"#FFFFFF",
"backgroundText":"#000000",
"outline":"#4DCC4D",
"surfaceContainer":"#F5FFF5",
"surfaceContainerHigh":"#EBFFEB",
"surfaceContainerHighest":"#E1FFE1",
"error":"#B3004D",
"warning":"#99CC00",
"info":"#00B899",
"matugen_type":"scheme-expressive"
}
}
```

### Single Mode Theme[​](#single-mode-theme "Direct link to Single Mode Theme")

For themes without light/dark variants, define colors at the top level:

```
{
"name":"Theme Name",
"primary":"#eeeeee",
"primaryText":"#000000",
"surface":"#ffffff",
"surfaceText":"#000000",
"background":"#f5f5f5",
"backgroundText":"#000000",
"outline":"#cccccc",
"matugen_type":"scheme-tonal-spot"
}
```

## Required Color Properties[​](#required-color-properties "Direct link to Required Color Properties")

### Primary Colors[​](#primary-colors "Direct link to Primary Colors")

- `primary` - Main accent color for buttons, highlights, and active states
- `primaryText` - Text color contrasting with primary background
- `primaryContainer` - Variant of primary for containers

### Secondary Colors[​](#secondary-colors "Direct link to Secondary Colors")

- `secondary` - Supporting accent color for variety and hierarchy
- `surfaceTint` - Tint color applied to surfaces (usually derived from primary)

### Surface Colors[​](#surface-colors "Direct link to Surface Colors")

![Surface Colors Hierarchy](https://danklinux.com/img/surfacecolorslight.jpg)![Surface Colors Hierarchy](https://danklinux.com/img/surfacecolors.jpg)

- `surface` - Default surface color for cards and panels
- `surfaceText` - Primary text color on surface backgrounds
- `surfaceVariant` - Alternate surface for subtle differentiation
- `surfaceVariantText` - Text color for surfaceVariant backgrounds
- `surfaceContainer` - Container surface, slightly different from surface
- `surfaceContainerHigh` - Elevated container for layered interfaces
- `surfaceContainerHighest` - Highest elevation container for top-level surfaces

### Background Colors[​](#background-colors "Direct link to Background Colors")

- `background` - Main background color for the interface
- `backgroundText` - Text color for background areas

### Outline[​](#outline "Direct link to Outline")

- `outline` - Color for subtle borders, dividers, muted icons, and extra subtle text

## Optional Properties[​](#optional-properties "Direct link to Optional Properties")

### Semantic Colors[​](#semantic-colors "Direct link to Semantic Colors")

- `error` - Error states, delete buttons, critical warnings
- `warning` - Warning states and caution indicators
- `info` - Informational states and neutral indicators

### Matugen Type[​](#matugen-type "Direct link to Matugen Type")

The `matugen_type` property controls the color scheme algorithm used for system app theming. Default is `scheme-tonal-spot` if not specified.

Available options:

- `scheme-content` - Content-based color extraction
- `scheme-expressive` - Expressive, vibrant color schemes
- `scheme-fidelity` - High fidelity to source material
- `scheme-fruit-salad` - Colorful, fruit salad-like schemes
- `scheme-monochrome` - Monochromatic color schemes
- `scheme-neutral` - Neutral, subdued color schemes
- `scheme-rainbow` - Rainbow-like color schemes
- `scheme-tonal-spot` - Tonal spot color schemes (default)

## Example Themes[​](#example-themes "Direct link to Example Themes")

Pre-built example themes are available in the [DankMaterialShell repository](https://github.com/AvengeMedia/DankMaterialShell/tree/master/docs):

- [Cyberpunk Electric](https://github.com/AvengeMedia/DankMaterialShell/blob/master/docs/theme_cyberpunk_electric.json) - Neon green and magenta cyberpunk aesthetic
- [Hotline Miami](https://github.com/AvengeMedia/DankMaterialShell/blob/master/docs/theme_hotline_miami.json) - Retro 80s hot pink and blue
- [Miami Vice](https://github.com/AvengeMedia/DankMaterialShell/blob/master/docs/theme_miami_vice.json) - Classic teal and pink vice aesthetic
- [Synthwave Electric](https://github.com/AvengeMedia/DankMaterialShell/blob/master/docs/theme_synthwave_electric.json) - Electric purple and cyan synthwave

## Applying Custom Themes[​](#applying-custom-themes "Direct link to Applying Custom Themes")

### Via Settings UI[​](#via-settings-ui "Direct link to Via Settings UI")

1. Open **Settings → Theme & Colors**
2. Select **Custom** from the theme dropdown
3. Choose your theme file path

### Via Configuration File[​](#via-configuration-file "Direct link to Via Configuration File")

Edit `~/.config/DankMaterialShell/settings.json`:

```
{
"currentThemeName":"custom",
"customThemeFile":"/path/to/mytheme.json"
}
```

### Live Editing[​](#live-editing "Direct link to Live Editing")

Custom theme files are reactive - editing the JSON file automatically updates the shell if it's the currently active theme.

## Theme Development Tips[​](#theme-development-tips "Direct link to Theme Development Tips")

- **Start from examples:** Use the pre-built themes as templates
- **Adjust incrementally:** Change one color at a time to see the impact
- **Test both modes:** If providing dark/light variants, test both thoroughly
- **Consider contrast:** Ensure text colors have sufficient contrast with backgrounds
- **Experiment with matugen\_type:** Different schemes work better with different color palettes
- **Version control:** Store themes in your dotfiles for easy synchronization