---
title: layers - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/
source: sitemap
fetched_at: 2026-05-07T21:23:55.046572148-03:00
rendered_js: false
word_count: 72
summary: This document provides an overview of the modular architecture and custom layer implementations available within the framework, covering components ranging from attention mechanisms to normalization and quantization.
tags:
    - deep-learning-layers
    - neural-network-architecture
    - attention-mechanisms
    - model-components
    - layer-definitions
category: reference
---

Modules:

Name Description `activation`

Custom activation functions.

`attention` `attention_layer_base`

Base class for attention-like layers.

`batch_invariant` `conv`

Conv Layer Class.

`deepseek_v4_attention`

DeepseekV4 MLA Attention Layer

`fla` `fused_moe` `layernorm`

Custom normalization layers.

`lightning_attn` `linear` `logits_processor`

A layer that compute logits from hidden\_stats.

`mamba` `mhc` `mla` `pooler` `quantization` `resampler`

Shared resampler perceiver network used in multimodal models and

`rotary_embedding`

Rotary Positional Embeddings.

`sparse_attn_indexer`

Custom Sparse Attention Indexer layers.

`utils`

Utility methods for model layers.

`vocab_parallel_embedding`