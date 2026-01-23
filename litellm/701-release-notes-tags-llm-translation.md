---
title: 3 posts tagged with "llm translation" | liteLLM
url: https://docs.litellm.ai/release_notes/tags/llm-translation
source: sitemap
fetched_at: 2026-01-21T19:41:45.788643514-03:00
rendered_js: false
word_count: 32
summary: LiteLLM version 1.63.0 updates the Anthropic extended thinking response format by renaming signature_delta to signature for consistency with the official API.
tags:
    - litellm
    - anthropic
    - api-integration
    - extended-thinking
    - changelog
category: other
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