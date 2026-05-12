---
title: colqwen3 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/configs/colqwen3/
source: sitemap
fetched_at: 2026-05-07T21:36:50.808744641-03:00
rendered_js: false
word_count: 101
summary: This document defines configuration classes for ColQwen3 model variants in vLLM, enabling model loading without trust_remote_code by mapping custom model types to standard configurations.
tags:
    - vllm
    - model-configuration
    - colqwen3
    - transformers
    - embedding-projection
category: reference
---

## vllm.transformers\_utils.configs.colqwen3 [¶](#vllm.transformers_utils.configs.colqwen3 "Permanent link")

ColQwen3 configuration that extends Qwen3VLConfig with embedding projection fields. This allows ColQwen3 models to be loaded without trust\_remote\_code by mapping their custom model\_type (colqwen3, ops\_colqwen3, etc.) to a standard config class that vLLM understands.

Supported model\_types: - colqwen3 (TomoroAI/tomoro-colqwen3-embed-8b) - ops\_colqwen3 (OpenSearch-AI/Ops-Colqwen3-4B) - qwen3\_vl\_nemotron\_embed (nvidia/nemotron-colembed-vl-8b-v2)

## ColQwen3Config [¶](#vllm.transformers_utils.configs.colqwen3.ColQwen3Config "Permanent link")

Bases: `Qwen3VLConfig`

Configuration class for ColQwen3 models.

Extends Qwen3VLConfig with additional fields used by ColQwen3 variants for the embedding projection layer.

Source code in `vllm/transformers_utils/configs/colqwen3.py`

```
classColQwen3Config(Qwen3VLConfig):
"""Configuration class for ColQwen3 models.

    Extends Qwen3VLConfig with additional fields used by ColQwen3 variants
    for the embedding projection layer.
    """

    # Accept any ColQwen3 variant model_type
    model_type = "colqwen3"

    def__init__(
        self,
        embed_dim: int | None = None,
        dims: int | None = None,
        dim: int | None = None,
        projection_dim: int | None = None,
        colbert_dim: int | None = None,
        pooling: str | None = None,
        **kwargs,
    ):
        # Store embedding projection config fields
        self.embed_dim = embed_dim
        self.dims = dims
        self.dim = dim
        self.projection_dim = projection_dim
        self.colbert_dim = colbert_dim
        self.pooling = pooling

        super().__init__(**kwargs)
```

## OpsColQwen3Config [¶](#vllm.transformers_utils.configs.colqwen3.OpsColQwen3Config "Permanent link")

Bases: `ColQwen3Config`

Configuration for OpenSearch-AI ColQwen3 variants.

Source code in `vllm/transformers_utils/configs/colqwen3.py`

```
classOpsColQwen3Config(ColQwen3Config):
"""Configuration for OpenSearch-AI ColQwen3 variants."""

    model_type = "ops_colqwen3"
```

## Qwen3VLNemotronEmbedConfig [¶](#vllm.transformers_utils.configs.colqwen3.Qwen3VLNemotronEmbedConfig "Permanent link")

Bases: `ColQwen3Config`

Configuration for NVIDIA Nemotron ColEmbed variants.

Source code in `vllm/transformers_utils/configs/colqwen3.py`

```
classQwen3VLNemotronEmbedConfig(ColQwen3Config):
"""Configuration for NVIDIA Nemotron ColEmbed variants."""

    model_type = "qwen3_vl_nemotron_embed"
```