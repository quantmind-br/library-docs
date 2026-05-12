---
title: Deployments Quickstart
url: https://docs.fireworks.ai/getting-started/ondemand-quickstart
source: sitemap
fetched_at: 2026-04-27T20:18:34.287713224-03:00
rendered_js: false
word_count: 175
summary: This quickstart guide explains how to create and manage an on-demand deployment using Fireworks AI, detailing the process from setting up an API key to querying the deployment via various SDKs and CLI commands.
tags:
    - on-demand-deployment
    - fireworks-ai
    - quickstart
    - cli-tooling
    - api-key
    - autoscaling
category: tutorial
optimized: true
optimized_at: 2026-04-27T23:27:00Z
---
On-demand deployments are dedicated GPUs that give you better performance, no rate limits, fast autoscaling, and a wider selection of models than serverless. This quickstart spins up your first on-demand deployment in minutes.

## Step 1: Create and export an API key

Create an API key in the [Fireworks dashboard](https://app.fireworks.ai/settings/users/api-keys). Export it as an environment variable:

```bash
# macOS / Linux
export FIREWORKS_API_KEY="your_api_key_here"

# Windows
setx FIREWORKS_API_KEY "your_api_key_here"
```

## Step 2: Install the CLI

Install the `firectl` CLI tool, then sign in.

## Step 3: Create a deployment

Creates a GPT OSS 120B deployment optimized for speed (takes a few minutes, scales to 1 replica):

```bash
firectl deployment create accounts/fireworks/models/gpt-oss-120b \
        --deployment-shape fast \
        --scale-down-window 5m \
        --scale-up-window 30s \
        --min-replica-count 0 \
        --max-replica-count 1 \
        --scale-to-zero-window 5m \
        --wait
```

Response example:

```
Name: accounts/<YOUR ACCOUNT ID>/deployments/<DEPLOYMENT_ID>
Create Time: <CREATION_TIME>
Expire Time: <EXPIRATION_TIME>
Created By: <YOUR EMAIL>
State: CREATING
Status: OK
Min Replica Count: 0
Max Replica Count: 1
Desired Replica Count: 0
Replica Count: 0
Autoscaling Policy:
  Scale Up Window: 30s
  Scale Down Window: 5m0s
  Scale To Zero Window: 5m0s
Base Model: accounts/fireworks/models/gpt-oss-120b
...other fields...
```

Save the `Name:` value for the next step. See [[070-guides-ondemand-deployments]] for deployment and autoscaling options.

## Step 4: Query your deployment

Query using the same API as serverless models, replacing `<DEPLOYMENT_NAME>` with your deployment's name:

```python
from fireworks import Fireworks

client = Fireworks()

response = client.chat.completions.create(
    model="accounts/fireworks/models/gpt-oss-120b#<DEPLOYMENT_NAME>",
    messages=[{"role": "user", "content": "Explain quantum computing in simple terms"}],
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
    model="<DEPLOYMENT_NAME>",
    messages=[{"role": "user", "content": "Explain quantum computing in simple terms"}],
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
  model: "<DEPLOYMENT_NAME>",
  messages: [{role: "user", content: "Explain quantum computing in simple terms"}],
});

console.log(response.choices[0].message.content);
```

```bash
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -d '{"model": "<DEPLOYMENT_NAME>", "messages": [{"role": "user", "content": "Explain quantum computing in simple terms"}]}'
```

> [!tip]
> Replace the model string in [[009-getting-started-quickstart]] examples with your deployment-specific model string.

## Common use cases

### Autoscale by requests per second

```bash
firectl deployment create accounts/fireworks/models/gpt-oss-120b \
        --deployment-shape fast \
        --scale-down-window 5m \
        --scale-up-window 30s \
        --scale-to-zero-window 5m \
        --min-replica-count 0 \
        --max-replica-count 4 \
        --load-targets requests_per_second=5 \
        --wait
```

### Autoscale by concurrent requests

```bash
firectl deployment create accounts/fireworks/models/gpt-oss-120b \
        --deployment-shape fast \
        --scale-down-window 5m \
        --scale-up-window 30s \
        --scale-to-zero-window 5m \
        --min-replica-count 0 \
        --max-replica-count 4 \
        --load-targets concurrent_requests=5 \
        --wait
```

## Next steps

Ready to scale to production, explore other modalities, or customize your models?