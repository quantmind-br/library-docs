---
title: Skills - OpenClaw
url: https://docs.openclaw.ai/platforms/mac/skills
source: sitemap
fetched_at: 2026-01-30T20:26:34.407538111-03:00
rendered_js: false
word_count: 113
summary: This document explains how the macOS OpenClaw application interfaces with the gateway to manage skills, including installation, configuration, and environment variables.
tags:
    - macos
    - skills-management
    - gateway-communication
    - installation
    - configuration
    - environment-variables
category: guide
---

## Skills (macOS)

The macOS app surfaces OpenClaw skills via the gateway; it does not parse skills locally.

## Data source

- `skills.status` (gateway) returns all skills plus eligibility and missing requirements (including allowlist blocks for bundled skills).
- Requirements are derived from `metadata.openclaw.requires` in each `SKILL.md`.

## Install actions

- `metadata.openclaw.install` defines install options (brew/node/go/uv).
- The app calls `skills.install` to run installers on the gateway host.
- The gateway surfaces only one preferred installer when multiple are provided (brew when available, otherwise node manager from `skills.install`, default npm).

## Env/API keys

- The app stores keys in `~/.openclaw/openclaw.json` under `skills.entries.<skillKey>`.
- `skills.update` patches `enabled`, `apiKey`, and `env`.

## Remote mode

- Install + config updates happen on the gateway host (not the local Mac).