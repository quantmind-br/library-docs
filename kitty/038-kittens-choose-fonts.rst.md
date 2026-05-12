---
title: Changing kitty fonts
url: https://github.com/kovidgoyal/kitty/blob/master/docs/kittens/choose-fonts.rst
source: git
fetched_at: 2026-05-04T15:57:51.470508789-03:00
rendered_js: false
word_count: 263
summary: Configure font rendering in kitty — the choose-fonts kitten for interactive selection, OpenType features, variable fonts, and the font specification syntax for kitty.conf.
tags:
    - kitty
    - terminal-emulator
    - font-configuration
    - typography
    - opentype
    - variable-fonts
category: configuration
optimized: true
optimized_at: 2026-05-04T20:30:00Z
---
# Changing kitty fonts

kitty supports OpenType features (alternate glyphs), variable fonts (weight/spacing control), per-Unicode-codepoint font selection via `symbol_map`, font metric modification via `modify_font`, and gamma curve adjustment via `text_composition_strategy`.

## Interactive font selection

Run the choose-fonts kitten:

```bash
kitten choose-fonts
```

Workflow:
1. Type letters to filter the family list. Press Enter to select.
2. Preview regular/bold/italic faces. Press R to fine-tune the regular face — others auto-adjust.
3. Click a style or feature to select it. Use sliders for variable axis values.

## Font specification syntax

Four face keys in `kitty.conf`: `font_family`, `bold_font`, `italic_font`, `bold_italic_font`. Each accepts three value types:

### Font family name

```conf
font_family Fira Code
```

OS searches for a matching font.

### `auto`

```conf
font_family auto
```

kitty auto-selects bold/italic variants from `font_family`.

### `key=value` syntax

For precise control:

```conf
font_family family="Fira Code"
font_family postscript_name=FiraCode
font_family family=SourceCodeVF variable_name=SourceCodeUpright features="+zero cv01=2" wght=380
```

**Keys:**

| Key | Description |
|-----|-------------|
| `family` | Font family name. Multiple actual faces (bold, italic) can be variable. |
| `style` | Style name to choose a particular face from a family. |
| `postscript_name` | Select exact face by PostScript name. Insufficient for variable fonts. |
| `full_name` | Less precise than `postscript_name` — avoid. |
| `variable_name` | Distinguish multiple font files in a variable font family (e.g., upright vs. italic). Use with `family`. |
| `features` | Space-separated OpenType features: `+feature` enables, `-feature` disables, `feature=value` sets. HarfBuzz syntax. |
| `system` | Pass a string directly to OS font selection APIs. Use alone, not with other keys. |

Any four-letter key is treated as a variable font axis name (e.g., `wght` for weight, `wdth` for width) and sets its value.

#kitty #terminal-emulator #font-configuration #opentype #variable-fonts
