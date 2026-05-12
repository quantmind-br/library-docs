---
title: poolers - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/pooler/tokwise/poolers/
source: sitemap
fetched_at: 2026-05-07T21:26:28.874707378-03:00
rendered_js: false
word_count: 49
summary: This document defines the ClassTokenPooler class, a structural layer designed to extract and aggregate information from hidden states in neural networks for structured output generation.
tags:
    - pooler
    - neural-networks
    - token-pooling
    - hidden-states
    - deep-learning
    - vllm-framework
category: reference
---

Bases: `Pooler`

A layer that pools specific information from hidden states.

This layer does the following: 1. Extracts specific tokens or aggregates data based on pooling method. 2. Postprocesses the output based on pooling head. 3. Returns structured results as `PoolerOutput`.

Source code in `vllm/model_executor/layers/pooler/tokwise/poolers.py`

```
classTokenPooler(Pooler):
"""
    A layer that pools specific information from hidden states.

    This layer does the following:
    1. Extracts specific tokens or aggregates data based on pooling method.
    2. Postprocesses the output based on pooling head.
    3. Returns structured results as `PoolerOutput`.
    """

    def__init__(
        self,
        pooling: TokenPoolingMethod | TokenPoolingFn,
        head: TokenPoolerHead | TokenPoolingHeadFn | None = None,
    ) -> None:
        super().__init__()

        self.pooling = pooling
        self.head = head

    defget_supported_tasks(self) -> Set[PoolingTask]:
        tasks = set(POOLING_TASKS)

        if isinstance(self.pooling, TokenPoolingMethod):
            tasks &= self.pooling.get_supported_tasks()
        if isinstance(self.head, TokenPoolerHead):
            tasks &= self.head.get_supported_tasks()

        return tasks

    defget_pooling_updates(self, task: PoolingTask) -> PoolingParamsUpdate:
        updates = PoolingParamsUpdate()

        if isinstance(self.pooling, TokenPoolingMethod):
            updates |= self.pooling.get_pooling_updates(task)

        return updates

    defforward(
        self,
        hidden_states: torch.Tensor,
        pooling_metadata: PoolingMetadata,
    ) -> TokenPoolerOutput:
        pooled_data = self.pooling(hidden_states, pooling_metadata)
        if self.head is not None:
            pooled_data = self.head(pooled_data, pooling_metadata)
        return pooled_data
```