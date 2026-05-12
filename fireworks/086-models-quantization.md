---
title: Quantization - Fireworks AI Docs
url: https://docs.fireworks.ai/models/quantization
source: sitemap
fetched_at: 2026-04-27T20:18:08.70648387-03:00
rendered_js: false
word_count: 178
summary: This document explains how model quantization reduces computational requirements and cost by allowing different numerical precisions like FP16, FP8, and INT8. It provides instructions on checking available precisions, preparing a model for specific precisions (like FP8), and creating a deployment that utilizes the quantized checkpoint.
tags:
    - model-quantization
    - numerical-precision
    - fp8-optimization
    - api-usage
    - deployment-setup
    - fireworks-ai
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Quantization reduces the number of bits used to serve a model, improving performance and reducing cost by 30–50%. This can change model numerics and may introduce small changes to the output.

## Checking available precisions

Models may support different numerical precisions (FP16, FP8, BF16, INT8) which affect memory usage and inference speed.

**Check default precision:**
```bash
firectl model get accounts/fireworks/models/llama-v3p1-8b-instruct | grep "Default Precision"
```

**Check supported precisions:**
```bash
firectl model get accounts/fireworks/models/llama-v3p1-8b-instruct | grep -E "(Supported Precisions|Supported Precisions With Calibration)"
```

The `Precisions` field indicates what precisions the model has been prepared for.

## Quantizing a model

A model can be quantized to FP8 precision.

| Tool | Command |
|---|---|
| firectl | `firectl prepare-model <MODEL_ID>` |

```python
import os
import requests

ACCOUNT_ID = os.environ.get("FIREWORKS_ACCOUNT_ID")
API_KEY = os.environ.get("FIREWORKS_API_KEY")
MODEL_ID = "<YOUR_MODEL_ID>" # The ID of the model you want to prepare

response = requests.post(
  f"https://api.fireworks.ai/v1/accounts/{ACCOUNT_ID}/models/{MODEL_ID}:prepare",
  headers={
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
  },
  json={
    "precision": "FP8"
  }
)

print(response.json())
```

**Check preparation status:**

| Tool | Command |
|---|---|
| firectl | `firectl model get <MODEL_ID>` |

```python
import os
import requests

ACCOUNT_ID = os.environ.get("FIREWORKS_ACCOUNT_ID")
API_KEY = os.environ.get("FIREWORKS_API_KEY")
MODEL_ID = "<YOUR_MODEL_ID>" # The ID of the model you want to get

response = requests.get(
  f"https://api.fireworks.ai/v1/accounts/{ACCOUNT_ID}/models/{MODEL_ID}",
  headers={
    "Authorization": f"Bearer {API_KEY}"
  }
)

print(response.json())
```

A successfully prepared model will have the desired precision added to the `Precisions` list.

## Creating an FP8 deployment

By default, creating a deployment uses the FP16 checkpoint. To use a quantized FP8 checkpoint, first ensure the model has been [prepared for FP8](#checking-available-preisions), then pass the `--precision` flag:

| Tool | Command |
|---|---|
| firectl | `firectl deployment create <MODEL> --accelerator-type NVIDIA_H100_80GB --precision FP8` |

```python
import os
import requests

ACCOUNT_ID = os.environ.get("FIREWORKS_ACCOUNT_ID")
API_KEY = os.environ.get("FIREWORKS_API_KEY")
MODEL_ID = "<YOUR_MODEL_ID>" # The ID of the model you want to deploy. The model must be prepared for FP8 precision.
DEPLOYMENT_NAME = "My FP8 Deployment"

response = requests.post(
  f"https://api.fireworks.ai/v1/accounts/{ACCOUNT_ID}/deployments",
  headers={
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
  },
  json={
    "displayName": DEPLOYMENT_NAME,
    "baseModel": MODEL_ID,
    "acceleratorType": "NVIDIA_H100_80GB",
    "precision": "FP8",
  }
)

print(response.json())
```
