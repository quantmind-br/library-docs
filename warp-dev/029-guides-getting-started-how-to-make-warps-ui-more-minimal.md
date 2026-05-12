---
title: Make Warp's UI More Minimal | Guides | Warp
url: https://docs.warp.dev/guides/getting-started/how-to-make-warps-ui-more-minimal
source: sitemap
fetched_at: 2026-04-29T15:06:16.478456865-03:00
rendered_js: false
word_count: 255
summary: Declutter and simplify the Warp terminal interface by adjusting UI toggles, themes, prompt styles, and tab visibility.
tags:
    - terminal-customization
    - ui-optimization
    - warp-terminal
    - workflow-efficiency
    - interface-settings
    - minimalism
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
## 1. Start with the Command Palette

Open the Command Palette (`Cmd+P` / `Ctrl+Shift+P`), type "Disable" to see all UI toggles for hiding features and visual elements.

## 2. Key UI Toggles to Disable

**Inline & AI Features:**

- Disable Auto Suggestions — removes inline code hints
- Disable Active AI — hides the ghost prompt
- Disable Completion Menu — prevents popup completions
- Disable Voice Input — hides the microphone icon

**Interface & Layout:**

- Disable Block Dividers — removes horizontal lines between commands
- Disable Tab Indicators — hides colored status markers across the tab bar
- Disable Dimming Inactive Panes — keeps all split panes at equal brightness
- Disable VIM Status Bar — removes the VIM indicator when not using VIM mode

## 3. Choose a Simpler Theme

Visual noise comes from colors too. Open the Command Palette → type "Theme" → pick a calmer theme:

- **Adeberry** — calm, gray, minimal aesthetic
- **Classic Dark** — familiar and focused

## 4. Switch to the Classic Prompt

Warp's Universal Prompt supports slash commands, voice input, image context, and Agent Mode. To get a classic terminal feel:

1. Command Palette → search "Prompt" → choose **Classic Prompt**
2. (Optional) Open the Prompt Customizer to toggle chips — keep only what you need (e.g., file path), hide the rest

This instantly gives Warp a retro, text-first look.

## 5. Reduce Tab Bar Visibility

To make the tab bar appear only on hover:

1. **Settings → Appearance**
2. Enable **Show Tabs on Hover**
