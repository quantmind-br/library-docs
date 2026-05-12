---
title: firectl dpo-job export-metrics
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/dpo-job-export-metrics
source: sitemap
fetched_at: 2026-04-27T20:17:45.93977673-03:00
rendered_js: false
word_count: 104
summary: Export metrics for a DPO job to a file.
tags:
  - cli
  - command
  - dpo-job
  - export-metrics
  - fireworks
  - metrics
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# firectl dpo-job export-metrics

Export training metrics for a DPO (Direct Preference Optimization) job to a local file.

## Usage

```bash
firectl dpo-job export-metrics [flags]
```

## Examples

```bash
firectl dpo-job export-metrics my-dpo-job
firectl dpo-job export-metrics accounts/my-account/dpoJobs/my-dpo-job
```

## Flags

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--filename` | string | `"metrics.jsonl"` | Output file name. |
| `-h, --help` | | | Help for export-metrics. |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if unset. |
| `--api-key` | string | API key for authentication. |
| `-p, --profile` | string | Auth and settings profile to use. |
