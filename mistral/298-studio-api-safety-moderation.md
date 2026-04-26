---
title: Moderation & Guardrailing | Mistral Docs
url: https://docs.mistral.ai/studio-api/safety-moderation
source: sitemap
fetched_at: 2026-04-26T04:13:26.542937361-03:00
rendered_js: false
word_count: 618
summary: Content moderation and safety guardrails for LLM deployments using custom inline configuration or a dedicated moderation API.
tags:
    - content-moderation
    - llm-security
    - guardrails
    - api-configuration
    - safety-filtering
    - input-validation
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Moderation & Guardrailing

Deploy LLMs with appropriate safety levels for your use case.

## Two Methods

| Method | Description |
|--------|-------------|
| **Custom Guardrails** *(recommended)* | Declare moderation rules in API requests |
| **Moderation API** | Dedicated API for raw scores and custom pipelines |

## Moderation API

Powered by `mistral-moderation-2603`. Classifies text across policy categories.

> [!warning] `mistral-moderation-2411` deprecated March 31, 2026.

### Endpoints

| Endpoint | Input |
|----------|-------|
| `/v1/moderations` | Raw text |
| `/v1/chat/moderations` | Conversational content |

### Usage

```python
response = client.moderations(
    input="Text to classify",
    categories=["harassment", "hate_speech", "violence"]
)
```

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

## Custom Guardrails

Declare moderation rules directly in API requests. Runs **before** the request reaches the model. Blocked requests return `403`.

### Configuration

```python
guardrails = {
    "moderation_llm_v2": {
        "custom_category_thresholds": {"harassment": 0.5, "hate_speech": 0.3},
        "ignore_other_categories": False,
        "action": "block",
        "block_on_error": True
    }
}
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `custom_category_thresholds` | object | Category → threshold (0–1). Set to `1` to disable |
| `ignore_other_categories` | boolean | Only evaluate listed categories |
| `action` | string | `"block"` to block on violation |
| `block_on_error` | boolean | Block if moderation API fails |
| `model_name` | string | Override default model (optional) |

### Apply Guardrails

| Point | Method |
|-------|--------|
| Chat completions | `guardrails` in `POST /v1/chat/completions` |
| Conversations | `guardrails` in `POST /v1/conversations` |
| Agent creation | `guardrails` when creating agent |

### Success Response

```python
{
    "guardrails": {
        "moderation_llm_v2": {
            "evaluated_categories": {
                "harassment": {"flagged": False, "score": 0.02}
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
        "message": "Request blocked due to: harassment"
    }
}
```

## Cookbooks

- [System-level guardrails](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/moderation/system-level-guardrails.ipynb)
- [Moderation explored](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/moderation/moderation-explored.ipynb)

#content-moderation #llm-security #guardrails #api-configuration #safety-filtering #input-validation
