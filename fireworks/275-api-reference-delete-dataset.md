---
title: Delete Dataset - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/delete-dataset
source: sitemap
fetched_at: 2026-04-27T20:14:53.627209958-03:00
rendered_js: false
word_count: 68
summary: Delete a specific dataset associated with an account using the Fireworks API.
tags:
    - api-delete
    - dataset-management
    - fireworks-ai
    - rest-api
    - account-id
    - bearer-token
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Delete Dataset

Deletes a specific dataset for an account.

#### Authorizations

Bearer authentication using your Fireworks API key. Format: `Bearer <API_KEY>`

#### Path Parameters

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| account_id | string | Yes | The Account Id. |
| dataset_id | string | Yes | The Dataset Id. |

#### Response

Returns an `object`.

#### Endpoint

```
DELETE /v1/accounts/{account_id}/datasets/{dataset_id}
```

#### Example

```bash
curl --request DELETE \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/datasets/{dataset_id} \
  --header 'Authorization: Bearer <token>'
```

#api-reference #datasets
