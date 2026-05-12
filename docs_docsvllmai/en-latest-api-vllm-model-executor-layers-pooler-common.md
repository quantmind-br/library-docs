---
title: common - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/pooler/common/
source: sitemap
fetched_at: 2026-05-07T21:26:20.985748627-03:00
rendered_js: false
word_count: 19
summary: This document defines the PoolingParamsUpdate dataclass used to configure pooling parameters, specifically providing a flag to enable prompt token IDs for poolers.
tags:
    - vllm
    - pooling-params
    - token-ids
    - model-executor
    - dataclass-configuration
category: reference
---

Source code in `vllm/model_executor/layers/pooler/common.py`

```
@dataclass(frozen=True)
classPoolingParamsUpdate:
    requires_token_ids: bool = False
"""Set this flag to enable prompt token IDs for your pooler."""

    def__or__(self, other: "PoolingParamsUpdate") -> "PoolingParamsUpdate":
        return PoolingParamsUpdate(
            requires_token_ids=self.requires_token_ids or other.requires_token_ids,
        )

    defapply(self, params: PoolingParams) -> None:
        params.requires_token_ids = self.requires_token_ids
```

### requires\_token\_ids `class-attribute` `instance-attribute` [¶](#vllm.model_executor.layers.pooler.common.PoolingParamsUpdate.requires_token_ids "Permanent link")

```
requires_token_ids: bool = False
```

Set this flag to enable prompt token IDs for your pooler.