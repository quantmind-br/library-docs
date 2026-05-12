---
title: firectl training-shape-version update
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/training-shape-version-update
source: sitemap
fetched_at: 2026-04-27T20:16:25.087774733-03:00
rendered_js: false
word_count: 122
summary: This document provides command-line reference details for the `firectl training-shape-version update` command, detailing available flags and their functions.
tags:
    - cli-command
    - training-shape-version
    - update
    - flags
    - fireworks
    - api
category: reference
optimized: true
optimized_at: 2026-04-27T20:16:25.087774733-03:00
---
# firectl training-shape-version update

Update a training shape version.

```bash
firectl training-shape-version update [flags]
```

## Examples

```bash
firectl training-shape-version update accounts/my-account/trainingShapes/my-shape/versions/my-version --public=true
```

## Flags

| Flag | Type | Description |
|------|------|-------------|
| `--dry-run` | | Print the request proto without running it. |
| `-h, --help` | | Help for update |
| `-o, --output` | Output | Output format: `text`, `json`, or `flag` (default: `text`) |
| `--public` | | Set the version as public. |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if not specified. |
| `--api-key` | string | API key for authentication. |
| `-p, --profile` | string | fireworks auth and settings profile to use. |

#cli-command #training-shape-version #update #firectl
