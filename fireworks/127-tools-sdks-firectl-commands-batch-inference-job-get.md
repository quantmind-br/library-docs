---
title: firectl batch-inference-job get
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/batch-inference-job-get
source: sitemap
fetched_at: 2026-04-27T20:18:04.491567788-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - cli-command
    - batch-inference
category: reference
word_count: 90
---
Retrieve details for a specific batch inference job.

```bash
firectl batch-inference-job get [flags]
```

### Examples

```bash
firectl batch-inference-job get my-batch-job
firectl batch-inference-job get accounts/my-account/batchInferenceJobs/my-batch-job
```

### Flags

| Flag | Description |
|------|-------------|
| `--dry-run` | Print the request proto without executing |
| `-h, --help` | Help for get |
| `-o, --output` | Output format: `text`, `json`, or `flag` (default: `text`) |

### Global Flags

| Flag | Description |
|------|-------------|
| `-a, --account-id` | Fireworks account ID (reads from `~/.fireworks/auth.ini` if unset) |
| `--api-key` | API key for authentication |
| `-p, --profile` | Auth and settings profile to use |
