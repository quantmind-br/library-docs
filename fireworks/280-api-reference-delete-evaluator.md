---
title: Delete Evaluator - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/delete-evaluator
source: sitemap
fetched_at: 2026-04-27T20:19:21.029095371-03:00
rendered_js: false
word_count: 110
summary: This document serves as an API reference detailing various endpoints for interacting with Fireworks AI services, covering sections like Inference, Deployments, Fine-tuning, and specifically providing detailed operations for managing evaluators.
tags:
    - api-reference
    - fireworks-ai
    - evaluator-management
    - inference
    - deployment
    - rest-api
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Delete Evaluator

Permanently delete an evaluator from an account.

## Endpoint

```
DELETE /v1/accounts/{account_id}/evaluators/{evaluator_id}
```

## Authorizations

| Type | Location | Description |
|------|----------|-------------|
| Bearer | `Authorization` header | Fireworks API key. Format: `Bearer <API_KEY>` |

## Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `account_id` | string | The Account ID |
| `evaluator_id` | string | The Evaluator ID |

## Response

Returns an `object`.

## Example

```bash
curl --request DELETE \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/evaluators/{evaluator_id} \
  --header 'Authorization: Bearer <token>'
```

## Related Operations

- [[001-api-reference-introduction|Introduction]] · [[094-tools-sdks-python-sdk|Python SDK]]
- [[258-api-reference-create-evaluator|Create Evaluator]] · [[215-api-reference-list-evaluators|List Evaluators]] · [[240-api-reference-get-evaluator|Get Evaluator]]
- [[239-api-reference-get-evaluator-upload-endpoint|Get Upload Endpoint]] · [[237-api-reference-get-evaluator-build-log-endpoint|Get Build Log Endpoint]] · [[238-api-reference-get-evaluator-source-code-endpoint|Get Source Code Endpoint]]
- [[268-api-reference-update-evaluator|Update Evaluator]] · [[306-api-reference-validate-evaluator-upload|Validate Upload]]

#evaluator-management #rest-api
