---
title: eagle2_5_vl - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/eagle2_5_vl/
source: sitemap
fetched_at: 2026-05-07T21:29:46.10753813-03:00
rendered_js: false
word_count: 0
summary: This document defines the Eagle2.5-VL multimodal model architecture, integrating a SigLIP vision encoder with a Qwen2 language model via an MLP projection layer and pixel-shuffle downsampling.
tags:
    - multimodal
    - computer-vision
    - transformer
    - eagle-2-5
    - vllm
    - neural-network
    - feature-extraction
category: concept
---

```
@MULTIMODAL_REGISTRY.register_processor(
    Eagle2_5_VLMultiModalProcessor,
    info=Eagle2_5_VLProcessingInfo,
    dummy_inputs=Eagle2_5_VLDummyInputsBuilder,
)
classEagle2_5_VLForConditionalGeneration(
    nn.Module, SupportsMultiModal, SupportsPP, SupportsLoRA
):
"""
    Eagle2.5-VL model for conditional generation.

    Architecture:
        - Vision Encoder: SigLIP
        - Language Model: Qwen2
        - Projection: MLP with pixel shuffle downsampling
    """

    supports_encoder_tp_data = True

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("image"):
            return "<image>"
        raise ValueError("Only image modality is supported")

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = "") -> None:
        super().__init__()

        config = vllm_config.model_config.hf_config
        quant_config = vllm_config.quant_config
        multimodal_config = vllm_config.model_config.multimodal_config

        self.config = config
        self.multimodal_config = multimodal_config
        self.use_data_parallel = multimodal_config.mm_encoder_tp_mode == "data"

        # Image configuration
        image_size = (
            getattr(config, "force_image_size", None) or config.vision_config.image_size
        )
        patch_size = config.vision_config.patch_size
        self.patch_size = patch_size
        self.downsample_ratio = getattr(config, "downsample_ratio", 0.5)
        self.num_image_token = int(
            (image_size // patch_size) ** 2 * (self.downsample_ratio**2)
        )

        self.select_layer = getattr(config, "select_layer", -1)

        with self._mark_tower_model(vllm_config, "image"):
            # Vision encoder (SigLIP)
            self.vision_model = self._init_vision_model(
                config,
                quant_config=quant_config,
                prefix=maybe_prefix(prefix, "vision_model"),
            )

            # MLP projection
            self.mlp1 = self._init_mlp1(config)

        with self._mark_language_model(vllm_config):
            # Language model (Qwen2)
            self.language_model = init_vllm_registered_model(
                vllm_config=vllm_config,
                hf_config=config.text_config,
                prefix=maybe_prefix(prefix, "language_model"),
            )

        self.img_context_token_id = None

        self.make_empty_intermediate_tensors = (
            self.language_model.make_empty_intermediate_tensors
        )

    def_init_vision_model(
        self,
        config: PretrainedConfig,
        quant_config: QuantizationConfig | None,
        prefix: str,
    ):
"""Initialize SigLIP vision model."""
        vision_config = config.vision_config

        # Determine number of hidden layers based on select_layer
        vision_feature_layer = self.select_layer
        if vision_feature_layer < 0:
            num_hidden_layers = (
                vision_config.num_hidden_layers + vision_feature_layer + 1
            )
        else:
            num_hidden_layers = vision_feature_layer + 1

        # Disable the pooling head - Eagle2.5 needs all patch tokens,
        # not a single pooled output
        vision_config.vision_use_head = False

        return SiglipVisionModel(
            vision_config,
            quant_config=quant_config,
            num_hidden_layers_override=num_hidden_layers,
            prefix=prefix,
        )

    def_init_mlp1(self, config: PretrainedConfig) -> nn.Module:
"""Initialize MLP projection layer."""
        vit_hidden_size = config.vision_config.hidden_size
        llm_hidden_size = config.text_config.hidden_size

        return nn.Sequential(
            nn.LayerNorm(vit_hidden_size * int(1 / self.downsample_ratio) ** 2),
            nn.Linear(
                vit_hidden_size * int(1 / self.downsample_ratio) ** 2, llm_hidden_size
            ),
            nn.GELU(),
            nn.Linear(llm_hidden_size, llm_hidden_size),
        )

    defpixel_shuffle(self, x: torch.Tensor, scale_factor: float = 0.5) -> torch.Tensor:
"""
        Pixel shuffle operation for downsampling vision features.

        Args:
            x: Input tensor of shape (n, w, h, c)
            scale_factor: Downsampling factor

        Returns:
            Downsampled tensor
        """
        n, w, h, c = x.size()
        # N, W, H, C --> N, W, H * scale, C // scale
        x = x.view(n, w, int(h * scale_factor), int(c / scale_factor))
        # N, W, H * scale, C // scale --> N, H * scale, W, C // scale
        x = x.permute(0, 2, 1, 3).contiguous()
        # N, H * scale, W, C // scale --> N, H * scale, W * scale, C // (scale ** 2)
        x = x.view(
            n,
            int(h * scale_factor),
            int(w * scale_factor),
            int(c / (scale_factor * scale_factor)),
        )
        x = x.permute(0, 2, 1, 3).contiguous()
        return x

    defextract_feature(self, pixel_values: torch.Tensor) -> torch.Tensor:
"""
        Extract visual features from pixel values.

        Args:
            pixel_values: Input pixel values of shape (batch, channels, height, width)

        Returns:
            Visual embeddings
        """
        vit_embeds = self.vision_model(pixel_values=pixel_values)

        h = w = int(vit_embeds.shape[1] ** 0.5)
        vit_embeds = vit_embeds.reshape(vit_embeds.shape[0], h, w, -1)
        vit_embeds = self.pixel_shuffle(vit_embeds, scale_factor=self.downsample_ratio)
        vit_embeds = vit_embeds.reshape(vit_embeds.shape[0], -1, vit_embeds.shape[-1])
        vit_embeds = self.mlp1(vit_embeds)
        return vit_embeds

    def_parse_and_validate_image_input(
        self, **kwargs: object
    ) -> Eagle2_5_VLImageInputs | None:
"""Parse and validate image inputs."""
        pixel_values_flat = kwargs.pop("pixel_values_flat", None)
        image_num_patches = kwargs.pop("image_num_patches", None)
        image_embeds = kwargs.pop("image_embeds", None)

        if pixel_values_flat is None and image_embeds is None:
            return None

        if image_embeds is not None:
            return Eagle2_5_VLImageEmbeddingInputs(
                type="image_embeds",
                data=image_embeds,
            )

        image_token_id = kwargs.get("image_token_id")
        if image_token_id is not None:
            if isinstance(image_token_id, torch.Tensor):
                image_token_id = image_token_id.flatten().unique().item()
            assert isinstance(image_token_id, int)
            self.img_context_token_id = image_token_id

        if pixel_values_flat is not None:
            image_size = getattr(self.config, "force_image_size", None)
            if image_size is None:
                image_size = self.config.vision_config.image_size
            expected_h = expected_w = image_size
            resolve_bindings = {"h": expected_h, "w": expected_w}

            return Eagle2_5_VLImagePixelInputs(
                type="pixel_values",
                pixel_values_flat=pixel_values_flat,
                num_patches=image_num_patches,
                resolve_bindings=resolve_bindings,
            )

        raise AssertionError("This line should be unreachable.")

    def_process_image_input(
        self,
        image_input: Eagle2_5_VLImageInputs,
    ) -> tuple[torch.Tensor, ...]:
"""Process image input to get embeddings."""
        if image_input["type"] == "image_embeds":
            return image_input["data"]

        assert self.vision_model is not None

        image_embeds = self.extract_feature(image_input["pixel_values_flat"])

        num_patches = image_input["num_patches"]

        # Only one image in the current batch
        if len(num_patches) == 1:
            return (image_embeds.view(-1, self.config.text_config.hidden_size),)

        # Split embeddings by image
        feature_size = image_embeds.shape[1]
        image_embeds = image_embeds.view(-1, self.config.text_config.hidden_size)
        image_feature_sizes = [
            num_patches * feature_size for num_patches in num_patches
        ]
        return image_embeds.split(image_feature_sizes)

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
"""Embed multimodal inputs."""
        image_input = self._parse_and_validate_image_input(**kwargs)
        if image_input is None:
            return []

        image_embeddings = self._process_image_input(image_input)
        return tuple(image_embeddings)

    defembed_input_ids(
        self,
        input_ids: torch.Tensor,
        multimodal_embeddings: MultiModalEmbeddings | None = None,
        *,
        is_multimodal: torch.Tensor | None = None,
    ) -> torch.Tensor:
"""Embed input IDs with optional multimodal embeddings."""
        if multimodal_embeddings is None or is_multimodal is None:
            return super().embed_input_ids(input_ids)

        return super().embed_input_ids(
            input_ids,
            multimodal_embeddings=multimodal_embeddings,
            is_multimodal=is_multimodal,
        )

    defforward(
        self,
        input_ids: torch.Tensor | None,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
        **kwargs: object,
    ) -> IntermediateTensors:
"""Forward pass through the model."""
        if intermediate_tensors is not None:
            inputs_embeds = None

        forward_kwargs = {
            "input_ids": input_ids,
            "positions": positions,
            "intermediate_tensors": intermediate_tensors,
            "inputs_embeds": inputs_embeds,
        }

        hidden_states = self.language_model.model(**forward_kwargs)
        return hidden_states

    defcompute_logits(
        self,
        hidden_states: torch.Tensor,
    ) -> torch.Tensor | None:
"""Compute logits from hidden states."""
        return self.language_model.compute_logits(hidden_states)

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
"""Load model weights."""
        loader = AutoWeightsLoader(self)
        return loader.load_weights(weights)

    defget_mm_mapping(self) -> MultiModelKeys:
"""Get the module prefix mapping for multimodal models."""
        return MultiModelKeys.from_string_field(
            language_model="language_model",
            connector="mlp1",
            tower_model="vision_model",
        )
```