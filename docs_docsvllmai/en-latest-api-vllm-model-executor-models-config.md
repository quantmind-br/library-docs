---
title: config - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/config/
source: sitemap
fetched_at: 2026-05-07T21:29:29.966528006-03:00
rendered_js: false
word_count: 384
summary: This document defines configuration validation classes for vLLM models, specifically handling backend selection for Gemma4 heterogeneous head dimensions and kv-cache scaling constraints for hybrid attention-mamba architectures.
tags:
    - vllm
    - model-config
    - gemma4
    - attention-backend
    - hybrid-model
    - kv-cache
    - triton-attn
category: reference
---

## Gemma4Config [¶](#vllm.model_executor.models.config.Gemma4Config "Permanent link")

Bases: `VerifyAndUpdateConfig`

Source code in `vllm/model_executor/models/config.py`

```
classGemma4Config(VerifyAndUpdateConfig):
    @staticmethod
    defverify_and_update_config(vllm_config: "VllmConfig") -> None:
"""Force unified attention backend for models with heterogeneous
        head dimensions.

        Some Gemma4 variants use different head dimensions for
        sliding window (head_dim) vs full attention (global_head_dim) layers.
        When global_head_dim > 256, FlashAttention rejects those layers
        (head_size <= 256 kernel limit), causing vLLM to select a different
        backend for each layer type. This mixed-backend execution produces
        numerical divergence and output corruption.

        The fix detects heterogeneous head dimensions from the model config
        and forces TRITON_ATTN (which has no head_size ceiling) for all
        layers when the user hasn't explicitly chosen a backend.

        TODO: Heterogeneous head_sizes (head_dim != global_head_dim)
        require NixlConnector changes to support per-layer KV transfer
        with different head dimensions for prefill-decode disaggregation.
        """
        hf_text_config = vllm_config.model_config.hf_text_config
        head_dim = getattr(hf_text_config, "head_dim", None)
        global_head_dim = getattr(hf_text_config, "global_head_dim", None)

        # Only force Triton when head dimensions actually differ AND the
        # larger one exceeds FlashAttention's kernel limit (head_size <= 256).
        # This avoids unnecessary backend forcing on smaller models where
        # the config carries global_head_dim but all layers can still use
        # the same FA backend.
        max_head_dim = max(head_dim or 0, global_head_dim or 0)
        if (
            head_dim is not None
            and global_head_dim is not None
            and head_dim != global_head_dim
            and max_head_dim > 256
            and vllm_config.attention_config.backend is None
        ):
            fromvllm.v1.attention.backends.registryimport (
                AttentionBackendEnum,
            )

            vllm_config.attention_config.backend = AttentionBackendEnum.TRITON_ATTN
            logger.info(
                "Gemma4 model has heterogeneous head dimensions "
                "(head_dim=%d, global_head_dim=%d). Forcing TRITON_ATTN "
                "backend to prevent mixed-backend numerical divergence.",
                head_dim,
                global_head_dim,
            )
```

### verify\_and\_update\_config `staticmethod` [¶](#vllm.model_executor.models.config.Gemma4Config.verify_and_update_config "Permanent link")

```
verify_and_update_config(vllm_config: VllmConfig) -> None
```

Force unified attention backend for models with heterogeneous head dimensions.

Some Gemma4 variants use different head dimensions for sliding window (head\_dim) vs full attention (global\_head\_dim) layers. When global\_head\_dim &gt; 256, FlashAttention rejects those layers (head\_size &lt;= 256 kernel limit), causing vLLM to select a different backend for each layer type. This mixed-backend execution produces numerical divergence and output corruption.

The fix detects heterogeneous head dimensions from the model config and forces TRITON\_ATTN (which has no head\_size ceiling) for all layers when the user hasn't explicitly chosen a backend.

TODO: Heterogeneous head\_sizes (head\_dim != global\_head\_dim) require NixlConnector changes to support per-layer KV transfer with different head dimensions for prefill-decode disaggregation.

