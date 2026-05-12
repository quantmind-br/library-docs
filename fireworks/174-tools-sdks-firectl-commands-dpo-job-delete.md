---
title: firectl dpo-job delete - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/dpo-job-delete
source: sitemap
fetched_at: 2026-04-27T20:17:45.010422659-03:00
rendered_js: false
word_count: 151
summary: This document describes the `firectl dpo-job delete` command, detailing its usage along with available flags for various operations.
tags:
    - command-line
    - dpo-job-deletion
    - fireworks-cli
    - flags
    - dry-run
    - output
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# firectl dpo-job delete

Delete a DPO job.

```
firectl dpo-job delete [flags]
```

## Examples

```bash
firectl dpo-job delete my-dpo-job
firectl dpo-job delete accounts/my-account/dpoJobs/my-dpo-job
```

## Flags

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--dry-run` | | | Print the request proto without running it |
| `-h, --help` | | | help for delete |
| `-o, --output` | Output | `text` | Set the output format to `text`, `json`, or `flag` |
| `--wait` | | | Wait until the DPO job is deleted |
| `--wait-timeout` | duration | `30m0s` | Maximum time to wait when using `--wait` flag |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. If not specified, reads from `~/.fireworks/auth.ini` |
| `--api-key` | string | API key used to authenticate with Fireworks |
| `-p, --profile` | string | Fireworks auth and settings profile to use |

#firectl #dpo-job #delete #command-line #reference
