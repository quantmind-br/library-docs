---
title: Update Model
url: https://docs.fireworks.ai/api-reference/update-model
source: sitemap
fetched_at: 2026-04-27T20:13:35.473943637-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - model-metadata
    - ai-specification
    - deployment-details
    - llm-config
    - tunable-parameters
    - model-attributes
category: reference
word_count: 4
---
Model metadata response schema.

```json
{
  "name": "<string>",
  "displayName": "<string>",
  "description": "<string>",
  "createTime": "2023-11-07T05:31:56Z",
  "state": "STATE_UNSPECIFIED",
  "status": {
    "code": "OK",
    "message": "<string>"
  },
  "kind": "KIND_UNSPECIFIED",
  "githubUrl": "<string>",
  "huggingFaceUrl": "<string>",
  "baseModelDetails": {
    "worldSize": 123,
    "checkpointFormat": "CHECKPOINT_FORMAT_UNSPECIFIED",
    "huggingfaceFiles": ["<string>"],
    "parameterCount": "<string>",
    "moe": true,
    "tunable": true,
    "modelType": "<string>",
    "supportsFireattention": true,
    "defaultPrecision": "PRECISION_UNSPECIFIED",
    "supportsMtp": true
  },
  "peftDetails": {
    "baseModel": "<string>",
    "r": 123,
    "targetModules": ["<string>"],
    "baseModelType": "<string>",
    "mergeAddonModelName": "<string>"
  },
  "teftDetails": {},
  "public": true,
  "conversationConfig": {
    "style": "<string>",
    "system": "<string>",
    "template": "<string>"
  },
  "contextLength": 123,
  "supportsImageInput": true,
  "supportsTools": true,
  "importedFrom": "<string>",
  "fineTuningJob": "<string>",
  "defaultDraftModel": "<string>",
  "defaultDraftTokenCount": 123,
  "deployedModelRefs": [
    {
      "name": "<string>",
      "deployment": "<string>",
      "state": "STATE_UNSPECIFIED",
      "default": true,
      "public": true
    }
  ],
  "cluster": "<string>",
  "deprecationDate": {
    "year": 123,
    "month": 123,
    "day": 123
  },
  "calibrated": true,
  "tunable": true,
  "supportsLora": true,
  "useHfApplyChatTemplate": true,
  "updateTime": "2023-11-07T05:31:56Z",
  "defaultSamplingParams": {},
  "rlTunable": true,
  "trainingContextLength": 123,
  "snapshotType": "FULL_SNAPSHOT",
  "supportsServerless": true,
  "supervisedLoraTunable": true,
  "supervisedFullParameterTunable": true,
  "rlLoraTunable": true,
  "rlFullParameterTunable": true
}
```
