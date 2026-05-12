---
title: firectl dpo-job cancel
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/dpo-job-cancel
source: sitemap
fetched_at: 2026-04-27T20:17:40.852495302-03:00
rendered_js: false
word_count: 114
summary: Stop a running DPO job.
tags:
  - command
  - dpo-job
  - cancel
  - firesctrl
  - flag
  - job-management
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# firectl dpo-job cancel

Stop a running DPO (Direct Preference Optimization) job.

## Usage

```bash
firectl dpo-job cancel [flags]
```

## Examples

```bash
firectl dpo-job cancel my-dpo-job
firectl dpo-job cancel accounts/my-account/dpoJobs/my-dpo-job
```

## Flags

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--wait` | | | Block until the job is cancelled. |
| `--wait-timeout` | duration | `10m0s` | Maximum time to wait when using `--wait`. |
| `-h, --help` | | | Help for cancel. |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if unset. |
| `--api-key` | string | API key for authentication. |
| `-p, --profile` | string | Auth and settings profile to use. |
