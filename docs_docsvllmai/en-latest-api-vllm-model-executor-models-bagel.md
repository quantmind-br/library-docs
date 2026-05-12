---
title: bagel - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/bagel/
source: sitemap
fetched_at: 2026-05-07T21:29:06.066127255-03:00
rendered_js: false
word_count: 0
summary: This document defines the BagelForConditionalGeneration class, which integrates a vision model and language model for multimodal understanding within the vLLM framework.
tags:
    - vllm
    - multimodal
    - computer-vision
    - machine-learning
    - model-architecture
    - siglip
    - qwen2
category: api
---

```
@MULTIMODAL_REGISTRY.register_processor(
    BagelMultiModalProcessor,
    info=BagelProcessingInfo,
    dummy_inputs=BagelDummyInputsBuilder,
)
classBagelForConditionalGeneration(
    nn.Module, SupportsMultiModal, SupportsLoRA, SupportsPP
):
"""
    BAGEL: A unified multimodal model for image understanding and generation.

    For vLLM, we focus on the image understanding (vision-to-text) capabilities.
    The image generation part is not supported in vLLM.
    """

    # Weight mapping from HF to vLLM
    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={
            "language_model.": "language_model.",
            "vit_model.": "vit_model.",
            "connector.": "connector.",
            "vit_pos_embed.": "vit_pos_embed.",
        }
    )

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("image"):
            return "<|image_pad|>"

        raise ValueError("Only image modality is supported")

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()

        config = vllm_config.model_config.hf_config
        quant_config = vllm_config.quant_config
        multimodal_config = vllm_config.model_config.multimodal_config

        # Ensure we have a BagelConfig (check by name to handle trust_remote_code)
        # When trust_remote_code=True, the config comes from transformers_modules
        if type(config).__name__ != "BagelConfig":
            raise ValueError(
                f"Expected BagelConfig, got {type(config).__name__}. "
                "Make sure the model config is properly loaded."
            )

        self.config = config
        self.multimodal_config = multimodal_config

        # Initialize language model (Qwen2)
        # Pass the llm_config from BagelConfig to initialize Qwen2 properly
        with self._mark_language_model(vllm_config):
            self.language_model = init_vllm_registered_model(
                vllm_config=vllm_config,
                hf_config=config.llm_config,
                prefix=maybe_prefix(prefix, "language_model"),
                architectures=["Qwen2ForCausalLM"],
            )

        # Initialize vision model (SigLIP) if visual understanding is enabled
        if config.visual_und:
            # Fix vit_config: checkpoint has 26 layers (0-25) but config says 27
            # Also disable head as it's not in checkpoint
            vit_config = config.vit_config
            if vit_config.num_hidden_layers == 27:
                logger.warning(
                    "Overriding vit_config.num_hidden_layers from 27 to 26 "
                    "to match the Bagel model checkpoint."
                )
                vit_config.num_hidden_layers = 26
            if not hasattr(vit_config, "vision_use_head"):
                logger.warning(
                    "Setting vit_config.vision_use_head to False as it is not "
                    "present in the Bagel model checkpoint."
                )
                vit_config.vision_use_head = False

            with self._mark_tower_model(vllm_config, "image"):
                self.vit_model = SiglipVisionModel(
                    config=vit_config,
                    quant_config=quant_config,
                    prefix=maybe_prefix(prefix, "vit_model"),
                )

                # Initialize connector (MLP)
                vit_hidden_size = config.vit_config.hidden_size
                llm_hidden_size = config.llm_config.hidden_size

                self.connector = BagelVisionMLP(
                    in_features=vit_hidden_size,
                    hidden_features=llm_hidden_size,
                    out_features=llm_hidden_size,
                    act_layer=config.connector_act,
                    quant_config=quant_config,
                    prefix=maybe_prefix(prefix, "connector"),
                )

                # Position embedding for vision tokens
                self.vit_pos_embed = PositionEmbedding(
                    max_num_patch_per_side=config.vit_max_num_patch_per_side,
                    hidden_size=llm_hidden_size,
                )
        else:
            self.vit_model = StageMissingLayer("image_tower")
            self.connector = StageMissingLayer("image_tower")
            self.vit_pos_embed = StageMissingLayer("image_tower")

        self.make_empty_intermediate_tensors = (
            self.language_model.make_empty_intermediate_tensors
        )

    def_parse_and_validate_image_input(
        self, **kwargs: object
    ) -> BagelImageInputs | None:
        pixel_values = kwargs.pop("pixel_values", None)

        if pixel_values is None:
            return None

        return BagelImagePixelInputs(
            type="pixel_values",
            pixel_values=pixel_values,
        )

    def_process_image_input(
        self, image_input: BagelImageInputs
    ) -> tuple[torch.Tensor, ...]:
"""Process image inputs through vision encoder and connector."""
        pixel_values = image_input["pixel_values"]

        # Handle potential extra batch dimension
        # Expected shape: (batch_size * num_images, 3, H, W)
        # But might receive: (batch_size, num_images, 3, H, W)
        if pixel_values.ndim == 5:
            # Flatten batch and num_images dimensions
            batch_size, num_images, channels, height, width = pixel_values.shape
            pixel_values = pixel_values.reshape(
                batch_size * num_images, channels, height, width
            )

        # Get vision features from SigLIP
        # pixel_values shape: (batch_size * num_images, 3, H, W)
        vision_features = self.vit_model(pixel_values)

        # Pass through connector
        vision_embeds = self.connector(vision_features)

        # Add position embeddings
        batch_size, num_patches, hidden_size = vision_embeds.shape
        patch_size = self.config.vit_config.patch_size
        image_size = self.config.vit_config.image_size

        # Calculate grid dimensions
        num_patches_per_side = image_size // patch_size

        # Create flattened position IDs (0 to num_patches-1)
        # For BAGEL, we use extrapolate mode by default
        h_coords = torch.arange(num_patches_per_side, device=vision_embeds.device)
        w_coords = torch.arange(num_patches_per_side, device=vision_embeds.device)
        position_ids = (
            h_coords[:, None] * self.config.vit_max_num_patch_per_side + w_coords
        ).flatten()
        position_ids = position_ids.unsqueeze(0).expand(batch_size, -1).flatten()

        # Add position embeddings
        pos_embeds = self.vit_pos_embed(position_ids)
        pos_embeds = pos_embeds.reshape(batch_size, num_patches, hidden_size)
        # Ensure pos_embeds are on the same device as vision_embeds
        pos_embeds = pos_embeds.to(vision_embeds.device)
        vision_embeds = vision_embeds + pos_embeds

        # Split by image
        return tuple(vision_embeds)

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
"""Get multimodal embeddings from input."""
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
"""Run forward pass for BAGEL.

        Args:
            input_ids: Flattened (concatenated) input_ids corresponding to a batch.
            positions: Flattened (concatenated) position ids corresponding to a batch.
            intermediate_tensors: Intermediate tensors from prior forward pass.
            inputs_embeds: Optional tensor of input embeddings.
        """
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
"""Load weights from checkpoint."""
        # Skip generation-related weights since we only support text2text and image2text
        # Filter out all image generation components:
        # - 'moe_gen': MoE generation weights
        # - 'latent_pos_embed': Latent position embeddings for VAE
        # - 'llm2vae', 'vae2llm': LLM-VAE projections
        # - 'time_embedder': Timestep embeddings for diffusion
        # - VAE encoder/decoder: Use specific prefixes to avoid matching vision encoder
        generation_keywords = [
            "moe_gen",
            "latent_pos_embed",
            "llm2vae",
            "vae2llm",
            "time_embedder",
        ]
        vae_prefixes = [
            "decoder.",
            "encoder.",
        ]  # VAE encoder/decoder, not vision encoder
        filtered_weights = []
        for name, tensor in weights:
            # Skip generation-related keywords
            if any(skip in name for skip in generation_keywords):
                continue
            if any(name.startswith(prefix) for prefix in vae_prefixes):
                continue

            if "patch_embedding.weight" in name and tensor.ndim == 2:
                out_channels = tensor.shape[0]
                in_features = tensor.shape[1]
                patch_size = self.config.vit_config.patch_size
                in_channels = self.config.vit_config.num_channels
                if in_features == in_channels * patch_size * patch_size:
                    tensor = tensor.reshape(
                        out_channels, patch_size, patch_size, in_channels
                    )
                    tensor = tensor.permute(0, 3, 1, 2).contiguous()

            filtered_weights.append((name, tensor))

        # Skip vit_pos_embed.pos_embed as it's handled by PositionEmbedding module
        loader = AutoWeightsLoader(self, skip_prefixes=["vit_pos_embed.pos_embed"])
        return loader.load_weights(filtered_weights, mapper=self.hf_to_vllm_mapper)
```