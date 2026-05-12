---
title: interface - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/sample/logits_processor/interface/
source: sitemap
fetched_at: 2026-05-07T21:41:25.223990922-03:00
rendered_js: false
word_count: 130
summary: This document defines the abstract base class LogitsProcessor, which provides the interface for implementing custom logic to transform logits during the sampling process in vLLM.
tags:
    - vllm
    - logits-processor
    - python-interface
    - abstract-base-class
    - machine-learning
    - sampling
category: reference
---

Bases: `ABC`

Source code in `vllm/v1/sample/logits_processor/interface.py`

```
classLogitsProcessor(ABC):
    @classmethod
    defvalidate_params(cls, sampling_params: SamplingParams):
"""Validate sampling params for this logits processor.

        Raise ValueError for invalid ones.
        """
        return None

    @abstractmethod
    def__init__(
        self, vllm_config: "VllmConfig", device: torch.device, is_pin_memory: bool
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    defapply(self, logits: torch.Tensor) -> torch.Tensor:
"""Apply LogitsProcessor to batch logits tensor.

        The updated tensor must be returned but may be
        modified in-place.
        """
        raise NotImplementedError

    @abstractmethod
    defis_argmax_invariant(self) -> bool:
"""True if logits processor has no impact on the
        argmax computation in greedy sampling.
        NOTE: may or may not have the same value for all
        instances of a given LogitsProcessor subclass,
        depending on subclass implementation.
        """
        raise NotImplementedError

    @abstractmethod
    defupdate_state(
        self,
        batch_update: "BatchUpdate | None",
    ) -> None:
"""Called when there are new output tokens, prior
        to each forward pass.

        Args:
            batch_update: Non-None iff there have been changes
                to the batch makeup.
        """
        raise NotImplementedError
```

### apply `abstractmethod` [¶](#vllm.v1.sample.logits_processor.interface.LogitsProcessor.apply "Permanent link")

Apply LogitsProcessor to batch logits tensor.

The updated tensor must be returned but may be modified in-place.

Source code in `vllm/v1/sample/logits_processor/interface.py`

```
@abstractmethod
defapply(self, logits: torch.Tensor) -> torch.Tensor:
"""Apply LogitsProcessor to batch logits tensor.

    The updated tensor must be returned but may be
    modified in-place.
    """
    raise NotImplementedError
```

### is\_argmax\_invariant `abstractmethod` [¶](#vllm.v1.sample.logits_processor.interface.LogitsProcessor.is_argmax_invariant "Permanent link")

```
is_argmax_invariant() -> bool
```

True if logits processor has no impact on the argmax computation in greedy sampling. NOTE: may or may not have the same value for all instances of a given LogitsProcessor subclass, depending on subclass implementation.

Source code in `vllm/v1/sample/logits_processor/interface.py`

```
@abstractmethod
defis_argmax_invariant(self) -> bool:
"""True if logits processor has no impact on the
    argmax computation in greedy sampling.
    NOTE: may or may not have the same value for all
    instances of a given LogitsProcessor subclass,
    depending on subclass implementation.
    """
    raise NotImplementedError
```

### update\_state `abstractmethod` [¶](#vllm.v1.sample.logits_processor.interface.LogitsProcessor.update_state "Permanent link")

```
update_state(batch_update: BatchUpdate | None) -> None
```

Called when there are new output tokens, prior to each forward pass.

Parameters:

Name Type Description Default `batch_update` `BatchUpdate | None`

Non-None iff there have been changes to the batch makeup.

*required*

Source code in `vllm/v1/sample/logits_processor/interface.py`

```
@abstractmethod
defupdate_state(
    self,
    batch_update: "BatchUpdate | None",
) -> None:
"""Called when there are new output tokens, prior
    to each forward pass.

    Args:
        batch_update: Non-None iff there have been changes
            to the batch makeup.
    """
    raise NotImplementedError
```

### validate\_params `classmethod` [¶](#vllm.v1.sample.logits_processor.interface.LogitsProcessor.validate_params "Permanent link")

Validate sampling params for this logits processor.

Raise ValueError for invalid ones.

Source code in `vllm/v1/sample/logits_processor/interface.py`

```
@classmethod
defvalidate_params(cls, sampling_params: SamplingParams):
"""Validate sampling params for this logits processor.

    Raise ValueError for invalid ones.
    """
    return None
```