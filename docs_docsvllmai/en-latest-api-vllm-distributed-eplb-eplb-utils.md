---
title: eplb_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/eplb/eplb_utils/
source: sitemap
fetched_at: 2026-05-07T21:17:58.015113752-03:00
rendered_js: false
word_count: 210
summary: This document describes utility functions for Expert Parallel Load Balancing (EPLB), specifically a synchronization class for cross-thread GPU event coordination and an environment variable override mechanism to prevent deadlocks with deep-learning backends.
tags:
    - eplb
    - cuda-synchronization
    - parallel-computing
    - thread-management
    - distributed-training
    - nccl
category: reference
---

Utility functions for EPLB (Expert Parallel Load Balancing).

## CpuGpuEvent [¶](#vllm.distributed.eplb.eplb_utils.CpuGpuEvent "Permanent link")

Combines a CUDA event with a CPU threading event to enforce record-&gt;wait ordering across two threads.

This class is designed for exactly two threads: one producer that calls record() and one consumer that calls wait(). Using it with more than two threads is not supported and will produce undefined behavior.

CUDA events alone are insufficient for cross-thread synchronization because waiting on an unrecorded CUDA event is a no-op. The wait will return immediately instead of blocking. This class adds a threading.Event so that the waiting thread blocks on the CPU side until record() is called, at which point the CUDA event is guaranteed to be in-flight and event.wait() will correctly synchronize the GPU stream.

Source code in `vllm/distributed/eplb/eplb_utils.py`

```
classCpuGpuEvent:
"""
    Combines a CUDA event with a CPU threading event to enforce record->wait
    ordering across two threads.

    This class is designed for exactly two threads: one producer that calls
    record() and one consumer that calls wait(). Using it with more than two
    threads is not supported and will produce undefined behavior.

    CUDA events alone are insufficient for cross-thread synchronization because
    waiting on an unrecorded CUDA event is a no-op. The wait will return
    immediately instead of blocking. This class adds a threading.Event so
    that the waiting thread blocks on the CPU side until record() is called, at
    which point the CUDA event is guaranteed to be in-flight and event.wait() will
    correctly synchronize the GPU stream.
    """

    def__init__(self):
        self._event = torch.cuda.Event()
        self._recorded = threading.Event()

    defwait(self, stream: torch.cuda.Stream | None = None):
"""
        Blocks the calling thread until record finishes. Used to guarantee that the
        record kernel is called before wait.

        Should only be called by the Async Eplb thread.
        """
        self._recorded.wait()
        self._event.wait(stream)
        self._recorded.clear()

    defrecord(self, stream: torch.cuda.Stream | None = None):
"""
        Unblocks the waiting thread after calling event.record().

        Should only be called by the main thread.
        """
        if self._recorded.is_set():
            raise RuntimeError(
                "CpuGpuEvent.record() called before the previous event was "
                "consumed by wait()"
            )
        self._event = torch.cuda.Event()
        self._event.record(stream)
        self._recorded.set()
```

### record [¶](#vllm.distributed.eplb.eplb_utils.CpuGpuEvent.record "Permanent link")

```
record(stream: Stream | None = None)
```

Unblocks the waiting thread after calling event.record().

Should only be called by the main thread.

Source code in `vllm/distributed/eplb/eplb_utils.py`

```
defrecord(self, stream: torch.cuda.Stream | None = None):
"""
    Unblocks the waiting thread after calling event.record().

    Should only be called by the main thread.
    """
    if self._recorded.is_set():
        raise RuntimeError(
            "CpuGpuEvent.record() called before the previous event was "
            "consumed by wait()"
        )
    self._event = torch.cuda.Event()
    self._event.record(stream)
    self._recorded.set()
```

### wait [¶](#vllm.distributed.eplb.eplb_utils.CpuGpuEvent.wait "Permanent link")

```
wait(stream: Stream | None = None)
```

Blocks the calling thread until record finishes. Used to guarantee that the record kernel is called before wait.

Should only be called by the Async Eplb thread.

Source code in `vllm/distributed/eplb/eplb_utils.py`

```
defwait(self, stream: torch.cuda.Stream | None = None):
"""
    Blocks the calling thread until record finishes. Used to guarantee that the
    record kernel is called before wait.

    Should only be called by the Async Eplb thread.
    """
    self._recorded.wait()
    self._event.wait(stream)
    self._recorded.clear()
```

## override\_envs\_for\_eplb [¶](#vllm.distributed.eplb.eplb_utils.override_envs_for_eplb "Permanent link")

Override environment variables for EPLB when specific conditions are met.

Parameters:

Name Type Description Default `parallel_config` `ParallelConfig`

The parallel configuration object.

*required*

Source code in `vllm/distributed/eplb/eplb_utils.py`

```
defoverride_envs_for_eplb(parallel_config: ParallelConfig) -> None:
"""
    Override environment variables for EPLB when specific conditions are met.

    Args:
        parallel_config: The parallel configuration object.
    """
    is_data_parallel = parallel_config.data_parallel_size > 1
    is_eplb_enabled = parallel_config.enable_eplb
    async_eplb = parallel_config.eplb_config.use_async
    is_deepep_ll = parallel_config.all2all_backend == "deepep_low_latency"
    is_nccl_based_eplb_communicator = parallel_config.eplb_config.communicator in (
        "torch_nccl",
        "pynccl",
    )

    # Override NCCL_MAX_CTAS to avoid hangs when using async EPLB with the
    # DeepEP low-latency backend.
    #
    # The hang happens when two ranks interleave kernel launches differently
    # between NCCL collectives (used by async EPLB weight exchange) and DeepEP
    # low-latency (LL) kernels. DeepEP LL uses a cooperative launch and tries
    # to reserve a large fraction of the GPU's SMs; if those SMs are currently
    # occupied by NCCL, the DeepEP LL launch blocks until enough SMs are
    # freed.
    #
    # If rank A enters DeepEP LL in main thread while rank B is still executing
    # NCCL in async thread, rank A can block waiting for SMs, while rank B can
    # block inside NCCL waiting for rank A to participate in the collective.
    # This circular wait causes a deadlock.
    # Limiting NCCL occupancy via NCCL_MAX_CTAS leaves space for the DeepEP
    # cooperative kernel to launch and complete, breaking the deadlock.
    # See: https://github.com/deepseek-ai/DeepEP/issues/496
    if (
        is_data_parallel
        and is_eplb_enabled
        and is_deepep_ll
        and async_eplb
        and is_nccl_based_eplb_communicator
    ):
        current_value_str = os.getenv("NCCL_MAX_CTAS")

        if current_value_str and current_value_str.isdigit():
            return

        override_value = 8
        os.environ["NCCL_MAX_CTAS"] = str(override_value)
        logger.info_once(
            f"EPLB: Setting NCCL_MAX_CTAS={override_value} "
            "for expert parallel with NCCL-based EPLB communicator and "
            "deepep_low_latency backend",
            scope="global",
        )
```