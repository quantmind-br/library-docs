---
title: firectl batch-inference-job delete - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/batch-inference-job-delete
source: sitemap
fetched_at: 2026-04-27T20:18:00.811488557-03:00
rendered_js: false
word_count: 153
summary: This document describes the command available in firectl for deleting a batch inference job, providing syntax and detailing various associated flags.
tags:
    - firectl-command
    - batch-inference-job
    - delete
    - api-flags
    - cli-tool
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# firectl batch-inference-job delete

Delete a batch inference job.

```
firectl batch-inference-job delete [flags]
```

## Examples

```bash
firectl batch-inference-job delete my-batch-job
firectl batch-inference-job delete accounts/my-account/batchInferenceJobs/my-batch-job
```

## Flags

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--dry-run` | | | Print the request proto without running it |
| `-h, --help` | | | help for delete |
| `-o, --output` | Output | `text` | Set the output format to `text`, `json`, or `flag` |
| `--wait` | | | Wait until the batch inference job is deleted |
| `--wait-timeout` | duration | `30m0s` | Maximum time to wait when using `--wait` flag |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. If not specified, reads from `~/.fireworks/auth.ini` |
| `--api-key` | string | API key used to authenticate with Fireworks |
| `-p, --profile` | string | Fireworks auth and settings profile to use |

#firectl #batch-inference-job #delete #command-line #reference
