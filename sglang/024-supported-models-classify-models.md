---
title: Classification API — SGLang
url: https://docs.sglang.io/supported_models/classify_models.html
source: crawler
fetched_at: 2026-02-04T08:47:07.634435427-03:00
rendered_js: false
word_count: 400
summary: This document describes the implementation and usage of the SGLang /v1/classify API, which provides a vLLM-compatible interface for text classification and reward modeling.
tags:
    - sglang
    - classification-api
    - vllm-compatibility
    - text-classification
    - rest-api
    - machine-learning
category: api
---

## Contents

## Classification API[#](#classification-api "Link to this heading")

This document describes the `/v1/classify` API endpoint implementation in SGLang, which is compatible with vLLM’s classification API format.

## Overview[#](#overview "Link to this heading")

The classification API allows you to classify text inputs using classification models. This implementation follows the same format as vLLM’s 0.7.0 classification API.

## API Endpoint[#](#api-endpoint "Link to this heading")

## Request Format[#](#request-format "Link to this heading")

```
{
"model":"model_name",
"input":"text to classify"
}
```

### Parameters[#](#parameters "Link to this heading")

- `model` (string, required): The name of the classification model to use
- `input` (string, required): The text to classify
- `user` (string, optional): User identifier for tracking
- `rid` (string, optional): Request ID for tracking
- `priority` (integer, optional): Request priority

## Response Format[#](#response-format "Link to this heading")

```
{
"id":"classify-9bf17f2847b046c7b2d5495f4b4f9682",
"object":"list",
"created":1745383213,
"model":"jason9693/Qwen2.5-1.5B-apeach",
"data":[
{
"index":0,
"label":"Default",
"probs":[0.565970778465271,0.4340292513370514],
"num_classes":2
}
],
"usage":{
"prompt_tokens":10,
"total_tokens":10,
"completion_tokens":0,
"prompt_tokens_details":null
}
}
```

### Response Fields[#](#response-fields "Link to this heading")

- `id`: Unique identifier for the classification request
- `object`: Always “list”
- `created`: Unix timestamp when the request was created
- `model`: The model used for classification
- `data`: Array of classification results
  
  - `index`: Index of the result
  - `label`: Predicted class label
  - `probs`: Array of probabilities for each class
  - `num_classes`: Total number of classes
- `usage`: Token usage information
  
  - `prompt_tokens`: Number of input tokens
  - `total_tokens`: Total number of tokens
  - `completion_tokens`: Number of completion tokens (always 0 for classification)
  - `prompt_tokens_details`: Additional token details (optional)

## Example Usage[#](#example-usage "Link to this heading")

### Using curl[#](#using-curl "Link to this heading")

```
curl-v"http://127.0.0.1:8000/v1/classify"\
-H"Content-Type: application/json"\
-d'{
    "model": "jason9693/Qwen2.5-1.5B-apeach",
    "input": "Loved the new café—coffee was great."
  }'
```

### Using Python[#](#using-python "Link to this heading")

```
importrequests
importjson

# Make classification request
response = requests.post(
    "http://127.0.0.1:8000/v1/classify",
    headers={"Content-Type": "application/json"},
    json={
        "model": "jason9693/Qwen2.5-1.5B-apeach",
        "input": "Loved the new café—coffee was great."
    }
)

# Parse response
result = response.json()
print(json.dumps(result, indent=2))
```

## Supported Models[#](#supported-models "Link to this heading")

The classification API works with any classification model supported by SGLang, including:

### Classification Models (Multi-class)[#](#classification-models-multi-class "Link to this heading")

- `LlamaForSequenceClassification` - Multi-class classification
- `Qwen2ForSequenceClassification` - Multi-class classification
- `Qwen3ForSequenceClassification` - Multi-class classification
- `BertForSequenceClassification` - Multi-class classification
- `Gemma2ForSequenceClassification` - Multi-class classification

**Label Mapping**: The API automatically uses the `id2label` mapping from the model’s `config.json` file to provide meaningful label names instead of generic class names. If `id2label` is not available, it falls back to `LABEL_0`, `LABEL_1`, etc., or `Class_0`, `Class_1` as a last resort.

### Reward Models (Single score)[#](#reward-models-single-score "Link to this heading")

- `InternLM2ForRewardModel` - Single reward score
- `Qwen2ForRewardModel` - Single reward score
- `LlamaForSequenceClassificationWithNormal_Weights` - Special reward model

**Note**: The `/classify` endpoint in SGLang was originally designed for reward models but now supports all non-generative models. Our `/v1/classify` endpoint provides a standardized vLLM-compatible interface for classification tasks.

## Error Handling[#](#error-handling "Link to this heading")

The API returns appropriate HTTP status codes and error messages:

- `400 Bad Request`: Invalid request format or missing required fields
- `500 Internal Server Error`: Server-side processing error

Error response format:

```
{
"error":"Error message",
"type":"error_type",
"code":400
}
```

## Implementation Details[#](#implementation-details "Link to this heading")

The classification API is implemented using:

1. **Rust Model Gateway**: Handles routing and request/response models in `sgl-model-gateway/src/protocols/spec.rs`
2. **Python HTTP Server**: Implements the actual endpoint in `python/sglang/srt/entrypoints/http_server.py`
3. **Classification Service**: Handles the classification logic in `python/sglang/srt/entrypoints/openai/serving_classify.py`

## Testing[#](#testing "Link to this heading")

Use the provided test script to verify the implementation:

```
pythontest_classify_api.py
```

## Compatibility[#](#compatibility "Link to this heading")

This implementation is compatible with vLLM’s classification API format, allowing seamless migration from vLLM to SGLang for classification tasks.