---
title: sequence - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/sequence/
source: sitemap
fetched_at: 2026-05-07T21:35:32.931405878-03:00
rendered_js: false
word_count: 70
summary: This document defines the IntermediateTensors data structure used for managing hidden states, residuals, and connector outputs during pipeline execution in vLLM.
tags:
    - vllm
    - pipeline-processing
    - tensor-management
    - hidden-states
    - data-structures
    - distributed-inference
category: reference
---

Sequence and its related classes.

For all pipeline stages except the last, we need to return the hidden states and residuals to be sent to the next stage. This data structure contains the hidden states and residuals for a request.

Each stage also needs to handle its own kv\_connector\_output.

Source code in `vllm/sequence.py`

```
@dataclass
classIntermediateTensors:
"""For all pipeline stages except the last, we need to return the hidden
    states and residuals to be sent to the next stage. This data structure
    contains the hidden states and residuals for a request.

    Each stage also needs to handle its own kv_connector_output.
    """

    tensors: dict[str, torch.Tensor]
    kv_connector_output: KVConnectorOutput | None

    def__init__(
        self,
        tensors: dict[str, torch.Tensor],
        kv_connector_output: KVConnectorOutput | None = None,
    ) -> None:
        # manually define this function, so that
        # Dynamo knows `IntermediateTensors()` comes from this file.
        # Otherwise, dataclass will generate this function by evaluating
        # a string, and we will lose the information about the source file.
        self.tensors = tensors
        self.kv_connector_output = kv_connector_output

    def__getitem__(self, key: str | slice):
        if isinstance(key, str):
            return self.tensors[key]
        elif isinstance(key, slice):
            return self.__class__({k: v[key] for k, v in self.tensors.items()})

    def__setitem__(self, key: str, value: torch.Tensor):
        self.tensors[key] = value

    defitems(self):
        return self.tensors.items()

    def__len__(self):
        return len(self.tensors)

    def__eq__(self, other: object):
        if not isinstance(other, self.__class__):
            return False
        if self.tensors.keys() != other.tensors.keys():
            return False
        return all(torch.equal(self.tensors[k], other.tensors[k]) for k in self.tensors)

    def__repr__(self) -> str:
        return f"IntermediateTensors(tensors={self.tensors})"

    @staticmethod
    defempty_like(
        intermediate_tensors: "IntermediateTensors",
    ) -> "IntermediateTensors":
        tensors = {
            k: torch.empty_like(v) for k, v in intermediate_tensors.tensors.items()
        }
        return IntermediateTensors(tensors)
```