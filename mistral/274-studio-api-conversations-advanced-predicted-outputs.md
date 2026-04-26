---
title: Predicted Outputs | Mistral Docs
url: https://docs.mistral.ai/studio-api/conversations/advanced/predicted-outputs
source: sitemap
fetched_at: 2026-04-26T04:12:19.541476123-03:00
rendered_js: false
word_count: 156
summary: Use Predicted Outputs feature to reduce latency and improve computational efficiency by pre-defining expected content in model responses.
tags:
    - predicted-outputs
    - latency-optimization
    - api-performance
    - computational-efficiency
    - text-generation
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Predicted Outputs

Predicted Outputs **optimize response time** by leveraging known or predictable content. Models allocate more computational resources to unpredictable elements, improving overall efficiency.

> [!tip] Ideal for editing large texts, modifying code, or generating template-based responses where significant portions are predetermined.

## Usage

Use the `prediction` parameter to define predicted outputs:

```python
response = client.chat(
    model="mistral-large-latest",
    messages=[
        {"role": "user", "content": "Update the model in this fine-tuning job to mistral-large-latest"},
        {"role": "assistant", "content": "To update the model, you would modify the job configuration as follows:"},
        {"role": "user", "content": "Here is the code snippet to modify:\n```python\njob = client.fine_tuning.create(\n    model='mistral-medium-latest',\n    dataset_id='dataset-123'\n)\n```"}
    ],
    prediction={
        "content": "```python\njob = client.fine_tuning.create(\n    model='mistral-large-latest',\n    dataset_id='dataset-123'\n)\n```"
    }
)
```

## How It Works

1. Include known/expected content as both user prompt and predicted output
2. Model skips regenerating known content, focusing compute on new content
3. Result is faster response with same quality

## When to Use

| Use Case | Example |
|----------|---------|
| Code modification | Regenerating files with minor changes |
| Template filling | Completing structured documents |
| Text editing | Updating existing content |

> [!note] For more on chat completions, see [Chat Completions](https://docs.mistral.ai/studio-api/conversations/chat-completion).

#predicted-outputs #latency-optimization #api-performance #computational-efficiency #text-generation
