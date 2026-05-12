---
title: firectl dpo-job resume
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/dpo-job-resume
source: sitemap
fetched_at: 2026-04-27T20:17:47.097825019-03:00
rendered_js: false
word_count: 86
summary: Resume a stopped DPO job.
tags:
  - command-line
  - firectl
  - dpo-job
  - resume
  - flags
  - reference
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# firectl dpo-job resume

Resume a stopped or failed DPO (Direct Preference Optimization) job.

## Usage

```bash
firectl dpo-job resume [flags]
```

## Examples

```bash
firectl dpo-job resume my-dpo-job
firectl dpo-job resume accounts/my-account/dpoJobs/my-dpo-job
```

## Flags

| Flag | Type | Description |
|------|------|-------------|
| `-h, --help` | | Help for resume. |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if unset. |
| `--api-key` | string | API key for authentication. |
| `-p, --profile` | string | Auth and settings profile to use. |
