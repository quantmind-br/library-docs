---
title: utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/lora/punica_wrapper/utils/
source: sitemap
fetched_at: 2026-05-07T21:23:08.053731075-03:00
rendered_js: false
word_count: 0
summary: This function converts LoRAMapping objects into structured index tensors required for efficient LoRA-based inference operations.
tags:
    - lora
    - tensor-manipulation
    - inference-optimization
    - deep-learning
    - pytorch
category: api
---

```
defconvert_mapping(
    mapping: "LoRAMapping",
    lora_index_to_id: list[int | None],
    max_loras: int,
    vocab_size: int,
    extra_vocab_size: int,
    device: torch.device,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, list[int]]:
"""Converts LoRAMapping to index tensors.

    Args:
        mapping: LoRAMapping mapping rows in a batch to LoRA ids.
        lora_index_to_id: List mapping LoRA ids to LoRA indices.
        max_loras: Maximum number of LoRAs.
        vocab_size: Model vocab size.
        extra_vocab_size: Extra vocab size each LoRA can have.

    Returns:
        A tuple of tensors:
            base_indices: Tensor of shape [batch_size] mapping batch rows to
                LoRA indices.
            sampler_indices: Tensor of shape [batch_size] mapping requests to
                LoRA indices for sampler. For generation, this will be the
                same as base_indices. For prefill, this will map requests
                to LoRA indices.
            sampler_indices_padded: Tensor of shape [batch_size] mapping
                requests to LoRA indices for sampler with padding.
                Same as sampler_indices, but -1 is replaced with
                max_loras.
            embeddings_indices: Tensor of shape [2, batch_size] mapping
                requests to embedding indices. First row is for embeddings
                added by the LoRAs, second row is for the LoRA.lora_a
                embeddings.
            indices_len: List of lengths of the above tensors. It contains
                (base_indices, sampler_indices, sampler_indices_padded,
                embeddings_indices).
    """
    index_mapping_indices: list[int] = list(mapping.index_mapping).copy()
    embedding_indices = index_mapping_indices.copy()
    lora_indices = index_mapping_indices.copy()

    prompt_mapping: list[int] = [
        lora_index_to_id.index(x) if x > 0 else -1 for x in mapping.prompt_mapping
    ]
    lora_idx = None
    for i in range(len(index_mapping_indices)):
        # TODO index can be slow. optimize
        lora_idx = (
            lora_index_to_id.index(index_mapping_indices[i])
            if index_mapping_indices[i] > 0
            else -1
        )
        embedding_indices[i] = lora_idx if index_mapping_indices[i] > 0 else 0
        lora_indices[i] = lora_idx

    indices_list: list[list[int] | torch.Tensor] = [
        index_mapping_indices,
        lora_indices,
        embedding_indices,
    ]

    indices = torch.tensor(indices_list, dtype=torch.long, device=device)
    prompt_mapping_tensor = torch.tensor(
        prompt_mapping, dtype=torch.long, device=device
    )
    embeddings_indices = torch.stack(
        [
            indices[2] * extra_vocab_size,
            indices[2] * (vocab_size + extra_vocab_size),
        ]
    )
    embeddings_indices = torch.where(
        embeddings_indices == -1, max_loras - 1, embeddings_indices
    )
    base_indices = indices[1]
    sampler_indices = prompt_mapping_tensor
    sampler_indices_padded = sampler_indices.clone()
    sampler_indices_padded = torch.where(
        sampler_indices_padded == -1, max_loras - 1, sampler_indices_padded
    )
    sampler_indices_padded = torch.arange(
        0, len(sampler_indices_padded), device=device, dtype=torch.long
    ) + (sampler_indices_padded * len(sampler_indices_padded))

    # Contain length of indices tensors. Used to index into each tensor.
    indices_len = [
        base_indices.shape[-1],
        sampler_indices.shape[-1],
        sampler_indices_padded.shape[-1],
        embeddings_indices.shape[-1],
    ]

    return (
        base_indices,
        sampler_indices,
        sampler_indices_padded,
        embeddings_indices,
        indices_len,
    )
```