---
title: processor - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/processor/
source: sitemap
fetched_at: 2026-05-07T21:37:45.350653139-03:00
rendered_js: false
word_count: 313
summary: This document outlines utility classes for hashable data structures and compatibility patches for Hugging Face Transformers versions, alongside helper functions for loading feature extractors and image processors.
tags:
    - python-utilities
    - transformers-compatibility
    - data-structures
    - huggingface-integration
    - feature-extraction
    - image-processing
category: reference
---

## HashableDict [¶](#vllm.transformers_utils.processor.HashableDict "Permanent link")

Bases: `dict`

A dictionary that can be hashed by lru\_cache.

Source code in `vllm/transformers_utils/processor.py`

```
classHashableDict(dict):
"""
    A dictionary that can be hashed by lru_cache.
    """

    # NOTE: pythonic dict is not hashable,
    # we override on it directly for simplicity
    def__hash__(self) -> int:  # type: ignore[override]
        return hash(frozenset(self.items()))
```

## HashableList [¶](#vllm.transformers_utils.processor.HashableList "Permanent link")

Bases: `list`

A list that can be hashed by lru\_cache.

Source code in `vllm/transformers_utils/processor.py`

```
classHashableList(list):
"""
    A list that can be hashed by lru_cache.
    """

    def__hash__(self) -> int:  # type: ignore[override]
        return hash(tuple(self))
```

## \_transformers\_v4\_compatibility\_import [¶](#vllm.transformers_utils.processor._transformers_v4_compatibility_import "Permanent link")

```
_transformers_v4_compatibility_import()
```

Some remote code processors still import `ChatTemplateLoadKwargs` which was a subset of `ProcessorChatTemplateKwargs` as defined in Transformers v4. In Transformers v5 these were merged into `ProcessorChatTemplateKwargs` and `ChatTemplateLoadKwargs` was removed. For backward compatibility, we add an alias for `ChatTemplateLoadKwargs` if it doesn't exist.

This can be removed if `HCXVisionForCausalLM` is upstreamed to Transformers.

Source code in `vllm/transformers_utils/processor.py`

```
def_transformers_v4_compatibility_import():
"""Some remote code processors still import `ChatTemplateLoadKwargs` which was a
    subset of `ProcessorChatTemplateKwargs` as defined in Transformers v4.
    In Transformers v5 these were merged into `ProcessorChatTemplateKwargs` and
    `ChatTemplateLoadKwargs` was removed. For backward compatibility, we add an alias
    for `ChatTemplateLoadKwargs` if it doesn't exist.

    This can be removed if `HCXVisionForCausalLM` is upstreamed to Transformers."""
    old_import = getattr(processing_utils, "ChatTemplateLoadKwargs", None)
    new_import = getattr(processing_utils, "ProcessorChatTemplateKwargs", None)
    if old_import is None and new_import is not None:
        processing_utils.ChatTemplateLoadKwargs = new_import
```

## \_transformers\_v4\_compatibility\_init [¶](#vllm.transformers_utils.processor._transformers_v4_compatibility_init "Permanent link")

```
_transformers_v4_compatibility_init() -> Any
```

Some remote code processors may define `optional_attributes` in their `ProcessorMixin` subclass, and then pass these arbitrary attributes directly to `ProcessorMixin.__init__`, which is no longer allowed in Transformers v5. For backward compatibility, we intercept these optional attributes and set them on the processor instance before calling the original `ProcessorMixin.__init__`.

This can be removed if `Molmo2ForConditionalGeneration` is upstreamed to Transformers.

Source code in `vllm/transformers_utils/processor.py`

