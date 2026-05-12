---
title: Deployments - Fireworks AI Docs
url: https://docs.fireworks.ai/guides/ondemand-deployments
source: sitemap
fetched_at: 2026-04-27T20:18:27.936577051-03:00
rendered_js: false
word_count: 246
summary: This document explains the advantages of using on-demand GPU deployments over serverless options and provides comprehensive instructions, commands, and code examples for creating, querying, and managing these deployments.
tags:
    - on-demand-deployments
    - gpu-management
    - deployment-creation
    - api-usage
    - fireworks-sdk
    - scaling-configuration
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# On-Demand Deployments

On-demand deployments provide dedicated GPUs for your models with lower latency, higher throughput, predictable performance, no hard rate limits, and cost savings at scale. They are [billed by GPU-second](https://fireworks.ai/pricing) and offer access to models not available on serverless, including custom models from Hugging Face.

Need higher GPU quotas or reserved capacity? [Contact us](https://fireworks.ai/contact).

## Creating & Querying Deployments

Create a deployment and save the returned `accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>` identifier:

```bash
firectl deployment create accounts/fireworks/models/<MODEL_NAME> --wait
```

Query your deployment using that identifier (e.g., `accounts/alice/deployments/12345678`).

### Code Examples

- Python (Fireworks SDK)
- Python (OpenAI SDK)
- JavaScript
- curl

```python
from fireworks import Fireworks

client = Fireworks()

response = client.chat.completions.create(
  model="accounts/fireworks/models/gpt-oss-120b#<DEPLOYMENT_NAME>",
  messages=[{"role": "user", "content": "Explain quantum computing in simple terms"}]
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
    model="accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>",
    messages=[{"role": "user", "content": "Explain quantum computing in simple terms"}]
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
  model: "accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>",
  messages: [
    {
      role: "user",
      content: "Explain quantum computing in simple terms",
    },
  ],
});

console.log(response.choices[0].message.content);
```

```bash
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -d '{
    "model": "accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>",
    "messages": [
      {
        "role": "user",
        "content": "Explain quantum computing in simple terms"
      }
    ]
  }'
```

## Deployment Shapes

Deployment shapes are pre-configured templates for speed, cost, or efficiency optimization:

| Shape | Use Case |
|-------|----------|
| Fast | Low latency for interactive workloads |
| Throughput | Cost-per-token at scale for high-volume workloads |
| Minimal | Lowest cost for testing or light workloads |

```bash
# List available shapes
firectl deployment-shape-version list --base-model <model-id>

# Create with a shape (shorthand)
firectl deployment create accounts/fireworks/models/deepseek-v3 --deployment-shape throughput

# Create with full shape ID
firectl deployment create accounts/fireworks/models/llama-v3p3-70b-instruct \
  --deployment-shape accounts/fireworks/deploymentShapes/llama-v3p3-70b-instruct-fast

# View shape details
firectl deployment-shape-version get <full-deployment-shape-version-id>
```

## Managing & Configuring Deployments

### Basic Management

```bash
# List all deployments
firectl deployment list

# Check deployment status
firectl deployment get <DEPLOYMENT_ID>

# Delete a deployment
firectl deployment delete <DEPLOYMENT_ID>
```

### GPU Hardware

Choose GPU type with `--accelerator-type`:

- `NVIDIA_A100_80GB`
- `NVIDIA_H100_80GB`
- `NVIDIA_H200_141GB`

### Autoscaling

Control replica counts, scale timing, and load targets. See [[025-deployments-autoscaling]] for configuration options.

### Multiple GPUs per Replica

```bash
firectl deployment create <MODEL_NAME> --accelerator-count 2
```

Scaling is sub-linear (2x GPUs ≠ 2x performance).

## Advanced Topics

- [[032-deployments-speculative-decoding]] — Speed up text generation using draft models or n-gram speculation
- [[086-models-quantization]] — Reduce model precision (e.g., FP16 to FP8) to improve speeds and reduce costs by 30–50%
- [[026-deployments-benchmarking]] — Measure and optimize your deployment's performance with load testing

#on-demand-deployments #gpu-management #deployment-creation #api-usage #fireworks-sdk #scaling-configuration
