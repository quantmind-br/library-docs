---
title: Moderation & Guardrailing | Mistral Docs
url: https://docs.mistral.ai/studio-api/conversations/moderation
source: sitemap
fetched_at: 2026-04-26T04:12:29.379560109-03:00
rendered_js: false
word_count: 618
summary: Implement safety guardrails for LLM applications using integrated API configuration or a dedicated moderation endpoint.
tags:
    - content-moderation
    - llm-guardrails
    - api-security
    - input-filtering
    - safety-policies
    - mistral-moderation
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Moderation & Guardrailing

Deploy LLMs with appropriate safety levels. Guardrail applications to ensure generated content is safe and respectful, or detect and filter harmful/PII content.

## Two Guardrailing Methods

| Method | Description |
|--------|-------------|
| **Custom Guardrails** *(recommended)* | Declare moderation rules in API requests — no separate calls or threshold logic |
| **Moderation API** | Dedicated API for raw scores and full control in custom pipelines |

## Moderation API

Powered by `mistral-moderation-2603`. Classifies text across policy categories including `jailbreaking`.

> [!warning] `mistral-moderation-2411` was deprecated on March 31, 2026.

### Endpoints

| Endpoint | Description |
|----------|-------------|
| `/v1/moderations` | Classify raw text |
| `/v1/chat/moderations` | Classify conversational content |

### Input

```python
response = client.moderations(
    input="Your text to moderate",
    categories=["harassment", "hate_speech", "violence"]
)
```

### Policy Categories

| Category | Description |
|----------|-------------|
| `harassment` | Harassing language |
| `hate_speech` | Discriminatory content |
| `violence` | Violent content |
| `self_harm` | Self-harm content |
| `sexual` | Sexual content |
| `jailbreaking` | Attempts to bypass safety measures |

### Response

```python
{
    "results": [{
        "flagged": False,
        "category_scores": {
            "harassment": 0.01,
            "hate_speech": 0.02,
            "violence": 0.01
        }
    }]
}
```

> [!tip] Set thresholds based on your use case. The default threshold is calibrated on Mistral's internal test set.

## Custom Guardrails

Declare moderation rules directly in API requests. Guardrails apply **input moderation only** — runs before the request reaches the model. Blocked requests return `403`.

### Configuration

```python
guardrails = {
    "moderation_llm_v2": {
        "custom_category_thresholds": {
            "harassment": 0.5,
            "hate_speech": 0.3
        },
        "ignore_other_categories": False,
        "action": "block",
        "block_on_error": True
    }
}

# Apply to chat completion
response = client.chat(
    model="mistral-large-latest",
    messages=[{"role": "user", "content": "User input"}],
    guardrails=guardrails
)
```

### Guardrail Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `custom_category_thresholds` | object | Category names to threshold values (0–1). Set to `1` to disable |
| `ignore_other_categories` | boolean | If `true`, only listed categories are evaluated |
| `action` | string | `"block"` to block on violation |
| `block_on_error` | boolean | Block if moderation API fails |
| `model_name` | string | Override default moderation model (optional) |

### Guardrail Application Points

| Point | Method |
|-------|--------|
| Chat completions | `guardrails` field in `POST /v1/chat/completions` |
| Conversations | `guardrails` field in `POST /v1/conversations` |
| Agent creation | `guardrails` field when creating agent |

### Success Response

```python
{
    "guardrails": {
        "moderation_llm_v2": {
            "evaluated_categories": {
                "harassment": {"flagged": False, "score": 0.02},
                "hate_speech": {"flagged": False, "score": 0.01}
            }
        }
    }
}
```

### Blocked Response (403)

```python
{
    "error": {
        "code": "guardrail_triggered",
        "message": "Request blocked due to: harassment",
        "details": {"categories": ["harassment"]}
    }
}
```

## Related

- [Moderation cookbook](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/moderation/system-level-guardrails.ipynb) — System-level guardrails
- [Moderation explored](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/moderation/moderation-explored.ipynb) — Exploratory examples

#content-moderation #llm-guardrails #api-security #input-filtering #safety-policies #mistral-moderation
