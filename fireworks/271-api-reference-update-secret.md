---
title: Update Secret - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/update-secret
source: sitemap
fetched_at: 2026-04-27T20:13:30.921635758-03:00
rendered_js: false
word_count: 101
summary: Update an existing secret's value using the Fireworks API.
tags:
    - bearer-authentication
    - api-key
    - path-parameters
    - input-only
    - request-response
    - secrets
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Update Secret

Updates the value of an existing secret. Only the `secret` field is accepted in the request body — it is `INPUT_ONLY` and will not be returned in GET or LIST responses.

#### Authorizations

Bearer authentication using your Fireworks API key. Format: `Bearer <API_KEY>`

#### Path Parameters

None

#### Body

| Field | Type | Description |
|-------|------|-------------|
| secret | string | The secret value. **INPUT_ONLY** — not returned in GET or LIST responses. |

**Example:** `"sk-1234567890abcdef"`

#### Response

The updated secret value (same as input — `INPUT_ONLY` field is not returned in responses).

**Example:** `"sk-1234567890abcdef"`

#api-reference #secrets
