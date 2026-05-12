---
title: Accessibility | Warp
url: https://docs.warp.dev/terminal/more-features/accessibility
source: sitemap
fetched_at: 2026-04-29T15:03:02.424936664-03:00
rendered_js: false
word_count: 224
summary: This document provides an overview of the current accessibility features in the Warp terminal, including how to use VoiceOver, navigate the interface, and utilize voice input.
tags:
    - accessibility
    - voiceover
    - terminal-emulator
    - warp
    - assistive-technology
    - user-interface
category: guide
optimized: true
optimized_at: 2026-04-29T19:02:00Z
---
> [!warning]
> This is a work-in-progress. The current accessibility state is not final.

Warp aims to improve the terminal experience for visually impaired users, an area where other terminal emulators lack.

## VoiceOver setup

**Install via Homebrew** (recommended for automatic updates):
```bash
brew install warp
```

After installation:
1. Warp works seamlessly with VoiceOver — it announces screen content and available actions proactively
2. Log in and complete onboarding
3. Telemetry is sent to improve UX (see [privacy docs](https://docs.warp.dev/support-and-community/privacy-and-security/privacy))

> [!note]
> VoiceOver navigation between UI elements via VO key combinations is not yet available.

## Terminal layout

- **Command Input**: where you type commands
- **Blocks**: grouped command + output pairs
- **Command Palette**: access via `CMD-P` to discover features and actions

## Differences from standard VoiceOver workflow

Warp announces actions and state changes as they occur, rather than relying on traditional VO navigation. All features have assigned keybindings by default.

**Customize keybindings:** See [keysets repository](https://github.com/warpdotdev/keysets)

## Accessibility-specific settings

Access via [Command Palette](https://docs.warp.dev/terminal/command-palette):
- Adjust message verbosity (search "a11y")
- View feature keybindings

## Voice input

Alternative interaction via voice commands for issuing terminal commands, asking about usage, and performing multi-step operations.

**Enable:** **Settings** → **Agents** → **Warp Agent** → **Voice**

See [Voice documentation](https://docs.warp.dev/agent-platform/warp-agents/interacting-with-agents/voice) for details.

## Future work

New features undergo a11y review before release. Milestone: keyboard-based UI element navigation.

[Share feedback](https://docs.warp.dev/support-and-community/troubleshooting-and-support/sending-us-feedback)

#accessibility #voiceover #assistive-technology #user-interface
