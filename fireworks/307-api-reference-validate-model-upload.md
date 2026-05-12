---
title: Validate Model Upload
url: https://docs.fireworks.ai/api-reference/validate-model-upload
source: sitemap
fetched_at: 2026-04-27T20:13:29.713778903-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - reference
category: reference
word_count: 88
---
# Validate Model Upload

Validates that a model upload completed successfully. Returns warnings if any validation checks failed.

## Endpoint

```
GET /v1/accounts/{account_id}/models/{model_id}:validateUpload
```

## Request

```bash
curl --request GET \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/models/{model_id}:validateUpload \
  --header 'Authorization: Bearer <token>'
```

## Authorization

Bearer token — format: `Bearer <API_KEY>`

## Query Parameters

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `skip_hf_config_validation` | boolean | `false` | Skip Hugging Face config validation. |
| `trust_remote_code` | boolean | `false` | Trust remote code when validating Hugging Face config. |
| `skip_tokenizer_validation` | boolean | `false` | Skip tokenizer and parameter name validation. |

## Response

```json
{
  "warnings": ["<string>"]
}
```