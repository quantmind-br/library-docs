---
title: Get Evaluator Build Log Endpoint - Fireworks AI
url: https://docs.fireworks.ai/api-reference/get-evaluator-build-log-endpoint
source: sitemap
fetched_at: 2026-04-27T20:19:20.128039138-03:00
rendered_js: false
word_count: 55
summary: Retrieves a short-lived signed URL for downloading the build log of an evaluator.
tags:
    - api-reference
    - evaluator
    - logs
    - build
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
GET `v1/accounts/{account_id}/evaluators/{evaluator_id}:getBuildLogEndpoint`

Retrieves a short-lived signed URL for downloading the build log of an evaluator.

**Authorizations:** Bearer authentication using your Fireworks API key. Format: `Bearer <API_KEY>`

### Request

No body required.

### Response

| Field | Type | Description |
|---|---|---|
| `buildLogSignedUri` | string | Short-lived signed URL for the build log file |

```bash
curl --request GET \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/evaluators/{evaluator_id}:getBuildLogEndpoint \
  --header 'Authorization: Bearer <token>'
```

```json
{
  "buildLogSignedUri": "<string>"
}
```