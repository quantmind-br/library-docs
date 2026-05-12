---
title: Get Model - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/get-model
source: sitemap
fetched_at: 2026-04-27T20:14:05.826048519-03:00
rendered_js: false
word_count: 146
summary: Returns the full model object schema including base model details, PEFT configuration, and deployment status.
tags:
    - model-metadata
    - ai-configuration
    - deployment-details
    - llm-specifications
    - peft
    - tunability
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Get Model

Returns the full model configuration object.

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

## Key Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Model identifier. |
| `displayName` | string | Human-readable name. |
| `baseModelDetails` | object | Base model architecture, PEFT support, MoE config. |
| `peftDetails` | object | PEFT (LoRA) configuration: `baseModel`, `r`, `targetModules`. |
| `public` | boolean | Whether the model is publicly available. |
| `contextLength` | integer | Maximum context length in tokens. |
| `supportsImageInput` | boolean | Vision capability. |
| `supportsTools` | boolean | Tool/function calling support. |
| `tunable` | boolean | Whether full-parameter fine-tuning is supported. |
| `supportsLora` | boolean | LoRA fine-tuning support. |
| `rlTunable` | boolean | RL fine-tuning support. |

> [!info]
> Schema for model objects including PEFT/TEFT configuration and deployment status. #model-metadata #ai-configuration #llm-specifications