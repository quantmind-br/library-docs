---
title: models - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/
source: sitemap
fetched_at: 2026-05-07T21:28:55.993897552-03:00
rendered_js: false
word_count: 41
summary: This document defines the ClassSupportsMultiModal protocol, establishing the required interface and structural configuration flags for implementing multi-modal models within the framework.
tags:
    - multimodal
    - protocol
    - interface
    - deep-learning
    - model-architecture
    - vllm
category: reference
---

```
@runtime_checkable
classSupportsMultiModal(Protocol):
"""The interface required for all multi-modal models."""

    supports_multimodal: ClassVar[Literal[True]] = True
"""
    A flag that indicates this model supports multi-modal inputs.

    Note:
        There is no need to redefine this flag if this class is in the
        MRO of your model class.
    """

    supports_multimodal_raw_input_only: ClassVar[bool] = False
"""
    A flag that indicates this model supports multi-modal inputs and processes
    them in their raw form and not embeddings.
    """

    supports_encoder_tp_data: ClassVar[bool] = False
"""
    A flag that indicates whether this model supports
    `multimodal_config.mm_encoder_tp_mode="data"`.
    """

    requires_raw_input_tokens: ClassVar[bool] = False
"""
    A flag that indicates this model processes input id tokens
    in their raw form and not input embeddings.
    """

    _processor_factory: ClassVar[_ProcessorFactories]
"""
    Set internally by `MultiModalRegistry.register_processor`.
    """

    _language_model_names: list[str] = []
"""
    Set internally by `_mark_language_model`.
    """

    _tower_model_names: list[str] = []
"""
    Set internally by `_mark_tower_model`.
    """

    _has_oov_mm_tokens: bool = False
"""
    In general, this should be set at init time by invoking
    `configure_mm_token_handling` models & passing all potentially
    OOV multimodal tokens.
    """

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
"""
        Get the placeholder text for the `i`th `modality` item in the prompt.
        """
        ...

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
"""
        Returns multimodal embeddings generated from multimodal kwargs
        to be merged with text embeddings.

        Note:
            The returned multimodal embeddings must be in the same order as
            the appearances of their corresponding multimodal data item in the
            input prompt.
        """
        ...

    defconfigure_mm_token_handling(self, vocab_size: int, mm_token_ids: list[int]):
"""Check if any multimodal tokens are out of vocabulary. If so, we will
        explicitly mask all multimodal tokens out when computing text embeddings,
        since the multimodal embeddings will be scattered over the results.
        """
        self._has_oov_mm_tokens = any(tok_id >= vocab_size for tok_id in mm_token_ids)
        logger.info(
            "Contains out of vocabulary multimodal tokens? %s",
            self._has_oov_mm_tokens,
        )

    defget_language_model(self) -> VllmModel:
"""
        Returns the underlying language model used for text generation.

        This is typically the `torch.nn.Module` instance responsible for
        processing the merged multimodal embeddings and producing hidden states

        Returns:
            torch.nn.Module: The core language model component.
        """
        # Cached
        if self in _language_model_by_module:
            return _language_model_by_module[self]

        if self._language_model_names:
            mod = self
            for attr in common_prefix(
                [name.split(".") for name in self._language_model_names]
            ):
                if attr:
                    mod = getattr(mod, attr)

            if mod is not self and hasattr(mod, "embed_input_ids"):
                _language_model_by_module[self] = mod
                return mod

        # Fallback
        for mod in self.children():
            if hasattr(mod, "embed_input_ids"):
                _language_model_by_module[self] = mod
                return mod

        raise NotImplementedError(
            f"No language model found in {type(self).__name__}! "
            "You should initialize it via `_mark_language_model`."
        )

    @contextmanager
    def_mark_language_model(
        self,
        vllm_config: VllmConfig,
        *,
        targets: type[nn.Module] | tuple[type[nn.Module], ...] | None = None,
    ):
"""
        Mark each child module that was assigned to this model during this context
        as a language model component.

        Language model components are automatically skipped in `--mm-encoder-only`
        mode.

        If `targets` is set, instead include descendants that are an instance
        of `targets`, even if they aren't direct children.
        """
        from.utilsimport StageMissingLayer, collect_children, no_init_weights

        mm_config = vllm_config.model_config.multimodal_config

        with collect_children(self, targets=targets) as children_names:  # noqa: SIM117
            with (
                no_init_weights(
                    self,
                    lambda mod: StageMissingLayer("language_model", mod),
                    targets=targets,
                )
                if mm_config.mm_encoder_only
                else nullcontext()
            ):
                yield

        self._language_model_names = children_names

    @contextmanager
    def_mark_tower_model(
        self,
        vllm_config: VllmConfig,
        modalities: set[str] | str,
        *,
        targets: type[nn.Module] | tuple[type[nn.Module], ...] | None = None,
    ):
"""
        Mark each child module that was assigned to this model during this context
        as a tower model component.

        Tower model components are automatically skipped when `--limit-mm-per-prompt`
        is set to zero for all of their modalities.

        If `targets` is set, instead include descendants that are an instance
        of `targets`, even if they aren't direct children.
        """
        from.utilsimport StageMissingLayer, collect_children, no_init_weights

        if isinstance(modalities, str):
            modalities = {modalities}

        if modalities == {"image", "video"}:
            stage_name = "vision_tower"
        else:
            stage_name = "_".join([*modalities, "tower"])

        mm_config = vllm_config.model_config.multimodal_config

        with collect_children(self, targets=targets) as children_names:  # noqa: SIM117
            with (
                no_init_weights(
                    self,
                    lambda mod: StageMissingLayer(stage_name, mod),
                    targets=targets,
                )
                if all(mm_config.get_limit_per_prompt(m) == 0 for m in modalities)
                else nullcontext()
            ):
                yield

        self._tower_model_names = children_names

    @contextmanager
    def_mark_composite_model(
        self,
        vllm_config: VllmConfig,
        *,
        language_targets: type[nn.Module] | tuple[type[nn.Module], ...],
        tower_targets: dict[str, type[nn.Module] | tuple[type[nn.Module], ...]],
    ):
"""
        Composite wrapper over `_mark_language_model` and
        `_mark_tower_model` by modality.
        """
        with ExitStack() as stack:
            stack.enter_context(
                self._mark_language_model(
                    vllm_config,
                    targets=language_targets,
                )
            )

            for modality, modality_targets in tower_targets.items():
                stack.enter_context(
                    self._mark_tower_model(
                        vllm_config,
                        modality,
                        targets=modality_targets,
                    )
                )

            yield

    defget_num_mm_encoder_tokens(self, num_image_tokens: int) -> int:
"""
        Implement this function to enable LoRA support
        for the tower module of the multi-modal model.
        Given the number of image tokens, output the number of
        multi-modal encoder tokens.
        """
        ...

    defget_num_mm_connector_tokens(self, num_vision_tokens: int) -> int:
"""
        Implement this function to enable LoRA support
        for the connector module of the multi-modal model.
        Given the number of vision tokens, output the number of
        multi-modal connector tokens.
        """
        ...

    @overload
    defembed_input_ids(self, input_ids: Tensor) -> Tensor: ...

    @overload
    defembed_input_ids(
        self,
        input_ids: Tensor,
        multimodal_embeddings: MultiModalEmbeddings,
        *,
        is_multimodal: torch.Tensor,
    ) -> Tensor: ...

    def_embed_text_input_ids(
        self,
        input_ids: Tensor,
        embed_input_ids: Callable[[Tensor], Tensor],
        *,
        is_multimodal: Tensor | None,
    ) -> Tensor:
        if is_multimodal is not None and self._has_oov_mm_tokens:
            # Force all input IDs to be in vocab; we do this instead of squeezing
            # to ensure that any external configuration requiring offset tracking,
            # e.g., LoRA, are applied correctly regardless of whether or not
            # we have multimodal tokens.
            in_vocab_ids = input_ids.masked_fill(
                is_multimodal.to(device=input_ids.device, non_blocking=True), 0
            )
            return embed_input_ids(in_vocab_ids)

        return embed_input_ids(input_ids)

    defembed_input_ids(
        self,
        input_ids: Tensor,
        multimodal_embeddings: MultiModalEmbeddings | None = None,
        *,
        is_multimodal: Tensor | None = None,
    ) -> Tensor:
"""
        Apply token embeddings to `input_ids`.

        If `multimodal_embeddings` is passed, scatter them into
        `input_ids` according to the mask `is_multimodal`.

        NOTE: If this model has multimodal tokens that are of vocabulary
        (i.e., self._has_oov_mm_tokens=True), the input_ids will be copied
        and masked to 0 during the forward pass for the text embeddings.
        """
        from.utilsimport _merge_multimodal_embeddings

        # Get text embeddings first; multimodal embeddings will clobber
        # any invalid contents in the indices of multimodal embeddings
        # for the in vocabulary and out of vocabulary case.
        inputs_embeds = self._embed_text_input_ids(
            input_ids,
            self.get_language_model().embed_input_ids,
            is_multimodal=is_multimodal,
        )

        if multimodal_embeddings is None or len(multimodal_embeddings) == 0:
            return inputs_embeds

        return _merge_multimodal_embeddings(
            inputs_embeds=inputs_embeds,
            multimodal_embeddings=multimodal_embeddings,
            is_multimodal=_require_is_multimodal(is_multimodal),
        )
```