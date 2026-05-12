---
title: hasher - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/multimodal/hasher/
source: sitemap
fetched_at: 2026-05-07T21:34:07.043894997-03:00
rendered_js: false
word_count: 48
summary: This document describes a utility function that retrieves a specific hashing algorithm factory, supporting blake3, sha256, and sha512 for multimodal data processing.
tags:
    - hashing
    - cryptography
    - multimodal
    - fips-compliance
    - algorithm-selection
    - python-utility
category: api
---

Get the hasher factory based on the configured algorithm.

Parameters:

Name Type Description Default `algorithm` `str`

Hash algorithm name (blake3, sha256, or sha512)

*required*

Returns a callable that creates a new hasher instance. Supports blake3 (default), sha256, and sha512 for FIPS compliance.

See: https://github.com/vllm-project/vllm/issues/18334

Source code in `vllm/multimodal/hasher.py`

```
@functools.lru_cache(maxsize=3)
def_get_hasher_factory(algorithm: str) -> Callable[[], "hashlib._Hash"]:
"""
    Get the hasher factory based on the configured algorithm.

    Args:
        algorithm: Hash algorithm name (blake3, sha256, or sha512)

    Returns a callable that creates a new hasher instance.
    Supports blake3 (default), sha256, and sha512 for FIPS compliance.

    See: https://github.com/vllm-project/vllm/issues/18334
    """
    algorithm = algorithm.lower()

    if algorithm == "blake3":
        fromblake3import blake3

        return blake3
    elif algorithm == "sha256":
        return hashlib.sha256
    elif algorithm == "sha512":
        return hashlib.sha512
    else:
        # This should never happen due to env_with_choices validation
        raise ValueError(f"Unsupported hash algorithm: {algorithm}")
```