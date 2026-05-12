---
title: paddleocr_vl - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/paddleocr_vl/
source: sitemap
fetched_at: 2026-05-07T21:32:29.866893734-03:00
rendered_js: false
word_count: 0
summary: This document defines the PaddleOCRVLForConditionalGeneration model class, implementing multimodal processing, vision encoding, and position embedding logic for integration with vLLM.
tags:
    - multimodal
    - vllm
    - pytorch
    - ocr
    - computer-vision
    - machine-learning
category: reference
---

```
@MULTIMODAL_REGISTRY.register_processor(
    PaddleOCRVLMultiModalProcessor,
    info=PaddleOCRVLProcessingInfo,
    dummy_inputs=PaddleOCRVLDummyInputsBuilder,
)
classPaddleOCRVLForConditionalGeneration(nn.Module, SupportsMultiModal, SupportsMRoPE):
    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={
            "model.": "language_model.model.",
            "lm_head.": "language_model.lm_head.",
        }
    )

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("image"):
            return "<|IMAGE_START|><|IMAGE_PLACEHOLDER|><|IMAGE_END|>"

        raise ValueError("Only image modality is supported")

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        config = vllm_config.model_config.hf_config
        if hasattr(config, "text_config"):
            text_config = config.text_config.to_dict()
            unsafe_keys = ["model_type", "architectures", "tie_word_embeddings"]
            for key in unsafe_keys:
                text_config.pop(key, None)
            config.update(text_config)

        quant_config = vllm_config.quant_config

        self.config = config

        with self._mark_tower_model(vllm_config, "image"):
            self.visual = SiglipVisionModel(
                config=config.vision_config,
                quant_config=quant_config,
                prefix=maybe_prefix(prefix, "visual"),
            )
            self.mlp_AR = Projector(config, config.vision_config)

        with self._mark_language_model(vllm_config):
            self.language_model = Ernie4_5ForCausalLM(
                vllm_config=vllm_config,
                prefix=maybe_prefix(prefix, "language_model"),
            )

            for layer in self.language_model.model.layers:
                if not isinstance(layer, PPMissingLayer):
                    layer.self_attn.rotary_emb.is_neox_style = True

        self.make_empty_intermediate_tensors = (
            self.language_model.make_empty_intermediate_tensors
        )

    defcompute_logits(
        self,
        hidden_states: torch.Tensor,
    ) -> torch.Tensor | None:
        return self.language_model.compute_logits(hidden_states)

    defiter_mm_grid_thw(
        self, mm_features: list[MultiModalFeatureSpec]
    ) -> Iterator[tuple[int, int, int, int, float]]:
"""
        Iterate over multimodal features and yield grid information.

        Args:
            mm_features: List of multimodal feature specifications

        Yields:
            Tuple of (offset, grid_t, grid_h, grid_w, t_factor) for each frame/image
        """
        spatial_merge_size = self.config.vision_config.spatial_merge_size
        tokens_per_second = getattr(self.config.vision_config, "tokens_per_second", 1.0)
        for mm_feature in sorted(mm_features, key=lambda f: f.mm_position.offset):
            offset = mm_feature.mm_position.offset
            if mm_feature.modality == "image":
                t, h, w = mm_feature.data["image_grid_thw"].data.tolist()
                assert t == 1, f"Image must have 1 frame, got {t}"
                yield offset, 1, h // spatial_merge_size, w // spatial_merge_size, 1.0
            elif mm_feature.modality == "video":
                t, h, w = mm_feature.data["video_grid_thw"].data.tolist()
                second_per_grid_ts = 1.0
                if mm_feature.data.get("second_per_grid_ts", None):
                    second_per_grid_ts = mm_feature.data[
                        "second_per_grid_ts"
                    ].data.item()
                t_factor = second_per_grid_ts * tokens_per_second
                yield (
                    offset,
                    t,
                    h // spatial_merge_size,
                    w // spatial_merge_size,
                    t_factor,
                )
            else:
                raise ValueError(f"Unsupported modality: {mm_feature.modality}")

    defget_mrope_input_positions(
        self,
        input_tokens: list[int],
        mm_features: list[MultiModalFeatureSpec],
    ) -> tuple[torch.Tensor, int]:
        llm_pos_ids_list: list = []
        st = 0

        for (
            offset,
            llm_grid_t,
            llm_grid_h,
            llm_grid_w,
            t_factor,
        ) in self.iter_mm_grid_thw(mm_features):
            text_len = offset - st
            st_idx = llm_pos_ids_list[-1].max() + 1 if len(llm_pos_ids_list) > 0 else 0
            llm_pos_ids_list.append(
                np.broadcast_to(np.arange(text_len), (3, text_len)) + st_idx
            )

            grid_indices = np.indices((llm_grid_t, llm_grid_h, llm_grid_w))
            if t_factor != 1.0:
                grid_indices[0] = (grid_indices[0] * t_factor).astype(np.int64)

            llm_pos_ids_list.append(grid_indices.reshape(3, -1) + text_len + st_idx)
            st = offset + llm_grid_t * llm_grid_h * llm_grid_w

        if st < len(input_tokens):
            st_idx = llm_pos_ids_list[-1].max() + 1 if len(llm_pos_ids_list) > 0 else 0
            text_len = len(input_tokens) - st
            llm_pos_ids_list.append(
                np.broadcast_to(np.arange(text_len), (3, text_len)) + st_idx
            )

        llm_positions = np.concatenate(llm_pos_ids_list, axis=1).reshape(3, -1)
        mrope_position_delta = (llm_positions.max() + 1 - len(input_tokens)).item()

        return torch.from_numpy(llm_positions), mrope_position_delta

    def_parse_and_validate_image_input(
        self, **kwargs: object
    ) -> PaddleOCRImagePixelInputs | None:
        pixel_values = kwargs.pop("pixel_values", None)
        image_grid_thw = kwargs.pop("image_grid_thw", None)

        if pixel_values is None:
            return None

        return PaddleOCRImagePixelInputs(
            type="pixel_values",
            pixel_values=pixel_values,
            image_grid_thw=image_grid_thw,
        )

    defforward(
        self,
        input_ids: torch.Tensor | None,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
        **kwargs,
    ):
        if intermediate_tensors is not None:
            inputs_embeds = None

        return self.language_model(
            input_ids, positions, intermediate_tensors, inputs_embeds
        )

    defencode_image(
        self, pixel_values: torch.Tensor, image_grid_thw: torch.Tensor
    ) -> torch.Tensor:
        pixel_values = pixel_values.type(self.visual.dtype)
        siglip_position_ids = list()
        image_grid_hws = list()
        cu_seqlens = [0]

        thw_tuple = tuple(image_grid_thw.tolist())
        numel = np.prod(thw_tuple)
        image_grid_hws.append(thw_tuple)
        image_position_ids = torch.arange(numel) % np.prod(thw_tuple[1:])
        siglip_position_ids.append(image_position_ids)
        cu_seqlens.append(cu_seqlens[-1] + numel)

        siglip_position_ids = torch.concat(siglip_position_ids, dim=0).to(
            pixel_values.device
        )
        cu_seqlens = torch.tensor(cu_seqlens, dtype=torch.int32).to(pixel_values.device)

        vision_outputs = self.visual(
            pixel_values=pixel_values,
            image_grid_thw=image_grid_hws,
            position_ids=siglip_position_ids,
            interpolate_pos_encoding=True,
            cu_seqlens=cu_seqlens,
        )
        return vision_outputs

    def_process_image_input(
        self, image_input: PaddleOCRImagePixelInputs
    ) -> MultiModalEmbeddings:
        pixel_values = image_input.pixel_values
        image_grid_thw = image_input.image_grid_thw
        vision_outputs = tuple(
            self.encode_image(pixel, grid).squeeze(0)
            for pixel, grid in zip(pixel_values, image_grid_thw)
        )
        image_embeds = self.mlp_AR(vision_outputs, image_grid_thw)
        return image_embeds

    defembed_multimodal(self, **kwargs) -> MultiModalEmbeddings:
        image_input = self._parse_and_validate_image_input(**kwargs)
        if image_input is None:
            return ()

        multimodal_embeddings: tuple[torch.Tensor, ...] = ()
        image_embeds = self._process_image_input(image_input)
        multimodal_embeddings += tuple(image_embeds)

        return multimodal_embeddings

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        loader = AutoWeightsLoader(self)
        autoloaded_weights = loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
        return autoloaded_weights
```