---
title: tarsier - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/tarsier/
source: sitemap
fetched_at: 2026-05-07T21:33:29.024020767-03:00
rendered_js: false
word_count: 8
summary: This document defines the TarsierForConditionalGeneration class, a multimodal PyTorch module designed for integration with vLLM, providing logic for vision tower processing, feature projection, and the injection of spatial delimiter tokens.
tags:
    - vllm
    - multimodal
    - pytorch
    - vision-tower
    - model-architecture
    - feature-projection
category: api
---

```
@MULTIMODAL_REGISTRY.register_processor(
    TarsierMultiModalProcessor,
    info=TarsierProcessingInfo,
    dummy_inputs=TarsierDummyInputsBuilder,
)
classTarsierForConditionalGeneration(nn.Module, SupportsMultiModal, SupportsPP):
    packed_modules_mapping = {
        "qkv_proj": ["q_proj", "k_proj", "v_proj"],
        "gate_up_proj": ["gate_proj", "up_proj"],
    }

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("image"):
            return "<image>"

        raise ValueError("Only image modality is supported")

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = "") -> None:
        super().__init__()

        config: TarsierHfConfig = vllm_config.model_config.hf_config
        quant_config = vllm_config.quant_config

        self.config = config  # Storing the Tarsier-specific HF config

        with self._mark_tower_model(vllm_config, "image"):
            self.vision_tower = init_vision_tower_for_tarsier(
                config,
                quant_config=quant_config,
                require_post_norm=False,
                prefix=maybe_prefix(prefix, "vision_tower"),
            )
            projector_bias = getattr(config, "multimodal_projector_bias", True)

            self.multi_modal_projector = TarsierMultiModalProjector(
                vision_hidden_size=config.vision_config.hidden_size,
                text_hidden_size=config.text_config.hidden_size,
                projector_hidden_act=config.projector_hidden_act,
                multimodal_projector_bias=projector_bias,
                quant_config=quant_config,
                prefix=maybe_prefix(prefix, "multi_modal_projector"),
            )
            self.register_buffer(
                "image_newline_idx_tensor",
                torch.tensor([config.image_newline_idx], dtype=torch.long),
                persistent=False,
            )
            self.register_buffer(
                "image_new_idx_tensor",
                torch.tensor([config.image_new_idx], dtype=torch.long),
                persistent=False,
            )

        with self._mark_language_model(vllm_config):
            self.language_model = init_vllm_registered_model(
                vllm_config=vllm_config,
                # Use text_config from Tarsier's main config
                hf_config=config.text_config,
                prefix=maybe_prefix(prefix, "language_model"),
            )

        self.make_empty_intermediate_tensors = (
            self.language_model.make_empty_intermediate_tensors
        )

    def_parse_and_validate_image_input(
        self, **kwargs: object
    ) -> TarsierImageInputs | None:
        pixel_values = kwargs.pop("pixel_values", None)
        image_embeds = kwargs.pop("image_embeds", None)

        if pixel_values is None and image_embeds is None:
            return None

        if pixel_values is not None:
            return TarsierImagePixelInputs(
                type="pixel_values",
                pixel_values=pixel_values,
            )

        if image_embeds is not None:
            return TarsierImageEmbeddingInputs(
                type="image_embeds",
                data=image_embeds,
            )

        raise AssertionError("This line should be unreachable.")

    def_image_pixels_to_features(
        self,
        vision_tower: CLIPVisionModel | SiglipVisionModel,
        pixel_values: torch.Tensor | list[torch.Tensor],
    ) -> torch.Tensor | tuple[torch.Tensor, ...]:
        # From vLLM LLaVA, vision tower output handling
        return vision_tower(
            pixel_values,
            feature_select_strategy=self.config.vision_feature_select_strategy,
        )

    def_add_tarsier_split_tokens(
        self, projected_image_features: torch.Tensor
    ) -> torch.Tensor:
"""
        Implements Tarsier's `add_split_tokens` logic.
        """
        num_images, num_projected_patches, embed_dim = projected_image_features.shape
        num_height_patches = int(math.sqrt(num_projected_patches))
        num_width_patches = num_projected_patches // num_height_patches
        device = projected_image_features.device
        embedding_layer = self.language_model.model.embed_tokens
        image_newline_emb = embedding_layer(
            self.image_newline_idx_tensor.to(device)
        ).squeeze(0)
        image_new_emb = embedding_layer(self.image_new_idx_tensor.to(device)).squeeze(0)
        try:
            current_image_features_grid = projected_image_features.view(
                num_images, num_height_patches, num_width_patches, embed_dim
            )
        except RuntimeError as e:
            raise RuntimeError(
                "Cannot reshape projected_image_features"
                f" with shape {projected_image_features.shape} "
                f"to ({num_images}, {num_height_patches},"
                f" {num_width_patches}, {embed_dim}). "
                "Ensure num_projected_patches is compatible"
                " with a grid structure. "
                f"num_projected_patches={num_projected_patches}, "
                f"derived num_height_patches={num_height_patches}. "
            ) frome

        image_newline_expanded = image_newline_emb.expand(
            (num_images, num_height_patches, 1, embed_dim)
        )
        features_with_newlines = torch.cat(
            [current_image_features_grid, image_newline_expanded],
            dim=2,  # Concatenate along width dim
        )
        new_num_patches_after_newline = num_projected_patches + num_height_patches
        features_with_newlines_flat = features_with_newlines.view(
            num_images, new_num_patches_after_newline, embed_dim
        )
        image_new_expanded = image_new_emb.expand((num_images, 1, embed_dim))
        final_image_features = torch.cat(
            [features_with_newlines_flat, image_new_expanded],
            dim=1,  # Concatenate along patch sequence dim
        )
        return final_image_features

    def_process_image_pixels(
        self,
        inputs: TarsierImagePixelInputs,
    ) -> torch.Tensor | tuple[torch.Tensor, ...]:
        pixel_values = inputs["pixel_values"]
        image_features_selected = self._image_pixels_to_features(
            self.vision_tower, pixel_values
        )  # type: ignore
        if isinstance(image_features_selected, torch.Tensor):
            projected_features = self.multi_modal_projector(image_features_selected)
            final_features = self._add_tarsier_split_tokens(projected_features)
            return final_features
        else:
            raise TypeError(
                f"_image_pixels_to_features type:"
                f" {type(image_features_selected)} is not supported"
            )

    def_process_image_input(
        self,
        image_input: TarsierImageInputs,
    ) -> torch.Tensor | tuple[torch.Tensor, ...]:
        if image_input["type"] == "image_embeds":
            projected_features = image_input["data"]
            if isinstance(projected_features, torch.Tensor):
                return self._add_tarsier_split_tokens(projected_features)
            else:
                raise ValueError(
                    "Incorrect type of image_embeds. "
                    f"Got type: {type(projected_features)}. "
                )

        return self._process_image_pixels(image_input)

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
        image_input = self._parse_and_validate_image_input(**kwargs)
        if image_input is None:
            return []
        return self._process_image_input(image_input)

    defforward(
        self,
        input_ids: torch.Tensor | None,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
        **kwargs: object,
    ) -> torch.Tensor | IntermediateTensors:
        if intermediate_tensors is not None:
            inputs_embeds = None

        hidden_states = self.language_model.model(
            input_ids=input_ids,
            positions=positions,
            intermediate_tensors=intermediate_tensors,
            inputs_embeds=inputs_embeds,
        )
        return hidden_states

    defcompute_logits(
        self,
        hidden_states: torch.Tensor,
    ) -> torch.Tensor | None:
        return self.language_model.compute_logits(hidden_states)

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        loader = AutoWeightsLoader(self)
        return loader.load_weights(weights)
```