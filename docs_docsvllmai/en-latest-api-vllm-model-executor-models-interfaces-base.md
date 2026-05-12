---
title: interfaces_base - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/interfaces_base/
source: sitemap
fetched_at: 2026-05-07T21:30:55.067890742-03:00
rendered_js: false
word_count: 224
summary: This document defines the base interfaces and protocols for implementing custom generative and pooling models within the vLLM framework.
tags:
    - vllm
    - model-interface
    - python-protocol
    - model-executor
    - pooling-models
    - text-generation
    - api-design
category: reference
---

## VllmModel [¶](#vllm.model_executor.models.interfaces_base.VllmModel "Permanent link")

Bases: `Protocol[T_co]`

The interface required for all models in vLLM.

Source code in `vllm/model_executor/models/interfaces_base.py`

```
@runtime_checkable
classVllmModel(Protocol[T_co]):
"""The interface required for all models in vLLM."""

    def__init__(self, vllm_config: VllmConfig, prefix: str = "") -> None: ...

    defembed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
"""Apply token embeddings to `input_ids`."""
        ...

    defforward(self, input_ids: torch.Tensor, positions: torch.Tensor) -> T_co: ...
```

### embed\_input\_ids [¶](#vllm.model_executor.models.interfaces_base.VllmModel.embed_input_ids "Permanent link")

Apply token embeddings to `input_ids`.

Source code in `vllm/model_executor/models/interfaces_base.py`

```
defembed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
"""Apply token embeddings to `input_ids`."""
    ...
```

## VllmModelForPooling [¶](#vllm.model_executor.models.interfaces_base.VllmModelForPooling "Permanent link")

Bases: `VllmModel[T_co]`, `Protocol[T_co]`

The interface required for all pooling models in vLLM.

Source code in `vllm/model_executor/models/interfaces_base.py`

```
@runtime_checkable
classVllmModelForPooling(VllmModel[T_co], Protocol[T_co]):
"""The interface required for all pooling models in vLLM."""

    is_pooling_model: ClassVar[Literal[True]] = True
"""
    A flag that indicates this model supports pooling.

    Note:
        There is no need to redefine this flag if this class is in the
        MRO of your model class.
    """

    default_seq_pooling_type: ClassVar[SequencePoolingType] = "LAST"
"""
    Indicates the [vllm.config.pooler.PoolerConfig.seq_pooling_type][]
    to use by default.

    You can use the
    [vllm.model_executor.models.interfaces_base.default_pooling_type][]
    decorator to conveniently set this field.
    """

    default_tok_pooling_type: ClassVar[TokenPoolingType] = "ALL"
"""
    Indicates the [vllm.config.pooler.PoolerConfig.tok_pooling_type][]
    to use by default.

    You can use the
    [vllm.model_executor.models.interfaces_base.default_pooling_type][]
    decorator to conveniently set this field.
    """

    attn_type: ClassVar[AttnTypeStr] = "decoder"
"""
    Indicates the
    [vllm.config.model.ModelConfig.attn_type][]
    to use by default.

    You can use the
    [vllm.model_executor.models.interfaces_base.attn_type][]
    decorator to conveniently set this field.
    """

    score_type: ClassVar[ScoreType] = "bi-encoder"
"""
    Indicates the
    [vllm.config.model.ModelConfig.score_type][]
    to use by default.

    Scoring API handles score/rerank for:\n
    - "classify" task (score_type: cross-encoder models)\n
    - "embed" task (score_type: bi-encoder models)\n
    - "token_embed" task (score_type: late interaction models)\n

    score_type defaults to bi-encoder, then the Score API uses the "embed" task.\n
    If you set score_type to cross-encoder via 
    [vllm.model_executor.models.interfaces.SupportsCrossEncoding][], 
    then the Score API uses the "score" task.\n
    If you set score_type to late-interaction via 
    [vllm.model_executor.models.interfaces.SupportsLateInteraction][], 
    then the Score API uses the "token_embed" task.\n
    """

    pooler: Pooler
"""The pooler is only called on TP rank 0."""
```

### is\_pooling\_model `class-attribute` [¶](#vllm.model_executor.models.interfaces_base.VllmModelForPooling.is_pooling_model "Permanent link")

```
is_pooling_model: Literal[True] = True
```

A flag that indicates this model supports pooling.

Note

There is no need to redefine this flag if this class is in the MRO of your model class.

### pooler `instance-attribute` [¶](#vllm.model_executor.models.interfaces_base.VllmModelForPooling.pooler "Permanent link")

The pooler is only called on TP rank 0.

## VllmModelForTextGeneration [¶](#vllm.model_executor.models.interfaces_base.VllmModelForTextGeneration "Permanent link")

Bases: `VllmModel[T]`, `Protocol[T]`

The interface required for all generative models in vLLM.

Source code in `vllm/model_executor/models/interfaces_base.py`

```
@runtime_checkable
classVllmModelForTextGeneration(VllmModel[T], Protocol[T]):
"""The interface required for all generative models in vLLM."""

    defcompute_logits(
        self,
        hidden_states: T,
    ) -> T | None:
"""Return `None` if TP rank > 0."""
        ...
```

### compute\_logits [¶](#vllm.model_executor.models.interfaces_base.VllmModelForTextGeneration.compute_logits "Permanent link")

```
compute_logits(hidden_states: T) -> T | None
```

Return `None` if TP rank &gt; 0.

Source code in `vllm/model_executor/models/interfaces_base.py`

```
defcompute_logits(
    self,
    hidden_states: T,
) -> T | None:
"""Return `None` if TP rank > 0."""
    ...
```

## attn\_type [¶](#vllm.model_executor.models.interfaces_base.attn_type "Permanent link")

```
attn_type(attn_type: AttnTypeStr)
```

Decorator to set `VllmModelForPooling.attn_type`.

Source code in `vllm/model_executor/models/interfaces_base.py`

```
defattn_type(attn_type: AttnTypeStr):
"""Decorator to set `VllmModelForPooling.attn_type`."""

    deffunc(model: _T) -> _T:
        model.attn_type = attn_type  # type: ignore
        return model

    return func
```

## default\_pooling\_type [¶](#vllm.model_executor.models.interfaces_base.default_pooling_type "Permanent link")

```
default_pooling_type(
    *,
    seq_pooling_type: SequencePoolingType = "LAST",
    tok_pooling_type: TokenPoolingType = "ALL",
)
```

Decorator to set `VllmModelForPooling.default_*_pooling_type`.

Source code in `vllm/model_executor/models/interfaces_base.py`

```
defdefault_pooling_type(
    *,
    seq_pooling_type: SequencePoolingType = "LAST",
    tok_pooling_type: TokenPoolingType = "ALL",
):
"""Decorator to set `VllmModelForPooling.default_*_pooling_type`."""

    deffunc(model: _T) -> _T:
        model.default_seq_pooling_type = seq_pooling_type  # type: ignore
        model.default_tok_pooling_type = tok_pooling_type  # type: ignore
        return model

    return func
```