---
title: protocol - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/serve/tokenize/protocol/
source: sitemap
fetched_at: 2026-05-07T21:21:49.185199031-03:00
rendered_js: false
word_count: 13
summary: This document defines the TokenizerInfoResponse class, which structures the output for tokenizer configuration data matching the standard tokenizer_config.json format.
tags:
    - tokenizer-config
    - api-response
    - vllm
    - model-configuration
    - protocol-definition
category: reference
---

Bases: `OpenAIBaseModel`

Response containing tokenizer configuration equivalent to tokenizer\_config.json

Source code in `vllm/entrypoints/serve/tokenize/protocol.py`

```
classTokenizerInfoResponse(OpenAIBaseModel):
"""
    Response containing tokenizer configuration
    equivalent to tokenizer_config.json
    """

    model_config = ConfigDict(extra="allow")
    tokenizer_class: str
```