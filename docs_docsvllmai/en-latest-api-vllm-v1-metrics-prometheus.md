---
title: prometheus - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/metrics/prometheus/
source: sitemap
fetched_at: 2026-05-07T21:41:12.163571251-03:00
rendered_js: false
word_count: 95
summary: This document provides an API reference for managing Prometheus metrics collection, including multiprocess configuration and registry cleanup functions within the vLLM framework.
tags:
    - prometheus
    - metrics-collection
    - multiprocessing
    - api-reference
    - monitoring
    - vllm
category: api
---

## get\_prometheus\_registry [¶](#vllm.v1.metrics.prometheus.get_prometheus_registry "Permanent link")

```
get_prometheus_registry() -> CollectorRegistry
```

Get the appropriate prometheus registry based on multiprocessing configuration.

Returns:

Name Type Description `Registry` `CollectorRegistry`

A prometheus registry

Source code in `vllm/v1/metrics/prometheus.py`

```
defget_prometheus_registry() -> CollectorRegistry:
"""Get the appropriate prometheus registry based on multiprocessing
    configuration.

    Returns:
        Registry: A prometheus registry
    """
    if os.getenv("PROMETHEUS_MULTIPROC_DIR") is not None:
        logger.debug("Using multiprocess registry for prometheus metrics")
        registry = CollectorRegistry()
        multiprocess.MultiProcessCollector(registry)
        return registry

    return REGISTRY
```

## setup\_multiprocess\_prometheus [¶](#vllm.v1.metrics.prometheus.setup_multiprocess_prometheus "Permanent link")

```
setup_multiprocess_prometheus()
```

Set up prometheus multiprocessing directory if not already configured.

Source code in `vllm/v1/metrics/prometheus.py`

```
defsetup_multiprocess_prometheus():
"""Set up prometheus multiprocessing directory if not already configured."""
    global _prometheus_multiproc_dir

    if "PROMETHEUS_MULTIPROC_DIR" not in os.environ:
        # Make TemporaryDirectory for prometheus multiprocessing
        # Note: global TemporaryDirectory will be automatically
        # cleaned up upon exit.
        _prometheus_multiproc_dir = tempfile.TemporaryDirectory()
        os.environ["PROMETHEUS_MULTIPROC_DIR"] = _prometheus_multiproc_dir.name
        logger.debug(
            "Created PROMETHEUS_MULTIPROC_DIR at %s", _prometheus_multiproc_dir.name
        )
    else:
        logger.warning(
            "Found PROMETHEUS_MULTIPROC_DIR was set by user. "
            "This directory must be wiped between vLLM runs or "
            "you will find inaccurate metrics. Unset the variable "
            "and vLLM will properly handle cleanup."
        )
```

## shutdown\_prometheus [¶](#vllm.v1.metrics.prometheus.shutdown_prometheus "Permanent link")

Shutdown prometheus metrics.

Source code in `vllm/v1/metrics/prometheus.py`

```
defshutdown_prometheus():
"""Shutdown prometheus metrics."""

    path = _prometheus_multiproc_dir
    if path is None:
        return
    try:
        pid = os.getpid()
        multiprocess.mark_process_dead(pid, path)
        logger.debug("Marked Prometheus metrics for process %d as dead", pid)
    except Exception as e:
        logger.error("Error during metrics cleanup: %s", str(e))
```

## unregister\_vllm\_metrics [¶](#vllm.v1.metrics.prometheus.unregister_vllm_metrics "Permanent link")

```
unregister_vllm_metrics()
```

Unregister any existing vLLM collectors from the prometheus registry.

This is useful for testing and CI/CD where metrics may be registered multiple times across test runs.

Also, in case of multiprocess, we need to unregister the metrics from the global registry.

Source code in `vllm/v1/metrics/prometheus.py`

```
defunregister_vllm_metrics():
"""Unregister any existing vLLM collectors from the prometheus registry.

    This is useful for testing and CI/CD where metrics may be registered
    multiple times across test runs.

    Also, in case of multiprocess, we need to unregister the metrics from the
    global registry.
    """
    registry = REGISTRY
    # Unregister any existing vLLM collectors
    for collector in list(registry._collector_to_names):
        if hasattr(collector, "_name") and "vllm" in collector._name:
            registry.unregister(collector)
```