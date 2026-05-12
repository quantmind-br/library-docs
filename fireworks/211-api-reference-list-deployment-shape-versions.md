---
title: List Deployment Shapes Versions - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/list-deployment-shape-versions
source: sitemap
fetched_at: 2026-04-27T20:13:57.344732333-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - deployment-shape
    - versioning
    - metadata
    - model-configuration
    - ai-deployment
category: reference
word_count: 63
---
# List Deployment Shapes Versions

`GET /deployment_shape_versions` — Returns a paginated list of deployment shape versions.

## Response Schema

```json
{
  "deploymentShapeVersions": [
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
  ],
  "nextPageToken": "<string>",
  "totalSize": 123
}
```

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `deploymentShapeVersions` | array | List of deployment shape version objects. |
| `nextPageToken` | string | Token for fetching the next page. |
| `totalSize` | integer | Total number of versions. |