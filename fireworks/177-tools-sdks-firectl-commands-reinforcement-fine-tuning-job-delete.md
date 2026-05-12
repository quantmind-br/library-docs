---
title: firectl reinforcement-fine-tuning-job delete
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/reinforcement-fine-tuning-job-delete
source: sitemap
fetched_at: 2026-04-27T20:17:18.398542308-03:00
rendered_js: false
word_count: 142
summary: Delete a reinforcement fine-tuning job by ID or full resource name.
tags:
    - command
    - reinforcement-fine-tuning-job
    - delete
    - firectl
    - flags
    - api
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Delete a reinforcement fine-tuning job by ID or full resource name.

```bash
firectl reinforcement-fine-tuning-job delete [flags]
```

## Examples

```bash
firectl reinforcement-fine-tuning-job delete my-rftj
firectl reinforcement-fine-tuning-job delete accounts/my-account/reinforcementFineTuningJobs/my-rftj
```

## Flags

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--dry-run` | bool | | Print the request proto without running it. |
| `-h`, `--help` | | | help for delete |
| `-o`, `--output` | Output | `text` | Output format: `text`, `json`, or `flag`. |
| `--wait` | bool | | Wait until the reinforcement fine-tuning job is deleted. |
| `--wait-timeout` | duration | `30m0s` | Maximum time to wait when using `--wait`. |

## Global flags

| Flag | Type | Description |
|------|------|-------------|
| `-a`, `--account-id` | string | Fireworks account ID. Defaults to `~/.fireworks/auth.ini`. |
| `--api-key` | string | API key for authentication. |
| `-p`, `--profile` | string | fireworks auth and settings profile to use. |
