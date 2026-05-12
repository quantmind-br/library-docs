---
title: firectl billing export-metrics
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/billing-export-metrics
source: sitemap
fetched_at: 2026-04-27T20:17:58.584933757-03:00
rendered_js: false
word_count: 110
summary: Export billing metrics to a CSV file.
tags:
    - billing-export
    - cli-command
    - fireworks
    - metrics-extraction
    - flags
    - time-range
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Export billing metrics to a CSV file.

```bash
firectl billing export-metrics [flags]
```

## Examples

```bash
firectl billing export-metrics
```

## Flags

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--end-time` | string | | End time (exclusive). |
| `--filename` | string | `billing_metrics.csv` | Output file name. |
| `-h`, `--help` | | | help for export-metrics |
| `--start-time` | string | | Start time (inclusive). |

## Global flags

| Flag | Type | Description |
|------|------|-------------|
| `-a`, `--account-id` | string | Fireworks account ID. Defaults to `~/.fireworks/auth.ini`. |
| `--api-key` | string | API key for authentication. |
| `-p`, `--profile` | string | fireworks auth and settings profile to use. |
