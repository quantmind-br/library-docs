---
title: observability - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/config/observability/
source: sitemap
fetched_at: 2026-05-07T21:17:05.858511344-03:00
rendered_js: false
word_count: 596
summary: This document defines the configuration schema for observability settings in vLLM, including parameters for metrics collection, distributed tracing, and performance monitoring.
tags:
    - observability
    - metrics
    - tracing
    - opentelemetry
    - nvtx
    - configuration
    - performance-monitoring
category: configuration
---

## ObservabilityConfig [¶](#vllm.config.observability.ObservabilityConfig "Permanent link")

Configuration for observability - metrics and tracing.

Source code in `vllm/config/observability.py`

```
@config
classObservabilityConfig:
"""Configuration for observability - metrics and tracing."""

    show_hidden_metrics_for_version: str | None = None
"""Enable deprecated Prometheus metrics that have been hidden since the
    specified version. For example, if a previously deprecated metric has been
    hidden since the v0.7.0 release, you use
    `--show-hidden-metrics-for-version=0.7` as a temporary escape hatch while
    you migrate to new metrics. The metric is likely to be removed completely
    in an upcoming release."""

    @cached_property
    defshow_hidden_metrics(self) -> bool:
"""Check if the hidden metrics should be shown."""
        if self.show_hidden_metrics_for_version is None:
            return False
        return version._prev_minor_version_was(self.show_hidden_metrics_for_version)

    otlp_traces_endpoint: str | None = None
"""Target URL to which OpenTelemetry traces will be sent."""

    collect_detailed_traces: list[DetailedTraceModules] | None = None
"""It makes sense to set this only if `--otlp-traces-endpoint` is set. If
    set, it will collect detailed traces for the specified modules. This
    involves use of possibly costly and or blocking operations and hence might
    have a performance impact.

    Note that collecting detailed timing information for each request can be
    expensive."""

    kv_cache_metrics: bool = False
"""Enable KV cache residency metrics (lifetime, idle time, reuse gaps).
    Uses sampling to minimize overhead.
    Requires log stats to be enabled (i.e., --disable-log-stats not set)."""

    kv_cache_metrics_sample: float = Field(default=0.01, gt=0, le=1)
"""Sampling rate for KV cache metrics (0.0, 1.0]. Default 0.01 = 1% of blocks."""

    cudagraph_metrics: bool = False
"""Enable CUDA graph metrics (number of padded/unpadded tokens, runtime cudagraph
    dispatch modes, and their observed frequencies at every logging interval)."""

    enable_layerwise_nvtx_tracing: bool = False
"""Enable layerwise NVTX tracing. This traces the execution of each layer or
    module in the model and attach information such as input/output shapes to
    nvtx range markers. Noted that this doesn't work with CUDA graphs enabled."""

    enable_mfu_metrics: bool = False
"""Enable Model FLOPs Utilization (MFU) metrics."""

    enable_mm_processor_stats: bool = False
"""Enable collection of timing statistics for multimodal processor operations.
    This is for internal use only (e.g., benchmarks) and is not exposed as a CLI
    argument."""

    enable_logging_iteration_details: bool = False
"""Enable detailed logging of iteration details.
    If set, vllm EngineCore will log iteration details
    This includes number of context/generation requests and tokens
    and the elapsed cpu time for the iteration."""

    @cached_property
    defcollect_model_forward_time(self) -> bool:
"""Whether to collect model forward time for the request."""
        return self.collect_detailed_traces is not None and (
            "model" in self.collect_detailed_traces
            or "all" in self.collect_detailed_traces
        )

    @cached_property
    defcollect_model_execute_time(self) -> bool:
"""Whether to collect model execute time for the request."""
        return self.collect_detailed_traces is not None and (
            "worker" in self.collect_detailed_traces
            or "all" in self.collect_detailed_traces
        )

    defcompute_hash(self) -> str:
"""
        WARNING: Whenever a new field is added to this config,
        ensure that it is included in the factors list if
        it affects the computation graph.

        Provide a hash that uniquely identifies all the configs
        that affect the structure of the computation
        graph from input ids/embeddings to the final hidden states,
        excluding anything before input ids/embeddings and after
        the final hidden states.
        """
        # no factors to consider.
        # this config will not affect the computation graph.
        factors: list[Any] = []
        hash_str = safe_hash(str(factors).encode(), usedforsecurity=False).hexdigest()
        return hash_str

    @field_validator("show_hidden_metrics_for_version")
    @classmethod
    def_validate_show_hidden_metrics_for_version(cls, value: str | None) -> str | None:
        if value is not None:
            # Raises an exception if the string is not a valid version.
            parse(value)
        return value

    @field_validator("otlp_traces_endpoint")
    @classmethod
    def_validate_otlp_traces_endpoint(cls, value: str | None) -> str | None:
        if value is not None:
            fromvllm.tracingimport is_tracing_available, otel_import_error_traceback

            if not is_tracing_available():
                raise ValueError(
                    "OpenTelemetry is not available. Unable to configure "
                    "'otlp_traces_endpoint'. Ensure OpenTelemetry packages are "
                    f"installed. Original error:\n{otel_import_error_traceback}"
                )
        return value

    @field_validator("collect_detailed_traces")
    @classmethod
    def_validate_collect_detailed_traces(
        cls, value: list[DetailedTraceModules] | None
    ) -> list[DetailedTraceModules] | None:
"""Handle the legacy case where users might provide a comma-separated
        string instead of a list of strings."""
        if value is not None and len(value) == 1 and "," in value[0]:
            value = cast(list[DetailedTraceModules], value[0].split(","))
        return value

    @model_validator(mode="after")
    def_validate_tracing_config(self):
        if self.collect_detailed_traces and not self.otlp_traces_endpoint:
            raise ValueError(
                "collect_detailed_traces requires `--otlp-traces-endpoint` to be set."
            )
        return self
```

