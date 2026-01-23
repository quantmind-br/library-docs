---
title: 3 posts tagged with "claude-3-7-sonnet" | liteLLM
url: https://docs.litellm.ai/release_notes/tags/claude-3-7-sonnet
source: sitemap
fetched_at: 2026-01-21T19:41:26.562549225-03:00
rendered_js: false
word_count: 32
summary: This update for LiteLLM v1.63.0 fixes Anthropic thinking responses during streaming and aligns the response structure by renaming signature_delta to signature.
tags:
    - litellm
    - anthropic
    - extended-thinking
    - api-update
    - streaming
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