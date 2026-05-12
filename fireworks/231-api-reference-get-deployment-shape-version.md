---
title: Get Deployment Shape Version - Fireworks AI
url: https://docs.fireworks.ai/api-reference/get-deployment-shape-version
source: sitemap
fetched_at: 2026-04-27T20:14:10.201535218-03:00
rendered_js: false
word_count: 247
summary: Response schema for the GET /accounts/{account_id}/deploymentShapeVersions/{deployment_shape_version_id} endpoint.
tags:
    - api-reference
    - deployment-shapes
    - response-schema
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
GET `v1/accounts/{account_id}/deploymentShapeVersions/{deployment_shape_version_id}`

## Response

| Field | Type | Description |
|---|---|---|
| `name` | string | Resource name |
| `createTime` | string (RFC3339) | Creation timestamp |
| `snapshot` | object | Snapshot configuration |
| `snapshot.baseModel` | string | Base model identifier |
| `snapshot.name` | string | Snapshot name |
| `snapshot.displayName` | string | Display name |
| `snapshot.description` | string | Description |
| `snapshot.createTime` | string (RFC3339) | Snapshot creation time |
| `snapshot.updateTime` | string (RFC3339) | Snapshot update time |
| `snapshot.modelType` | string | Model type |
| `snapshot.parameterCount` | string | Parameter count |
| `snapshot.acceleratorCount` | integer | Number of accelerators |
| `snapshot.acceleratorType` | string | Accelerator type |
| `snapshot.precision` | string | Precision setting |
| `snapshot.disableDeploymentSizeValidation` | boolean | Disable size validation |
| `snapshot.enableAddons` | boolean | Enable addons |
| `snapshot.draftTokenCount` | integer | Draft token count |
| `snapshot.draftModel` | string | Draft model |
| `snapshot.ngramSpeculationLength` | integer | N-gram speculation length |
| `snapshot.disableSpeculativeDecoding` | boolean | Disable speculative decoding |
| `snapshot.enableSessionAffinity` | boolean | Enable session affinity |
| `snapshot.numLoraDeviceCached` | integer | Number of LoRA devices cached |
| `snapshot.maxContextLength` | integer | Max context length |
| `snapshot.presetType` | string | Preset type |
| `validated` | boolean | Whether validated |
| `public` | boolean | Whether publicly accessible |
| `latestValidated` | boolean | Whether the latest validated version |

```json
{
  "name": "<string>",
  "createTime": "2023-11-07T05:31:56Z",
  "snapshot": {
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
  },
  "validated": true,
  "public": true,
  "latestValidated": true
}
```