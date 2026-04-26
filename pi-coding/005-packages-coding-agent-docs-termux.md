---
title: Termux
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/termux.md
source: git
fetched_at: 2026-04-26T05:48:33.487255529-03:00
rendered_js: false
word_count: 409
summary: This document provides instructions for installing and configuring the Pi coding agent within the Termux terminal emulator on Android.
tags:
    - termux
    - android
    - linux-environment
    - setup-guide
    - mobile-development
    - cli-tools
category: guide
optimized: true
optimized_at: 2026-04-26T09:00:00Z
---

# Termux (Android) Setup

Pi runs on Android via [Termux](https://termux.dev/), a terminal emulator and Linux environment.

## Prerequisites

1. Install [Termux](https://github.com/termux/termux-app#installation) from GitHub or F-Droid (not Google Play — deprecated)
2. Install [Termux:API](https://github.com/termux/termux-api#installation) from GitHub or F-Droid for clipboard and device integrations

## Installation

```bash
# Update packages
pkg update && pkg upgrade

# Install dependencies
pkg install nodejs termux-api git

# Install pi
npm install -g @mariozechner/pi-coding-agent

# Create config directory
mkdir -p ~/.pi/agent

# Run pi
pi
```

## Clipboard Support

Clipboard operations use `termux-clipboard-set` / `termux-clipboard-get`. The Termux:API app must be installed.

> [!warning] Image clipboard is not supported on Termux (`ctrl+v` image paste will not work).

## Example AGENTS.md for Termux

Create `~/.pi/agent/AGENTS.md`:

```markdown
# Agent Environment: Termux on Android

## Location
- **OS**: Android (Termux terminal emulator)
- **Home**: `/data/data/com.termux/files/home`
- **Prefix**: `/data/data/com.termux/files/usr`
- **Shared storage**: `/storage/emulated/0` (Downloads, Documents, etc.)

## Opening URLs
```bash
termux-open-url "https://example.com"
```

## Opening Files
```bash
termux-open file.pdf          # Opens with default app
termux-open -c image.jpg      # Choose app
```

## Clipboard
```bash
termux-clipboard-set "text"   # Copy
termux-clipboard-get          # Paste
```

## Notifications
```bash
termux-notification -t "Title" -c "Content"
```

## Device Info
```bash
termux-battery-status         # Battery info
termux-wifi-connectioninfo    # WiFi info
termux-telephony-deviceinfo   # Device info
```

## Sharing
```bash
termux-share -a send file.txt # Share file
```

## Other Useful Commands
```bash
termux-toast "message"        # Quick toast popup
termux-vibrate                # Vibrate device
termux-tts-speak "hello"      # Text to speech
termux-camera-photo out.jpg   # Take photo
```

## Notes
- Termux:API app must be installed for `termux-*` commands
- Use `pkg install termux-api` for the command-line tools
- Storage permission needed for `/storage/emulated/0` access
```

## Limitations

- **No image clipboard** — Termux clipboard API only supports text
- **No native binaries** — Some optional native dependencies (e.g., clipboard module) are unavailable on Android ARM64 and skipped during installation
- **Storage access** — Run `termux-setup-storage` once to grant permissions for `/storage/emulated/0`

## Troubleshooting

**Clipboard not working** — ensure both apps are installed (Termux + Termux:API from GitHub/F-Droid), then:

```bash
pkg install termux-api
```

**Permission denied for shared storage** — grant once:

```bash
termux-setup-storage
```

**Node.js installation issues** — clear cache:

```bash
npm cache clean --force
```

#termux #android #setup-guide