### collect\_detailed\_traces `class-attribute` `instance-attribute` [¶](#vllm.config.observability.ObservabilityConfig.collect_detailed_traces "Permanent link")

```
collect_detailed_traces: (
    list[DetailedTraceModules] | None
) = None
```

It makes sense to set this only if `--otlp-traces-endpoint` is set. If set, it will collect detailed traces for the specified modules. This involves use of possibly costly and or blocking operations and hence might have a performance impact.

Note that collecting detailed timing information for each request can be expensive.

### collect\_model\_execute\_time `cached` `property` [¶](#vllm.config.observability.ObservabilityConfig.collect_model_execute_time "Permanent link")

```
collect_model_execute_time: bool
```

Whether to collect model execute time for the request.

### collect\_model\_forward\_time `cached` `property` [¶](#vllm.config.observability.ObservabilityConfig.collect_model_forward_time "Permanent link")

```
collect_model_forward_time: bool
```

Whether to collect model forward time for the request.

### cudagraph\_metrics `class-attribute` `instance-attribute` [¶](#vllm.config.observability.ObservabilityConfig.cudagraph_metrics "Permanent link")

```
cudagraph_metrics: bool = False
```

Enable CUDA graph metrics (number of padded/unpadded tokens, runtime cudagraph dispatch modes, and their observed frequencies at every logging interval).

### enable\_layerwise\_nvtx\_tracing `class-attribute` `instance-attribute` [¶](#vllm.config.observability.ObservabilityConfig.enable_layerwise_nvtx_tracing "Permanent link")

```
enable_layerwise_nvtx_tracing: bool = False
```

Enable layerwise NVTX tracing. This traces the execution of each layer or module in the model and attach information such as input/output shapes to nvtx range markers. Noted that this doesn't work with CUDA graphs enabled.

### enable\_logging\_iteration\_details `class-attribute` `instance-attribute` [¶](#vllm.config.observability.ObservabilityConfig.enable_logging_iteration_details "Permanent link")

```
enable_logging_iteration_details: bool = False
```

Enable detailed logging of iteration details. If set, vllm EngineCore will log iteration details This includes number of context/generation requests and tokens and the elapsed cpu time for the iteration.

