---
title: v1.63.0 - Anthropic 'thinking' response update
url: https://docs.litellm.ai/release_notes/v1.63.0
source: sitemap
fetched_at: 2026-01-21T19:43:22.801314169-03:00
rendered_js: false
word_count: 32
summary: This document outlines an update to LiteLLM version 1.63.0 that aligns Anthropic streaming responses with official specifications by renaming the signature_delta field to signature. It ensures the signature block is correctly returned during extended thinking response streaming.
tags:
    - litellm
    - anthropic-api
    - streaming-responses
    - extended-thinking
    - api-update
    - bug-fix
category: reference
---

v1.63.0 fixes Anthropic 'thinking' response on streaming to return the `signature` block. [Github Issue](https://github.com/BerriAI/litellm/issues/8964)

It also moves the response structure from `signature_delta` to `signature` to be the same as Anthropic. [Anthropic Docs](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#implementing-extended-thinking)

```
"message": {
    ...
    "reasoning_content": "The capital of France is Paris.",
    "thinking_blocks": [
        {
            "type": "thinking",
            "thinking": "The capital of France is Paris.",
-            "signature_delta": "EqoBCkgIARABGAIiQL2UoU0b1OHYi+..." # 👈 OLD FORMAT
+            "signature": "EqoBCkgIARABGAIiQL2UoU0b1OHYi+..." # 👈 KEY CHANGE
        }
    ]
}
```