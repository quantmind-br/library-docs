---
title: firectl supervised-fine-tuning-job cancel - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/supervised-fine-tuning-job-cancel
source: sitemap
fetched_at: 2026-04-27T20:17:14.740480359-03:00
rendered_js: false
word_count: 49
summary: This document describes the command `firectl supervised-fine-tuning-job cancel`, which is used to terminate an existing fine-tuning job managed via the firectl CLI.
tags:
    - cli
    - command
    - supervised-fine-tuning
    - job-management
    - cancel
category: reference
optimized: true
optimized_at: 2026-04-27T20:44:11Z
---
```bash
firectl supervised-fine-tuning-job cancel [flags]
```

**Examples**

```bash
firectl supervised-fine-tuning-job cancel my-sft-job
firectl supervised-fine-tuning-job cancel accounts/my-account/supervisedFineTuningJobs/my-sft-job
```

| Global Flag | Type | Description |
|-------------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if unset. |
| `--api-key` | string | API key for authentication. |
| `-p, --profile` | string | fireworks auth and settings profile to use. |