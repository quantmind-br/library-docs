---
title: Guides Batch Inference
url: https://docs.fireworks.ai/guides/batch-inference
source: sitemap
fetched_at: 2026-04-27T20:17:06.682132881-03:00
rendered_js: false
word_count: 67
summary: This document outlines the specific requirements for datasets to be used in batch processing, stipulating that they must adhere to the JSONL format and include certain mandatory fields.
tags:
    - dataset-requirements
    - jsonl-format
    - batch-input
    - required-fields
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Batch datasets must be in JSONL format. Each line is a valid JSON object.

## Requirements

| Field | Description |
|-------|-------------|
| `custom_id` | Unique identifier for each request |
| `body` | Request parameters (same as chat completion API) |
| **File size** | Under 1GB |

## Example dataset

```jsonl
{"custom_id": "request-1", "body": {"messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "What is the capital of France?"}], "max_tokens": 100}}
{"custom_id": "request-2", "body": {"messages": [{"role": "user", "content": "Explain quantum computing"}], "temperature": 0.7}}
{"custom_id": "request-3", "body": {"messages": [{"role": "user", "content": "Tell me a joke"}]}}
```

Save as `batch_input_data.jsonl` locally, then use the [Batch Inference API](https://docs.fireworks.ai/api-reference/create-batch-inference-job) to submit.

#batch-inference #dataset-requirements #jsonl