Source code in `vllm/model_executor/models/config.py`

```
@staticmethod
defverify_and_update_config(vllm_config: "VllmConfig") -> None:
"""Force unified attention backend for models with heterogeneous
    head dimensions.

    Some Gemma4 variants use different head dimensions for
    sliding window (head_dim) vs full attention (global_head_dim) layers.
    When global_head_dim > 256, FlashAttention rejects those layers
    (head_size <= 256 kernel limit), causing vLLM to select a different
    backend for each layer type. This mixed-backend execution produces
    numerical divergence and output corruption.

    The fix detects heterogeneous head dimensions from the model config
    and forces TRITON_ATTN (which has no head_size ceiling) for all
    layers when the user hasn't explicitly chosen a backend.

    TODO: Heterogeneous head_sizes (head_dim != global_head_dim)
    require NixlConnector changes to support per-layer KV transfer
    with different head dimensions for prefill-decode disaggregation.
    """
    hf_text_config = vllm_config.model_config.hf_text_config
    head_dim = getattr(hf_text_config, "head_dim", None)
    global_head_dim = getattr(hf_text_config, "global_head_dim", None)

    # Only force Triton when head dimensions actually differ AND the
    # larger one exceeds FlashAttention's kernel limit (head_size <= 256).
    # This avoids unnecessary backend forcing on smaller models where
    # the config carries global_head_dim but all layers can still use
    # the same FA backend.
    max_head_dim = max(head_dim or 0, global_head_dim or 0)
    if (
        head_dim is not None
        and global_head_dim is not None
        and head_dim != global_head_dim
        and max_head_dim > 256
        and vllm_config.attention_config.backend is None
    ):
        fromvllm.v1.attention.backends.registryimport (
            AttentionBackendEnum,
        )

        vllm_config.attention_config.backend = AttentionBackendEnum.TRITON_ATTN
        logger.info(
            "Gemma4 model has heterogeneous head dimensions "
            "(head_dim=%d, global_head_dim=%d). Forcing TRITON_ATTN "
            "backend to prevent mixed-backend numerical divergence.",
            head_dim,
            global_head_dim,
        )
```

## HybridAttentionMambaModelConfig [¶](#vllm.model_executor.models.config.HybridAttentionMambaModelConfig "Permanent link")

Bases: `VerifyAndUpdateConfig`

Source code in `vllm/model_executor/models/config.py`

```
classHybridAttentionMambaModelConfig(VerifyAndUpdateConfig):
    @classmethod
    defverify_and_update_config(cls, vllm_config: "VllmConfig") -> None:
"""
        Perform early validation and setup for hybrid attention/mamba models.

        Block size alignment with mamba page sizes is handled later by
        Platform.update_block_size_for_backend(), which runs after model
        layers are constructed and the attention backend is known.

        Args:
            vllm_config: vLLM Config
        """
        cache_config = vllm_config.cache_config

        # Disable calculate_kv_scales for hybrid models: uninitialized
        # recurrent state corrupts scales during the calibration pass.
        # See issue: https://github.com/vllm-project/vllm/issues/37554

        if cache_config.calculate_kv_scales:
            logger.warning(
                "Disabling calculate_kv_scales for hybrid model '%s'. "
                "Hybrid models with recurrent layers (GDN, Mamba, SSM) "
                "produce unreliable KV cache scales during the "
                "calibration pass because recurrent state is "
                "uninitialized. Using default scale of 1.0 instead.",
                vllm_config.model_config.model,
            )
            cache_config.calculate_kv_scales = False

        # Enable FULL_AND_PIECEWISE by default
        MambaModelConfig.verify_and_update_config(vllm_config)
```

### verify\_and\_update\_config `classmethod` [¶](#vllm.model_executor.models.config.HybridAttentionMambaModelConfig.verify_and_update_config "Permanent link")

```
verify_and_update_config(vllm_config: VllmConfig) -> None
```

