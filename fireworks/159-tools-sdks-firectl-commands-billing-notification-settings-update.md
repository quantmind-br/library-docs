---
title: firectl billing notification-settings update - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/billing-notification-settings-update
source: sitemap
fetched_at: 2026-04-27T20:16:58.238151739-03:00
rendered_js: false
word_count: 127
summary: Update billing notification settings to manage spend alert thresholds.
tags:
    - billing
    - notification-settings
    - update
    - command-line
    - flags
    - thresholds
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# firectl billing notification-settings update

Update billing spend alert thresholds.

```bash
firectl billing notification-settings update [flags]
```

## Flags

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--dry-run` | flag | — | Print the request proto without running it |
| `--monthly-spend-usd-thresholds` | int64Slice | `[]` | Spend alert thresholds in whole USD (e.g. `500,800`). Use `""` to clear |
| `-o, --output` | Output | `text` | Output format: `text`, `json`, or `flag` |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if unset |
| `--api-key` | string | API key for authentication |
| `-p, --profile` | string | Auth and settings profile to use |

## Examples

```bash
firectl billing notification-settings update --monthly-spend-usd-thresholds=500,800

firectl billing notification-settings update --monthly-spend-usd-thresholds=500 --monthly-spend-usd-thresholds=800

firectl billing notification-settings update --monthly-spend-usd-thresholds=""
```

#billing #notifications #firectl #spend-alerts
