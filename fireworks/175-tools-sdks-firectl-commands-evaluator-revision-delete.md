---
title: firectl evaluator-revision delete - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/evaluator-revision-delete
source: sitemap
fetched_at: 2026-04-27T20:17:36.341913069-03:00
rendered_js: false
word_count: 118
summary: This document describes the `firectl evaluator-revision delete` command, detailing its usage syntax and available flags for performing a revision deletion operation.
tags:
    - firectl
    - evaluator-revision
    - delete-command
    - api-client
    - flags
    - revision-management
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# firectl evaluator-revision delete

Delete an evaluator revision.

```
firectl evaluator-revision delete [flags]
```

## Examples

```bash
firectl evaluator-revision delete accounts/my-account/evaluators/my-evaluator/versions/abc123
```

## Flags

| Flag | Type | Description |
|------|------|-------------|
| `--dry-run` | | Print the request proto without running it |
| `-h, --help` | | help for delete |
| `-o, --output` | Output | Set the output format to `text`, `json`, or `flag` (default `text`) |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. If not specified, reads from `~/.fireworks/auth.ini` |
| `--api-key` | string | API key used to authenticate with Fireworks |
| `-p, --profile` | string | Fireworks auth and settings profile to use |

#firectl #evaluator-revision #delete #command-line #reference
