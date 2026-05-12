---
title: mm_serde - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/serve/disagg/mm_serde/
source: sitemap
fetched_at: 2026-05-07T21:21:22.977896812-03:00
rendered_js: false
word_count: 45
summary: This document provides the reference implementation for encoding and decoding multimodal tensor metadata to and from base64 strings for use in disaggregated vLLM endpoints.
tags:
    - multimodal-tensors
    - serialization
    - deserialization
    - vllm-entrypoints
    - base64-encoding
    - data-serde
category: reference
---

## vllm.entrypoints.serve.disagg.mm\_serde [¶](#vllm.entrypoints.serve.disagg.mm_serde "Permanent link")

Encode/decode utilities for multimodal tensors and field metadata over JSON/HTTP, used by the disaggregated generate endpoint.

## decode\_mm\_kwargs\_item [¶](#vllm.entrypoints.serve.disagg.mm_serde.decode_mm_kwargs_item "Permanent link")

Deserialize a base64 string back to a MultiModalKwargsItem.

Source code in `vllm/entrypoints/serve/disagg/mm_serde.py`

```
defdecode_mm_kwargs_item(data: str) -> MultiModalKwargsItem:
"""Deserialize a base64 string back to a MultiModalKwargsItem."""
    raw = pybase64.b64decode(data)
    return _decoder.decode(raw)
```

## encode\_mm\_kwargs\_item [¶](#vllm.entrypoints.serve.disagg.mm_serde.encode_mm_kwargs_item "Permanent link")

Serialize a MultiModalKwargsItem to a base64 string.

Source code in `vllm/entrypoints/serve/disagg/mm_serde.py`

```
defencode_mm_kwargs_item(item: MultiModalKwargsItem) -> str:
"""Serialize a MultiModalKwargsItem to a base64 string."""
    bufs = _encoder.encode(item)
    assert len(bufs) == 1, "All tensors should be inline"
    return pybase64.b64encode(bufs[0]).decode("ascii")
```