---
title: "ForgeCode Services Overview"
url: https://forgecode.dev/docs/forge-services/
source: sitemap
fetched_at: 2026-04-30T14:09:07.674858535-03:00
rendered_js: false
word_count: 152
summary: "ForgeCode Services provides runtime capabilities like context management, tool-call guardrails, and skill selection."
tags:
  - runtime-layer
  - context-engine
  - tool-call-guardrails
  - project-indexing
  - agent-configuration
category: guide
optimized: true
---
# ForgeCode Services Overview

> **TL;DR**
> Runtime layer for context, tool-call safety, and skill selection. Enable once, runs in the background.

## Core Capabilities

| Feature | Benefit |
|---------|---------|
| **Context Engine** | 93% fewer tokens, faster retrieval |
| **Tool-Call Guardrails** | Auto-corrects invalid arguments |
| **Skill Engine** | Applies task-specific guidance |

## Setup

1. **Enable Services**:
   ```bash
   :login
   ```
   Select **ForgeServices** and authenticate (Google/GitHub).

2. **Index Project**:
   ```bash
   :sync
   ```
   Enables `sem_search` and project context.

3. **Monitor Progress**:
   ```bash
   :status
   ```

## Configuration
- **No API key required** (browser auth only).
- **Ignored files**: Excluded from sync and retrieval. See [Ignoring Files](https://forgecode.dev/docs/ignoring-files/).

## Commands

| Command | Action |
|---------|--------|
| `:login` | Enable services |
| `:sync` | Index project |
| `:status` | Check sync progress |
| `:logout` | Disable services |

## Verification
- Check for `sem_search` under `SYSTEM` in `:tools`.
- Files ignored via `.gitignore` or [Ignoring Files](https://forgecode.dev/docs/ignoring-files/) are excluded.