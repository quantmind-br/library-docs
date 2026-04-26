---
title: Themes
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/themes.md
source: git
fetched_at: 2026-04-26T05:48:35.304852309-03:00
rendered_js: false
word_count: 1029
summary: This document explains how to create, configure, and customize themes for the Pi TUI using JSON files that define color palettes and token mappings.
tags:
    - theming
    - json-configuration
    - ui-customization
    - color-palette
    - terminal-interface
category: guide
optimized: true
optimized_at: 2026-04-26T09:00:00Z
---

# Themes

Themes are JSON files defining TUI colors. Every theme must define all 51 color tokens — none are optional.

## Locations

Pi loads themes from, in order:

| Source | Path / Mechanism |
|--------|-----------------|
| Built-in | `dark`, `light` |
| Global | `~/.pi/agent/themes/*.json` |
| Project | `.pi/themes/*.json` |
| Packages | `themes/` directories or `pi.themes` entries in `package.json` |
| Settings | `themes` array with files or directories |
| CLI | `--theme <path>` (repeatable) |

Disable all discovery with `--no-themes`.

## Selecting a Theme

Set via `/settings` or in `settings.json`:

```json
{
  "theme": "my-theme"
}
```

On first run, pi detects terminal background and defaults to `dark` or `light`.

## Creating a Custom Theme

1. Create the file:

```bash
mkdir -p ~/.pi/agent/themes
vim ~/.pi/agent/themes/my-theme.json
```

2. Define all 51 color tokens:

```json
{
  "$schema": "https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/src/modes/interactive/theme/theme-schema.json",
  "name": "my-theme",
  "vars": {
    "primary": "#00aaff",
    "secondary": 242
  },
  "colors": {
    "accent": "primary",
    "border": "primary",
    "borderAccent": "#00ffff",
    "borderMuted": "secondary",
    "success": "#00ff00",
    "error": "#ff0000",
    "warning": "#ffff00",
    "muted": "secondary",
    "dim": 240,
    "text": "",
    "thinkingText": "secondary",
    "selectedBg": "#2d2d30",
    "userMessageBg": "#2d2d30",
    "userMessageText": "",
    "customMessageBg": "#2d2d30",
    "customMessageText": "",
    "customMessageLabel": "primary",
    "toolPendingBg": "#1e1e2e",
    "toolSuccessBg": "#1e2e1e",
    "toolErrorBg": "#2e1e1e",
    "toolTitle": "primary",
    "toolOutput": "",
    "mdHeading": "#ffaa00",
    "mdLink": "primary",
    "mdLinkUrl": "secondary",
    "mdCode": "#00ffff",
    "mdCodeBlock": "",
    "mdCodeBlockBorder": "secondary",
    "mdQuote": "secondary",
    "mdQuoteBorder": "secondary",
    "mdHr": "secondary",
    "mdListBullet": "#00ffff",
    "toolDiffAdded": "#00ff00",
    "toolDiffRemoved": "#ff0000",
    "toolDiffContext": "secondary",
    "syntaxComment": "secondary",
    "syntaxKeyword": "primary",
    "syntaxFunction": "#00aaff",
    "syntaxVariable": "#ffaa00",
    "syntaxString": "#00ff00",
    "syntaxNumber": "#ff00ff",
    "syntaxType": "#00aaff",
    "syntaxOperator": "primary",
    "syntaxPunctuation": "secondary",
    "thinkingOff": "secondary",
    "thinkingMinimal": "primary",
    "thinkingLow": "#00aaff",
    "thinkingMedium": "#00ffff",
    "thinkingHigh": "#ff00ff",
    "thinkingXhigh": "#ff0000",
    "bashMode": "#ffaa00"
  }
}
```

3. Select via `/settings`.

> [!tip] Hot reload: editing the currently active custom theme file reloads it automatically for immediate visual feedback.

## Theme Format

```json
{
  "$schema": "https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/src/modes/interactive/theme/theme-schema.json",
  "name": "my-theme",
  "vars": {
    "blue": "#0066cc",
    "gray": 242
  },
  "colors": {
    "accent": "blue",
    "muted": "gray",
    "text": "",
    ...
  }
}
```

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Unique theme name |
| `vars` | No | Reusable color definitions referenced in `colors` |
| `colors` | Yes | All 51 tokens |
| `$schema` | No | Enables editor auto-completion and validation |

## Color Tokens

### Core UI (11)

