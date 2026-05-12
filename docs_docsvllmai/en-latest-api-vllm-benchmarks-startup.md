---
title: startup - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/benchmarks/startup/
source: sitemap
fetched_at: 2026-05-07T21:15:55.838256386-03:00
rendered_js: false
word_count: 145
summary: This document outlines the vLLM benchmark module for measuring cold and warm startup performance, detailing the classes and functions used to isolate cache environments and collect timing metrics.
tags:
    - vllm
    - benchmarking
    - performance-metrics
    - model-startup
    - caching
    - subprocess-execution
category: reference
---

## vllm.benchmarks.startup [¶](#vllm.benchmarks.startup "Permanent link")

Benchmark the cold and warm startup time of vLLM models.

This script measures total startup time (including model loading, compilation, and cache operations) for both cold and warm scenarios: - Cold startup: Fresh start with no caches (temporary cache directories) - Warm startup: Using cached compilation and model info

## MetricDesc [¶](#vllm.benchmarks.startup.MetricDesc "Permanent link")

Bases: `NamedTuple`

Descriptor for a metric to collect from each iteration.

Source code in `vllm/benchmarks/startup.py`

```
classMetricDesc(NamedTuple):
"""Descriptor for a metric to collect from each iteration."""

    iter_key: str  # key in the iteration result dict
    suffix: str  # result key suffix, e.g. "startup", "compilation"
    display_name: str
```

## MetricStats [¶](#vllm.benchmarks.startup.MetricStats "Permanent link")

Bases: `NamedTuple`

Aggregated statistics for a single benchmark metric.

Source code in `vllm/benchmarks/startup.py`

```
classMetricStats(NamedTuple):
"""Aggregated statistics for a single benchmark metric."""

    key: str  # e.g. "cold_startup", "warm_encoder_compilation"
    display_name: str
    values: list[float]
    avg: float
    percentiles: dict[int, float]
```

## cold\_startup [¶](#vllm.benchmarks.startup.cold_startup "Permanent link")

Context manager to measure cold startup time: 1. Uses a temporary directory for vLLM cache to avoid any pollution between cold startup iterations. 2. Uses inductor's fresh\_cache to clear torch.compile caches.

Source code in `vllm/benchmarks/startup.py`

```
@contextmanager
defcold_startup():
"""
    Context manager to measure cold startup time:
    1. Uses a temporary directory for vLLM cache to avoid any pollution
       between cold startup iterations.
    2. Uses inductor's fresh_cache to clear torch.compile caches.
    """
    fromtorch._inductor.utilsimport fresh_cache

    # Use temporary directory for caching to avoid any pollution between cold startups
    original_cache_root = os.environ.get("VLLM_CACHE_ROOT")
    temp_cache_dir = tempfile.mkdtemp(prefix="vllm_startup_bench_cold_")
    try:
        os.environ["VLLM_CACHE_ROOT"] = temp_cache_dir
        with fresh_cache():
            yield
    finally:
        # Clean up temporary cache directory
        shutil.rmtree(temp_cache_dir, ignore_errors=True)
        if original_cache_root:
            os.environ["VLLM_CACHE_ROOT"] = original_cache_root
        else:
            os.environ.pop("VLLM_CACHE_ROOT", None)
```

## run\_startup\_in\_subprocess [¶](#vllm.benchmarks.startup.run_startup_in_subprocess "Permanent link")

```
run_startup_in_subprocess(engine_args, result_queue)
```

Run LLM startup in a subprocess and return timing metrics via a queue. This ensures complete isolation between iterations.

Source code in `vllm/benchmarks/startup.py`

```
defrun_startup_in_subprocess(engine_args, result_queue):
"""
    Run LLM startup in a subprocess and return timing metrics via a queue.
    This ensures complete isolation between iterations.
    """
    try:
        # Import inside the subprocess to avoid issues with forking
        fromvllmimport LLM

        # Measure total startup time
        start_time = time.perf_counter()

        llm = LLM.from_engine_args(engine_args)

        total_startup_time = time.perf_counter() - start_time

        # Extract compilation time if available
        compilation_time = 0.0
        encoder_compilation_time = 0.0
        if hasattr(llm.llm_engine, "vllm_config"):
            vllm_config = llm.llm_engine.vllm_config
            if (
                hasattr(vllm_config, "compilation_config")
                and vllm_config.compilation_config is not None
            ):
                compilation_time = vllm_config.compilation_config.compilation_time
                encoder_compilation_time = (
                    vllm_config.compilation_config.encoder_compilation_time
                )

        result_queue.put(
            {
                "total_startup_time": total_startup_time,
                "compilation_time": compilation_time,
                "encoder_compilation_time": encoder_compilation_time,
            }
        )

    except Exception as e:
        result_queue.put(None)
        result_queue.put(str(e))
```