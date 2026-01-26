---
title: "null"
url: https://docs.clawd.bot/cli/skills.md
source: llms
fetched_at: 2026-01-26T10:12:31.212903467-03:00
rendered_js: false
word_count: 51
summary: This document explains how to use the clawdbot skills CLI command to inspect, list, and verify the eligibility of bundled and workspace skill modules.
tags:
    - clawdbot-cli
    - skills-management
    - cli-commands
    - workspace-skills
    - dependency-checking
category: reference
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.clawd.bot/llms.txt
> Use this file to discover all available pages before exploring further.

# null

# `clawdbot skills`

Inspect skills (bundled + workspace + managed overrides) and see what’s eligible vs missing requirements.

Related:

* Skills system: [Skills](/tools/skills)
* Skills config: [Skills config](/tools/skills-config)
* ClawdHub installs: [ClawdHub](/tools/clawdhub)

## Commands

```bash  theme={null}
clawdbot skills list
clawdbot skills list --eligible
clawdbot skills info <name>
clawdbot skills check
```