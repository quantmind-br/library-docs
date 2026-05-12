---
title: utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/utils/
source: sitemap
fetched_at: 2026-05-07T21:38:27.146999626-03:00
rendered_js: false
word_count: 17
summary: This document provides a utility function to determine the total request length in tokens by evaluating either prompt token identifiers or prompt embeddings.
tags:
    - token-calculation
    - vllm-utils
    - prompt-length
    - pytorch-tensor
    - request-processing
category: api
---

Calculate the request length (in number of tokens) give either prompt\_token\_ids or prompt\_embeds.

Source code in `vllm/utils/__init__.py`

```
deflength_from_prompt_token_ids_or_embeds(
    prompt_token_ids: list[int] | torch.Tensor | None,
    prompt_embeds: torch.Tensor | None,
) -> int:
"""Calculate the request length (in number of tokens) give either
    prompt_token_ids or prompt_embeds.
    """
    prompt_token_len = None if prompt_token_ids is None else len(prompt_token_ids)
    prompt_embeds_len = None if prompt_embeds is None else len(prompt_embeds)

    if prompt_token_len is None:
        if prompt_embeds_len is None:
            raise ValueError("Neither prompt_token_ids nor prompt_embeds were defined.")
        return prompt_embeds_len
    else:
        if prompt_embeds_len is not None and prompt_embeds_len != prompt_token_len:
            raise ValueError(
                "Prompt token ids and prompt embeds had different lengths"
                f" prompt_token_ids={prompt_token_len}"
                f" prompt_embeds={prompt_embeds_len}"
            )
        return prompt_token_len
```