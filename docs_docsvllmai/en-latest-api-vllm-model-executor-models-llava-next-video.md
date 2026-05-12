---
title: llava_next_video - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/llava_next_video/
source: sitemap
fetched_at: 2026-05-07T21:31:31.849829491-03:00
rendered_js: false
word_count: 0
summary: This document defines the LlaVA-NeXT-Video model implementation within the vLLM framework, providing the class structure for processing video inputs and performing multimodal inference.
tags:
    - vllm
    - multimodal
    - llava-next
    - video-processing
    - model-architecture
    - neural-network
category: api
---

```
@MULTIMODAL_REGISTRY.register_processor(
    LlavaNextVideoMultiModalProcessor,
    info=LlavaNextVideoProcessingInfo,
    dummy_inputs=LlavaNextVideoDummyInputsBuilder,
)
classLlavaNextVideoForConditionalGeneration(nn.Module, SupportsMultiModal, SupportsPP):
    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={
            # mapping for new names in checkpoint saved after transformers v4.52
            "model.language_model.": "language_model.model.",
            "model.vision_tower.": "vision_tower.",
            "model.multi_modal_projector.": "multi_modal_projector.",
            "model.image_newline": "image_newline",
            "lm_head.": "language_model.lm_head.",
        }
    )

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("video"):
            return "<video>"

        raise ValueError("Only video modality is supported")

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = "") -> None:
        super().__init__()

        config = vllm_config.model_config.hf_config
        quant_config = vllm_config.quant_config
        multimodal_config = vllm_config.model_config.multimodal_config

        self.config = config
        self.multimodal_config = multimodal_config

        with self._mark_tower_model(vllm_config, "video"):
            # Initialize the vision tower only up to the required feature layer
            self.vision_tower = init_vision_tower_for_llava(
                config,
                quant_config=quant_config,
                require_post_norm=False,
                prefix=maybe_prefix(prefix, "vision_tower"),
            )
            self.vision_resampler = LlavaNextVideoPooler(config)
            self.multi_modal_projector = LlavaNextMultiModalProjector(
                vision_hidden_size=config.vision_config.hidden_size,
                text_hidden_size=config.text_config.hidden_size,
                projector_hidden_act=config.projector_hidden_act,
                multimodal_projector_bias=config.multimodal_projector_bias,
            )

        with self._mark_language_model(vllm_config):
            self.language_model = init_vllm_registered_model(
                vllm_config=vllm_config,
                hf_config=config.text_config,
                prefix=maybe_prefix(prefix, "language_model"),
            )

        self.make_empty_intermediate_tensors = (
            self.language_model.model.make_empty_intermediate_tensors
        )

    def_parse_and_validate_video_input(
        self, **kwargs: object
    ) -> LlavaNextVideoPixelInputs | None:
"""
        A legal video input should have the following dimensions:
        {
            "pixel_values_videos" :
                list[b, Tensor(nb_frames, nb_channels, height, width)]
        }
        """
        pixel_values_videos = kwargs.pop("pixel_values_videos", None)

        if pixel_values_videos is None:
            return None

        expected_h = expected_w = self.config.vision_config.image_size
        return LlavaNextVideoPixelInputs(
            type="pixel_values_videos",
            pixel_values_videos=pixel_values_videos,
            resolve_bindings={
                "h": expected_h,
                "w": expected_w,
            },
        )

    def_video_pixels_to_features(
        self,
        vision_tower: CLIPVisionModel | SiglipVisionModel,
        pixel_values: torch.Tensor,
    ) -> torch.Tensor:
        # NOTE: we skip the step to select the vision feature layer since
        # this is already done inside the vision tower
        image_features = vision_tower(
            pixel_values,
            feature_select_strategy=self.config.vision_feature_select_strategy,
        )
        image_features = self.vision_resampler(image_features)
        image_features = self.multi_modal_projector(image_features)
        return image_features

    def_process_video_pixels(self, inputs: LlavaNextVideoPixelInputs):
        video_pixels = inputs["pixel_values_videos"]

        if isinstance(video_pixels, torch.Tensor):
            bn, f, c, h, w = video_pixels.shape
            stacked_pixels = video_pixels.view(bn * f, c, h, w)
            stacked_embeddings = self._video_pixels_to_features(
                self.vision_tower, stacked_pixels
            )
            embeds = stacked_embeddings.view(bn, f, *stacked_embeddings.shape[1:])

        elif is_list_of(video_pixels, torch.Tensor):
            frames_per_videos = [v.shape[0] for v in video_pixels]
            stacked_pixels = torch.cat(video_pixels, dim=0)
            stacked_embeddings = self._video_pixels_to_features(
                self.vision_tower, stacked_pixels
            )
            embeds = torch.split(stacked_embeddings, frames_per_videos, dim=0)
        else:
            raise ValueError(f"Unsupported type of video input {type(video_pixels)}")

        return [e.flatten(0, 1) for e in embeds]

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
        video_input = self._parse_and_validate_video_input(**kwargs)
        if video_input is None:
            return []
        vision_embeddings = self._process_video_pixels(video_input)
        return vision_embeddings

    defforward(
        self,
        input_ids: torch.Tensor | None,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
        **kwargs: object,
    ) -> torch.Tensor | IntermediateTensors:
"""Run forward pass for LlaVA-NeXT-Video.
        Args:
            input_ids: Flattened (concatenated) input_ids corresponding to a
                batch.
            pixel_values_videos: Pixels in each frames for each input videos.
        """
        if intermediate_tensors is not None:
            inputs_embeds = None

        hidden_states = self.language_model.model(
            input_ids, positions, intermediate_tensors, inputs_embeds=inputs_embeds
        )

        return hidden_states

    defcompute_logits(
        self,
        hidden_states: torch.Tensor,
    ) -> torch.Tensor | None:
        return self.language_model.compute_logits(hidden_states)

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        loader = AutoWeightsLoader(
            self,
            # This model doesn't support images for now
            ignore_unexpected_prefixes=["image_newline"],
        )
        return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
```