```
def_transformers_v4_compatibility_init() -> Any:
"""Some remote code processors may define `optional_attributes` in their
    `ProcessorMixin` subclass, and then pass these arbitrary attributes directly to
    `ProcessorMixin.__init__`, which is no longer allowed in Transformers v5. For
    backward compatibility, we intercept these optional attributes and set them on the
    processor instance before calling the original `ProcessorMixin.__init__`.

    This can be removed if `Molmo2ForConditionalGeneration` is upstreamed to
    Transformers."""
    # Transformers v4
    if hasattr(ProcessorMixin, "optional_attributes"):
        return
    # Transformers v5
    if hasattr(ProcessorMixin.__init__, "_vllm_patched"):
        return

    original_init = ProcessorMixin.__init__

    def__init__(self, *args, **kwargs):
        for optional_attribute in getattr(self, "optional_attributes", []):
            if optional_attribute in kwargs:
                setattr(self, optional_attribute, kwargs.pop(optional_attribute))

        original_init(self, *args, **kwargs)

    # Only patch if ProcessorMixin is not mocked (for docs builds)
    if not hasattr(ProcessorMixin, "_mock_name"):
        __init__._vllm_patched = True  # type: ignore[attr-defined]
        ProcessorMixin.__init__ = __init__

get_feature_extractor(
    processor_name: str,
    *args: Any,
    revision: str | None = None,
    trust_remote_code: bool = False,
    **kwargs: Any,
)
```

Load an audio feature extractor for the given model name via HuggingFace.

Source code in `vllm/transformers_utils/processor.py`

```
defget_feature_extractor(
    processor_name: str,
    *args: Any,
    revision: str | None = None,
    trust_remote_code: bool = False,
    **kwargs: Any,
):
"""Load an audio feature extractor for the given model name
    via HuggingFace."""
    try:
        processor_name = convert_model_repo_to_path(processor_name)
        feature_extractor = AutoFeatureExtractor.from_pretrained(
            processor_name,
            *args,
            revision=revision,
            trust_remote_code=trust_remote_code,
            **kwargs,
        )
    except ValueError as e:
        # If the error pertains to the processor class not existing or not
        # currently being imported, suggest using the --trust-remote-code flag.
        # Unlike AutoTokenizer, AutoImageProcessor does not separate such errors
        if not trust_remote_code:
            err_msg = (
                "Failed to load the feature extractor. If the feature "
                "extractor is a custom extractor not yet available in the "
                "HuggingFace transformers library, consider setting "
                "`trust_remote_code=True` in LLM or using the "
                "`--trust-remote-code` flag in the CLI."
            )
            raise RuntimeError(err_msg) frome
        else:
            raise e
    return cast(FeatureExtractionMixin, feature_extractor)
```

## get\_image\_processor [¶](#vllm.transformers_utils.processor.get_image_processor "Permanent link")

```
get_image_processor(
    processor_name: str,
    *args: Any,
    revision: str | None = None,
    trust_remote_code: bool = False,
    **kwargs: Any,
)
```

Load an image processor for the given model name via HuggingFace.

Source code in `vllm/transformers_utils/processor.py`

```
defget_image_processor(
    processor_name: str,
    *args: Any,
    revision: str | None = None,
    trust_remote_code: bool = False,
    **kwargs: Any,
):
"""Load an image processor for the given model name via HuggingFace."""
    try:
        processor_name = convert_model_repo_to_path(processor_name)
        processor = AutoImageProcessor.from_pretrained(
            processor_name,
            *args,
            revision=revision,
            trust_remote_code=trust_remote_code,
            **kwargs,
        )
    except ValueError as e:
        # If the error pertains to the processor class not existing or not
        # currently being imported, suggest using the --trust-remote-code flag.
        # Unlike AutoTokenizer, AutoImageProcessor does not separate such errors
        if not trust_remote_code:
            err_msg = (
                "Failed to load the image processor. If the image processor is "
                "a custom processor not yet available in the HuggingFace "
                "transformers library, consider setting "
                "`trust_remote_code=True` in LLM or using the "
                "`--trust-remote-code` flag in the CLI."
            )
            raise RuntimeError(err_msg) frome
        else:
            raise e

    return cast(BaseImageProcessor, processor)
```

## get\_processor [¶](#vllm.transformers_utils.processor.get_processor "Permanent link")

```
get_processor(
    processor_name: str,
    *args: Any,
    revision: str | None = None,
    trust_remote_code: bool = False,
    processor_cls: type[_P]
    | tuple[type[_P], ...] = ProcessorMixin,
    **kwargs: Any,
) -> _P
```

