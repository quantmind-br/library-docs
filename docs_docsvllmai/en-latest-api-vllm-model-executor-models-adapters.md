---
title: adapters - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/adapters/
source: sitemap
fetched_at: 2026-05-07T21:28:56.959027956-03:00
rendered_js: false
word_count: 7
summary: This function provides a wrapper to extend vLLM models for sequence classification tasks by dynamically injecting a pooling layer and classification head.
tags:
    - vllm
    - model-subclassing
    - sequence-classification
    - pooling-layer
    - model-executor
    - machine-learning
category: api
---

```
defas_seq_cls_model(cls: _T) -> _T:
"""
    Subclass an existing vLLM model to support classify and score tasks.

    By default, the class probabilities are extracted from the softmaxed
    hidden state corresponding to the last token.

    Note:
        We assume that the classification head is a single linear layer
        stored as the attribute `score` of the top-level model;
        please implement your own model if this is not the case.
    """
    # Avoid modifying existing classification models
    if is_pooling_model(cls):
        return cls

    # Lazy import
    fromvllm.model_executor.layers.linearimport ReplicatedLinear
    fromvllm.model_executor.layers.poolerimport DispatchPooler
    fromvllm.model_executor.models.interfacesimport SupportsCrossEncoding

    from.utilsimport maybe_prefix

    classModelForSequenceClassification(
        _create_pooling_model_cls(cls), SupportsCrossEncoding
    ):
        def_init_pooler(
            self,
            vllm_config: "VllmConfig",
            prefix: str = "",
        ) -> "Pooler":
            hf_config = vllm_config.model_config.hf_config
            text_config = hf_config.get_text_config()
            model_config = vllm_config.model_config

            # Check if score weights are derived online from LM head
            # (same condition as load_weights branch)
            tokens = getattr(
                hf_config,
                "classifier_from_token",
                getattr(text_config, "classifier_from_token", None),
            )
            method = getattr(
                hf_config,
                "method",
                getattr(text_config, "method", None),
            )

            # Online conversion: no score weights in checkpoint, don't
            # quantize (small output_dim breaks FP8/Marlin tile alignment).
            # Checkpoint-based: respect the model's quant_config.
            quant_config = (
                None
                if (tokens is not None or method is not None)
                else vllm_config.quant_config
            )

            self.score = ReplicatedLinear(
                model_config.get_hidden_size(),
                text_config.num_labels,
                bias=False,
                params_dtype=model_config.head_dtype,
                quant_config=quant_config,
                return_bias=False,
                prefix=maybe_prefix(prefix, "score"),
            )

            pooler_config = vllm_config.model_config.pooler_config
            assert pooler_config is not None

            return DispatchPooler.for_seq_cls(pooler_config, classifier=self.score)

        defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]):
            hf_config = self.config
            text_config = hf_config.get_text_config()
            tokens = getattr(
                hf_config,
                "classifier_from_token",
                getattr(text_config, "classifier_from_token", None),
            )
            method = getattr(hf_config, "method", getattr(text_config, "method", None))

            defauto_set_score_bias(weights):
                for name, weight in weights:
                    if name == "score.bias":
                        device = self.score.weight.device
                        dtype = self.score.weight.dtype
                        bias = weight.to(device).to(dtype)
                        self.score.bias = torch.nn.Parameter(bias)
                        self.score.skip_bias_add = False
                    else:
                        yield name, weight

            weights = auto_set_score_bias(weights)
            if tokens is None and method is None:
                return super().load_weights(weights)
            else:
                # Online convert ForCausalLM into
                # ForSequenceClassification model.
                return seq_cls_model_loader(self, weights)

    ModelForSequenceClassification.__name__ = _get_pooling_model_name(
        cls.__name__, "ForSequenceClassification"
    )

    return ModelForSequenceClassification  # type: ignore
```