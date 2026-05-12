---
title: Get Deployment Shape - Fireworks AI
url: https://docs.fireworks.ai/api-reference/get-deployment-shape
source: sitemap
fetched_at: 2026-04-27T20:14:12.404219577-03:00
rendered_js: false
word_count: 193
summary: Response schema for the GET /accounts/{account_id}/deploymentShapes/{deployment_shape_id} endpoint.
tags:
    - api-reference
    - deployment-shapes
    - response-schema
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
GET `v1/accounts/{account_id}/deploymentShapes/{deployment_shape_id}`

## Response

| Field | Type | Description |
|---|---|---|
| `baseModel` | string | Base model identifier |
| `name` | string | Resource name |
| `displayName` | string | Display name |
| `description` | string | Description |
| `createTime` | string (RFC3339) | Creation timestamp |
| `updateTime` | string (RFC3339) | Last update timestamp |
| `modelType` | string | Model type |
| `parameterCount` | string | Parameter count |
| `acceleratorCount` | integer | Number of accelerators |
| `acceleratorType` | string | Accelerator type |
| `precision` | string | Precision setting |
| `disableDeploymentSizeValidation` | boolean | Disable size validation |
| `enableAddons` | boolean | Enable addons |
| `draftTokenCount` | integer | Draft token count |
| `draftModel` | string | Draft model |
| `ngramSpeculationLength` | integer | N-gram speculation length |
| `disableSpeculativeDecoding` | boolean | Disable speculative decoding |
| `enableSessionAffinity` | boolean | Enable session affinity |
| `numLoraDeviceCached` | integer | Number of LoRA devices cached |
| `maxContextLength` | integer | Max context length |
| `presetType` | string | Preset type |

```json
{
  "baseModel": "<string>",
  "name": "<string>",
  "displayName": "<string>",
  "description": "<string>",
  "createTime": "2023-11-07T05:31:56Z",
  "updateTime": "2023-11-07T05:31:56Z",
  "modelType": "<string>",
  "parameterCount": "<string>",
  "acceleratorCount": 123,
  "acceleratorType": "ACCELERATOR_TYPE_UNSPECIFIED",
  "precision": "PRECISION_UNSPECIFIED",
  "disableDeploymentSizeValidation": true,
  "enableAddons": true,
  "draftTokenCount": 123,
  "draftModel": "<string>",
  "ngramSpeculationLength": 123,
  "disableSpeculativeDecoding": true,
  "enableSessionAffinity": true,
  "numLoraDeviceCached": 123,
  "maxContextLength": 123,
  "presetType": "PRESET_TYPE_UNSPECIFIED"
}
```