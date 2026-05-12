---
title: logits_process - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/logits_process/
source: sitemap
fetched_at: 2026-05-07T21:22:27.827449855-03:00
rendered_js: false
word_count: 40
summary: Defines the LogitsProcessor type alias for functions that modify logit tensors during the token generation process.
tags:
    - logits-processor
    - token-generation
    - type-alias
    - tensor-manipulation
    - vllm-library
category: reference
---

## LogitsProcessor `module-attribute` [¶](#vllm.logits_process.LogitsProcessor "Permanent link")

```
LogitsProcessor: TypeAlias = (
    Callable[[list[int], Tensor], Tensor]
    | Callable[[list[int], list[int], Tensor], Tensor]
)
```

LogitsProcessor is a function that takes a list of previously generated tokens, the logits tensor for the next token and, optionally, prompt tokens as a first argument, and returns a modified tensor of logits to sample from.