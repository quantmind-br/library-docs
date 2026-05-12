---
title: abstract - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/pooler/abstract/
source: sitemap
fetched_at: 2026-05-07T21:26:18.971797751-03:00
rendered_js: false
word_count: 53
summary: This document defines the abstract base class and interface requirements for implementing custom pooling layers within the vLLM model execution framework.
tags:
    - vllm
    - pooling-layer
    - abstract-base-class
    - model-execution
    - developer-interface
category: reference
---

## vllm.model\_executor.layers.pooler.abstract [¶](#vllm.model_executor.layers.pooler.abstract "Permanent link")

## Pooler [¶](#vllm.model_executor.layers.pooler.abstract.Pooler "Permanent link")

Bases: `Module`, `ABC`

The interface required for all poolers used in pooling models in vLLM.

Source code in `vllm/model_executor/layers/pooler/abstract.py`

```
classPooler(nn.Module, ABC):
"""The interface required for all poolers used in pooling models in vLLM."""

    @abstractmethod
    defget_supported_tasks(self) -> Set[PoolingTask]:
"""Determine which pooling tasks are supported."""
        raise NotImplementedError

    defget_pooling_updates(self, task: PoolingTask) -> PoolingParamsUpdate:
"""
        Construct the updated pooling parameters to use for a supported task.
        """
        return PoolingParamsUpdate()

    @abstractmethod
    defforward(
        self,
        hidden_states: torch.Tensor,
        pooling_metadata: PoolingMetadata,
    ) -> PoolerOutput:
        raise NotImplementedError
```

### get\_pooling\_updates [¶](#vllm.model_executor.layers.pooler.abstract.Pooler.get_pooling_updates "Permanent link")

Construct the updated pooling parameters to use for a supported task.

Source code in `vllm/model_executor/layers/pooler/abstract.py`

```
defget_pooling_updates(self, task: PoolingTask) -> PoolingParamsUpdate:
"""
    Construct the updated pooling parameters to use for a supported task.
    """
    return PoolingParamsUpdate()
```

### get\_supported\_tasks `abstractmethod` [¶](#vllm.model_executor.layers.pooler.abstract.Pooler.get_supported_tasks "Permanent link")

```
get_supported_tasks() -> Set[PoolingTask]
```

Determine which pooling tasks are supported.

Source code in `vllm/model_executor/layers/pooler/abstract.py`

```
@abstractmethod
defget_supported_tasks(self) -> Set[PoolingTask]:
"""Determine which pooling tasks are supported."""
    raise NotImplementedError
```