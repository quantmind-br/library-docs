---
title: "null"
url: https://docs.clawd.bot/cli/skills.md
source: llms
fetched_at: 2026-01-26T09:51:02.387809275-03:00
rendered_js: false
word_count: 51
summary: This document details the command-line interface for inspecting and managing ClawdBot skills, including listing eligible skills and checking requirements.
tags:
    - clawdbot-cli
    - skills-management
    - command-line-interface
    - debugging-skills
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