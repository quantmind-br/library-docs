---
title: protocol - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/engine/protocol/
source: sitemap
fetched_at: 2026-05-07T21:19:14.022643027-03:00
rendered_js: false
word_count: 127
summary: This document defines the EngineClient abstract base class, which serves as the core protocol for managing interactions between a client and a vLLM inference engine, including generation, lifecycle, and cache management.
tags:
    - vllm
    - inference-engine
    - python-protocol
    - abstract-base-class
    - model-serving
    - asynchronous-programming
category: api
---

```
classEngineClient(ABC):
"""Protocol class for Clients to Engine"""

    vllm_config: VllmConfig
    model_config: ModelConfig
    renderer: BaseRenderer
    input_processor: InputProcessor

    @property
    @abstractmethod
    defis_running(self) -> bool: ...

    @property
    @abstractmethod
    defis_stopped(self) -> bool: ...

    @property
    @abstractmethod
    deferrored(self) -> bool: ...

    @property
    @abstractmethod
    defdead_error(self) -> BaseException: ...

    @abstractmethod
    defgenerate(
        self,
        prompt: EngineCoreRequest
        | PromptType
        | EngineInput
        | AsyncGenerator[StreamingInput, None],
        sampling_params: SamplingParams,
        request_id: str,
        *,
        prompt_text: str | None = None,
        lora_request: LoRARequest | None = None,
        tokenization_kwargs: dict[str, Any] | None = None,
        trace_headers: Mapping[str, str] | None = None,
        priority: int = 0,
        data_parallel_rank: int | None = None,
        reasoning_ended: bool | None = None,
        reasoning_parser_kwargs: dict[str, Any] | None = None,
    ) -> AsyncGenerator[RequestOutput, None]:
"""Generate outputs for a request."""
        ...

    @abstractmethod
    defencode(
        self,
        prompt: PromptType | EngineInput,
        pooling_params: PoolingParams,
        request_id: str,
        lora_request: LoRARequest | None = None,
        trace_headers: Mapping[str, str] | None = None,
        priority: int = 0,
        tokenization_kwargs: dict[str, Any] | None = None,
        reasoning_ended: bool | None = None,
    ) -> AsyncGenerator[PoolingRequestOutput, None]:
"""Generate outputs for a request from a pooling model."""
        ...

    @abstractmethod
    async defabort(self, request_id: str | Iterable[str]) -> None:
"""Abort a request.

        Args:
            request_id: The unique id of the request,
                        or an iterable of such ids.
        """
        ...

    @abstractmethod
    async defis_tracing_enabled(self) -> bool: ...

    @abstractmethod
    async defdo_log_stats(self) -> None: ...

    @abstractmethod
    async defcheck_health(self) -> None:
"""Raise if unhealthy"""
        ...

    @abstractmethod
    async defstart_profile(self) -> None:
"""Start profiling the engine"""
        ...

    @abstractmethod
    async defstop_profile(self) -> None:
"""Stop profiling the engine"""
        ...

    @abstractmethod
    async defreset_mm_cache(self) -> None:
"""Reset the multi-modal cache"""
        ...

    @abstractmethod
    async defreset_encoder_cache(self) -> None:
"""Reset the encoder cache"""
        ...

    @abstractmethod
    async defreset_prefix_cache(
        self, reset_running_requests: bool = False, reset_connector: bool = False
    ) -> bool:
"""Reset the prefix cache and optionally any configured connector cache"""
        ...

    @abstractmethod
    async defsleep(self, level: int = 1, mode: "PauseMode" = "abort") -> None:
"""Sleep the engine"""
        ...

    @abstractmethod
    async defwake_up(self, tags: list[str] | None = None) -> None:
"""Wake up the engine"""
        ...

    @abstractmethod
    async defis_sleeping(self) -> bool:
"""Check whether the engine is sleeping"""
        ...

    @abstractmethod
    async defadd_lora(self, lora_request: LoRARequest) -> bool:
"""Load a new LoRA adapter into the engine for future requests."""
        ...

    @abstractmethod
    async defpause_generation(
        self,
        *,
        mode: "PauseMode" = "abort",
        wait_for_inflight_requests: bool = False,
        clear_cache: bool = True,
    ) -> None:
"""Pause new generation/encoding requests.

        Args:
            mode: How to handle in-flight requests:
                - ``"abort"``: Abort all in-flight requests immediately
                  and return partial results with "abort" reason (default).
                - ``"wait"``: Wait for in-flight requests to complete.
                - ``"keep"``: Freeze requests in queue; they resume on
                  :meth:`resume_generation`.
            wait_for_inflight_requests: DEPRECATED. Use ``mode="wait"`` instead.
            clear_cache: DEPRECATED. Whether to clear KV and prefix caches
                after draining.
        """
        ...

    @abstractmethod
    async defresume_generation(self) -> None:
"""Resume accepting generation/encoding requests."""
        ...

    @abstractmethod
    async defis_paused(self) -> bool:
"""Return whether the engine is currently paused."""
        ...

    @abstractmethod
    defshutdown(self, timeout: float | None = None) -> None:
"""Shutdown the engine with optional timeout."""
        ...

    async defscale_elastic_ep(
        self, new_data_parallel_size: int, drain_timeout: int = 300
    ) -> None:
"""Scale the engine"""
        raise NotImplementedError

    async defcollective_rpc(
        self,
        method: str,
        timeout: float | None = None,
        args: tuple = (),
        kwargs: dict | None = None,
    ):
"""Perform a collective RPC call to the given path."""
        raise NotImplementedError

    async defget_supported_tasks(self) -> tuple[SupportedTask, ...]:
"""Get supported tasks"""
        raise NotImplementedError

    async definit_weight_transfer_engine(
        self, init_request: WeightTransferInitRequest
    ) -> None:
"""Initialize weight transfer for RL training."""
        raise NotImplementedError

    async defupdate_weights(self, request: WeightTransferUpdateRequest) -> None:
"""Batched weight update for RL training."""
        raise NotImplementedError
```