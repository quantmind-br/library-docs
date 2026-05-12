---
title: firectl evaluator-revision get
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/evaluator-revision-get
source: sitemap
fetched_at: 2026-04-27T20:17:34.288065444-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - cli-command
    - evaluator
category: reference
word_count: 90
---
Retrieve a specific revision (version) of an evaluator.

```bash
firectl evaluator-revision get [flags]
```

### Example

```bash
firectl evaluator-revision get accounts/my-account/evaluators/my-evaluator/versions/latest
```

### Flags

| Flag | Description |
|------|-------------|
| `--dry-run` | Print the request proto without executing |
| `-h, --help` | Help for get |
| `-o, --output` | Output format: `text`, `json`, or `flag` (default: `text`) |

### Global Flags

| Flag | Description |
|------|-------------|
| `-a, --account-id` | Fireworks account ID (reads from `~/.fireworks/auth.ini` if unset) |
| `--api-key` | API key for authentication |
| `-p, --profile` | Auth and settings profile to use |
