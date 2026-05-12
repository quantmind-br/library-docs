---
title: colqwen3 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/colqwen3/
source: sitemap
fetched_at: 2026-05-07T21:29:26.8017095-03:00
rendered_js: false
word_count: 0
summary: This document defines the ColQwen3 model architecture, which extends a multi-modal vision-language backbone with a linear projection layer to generate L2-normalized per-token embeddings for late interaction retrieval tasks.
tags:
    - multi-modal
    - embeddings
    - late-interaction
    - colbert
    - qwen
    - retrieval
    - vllm
category: concept
---

```
@default_pooling_type(seq_pooling_type="CLS", tok_pooling_type="ALL")
@MULTIMODAL_REGISTRY.register_processor(
    Qwen3VLMultiModalProcessor,
    info=ColQwen3ProcessingInfo,
    dummy_inputs=Qwen3VLDummyInputsBuilder,
)
classColQwen3Model(Qwen3VLForConditionalGeneration, SupportsLateInteraction):
"""ColQwen3 late interaction model for multi-modal retrieval/reranking.

    This model extends Qwen3VLForConditionalGeneration with a ColBERT-style
    linear projection layer for per-token embeddings. It supports:
    - "token_embed" task: Per-token embeddings for late interaction scoring

    The model produces L2-normalized per-token embeddings by:
    1. Running the Qwen3-VL backbone (vision + language) to get hidden states
    2. Projecting hidden states through a linear layer (hidden_size -> embed_dim)
    3. L2-normalizing the projected embeddings

    ColBERT-style MaxSim scoring is computed externally, either client-side
    or via the late interaction scoring path in ServingScores.

    Attributes:
        custom_text_proj: Linear projection from hidden_size to embed_dim
    """

    # Mark this as a pooling model so vLLM routes to pooler path
    is_pooling_model = True

    # Override hf_to_vllm_mapper to handle ColQwen3 weight naming.
    # NOTE: WeightsMapper applies ALL matching prefix rules sequentially
    # (no early exit), so more-specific prefixes must come first.
    #   TomoroAI:    "vlm.model.visual.", "vlm.model.language_model."
    #   ColPali:     "model.visual.", "model.language_model."
    #   OpenSearch:  "visual.", "language_model." (no outer prefix,
    #                re-prefixed to "model.*" in load_weights)
    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={
            # TomoroAI naming convention (most specific first)
            "vlm.model.visual.": "visual.",
            "vlm.lm_head.": "language_model.lm_head.",
            "vlm.model.language_model.": "language_model.model.",
            # ColPali / nvidia naming convention
            "model.visual.": "visual.",
            "lm_head.": "language_model.lm_head.",
            # OpenSearch-AI: after re-prefix, "language_model.model.*"
            # becomes "model.language_model.model.*" — handle this before
            # the shorter "model.language_model." rule to avoid double map
            "model.language_model.model.": "language_model.model.",
            "model.language_model.": "language_model.model.",
        }
    )

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = "model"):
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
        self._proj_hidden_size = hidden_size

        # (TomoroAI: embed_dim, OpenSearch: dims, ColPali: dim)
        self.embed_dim: int | None = (
            getattr(config, "embed_dim", None)
            or getattr(config, "dims", None)
            or getattr(config, "dim", None)
            or getattr(config, "projection_dim", None)
            or getattr(config, "colbert_dim", None)
        )

        # Build the projection layer if embed_dim is known
        if self.embed_dim is not None:
            self.custom_text_proj = nn.Linear(
                hidden_size,
                self.embed_dim,
                bias=False,
                dtype=head_dtype,
            )
        else:
            # Will be created during load_weights when dim is inferred
            self.custom_text_proj = None

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

        if self.custom_text_proj is not None:
            proj_dtype = self.custom_text_proj.weight.dtype
            if hidden_states.dtype != proj_dtype:
                hidden_states = hidden_states.to(proj_dtype)
            hidden_states = self.custom_text_proj(hidden_states)

        # L2 normalize
        return torch.nn.functional.normalize(hidden_states, p=2, dim=-1)

    # Names used for the projection layer across different ColQwen3 variants
    _PROJ_LAYER_NAMES = {
        "custom_text_proj",  # ColPali naming
        "embedding_proj_layer",  # TomoroAI naming
    }

    def_is_proj_weight(self, name: str) -> bool:
"""Check if a weight name belongs to the projection layer."""
        return any(proj_name in name for proj_name in self._PROJ_LAYER_NAMES)

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
"""Load weights with special handling for ColQwen3 projection layer."""
        weights_list = list(weights)
        proj_weights: list[tuple[str, torch.Tensor]] = []
        model_weights: list[tuple[str, torch.Tensor]] = []

        # Scan all weight names to determine if re-prefixing is needed.
        # OpenSearch-AI models have unprefixed weights ("language_model.*",
        # "visual.*") that need "model." added so hf_to_vllm_mapper can
        # process them. Only re-prefix if ALL backbone weights are
        # unprefixed (no "vlm." or "model." prefix found).
        has_unprefixed = any(
            name.startswith("language_model.") or name.startswith("visual.")
            for name, _ in weights_list
        )
        has_prefixed = any(
            name.startswith("vlm.") or name.startswith("model.")
            for name, _ in weights_list
        )
        needs_reprefix = has_unprefixed and not has_prefixed

        for name, weight in weights_list:
            if self._is_proj_weight(name):
                proj_weights.append((name, weight))
            else:
                if needs_reprefix and not self._is_proj_weight(name):
                    name = "model." + name
                model_weights.append((name, weight))

        loader = AutoWeightsLoader(self)
        loaded = loader.load_weights(model_weights, mapper=self.hf_to_vllm_mapper)

        if proj_weights:
            model_dtype = next(self.language_model.parameters()).dtype
            model_device = next(self.language_model.parameters()).device

            for name, weight in proj_weights:
                if self.embed_dim is None and "weight" in name:
                    self.embed_dim = weight.shape[0]
                    has_bias = any("bias" in n for n, _ in proj_weights)
                    self.custom_text_proj = nn.Linear(
                        self._proj_hidden_size,
                        self.embed_dim,
                        bias=has_bias,
                        dtype=model_dtype,
                    )
                    self.custom_text_proj.to(model_device)

                if self.custom_text_proj is not None:
                    param_name = name.split(".")[-1]
                    param = getattr(self.custom_text_proj, param_name, None)
                    if param is not None:
                        weight = weight.to(device=param.device, dtype=param.dtype)
                        default_weight_loader(param, weight)
                        loaded.add(f"custom_text_proj.{param_name}")

        return loaded
```