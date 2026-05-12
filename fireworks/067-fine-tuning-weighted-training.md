---
title: Fine Tuning Weighted Training
url: https://docs.fireworks.ai/fine-tuning/weighted-training
source: sitemap
fetched_at: 2026-04-27T20:18:32.544492491-03:00
rendered_js: false
word_count: 221
summary: This document explains the concept of weighted training, detailing how assigning importance levels (weights) to dataset samples allows for controlled learning in a model. It covers global sample weighting and specific message-level weighting within multi-turn conversations.
tags:
    - weighted-training
    - dataset-weighting
    - sample-importance
    - model-learning
    - jsonl-format
    - message-weight
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Weighted training assigns importance levels to dataset samples, giving control over how the model learns. Higher weights produce stronger learning signals; lower weights (including negative) reduce or reverse a sample's influence.

## How it works

Each sample's loss is multiplied by its weight before updating model parameters. This lets you emphasize high-quality examples and de-emphasize noisy ones.

## Dataset format

Add a `weight` field at the root level of each JSON object in your JSONL dataset:

```json
{
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is 2 + 2?"},
    {"role": "assistant", "content": "4"}
  ],
  "weight": 2.0
}
```

### Weight values

| Weight | Effect |
|--------|--------|
| `> 1.0` | Increased importance — model learns more |
| `1.0` | Default behavior |
| `0.0 – 1.0` | Reduced importance |
| `0.0` | Sample ignored during training |
| `< 0.0` | Negative weight — reverses learning signal |

## Use cases

- **Upweight high-quality examples**: Give best examples `weight: 2.0`, average ones `weight: 1.0`, lower-quality ones `weight: 0.5`
- **Balance dataset distribution**: Upweight underrepresented prompt types to `weight: 3.0`
- **De-emphasize noisy samples**: Reduce noise with `weight: 0.3`

## Message-level weighting

For multi-turn conversations, control which assistant messages are included by adding `weight` to individual messages (follows the [OpenAI fine-tuning specification](https://platform.openai.com/docs/api-reference/fine-tuning/chat-input#fine_tuning-chat_input-messages-assistant_message_weight)):

```json
{
  "messages": [
    {"role": "user", "content": "What's the capital of France?"},
    {"role": "assistant", "content": "Paris.", "weight": 1},
    {"role": "user", "content": "What about Germany?"},
    {"role": "assistant", "content": "Berlin.", "weight": 0}
  ]
}
```

Message-level weights accept only `0` (exclude) or `1` (include).

## Example dataset

```jsonl
{"messages": [{"role": "system", "content": "You are a math tutor."}, {"role": "user", "content": "What is 15 * 3?"}, {"role": "assistant", "content": "15 * 3 = 45"}], "weight": 1.0}
{"messages": [{"role": "system", "content": "You are a math tutor."}, {"role": "user", "content": "Solve: 2x + 5 = 15"}, {"role": "assistant", "content": "x = 5"}], "weight": 1.5}
{"messages": [{"role": "system", "content": "You are a math tutor."}, {"role": "user", "content": "Integrate x^2 dx"}, {"role": "assistant", "content": "(x^3)/3 + C"}], "weight": 2.0}
```

This dataset upweights more complex problems, focusing model attention on calculus over basic arithmetic.

#weighted-training #dataset-weighting #fine-tuning