Load a processor for the given model name via HuggingFace.

Source code in `vllm/transformers_utils/processor.py`

```
defget_processor(
    processor_name: str,
    *args: Any,
    revision: str | None = None,
    trust_remote_code: bool = False,
    processor_cls: type[_P] | tuple[type[_P], ...] = ProcessorMixin,
    **kwargs: Any,
) -> _P:
"""Load a processor for the given model name via HuggingFace."""
    if revision is None:
        revision = "main"
    try:
        processor_name = convert_model_repo_to_path(processor_name)
        registered_cls_name = get_processor_cls_name_from_config(
            processor_name, revision=revision
        )
        registered_processor_cls = (
            getattr(processors, registered_cls_name, None)
            if registered_cls_name
            else None
        )
        registered_processor_cls = cast(type[_P] | None, registered_processor_cls)
        # Use registered processor class when it's available
        # and explicit processor_cls is not set.
        if isinstance(processor_cls, tuple) or processor_cls == ProcessorMixin:
            _processor_cls = registered_processor_cls or AutoProcessor
            processor = _processor_cls.from_pretrained(
                processor_name,
                *args,
                revision=revision,
                trust_remote_code=trust_remote_code,
                **kwargs,
            )
        elif issubclass(processor_cls, ProcessorMixin):
            processor = processor_cls.from_pretrained(
                processor_name,
                *args,
                revision=revision,
                trust_remote_code=trust_remote_code,
                **kwargs,
            )
        else:
            # Processors that are standalone classes unrelated to HF
            processor = processor_cls(*args, **kwargs)
    except ValueError as e:
        # If the error pertains to the processor class not existing or not
        # currently being imported, suggest using the --trust-remote-code flag.
        # Unlike AutoTokenizer, AutoProcessor does not separate such errors
        if not trust_remote_code:
            err_msg = (
                "Failed to load the processor. If the processor is "
                "a custom processor not yet available in the HuggingFace "
                "transformers library, consider setting "
                "`trust_remote_code=True` in LLM or using the "
                "`--trust-remote-code` flag in the CLI."
            )
            raise RuntimeError(err_msg) frome
        else:
            raise e

    if not isinstance(processor, processor_cls):
        raise TypeError(
            "Invalid type of HuggingFace processor. "
            f"Expected type: {processor_cls}, but "
            f"found type: {type(processor)}"
        )

    return processor
```

## get\_video\_processor [¶](#vllm.transformers_utils.processor.get_video_processor "Permanent link")

```
get_video_processor(
    processor_name: str,
    *args: Any,
    revision: str | None = None,
    trust_remote_code: bool = False,
    processor_cls_overrides: type[_V] | None = None,
    **kwargs: Any,
)
```

Load a video processor for the given model name via HuggingFace.

Source code in `vllm/transformers_utils/processor.py`

```
defget_video_processor(
    processor_name: str,
    *args: Any,
    revision: str | None = None,
    trust_remote_code: bool = False,
    processor_cls_overrides: type[_V] | None = None,
    **kwargs: Any,
):
"""Load a video processor for the given model name via HuggingFace."""
    try:
        processor_name = convert_model_repo_to_path(processor_name)
        processor_cls = processor_cls_overrides or AutoVideoProcessor
        processor = processor_cls.from_pretrained(
            processor_name,
            *args,
            revision=revision,
            trust_remote_code=trust_remote_code,
            **kwargs,
        )
    except ValueError as e:
        # If the error pertains to the processor class not existing or not
        # currently being imported, suggest using the --trust-remote-code flag.
        # Unlike AutoTokenizer, AutoVideoProcessor does not separate such errors
        if not trust_remote_code:
            err_msg = (
                "Failed to load the video processor. If the video processor is "
                "a custom processor not yet available in the HuggingFace "
                "transformers library, consider setting "
                "`trust_remote_code=True` in LLM or using the "
                "`--trust-remote-code` flag in the CLI."
            )
            raise RuntimeError(err_msg) frome
        else:
            raise e

    return cast(BaseVideoProcessor, processor)
```