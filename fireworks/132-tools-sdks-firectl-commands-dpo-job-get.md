---
title: firectl dpo-job get
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/dpo-job-get
source: sitemap
fetched_at: 2026-04-27T20:17:47.264308744-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - cli-command
    - dpo-job
category: reference
word_count: 92
---
Retrieve details for a DPO (Direct Preference Optimization) fine-tuning job.

```bash
firectl dpo-job get [flags]
```

### Examples

```bash
firectl dpo-job get my-dpo-job
firectl dpo-job get accounts/my-account/dpoJobs/my-dpo-job
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
