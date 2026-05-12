---
title: colqwen3_5 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/colqwen3_5/
source: sitemap
fetched_at: 2026-05-07T21:29:28.276048235-03:00
rendered_js: false
word_count: 0
summary: This document defines the ColQwen3_5Model class, which extends a multi-modal Qwen model with a linear projection layer to support ColBERT-style late interaction for document retrieval and reranking tasks.
tags:
    - multi-modal
    - late-interaction
    - embedding-model
    - colbert
    - vllm
    - representation-learning
category: api
---

```
@default_pooling_type(seq_pooling_type="CLS", tok_pooling_type="ALL")
@MULTIMODAL_REGISTRY.register_processor(
    Qwen3VLMultiModalProcessor,
    info=ColQwen3_5ProcessingInfo,
    dummy_inputs=Qwen3VLDummyInputsBuilder,
)
classColQwen3_5Model(
    Qwen3_5ForConditionalGeneration,
    SupportsLateInteraction,
):
"""ColQwen3.5 late interaction model for multi-modal retrieval/reranking.

    This model extends Qwen3_5ForConditionalGeneration with a ColBERT-style
    linear projection layer for per-token embeddings. It supports:
    - "token_embed" task: Per-token embeddings for late interaction scoring

    The model produces per-token embeddings by:
    1. Running the Qwen3.5 backbone (vision + language) to get hidden states
    2. Projecting hidden states through a linear layer (hidden_size -> embed_dim)
    3. L2 normalization is handled by the pooler via PoolerNormalize

    Attributes:
        custom_text_proj: Linear projection from hidden_size to embed_dim
    """

    # Mark this as a pooling model so vLLM routes to pooler path
    is_pooling_model = True

    # Override hf_to_vllm_mapper to handle ColQwen3.5 weight naming.
    # ColPali saves weights as "language_model.*" but vLLM's
    # Qwen3_5ForCausalLM has them under "language_model.model.*".
    # Visual weights ("visual.*") already match the vLLM module path.
    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={
            "language_model.": "language_model.model.",
        }
    )

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__(vllm_config=vllm_config, prefix=prefix)

        config = vllm_config.model_config.hf_config
        head_dtype = vllm_config.model_config.head_dtype

        hidden_size = getattr(config, "hidden_size", None)
        if hidden_size is None and hasattr(config, "text_config"):
            hidden_size = config.text_config.hidden_size
        if hidden_size is None:
            raise ValueError(
                "Unable to determine text hidden size from config. "
                "Expected 'hidden_size' or 'text_config.hidden_size'."
            )

        # (ColPali: dim, projection_dim, colbert_dim)
        self.embed_dim: int = (
            getattr(config, "embed_dim", None)
            or getattr(config, "dims", None)
            or getattr(config, "dim", None)
            or getattr(config, "projection_dim", None)
            or getattr(config, "colbert_dim", None)
            or 128  # default from reference implementation
        )

        self.custom_text_proj = nn.Linear(
            hidden_size,
            self.embed_dim,
            bias=False,
            dtype=head_dtype,
        )

        pooler_config = vllm_config.model_config.pooler_config
        assert pooler_config is not None
        self.pooler = pooler_for_token_embed(
            pooler_config,
            projector=None,
        )

    defforward(
        self,
        input_ids: torch.Tensor | None,
        positions: torch.Tensor,
        intermediate_tensors=None,
        inputs_embeds: torch.Tensor | None = None,
        **kwargs: object,
    ) -> torch.Tensor:
"""Run forward pass producing per-token embeddings."""
        hidden_states = super().forward(
            input_ids=input_ids,
            positions=positions,
            intermediate_tensors=intermediate_tensors,
            inputs_embeds=inputs_embeds,
            **kwargs,
        )

        if not isinstance(hidden_states, torch.Tensor):
            return hidden_states  # type: ignore

        proj_dtype = self.custom_text_proj.weight.dtype
        if hidden_states.dtype != proj_dtype:
            hidden_states = hidden_states.to(proj_dtype)

        # Project to embedding dimension (normalization handled by pooler)
        return self.custom_text_proj(hidden_states)

    # Names used for the projection layer across different ColQwen3.5 variants
    _PROJ_LAYER_NAMES = {
        "custom_text_proj",  # ColPali naming
        "embedding_proj_layer",  # Alternative naming
    }

    def_is_proj_weight(self, name: str) -> bool:
"""Check if a weight name belongs to the projection layer."""
        return any(proj_name in name for proj_name in self._PROJ_LAYER_NAMES)

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
"""Load weights with special handling for projection layer."""
        weights_list = list(weights)
        proj_weights: list[tuple[str, torch.Tensor]] = []
        model_weights: list[tuple[str, torch.Tensor]] = []

        for name, weight in weights_list:
            if self._is_proj_weight(name):
                proj_weights.append((name, weight))
            else:
                model_weights.append((name, weight))

        loader = AutoWeightsLoader(
            self,
            skip_prefixes=["mtp."],
        )
        loaded = loader.load_weights(model_weights, mapper=self.hf_to_vllm_mapper)

        for name, weight in proj_weights:
            param_name = name.split(".")[-1]
            param = getattr(self.custom_text_proj, param_name, None)
            if param is not None:
                weight = weight.to(device=param.device, dtype=param.dtype)
                default_weight_loader(param, weight)
                loaded.add(f"custom_text_proj.{param_name}")

        return loaded
```