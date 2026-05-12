---
title: transformers - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/transformers/
source: sitemap
fetched_at: 2026-05-07T21:33:33.220335909-03:00
rendered_js: false
word_count: 80
summary: This document provides an overview of the vLLM transformers model executor backend, outlining its internal modules and the dynamic attribute handling mechanism for model loading.
tags:
    - vllm
    - transformers-backend
    - model-executor
    - python-api
    - module-architecture
category: reference
---

## vllm.model\_executor.models.transformers [¶](#vllm.model_executor.models.transformers "Permanent link")

Wrapper around `transformers` models

Modules:

Name Description `base`

Transformers modeling backend base class.

`causal`

Transformers modeling backend mixin for causal language models.

`legacy`

Transformers modeling backend mixin for legacy models.

`moe`

Transformers modeling backend mixin for Mixture of Experts (MoE) models.

`multimodal`

Transformers modeling backend mixin for multi-modal models.

`pooling`

Transformers modeling backend mixins for pooling models.

`utils`

Transformers modeling backend utilities.

## \_\_getattr\__ [¶](#vllm.model_executor.models.transformers.__getattr__ "Permanent link")

Handle imports of non-existent classes with a helpful error message.

Source code in `vllm/model_executor/models/transformers/__init__.py`

```
def__getattr__(name: str):
"""Handle imports of non-existent classes with a helpful error message."""
    if name not in globals():
        raise AttributeError(
            "The Transformers modeling backend does not currently have a class to "
            f"handle the requested model type: {name}. Please open an issue at "
            "https://github.com/vllm-project/vllm/issues/new"
        )
    return globals()[name]
```