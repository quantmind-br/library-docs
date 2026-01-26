---
title: "null"
url: https://docs.clawd.bot/reference/templates/TOOLS.md
source: llms
fetched_at: 2026-01-26T09:53:45.73892595-03:00
rendered_js: false
word_count: 109
summary: This document explains how to use a local notes file to store environment-specific configurations like device names and SSH hosts separately from shared tool logic.
tags:
    - environment-setup
    - configuration-management
    - local-notes
    - documentation-standards
    - device-mapping
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.clawd.bot/llms.txt
> Use this file to discover all available pages before exploring further.

# null

# TOOLS.md - Local Notes

Skills define *how* tools work. This file is for *your* specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

* Camera names and locations
* SSH hosts and aliases
* Preferred voices for TTS
* Speaker/room names
* Device nicknames
* Anything environment-specific

## Examples

```markdown  theme={null}
### Cameras
- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH
- home-server → 192.168.1.100, user: admin

### TTS
- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

***

Add whatever helps you do your job. This is your cheat sheet.