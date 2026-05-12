---
title: tokwise - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/pooler/tokwise/
source: sitemap
fetched_at: 2026-05-07T21:26:27.038121567-03:00
rendered_js: false
word_count: 68
summary: This document defines the TokenPooler class in vLLM, which extracts and aggregates hidden state information to produce structured token-level output.
tags:
    - vllm
    - token-pooling
    - model-executor
    - hidden-states
    - layer-architecture
category: reference
---

## vllm.model\_executor.layers.pooler.tokwise [¶](#vllm.model_executor.layers.pooler.tokwise "Permanent link")

Poolers that produce an output for each token in the sequence.

Modules:

Name Description `poolers`

## TokenPooler [¶](#vllm.model_executor.layers.pooler.tokwise.TokenPooler "Permanent link")

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