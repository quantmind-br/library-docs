---
title: utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/pooling/scoring/utils/
source: sitemap
fetched_at: 2026-05-07T21:21:13.515754653-03:00
rendered_js: false
word_count: 360
summary: This document outlines utility functions used for processing, scoring, and formatting query-document pairs, including multi-modal data tracking and token manipulation for scoring models.
tags:
    - scoring-utils
    - multi-modal
    - tokenization
    - cross-encoder
    - late-interaction
    - vllm
category: reference
---

## \_ensure\_str [¶](#vllm.entrypoints.pooling.scoring.utils._ensure_str "Permanent link")

Extract a single string prompt from parsed conversation content.

Source code in `vllm/entrypoints/pooling/scoring/utils.py`

```
def_ensure_str(content: list[ConversationMessage]) -> str:
"""Extract a single string prompt from parsed conversation content."""
    assert len(content) == 1
    prompt = content[0]["content"]
    if prompt is not None and isinstance(prompt, str):
        return cast(str, prompt)
    raise ValueError(f"Only string content is supported, but got {content}.")
```

## compress\_token\_type\_ids [¶](#vllm.entrypoints.pooling.scoring.utils.compress_token_type_ids "Permanent link")

```
compress_token_type_ids(token_type_ids: list[int]) -> int
```

Return position of the first 1 or the length of the list if not found.

Source code in `vllm/entrypoints/pooling/scoring/utils.py`

```
defcompress_token_type_ids(token_type_ids: list[int]) -> int:
"""
    Return position of the first 1 or the length of the list
    if not found.
    """
    first_one = len(token_type_ids)
    err_msg = (
        "Token type ids are expected to be a sequence"
        " of zeros followed by a sequence of ones"
    )
    for i, type_id in enumerate(token_type_ids):
        if type_id == 0 and first_one < i:
            raise ValueError(err_msg)
        elif type_id == 1 and first_one > i:
            first_one = i
        elif type_id > 1:
            raise ValueError(err_msg)

    return first_one
```

## compute\_maxsim\_score [¶](#vllm.entrypoints.pooling.scoring.utils.compute_maxsim_score "Permanent link")

Compute ColBERT MaxSim score.

Parameters:

Name Type Description Default `q_emb` `Tensor`

Query token embeddings \[query\_len, dim]

*required* `d_emb` `Tensor`

Document token embeddings \[doc\_len, dim]

*required*

Returns:

Type Description `Tensor`

MaxSim score (sum over query tokens of max similarity to any doc token)

Source code in `vllm/entrypoints/pooling/scoring/utils.py`

```
defcompute_maxsim_score(q_emb: torch.Tensor, d_emb: torch.Tensor) -> torch.Tensor:
"""
    Compute ColBERT MaxSim score.

    Args:
        q_emb: Query token embeddings [query_len, dim]
        d_emb: Document token embeddings [doc_len, dim]

    Returns:
        MaxSim score (sum over query tokens of max similarity to any doc token)
    """
    # compute in float32 for numerical stability
    # [query_len, doc_len]
    token_scores = torch.matmul(q_emb.float(), d_emb.float().T)
    # Max over document tokens, sum over query tokens
    return token_scores.amax(dim=-1).sum()
```

## get\_num\_special\_tokens\_for\_pair [¶](#vllm.entrypoints.pooling.scoring.utils.get_num_special_tokens_for_pair "Permanent link")

```
get_num_special_tokens_for_pair(tokenizer) -> int
```

Get number of special tokens added for a text pair encoding.

Source code in `vllm/entrypoints/pooling/scoring/utils.py`

```
defget_num_special_tokens_for_pair(tokenizer) -> int:
"""Get number of special tokens added for a text pair encoding."""
    method = getattr(tokenizer, "num_special_tokens_to_add", None)
    if method is not None:
        try:
            return method(pair=True)
        except TypeError:
            pass
    # Fallback: compute by tokenizing empty strings
    empty_encoding = tokenizer("", text_pair="", add_special_tokens=True)
    return len(empty_encoding["input_ids"])
```

## parse\_score\_data [¶](#vllm.entrypoints.pooling.scoring.utils.parse_score_data "Permanent link")

Parse a query-document pair into text prompts and shared multi-modal data.

Uses a **single** :class:`MultiModalItemTracker` so that multi-modal items from both inputs are merged into one `mm_data` dict. This is the correct behaviour for cross-encoder scoring, where query and document are concatenated into a single model prompt.

Source code in `vllm/entrypoints/pooling/scoring/utils.py`

