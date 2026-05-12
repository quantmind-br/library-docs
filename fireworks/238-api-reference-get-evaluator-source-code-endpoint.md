---
title: Get Evaluator Source Code Endpoint - Fireworks AI
url: https://docs.fireworks.ai/api-reference/get-evaluator-source-code-endpoint
source: sitemap
fetched_at: 2026-04-27T20:19:22.194689759-03:00
rendered_js: false
word_count: 61
summary: Retrieves a mapping of filenames to signed URLs for downloading the source code of an evaluator.
tags:
    - api-reference
    - evaluator
    - source-code
    - signed-url
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
GET `v1/accounts/{account_id}/evaluators/{evaluator_id}:getSourceCodeSignedUrl`

Retrieves a mapping of filenames to signed URLs for downloading the source code of an evaluator.

**Authorizations:** Bearer authentication using your Fireworks API key. Format: `Bearer <API_KEY>`

### Request

No body required.

### Response

| Field | Type | Description |
|---|---|---|
| `filenameToSignedUrls` | object | Mapping from filename to signed URL for downloading the source code |

```bash
curl --request GET \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/evaluators/{evaluator_id}:getSourceCodeSignedUrl \
  --header 'Authorization: Bearer <token>'
```

```json
{
  "filenameToSignedUrls": {}
}
```