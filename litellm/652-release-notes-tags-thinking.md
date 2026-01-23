---
title: 3 posts tagged with "thinking" | liteLLM
url: https://docs.litellm.ai/release_notes/tags/thinking
source: sitemap
fetched_at: 2026-01-21T19:42:10.53703329-03:00
rendered_js: false
word_count: 32
summary: This document explains a fix in LiteLLM v1.63.0 that aligns the Anthropic thinking response structure with the official API by renaming the signature_delta field to signature.
tags:
    - litellm
    - anthropic
    - api-update
    - streaming
    - thinking-blocks
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