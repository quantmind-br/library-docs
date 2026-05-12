---
title: Terminal integrations | Warp
url: https://docs.warp.dev/terminal/integrations-and-plugins
source: sitemap
fetched_at: 2026-04-29T15:03:19.469410241-03:00
rendered_js: false
word_count: 180
summary: This document provides instructions for integrating the Warp terminal with external development tools including Docker, Raycast, VSCode, and JetBrains IDEs.
tags:
    - terminal-integration
    - ide-configuration
    - docker-extension
    - warp-terminal
    - macos-tools
    - productivity-shortcuts
category: guide
optimized: true
optimized_at: 2026-04-29T19:02:00Z
---
Warp integrates with Docker, Raycast, VSCode, and JetBrains IDEs for streamlined workflows.

> [!info]
> Docker, Raycast, and JetBrains integrations are macOS only.

## Docker

Install Warp's [Docker extension](https://hub.docker.com/extensions/warpdotdev/warp) to open containers in a Warpified subshell:

1. Select a container
2. Choose shell type (`bash`, `zsh`, or `fish`)
3. Optionally specify a user
4. Click "Open in Warp"

## Raycast

Open new windows, tabs, or launch configurations via Raycast.

> [!tip]
> In Raycast Settings → Extensions → Apps, search for Warp and assign alias "terminal" for quick access.

## VSCode

Press `SHIFT-CMD-C` in [VSCode](https://code.visualstudio.com/docs/terminal/basics) to open a Warp session.

**Configuration:**
1. VSCode Settings → search `Terminal › External: Osx Exec`
2. Set to `Warp.app` (or full path to executable)

## JetBrains IDEs

**Create external tool:**
1. Apple Menu → **Preferences** → **External Tools** → **Add**
   - *Name*: Open Warp
   - *Program*: `/Applications/Warp.app`
   - *Arguments*: `$ProjectFileDir$`
   - *Working Directory*: `/Applications`

**Add keyboard shortcut:**
1. Apple Menu → **Preferences** → **Keymap** → **External Tools**
2. Right-click "Open Warp" → **Add Keyboard Shortcut**
3. Enter desired shortcut

#terminal-integration #ide-configuration #docker-extension #macos-tools #productivity-shortcuts