Perform early validation and setup for hybrid attention/mamba models.

Block size alignment with mamba page sizes is handled later by Platform.update\_block\_size\_for\_backend(), which runs after model layers are constructed and the attention backend is known.

Parameters:

Name Type Description Default `vllm_config` `VllmConfig`

vLLM Config

*required*

Source code in `vllm/model_executor/models/config.py`

```
@classmethod
defverify_and_update_config(cls, vllm_config: "VllmConfig") -> None:
"""
    Perform early validation and setup for hybrid attention/mamba models.

    Block size alignment with mamba page sizes is handled later by
    Platform.update_block_size_for_backend(), which runs after model
    layers are constructed and the attention backend is known.

    Args:
        vllm_config: vLLM Config
    """
    cache_config = vllm_config.cache_config

    # Disable calculate_kv_scales for hybrid models: uninitialized
    # recurrent state corrupts scales during the calibration pass.
    # See issue: https://github.com/vllm-project/vllm/issues/37554

    if cache_config.calculate_kv_scales:
        logger.warning(
            "Disabling calculate_kv_scales for hybrid model '%s'. "
            "Hybrid models with recurrent layers (GDN, Mamba, SSM) "
            "produce unreliable KV cache scales during the "
            "calibration pass because recurrent state is "
            "uninitialized. Using default scale of 1.0 instead.",
            vllm_config.model_config.model,
        )
        cache_config.calculate_kv_scales = False

    # Enable FULL_AND_PIECEWISE by default
    MambaModelConfig.verify_and_update_config(vllm_config)
```

## LlamaNemotronVLConfig [¶](#vllm.model_executor.models.config.LlamaNemotronVLConfig "Permanent link")

Bases: `VerifyAndUpdateConfig`

Config handler for LlamaNemotronVL embedding models.

Source code in `vllm/model_executor/models/config.py`

```
classLlamaNemotronVLConfig(VerifyAndUpdateConfig):
"""Config handler for LlamaNemotronVL embedding models."""

    @staticmethod
    defverify_and_update_model_config(model_config: "ModelConfig") -> None:
        fromvllm.config.poolerimport SequencePoolingType

        hf_config = model_config.hf_config

        # Set bidirectional attention on the language model config
        hf_config.is_causal = False
        if hasattr(hf_config, "llm_config"):
            hf_config.llm_config.is_causal = False

        if hasattr(hf_config, "vision_config"):
            hf_config.patch_size = hf_config.vision_config.patch_size

        # Set up pooling type
        pooling_type_map: dict[str, SequencePoolingType] = {
            "avg": "MEAN",
            "cls": "CLS",
            "last": "LAST",
        }

        # Get pooling type from config (check both top-level and llm_config)
        pooling = getattr(hf_config, "pooling", None)
        if pooling is None and hasattr(hf_config, "llm_config"):
            pooling = getattr(hf_config.llm_config, "pooling", "avg")

        pooling_type = pooling_type_map.get(pooling)
        if pooling_type is None:
            raise ValueError(f"pool_type {pooling!r} not supported")

        model_config.pooler_config.seq_pooling_type = pooling_type
```

## MambaModelConfig [¶](#vllm.model_executor.models.config.MambaModelConfig "Permanent link")

Bases: `VerifyAndUpdateConfig`

Source code in `vllm/model_executor/models/config.py`

