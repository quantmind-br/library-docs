---
title: firectl reinforcement-fine-tuning-job update - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/reinforcement-fine-tuning-job-update
source: sitemap
fetched_at: 2026-04-27T20:16:40.23487539-03:00
rendered_js: false
word_count: 161
summary: Update a reinforcement fine-tuning job's configuration including accelerator type and toleration.
tags:
    - command
    - reinforcement-fine-tuning-job
    - update
    - flags
    - cli
    - fireworks
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# firectl reinforcement-fine-tuning-job update

Update a reinforcement fine-tuning job's configuration.

```bash
firectl reinforcement-fine-tuning-job update [flags]
```

> [!info]
> The `firectl-admin rftj update` alias is available for admin operations.

## Positional Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `job` | string | Job name or resource name |

## Flags

| Flag | Type | Description |
|------|------|-------------|
| `--dry-run` | flag | Print the request proto without running it |
| `--training-accelerator-type` | string | Accelerator type for training (e.g. `NVIDIA_B200_180GB`) |
| `--toleration` | string | Toleration label (e.g. `fireworks.ai/rftj`) |
| `-o, --output` | Output | Output format: `text`, `json`, or `flag` (default `text`) |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if unset |
| `--api-key` | string | API key for authentication |
| `-p, --profile` | string | Auth and settings profile to use |

## Examples

```bash
firectl-admin rftj update my-job --training-accelerator-type=NVIDIA_B200_180GB

firectl-admin rftj update accounts/my-account/reinforcementFineTuningJobs/my-job --training-accelerator-type=NVIDIA_B200_180GB --toleration=fireworks.ai/rftj
```

#firectl #reinforcement-fine-tuning #rft #update #cli
