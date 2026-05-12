---
title: gemma3n_audio_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/gemma3n_audio_utils/
source: sitemap
fetched_at: 2026-05-07T21:30:13.944499702-03:00
rendered_js: false
word_count: 192
summary: This module provides utility functions for Gemma3n audio processing, specifically ensuring audio feature tensors conform to a fixed token length requirement through padding or truncation.
tags:
    - gemma3n
    - audio-processing
    - tensor-manipulation
    - padding
    - truncation
    - model-executor
category: reference
---

## vllm.model\_executor.models.gemma3n\_audio\_utils [¶](#vllm.model_executor.models.gemma3n_audio_utils "Permanent link")

Lightweight utility functions for Gemma3n audio processing.

This module is separate from gemma3n\_mm.py to avoid heavy CUDA dependencies, making it testable without a full vLLM build.

## adjust\_audio\_features\_to\_expected\_length [¶](#vllm.model_executor.models.gemma3n_audio_utils.adjust_audio_features_to_expected_length "Permanent link")

Adjust audio features to expected token length via padding or truncation.

The Gemma3nProcessor expects all audio will be ~30s in length and inserts a fixed number of audio soft tokens into the text. However, the audio preprocessing and encoder do not guarantee they will produce exactly that many soft tokens; they may produce fewer tokens (for shorter audio) or more tokens (for longer audio or due to BOA/EOA special tokens).

This function handles both cases: - If fewer tokens: pad with the provided padding embeddings - If more tokens: truncate to the expected count

Parameters:

Name Type Description Default `audio_features` `Tensor`

Audio embeddings tensor of shape (batch\_size, seq\_len, embed\_dim)

*required* `expected_tokens` `int`

The expected number of audio tokens (e.g., 188)

*required* `audio_padding_embs` `Tensor`

Padding embeddings tensor of shape (1, 1, embed\_dim)

*required*

Returns:

Type Description `Tensor`

Tuple of:

`int`

- adjusted\_features: Audio features adjusted to expected\_tokens length

`tuple[Tensor, int]`

- tokens\_truncated: Number of tokens truncated (0 if padding was applied)

Source code in `vllm/model_executor/models/gemma3n_audio_utils.py`

```
defadjust_audio_features_to_expected_length(
    audio_features: torch.Tensor,
    expected_tokens: int,
    audio_padding_embs: torch.Tensor,
) -> tuple[torch.Tensor, int]:
"""Adjust audio features to expected token length via padding or truncation.

    The Gemma3nProcessor expects all audio will be ~30s in length and inserts
    a fixed number of audio soft tokens into the text. However, the audio
    preprocessing and encoder do not guarantee they will produce exactly that
    many soft tokens; they may produce fewer tokens (for shorter audio) or more
    tokens (for longer audio or due to BOA/EOA special tokens).

    This function handles both cases:
    - If fewer tokens: pad with the provided padding embeddings
    - If more tokens: truncate to the expected count

    Args:
        audio_features: Audio embeddings tensor of shape
            (batch_size, seq_len, embed_dim)
        expected_tokens: The expected number of audio tokens (e.g., 188)
        audio_padding_embs: Padding embeddings tensor of shape (1, 1, embed_dim)

    Returns:
        Tuple of:
        - adjusted_features: Audio features adjusted to expected_tokens length
        - tokens_truncated: Number of tokens truncated (0 if padding was applied)
    """
    audio_batch_size, audio_seq_len, audio_embed_dim = audio_features.shape
    tokens_truncated = 0

    if audio_seq_len < expected_tokens:
        # Pad to expected length with padding embeddings
        extra_padding_tokens = expected_tokens - audio_seq_len
        extra_padding_features = audio_padding_embs.expand(
            audio_batch_size, extra_padding_tokens, audio_embed_dim
        )
        audio_features = torch.cat((audio_features, extra_padding_features), dim=1)
    elif audio_seq_len > expected_tokens:
        # Truncate to expected length (audio encoder produced more tokens
        # than expected, e.g., due to longer audio or placeholder mismatch)
        tokens_truncated = audio_seq_len - expected_tokens
        audio_features = audio_features[:, :expected_tokens, :]

    return audio_features, tokens_truncated
```