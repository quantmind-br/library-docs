---
title: typing - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/pooling/scoring/typing/
source: sitemap
fetched_at: 2026-05-07T21:21:12.526267738-03:00
rendered_js: false
word_count: 75
summary: Defines the ScoreMultiModalParam TypedDict, a specialized interface designed for scoring multimodal content within the vLLM framework.
tags:
    - vllm
    - multimodal-scoring
    - typeddict
    - api-interface
    - python-typing
category: reference
---

Bases: `TypedDict`

A specialized parameter type for scoring multimodal content

The reasons why don't reuse `CustomChatCompletionMessageParam` directly: 1. Score tasks don't need the 'role' field (user/assistant/system) that's required in chat completions 2. Including chat-specific fields would confuse users about their purpose in scoring 3. This is a more focused interface that only exposes what's needed for scoring

Source code in `vllm/entrypoints/pooling/scoring/typing.py`

```
classScoreMultiModalParam(TypedDict, total=False):
"""
    A specialized parameter type for scoring multimodal content

    The reasons why don't reuse `CustomChatCompletionMessageParam` directly:
    1. Score tasks don't need the 'role' field (user/assistant/system) that's required in chat completions
    2. Including chat-specific fields would confuse users about their purpose in scoring
    3. This is a more focused interface that only exposes what's needed for scoring
    """  # noqa: E501

    content: Required[list[ScoreContentPartParam]]
"""The multimodal contents"""
```

### content `instance-attribute` [¶](#vllm.entrypoints.pooling.scoring.typing.ScoreMultiModalParam.content "Permanent link")

The multimodal contents