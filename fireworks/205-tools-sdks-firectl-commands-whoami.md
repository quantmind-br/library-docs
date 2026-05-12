---
title: firectl whoami - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/whoami
source: sitemap
fetched_at: 2026-04-27T20:17:08.770453818-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - command-line
    - arguments
    - authentication
    - account-id
    - api-key
    - profile
category: reference
word_count: 60
---
# firectl whoami

Displays the currently authenticated Fireworks account.

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