### enable\_mfu\_metrics `class-attribute` `instance-attribute` [¶](#vllm.config.observability.ObservabilityConfig.enable_mfu_metrics "Permanent link")

```
enable_mfu_metrics: bool = False
```

Enable Model FLOPs Utilization (MFU) metrics.

### enable\_mm\_processor\_stats `class-attribute` `instance-attribute` [¶](#vllm.config.observability.ObservabilityConfig.enable_mm_processor_stats "Permanent link")

```
enable_mm_processor_stats: bool = False
```

Enable collection of timing statistics for multimodal processor operations. This is for internal use only (e.g., benchmarks) and is not exposed as a CLI argument.

### kv\_cache\_metrics `class-attribute` `instance-attribute` [¶](#vllm.config.observability.ObservabilityConfig.kv_cache_metrics "Permanent link")

```
kv_cache_metrics: bool = False
```

Enable KV cache residency metrics (lifetime, idle time, reuse gaps). Uses sampling to minimize overhead. Requires log stats to be enabled (i.e., --disable-log-stats not set).

### kv\_cache\_metrics\_sample `class-attribute` `instance-attribute` [¶](#vllm.config.observability.ObservabilityConfig.kv_cache_metrics_sample "Permanent link")

```
kv_cache_metrics_sample: float = Field(
    default=0.01, gt=0, le=1
)
```

Sampling rate for KV cache metrics (0.0, 1.0]. Default 0.01 = 1% of blocks.

### otlp\_traces\_endpoint `class-attribute` `instance-attribute` [¶](#vllm.config.observability.ObservabilityConfig.otlp_traces_endpoint "Permanent link")

```
otlp_traces_endpoint: str | None = None
```

Target URL to which OpenTelemetry traces will be sent.

### show\_hidden\_metrics `cached` `property` [¶](#vllm.config.observability.ObservabilityConfig.show_hidden_metrics "Permanent link")

```
show_hidden_metrics: bool
```

Check if the hidden metrics should be shown.

### show\_hidden\_metrics\_for\_version `class-attribute` `instance-attribute` [¶](#vllm.config.observability.ObservabilityConfig.show_hidden_metrics_for_version "Permanent link")

```
show_hidden_metrics_for_version: str | None = None
```

Enable deprecated Prometheus metrics that have been hidden since the specified version. For example, if a previously deprecated metric has been hidden since the v0.7.0 release, you use `--show-hidden-metrics-for-version=0.7` as a temporary escape hatch while you migrate to new metrics. The metric is likely to be removed completely in an upcoming release.

### \_validate\_collect\_detailed\_traces `classmethod` [¶](#vllm.config.observability.ObservabilityConfig._validate_collect_detailed_traces "Permanent link")

```
_validate_collect_detailed_traces(
    value: list[DetailedTraceModules] | None,
) -> list[DetailedTraceModules] | None
```

Handle the legacy case where users might provide a comma-separated string instead of a list of strings.

Source code in `vllm/config/observability.py`

```
@field_validator("collect_detailed_traces")
@classmethod
def_validate_collect_detailed_traces(
    cls, value: list[DetailedTraceModules] | None
) -> list[DetailedTraceModules] | None:
"""Handle the legacy case where users might provide a comma-separated
    string instead of a list of strings."""
    if value is not None and len(value) == 1 and "," in value[0]:
        value = cast(list[DetailedTraceModules], value[0].split(","))
    return value
```

### compute\_hash [¶](#vllm.config.observability.ObservabilityConfig.compute_hash "Permanent link")

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

Source code in `vllm/config/observability.py`

```
defcompute_hash(self) -> str:
"""
    WARNING: Whenever a new field is added to this config,
    ensure that it is included in the factors list if
    it affects the computation graph.

    Provide a hash that uniquely identifies all the configs
    that affect the structure of the computation
    graph from input ids/embeddings to the final hidden states,
    excluding anything before input ids/embeddings and after
    the final hidden states.
    """
    # no factors to consider.
    # this config will not affect the computation graph.
    factors: list[Any] = []
    hash_str = safe_hash(str(factors).encode(), usedforsecurity=False).hexdigest()
    return hash_str
```