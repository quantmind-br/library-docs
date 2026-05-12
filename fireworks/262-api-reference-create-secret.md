---
title: Create Secret
url: https://docs.fireworks.ai/api-reference/create-secret
source: sitemap
fetched_at: 2026-04-27T20:14:59.045187654-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - bearer-authentication
    - path-parameters
    - body-data
    - response-structure
    - secret-value
    - api-key
category: reference
word_count: 70
---
Creates a secret via the Fireworks API.

#### Authorizations

Bearer authentication using your Fireworks API key. Format: `Bearer <API_KEY>`

#### Body

| Field | Type | Description |
|-------|------|-------------|
| `secret` | string | The secret value. **INPUT_ONLY** — not returned in GET or LIST responses for security. |

#### Response

| Field | Type | Description |
|-------|------|-------------|
| `secret` | string | The secret value (echoed back). |
