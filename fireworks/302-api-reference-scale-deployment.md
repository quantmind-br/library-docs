---
title: Scale Deployment to a specific number of replicas or to zero - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/scale-deployment
source: sitemap
fetched_at: 2026-04-27T20:13:39.278385588-03:00
rendered_js: false
word_count: 73
summary: This document describes the API endpoint used to scale a specific deployment within an account, allowing users to set it to a defined replica count or zero.
tags:
    - deployment-scaling
    - api-endpoint
    - replica-count
    - patch-request
    - fireworks-ai
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Scale Deployment to a specific number of replicas or to zero

Scales a deployment to a specified replica count (including zero for scale-to-zero).

## Endpoint

```
PATCH /v1/accounts/{account_id}/deployments/{deployment_id}:scale
```

## Authorization

Bearer authentication using your Fireworks API key. Format: `Bearer <API_KEY>`

## Request Body

| Field | Type | Description |
|-------|------|-------------|
| `replicaCount` | integer | Desired number of replicas. Set to 0 to scale to zero. |

## Response

Returns an `object`.

## Example

```bash
curl --request PATCH \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/deployments/{deployment_id}:scale \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "replicaCount": 123
}
'
```
