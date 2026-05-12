---
title: firectl deployment undelete
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/deployment-undelete
source: sitemap
fetched_at: 2026-04-27T20:17:43.972200898-03:00
rendered_js: false
word_count: 112
summary: Restore a deleted deployment.
tags:
  - firectl
  - deployment
  - undelete
  - cli-command
  - flags
  - fireworks
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# firectl deployment undelete

Restore a previously deleted deployment.

## Usage

```bash
firectl deployment undelete [flags]
```

## Examples

```bash
firectl deployment undelete my-deployment
```

## Flags

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--wait` | | | Block until the deployment is fully restored. |
| `--wait-timeout` | duration | `1h0m0s` | Maximum time to wait when using `--wait`. |
| `-h, --help` | | | Help for undelete. |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if unset. |
| `--api-key` | string | API key for authentication. |
| `-p, --profile` | string | Auth and settings profile to use. |
