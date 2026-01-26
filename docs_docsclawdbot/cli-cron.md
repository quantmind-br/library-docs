---
title: "null"
url: https://docs.clawd.bot/cli/cron.md
source: llms
fetched_at: 2026-01-26T10:12:06.326088325-03:00
rendered_js: false
word_count: 61
summary: This document explains how to use the clawdbot cron command-line tool to manage and modify scheduled jobs within the Gateway scheduler.
tags:
    - clawdbot-cli
    - cron-jobs
    - scheduling
    - automation
    - gateway-scheduler
category: reference
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.clawd.bot/llms.txt
> Use this file to discover all available pages before exploring further.

# null

# `clawdbot cron`

Manage cron jobs for the Gateway scheduler.

Related:

* Cron jobs: [Cron jobs](/automation/cron-jobs)

Tip: run `clawdbot cron --help` for the full command surface.

## Common edits

Update delivery settings without changing the message:

```bash  theme={null}
clawdbot cron edit <job-id> --deliver --channel telegram --to "123456789"
```

Disable delivery for an isolated job:

```bash  theme={null}
clawdbot cron edit <job-id> --no-deliver
```