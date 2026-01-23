---
title: Pre-fix Assistant Messages | liteLLM
url: https://docs.litellm.ai/docs/completion/prefix
source: sitemap
fetched_at: 2026-01-21T19:44:38.596358581-03:00
rendered_js: false
word_count: 9
summary: This document illustrates the chat completion response structure and provides instructions on how to verify model feature support using the litellm library.
tags:
    - litellm
    - chat-completion
    - api-response
    - model-metadata
    - prefix-support
category: reference
---

```
{
    "id": "3b66124d79a708e10c603496b363574c",
    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "message": {
                "content": " won the FIFA World Cup in 2022.",
                "role": "assistant",
                "tool_calls": null,
                "function_call": null
            }
        }
    ],
    "created": 1723323084,
    "model": "deepseek/deepseek-chat",
    "object": "chat.completion",
    "system_fingerprint": "fp_7e0991cad4",
    "usage": {
        "completion_tokens": 12,
        "prompt_tokens": 16,
        "total_tokens": 28,
    },
    "service_tier": null
}
```

Call `litellm.get_model_info` to check if a model/provider supports `prefix`.