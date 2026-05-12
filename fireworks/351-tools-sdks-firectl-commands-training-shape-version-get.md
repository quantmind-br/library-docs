---
title: firectl training-shape-version get
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/training-shape-version-get
source: sitemap
fetched_at: 2026-04-27T20:16:21.656324296-03:00
rendered_js: false
word_count: 113
summary: This document describes the 'get' subcommand for the firectl training-shape-version command, detailing its usage syntax, available flags, and how global configuration options can be applied.
tags:
    - firectl
    - training-shape-version
    - get
    - flags
    - api-call
category: reference
optimized: true
optimized_at: 2026-04-27T20:16:21.656324296-03:00
---
# firectl training-shape-version get

Get a specific training shape version.

```bash
firectl training-shape-version get [flags]
```

## Examples

```bash
firectl training-shape-version get accounts/my-account/trainingShapes/my-shape/versions/my-version
firectl training-shape-version get accounts/my-account/trainingShapes/my-shape/versions/latest
```

## Flags

| Flag | Type | Description |
|------|------|-------------|
| `--dry-run` | | Print the request proto without running it. |
| `-h, --help` | | Help for get |
| `-o, --output` | Output | Output format: `text`, `json`, or `flag` (default: `text`) |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if not specified. |
| `--api-key` | string | API key for authentication. |
| `-p, --profile` | string | fireworks auth and settings profile to use. |

#firectl #training-shape-version #get #api-call
