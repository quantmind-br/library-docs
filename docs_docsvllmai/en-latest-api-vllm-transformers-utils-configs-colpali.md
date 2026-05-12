---
title: colpali - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/configs/colpali/
source: sitemap
fetched_at: 2026-05-07T21:36:49.813579588-03:00
rendered_js: false
word_count: 66
summary: This document defines the ColPaliConfig class, which extends the PaliGemma configuration to support embedding projection fields and enable seamless loading of ColPali models within the vLLM framework.
tags:
    - vllm
    - model-configuration
    - colpali
    - paligemma
    - embedding-projection
    - transformers-utils
category: reference
---

## vllm.transformers\_utils.configs.colpali [¶](#vllm.transformers_utils.configs.colpali "Permanent link")

ColPali configuration that extends PaliGemmaConfig with embedding projection fields. This allows ColPali models to be loaded without trust\_remote\_code by mapping their custom model\_type (colpali) to a standard config class that vLLM understands.

Supported model\_types: - colpali (vidore/colpali-v1.3-hf)

## ColPaliConfig [¶](#vllm.transformers_utils.configs.colpali.ColPaliConfig "Permanent link")

Bases: `PaliGemmaConfig`

Configuration class for ColPali models.

Extends PaliGemmaConfig with additional fields used by ColPali variants for the embedding projection layer.

Source code in `vllm/transformers_utils/configs/colpali.py`

```
classColPaliConfig(PaliGemmaConfig):
"""Configuration class for ColPali models.

    Extends PaliGemmaConfig with additional fields used by ColPali variants
    for the embedding projection layer.
    """

    model_type = "colpali"

    def__init__(
        self,
        embedding_dim: int | None = None,
        embed_dim: int | None = None,
        dim: int | None = None,
        colbert_dim: int | None = None,
        pooling: str | None = None,
        vlm_config: dict | None = None,
        **kwargs,
    ):
        # Store embedding projection config fields
        self.embedding_dim = embedding_dim
        self.embed_dim = embed_dim
        self.dim = dim
        self.colbert_dim = colbert_dim
        self.pooling = pooling

        # The HF checkpoint nests PaliGemma config inside "vlm_config".
        # Flatten it so PaliGemmaConfig receives vision_config, text_config,
        # image_token_index, etc. directly.
        # Use setdefault to avoid overwriting keys already set (e.g.
        # model_type="colpali" would be clobbered by "paligemma" from
        # vlm_config).
        if vlm_config is not None:
            vlm_dict = (
                vlm_config if isinstance(vlm_config, dict) else vlm_config.to_dict()
            )
            _conflicting = {"model_type", "_name_or_path"}
            for key, value in vlm_dict.items():
                if key not in _conflicting:
                    kwargs.setdefault(key, value)

        super().__init__(**kwargs)
```