---
title: multimodal - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/transformers/multimodal/
source: sitemap
fetched_at: 2026-05-07T21:33:37.883897167-03:00
rendered_js: false
word_count: 16
summary: This document defines a MultiModalMixin class that provides the architectural framework and utility methods for integrating multimodal vision encoders into vLLM's Transformers-based models, including support for torch compilation and input embedding processing.
tags:
    - vllm
    - multimodal
    - vision-encoder
    - torch-compile
    - transformer-models
    - model-architecture
category: concept
---

```
classMultiModalMixin(SupportsMultiModal, SupportsMRoPE):
    supports_multimodal_raw_input_only = True

    def__init__(self, *, vllm_config: "VllmConfig", prefix: str = ""):
        # Skip SupportsMRoPE.__init__ and call the next class in MRO
        super(SupportsMRoPE, self).__init__(vllm_config=vllm_config, prefix=prefix)

    def_get_encoder_cls(
        self, modality: str = "image", **kwargs: dict
    ) -> type["PreTrainedModel"]:
"""
        Get the encoder class from the model.

        Args:
            kwargs: The kwargs to create the model.

        Returns:
            The encoder class.
        """
        with torch.device("meta"):
            model: PreTrainedModel = AutoModel.from_config(**kwargs)
        encoder_cls = type(model.get_encoder(modality=modality))
        logger.debug("Identified encoder class as: %s", encoder_cls)
        if type(model) is encoder_cls:
            raise ValueError(
                "Unable to infer vision encoder class from the model. "
                "You must either: update the model so that "
                "https://huggingface.co/docs/transformers/en/main_classes/model#transformers.PreTrainedModel.get_encoder"
                " can detect the vision encoder correctly, or remove "
                "'compile_mm_encoder'."
            )
        del model
        return encoder_cls

    def_decorate_for_torch_compile(self, **kwargs: dict):
"""
        Decorate the model's decoder and encoder classes to indicate to vLLM that they
        support torch compile if `can_enable_torch_compile` and
        `should_torch_compile_mm_encoder` are True respectively.

        Args:
            kwargs: The kwargs to create the model, which are needed to get the decoder
                and encoder classes.
        """
        super()._decorate_for_torch_compile(**kwargs)
        # Decorate the vision encoder model class to support torch compile if needed
        if self.compilation_config.compile_mm_encoder:
            self.check_version("5.0.0", "multimodal encoder compilation support")
            logger.warning_once(
                "Multimodal encoder compilation with the Transformers modeling backend "
                "is an experimental feature. It relies on:\n"
                "- The vision encoder being torch compilable.\n"
                "- All vision encoder tensor inputs must be type hinted as either "
                "`torch.Tensor` or `torch.FloatTensor`.\n"
                "- The 0-th dimension of all tensor inputs to the vision encoder being "
                "the dynamic dimension (i.e., sequence length or number of patches).\n"
                "Please report any issues you encounter to help us improve it."
            )
            self._decorate_cls_for_torch_compile(
                cls=self._get_encoder_cls(**kwargs),
                # TODO: properly infer dynamic_arg_dims based on the encoder's forward
                # method signature. Currently we assume dim 0 for all tensor inputs.
                dynamic_arg_dims=None,
                enable_if=should_torch_compile_mm_encoder,
                is_encoder=True,
            )

    defforward(
        self,
        input_ids: torch.Tensor | None,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
        **kwargs: object,
    ) -> torch.Tensor | IntermediateTensors:
        # Gemma3 and PaliGemma needs `token_type_ids` to work correctly
        # Other models will not have `token_type_ids` in kwargs
        kwargs = {k: v for k, v in kwargs.items() if k == "token_type_ids"}
        # Positions shape handling for MRoPE models
        if self.model_config.uses_mrope:
            # [3, seq_len] -> [3, 1, seq_len]
            positions = positions[:, None]
        model_output = super().forward(
            input_ids, positions, intermediate_tensors, inputs_embeds, **kwargs
        )
        return model_output

    defget_language_model(self) -> torch.nn.Module:
"""Transformers modeling backend multimodal classes do not contain a separate
        vLLM language model class. Therefore, in order to return a language model vLLM
        class, we use a wrapper to give `self` the same interface as a text model."""

        # Exclude self and object
        bases = self.__class__.mro()[1:-1]
        # Keep only classes defined in `vllm.model_executor.models.transformers`
        bases = [b for b in bases if ".transformers." in b.__module__]
        # Exclude MultiModalMixin itself
        bases = [b for b in bases if b is not MultiModalMixin]

        classLanguageModel(*bases):
            def__init__(self, multimodal_model):
                # Don't call super().__init__() to avoid re-initialization
                self.__dict__.update(multimodal_model.__dict__)

            model = getattr_iter(self.model, ("language_model", "text_model"), None)

        return LanguageModel(self)

    defembed_multimodal(self, **kwargs):
        pixel_values: torch.Tensor | None = kwargs.pop("pixel_values", None)
        image_embeds: torch.Tensor | None = kwargs.pop("image_embeds", None)
        # Model might use `image_patches` instead of `pixel_values`
        if pixel_values is None:
            pixel_values = kwargs.pop("image_patches", None)

        if image_embeds is not None:
            return image_embeds

        if pixel_values is None:
            return None

        num_image_patches = kwargs.pop("num_image_patches")
        kwargs.pop("token_type_ids", None)  # used only in `forward`
        kwargs.pop("mm_token_type_ids", None)  # used only in `model.get_rope_index`

        if pixel_values is not None:
            # ROCm: Force math SDP backend for vision encoder to avoid accuracy issues
            # with flash_sdp and mem_efficient_sdp
            if current_platform.is_rocm():
                # TODO: [ROCm] Fix accuracy issues with flash backend
                logger.debug(
                    "ROCm platform detected. Forcing math SDP backend "
                    "for vision encoder. Currently ROCm platform has "
                    "accuracy issues with `flash_sdp` and"
                    "`mem_efficient_sdp` backends. See issue: "
                    "https://github.com/vllm-project/vllm/issues/30167"
                )
                with torch.nn.attention.sdpa_kernel(
                    backends=[torch.nn.attention.SDPBackend.MATH]
                ):
                    vision_embeddings = self.model.get_image_features(
                        pixel_values, **kwargs
                    )
            else:
                vision_embeddings = self.model.get_image_features(
                    pixel_values, **kwargs
                )

            # Transformers `v5`, `self.get_image_features` returns a tuple
            # containing the features and optionally attentions/hidden_states
            # After v5 is settled, we can enable qwen3-vl with several outputs
            # from `self.get_image_features`
            if isinstance(vision_embeddings, tuple):
                vision_embeddings = vision_embeddings[0]
            elif isinstance(vision_embeddings, dict):
                vision_embeddings = vision_embeddings.pooler_output

            if isinstance(vision_embeddings, torch.Tensor):
                split_sizes = num_image_patches.flatten().tolist()
                total_patches = sum(split_sizes)

                # Flatten to 2D: [total_tokens, hidden_dim]
                if vision_embeddings.ndim == 3:
                    vision_embeddings = vision_embeddings.view(
                        -1, vision_embeddings.shape[-1]
                    )

                total_tokens = vision_embeddings.shape[0]
                if total_tokens == total_patches:
                    # Direct match: num_image_patches are actual token counts
                    # (e.g., Qwen2.5-VL style)
                    token_split_sizes = split_sizes
                elif total_patches > 0 and total_tokens % total_patches == 0:
                    # Uniform expansion: each patch expands to N tokens
                    # (e.g., Idefics3 style)
                    tokens_per_patch = total_tokens // total_patches
                    token_split_sizes = [s * tokens_per_patch for s in split_sizes]
                elif total_patches > 0:
                    # Mismatch (profiling with dummy data) - pad/truncate
                    if total_tokens == 0:
                        raise ValueError(
                            "Vision encoder returned empty embeddings. "
                            f"Expected {total_patches} patches from "
                            f"num_image_patches={split_sizes}"
                        )
                    if total_tokens < total_patches:
                        repeat_factor = (
                            total_patches + total_tokens - 1
                        ) // total_tokens
                        vision_embeddings = vision_embeddings.repeat(repeat_factor, 1)
                    vision_embeddings = vision_embeddings[:total_patches]
                    token_split_sizes = split_sizes
                else:
                    return []

                return list(torch.split(vision_embeddings, token_split_sizes, dim=0))

            return vision_embeddings
        else:
            logger.debug(
                "No pixel values or image embeddings provided for multimodal embedding."
            )
            return None

    defget_mrope_input_positions(
        self,
        input_tokens: list[int],
        mm_features: list[MultiModalFeatureSpec],
    ) -> tuple[torch.Tensor, int]:
        kwargs = MultiModalFeatureSpec.gather_kwargs(
            mm_features,
            {
                "image_grid_thw",
                "video_grid_thw",
                "mm_token_type_ids",
                "second_per_grid_ts",
                "audio_feature_lengths",
                "use_audio_in_video",
            },
        )
        if any(
            v
            for k, v in kwargs.items()
            if k not in {"image_grid_thw", "mm_token_type_ids"}
        ):
            raise NotImplementedError(
                "Transformers modeling backend only supports images."
            )

        image_grid_thw = kwargs.get("image_grid_thw", [])
        video_grid_thw = kwargs.get("video_grid_thw", [])
        mm_token_type_ids = kwargs.get("mm_token_type_ids")

        image_grid_thw = (torch.stack if image_grid_thw else torch.tensor)(
            image_grid_thw
        )
        video_grid_thw = (torch.stack if video_grid_thw else torch.tensor)(
            video_grid_thw
        )

        # In v4 `get_rope_index` doesn't have wildcard `kwargs`, and
        # can't accept arbitrary args, even if its value is `None`
        kwargs = {}
        if not hasattr(self, "_get_rope_index_accepts_mm_token_type_ids"):
            importinspect

            sig = inspect.signature(self.model.get_rope_index)
            params = sig.parameters
            self._get_rope_index_accepts_mm_token_type_ids = (
                "mm_token_type_ids" in params
                or any(p.kind == inspect.Parameter.VAR_KEYWORD for p in params.values())
            )
        if self._get_rope_index_accepts_mm_token_type_ids:
            if mm_token_type_ids:
                kwargs["mm_token_type_ids"] = torch.cat(mm_token_type_ids)
            else:
                shape = (1, len(input_tokens))
                kwargs["mm_token_type_ids"] = torch.zeros(*shape, dtype=torch.int)

        mrope_positions, mrope_position_delta = self.model.get_rope_index(
            input_ids=torch.tensor(input_tokens).unsqueeze(0),
            image_grid_thw=image_grid_thw,
            video_grid_thw=video_grid_thw,
            **kwargs,
        )

        mrope_positions = mrope_positions[:, 0]
        mrope_position_delta = mrope_position_delta[0].item()

        return mrope_positions, mrope_position_delta
```