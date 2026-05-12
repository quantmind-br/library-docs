---
title: kv_cache_metrics - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/core/kv_cache_metrics/
source: sitemap
fetched_at: 2026-05-07T21:40:19.720306106-03:00
rendered_js: false
word_count: 44
summary: This document defines classes for tracking and collecting performance metrics related to KV cache block lifecycles and eviction events in vLLM.
tags:
    - kv-cache
    - metrics-collection
    - block-lifecycle
    - performance-monitoring
    - vllm-core
category: reference
---

KV cache metrics tracking.

## BlockMetricsState [¶](#vllm.v1.core.kv_cache_metrics.BlockMetricsState "Permanent link")

Tracks lifecycle metrics for a single KV cache block.

Source code in `vllm/v1/core/kv_cache_metrics.py`

```
classBlockMetricsState:
"""Tracks lifecycle metrics for a single KV cache block."""

    def__init__(self):
        now_ns = time.monotonic_ns()
        self.birth_time_ns = now_ns
        self.last_access_ns = now_ns
        # Bounded to prevent unbounded growth if a block is accessed many times.
        self.access_history: deque[int] = deque(maxlen=4)

    defrecord_access(self) -> None:
        now_ns = time.monotonic_ns()
        self.last_access_ns = now_ns
        self.access_history.append(now_ns)

    defget_lifetime_seconds(self) -> float:
        now_ns = time.monotonic_ns()
        return (now_ns - self.birth_time_ns) / 1e9

    defget_idle_time_seconds(self) -> float:
        now_ns = time.monotonic_ns()
        return (now_ns - self.last_access_ns) / 1e9

    defget_reuse_gaps_seconds(self) -> list[float]:
        if len(self.access_history) < 2:
            return []
        history = list(self.access_history)
        return [(history[i] - history[i - 1]) / 1e9 for i in range(1, len(history))]
```

## KVCacheMetricsCollector [¶](#vllm.v1.core.kv_cache_metrics.KVCacheMetricsCollector "Permanent link")

Collects KV cache residency metrics with sampling.

Source code in `vllm/v1/core/kv_cache_metrics.py`

```
classKVCacheMetricsCollector:
"""Collects KV cache residency metrics with sampling."""

    def__init__(self, sample_rate: float = 0.01):
        assert 0 < sample_rate <= 1.0, (
            f"sample_rate must be in (0, 1.0], got {sample_rate}"
        )
        self.sample_rate = sample_rate

        self.block_metrics: dict[int, BlockMetricsState] = {}

        self._eviction_events: list[KVCacheEvictionEvent] = []

    defshould_sample_block(self) -> bool:
        return random.random() < self.sample_rate

    defon_block_allocated(self, block: "KVCacheBlock") -> None:
        if self.should_sample_block():
            self.block_metrics[block.block_id] = BlockMetricsState()

    defon_block_accessed(self, block: "KVCacheBlock") -> None:
        metrics = self.block_metrics.get(block.block_id)
        if metrics:
            metrics.record_access()

    defon_block_evicted(self, block: "KVCacheBlock") -> None:
        metrics = self.block_metrics.pop(block.block_id, None)
        if not metrics:
            return

        lifetime = metrics.get_lifetime_seconds()
        idle_time = metrics.get_idle_time_seconds()
        reuse_gaps = tuple(metrics.get_reuse_gaps_seconds())

        self._eviction_events.append(
            KVCacheEvictionEvent(
                lifetime_seconds=lifetime,
                idle_seconds=idle_time,
                reuse_gaps_seconds=reuse_gaps,
            )
        )

    defreset(self) -> None:
"""Clear all state on cache reset."""
        self.block_metrics.clear()
        self._eviction_events.clear()

    defdrain_events(self) -> list[KVCacheEvictionEvent]:
        events = self._eviction_events
        self._eviction_events = []
        return events
```

### reset [¶](#vllm.v1.core.kv_cache_metrics.KVCacheMetricsCollector.reset "Permanent link")

Clear all state on cache reset.

Source code in `vllm/v1/core/kv_cache_metrics.py`

```
defreset(self) -> None:
"""Clear all state on cache reset."""
    self.block_metrics.clear()
    self._eviction_events.clear()
```