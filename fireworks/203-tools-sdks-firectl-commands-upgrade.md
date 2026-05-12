---
title: firectl upgrade - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/upgrade
source: sitemap
fetched_at: 2026-04-27T20:17:11.714535461-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - command-line
    - options
    - account-id
    - api-key
    - profile
    - fireworks
category: reference
word_count: 62
---
# firectl upgrade

Updates the `firectl` CLI to the latest version.

## Options

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | The Fireworks account ID. Falls back to `~/.fireworks/auth.ini`. |
| `--api-key` | string | API key for authentication with Fireworks. |
| `-p, --profile` | string | fireworks auth and settings profile to use. |

```bash
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```