```
defparse_score_data(
    data_1: ScoreData,
    data_2: ScoreData,
    model_config: ModelConfig,
) -> tuple[str, str, MultiModalDataDict | None, MultiModalUUIDDict | None]:
"""Parse a query-document pair into text prompts and shared multi-modal
    data.

    Uses a **single** :class:`MultiModalItemTracker` so that multi-modal
    items from both inputs are merged into one ``mm_data`` dict.  This is
    the correct behaviour for cross-encoder scoring, where query and
    document are concatenated into a single model prompt.
    """
    mm_tracker = MultiModalItemTracker(model_config)

    content_1 = _parse_score_content("query", data_1, mm_tracker)
    content_2 = _parse_score_content("document", data_2, mm_tracker)

    prompt_1 = _ensure_str(content_1)
    prompt_2 = _ensure_str(content_2)
    mm_items, mm_uuids = mm_tracker.resolve_items()

    return prompt_1, prompt_2, mm_items, mm_uuids
```

## parse\_score\_data\_single [¶](#vllm.entrypoints.pooling.scoring.utils.parse_score_data_single "Permanent link")

Parse **one** ScoreData into a text prompt and its own multi-modal data.

Unlike :func:`parse_score_data`, each call creates an **independent** :class:`MultiModalItemTracker` so multi-modal items are kept separate. This is the correct behaviour for late-interaction scoring, where query and document are encoded independently.

Source code in `vllm/entrypoints/pooling/scoring/utils.py`

```
defparse_score_data_single(
    data: ScoreData,
    role: str,
    model_config: ModelConfig,
) -> tuple[str, MultiModalDataDict | None, MultiModalUUIDDict | None]:
"""Parse **one** ScoreData into a text prompt and its own multi-modal
    data.

    Unlike :func:`parse_score_data`, each call creates an **independent**
    :class:`MultiModalItemTracker` so multi-modal items are kept separate.
    This is the correct behaviour for late-interaction scoring, where
    query and document are encoded independently.
    """
    mm_tracker = MultiModalItemTracker(model_config)
    content = _parse_score_content(role, data, mm_tracker)

    prompt = _ensure_str(content)
    mm_items, mm_uuids = mm_tracker.resolve_items()
    return prompt, mm_items, mm_uuids
```

## score\_data\_to\_prompts [¶](#vllm.entrypoints.pooling.scoring.utils.score_data_to_prompts "Permanent link")

Convert a list of ScoreData into PromptType objects.

For plain text inputs, returns the string directly. For multimodal inputs (list of content parts), parses them into a :class:`TextPrompt` with attached `multi_modal_data` / `multi_modal_uuids`.

This is used by late-interaction scoring where each query/document is encoded independently.

Source code in `vllm/entrypoints/pooling/scoring/utils.py`

```
defscore_data_to_prompts(
    data_list: list[ScoreData],
    role: str,
    model_config: ModelConfig,
) -> list[PromptType]:
"""Convert a list of ScoreData into PromptType objects.

    For plain text inputs, returns the string directly.
    For multimodal inputs (list of content parts), parses them into
    a :class:`TextPrompt` with attached ``multi_modal_data`` /
    ``multi_modal_uuids``.

    This is used by late-interaction scoring where each query/document
    is encoded independently.
    """
    prompts: list[PromptType] = []
    for data in data_list:
        if isinstance(data, str):
            prompts.append(data)
        else:
            text, mm_data, mm_uuids = parse_score_data_single(data, role, model_config)
            prompt: TextPrompt = TextPrompt(prompt=text)
            if mm_data is not None:
                prompt["multi_modal_data"] = mm_data
            if mm_uuids is not None:
                prompt["multi_modal_uuids"] = mm_uuids
            prompts.append(prompt)
    return prompts
```

## truncate\_text\_to\_tokens [¶](#vllm.entrypoints.pooling.scoring.utils.truncate_text_to_tokens "Permanent link")

```
truncate_text_to_tokens(
    text: str, tokenizer, max_tokens: int
) -> str
```

Truncate text to a maximum number of content tokens.

Uses offset\_mapping to slice the original text at the exact character boundary, avoiding lossy encode→decode round-trips that can shift the token count by 1-3 tokens due to BPE merge boundary changes.

Source code in `vllm/entrypoints/pooling/scoring/utils.py`

```
deftruncate_text_to_tokens(
    text: str,
    tokenizer,
    max_tokens: int,
) -> str:
"""Truncate text to a maximum number of content tokens.

    Uses offset_mapping to slice the original text at the exact character
    boundary, avoiding lossy encode→decode round-trips that can shift
    the token count by 1-3 tokens due to BPE merge boundary changes.
    """
    encoding = tokenizer(text, add_special_tokens=False, return_offsets_mapping=True)
    if len(encoding["input_ids"]) <= max_tokens:
        return text
    char_end = encoding["offset_mapping"][max_tokens - 1][1]
    return text[:char_end]
```