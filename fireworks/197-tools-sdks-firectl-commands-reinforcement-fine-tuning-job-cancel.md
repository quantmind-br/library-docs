---
title: firectl reinforcement-fine-tuning-job cancel - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/reinforcement-fine-tuning-job-cancel
source: sitemap
fetched_at: 2026-04-27T20:17:20.467601047-03:00
rendered_js: false
word_count: 49
summary: This document describes the `firectl reinforcement-fine-tuning-job cancel` command, which is used to terminate a specific Reinforcement Fine Tuning job.
tags:
    - cli-command
    - reinforcement-tuning
    - job-management
    - cancellation
    - fireworks
category: reference
optimized: true
optimized_at: 2026-04-27T20:44:11Z
---
```bash
firectl reinforcement-fine-tuning-job cancel [flags]
```

**Examples**

```bash
firectl reinforcement-fine-tuning-job cancel my-rftj
firectl reinforcement-fine-tuning-job cancel accounts/my-account/reinforcementFineTuningJobs/my-rftj
```

| Global Flag | Type | Description |
|-------------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if unset. |
| `--api-key` | string | API key for authentication. |
| `-p, --profile` | string | fireworks auth and settings profile to use. |