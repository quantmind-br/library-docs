---
title: Migrate to Warp from iTerm2 | Warp
url: https://docs.warp.dev/getting-started/migrate-to-warp/migrate-to-warp-from-iterm2
source: sitemap
fetched_at: 2026-04-29T15:02:06.364123059-03:00
rendered_js: false
word_count: 469
summary: This document provides instructions for migrating terminal profiles and settings from iTerm2 to Warp, detailing what is automatically imported and which configurations require manual adjustment.
tags:
    - migration-guide
    - iterm2-import
    - terminal-configuration
    - warp-settings
    - user-onboarding
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Warp imports your iTerm2 profile automatically, bringing over theme, font, keybindings, hotkey window, and more in a few clicks. This page walks through the importer, what it covers, and what to reconfigure manually after.

## What transfers automatically

Warp ships a built-in iTerm2 importer that reads your default profile from `~/Library/Preferences/com.googlecode.iterm2.plist`. It imports:

- **Theme** — foreground, background, cursor, and all 16 ANSI colors (light and dark variants if configured)
- **Font** — family and size (when the font exists on your system and is supported by Warp)
- **Default shell** — if you've set a custom Command in your iTerm2 profile
- **Working directory behavior** — Warp translates iTerm2's "Reuse previous session's directory" and similar options
- **Window dimensions** — rows and columns
- **Opacity and blur**
- **Copy-on-select, mouse and scroll reporting, and Option-as-Meta settings**
- **Global hotkey** — if you use a hotkey window or hotkey activation, Warp maps it

To run the importer:

1. Search for **Import External Settings**.
2. Select **iTerm2 Profile: Default**. Warp only imports the profile marked as your Default Bookmark in iTerm2.
3. Choose which settings to keep or skip on the preview screen.

![Select a settings profile to import](https://docs.warp.dev/~gitbook/image?url=https%3A%2F%2F4009768362-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPsjNxoJ0NFCXW6rRdHH3%252Fuploads%252Fgit-blob-355fb38a9eca18812a736fe79f11c7ee142ec30f%252Fmigrate-to-warp.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=8a48ea8f&sv=2)

## Use Warp's agent for follow-up settings

If the importer doesn't pick up something you care about — a non-default profile, an unusual keybinding, a specific setting — ask Warp's agent to translate it directly. Warp ships a [`settings.toml` file](https://docs.warp.dev/terminal/settings) and a bundled `modify-settings` skill that lets the agent read your iTerm2 plist and write equivalent values into Warp's settings.

1. Paste a prompt like:

   > Read my iTerm2 preferences with `defaults read com.googlecode.iterm2` and port any settings that the importer didn't cover (extra profiles, custom keybindings) into my Warp `settings.toml` using the `modify-settings` skill. Show me a diff before applying.

2. Review the proposed diff and approve. Warp hot-reloads `settings.toml`.

## What to reconfigure manually

A few iTerm2 features don't map directly and need a manual pass after import:

| Feature | Warp Equivalent |
|---|---|
| Multiple profiles | [[023-getting-started-migrate-to-warp-migrate-to-warp-from-windows-terminal\|Tab configs]] |
| Keyboard shortcuts | [[016-getting-started-keyboard-shortcuts\|Settings → Keyboard shortcuts]] |
| Triggers | [[107-terminal-entry-yaml-workflows\|YAML workflows]] or Agent Mode |

After the import, choose which prompt to use:

1. [**Warp prompt**](https://docs.warp.dev/terminal/appearance/prompt#warp-prompt) — Warp's native prompt with drag-and-drop context chips for git branch, directory, timestamps, and more. Configure in **Settings** → **Appearance** → **Prompt**.
2. [**Shell prompt (PS1)**](https://docs.warp.dev/terminal/appearance/prompt#custom-prompt) — inherits your existing shell prompt configuration unchanged.

## Warp-native equivalents

| iTerm2 Feature | Warp Equivalent |
|---|---|
| Hotkey window (Quake mode) | [[249-terminal-windows-global-hotkey\|Global hotkey]] |
| Triggers | [[107-terminal-entry-yaml-workflows\|YAML workflows]] for repeatable actions; Agent Mode for pattern-based automation |
| Password manager integration | Native integration available |

For more on what you can configure after migrating, see the [[025-getting-started-quickstart|Warp quickstart]] and [[014-getting-started-customizing-warp|Customizing Warp]].

#migration-guide #iterm2-import #terminal-configuration #warp-settings #user-onboarding