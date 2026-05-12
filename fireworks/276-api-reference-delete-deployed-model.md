---
title: Delete Deployed Model - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/delete-deployed-model
source: sitemap
fetched_at: 2026-04-27T20:14:52.277367122-03:00
rendered_js: false
word_count: 70
summary: Delete a deployed model associated with an account using the Fireworks API.
tags:
    - api-deletion
    - deployed-models
    - curl-command
    - fireworks-ai
    - bearer-token
    - delete-request
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Delete Deployed Model

Deletes a deployed model for an account.

#### Authorizations

Bearer authentication using your Fireworks API key. Format: `Bearer <API_KEY>`

#### Path Parameters

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| account_id | string | Yes | The Account Id. |
| deployed_model_id | string | Yes | The Deployed Model Id. |

#### Response

Returns an `object`.

#### Endpoint

```
DELETE /v1/accounts/{account_id}/deployedModels/{deployed_model_id}
```

#### Example

```bash
curl --request DELETE \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/deployedModels/{deployed_model_id} \
  --header 'Authorization: Bearer <token>'
```

#api-reference #deployed-models
