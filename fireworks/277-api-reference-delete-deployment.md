---
title: Delete Deployment - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/delete-deployment
source: sitemap
fetched_at: 2026-04-27T20:14:53.313274058-03:00
rendered_js: false
word_count: 122
summary: Delete a specific deployment within an account using the Fireworks API.
tags:
    - api-delete
    - deployment-deletion
    - account-management
    - rest-endpoint
    - bearer-auth
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Delete Deployment

Deletes a deployment for an account. Supports optional hard deletion and force deletion flags.

#### Authorizations

Bearer authentication using your Fireworks API key. Format: `Bearer <API_KEY>`

#### Path Parameters

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| account_id | string | Yes | The Account Id. |
| deployment_id | string | Yes | The Deployment Id. |

#### Query Parameters

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| hard_delete | boolean | false | If true, performs a hard deletion. |
| force | boolean | false | If true, ignores checks and forces deletion of a deployed, in-use deployment. |

#### Response

Returns an `object`.

#### Endpoint

```
DELETE /v1/accounts/{account_id}/deployments/{deployment_id}
```

#### Example

```bash
curl --request DELETE \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/deployments/{deployment_id} \
  --header 'Authorization: Bearer <token>'
```

#api-reference #deployments