| Token | Purpose |
|-------|---------|
| `accent` | Primary accent (logo, selected items, cursor) |
| `border` | Normal borders |
| `borderAccent` | Highlighted borders |
| `borderMuted` | Subtle borders (editor) |
| `success` | Success states |
| `error` | Error states |
| `warning` | Warning states |
| `muted` | Secondary text |
| `dim` | Tertiary text |
| `text` | Default text (usually `""`) |
| `thinkingText` | Thinking block text |

### Backgrounds & Content (11)

| Token | Purpose |
|-------|---------|
| `selectedBg` | Selected line background |
| `userMessageBg` | User message background |
| `userMessageText` | User message text |
| `customMessageBg` | Extension message background |
| `customMessageText` | Extension message text |
| `customMessageLabel` | Extension message label |
| `toolPendingBg` | Tool box (pending) |
| `toolSuccessBg` | Tool box (success) |
| `toolErrorBg` | Tool box (error) |
| `toolTitle` | Tool title |
| `toolOutput` | Tool output text |

### Markdown (10)

| Token | Purpose |
|-------|---------|
| `mdHeading` | Headings |
| `mdLink` | Link text |
| `mdLinkUrl` | Link URL |
| `mdCode` | Inline code |
| `mdCodeBlock` | Code block content |
| `mdCodeBlockBorder` | Code block fences |
| `mdQuote` | Blockquote text |
| `mdQuoteBorder` | Blockquote border |
| `mdHr` | Horizontal rule |
| `mdListBullet` | List bullets |

### Tool Diffs (3)

| Token | Purpose |
|-------|---------|
| `toolDiffAdded` | Added lines |
| `toolDiffRemoved` | Removed lines |
| `toolDiffContext` | Context lines |

### Syntax Highlighting (9)

| Token | Purpose |
|-------|---------|
| `syntaxComment` | Comments |
| `syntaxKeyword` | Keywords |
| `syntaxFunction` | Function names |
| `syntaxVariable` | Variables |
| `syntaxString` | Strings |
| `syntaxNumber` | Numbers |
| `syntaxType` | Types |
| `syntaxOperator` | Operators |
| `syntaxPunctuation` | Punctuation |

### Thinking Level Borders (6)

Border colors indicating thinking level (subtle to prominent):

| Token | Purpose |
|-------|---------|
| `thinkingOff` | Thinking off |
| `thinkingMinimal` | Minimal thinking |
| `thinkingLow` | Low thinking |
| `thinkingMedium` | Medium thinking |
| `thinkingHigh` | High thinking |
| `thinkingXhigh` | Extra high thinking |

### Bash Mode (1)

| Token | Purpose |
|-------|---------|
| `bashMode` | Editor border in bash mode (`!` prefix) |

### HTML Export (optional)

The `export` section controls `/export` HTML output. If omitted, colors derive from `userMessageBg`.

```json
{
  "export": {
    "pageBg": "#18181e",
    "cardBg": "#1e1e24",
    "infoBg": "#3c3728"
  }
}
```

## Color Values

| Format | Example | Description |
|--------|---------|-------------|
| Hex | `"#ff0000"` | 6-digit hex RGB |
| 256-color | `39` | xterm 256-color palette index (0-255) |
| Variable | `"primary"` | Reference to a `vars` entry |
| Default | `""` | Terminal's default color |

### 256-Color Palette

- `0-15`: Basic ANSI colors (terminal-dependent)
- `16-231`: 6x6x6 RGB cube (`16 + 36*R + 6*G + B` where R,G,B are 0-5)
- `232-255`: Grayscale ramp

### Terminal Compatibility

Pi uses 24-bit RGB colors. Most modern terminals support this (iTerm2, Kitty, WezTerm, Windows Terminal, VS Code). For 256-color-only terminals, pi falls back to nearest approximation.

```bash
echo $COLORTERM  # Should output "truecolor" or "24bit"
```

## Tips

- **Dark terminals:** Use bright, saturated colors with higher contrast.
- **Light terminals:** Use darker, muted colors with lower contrast.
- **Color harmony:** Start with a base palette (Nord, Gruvbox, Tokyo Night), define in `vars`, reference consistently.
- **Testing:** Check with different message types, tool states, markdown content, and long wrapped text.
- **VS Code:** Set `terminal.integrated.minimumContrastRatio` to `1` for accurate colors.

## Examples

Built-in themes:
- [dark.json](../src/modes/interactive/theme/dark.json)
- [light.json](../src/modes/interactive/theme/light.json)

#theming #json-configuration #ui-customization #color-palette #terminal-interface
