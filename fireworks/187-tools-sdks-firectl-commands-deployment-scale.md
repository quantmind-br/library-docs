---
title: firectl deployment scale
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/deployment-scale
source: sitemap
fetched_at: 2026-04-27T20:17:51.740816796-03:00
rendered_js: false
word_count: 102
summary: Change the replica count of a deployment.
tags:
  - deployment-scale
  - firectl
  - replica-count
  - fireworks
  - command-line
  - flags
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# firectl deployment scale

Set the desired number of replicas for a deployment.

## Usage

```bash
firectl deployment scale [flags]
```

## Examples

```bash
firectl deployment scale my-deployment --replica-count=3
firectl deployment scale accounts/my-account/deployments/my-deployment --replica-count=3
```

## Flags

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--replica-count` | int32 | | Desired number of replicas. Must be non-negative. |
| `-h, --help` | | | Help for scale. |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if unset. |
| `--api-key` | string | API key for authentication. |
| `-p, --profile` | string | Auth and settings profile to use. |
