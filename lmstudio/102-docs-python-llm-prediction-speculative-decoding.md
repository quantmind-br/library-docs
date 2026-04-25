---
title: Speculative Decoding
url: https://lmstudio.ai/docs/python/llm-prediction/speculative-decoding
source: sitemap
fetched_at: 2026-04-07T21:31:08.538368206-03:00
rendered_js: false
word_count: 57
summary: This document explains how to implement speculative decoding in the lmstudio-python SDK, a technique used to boost the generation speed of large language models.
tags:
    - speculative-decoding
    - llm
    - python-sdk
    - generation-speed
    - lmstudio
category: tutorial
---

*Required Python SDK version*: **1.2.0**

Speculative decoding is a technique that can substantially increase the generation speed of large language models (LLMs) without reducing response quality. See [Speculative Decoding](https://lmstudio.ai/docs/app/advanced/speculative-decoding) for more info.

To use speculative decoding in `lmstudio-python`, simply provide a `draftModel` parameter when performing the prediction. You do not need to load the draft model separately.

```
import lmstudio as lms

main_model_key = "qwen2.5-7b-instruct"
draft_model_key = "qwen2.5-0.5b-instruct"

model = lms.llm(main_model_key)
result = model.respond(
    "What are the prime numbers between 0 and 100?",
    config={
        "draftModel": draft_model_key,
    }
)

print(result)
stats = result.stats
print(f"Accepted {stats.accepted_draft_tokens_count}/{stats.predicted_tokens_count} tokens")
```