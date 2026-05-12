---
title: engine - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/engine/
source: sitemap
fetched_at: 2026-05-07T21:40:30.377723174-03:00
rendered_js: false
word_count: 265
summary: This document provides technical documentation and class definitions for the vLLM engine core, detailing the request handling, events, status responses, and configuration types used for managing LLM inference.
tags:
    - vllm
    - llm-inference
    - engine-core
    - request-handling
    - api-reference
    - distributed-computing
category: reference
---

Modules:

Name Description `async_llm` `coordinator` `core` `core_client` `detokenizer` `exceptions` `input_processor` `llm_engine` `logprobs` `output_processor` `parallel_sampling` `tensor_ipc`

Tensor IPC transport via torch.multiprocessing.Queue.

`utils`

## EngineCoreEvent [¶](#vllm.v1.engine.EngineCoreEvent "Permanent link")

Bases: `Struct`

A timestamped engine core event associated with a request.

The timestamp is a monotonic timestamps and is used for by the engine frontend to calculate intervals between engine core events. These timestamps should not be compared with timestamps from other processes.

Source code in `vllm/v1/engine/__init__.py`

```
classEngineCoreEvent(msgspec.Struct):
"""A timestamped engine core event associated with a request.

    The timestamp is a monotonic timestamps and is used for by the engine
    frontend to calculate intervals between engine core events. These
    timestamps should not be compared with timestamps from other processes.
    """

    type: EngineCoreEventType
    timestamp: float

    @classmethod
    defnew_event(
        cls, event_type: EngineCoreEventType, timestamp: float | None = None
    ) -> "EngineCoreEvent":
        timestamp = time.monotonic() if timestamp is None else timestamp
        return cls(event_type, timestamp)
```

## EngineCoreEventType [¶](#vllm.v1.engine.EngineCoreEventType "Permanent link")

Bases: `IntEnum`

The type of engine core request event.

Source code in `vllm/v1/engine/__init__.py`

```
classEngineCoreEventType(enum.IntEnum):
"""The type of engine core request event."""

    QUEUED = 1
    SCHEDULED = 2
    PREEMPTED = 3
```

## EngineCoreReadyResponse `dataclass` [¶](#vllm.v1.engine.EngineCoreReadyResponse "Permanent link")

Sent from EngineCore to each frontend at the end of engine startup.

Contains post-initialization config that may differ from the original values (e.g. max\_model\_len after KV cache auto-fitting).

Source code in `vllm/v1/engine/__init__.py`

```
@dataclass
classEngineCoreReadyResponse:
"""Sent from EngineCore to each frontend at the end of engine startup.

    Contains post-initialization config that may differ from the original
    values (e.g. max_model_len after KV cache auto-fitting).
    """

    max_model_len: int
    num_gpu_blocks: int
    dp_stats_address: str | None
```

## EngineCoreRequest [¶](#vllm.v1.engine.EngineCoreRequest "Permanent link")

Bases: `Struct`

Source code in `vllm/v1/engine/__init__.py`

```
classEngineCoreRequest(
    msgspec.Struct,
    array_like=True,  # type: ignore[call-arg]
    omit_defaults=True,  # type: ignore[call-arg]
    gc=False,
):  # type: ignore[call-arg]
    request_id: str
    prompt_token_ids: list[int] | None
    mm_features: list[MultiModalFeatureSpec] | None
    sampling_params: SamplingParams | None
    pooling_params: PoolingParams | None
    arrival_time: float
    lora_request: LoRARequest | None
    cache_salt: str | None
    data_parallel_rank: int | None
    prompt_embeds: torch.Tensor | None = None

    # Per-position mask for mixed-mode inputs (e.g chat completion with
    # prompt_embeds content parts). `True` means the position is a real
    # token ID; `False` means the position uses a pre-computed entry from
    # `prompt_embeds`. `None` for pure-tokens and pure-embeds requests.
    prompt_is_token_ids: list[bool] | None = None

    # Index of the client, used to ensure outputs are sent back to the same
    # client for this request when scaling out the front-end.
    client_index: int = 0

    # Used in DP case to indicate which wave of requests this is expected to
    # belong to, to cover a race condition where the request is sent before
    # a wave finished notification is received.
    current_wave: int = 0
    priority: int = 0

    trace_headers: Mapping[str, str] | None = None
    resumable: bool = False

    # The user-provided request ID. This field is set internally,
    # copied from the provided request_id that's originally assigned
    # to the request_id field, see InputProcessor.assign_request_id().
    # Used in outputs and to support abort(req_id, internal=False).
    external_req_id: str | None = None

    reasoning_ended: bool | None = None
    reasoning_parser_kwargs: dict[str, Any] | None = None

    @property
    defparams(self) -> SamplingParams | PoolingParams:
"""Return the processed params (sampling or pooling)."""
        if self.sampling_params is not None:
            return self.sampling_params
        assert self.pooling_params is not None
        return self.pooling_params
```

### params `property` [¶](#vllm.v1.engine.EngineCoreRequest.params "Permanent link")

Return the processed params (sampling or pooling).

## EngineCoreRequestType [¶](#vllm.v1.engine.EngineCoreRequestType "Permanent link")

Bases: `Enum`

Request types defined as hex byte strings, so it can be sent over sockets without separate encoding step.

Source code in `vllm/v1/engine/__init__.py`

```
classEngineCoreRequestType(enum.Enum):
"""
    Request types defined as hex byte strings, so it can be sent over sockets
    without separate encoding step.
    """

    ADD = b"\x00"
    ABORT = b"\x01"
    START_DP_WAVE = b"\x02"
    UTILITY = b"\x03"
    # Sentinel used within EngineCoreProc.
    EXECUTOR_FAILED = b"\x04"
    # Sentinel to wake up input_queue.get() during shutdown.
    WAKEUP = b"\x05"
```

## FinishReason [¶](#vllm.v1.engine.FinishReason "Permanent link")

Bases: `IntEnum`

Reason a request finished - stop, length, abort, error, or repetition.

Int rather than Str for more compact serialization.

stop - a stop string was emitted length - max\_tokens was consumed, or max\_model\_len was reached abort - aborted by client error - retryable request-level internal error (e.g., KV load failure). Invariant: always converted to 500 Internal Server Error. repetition - repetitive token pattern detected (hallucination)

Source code in `vllm/v1/engine/__init__.py`

```
classFinishReason(enum.IntEnum):
"""
    Reason a request finished - stop, length, abort, error, or repetition.

    Int rather than Str for more compact serialization.

    stop - a stop string was emitted
    length - max_tokens was consumed, or max_model_len was reached
    abort - aborted by client
    error - retryable request-level internal error (e.g., KV load failure).
            Invariant: always converted to 500 Internal Server Error.
    repetition - repetitive token pattern detected (hallucination)

    """

    STOP = 0
    LENGTH = 1
    ABORT = 2
    ERROR = 3
    REPETITION = 4

    def__str__(self):
        return FINISH_REASON_STRINGS[self.value]
```

## ReconfigureRankType [¶](#vllm.v1.engine.ReconfigureRankType "Permanent link")

Bases: `IntEnum`

Rank type for reconfiguring distributed request.

Source code in `vllm/v1/engine/__init__.py`

```
classReconfigureRankType(enum.IntEnum):
"""
    Rank type for reconfiguring distributed request.
    """

    KEEP_CURRENT_RANK = -1
    SHUTDOWN_CURRENT_RANK = -2
```