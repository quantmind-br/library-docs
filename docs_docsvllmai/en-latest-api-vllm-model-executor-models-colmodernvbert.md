---
title: colmodernvbert - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/colmodernvbert/
source: sitemap
fetched_at: 2026-05-07T21:29:24.978516475-03:00
rendered_js: false
word_count: 13
summary: This document defines the ColModernVBertForRetrieval class, a multimodal neural network architecture that integrates visual encoders and text embeddings for late-interaction information retrieval tasks.
tags:
    - multimodal-retrieval
    - pytorch
    - neural-network-architecture
    - late-interaction
    - vllm
    - vision-language-model
category: concept
---

```
@MULTIMODAL_REGISTRY.register_processor(
    ColModernVBertMultiModalProcessor,
    info=ColModernVBertProcessingInfo,
    dummy_inputs=ColModernVBertDummyInputsBuilder,
)
@default_pooling_type(seq_pooling_type="CLS", tok_pooling_type="ALL")
classColModernVBertForRetrieval(
    nn.Module, SupportsMultiModal, SupportsLateInteraction
):
"""ColModernVBERT multimodal late-interaction retrieval model.

    Architecture:
        Image -> SiglipVisionModel -> ColModernVBertConnector
                                                   ↓
        Text  -> ModernBertEmbeddings → [merge] → ModernBertLayers → norm
                                                                      ↓
                                              custom_text_proj → L2 norm
                                                   ↓
                                          per-token 128-d embeddings
    """

    is_pooling_model = True

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        config: ColModernVBertConfig = vllm_config.model_config.hf_config
        self.config = config
        text_config = config.text_config
        quant_config = vllm_config.quant_config

        # --- Vision encoder (reuses SiglipVisionModel from siglip.py) ---
        self.vision_model = SiglipVisionModel(
            config.vision_config,
            quant_config,
            prefix=maybe_prefix(prefix, "vision_model"),
        )

        # --- Connector (pixel shuffle + linear projection) ---
        self.connector = ColModernVBertConnector(config)

        # --- Text encoder (built from ModernBERT components directly) ---
        # We build the components individually rather than wrapping
        # ``ModernBertModel`` because ``ModernBertEncoderLayer`` reads
        # ``vllm_config.model_config.hf_config`` which would be
        # ``ColModernVBertConfig``, not ``ModernBertConfig``.
        self.text_embeddings = ModernBertEmbeddings(text_config)
        self.text_layers = nn.ModuleList(
            [
                ModernBertLayer(
                    config=text_config,
                    layer_id=i,
                    prefix=f"{prefix}.text_layers.{i}",
                )
                for i in range(text_config.num_hidden_layers)
            ]
        )
        self.text_final_norm = nn.LayerNorm(
            text_config.hidden_size,
            eps=text_config.norm_eps,
            bias=text_config.norm_bias,
        )

        # --- ColBERT projection (768 -> 128, with bias) ---
        self.custom_text_proj = nn.Linear(
            text_config.hidden_size,
            config.embedding_dim,
            bias=True,
            dtype=vllm_config.model_config.head_dtype,
        )

        # --- Pooler (applies projection + L2 normalize) ---
        pooler_config = vllm_config.model_config.pooler_config
        assert pooler_config is not None
        self.pooler = pooler_for_token_embed(
            pooler_config,
            projector=self.custom_text_proj,
        )

    # ---- multimodal ---------------------------------------------------------

    def_get_image_features(
        self,
        pixel_values: torch.Tensor,
    ) -> torch.Tensor:
        # Idefics3ImageProcessor may return (batch, tiles, C, H, W);
        # flatten to (batch*tiles, C, H, W) for SiglipVisionModel.
        if pixel_values.dim() == 5:
            b, t, c, h, w = pixel_values.shape
            pixel_values = pixel_values.reshape(b * t, c, h, w)
        vision_outputs = self.vision_model(
            pixel_values.to(dtype=self.vision_model.dtype),
        )
        return self.connector(vision_outputs)

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
        pixel_values = kwargs.pop("pixel_values", None)
        if pixel_values is None:
            return []
        assert isinstance(pixel_values, torch.Tensor)
        image_features = self._get_image_features(pixel_values)
        return list(image_features)

    # ---- forward ------------------------------------------------------------

    defforward(
        self,
        input_ids: torch.Tensor,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
    ) -> torch.Tensor:
        hidden_states = self.text_embeddings(input_ids, inputs_embeds=inputs_embeds)

        for layer in self.text_layers:
            hidden_states = layer(hidden_states, positions)

        return self.text_final_norm(hidden_states)

    # ---- weight loading -----------------------------------------------------

    # Checkpoint prefix → vLLM param prefix.
    # More-specific prefixes must appear before shorter ones.
    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={
            "model.text_model.layers.": "text_layers.",
            "model.text_model.embeddings.": "text_embeddings.",
            "model.text_model.final_norm.": "text_final_norm.",
            "model.connector.modality_projection.": "connector.proj.",
            "model.custom_text_proj.": "custom_text_proj.",
            "model.vision_model.vision_model.": "vision_model.vision_model.",
            "model.": "",
        },
    )

    defload_weights(
        self,
        weights: Iterable[tuple[str, torch.Tensor]],
    ) -> set[str]:
        loader = AutoWeightsLoader(self)
        loaded_params = loader.load_weights(
            weights,
            mapper=self.hf_to_vllm_mapper,
        )

        # The pooler wraps ``custom_text_proj`` as its head projector.
        # Mark those params as loaded under the pooler path too.
        if hasattr(self, "pooler") and hasattr(self.pooler, "head"):
            head = self.pooler.head
            projector = getattr(head, "projector", None)
            if projector is not None and isinstance(projector, nn.Module):
                for pname, _ in projector.named_parameters():
                    loaded_params.add(f"pooler.head.projector.{pname}")

        return loaded_params
```