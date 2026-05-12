---
title: firectl user update - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/user-update
source: sitemap
fetched_at: 2026-04-27T20:16:05.570877723-03:00
rendered_js: false
word_count: 162
summary: This document describes the command structure and available flags for updating a user via the 'firectl' interface.
tags:
    - command-line
    - user-management
    - firectl
    - update
    - flags
    - api-interaction
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# firectl user update

Update a user's display name, role, or permission settings.

```
firectl user update [flags]
```

## Examples

```bash
firectl user update my-user --display-name="Alice Cullen"
firectl user update accounts/my-account/users/my-user --display-name="Alice Cullen"
firectl user update my-agent --permission-preset=agent
```

## Flags

| Flag | Type | Description |
|------|------|-------------|
| `--display-name` | string | The display name of the user |
| `--dry-run` | | Print the request proto without running it |
| `-o, --output` | Output | Set the output format to `text`, `json`, or `flag` (default `text`) |
| `--permission-preset` | string | Permission preset for the service account. Automatically sets role to `custom` |
| `--role` | string | The role of the user. Must be one of `{user, admin, contributor, inference-user, custom}` |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. If not specified, reads from `~/.fireworks/auth.ini` |
| `--api-key` | string | API key used to authenticate with Fireworks |
| `-p, --profile` | string | Fireworks auth and settings profile to use |

#firectl #user-management #command-line #reference
