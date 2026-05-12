---
title: firectl quota update - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/quota-update
source: sitemap
fetched_at: 2026-04-27T20:17:26.750072597-03:00
rendered_js: false
word_count: 141
summary: Update a resource quota value within Fireworks for serverless inference, RPM, or TPM limits.
tags:
    - command-line
    - quota-update
    - flags
    - fireworks
    - serverless-inference
    - api
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# firectl quota update

Update the allowed quota value for a resource.

```bash
firectl quota update [flags]
```

## Positional Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `quota` | string | Quota resource name (e.g. `serverless-inference-rpm`) |

## Flags

| Flag | Type | Description |
|------|------|-------------|
| `--dry-run` | flag | Print the request proto without running it |
| `--value` | int | New quota value. Must be less than `max_value` |
| `-o, --output` | Output | Output format: `text`, `json`, or `flag` (default `text`) |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if unset |
| `--api-key` | string | API key for authentication |
| `-p, --profile` | string | Auth and settings profile to use |

## Examples

```bash
firectl quota update serverless-inference-rpm --value 300
```

#firectl #quota #update #cli
