---
title: metadata - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/simple_kv_offload/metadata/
source: sitemap
fetched_at: 2026-05-07T21:41:42.051867743-03:00
rendered_js: false
word_count: 108
summary: This document defines the metadata structures used for communication between the scheduler and workers during CPU offload operations in the vLLM system.
tags:
    - cpu-offload
    - kv-cache
    - scheduler-worker-communication
    - memory-management
    - distributed-computing
category: reference
---

Metadata for SimpleCPUOffloadConnector.

Bases: `KVConnectorMetadata`

Metadata passed from scheduler to worker for CPU offload operations.

The worker receives flat block lists keyed by a monotonic event\_idx. Job-&gt;req\_id translation is handled by the scheduler-side manager (via inverse maps), so the worker never knows about request identities.

Source code in `vllm/v1/simple_kv_offload/metadata.py`

```
@dataclass
classSimpleCPUOffloadMetadata(KVConnectorMetadata):
"""
    Metadata passed from scheduler to worker for CPU offload operations.

    The worker receives flat block lists keyed by a monotonic event_idx.
    Job->req_id translation is handled by the scheduler-side manager
    (via inverse maps), so the worker never knows about request identities.
    """

    # Load event per step. INVALID_JOB_ID means no blocks to load this step.
    load_event: int = INVALID_JOB_ID
    load_gpu_blocks: list[int] = field(default_factory=list)
    load_cpu_blocks: list[int] = field(default_factory=list)
    # Reverse map: load_event->req_ids, for tracking requests with finished load events
    load_event_to_reqs: dict[int, list[str]] = field(default_factory=dict)

    # Store event per step. INVALID_JOB_ID means no blocks to store this step.
    store_event: int = INVALID_JOB_ID
    store_gpu_blocks: list[int] = field(default_factory=list)
    store_cpu_blocks: list[int] = field(default_factory=list)

    # Whether any requests were preempted this step and need flush pending transfers.
    need_flush: bool = False
```

Bases: `KVConnectorWorkerMetadata`

Worker -&gt; Scheduler metadata for completed store events.

Each worker reports {event\_idx: 1} for newly completed stores. `aggregate()` sums counts across workers within a step. The scheduler-side manager accumulates across steps and processes a store completion only when count reaches `world_size`.

Source code in `vllm/v1/simple_kv_offload/metadata.py`

```
@dataclass
classSimpleCPUOffloadWorkerMetadata(KVConnectorWorkerMetadata):
"""Worker -> Scheduler metadata for completed store events.

    Each worker reports {event_idx: 1} for newly completed stores.
    ``aggregate()`` sums counts across workers within a step.
    The scheduler-side manager accumulates across steps and processes
    a store completion only when count reaches ``world_size``.
    """

    completed_store_events: dict[int, int]

    defaggregate(
        self, other: "KVConnectorWorkerMetadata"
    ) -> "KVConnectorWorkerMetadata":
        assert isinstance(other, SimpleCPUOffloadWorkerMetadata)
        merged = dict(self.completed_store_events)
        for k, v in other.completed_store_events.items():
            merged[k] = merged.get(k, 0) + v
        return SimpleCPUOffloadWorkerMetadata(completed_store_events=merged)
```