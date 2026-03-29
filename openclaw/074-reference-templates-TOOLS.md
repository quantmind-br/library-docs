---
title: TOOLS - OpenClaw
url: https://docs.openclaw.ai/reference/templates/TOOLS
source: sitemap
fetched_at: 2026-01-30T20:23:36.753034781-03:00
rendered_js: false
word_count: 87
summary: This document explains how to use a local notes file to store environment-specific configurations and personal tool settings separate from shared skills.
tags:
    - local-notes
    - tool-configuration
    - environment-setup
    - personal-settings
    - skill-separation
category: guide
---

## TOOLS.md - Local Notes

Skills define *how* tools work. This file is for *your* specifics — the stuff that’s unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```
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

* * *

Add whatever helps you do your job. This is your cheat sheet.