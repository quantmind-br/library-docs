---
title: List Models - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/list-models
source: sitemap
fetched_at: 2026-04-27T20:13:51.316033137-03:00
rendered_js: false
word_count: 0
summary: This document provides a structured representation of machine learning model metadata, detailing various properties like creation time, status, base model configurations, and fine-tuning capabilities.
tags:
    - model-metadata
    - llm-config
    - ai-structure
    - model-details
    - parameter-count
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
```
{
  "models": [
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
        "huggingfaceFiles": [
          "<string>"
        ],
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
        "targetModules": [
          "<string>"
        ],
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
  ],
  "nextPageToken": "<string>",
  "totalSize": 123
}
```
