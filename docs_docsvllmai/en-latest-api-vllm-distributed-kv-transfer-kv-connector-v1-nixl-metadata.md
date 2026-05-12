---
title: metadata - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/nixl/metadata/
source: sitemap
fetched_at: 2026-05-07T21:18:41.166940273-03:00
rendered_js: false
word_count: 168
summary: This document defines the metadata structure and compatibility verification logic for the NIXL KV transfer connector, utilizing a two-phase decoding process and SHA-256 hashing to ensure agent compatibility.
tags:
    - nixl
    - kv-transfer
    - compatibility-check
    - metadata
    - vllm-connector
    - handshake-protocol
category: reference
---

Metadata dataclasses and helpers for the NIXL connector.

Bases: `KVConnectorHandshakeMetadata`

Wrapper for NIXL handshake sent over the wire.

Enables two-phase decoding for graceful compatibility checking: 1. Decode NixlHandshakePayload to get compatibility\_hash 2. Compute local hash and compare 3. Only if hashes match, decode agent\_metadata\_bytes

This prevents decoder errors when NixlAgentMetadata schema is incompatible, allowing graceful failure with clear error message.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/nixl/metadata.py`

```
@dataclass
classNixlHandshakePayload(KVConnectorHandshakeMetadata):
"""
    Wrapper for NIXL handshake sent over the wire.

    Enables two-phase decoding for graceful compatibility checking:
    1. Decode NixlHandshakePayload to get compatibility_hash
    2. Compute local hash and compare
    3. Only if hashes match, decode agent_metadata_bytes

    This prevents decoder errors when NixlAgentMetadata schema is
    incompatible, allowing graceful failure with clear error message.
    """

    compatibility_hash: str
    agent_metadata_bytes: bytes  # NixlAgentMetadata encoded

compute_nixl_compatibility_hash(
    vllm_config: VllmConfig,
    attn_backend_name: str,
    cross_layers_blocks: bool,
) -> str
```

Compute compatibility hash for NIXL KV transfer.

Hash only the factors that affect whether two NIXL instances can successfully transfer KV cache data.

Factors included: - vLLM version and NIXL connector version - Model architecture (name, dtype, KV heads, layers) - KV cache format (dtype, sliding window) - Attention backend

Note: Factors like tensor\_parallel\_size, block\_size, and kv\_cache\_layout are validated at runtime in \_validate\_remote\_agent\_handshake and are not included in this hash to support heterogeneous deployments.

Note - the set of factors are likely to evolve significantly over time to be more or less permissive.

Returns:

Type Description `str`

SHA-256 hex digest

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/nixl/metadata.py`

```
defcompute_nixl_compatibility_hash(
    vllm_config: VllmConfig, attn_backend_name: str, cross_layers_blocks: bool
) -> str:
"""
    Compute compatibility hash for NIXL KV transfer.

    Hash only the factors that affect whether two NIXL instances can
    successfully transfer KV cache data.

    Factors included:
    - vLLM version and NIXL connector version
    - Model architecture (name, dtype, KV heads, layers)
    - KV cache format (dtype, sliding window)
    - Attention backend

    Note: Factors like tensor_parallel_size, block_size, and kv_cache_layout
    are validated at runtime in _validate_remote_agent_handshake and are not
    included in this hash to support heterogeneous deployments.

    Note - the set of factors are likely to evolve significantly over
    time to be more or less permissive.

    Returns:
        SHA-256 hex digest
    """
    fromvllmimport __version__ as vllm_version
    fromvllm.config.utilsimport hash_factors

    model_config = vllm_config.model_config
    cache_config = vllm_config.cache_config
    is_hma_enabled = not vllm_config.scheduler_config.disable_hybrid_kv_cache_manager

    factors = {
        # Version compatibility
        "vllm_version": vllm_version,
        "nixl_connector_version": NIXL_CONNECTOR_VERSION,
        # Model architecture - affects KV cache shape
        "model": model_config.model,
        "dtype": str(model_config.dtype),
        "num_kv_heads": model_config.get_total_num_kv_heads(),
        "head_size": model_config.get_head_size(),
        "num_hidden_layers": model_config.get_total_num_hidden_layers(),
        # Attention backend and KV cache dtype affect memory layout
        "attn_backend_name": attn_backend_name,
        "cache_dtype": str(cache_config.cache_dtype),
        "cross_layers_blocks": cross_layers_blocks,
        "is_hma_enabled": is_hma_enabled,
    }

    compat_hash = hash_factors(factors)
    logger.debug(
        "NIXL compatibility hash: %s (model=%s, dtype=%s, num_kv_heads=%d, "
        "cache_dtype=%s, attn_backend=%s)",
        compat_hash,
        factors["model"],
        factors["dtype"],
        factors["num_kv_heads"],
        factors["cache_dtype"],
        attn_backend_name,
    )
    return compat_hash
```