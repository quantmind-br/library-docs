---
title: firectl rlor-trainer-job delete
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/rlor-trainer-job-delete
source: sitemap
fetched_at: 2026-04-27T20:16:43.436805279-03:00
rendered_js: false
word_count: 142
summary: Delete an rlor trainer job by ID or full resource name.
tags:
    - command-line
    - rlor-trainer-job
    - delete
    - flags
    - fireworks
    - api
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Delete an rlor trainer job by ID or full resource name.

```bash
firectl rlor-trainer-job delete [flags]
```

## Examples

```bash
firectl rlor-trainer-job delete my-rlor-job
firectl rlor-trainer-job delete accounts/my-account/rlorTrainerJobs/my-rlor-job
```

## Flags

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--dry-run` | bool | | Print the request proto without running it. |
| `-h`, `--help` | | | help for delete |
| `-o`, `--output` | Output | `text` | Output format: `text`, `json`, or `flag`. |
| `--wait` | bool | | Wait until the rlor trainer job is deleted. |
| `--wait-timeout` | duration | `30m0s` | Maximum time to wait when using `--wait`. |

## Global flags

| Flag | Type | Description |
|------|------|-------------|
| `-a`, `--account-id` | string | Fireworks account ID. Defaults to `~/.fireworks/auth.ini`. |
| `--api-key` | string | API key for authentication. |
| `-p`, `--profile` | string | fireworks auth and settings profile to use. |
