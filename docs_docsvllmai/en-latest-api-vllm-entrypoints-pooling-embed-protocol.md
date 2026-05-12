---
title: protocol - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/pooling/embed/protocol/
source: sitemap
fetched_at: 2026-05-07T21:21:00.63852284-03:00
rendered_js: false
word_count: 93
summary: This document defines the protocols and utility functions for processing and formatting embedding data to be compatible with OpenAI and Cohere API standards, including base64 encoding and bit-packing operations.
tags:
    - vllm
    - embeddings
    - data-encoding
    - api-protocol
    - binary-packing
    - base64
    - cohere-api
    - openai-api
category: reference
---

## vllm.entrypoints.pooling.embed.protocol [¶](#vllm.entrypoints.pooling.embed.protocol "Permanent link")

Embedding API protocol models for OpenAI and Cohere formats.

OpenAI: https://platform.openai.com/docs/api-reference/embeddings Cohere: https://docs.cohere.com/reference/embed

## \_encode\_base64\_embeddings [¶](#vllm.entrypoints.pooling.embed.protocol._encode_base64_embeddings "Permanent link")

Encode float embeddings as base64 (little-endian float32).

Source code in `vllm/entrypoints/pooling/embed/protocol.py`

```
def_encode_base64_embeddings(
    float_embeddings: list[list[float]],
) -> list[str]:
"""Encode float embeddings as base64 (little-endian float32)."""
    result: list[str] = []
    for embedding in float_embeddings:
        buf = struct.pack(f"<{len(embedding)}f", *embedding)
        result.append(base64.b64encode(buf).decode("utf-8"))
    return result
```

## \_pack\_binary\_embeddings [¶](#vllm.entrypoints.pooling.embed.protocol._pack_binary_embeddings "Permanent link")

Bit-pack float embeddings: positive -&gt; 1, negative -&gt; 0.

Each bit is shifted left by `7 - idx%8`, and every 8 bits are packed into one byte.

Source code in `vllm/entrypoints/pooling/embed/protocol.py`

```
def_pack_binary_embeddings(
    float_embeddings: list[list[float]],
    signed: bool,
) -> list[list[int]]:
"""Bit-pack float embeddings: positive -> 1, negative -> 0.

    Each bit is shifted left by ``7 - idx%8``, and every 8 bits are packed
    into one byte.
    """
    result: list[list[int]] = []
    for embedding in float_embeddings:
        dim = len(embedding)
        if dim % 8 != 0:
            raise ValueError(
                "Embedding dimension must be a multiple of 8 for binary "
                f"embedding types, but got {dim}."
            )
        packed_len = dim // 8
        packed: list[int] = []
        byte_val = 0
        for idx, value in enumerate(embedding):
            bit = 1 if value >= 0 else 0
            byte_val += bit << (7 - idx % 8)
            if (idx + 1) % 8 == 0:
                if signed:
                    byte_val -= _UNSIGNED_TO_SIGNED_DIFF
                packed.append(byte_val)
                byte_val = 0
        assert len(packed) == packed_len
        result.append(packed)
    return result
```

## build\_typed\_embeddings [¶](#vllm.entrypoints.pooling.embed.protocol.build_typed_embeddings "Permanent link")

```
build_typed_embeddings(
    float_embeddings: list[list[float]],
    embedding_types: Sequence[str],
) -> CohereEmbedByTypeEmbeddings
```

Convert float embeddings to all requested Cohere embedding types.

Source code in `vllm/entrypoints/pooling/embed/protocol.py`

```
defbuild_typed_embeddings(
    float_embeddings: list[list[float]],
    embedding_types: Sequence[str],
) -> CohereEmbedByTypeEmbeddings:
"""Convert float embeddings to all requested Cohere embedding types."""
    result = CohereEmbedByTypeEmbeddings()

    for emb_type in embedding_types:
        if emb_type == "float":
            result.float = float_embeddings
        elif emb_type == "binary":
            result.binary = _pack_binary_embeddings(float_embeddings, signed=True)
        elif emb_type == "ubinary":
            result.ubinary = _pack_binary_embeddings(float_embeddings, signed=False)
        elif emb_type == "base64":
            result.base64 = _encode_base64_embeddings(float_embeddings)

    return result
```