```
classMambaModelConfig(VerifyAndUpdateConfig):
    @classmethod
    defverify_and_update_config(cls, vllm_config: "VllmConfig") -> None:
"""
        Enable FULL_AND_PIECEWISE cuda graph mode by default (required
        to get good performance for mamba layers in V1).

        Args:
            vllm_config: vLLM Config
        """
        model_config = vllm_config.model_config
        cache_config = vllm_config.cache_config

        if cache_config.enable_prefix_caching:
            if cache_config.mamba_cache_mode == "none":
                if (
                    model_config.supports_mamba_prefix_caching
                    and vllm_config.speculative_config is not None
                ):
                    cache_config.mamba_cache_mode = "align"
                    logger.warning(
                        "Mamba cache mode is set to 'align' for %s by default "
                        "when prefix caching and speculative decoding are enabled",
                        model_config.architecture,
                    )
                else:
                    cache_config.mamba_cache_mode = (
                        "all" if model_config.supports_mamba_prefix_caching else "align"
                    )
                    logger.warning(
                        "Mamba cache mode is set to '%s' for %s by default "
                        "when prefix caching is enabled",
                        cache_config.mamba_cache_mode,
                        model_config.architecture,
                    )
            if (
                cache_config.mamba_cache_mode == "all"
                and not model_config.supports_mamba_prefix_caching
            ):
                cache_config.mamba_cache_mode = "align"
                logger.warning(
                    "Hybrid or mamba-based model detected without support "
                    "for prefix caching with Mamba cache 'all' mode: "
                    "falling back to 'align' mode."
                )
            if cache_config.mamba_cache_mode == "align":
                assert vllm_config.scheduler_config.enable_chunked_prefill, (
                    "Chunked prefill is required for mamba cache mode 'align'."
                )
            logger.info(
                "Warning: Prefix caching in Mamba cache '%s' "
                "mode is currently enabled. "
                "Its support for Mamba layers is experimental. "
                "Please report any issues you may observe.",
                cache_config.mamba_cache_mode,
            )
            # By default, mamba block size will be set to max_model_len (see
            # below). When enabling prefix caching, we align mamba block size
            # to the block size as the basic granularity for prefix caching.
            if cache_config.mamba_block_size is None:
                cache_config.mamba_block_size = cache_config.block_size
        else:
            if cache_config.mamba_cache_mode != "none":
                cache_config.mamba_cache_mode = "none"
                logger.warning(
                    "Mamba cache mode is set to 'none' when prefix caching is disabled"
                )
            if cache_config.mamba_block_size is None:
                cache_config.mamba_block_size = model_config.max_model_len
```

### verify\_and\_update\_config `classmethod` [¶](#vllm.model_executor.models.config.MambaModelConfig.verify_and_update_config "Permanent link")

```
verify_and_update_config(vllm_config: VllmConfig) -> None
```

Enable FULL\_AND\_PIECEWISE cuda graph mode by default (required to get good performance for mamba layers in V1).

Parameters:

Name Type Description Default `vllm_config` `VllmConfig`

vLLM Config

*required*

Source code in `vllm/model_executor/models/config.py`

```
@classmethod
defverify_and_update_config(cls, vllm_config: "VllmConfig") -> None:
"""
    Enable FULL_AND_PIECEWISE cuda graph mode by default (required
    to get good performance for mamba layers in V1).

    Args:
        vllm_config: vLLM Config
    """
    model_config = vllm_config.model_config
    cache_config = vllm_config.cache_config

    if cache_config.enable_prefix_caching:
        if cache_config.mamba_cache_mode == "none":
            if (
                model_config.supports_mamba_prefix_caching
                and vllm_config.speculative_config is not None
            ):
                cache_config.mamba_cache_mode = "align"
                logger.warning(
                    "Mamba cache mode is set to 'align' for %s by default "
                    "when prefix caching and speculative decoding are enabled",
                    model_config.architecture,
                )
            else:
                cache_config.mamba_cache_mode = (
                    "all" if model_config.supports_mamba_prefix_caching else "align"
                )
                logger.warning(
                    "Mamba cache mode is set to '%s' for %s by default "
                    "when prefix caching is enabled",
                    cache_config.mamba_cache_mode,
                    model_config.architecture,
                )
        if (
            cache_config.mamba_cache_mode == "all"
            and not model_config.supports_mamba_prefix_caching
        ):
            cache_config.mamba_cache_mode = "align"
            logger.warning(
                "Hybrid or mamba-based model detected without support "
                "for prefix caching with Mamba cache 'all' mode: "
                "falling back to 'align' mode."
            )
        if cache_config.mamba_cache_mode == "align":
            assert vllm_config.scheduler_config.enable_chunked_prefill, (
                "Chunked prefill is required for mamba cache mode 'align'."
            )
        logger.info(
            "Warning: Prefix caching in Mamba cache '%s' "
            "mode is currently enabled. "
            "Its support for Mamba layers is experimental. "
            "Please report any issues you may observe.",
            cache_config.mamba_cache_mode,
        )
        # By default, mamba block size will be set to max_model_len (see
        # below). When enabling prefix caching, we align mamba block size
        # to the block size as the basic granularity for prefix caching.
        if cache_config.mamba_block_size is None:
            cache_config.mamba_block_size = cache_config.block_size
    else:
        if cache_config.mamba_cache_mode != "none":
            cache_config.mamba_cache_mode = "none"
            logger.warning(
                "Mamba cache mode is set to 'none' when prefix caching is disabled"
            )
        if cache_config.mamba_block_size is None:
            cache_config.mamba_block_size = model_config.max_model_len
```

