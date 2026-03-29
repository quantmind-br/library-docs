---
title: Cron - OpenClaw
url: https://docs.openclaw.ai/cli/cron
source: sitemap
fetched_at: 2026-01-30T20:36:10.950799967-03:00
rendered_js: false
word_count: 41
summary: This document explains how to manage cron jobs for the Gateway scheduler using command-line operations, including editing job delivery settings and disabling deliveries.
tags:
    - cron-jobs
    - gateway-scheduler
    - command-line
    - task-management
    - automation
category: reference
---

## [​](#openclaw-cron) `openclaw cron`

Manage cron jobs for the Gateway scheduler. Related:

- Cron jobs: [Cron jobs](https://docs.openclaw.ai/automation/cron-jobs)

Tip: run `openclaw cron --help` for the full command surface.

## [​](#common-edits) Common edits

Update delivery settings without changing the message:

```
openclaw cron edit <job-id> --deliver --channel telegram --to "123456789"
```

Disable delivery for an isolated job:

```
openclaw cron edit <job-id> --no-deliver
```