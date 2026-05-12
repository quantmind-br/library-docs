---
title: registry - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/tokenizers/registry/
source: sitemap
fetched_at: 2026-05-07T21:35:47.954935113-03:00
rendered_js: false
word_count: 0
summary: This function retrieves and initializes a tokenizer for a specified model using either HuggingFace or ModelScope, with handling for custom model configurations and class overrides.
tags:
    - python
    - tokenizer
    - hugging-face
    - model-loading
    - npl
    - vllm
category: api
---

```
defget_tokenizer(
    tokenizer_name: str | Path,
    *args,
    tokenizer_cls: type[_T] = TokenizerLike,  # type: ignore[assignment]
    trust_remote_code: bool = False,
    revision: str | None = None,
    download_dir: str | None = None,
    **kwargs,
) -> _T:
"""Gets a tokenizer for the given model name via HuggingFace or ModelScope."""
    tokenizer_mode, tokenizer_name, args, kwargs = cached_resolve_tokenizer_args(
        tokenizer_name,
        *args,
        trust_remote_code=trust_remote_code,
        revision=revision,
        download_dir=download_dir,
        **kwargs,
    )

    # Ensure that, if the config were to come from vllm.transformers_utils.config, it is
    # registered with AutoConfig before the tokenizer is loaded. This is necessary since
    # tokenizer_cls_.from_pretrained will call AutoConfig.from_pretrained internally.
    # This may fail for paths that don't have a model config (e.g. LoRA adapters),
    # which is fine — those don't need custom config registration.
    config = None
    with contextlib.suppress(ValueError, OSError):
        config = get_config(
            tokenizer_name,
            trust_remote_code=trust_remote_code,
            revision=revision,
        )

    # Some models have an incorrect tokenizer_class on the hub.
    # For these model types, bypass AutoTokenizer and use TokenizersBackend directly.
    model_type = getattr(config, "model_type", None) if config else None
    if model_type in _MODEL_TYPES_WITH_INCORRECT_TOKENIZER_CLASS:
        fromtransformers.tokenization_utils_tokenizersimport TokenizersBackend

        logger.debug(
            "Overriding tokenizer_class to TokenizersBackend for model_type=%r",
            model_type,
        )
        tokenizer_cls_ = TokenizersBackend
    elif tokenizer_cls == TokenizerLike:
        tokenizer_cls_ = TokenizerRegistry.load_tokenizer_cls(tokenizer_mode)
    else:
        tokenizer_cls_ = tokenizer_cls

    tokenizer = tokenizer_cls_.from_pretrained(tokenizer_name, *args, **kwargs)
    if not tokenizer.is_fast:
        logger.warning(
            "Using a slow tokenizer. This might cause a significant "
            "slowdown. Consider using a fast tokenizer instead."
        )

    return tokenizer  # type: ignore
```