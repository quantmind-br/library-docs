---
title: hashing - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/utils/hashing/
source: sitemap
fetched_at: 2026-05-07T21:38:39.140407968-03:00
rendered_js: false
word_count: 258
summary: This document provides a reference for utility functions used for hashing Python objects, supporting multiple algorithms like SHA-256 and xxHash with various serialization methods.
tags:
    - hashing
    - data-serialization
    - sha256
    - xxhash
    - python-utils
    - cbor
    - utility-functions
category: reference
---

## get\_hash\_fn\_by\_name [¶](#vllm.utils.hashing.get_hash_fn_by_name "Permanent link")

Get a hash function by name, or raise an error if the function is not found.

Parameters:

Name Type Description Default `hash_fn_name` `str`

Name of the hash function.

*required*

Returns:

Type Description `Callable[[Any], bytes]`

A hash function.

Source code in `vllm/utils/hashing.py`

```
defget_hash_fn_by_name(hash_fn_name: str) -> Callable[[Any], bytes]:
"""Get a hash function by name, or raise an error if the function is not found.

    Args:
        hash_fn_name: Name of the hash function.

    Returns:
        A hash function.
    """
    if hash_fn_name == "sha256":
        return sha256
    if hash_fn_name == "sha256_cbor":
        return sha256_cbor
    if hash_fn_name == "xxhash":
        return xxhash
    if hash_fn_name == "xxhash_cbor":
        return xxhash_cbor

    raise ValueError(f"Unsupported hash function: {hash_fn_name}")
```

## safe\_hash [¶](#vllm.utils.hashing.safe_hash "Permanent link")

```
safe_hash(
    data: bytes, usedforsecurity: bool = True
) -> HASH
```

Hash for configs, defaulting to md5 but falling back to sha256 in FIPS constrained environments.

Parameters:

Name Type Description Default `data` `bytes`

bytes

*required* `usedforsecurity` `bool`

Whether the hash is used for security purposes

`True`

Returns:

Type Description `HASH`

Hash object

Source code in `vllm/utils/hashing.py`

```
defsafe_hash(data: bytes, usedforsecurity: bool = True) -> HASH:
"""Hash for configs, defaulting to md5 but falling back to sha256
    in FIPS constrained environments.

    Args:
        data: bytes
        usedforsecurity: Whether the hash is used for security purposes

    Returns:
        Hash object
    """
    try:
        return hashlib.md5(data, usedforsecurity=usedforsecurity)
    except (UnsupportedDigestmodError, ValueError):
        return hashlib.sha256(data)
```

## sha256 [¶](#vllm.utils.hashing.sha256 "Permanent link")

Hash any picklable Python object using SHA-256.

The input is serialized using pickle before hashing, which allows arbitrary Python objects to be used. Note that this function does not use a hash seed—if you need one, prepend it explicitly to the input.

Parameters:

Name Type Description Default `input` `Any`

Any picklable Python object.

*required*

Returns:

Type Description `bytes`

Bytes representing the SHA-256 hash of the serialized input.

Source code in `vllm/utils/hashing.py`

```
defsha256(input: Any) -> bytes:
"""Hash any picklable Python object using SHA-256.

    The input is serialized using pickle before hashing, which allows
    arbitrary Python objects to be used. Note that this function does
    not use a hash seed—if you need one, prepend it explicitly to the input.

    Args:
        input: Any picklable Python object.

    Returns:
        Bytes representing the SHA-256 hash of the serialized input.
    """
    input_bytes = pickle.dumps(input, protocol=pickle.HIGHEST_PROTOCOL)
    return hashlib.sha256(input_bytes).digest()
```

## sha256\_cbor [¶](#vllm.utils.hashing.sha256_cbor "Permanent link")

Hash objects using CBOR serialization and SHA-256.

This option is useful for non-Python-dependent serialization and hashing.

Parameters:

Name Type Description Default `input` `Any`

Object to be serialized and hashed. Supported types include basic Python types and complex structures like lists, tuples, and dictionaries. Custom classes must implement CBOR serialization methods.

*required*

Returns:

Type Description `bytes`

Bytes representing the SHA-256 hash of the CBOR serialized input.

Source code in `vllm/utils/hashing.py`

```
defsha256_cbor(input: Any) -> bytes:
"""Hash objects using CBOR serialization and SHA-256.

    This option is useful for non-Python-dependent serialization and hashing.

    Args:
        input: Object to be serialized and hashed. Supported types include
            basic Python types and complex structures like lists, tuples, and
            dictionaries.
            Custom classes must implement CBOR serialization methods.

    Returns:
        Bytes representing the SHA-256 hash of the CBOR serialized input.
    """
    input_bytes = cbor2.dumps(input, canonical=True)
    return hashlib.sha256(input_bytes).digest()
```

## xxhash [¶](#vllm.utils.hashing.xxhash "Permanent link")

Hash picklable objects using xxHash.

Source code in `vllm/utils/hashing.py`

```
defxxhash(input: Any) -> bytes:
"""Hash picklable objects using xxHash."""
    input_bytes = pickle.dumps(input, protocol=pickle.HIGHEST_PROTOCOL)
    return _xxhash_digest(input_bytes)
```

## xxhash\_cbor [¶](#vllm.utils.hashing.xxhash_cbor "Permanent link")

Hash objects serialized with CBOR using xxHash.

Source code in `vllm/utils/hashing.py`

```
defxxhash_cbor(input: Any) -> bytes:
"""Hash objects serialized with CBOR using xxHash."""
    input_bytes = cbor2.dumps(input, canonical=True)
    return _xxhash_digest(input_bytes)
```