---
title: pooling - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/transformers/pooling/
source: sitemap
fetched_at: 2026-05-07T21:33:39.010821231-03:00
rendered_js: false
word_count: 29
summary: This document defines the SequenceClassificationMixin class in vLLM, which enables sequence classification capabilities by initializing classifiers on meta-devices and configuring model poolers.
tags:
    - vllm
    - sequence-classification
    - model-executor
    - pytorch
    - transformers
    - pooling
category: reference
---

Bases: `SupportsCrossEncoding`, `VllmModelForPooling`

Source code in `vllm/model_executor/models/transformers/pooling.py`

```
classSequenceClassificationMixin(SupportsCrossEncoding, VllmModelForPooling):
    default_seq_pooling_type = "CLS"

    def__init__(self, *, vllm_config: "VllmConfig", prefix: str = ""):
        # Skip VllmModelForPooling.__init__ and call the next class in MRO
        super(VllmModelForPooling, self).__init__(
            vllm_config=vllm_config, prefix=prefix
        )

        pooler_config = vllm_config.model_config.pooler_config
        assert pooler_config is not None

        # Certain information about the model and classifier can only be
        # inferred from the `ForSequenceClassification` class. Therefore, we
        # instantiate it on the "meta" device to avoid allocating GPU memory.
        with torch.device("meta"):
            seq_cls_model = AutoModelForSequenceClassification.from_config(
                self.config,
                dtype=self.model_config.dtype,
                trust_remote_code=self.model_config.trust_remote_code,
            )

        # When used for sequence classification, some models have their
        # pooling layers removed. Make sure this is reflected in vLLM.
        for module in seq_cls_model.modules():
            if hasattr(module, "pooler") and module.pooler is None:
                self.model.pooler = None
                break

        # Unlike `lm_head`, `classifier` is not always `nn.Linear`.
        self.classifier = getattr_iter(seq_cls_model, ["classifier", "score"], None)
        if self.classifier is None:
            raise ValueError(
                "Could not find `classifier` or `score` layer in the "
                "`AutoModelForSequenceClassification` instance."
            )
        self.init_parameters(self.classifier, dtype=self.model_config.head_dtype)

        classClassifierWithReshape(self.classifier.__class__):
"""
            Token extraction has already been applied in `pooler.pooling`.
            Add dim to match expected input shape of `classifier.forward`.
            """

            defforward(self, *args, **kwargs):
                if len(args) > 0:
                    args = (args[0].unsqueeze(1), *args[1:])
                return super().forward(*args, **kwargs)

        self.classifier.__class__ = ClassifierWithReshape

        self.pooler = DispatchPooler.for_seq_cls(
            pooler_config,
            classifier=self.classifier,
        )
```

### \_\_init\__ [¶](#vllm.model_executor.models.transformers.pooling.SequenceClassificationMixin.__init__ "Permanent link")

Source code in `vllm/model_executor/models/transformers/pooling.py`

```
def__init__(self, *, vllm_config: "VllmConfig", prefix: str = ""):
    # Skip VllmModelForPooling.__init__ and call the next class in MRO
    super(VllmModelForPooling, self).__init__(
        vllm_config=vllm_config, prefix=prefix
    )

    pooler_config = vllm_config.model_config.pooler_config
    assert pooler_config is not None

    # Certain information about the model and classifier can only be
    # inferred from the `ForSequenceClassification` class. Therefore, we
    # instantiate it on the "meta" device to avoid allocating GPU memory.
    with torch.device("meta"):
        seq_cls_model = AutoModelForSequenceClassification.from_config(
            self.config,
            dtype=self.model_config.dtype,
            trust_remote_code=self.model_config.trust_remote_code,
        )

    # When used for sequence classification, some models have their
    # pooling layers removed. Make sure this is reflected in vLLM.
    for module in seq_cls_model.modules():
        if hasattr(module, "pooler") and module.pooler is None:
            self.model.pooler = None
            break

    # Unlike `lm_head`, `classifier` is not always `nn.Linear`.
    self.classifier = getattr_iter(seq_cls_model, ["classifier", "score"], None)
    if self.classifier is None:
        raise ValueError(
            "Could not find `classifier` or `score` layer in the "
            "`AutoModelForSequenceClassification` instance."
        )
    self.init_parameters(self.classifier, dtype=self.model_config.head_dtype)

    classClassifierWithReshape(self.classifier.__class__):
"""
        Token extraction has already been applied in `pooler.pooling`.
        Add dim to match expected input shape of `classifier.forward`.
        """

        defforward(self, *args, **kwargs):
            if len(args) > 0:
                args = (args[0].unsqueeze(1), *args[1:])
            return super().forward(*args, **kwargs)

    self.classifier.__class__ = ClassifierWithReshape

    self.pooler = DispatchPooler.for_seq_cls(
        pooler_config,
        classifier=self.classifier,
    )
```