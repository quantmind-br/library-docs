---
title: siglip - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/siglip/
source: sitemap
fetched_at: 2026-05-07T21:33:15.940873629-03:00
rendered_js: false
word_count: 0
summary: This document defines the SiglipEmbeddingModel class, which integrates SigLIP vision and text transformers to provide multimodal embedding capabilities within a VLLM-based framework.
tags:
    - siglip
    - multimodal
    - pytorch
    - embedding
    - vllm
    - transformer
    - computer-vision
category: api
---

```
@default_pooling_type(seq_pooling_type="CLS")
@MULTIMODAL_REGISTRY.register_processor(
    SiglipMultiModalProcessor,
    info=SiglipProcessingInfo,
    dummy_inputs=SiglipDummyInputsBuilder,
)
classSiglipEmbeddingModel(nn.Module, SupportsMultiModal, SupportsQuant):
    is_pooling_model = True

    packed_modules_mapping = {"qkv_proj": ["q_proj", "k_proj", "v_proj"]}

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("image"):
            return None

        raise ValueError("Only image modality is supported")

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()

        config: SiglipConfig = vllm_config.model_config.hf_config
        quant_config = vllm_config.quant_config
        self.config = config

        if hasattr(config, "num_labels"):
            config.num_labels = 0

        text_config = config.text_config
        vision_config = config.vision_config

        self.text_embed_dim = text_config.hidden_size
        self.vision_embed_dim = vision_config.hidden_size
        self.text_projection_size = text_config.projection_size

        with self._mark_language_model(vllm_config):
            self.text_model = SiglipTextTransformer(
                text_config,
                quant_config=quant_config,
                prefix=maybe_prefix(prefix, "text_model"),
            )

        with self._mark_tower_model(vllm_config, "image"):
            self.vision_model = SiglipVisionTransformer(
                vision_config,
                quant_config=quant_config,
                prefix=maybe_prefix(prefix, "vision_model"),
                use_head=None,  # Allows potential pooling head
            )

        pooler_config = vllm_config.model_config.pooler_config
        assert pooler_config is not None
        self.pooler_config = pooler_config

        self.pooler = DispatchPooler.for_embedding(pooler_config)

        self._is_text_input = True

    defget_text_features(
        self,
        input_ids: torch.Tensor | None,
        position_ids: torch.Tensor,
        inputs_embeds: torch.Tensor | None = None,
    ) -> torch.Tensor:
        last_hidden_state = self.text_model(
            input_ids=input_ids,
            position_ids=position_ids,
            inputs_embeds=inputs_embeds,
        )
        text_features = self.text_model.head(last_hidden_state)

        # SigLIP uses reversed position_ids;
        # flip sequences to move EOS token to first position
        text_features = self._flip_sequences_by_position_ids(
            text_features, position_ids
        )

        return text_features

    def_flip_sequences_by_position_ids(
        self,
        features: torch.Tensor,
        position_ids: torch.Tensor,
    ) -> torch.Tensor:
"""Flip sequences so EOS token moves to first position for CLS pooling.

        SigLIP position_ids are reversed within each sequence. This method detects
        sequence boundaries and flips each sequence individually.
        """
        if len(features) == 1:
            return features

        # Detect sequence boundaries where position_ids decrease
        position_diffs = position_ids[1:] - position_ids[:-1]
        boundary_mask = position_diffs <= 0

        boundary_indices = torch.cat(
            [
                torch.tensor([0], device=features.device),
                torch.where(boundary_mask)[0] + 1,
                torch.tensor([len(features)], device=features.device),
            ]
        )

        # For each sequence [start, end), position i flips to: start + end - 1 - i
        lengths = boundary_indices[1:] - boundary_indices[:-1]
        starts = boundary_indices[:-1]
        ends = boundary_indices[1:]

        # Assign sequence ID to each element
        sequence_ids = torch.arange(
            len(lengths), device=features.device
        ).repeat_interleave(lengths)

        # Calculate flipped indices for all positions at once
        current_positions = torch.arange(len(features), device=features.device)
        flip_indices = starts[sequence_ids] + ends[sequence_ids] - 1 - current_positions

        return features[flip_indices]

    defget_image_features(
        self,
        pixel_values: torch.Tensor,
        feature_select_strategy: VisionFeatureSelectStrategy | None = None,
    ) -> torch.Tensor:
        if feature_select_strategy is None:
            feature_select_strategy = _get_vision_feature_select_strategy(
                self.pooler_config.seq_pooling_type
            )

        pooled_output = self.vision_model(
            pixel_values=pixel_values,
            select_layers=None,
            feature_select_strategy=feature_select_strategy,
        )

        return pooled_output

    def_parse_and_validate_image_input(
        self, **kwargs: object
    ) -> SiglipImagePixelInputs | None:
        pixel_values = kwargs.pop("pixel_values", None)
        if pixel_values is None:
            return None

        expected_h = expected_w = self.config.vision_config.image_size
        return SiglipImagePixelInputs(
            type="pixel_values",
            data=pixel_values,
            resolve_bindings={"h": expected_h, "w": expected_w},
        )

    def_process_image_inputs(self, inputs: SiglipImagePixelInputs) -> torch.Tensor:
        pixel_values = inputs["data"]

        return self.get_image_features(pixel_values)

    def_embed_text_input_ids(
        self,
        input_ids: torch.Tensor,
        embed_input_ids: Callable[[torch.Tensor], torch.Tensor],
        *,
        is_multimodal: torch.Tensor | None,
    ) -> torch.Tensor:
        inputs_embeds = super()._embed_text_input_ids(
            input_ids,
            embed_input_ids,
            is_multimodal=is_multimodal,
        )

        # NOTE: inputs_embeds in model runner has size text_config.projection_size
        # (instead of text_config.hidden_size) to accommodate image embeddings
        inputs_embeds_size = self.text_projection_size
        if inputs_embeds.shape[1] < inputs_embeds_size:
            inputs_embeds = torch.cat(
                [
                    inputs_embeds,
                    inputs_embeds.new_empty(
                        inputs_embeds.shape[0],
                        inputs_embeds_size - inputs_embeds.shape[1],
                    ),
                ],
                dim=1,
            )
        elif inputs_embeds.shape[1] > inputs_embeds_size:
            # No need to handle this case for now
            raise NotImplementedError

        return inputs_embeds

    defembed_input_ids(
        self,
        input_ids: torch.Tensor,
        multimodal_embeddings: MultiModalEmbeddings | None = None,
        *,
        is_multimodal: torch.Tensor | None = None,
    ) -> torch.Tensor:
        self._is_text_input = (
            multimodal_embeddings is None or len(multimodal_embeddings) == 0
        )

        if multimodal_embeddings is None or is_multimodal is None:
            return super().embed_input_ids(input_ids)

        return super().embed_input_ids(
            input_ids,
            multimodal_embeddings=multimodal_embeddings,
            is_multimodal=is_multimodal,
        )

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
        image_input = self._parse_and_validate_image_input(**kwargs)
        if image_input is None:
            return []

        vision_embeddings = self._process_image_inputs(image_input)
        return vision_embeddings

    defforward(
        self,
        input_ids: torch.Tensor | None,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
        **kwargs: object,
    ) -> torch.Tensor:
        if intermediate_tensors is not None:
            raise RuntimeError("PP is not supported for this model")

        # Multimodal inputs (image embeddings)
        if not self._is_text_input:
            return inputs_embeds

        # NOTE: inputs_embeds in model runner has size text_config.projection_size
        # (instead of text_config.hidden_size) to accommodate image embeddings
        hidden_size = self.text_embed_dim
        if inputs_embeds.shape[1] > hidden_size:
            inputs_embeds = inputs_embeds[:, :hidden_size]
        elif inputs_embeds.shape[1] < hidden_size:
            # No need to handle this case for now
            raise NotImplementedError

        return self.get_text_features(input_ids, positions, inputs_embeds)

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]):
        loader = AutoWeightsLoader(
            self,
            skip_substrs=[".position_ids"],
            ignore_unexpected_prefixes=["logit_scale.", "logit_bias."],
        )

        return loader.load_weights(weights)
```