---
title: common - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/offloading/common/
source: sitemap
fetched_at: 2026-05-07T21:18:47.857322342-03:00
rendered_js: false
word_count: 110
summary: This document defines the data structures and methods for tracking and aggregating KV transfer job completions between workers and the scheduler in a distributed environment.
tags:
    - distributed-computing
    - kv-transfer
    - metadata-management
    - job-scheduling
    - data-offloading
category: reference
---

## vllm.distributed.kv\_transfer.kv\_connector.v1.offloading.common [¶](#vllm.distributed.kv_transfer.kv_connector.v1.offloading.common "Permanent link")

Bases: `KVConnectorWorkerMetadata`

Worker -&gt; Scheduler metadata for completed transfer jobs.

Each worker reports {job\_id: 1} for newly completed transfer jobs (load or store). aggregate() sums counts across workers within a step. The scheduler accumulates across steps and processes a transfer completion only when count reaches num\_workers.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/offloading/common.py`

```
@dataclass
classOffloadingWorkerMetadata(KVConnectorWorkerMetadata):
"""Worker -> Scheduler metadata for completed transfer jobs.

    Each worker reports {job_id: 1} for newly completed transfer jobs
    (load or store). aggregate() sums counts across workers within a step.
    The scheduler accumulates across steps and processes
    a transfer completion only when count reaches num_workers.
    """

    completed_jobs: dict[int, int] = field(default_factory=dict)

    defmark_completed(self, job_id: int) -> None:
"""Record a transfer job completion from this worker."""
        self.completed_jobs[job_id] = 1

    defaggregate(
        self, other: "KVConnectorWorkerMetadata"
    ) -> "KVConnectorWorkerMetadata":
        assert isinstance(other, OffloadingWorkerMetadata)

        merged = dict(self.completed_jobs)
        for job_id, v in other.completed_jobs.items():
            merged[job_id] = merged.get(job_id, 0) + v

        return OffloadingWorkerMetadata(completed_jobs=merged)
```

### mark\_completed [¶](#vllm.distributed.kv_transfer.kv_connector.v1.offloading.common.OffloadingWorkerMetadata.mark_completed "Permanent link")

```
mark_completed(job_id: int) -> None
```

Record a transfer job completion from this worker.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/offloading/common.py`

```
defmark_completed(self, job_id: int) -> None:
"""Record a transfer job completion from this worker."""
    self.completed_jobs[job_id] = 1
```

## TransferJob `dataclass` [¶](#vllm.distributed.kv_transfer.kv_connector.v1.offloading.common.TransferJob "Permanent link")

A transfer job bundling request context with transfer spec.

Used for both loads and stores, keyed by scheduler-assigned job ID. The worker reports the job ID back when the transfer finishes, and the scheduler processes the completion.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/offloading/common.py`

```
@dataclass
classTransferJob:
"""A transfer job bundling request context with transfer spec.

    Used for both loads and stores, keyed by scheduler-assigned job ID.
    The worker reports the job ID back when the transfer finishes,
    and the scheduler processes the completion.
    """

    req_id: ReqId
    transfer_spec: TransferSpec
```