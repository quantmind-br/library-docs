---
title: protocol - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/serve/disagg/protocol/
source: sitemap
fetched_at: 2026-05-07T21:21:23.78557537-03:00
rendered_js: false
word_count: 206
summary: This document defines the data structures and request protocols for vLLM's disaggregated serving system, including request generation parameters and multimodal feature metadata.
tags:
    - vllm
    - disaggregated-serving
    - data-model
    - inference-protocol
    - multimodal-features
category: reference
---

## GenerateRequest [¶](#vllm.entrypoints.serve.disagg.protocol.GenerateRequest "Permanent link")

Bases: `BaseModel`

Source code in `vllm/entrypoints/serve/disagg/protocol.py`

```
classGenerateRequest(BaseModel):
    request_id: str = Field(
        default_factory=lambda: f"{random_uuid()}",
        description=(
            "The request_id related to this request. If the caller does "
            "not set it, a random_uuid will be generated. This id is used "
            "through out the inference process and return in response."
        ),
    )
    token_ids: list[int]
"""The token ids to generate text from."""

    @field_validator("token_ids")
    @classmethod
    defvalidate_token_ids(cls, v: list[int]) -> list[int]:
        if any(t < 0 for t in v):
            raise ValueError("token_ids must not contain negative values")
        return v

    features: MultiModalFeatures | None = None
"""Multimodal hashes and placeholder positions (populated for MM inputs)."""

    sampling_params: SamplingParams
"""The sampling parameters for the model."""

    model: str | None = None

    stream: bool | None = False
    stream_options: StreamOptions | None = None
    cache_salt: str | None = Field(
        default=None,
        description=(
            "If specified, the prefix cache will be salted with the provided "
            "string to prevent an attacker to guess prompts in multi-user "
            "environments. The salt should be random, protected from "
            "access by 3rd parties, and long enough to be "
            "unpredictable (e.g., 43 characters base64-encoded, corresponding "
            "to 256 bit)."
        ),
    )
    priority: int = Field(
        default=0,
        ge=-(2**63),
        le=2**63 - 1,
        description=(
            "The priority of the request (lower means earlier handling; "
            "default: 0). Any priority other than 0 will raise an error "
            "if the served model does not use priority scheduling."
        ),
    )
    kv_transfer_params: dict[str, Any] | None = Field(
        default=None,
        description="KVTransfer parameters used for disaggregated serving.",
    )

    defbuild_tok_params(self, model_config: ModelConfig) -> TokenizeParams:
        return TokenizeParams(
            max_total_tokens=None,
            max_output_tokens=0,
        )
```

### features `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.serve.disagg.protocol.GenerateRequest.features "Permanent link")

```
features: MultiModalFeatures | None = None
```

Multimodal hashes and placeholder positions (populated for MM inputs).

### sampling\_params `instance-attribute` [¶](#vllm.entrypoints.serve.disagg.protocol.GenerateRequest.sampling_params "Permanent link")

The sampling parameters for the model.

### token\_ids `instance-attribute` [¶](#vllm.entrypoints.serve.disagg.protocol.GenerateRequest.token_ids "Permanent link")

The token ids to generate text from.

## MultiModalFeatures [¶](#vllm.entrypoints.serve.disagg.protocol.MultiModalFeatures "Permanent link")

Bases: `BaseModel`

Lightweight multimodal metadata produced by the render step.

Carries hashes (for cache lookup / identification) and placeholder positions so the downstream `/generate` service knows *where* in the token sequence each multimodal item lives.

Source code in `vllm/entrypoints/serve/disagg/protocol.py`

```
classMultiModalFeatures(BaseModel):
"""Lightweight multimodal metadata produced by the render step.

    Carries hashes (for cache lookup / identification) and placeholder
    positions so the downstream `/generate` service knows *where* in
    the token sequence each multimodal item lives.
    """

    mm_hashes: dict[str, list[str]]
"""Per-modality item hashes, e.g. `{"image": ["abc", "def"]}`."""

    mm_placeholders: dict[str, list[PlaceholderRangeInfo]]
"""Per-modality placeholder ranges in the token sequence."""

    kwargs_data: dict[str, list[str | None]] | None = None
"""Per-modality serialized tensor data.

    Each value is a list parallel to ``mm_hashes[modality]``.  A ``str``
    entry is a base64-encoded ``MultiModalKwargsItem``; ``None`` means
    the item should be resolved from cache.  The entire field is
    ``None`` for metadata-only (cache-hit) responses.
    """
```

### kwargs\_data `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.serve.disagg.protocol.MultiModalFeatures.kwargs_data "Permanent link")

Per-modality serialized tensor data.

Each value is a list parallel to `mm_hashes[modality]`. A `str` entry is a base64-encoded `MultiModalKwargsItem`; `None` means the item should be resolved from cache. The entire field is `None` for metadata-only (cache-hit) responses.

### mm\_hashes `instance-attribute` [¶](#vllm.entrypoints.serve.disagg.protocol.MultiModalFeatures.mm_hashes "Permanent link")

Per-modality item hashes, e.g. `{"image": ["abc", "def"]}`.

### mm\_placeholders `instance-attribute` [¶](#vllm.entrypoints.serve.disagg.protocol.MultiModalFeatures.mm_placeholders "Permanent link")

Per-modality placeholder ranges in the token sequence.

## PlaceholderRangeInfo [¶](#vllm.entrypoints.serve.disagg.protocol.PlaceholderRangeInfo "Permanent link")

Bases: `BaseModel`

Serializable placeholder location for a single multi-modal item.

Source code in `vllm/entrypoints/serve/disagg/protocol.py`

```
classPlaceholderRangeInfo(BaseModel):
"""Serializable placeholder location for a single multi-modal item."""

    offset: int
"""Start index of the placeholder tokens in the prompt."""

    length: int
"""Number of placeholder tokens."""
```

### length `instance-attribute` [¶](#vllm.entrypoints.serve.disagg.protocol.PlaceholderRangeInfo.length "Permanent link")

Number of placeholder tokens.

### offset `instance-attribute` [¶](#vllm.entrypoints.serve.disagg.protocol.PlaceholderRangeInfo.offset "Permanent link")

Start index of the placeholder tokens in the prompt.