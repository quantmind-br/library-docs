---
title: bert - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/bert/
source: sitemap
fetched_at: 2026-05-07T21:29:11.97401702-03:00
rendered_js: false
word_count: 0
summary: This document defines a BERT-based model class implementation for generating SPLADE sparse embeddings within the vLLM framework, including specialized pooling and weight-loading logic.
tags:
    - bert
    - splade
    - sparse-embeddings
    - vllm
    - pooling
    - deep-learning
    - model-architecture
category: api
---

```
@default_pooling_type(seq_pooling_type="CLS")
classBertSpladeSparseEmbeddingModel(BertEmbeddingModel):
"""
    BertEmbeddingModel + SPLADE sparse embedding.
    - Make logits by self.mlm_head
    - pooler: SPLADESparsePooler(mlm_head...)
    """

    def__init__(
        self, *, vllm_config: VllmConfig, prefix: str = "", splade_pooling: str = "max"
    ):
        super().__init__(vllm_config=vllm_config, prefix=prefix)
        cfg = vllm_config.model_config.hf_config

        # MLM head
        self.mlm_head = BertMLMHead(
            hidden_size=cfg.hidden_size,
            vocab_size=cfg.vocab_size,
            layer_norm_eps=getattr(cfg, "layer_norm_eps", 1e-12),
        )

        self._splade_pooling = splade_pooling
        pooler_config = vllm_config.model_config.pooler_config
        assert pooler_config is not None
        self.pooler = self._build_pooler(pooler_config)

    def_build_pooler(self, pooler_config: PoolerConfig) -> Pooler:
        cfg = self.model.config

        if not hasattr(self, "mlm_head"):
            self.mlm_head = BertMLMHead(
                hidden_size=cfg.hidden_size,
                vocab_size=cfg.vocab_size,
                layer_norm_eps=getattr(cfg, "layer_norm_eps", 1e-12),
            )

        # None of vLLM's built-in sequence pooling types are
        # applicable so it is overwritten by SPLADESparsePooler
        pooling_mode = getattr(self, "_splade_pooling", "max")

        cls_id = getattr(cfg, "cls_token_id", None)
        sep_id = getattr(cfg, "sep_token_id", None)

        return DispatchPooler(
            {
                "token_embed": pooler_for_token_embed(pooler_config),
                "embed": SPLADESparsePooler(
                    mlm_head=self.mlm_head,
                    cls_token_id=cls_id,
                    sep_token_id=sep_id,
                    pooling=pooling_mode,  # "max" or "sum"
                    remove_cls_sep=True,
                ),
            }
        )

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]):
        if not hasattr(self, "mlm_head"):
            cfg = self.model.config
            self.mlm_head = BertMLMHead(
                hidden_size=cfg.hidden_size,
                vocab_size=cfg.vocab_size,
                layer_norm_eps=getattr(cfg, "layer_norm_eps", 1e-12),
            )

        def_strip(name: str) -> str:
            for p in ("model.", "bert."):
                if name.startswith(p):
                    name = name[len(p) :]
            return name

        weights_list = list(weights)
        model_side: list[tuple[str, torch.Tensor]] = []
        mlm_side: list[tuple[str, torch.Tensor]] = []

        for k, w in weights_list:
            name = _strip(k)
            if name.startswith("cls.predictions."):
                mlm_side.append((name, w))
            else:
                model_side.append((name, w))

        loaded: set[str] = set()
        loaded_model = self.model.load_weights(model_side)
        loaded.update({"model." + n for n in loaded_model})

        if mlm_side:
            name_map = {
                "cls.predictions.transform.dense.weight": "mlm_head.dense.weight",
                "cls.predictions.transform.dense.bias": "mlm_head.dense.bias",
                ("cls.predictions.transform.LayerNorm.weight"): (
                    "mlm_head.layer_norm.weight"
                ),
                ("cls.predictions.transform.LayerNorm.bias"): (
                    "mlm_head.layer_norm.bias"
                ),
                "cls.predictions.decoder.weight": "mlm_head.decoder.weight",
                "cls.predictions.decoder.bias": "mlm_head.decoder.bias",
            }
            remapped = [(name_map[n], w) for n, w in mlm_side if n in name_map]
            if remapped:
                loaded_mlm = AutoWeightsLoader(self).load_weights(remapped)
                loaded.update(loaded_mlm)

        return loaded
```