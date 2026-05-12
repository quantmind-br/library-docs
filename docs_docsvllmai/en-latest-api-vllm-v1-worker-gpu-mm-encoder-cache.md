---
title: encoder_cache - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/worker/gpu/mm/encoder_cache/
source: sitemap
fetched_at: 2026-05-07T21:42:31.347509429-03:00
rendered_js: false
word_count: 0
summary: This document defines a Python class for managing multi-modal encoder caches, providing methods to add, remove, and clear cached vision embeddings and request features.
tags:
    - python-class
    - memory-management
    - caching-mechanism
    - encoder-outputs
    - multi-modal-features
category: reference
---

```
classEncoderCache:
    def__init__(self):
        # req_id -> MM features
        self.mm_features: dict[str, list[MultiModalFeatureSpec]] = {}
        # MM hash -> encoder outputs
        self.encoder_outputs: dict[str, torch.Tensor] = {}

    defadd_request(
        self, req_id: str, mm_features: list[MultiModalFeatureSpec]
    ) -> None:
        self.mm_features[req_id] = mm_features

    defremove_request(self, req_id: str) -> None:
        self.mm_features.pop(req_id, None)

    defreset_mm_cache(self) -> None:
"""
        Clear the multi-modal cache that was used during profiling,
        but no longer needed during inference.
        """
        # TODO: Implement MM budget for encoder dummy run
        pass

    defreset_encoder_cache(self) -> None:
"""Clear the GPU-side encoder cache storing vision embeddings.

        This should be called when model weights are updated to ensure
        stale embeddings computed with old weights are not reused.
        """
        self.encoder_outputs.clear()

    deffree_encoder_cache(self, mm_hash: str) -> None:
        self.encoder_outputs.pop(mm_hash, None)
```