## NemotronHForCausalLMConfig [¶](#vllm.model_executor.models.config.NemotronHForCausalLMConfig "Permanent link")

Bases: `VerifyAndUpdateConfig`

Source code in `vllm/model_executor/models/config.py`

```
classNemotronHForCausalLMConfig(VerifyAndUpdateConfig):
    DEFAULT_MAMBA_SSM_CACHE_DTYPE = "float32"
"""Only `float32` is known to have no accuracy issues by default."""

    @classmethod
    defupdate_mamba_ssm_cache_dtype(
        cls, *, cache_config: "CacheConfig", hf_config: "PretrainedConfig"
    ) -> None:
"""Update mamba_ssm_cache_dtype for NemotronH models when set to 'auto'
        (or not explicitly set), to the value specified in the HF config, or to
        `float32` if not specified.
        """
        if cache_config.mamba_ssm_cache_dtype == "auto":
            mamba_ssm_cache_dtype = getattr(
                hf_config, "mamba_ssm_cache_dtype", cls.DEFAULT_MAMBA_SSM_CACHE_DTYPE
            )
            logger.info(
                "Updating mamba_ssm_cache_dtype to '%s' for NemotronH model",
                mamba_ssm_cache_dtype,
            )
            cache_config.mamba_ssm_cache_dtype = mamba_ssm_cache_dtype

    @classmethod
    defverify_and_update_config(cls, vllm_config: "VllmConfig") -> None:
        cls.update_mamba_ssm_cache_dtype(
            cache_config=vllm_config.cache_config,
            hf_config=vllm_config.model_config.hf_config,
        )
```

### DEFAULT\_MAMBA\_SSM\_CACHE\_DTYPE `class-attribute` `instance-attribute` [¶](#vllm.model_executor.models.config.NemotronHForCausalLMConfig.DEFAULT_MAMBA_SSM_CACHE_DTYPE "Permanent link")

```
DEFAULT_MAMBA_SSM_CACHE_DTYPE = 'float32'
```

Only `float32` is known to have no accuracy issues by default.

### update\_mamba\_ssm\_cache\_dtype `classmethod` [¶](#vllm.model_executor.models.config.NemotronHForCausalLMConfig.update_mamba_ssm_cache_dtype "Permanent link")

```
update_mamba_ssm_cache_dtype(
    *,
    cache_config: CacheConfig,
    hf_config: PretrainedConfig,
) -> None
```

Update mamba\_ssm\_cache\_dtype for NemotronH models when set to 'auto' (or not explicitly set), to the value specified in the HF config, or to `float32` if not specified.

Source code in `vllm/model_executor/models/config.py`

