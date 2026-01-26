---
title: "null"
url: https://docs.clawd.bot/platforms/mac/skills.md
source: llms
fetched_at: 2026-01-26T10:14:38.52933322-03:00
rendered_js: false
word_count: 135
summary: This document explains how the macOS application manages and installs Clawdbot skills through gateway interactions and local configuration files. It covers data sources, installation protocols, and credential storage.
tags:
    - macos-app
    - skill-management
    - gateway-api
    - configuration-storage
    - installation-process
category: reference
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.clawd.bot/llms.txt
> Use this file to discover all available pages before exploring further.

# null

# Skills (macOS)

The macOS app surfaces Clawdbot skills via the gateway; it does not parse skills locally.

## Data source

* `skills.status` (gateway) returns all skills plus eligibility and missing requirements
  (including allowlist blocks for bundled skills).
* Requirements are derived from `metadata.clawdbot.requires` in each `SKILL.md`.

## Install actions

* `metadata.clawdbot.install` defines install options (brew/node/go/uv).
* The app calls `skills.install` to run installers on the gateway host.
* The gateway surfaces only one preferred installer when multiple are provided
  (brew when available, otherwise node manager from `skills.install`, default npm).

## Env/API keys

* The app stores keys in `~/.clawdbot/clawdbot.json` under `skills.entries.<skillKey>`.
* `skills.update` patches `enabled`, `apiKey`, and `env`.

## Remote mode

* Install + config updates happen on the gateway host (not the local Mac).