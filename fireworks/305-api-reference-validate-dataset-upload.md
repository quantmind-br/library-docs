---
title: Validate Dataset Upload
url: https://docs.fireworks.ai/api-reference/validate-dataset-upload
source: sitemap
fetched_at: 2026-04-27T20:13:27.360579076-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - reference
category: reference
word_count: 29
---
# Validate Dataset Upload

Validates that a dataset upload completed successfully. Returns an empty `{}` on success.

## Endpoint

```
POST /v1/accounts/{account_id}/datasets/{dataset_id}:validateUpload
```

## Request

```bash
curl --request POST \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/datasets/{dataset_id}:validateUpload \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{}'
```

## Authorization

Bearer token — format: `Bearer <API_KEY>`