---
title: Deploying Fine Tuned Models - Fireworks AI Docs
url: https://docs.fireworks.ai/fine-tuning/deploying-loras
source: sitemap
fetched_at: 2026-04-27T20:18:44.555209356-03:00
rendered_js: false
word_count: 153
summary: This document explains the methods for deploying fine-tuned LoRA models on Fireworks, detailing both single-LoRA (live merge) and multi-LoRA deployment strategies. It also provides examples of how to route inference requests to specific LoRA addons within a multi-LoRA setup using various SDKs and curl.
tags:
    - lora-deployment
    - single-lora
    - multi-lora
    - fireworks-ai
    - model-serving
    - inference-routing
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
After fine-tuning your model on Fireworks, deploy it to make it available for inference.

## Single-LoRA Deployment

Deploy your LoRA fine-tuned model with a single command that delivers performance matching the base model. This streamlined approach, called **live merge**, eliminates the previous two-step process and provides better performance than multi-LoRA deployments.

```bash
firectl deployment create "accounts/fireworks/models/<MODEL_ID of lora model>"
```

## Multi-LoRA Deployment

Share a single base model deployment across multiple LoRA models to achieve higher utilization. Use multi-LoRA when you:

- Need to serve multiple fine-tuned models based on the same base model
- Want to maximize deployment utilization
- Can accept a performance tradeoff vs. single-LoRA deployment
- Are managing multiple variants or experiments of the same model

### Deploy with CLI

```bash
firectl deployment create "accounts/fireworks/models/<MODEL_ID of base model>"
```

## Routing Requests to LoRA Addons

Set `model` to `<model_name>#<deployment_name>` to route inference requests to a specific LoRA addon on a multi-LoRA deployment. The `#` separator tells Fireworks to load the specified LoRA addon.

```python
from fireworks import Fireworks

client = Fireworks()
response = client.chat.completions.create(
    model="accounts/<ACCOUNT_ID>/models/<FINE_TUNED_MODEL_ID>#accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("FIREWORKS_API_KEY"),
    base_url="https://api.fireworks.ai/inference/v1"
)
response = client.chat.completions.create(
    model="accounts/<ACCOUNT_ID>/models/<FINE_TUNED_MODEL_ID>#accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
    apiKey: process.env.FIREWORKS_API_KEY,
    baseURL: "https://api.fireworks.ai/inference/v1",
});

const response = await client.chat.completions.create({
    model: "accounts/<ACCOUNT_ID>/models/<FINE_TUNED_MODEL_ID>#accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>",
    messages: [{"role": "user", "content": "Hello!"}],
});
console.log(response.choices[0].message.content);
```

```bash
curl https://api.fireworks.ai/inference/v1/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $FIREWORKS_API_KEY" \
    -d '{
        "model": "accounts/<ACCOUNT_ID>/models/<FINE_TUNED_MODEL_ID>#accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>",
        "messages": [{"role": "user", "content": "Hello!"}]
    }'
```

#lora-deployment #single-lora #multi-lora #inference-routing
