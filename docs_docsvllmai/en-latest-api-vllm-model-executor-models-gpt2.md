---
title: gpt2 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/gpt2/
source: sitemap
fetched_at: 2026-05-07T21:30:31.35533647-03:00
rendered_js: false
word_count: 68
summary: This document provides the API reference for the GPT-2 sequence classification model implementation within the vLLM framework, detailing its architecture and class components.
tags:
    - vllm
    - gpt-2
    - sequence-classification
    - model-executor
    - deep-learning
    - transformer-models
category: reference
---

## vllm.model\_executor.models.gpt2 [¶](#vllm.model_executor.models.gpt2 "Permanent link")

Inference-only GPT-2 model compatible with HuggingFace weights.

## GPT2ForSequenceClassification [¶](#vllm.model_executor.models.gpt2.GPT2ForSequenceClassification "Permanent link")

Bases: `Module`, `SupportsCrossEncoding`

GPT2 Model for sequence classification.

This class expands GPT2Model with pooling and score functions - last token is being used for classification.

Attributes:

Name Type Description `transformer`

An instance of GPT2Model used for forward operations.

`score`

A layer for calculating logits.

`_pooler`

An instance of Pooler used for pooling operations.

Source code in `vllm/model_executor/models/gpt2.py`

```
classGPT2ForSequenceClassification(nn.Module, SupportsCrossEncoding):
"""GPT2 Model for sequence classification.

    This class expands GPT2Model with pooling and score functions - last token
    is being used for classification.

    Attributes:
        transformer: An instance of GPT2Model used for forward operations.
        score: A layer for calculating logits.
        _pooler: An instance of Pooler used for pooling operations.
    """

    is_pooling_model = True

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        config = vllm_config.model_config.hf_config
        self.transformer = GPT2Model(
            vllm_config=vllm_config, prefix=maybe_prefix(prefix, "gpt2")
        )
        self.score = nn.Linear(
            config.n_embd,
            config.num_labels,
            bias=False,
            dtype=vllm_config.model_config.head_dtype,
        )

        pooler_config = vllm_config.model_config.pooler_config
        assert pooler_config is not None

        self.pooler = DispatchPooler.for_seq_cls(pooler_config, classifier=self.score)

    defembed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
        return self.transformer.embed_input_ids(input_ids)

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]):
        loader = AutoWeightsLoader(self)
        return loader.load_weights(weights)

    defforward(
        self,
        input_ids: torch.Tensor | None,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
    ) -> torch.Tensor:
        hidden_states = self.transformer(
            input_ids=input_ids,
            position_ids=positions,
            inputs_embeds=inputs_embeds,
            intermediate_tensors=intermediate_tensors,
        )
        return hidden_states
```