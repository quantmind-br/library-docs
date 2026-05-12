---
title: firectl rlor-trainer-job cancel - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/rlor-trainer-job-cancel
source: sitemap
fetched_at: 2026-04-27T20:16:41.002699476-03:00
rendered_js: false
word_count: 92
summary: This command provides a way to cancel an RLOR trainer job via the `firectl` interface. It allows users to specify options like waiting for cancellation and setting timeouts.
tags:
    - firectl
    - rlor-trainer-job
    - cancel
    - job-management
    - fireworks-cli
    - flags
category: reference
optimized: true
optimized_at: 2026-04-27T20:44:11Z
---
Cancels an RLOR trainer job.

```bash
firectl rlor-trainer-job cancel [flags]
```

**Examples**

```bash
firectl rlor-trainer-job cancel my-rlor-job
firectl rlor-trainer-job cancel accounts/my-account/rlorTrainerJobs/my-rlor-job
```

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--wait` | flag | — | Block until the job is cancelled. |
| `--wait-timeout` | duration | `10m0s` | Maximum time to wait with `--wait`. |

| Global Flag | Type | Description |
|-------------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if unset. |
| `--api-key` | string | API key for authentication. |
| `-p, --profile` | string | fireworks auth and settings profile to use. |