---
title: seqwise - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/pooler/seqwise/
source: sitemap
fetched_at: 2026-05-07T21:26:22.089063372-03:00
rendered_js: false
word_count: 68
summary: This document describes the SequencePooler class in vLLM, which extracts and aggregates specific token information from model hidden states for structured output.
tags:
    - vllm
    - neural-network
    - pooling-layer
    - sequence-processing
    - model-execution
category: reference
---

## vllm.model\_executor.layers.pooler.seqwise [¶](#vllm.model_executor.layers.pooler.seqwise "Permanent link")

Poolers that produce an output aggregating all tokens in the sequence.

Modules:

Name Description `poolers`

## SequencePooler [¶](#vllm.model_executor.layers.pooler.seqwise.SequencePooler "Permanent link")

Bases: `Pooler`

A layer that pools specific information from hidden states.

This layer does the following: 1. Extracts specific tokens or aggregates data based on pooling method. 2. Postprocesses the output based on pooling head. 3. Returns structured results as `PoolerOutput`.

Source code in `vllm/model_executor/layers/pooler/seqwise/poolers.py`

```
classSequencePooler(Pooler):
"""
    A layer that pools specific information from hidden states.

    This layer does the following:
    1. Extracts specific tokens or aggregates data based on pooling method.
    2. Postprocesses the output based on pooling head.
    3. Returns structured results as `PoolerOutput`.
    """

    def__init__(
        self,
        pooling: SequencePoolingMethod | SequencePoolingFn,
        head: SequencePoolerHead | SequencePoolingHeadFn,
    ) -> None:
        super().__init__()

        self.pooling = pooling
        self.head = head

    defget_supported_tasks(self) -> Set[PoolingTask]:
        tasks = set(POOLING_TASKS)

        if isinstance(self.pooling, SequencePoolingMethod):
            tasks &= self.pooling.get_supported_tasks()
        if isinstance(self.head, SequencePoolerHead):
            tasks &= self.head.get_supported_tasks()

        return tasks

    defget_pooling_updates(self, task: PoolingTask) -> PoolingParamsUpdate:
        updates = PoolingParamsUpdate()

        if isinstance(self.pooling, SequencePoolingMethod):
            updates |= self.pooling.get_pooling_updates(task)

        return updates

    defforward(
        self,
        hidden_states: torch.Tensor,
        pooling_metadata: PoolingMetadata,
    ) -> SequencePoolerOutput:
        pooled_data = self.pooling(hidden_states, pooling_metadata)
        pooled_data = self.head(pooled_data, pooling_metadata)
        return pooled_data
```