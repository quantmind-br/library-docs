---
title: glm4v - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/glm4v/
source: sitemap
fetched_at: 2026-05-07T21:30:25.956738194-03:00
rendered_js: false
word_count: 0
summary: This document defines the GLM4VForCausalLM class, which implements a multimodal causal language model supporting image processing, vision-transformer integration, and specific positional encoding logic.
tags:
    - multimodal
    - glm4v
    - causal-lm
    - vllm
    - deep-learning
    - computer-vision
category: reference
---

```
@MULTIMODAL_REGISTRY.register_processor(
    GLM4VMultiModalProcessor,
    info=GLM4VProcessingInfo,
    dummy_inputs=GLM4VDummyInputsBuilder,
)
classGLM4VForCausalLM(
    ChatGLMBaseModel, SupportsMultiModal, SupportsLoRA, SupportsPP, SupportsMRoPE
):
    packed_modules_mapping = {
        "query_key_value": ["query_key_value"],
        "dense_h_to_4h": ["dense_h_to_4h"],
        "merged_proj": ["gate_proj", "dense_h_to_4h"],
    }

    defget_mm_mapping(self) -> MultiModelKeys:
"""
        Get the module prefix in multimodal models
        """
        return MultiModelKeys.from_string_field(
            language_model="transformer.encoder",
            connector="transformer.vision.linear_proj",
            tower_model="transformer.vision.transformer",
        )

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("image"):
            return "<|begin_of_image|><|endoftext|><|end_of_image|>"

        raise ValueError("Only image modality is supported")

    def__init__(
        self,
        *,
        vllm_config: VllmConfig,
        prefix: str = "",
        transformer_type: type[GLM4VModel] = GLM4VModel,
    ) -> None:
        with self._mark_composite_model(
            vllm_config,
            language_targets=GLMTransformer,
            tower_targets={"image": EVA2CLIPModel},
        ):
            super().__init__(
                vllm_config=vllm_config,
                prefix=prefix,
                transformer_type=transformer_type,
            )

        self.transformer: GLM4VModel

    def_parse_and_validate_image_input(
        self, **kwargs: object
    ) -> GLMVImagePixelInputs | None:
        pixel_values = kwargs.pop("pixel_values", None)

        if pixel_values is not None:
            expected_h = expected_w = self.config.vision_config["image_size"]
            return GLMVImagePixelInputs(
                type="pixel_values",
                data=pixel_values,
                resolve_bindings={"h": expected_h, "w": expected_w},
            )

        return None

    def_process_image_input(self, image_input: GLMVImagePixelInputs) -> torch.Tensor:
        pixel_values = image_input["data"].to(dtype=self.config.dtype)

        return self.transformer.vision(pixel_values)

    defiter_mm_grid_thw(
        self, mm_features: list[MultiModalFeatureSpec]
    ) -> Iterator[tuple[int, int, int, int]]:
        hf_config = self.config
        spatial_merge_size = hf_config.vision_config.spatial_merge_size
        for mm_feature in sorted(mm_features, key=lambda f: f.mm_position.offset):
            offset = mm_feature.mm_position.offset
            if mm_feature.modality == "image":
                t, h, w = mm_feature.data["image_grid_thw"].data.tolist()
                assert t == 1, f"Image must have 1 frame, got {t}"
                yield offset, t, h // spatial_merge_size, w // spatial_merge_size
            else:
                # glm4v only supports image modality
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
        ) in self.iter_mm_grid_thw(mm_features):
            text_len = offset - st
            st_idx = llm_pos_ids_list[-1].max() + 1 if len(llm_pos_ids_list) > 0 else 0
            llm_pos_ids_list.append(
                np.broadcast_to(np.arange(text_len), (3, text_len)) + st_idx
            )
            grid_indices = np.indices((llm_grid_t, llm_grid_h, llm_grid_w)).reshape(
                3, -1
            )
            llm_pos_ids_list.append(grid_indices + text_len + st_idx)
            # EVA2CLIPModel has embeddings for boi and eoi tokens as well
            st = offset + 1 + llm_grid_t * llm_grid_h * llm_grid_w + 1

        if st < len(input_tokens):
            text_len = len(input_tokens) - st
            st_idx = llm_pos_ids_list[-1].max() + 1 if len(llm_pos_ids_list) > 0 else 0
            llm_pos_ids_list.append(
                np.broadcast_to(np.arange(text_len), (3, text_len)) + st_idx
            )

        llm_positions = np.concatenate(llm_pos_ids_list, axis=1).reshape(3, -1)
        mrope_position_delta = (llm_positions.max() + 1 - len(input_tokens)).item()
        return torch.from_numpy(llm_positions), mrope_position_delta

    embed_input_ids = SupportsMultiModal.embed_input_ids

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
        image_input = self._parse_and_validate_image_input(**kwargs)
        if image_input is None:
            return []

        vision_embeddings = self._process_image_input(image_input)
        return vision_embeddings

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

        hidden_states = self.transformer(
            input_ids, positions, intermediate_tensors, inputs_embeds
        )

        return hidden_states
```