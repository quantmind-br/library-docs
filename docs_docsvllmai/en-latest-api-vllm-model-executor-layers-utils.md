---
title: utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/utils/
source: sitemap
fetched_at: 2026-05-07T21:28:33.076591337-03:00
rendered_js: false
word_count: 112
summary: This document provides the technical specification and implementation details for the apply_penalties utility function used to adjust model logits based on presence, frequency, and repetition penalties.
tags:
    - vllm
    - model-layers
    - logits-adjustment
    - penalty-calculation
    - token-sampling
    - machine-learning-utilities
category: reference
---

## vllm.model\_executor.layers.utils [¶](#vllm.model_executor.layers.utils "Permanent link")

Utility methods for model layers.

## apply\_penalties [¶](#vllm.model_executor.layers.utils.apply_penalties "Permanent link")

Applies penalties in place to the logits tensor logits : The input logits tensor of shape \[num\_seqs, vocab\_size] prompt\_tokens\_tensor: A tensor containing the prompt tokens. The prompts are padded to the maximum prompt length within the batch using `vocab_size` as the padding value. The value `vocab_size` is used for padding because it does not correspond to any valid token ID in the vocabulary. output\_tokens\_tensor: The output tokens tensor. presence\_penalties: The presence penalties of shape (num\_seqs, ) frequency\_penalties: The frequency penalties of shape (num\_seqs, ) repetition\_penalties: The repetition penalties of shape (num\_seqs, )

Source code in `vllm/model_executor/layers/utils.py`

```
defapply_penalties(
    logits: torch.Tensor,
    prompt_tokens_tensor: torch.Tensor,
    output_tokens_tensor: torch.Tensor,
    presence_penalties: torch.Tensor,
    frequency_penalties: torch.Tensor,
    repetition_penalties: torch.Tensor,
) -> torch.Tensor:
"""
    Applies penalties in place to the logits tensor
    logits : The input logits tensor of shape [num_seqs, vocab_size]
    prompt_tokens_tensor: A tensor containing the prompt tokens. The prompts
        are padded to the maximum prompt length within the batch using
        `vocab_size` as the padding value. The value `vocab_size` is used
        for padding because it does not correspond to any valid token ID
        in the vocabulary.
    output_tokens_tensor: The output tokens tensor.
    presence_penalties: The presence penalties of shape (num_seqs, )
    frequency_penalties: The frequency penalties of shape (num_seqs, )
    repetition_penalties: The repetition penalties of shape (num_seqs, )
    """
    num_seqs, vocab_size = logits.shape
    _, prompt_mask = get_token_bin_counts_and_mask(
        prompt_tokens_tensor, vocab_size, num_seqs
    )
    output_bin_counts, output_mask = get_token_bin_counts_and_mask(
        output_tokens_tensor, vocab_size, num_seqs
    )

    # Apply repetition penalties as a custom op
    fromvllm._custom_opsimport apply_repetition_penalties

    apply_repetition_penalties(logits, prompt_mask, output_mask, repetition_penalties)

    # We follow the definition in OpenAI API.
    # Refer to https://platform.openai.com/docs/api-reference/parameter-details
    logits -= frequency_penalties.unsqueeze(dim=1) * output_bin_counts
    logits -= presence_penalties.unsqueeze(dim=1) * output_mask
    return logits
```