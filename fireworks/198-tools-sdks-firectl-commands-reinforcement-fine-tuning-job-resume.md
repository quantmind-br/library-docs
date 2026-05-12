---
title: firectl reinforcement-fine-tuning-job resume - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/reinforcement-fine-tuning-job-resume
source: sitemap
fetched_at: 2026-04-27T20:17:25.505379719-03:00
rendered_js: false
word_count: 49
summary: This document provides documentation for the 'firectl reinforcement-fine-tuning-job resume' command, detailing how to execute it with various flags and showing examples of its usage.
tags:
    - command
    - reinforcement-fine-tuning
    - resume
    - flags
    - cli
    - fireworks
category: reference
optimized: true
optimized_at: 2026-04-27T20:44:11Z
---
```bash
firectl reinforcement-fine-tuning-job resume [flags]
```

**Examples**

```bash
firectl reinforcement-fine-tuning-job resume my-rftj
firectl reinforcement-fine-tuning-job resume accounts/my-account/reinforcementFineTuningJobs/my-rftj
```

| Global Flag | Type | Description |
|-------------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if unset. |
| `--api-key` | string | API key for authentication. |
| `-p, --profile` | string | fireworks auth and settings profile to use. |