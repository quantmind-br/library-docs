---
title: firectl supervised-fine-tuning-job delete - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/supervised-fine-tuning-job-delete
source: sitemap
fetched_at: 2026-04-27T20:17:16.720079231-03:00
rendered_js: false
word_count: 137
summary: This document describes the 'delete' command for managing supervised fine-tuning jobs within the firectl CLI tool. It details how to execute the deletion and lists available flags to control the operation.
tags:
    - firectl-cli
    - supervised-fine-tuning
    - job-deletion
    - command-reference
    - api-interaction
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Delete a supervised fine-tuning job.

```bash
firectl supervised-fine-tuning-job delete [flags]
```

## Examples

```bash
firectl supervised-fine-tuning-job delete my-sft-job
firectl supervised-fine-tuning-job delete accounts/my-account/supervisedFineTuningJobs/my-sft-job
```

## Flags

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--dry-run` | bool | | Print the request proto without running it |
| `-h, --help` | | | help for delete |
| `-o, --output` | string | `text` | Output format: `text`, `json`, or `flag` |
| `--wait` | bool | | Wait until the job is deleted |
| `--wait-timeout` | duration | `30m0s` | Maximum time to wait when using `--wait` |

## Global flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID (defaults to `~/.fireworks/auth.ini`) |
| `--api-key` | string | API key for authentication |
| `-p, --profile` | string | fireworks auth and settings profile to use |

#firectl-cli #supervised-fine-tuning #command-reference
