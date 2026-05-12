---
title: tokenizers - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/tokenizers/
source: sitemap
fetched_at: 2026-05-07T21:35:34.795520347-03:00
rendered_js: false
word_count: 117
summary: This document outlines functions for retrieving model tokenizers via HuggingFace or ModelScope and configuring thread-safe tokenizer pools in vLLM.
tags:
    - tokenizer-registry
    - vllm
    - thread-safety
    - huggingface
    - modelscope
    - concurrency
category: api
---

Modules:

Name Description `deepseek_v32` `deepseek_v4` `deepseek_v4_encoding`

DeepSeek-V4 Encoding

`detokenizer_utils` `fastokens`

`fastokens` tokenizer mode.

`grok2`

Tokenizer for Grok-2 .tok.json format.

`hf` `kimi_audio`

Tokenizer for Kimi-Audio using TikToken.

`mistral` `qwen_vl` `registry`

## get\_tokenizer [¶](#vllm.tokenizers.get_tokenizer "Permanent link")

```
get_tokenizer(
    tokenizer_name: str | Path,
    *args,
    tokenizer_cls: type[_T] = TokenizerLike,
    trust_remote_code: bool = False,
    revision: str | None = None,
    download_dir: str | None = None,
    **kwargs,
) -> _T
```

Gets a tokenizer for the given model name via HuggingFace or ModelScope.

Source code in `vllm/tokenizers/registry.py`

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

## maybe\_make\_thread\_pool [¶](#vllm.tokenizers.maybe_make_thread_pool "Permanent link")

```
maybe_make_thread_pool(tokenizer: _T, copies: int = 1)
```

If `tokenizer` is a `PreTrainedTokenizerFast`, modify the tokenizer in-place to make the public interface thread-safe by routing calls through a deep-copied tokenizer pool.

Note that: - Only `TokenizerLike`'s public interface is thread-safe. This doesn't include `_tokenizer` property nor any mutation methods like `add_special_tokens` or `add_tokens`. - Adjacent method calls could happen on different deep copies.

Source code in `vllm/tokenizers/hf.py`

```
defmaybe_make_thread_pool(tokenizer: _T, copies: int = 1):
"""
    If `tokenizer` is a `PreTrainedTokenizerFast`, modify the tokenizer
    in-place to make the public interface thread-safe by routing calls
    through a deep-copied tokenizer pool.

    Note that:
    - Only ``TokenizerLike``'s public interface is thread-safe.
      This doesn't include ``_tokenizer`` property nor any mutation
      methods like ``add_special_tokens`` or ``add_tokens``.
    - Adjacent method calls could happen on different deep copies.
    """
    if not isinstance(tokenizer, PreTrainedTokenizerFast) or isinstance(
        tokenizer, ThreadSafeHFTokenizerMixin
    ):
        return tokenizer

    og_tokenizer = copy.copy(tokenizer)

    tokenizer_pool: queue.Queue[PreTrainedTokenizerFast] = queue.Queue()
    for _ in range(copies):
        tokenizer_pool.put(copy.deepcopy(og_tokenizer))

    @contextlib.contextmanager
    def_borrow_from_pool():
        try:
            tok = tokenizer_pool.get_nowait()
            yield tok
        except queue.Empty:
            tok = copy.deepcopy(og_tokenizer)
            yield tok
        finally:
            tokenizer_pool.put(tok)

    classTokenizerPool(tokenizer.__class__, ThreadSafeHFTokenizerMixin):  # type: ignore
        defapply_chat_template(self, *args, **kwargs):
            with _borrow_from_pool() as tok:
                return tok.apply_chat_template(*args, **kwargs)

        defbatch_decode(self, *args, **kwargs):
            with _borrow_from_pool() as tok:
                return tok.batch_decode(*args, **kwargs)

        defbatch_encode(self, *args, **kwargs):
            with _borrow_from_pool() as tok:
                return tok.batch_encode(*args, **kwargs)

        defconvert_tokens_to_ids(self, *args, **kwargs):
            with _borrow_from_pool() as tok:
                return tok.convert_tokens_to_ids(*args, **kwargs)

        defconvert_ids_to_tokens(self, *args, **kwargs):
            with _borrow_from_pool() as tok:
                return tok.convert_ids_to_tokens(*args, **kwargs)

        defconvert_tokens_to_string(self, *args, **kwargs):
            with _borrow_from_pool() as tok:
                return tok.convert_tokens_to_string(*args, **kwargs)

        defdecode(self, *args, **kwargs):
            with _borrow_from_pool() as tok:
                return tok.decode(*args, **kwargs)

        defencode(self, *args, **kwargs):
            with _borrow_from_pool() as tok:
                return tok.encode(*args, **kwargs)

        def__call__(self, *args, **kwargs):
            with _borrow_from_pool() as tok:
                return tok(*args, **kwargs)

        def__reduce__(self):
            return maybe_make_thread_pool, (og_tokenizer, copies)

    TokenizerPool.__name__ = f"TokenizerPool{og_tokenizer.__class__.__name__}"

    tokenizer.__class__ = TokenizerPool
```