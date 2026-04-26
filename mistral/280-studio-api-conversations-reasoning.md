---
title: Reasoning | Mistral Docs
url: https://docs.mistral.ai/studio-api/conversations/reasoning
source: sitemap
fetched_at: 2026-04-26T04:12:30.609109998-03:00
rendered_js: false
word_count: 180
summary: Reasoning in large language models using chain-of-thought processes and test-time computation to improve performance on complex tasks.
tags:
    - large-language-models
    - chain-of-thought
    - test-time-computation
    - artificial-intelligence
    - reasoning-models
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Reasoning

**Reasoning** extends Chain of Thought (CoT) by encouraging models to generate chains of thought freely before producing final answers. Models explore problems more profoundly and reach better solutions using extra compute time — also described as **Test Time Computation**.

![Reasoning](https://docs.mistral.ai/img/_reasoning_graph.png)![Reasoning dark](https://docs.mistral.ai/img/_reasoning_graph-dark.png)

## Use Cases

Reasoning excels at complex tasks:
- Math problems
- Coding tasks
- Any scenario requiring deep logical analysis

## Output Structure

Response includes:
1. `thinking` chunk — Model's reasoning traces
2. `text` chunk — Final answer

## Approaches

| Approach | Model | Description |
|----------|-------|-------------|
| **Adjustable** | `mistral-small-latest` | Control thinking via `reasoning_effort` parameter |
| **Native** | `magistral-small-latest`, `magistral-medium-latest` | Always generates reasoning traces |

### Adjustable Reasoning

Control how much the model thinks:

```python
# High thinking effort
response = client.chat(
    model="mistral-small-latest",
    messages=[{"role": "user", "content": "Solve: 2x + 5 = 15"}],
    reasoning_effort="high"  # Full thinking trace
)

# Minimal thinking
response = client.chat(
    model="mistral-small-latest",
    messages=[{"role": "user", "content": "Hello"}],
    reasoning_effort="none"  # No thinking trace
)
```

### Native Reasoning

Models always generate reasoning traces:

```python
response = client.chat(
    model="magistral-medium-latest",
    messages=[{"role": "user", "content": "Explain quantum entanglement"}]
)
# Response includes thinking + final answer
```

## Related

- [Adjustable Reasoning](https://docs.mistral.ai/studio-api/conversations/reasoning/adjustable) — `reasoning_effort` parameter
- [Native Reasoning](https://docs.mistral.ai/studio-api/conversations/reasoning/native) — Purpose-built reasoning models

#large-language-models #chain-of-thought #test-time-computation #artificial-intelligence #reasoning-models
