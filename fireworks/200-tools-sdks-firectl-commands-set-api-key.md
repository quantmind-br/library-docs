---
title: firectl set-api-key - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/set-api-key
source: sitemap
fetched_at: 2026-04-27T20:17:12.35630791-03:00
rendered_js: false
word_count: 49
summary: This document provides the command syntax and options for the `firectl set-api-key` command, which is used to configure or set an API key for the Firectl tool.
tags:
    - command-line
    - api-key
    - configuration
    - flags
    - firectl
    - authentication
category: reference
optimized: true
optimized_at: 2026-04-27T20:44:11Z
---
```bash
firectl set-api-key [flags]
```

**Examples**

```bash
firectl set-api-key API_KEY
```

| Global Flag | Type | Description |
|-------------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if unset. |
| `--api-key` | string | API key for authentication. |
| `-p, --profile` | string | fireworks auth and settings profile to use. |