---
title: matcher_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/fusion/matcher_utils/
source: sitemap
fetched_at: 2026-05-07T21:16:25.869573542-03:00
rendered_js: false
word_count: 20
summary: This document defines the MatcherCustomOp abstract base class, which provides a framework for implementing custom operations with fallback mechanisms for native execution within the vLLM compilation pipeline.
tags:
    - vllm
    - abstract-base-class
    - custom-operation
    - compilation-pass
    - model-optimization
    - torch-utilities
category: reference
---

## MatcherCustomOp [¶](#vllm.compilation.passes.fusion.matcher_utils.MatcherCustomOp "Permanent link")

Bases: `ABC`

Source code in `vllm/compilation/passes/fusion/matcher_utils.py`

```
classMatcherCustomOp(ABC):
    def__init__(self, enabled: bool) -> None:
        config = get_current_vllm_config()
        self.model_dtype = config.model_config.dtype if config.model_config else None
        self.device = config.device_config.device if config.device_config else None

        self.enabled = enabled
        self.forward = self.forward_custom if enabled else self.forward_native

    @abstractmethod
    defforward_custom(self, *args: Any, **kwargs: Any) -> Any:
        pass

    @abstractmethod
    defforward_native(self, *args: Any, **kwargs: Any) -> Any:
        pass

    def__call__(self, *args: Any, **kwargs: Any) -> Any:
        return self.forward(*args, **kwargs)

    defempty(self, *args: Any, **kwargs: Any) -> torch.Tensor:
        return torch.empty(*args, dtype=self.model_dtype, device=self.device, **kwargs)

    defempty_int64(self, *args: Any, **kwargs: Any) -> torch.Tensor:
        return torch.empty(*args, dtype=torch.int64, device=self.device, **kwargs)

    defempty_f32(self, *args: Any, **kwargs: Any) -> torch.Tensor:
        return torch.empty(*args, dtype=torch.float32, device=self.device, **kwargs)

    definputs(self) -> list[torch.Tensor]:
"""Utility for inputs to the pattern"""
        raise NotImplementedError
```

### inputs [¶](#vllm.compilation.passes.fusion.matcher_utils.MatcherCustomOp.inputs "Permanent link")

Utility for inputs to the pattern

Source code in `vllm/compilation/passes/fusion/matcher_utils.py`

```
definputs(self) -> list[torch.Tensor]:
"""Utility for inputs to the pattern"""
    raise NotImplementedError
```