```
@classmethod
defupdate_mamba_ssm_cache_dtype(
    cls, *, cache_config: "CacheConfig", hf_config: "PretrainedConfig"
) -> None:
"""Update mamba_ssm_cache_dtype for NemotronH models when set to 'auto'
    (or not explicitly set), to the value specified in the HF config, or to
    `float32` if not specified.
    """
    if cache_config.mamba_ssm_cache_dtype == "auto":
        mamba_ssm_cache_dtype = getattr(
            hf_config, "mamba_ssm_cache_dtype", cls.DEFAULT_MAMBA_SSM_CACHE_DTYPE
        )
        logger.info(
            "Updating mamba_ssm_cache_dtype to '%s' for NemotronH model",
            mamba_ssm_cache_dtype,
        )
        cache_config.mamba_ssm_cache_dtype = mamba_ssm_cache_dtype
```

## Qwen3\_5ForConditionalGenerationConfig [¶](#vllm.model_executor.models.config.Qwen3_5ForConditionalGenerationConfig "Permanent link")

Bases: `VerifyAndUpdateConfig`

Source code in `vllm/model_executor/models/config.py`

```
classQwen3_5ForConditionalGenerationConfig(VerifyAndUpdateConfig):
    @staticmethod
    defverify_and_update_config(vllm_config: "VllmConfig") -> None:
"""Update mamba_ssm_cache_dtype for Qwen3.5 models when set to 'auto'
        (or not explicitly set), to the value specified in the HF config's
        mamba_ssm_dtype field. Warn if the user explicitly overrides it to a
        different value.
        """
        cache_config = vllm_config.cache_config
        hf_text_config = vllm_config.model_config.hf_text_config
        mamba_ssm_dtype = getattr(hf_text_config, "mamba_ssm_dtype", None)
        if cache_config.mamba_ssm_cache_dtype == "auto":
            if mamba_ssm_dtype is not None:
                cache_config.mamba_ssm_cache_dtype = mamba_ssm_dtype
        elif (
            mamba_ssm_dtype is not None
            and cache_config.mamba_ssm_cache_dtype != mamba_ssm_dtype
        ):
            logger.warning(
                "Qwen3.5 model specifies mamba_ssm_dtype='%s' in its config, "
                "but --mamba-ssm-cache-dtype='%s' was passed. "
                "Using the user-specified value.",
                mamba_ssm_dtype,
                cache_config.mamba_ssm_cache_dtype,
            )
```

### verify\_and\_update\_config `staticmethod` [¶](#vllm.model_executor.models.config.Qwen3_5ForConditionalGenerationConfig.verify_and_update_config "Permanent link")

```
verify_and_update_config(vllm_config: VllmConfig) -> None
```

Update mamba\_ssm\_cache\_dtype for Qwen3.5 models when set to 'auto' (or not explicitly set), to the value specified in the HF config's mamba\_ssm\_dtype field. Warn if the user explicitly overrides it to a different value.

Source code in `vllm/model_executor/models/config.py`

```
@staticmethod
defverify_and_update_config(vllm_config: "VllmConfig") -> None:
"""Update mamba_ssm_cache_dtype for Qwen3.5 models when set to 'auto'
    (or not explicitly set), to the value specified in the HF config's
    mamba_ssm_dtype field. Warn if the user explicitly overrides it to a
    different value.
    """
    cache_config = vllm_config.cache_config
    hf_text_config = vllm_config.model_config.hf_text_config
    mamba_ssm_dtype = getattr(hf_text_config, "mamba_ssm_dtype", None)
    if cache_config.mamba_ssm_cache_dtype == "auto":
        if mamba_ssm_dtype is not None:
            cache_config.mamba_ssm_cache_dtype = mamba_ssm_dtype
    elif (
        mamba_ssm_dtype is not None
        and cache_config.mamba_ssm_cache_dtype != mamba_ssm_dtype
    ):
        logger.warning(
            "Qwen3.5 model specifies mamba_ssm_dtype='%s' in its config, "
            "but --mamba-ssm-cache-dtype='%s' was passed. "
            "Using the user-specified value.",
            mamba_ssm_dtype,
            cache_config.mamba_ssm_cache_dtype,
        )
```