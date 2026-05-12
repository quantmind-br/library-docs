---
title: Themes
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/themes.md
source: git
fetched_at: 2026-05-03T09:31:27.544922723-03:00
optimized: true
word_count: 669
summary: Create, configure, and customize pi terminal themes using JSON files with 51 required color tokens.
tags:
    - cli
    - theming
    - json-schema
    - customization
    - terminal-ui
    - syntax-highlighting
category: guide
---
# Themes

JSON files defining TUI colors.

> pi can create themes. Ask it to build one for your setup.

## Locations

| Source | Path |
|--------|------|
| Built-in | `dark`, `light` |
| Global | `~/.pi/agent/themes/*.json` |
| Project | `.pi/themes/*.json` |
| Packages | `themes/` directories or `pi.themes` in `package.json` |
| Settings | `themes` array in `settings.json` |
| CLI | `--theme <path>` (repeatable) |

Disable discovery: `--no-themes`

## Selection

Via `/settings` or `settings.json`:

```json
{ "theme": "my-theme" }
```

On first run, pi detects terminal background and defaults to `dark` or `light`.

## Creating a Theme

```bash
mkdir -p ~/.pi/agent/themes
vim ~/.pi/agent/themes/my-theme.json
```

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

> [!TIP]
> Hot reload: editing the active custom theme file reloads automatically.

## Color Tokens (51 Required)

### Core UI (11)

| Token | Purpose |
|-------|---------|
| `accent` | Primary accent (logo, selected, cursor) |
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

## Color Values

| Format | Example | Description |
|--------|---------|-------------|
| Hex | `"#ff0000"` | 6-digit RGB |
| 256-color | `39` | xterm palette index (0-255) |
| Variable | `"primary"` | Reference to `vars` entry |
| Default | `""` | Terminal default |

**256-color palette**:
- `0-15`: Basic ANSI (terminal-dependent)
- `16-231`: 6×6×6 RGB cube (`16 + 36×R + 6×G + B` where R,G,B are 0-5)
- `232-255`: Grayscale ramp

> [!NOTE]
> Pi uses 24-bit RGB. Falls back to nearest 256-color approximation. Check support with `echo $COLORTERM` (should be `truecolor` or `24bit`).

## HTML Export (Optional)

```json
{
  "export": {
    "pageBg": "#18181e",
    "cardBg": "#1e1e24",
    "infoBg": "#3c3728"
  }
}
```

If omitted, colors derived from `userMessageBg`.

## Tips

- **Dark terminals**: Bright, saturated colors with higher contrast
- **Light terminals**: Darker, muted colors with lower contrast
- **Color harmony**: Start with base palette (Nord, Gruvbox, Tokyo Night), define in `vars`, reference consistently
- **VS Code**: Set `terminal.integrated.minimumContrastRatio` to `1` for accurate colors

## Examples

Built-in themes:
- `dark.json` (`../src/modes/interactive/theme/dark.json`)
- `light.json` (`../src/modes/interactive/theme/light.json`)
