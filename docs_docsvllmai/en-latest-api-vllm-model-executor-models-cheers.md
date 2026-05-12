---
title: cheers - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/cheers/
source: sitemap
fetched_at: 2026-05-07T21:29:18.985964145-03:00
rendered_js: false
word_count: 0
summary: This document defines a vLLM model implementation for the Cheers multimodal architecture, specifically enabling image understanding capabilities through a VAE, vision encoder, and projection pipeline.
tags:
    - vllm
    - multimodal
    - computer-vision
    - model-architecture
    - image-understanding
    - pytorch
category: api
---

```
@MULTIMODAL_REGISTRY.register_processor(
    CheersMultiModalProcessor,
    info=CheersProcessingInfo,
    dummy_inputs=CheersDummyInputsBuilder,
)
classCheersForConditionalGeneration(
    nn.Module, SupportsMultiModal, SupportsLoRA, SupportsPP
):
"""
    Cheers: A unified multimodal model for image understanding and generation.

    For vLLM, we focus on the image understanding (vision-to-text) capabilities.
    The image generation part is not supported in vLLM.
    """

    requires_raw_input_tokens = True

    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={
            "model.language_model.": "language_model.model.",
            "model.vision_representation.": "vision_representation.vision_model.",
            "model.und_projector.": "und_projector.",
            "model.vae_model.": "vae_model.",
            "model.vae_decoder_projector.": "vae_decoder_projector.",
            "lm_head.": "language_model.lm_head.",
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

        if type(config).__name__ not in ("CheersConfig", "UMMConfig"):
            raise ValueError(
                f"Expected CheersConfig or UMMConfig, got {type(config).__name__}."
            )

        self.config = config
        self.multimodal_config = multimodal_config

        # The Cheers model's custom Qwen2Config defaults rope_theta to
        # 1_000_000, but this isn't stored in the JSON.  vLLM's standard
        # Qwen2Config defaults to 10_000, causing a 100× mismatch.
        # We must patch BOTH the attribute AND rope_parameters (which
        # patch_rope_parameters may have already populated from the wrong
        # default before __init__ runs).
        _CHEERS_ROPE_THETA = 1_000_000.0
        tc = config.text_config
        old_theta = getattr(tc, "rope_theta", None)
        if old_theta != _CHEERS_ROPE_THETA:
            logger.info(
                "Overriding text_config.rope_theta from %s to %s",
                old_theta,
                _CHEERS_ROPE_THETA,
            )
            tc.rope_theta = _CHEERS_ROPE_THETA
        rp = getattr(tc, "rope_parameters", None)
        if rp is not None and rp.get("rope_theta") != _CHEERS_ROPE_THETA:
            logger.info(
                "Overriding rope_parameters.rope_theta from %s to %s",
                rp.get("rope_theta"),
                _CHEERS_ROPE_THETA,
            )
            rp["rope_theta"] = _CHEERS_ROPE_THETA

        with self._mark_language_model(vllm_config):
            self.language_model = init_vllm_registered_model(
                vllm_config=vllm_config,
                hf_config=config.text_config,
                prefix=maybe_prefix(prefix, "language_model"),
                architectures=["Qwen2ForCausalLM"],
            )

        vit_config = config.vision_representation_config

        with self._mark_tower_model(vllm_config, "image"):
            self.vae_model = CheersVAEModel(config)
            self.vae_decoder_projector = CheersVAEDecoderProjector(config)

            self.vision_representation = SiglipVisionModel(
                config=vit_config,
                quant_config=quant_config,
                prefix=maybe_prefix(prefix, "vision_representation"),
            )

            vit_hidden_size = vit_config.hidden_size
            llm_hidden_size = config.text_config.hidden_size

            self.und_projector = CheersUndProjector(
                image_embed_dim=vit_hidden_size,
                text_embed_dim=llm_hidden_size,
                compression_factor=(2, 2),
                quant_config=quant_config,
                prefix=maybe_prefix(prefix, "und_projector"),
            )

        self.make_empty_intermediate_tensors = (
            self.language_model.make_empty_intermediate_tensors
        )

    def_parse_and_validate_image_input(
        self, **kwargs: object
    ) -> CheersImageInputs | None:
        pixel_values = kwargs.pop("pixel_values", None)
        if pixel_values is None:
            return None
        return CheersImagePixelInputs(
            type="pixel_values",
            pixel_values=pixel_values,
        )

    def_process_image_input(
        self, image_input: CheersImageInputs
    ) -> tuple[torch.Tensor, ...]:
"""Process image inputs through VAE → SigLIP → projector pipeline.

        HF native path: pixel_values → VAE.encode(t=1.0) → vae_decoder_projector
                         → SigLIP → und_projector → text-space embeddings
        """
        pixel_values = image_input["pixel_values"]

        if pixel_values.ndim == 5:
            batch_size, num_images, channels, height, width = pixel_values.shape
            pixel_values = pixel_values.reshape(
                batch_size * num_images, channels, height, width
            )

        with torch.no_grad():
            vae_dtype = next(self.vae_model.parameters()).dtype
            image_latent = self.vae_model.encode(pixel_values.to(dtype=vae_dtype))
            image_pixel_hat = self.vae_decoder_projector(image_latent)

        vision_features = self.vision_representation(image_pixel_hat)
        vision_embeds = self.und_projector(vision_features)

        return tuple(vision_embeds)

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
"""Load weights, keeping VAE encoder/decoder projector for understanding."""
        skip_prefixes = [
            "model.time_embed.",
            "model.gen_projector.",
            "model.hi_gate.",
            "model.hi_projector.",
            "model.vae_model.decoder.",
        ]
        skip_keywords = [
            "text_loss_fc",
        ]

        filtered_weights = []
        for name, tensor in weights:
            if any(name.startswith(p) for p in skip_prefixes):
                continue
            if any(kw in name for kw in skip_keywords):
                continue
            filtered_weights.append((name, tensor))

        loader = AutoWeightsLoader(self)
        return loader.load_weights(filtered_weights, mapper=self.hf_to_vllm_mapper)
```