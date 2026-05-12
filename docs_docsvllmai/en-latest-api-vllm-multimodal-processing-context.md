---
title: context - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/multimodal/processing/context/
source: sitemap
fetched_at: 2026-05-07T21:34:18.402789336-03:00
rendered_js: false
word_count: 23
summary: This document defines the InputProcessingContext class, which provides an interface for managing model configurations, tokenizers, and multimodal processors during the data input preparation pipeline.
tags:
    - python
    - dataclass
    - huggingface
    - multimodal
    - model-configuration
    - data-preprocessing
    - processor-mixin
category: reference
---

```
@dataclass(frozen=True)
classInputProcessingContext:
"""
    Contains information about the model which may be used to
    modify the inputs.
    """

    model_config: ModelConfig
"""The configuration of the model."""

    tokenizer: TokenizerLike | None
"""The tokenizer used to tokenize the inputs."""

    defget_tokenizer(self) -> TokenizerLike:
        if self.tokenizer is None:
            raise ValueError(
                "You cannot pass text prompts when `skip_tokenizer_init=True`"
            )

        return self.tokenizer

    @overload
    defget_hf_config(self, /) -> PretrainedConfig: ...

    @overload
    defget_hf_config(
        self,
        typ: type[_C] | tuple[type[_C], ...],
        /,
    ) -> _C: ...

    defget_hf_config(
        self,
        typ: type[Any] | tuple[type[Any], ...] | None = None,
        /,
    ) -> Any:
"""
        Get the HuggingFace configuration
        (`transformers.PretrainedConfig`) of the model,
        additionally checking its type.

        Raises:
            TypeError: If the configuration is not of the specified type.
        """
        if typ is None:
            fromtransformers.configuration_utilsimport PretrainedConfig

            typ = PretrainedConfig

        hf_config = self.model_config.hf_config
        if not isinstance(hf_config, typ):
            raise TypeError(
                "Invalid type of HuggingFace config. "
                f"Expected type: {typ}, but "
                f"found type: {type(hf_config)}"
            )

        return hf_config

    defget_hf_image_processor_config(self) -> dict[str, Any]:
"""
        Get the HuggingFace image processor configuration of the model.
        """
        return self.model_config.hf_image_processor_config

    defget_mm_config(self):
"""
        Get the multimodal config of the model.

        Raises:
            RuntimeError: If the model is not a multimodal model.
        """
        mm_config = self.model_config.multimodal_config
        if mm_config is None:
            raise RuntimeError("Not a multimodal model")

        return mm_config

    @overload
    defget_hf_processor(self, /, **kwargs: object) -> ProcessorMixin: ...

    @overload
    defget_hf_processor(
        self,
        typ: type[_P] | tuple[type[_P], ...],
        /,
        **kwargs: object,
    ) -> _P: ...

    defget_hf_processor(
        self,
        typ: type[Any] | tuple[type[Any], ...] | None = None,
        /,
        **kwargs: object,
    ) -> Any:
"""
        Get the HuggingFace processor
        (`transformers.ProcessorMixin`) of the model,
        additionally checking its type.

        Raises:
            TypeError: If the processor is not of the specified type.
        """
        if typ is None:
            fromtransformers.processing_utilsimport ProcessorMixin

            typ = ProcessorMixin

        tokenizer = self.tokenizer
        if is_mistral_tokenizer(tokenizer):
            tokenizer = tokenizer.transformers_tokenizer  # type: ignore[union-attr]

        merged_kwargs = self.get_merged_mm_kwargs(kwargs)
        merged_kwargs.pop("tokenizer", None)

        return cached_processor_from_config(
            self.model_config,
            processor_cls=typ,
            tokenizer=tokenizer,
            **merged_kwargs,
        )

    definit_processor(
        self,
        typ: type[_T],
        /,
        **kwargs: object,
    ) -> _T:
"""
        Initialize a HuggingFace-like processor class, merging the
        keyword arguments with those in the model's configuration.
        """
        merged_kwargs = self.get_merged_mm_kwargs(kwargs)

        return typ(**merged_kwargs)

    def_postprocess_output(
        self,
        output: JSONTree,
    ) -> JSONTree:
        def_postprocess_one(x: object):
            if isinstance(x, torch.Tensor):  # noqa: SIM102
                # This mimics the behavior of transformers.BatchFeature
                if x.is_floating_point():
                    x = x.to(dtype=self.model_config.dtype)

            return x

        return json_map_leaves(_postprocess_one, output)

    defget_merged_mm_kwargs(self, kwargs: Mapping[str, object]):
        mm_config = self.model_config.get_multimodal_config()
        return mm_config.merge_mm_processor_kwargs(kwargs)

    defcall_hf_processor(
        self,
        hf_processor: Callable[..., BatchFeature] | ProcessorMixin,
        data: Mapping[str, object],
        kwargs: Mapping[str, object] = {},
        *,
        num_tries: int = 1,
        max_tries: int = 5,
    ) -> BatchFeature:
"""
        Call `hf_processor` on the prompt `data`
        (text, image, audio...) with configurable options `kwargs`.
        """
        assert callable(hf_processor)

        merged_kwargs = self.get_merged_mm_kwargs(kwargs)

        allowed_kwargs = get_allowed_kwarg_only_overrides(
            hf_processor,
            merged_kwargs,
            requires_kw_only=False,
            allow_var_kwargs=True,
        )
        allowed_kwargs.setdefault("return_tensors", "pt")

        try:
            output = hf_processor(**data, **allowed_kwargs)
        except Exception as exc:
            msg = (
                f"Failed to apply {type(hf_processor).__name__} "
                f"on data={data} with kwargs={allowed_kwargs}"
            )

            raise ValueError(msg) fromexc

        # this emulates output.to(dtype=self.model_config.dtype)
        fromtransformers.feature_extraction_utilsimport BatchFeature

        if isinstance(output, BatchFeature):
            output_ = self._postprocess_output(output.data)
            return BatchFeature(output_)  # type: ignore

        logger.warning_once(
            "%s did not return `BatchFeature`. "
            "Make sure to match the behaviour of `ProcessorMixin` when "
            "implementing custom processors.",
            type(hf_processor).__name__,
        )

        return self._postprocess_output(output)  # type: ignore
```