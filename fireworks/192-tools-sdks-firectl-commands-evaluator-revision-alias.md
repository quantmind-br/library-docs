---
title: firectl evaluator-revision alias
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/evaluator-revision-alias
source: sitemap
fetched_at: 2026-04-27T20:17:34.085834278-03:00
rendered_js: false
word_count: 88
summary: Set an alias for an evaluator revision.
tags:
  - firectl
  - evaluator-revision
  - alias
  - command-line
  - global-flags
  - authentication
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# firectl evaluator-revision alias

Assign an alias (e.g., `"current"`) to an evaluator revision for easy reference.

## Usage

```bash
firectl evaluator-revision alias [flags]
```

## Examples

```bash
firectl evaluator-revision alias accounts/my-account/evaluators/my-evaluator/versions/abc123 --alias-id current
```

## Flags

| Flag | Type | Description |
|------|------|-------------|
| `-h, --help` | | Help for alias. |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if unset. |
| `--api-key` | string | API key for authentication. |
| `-p, --profile` | string | Auth and settings profile to use. |
