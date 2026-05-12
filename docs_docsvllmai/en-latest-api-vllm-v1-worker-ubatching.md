---
title: ubatching - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/worker/ubatching/
source: sitemap
fetched_at: 2026-05-07T21:43:16.853213438-03:00
rendered_js: false
word_count: 16
summary: This document defines the UBatchContext class, which provides a synchronization context manager for managing micro-batching operations in vLLM using threading events and CUDA stream management.
tags:
    - micro-batching
    - cuda-streams
    - synchronization
    - threading
    - vllm-internals
    - gpu-computing
category: reference
---

## vllm.v1.worker.ubatching [¶](#vllm.v1.worker.ubatching "Permanent link")

## UBatchContext [¶](#vllm.v1.worker.ubatching.UBatchContext "Permanent link")

Context manager for micro-batching synchronization using threading events.

Source code in `vllm/v1/worker/ubatching.py`

```
classUBatchContext:
"""
    Context manager for micro-batching synchronization using threading events.
    """

    def__init__(
        self,
        id: int,
        comm_stream: torch.cuda.Stream,
        compute_stream: torch.cuda.Stream,
        forward_context: ForwardContext,
        ready_barrier: threading.Barrier,
        cpu_wait_event: threading.Event,
        cpu_signal_event: threading.Event,
        gpu_comm_done_event: torch.Event,
        gpu_compute_done_event: torch.Event,
        schedule: str = "default",
    ):
        self.id = id
        self.comm_stream = comm_stream
        self.compute_stream = compute_stream
        self.forward_context = forward_context
        self.ready_barrier = ready_barrier
        self.cpu_wait_event = cpu_wait_event
        self.cpu_signal_event = cpu_signal_event
        self.current_stream = compute_stream
        self.gpu_comm_done_event = gpu_comm_done_event
        self.gpu_compute_done_event = gpu_compute_done_event
        self.schedule = schedule
        self.recv_hook = None

    def__enter__(self):
        global _CURRENT_CONTEXTS, _THREAD_ID_TO_CONTEXT
        _THREAD_ID_TO_CONTEXT[threading.get_ident()] = self.id
        _CURRENT_CONTEXTS[self.id] = self
        # _NUM_UBATCHES is set in make_ubatch_contexts
        self.ready_barrier.wait()

        self.cpu_wait_event.wait()
        self.cpu_wait_event.clear()
        self._restore_context()
        # Assume we want to start on the compute stream
        self.update_stream(self.compute_stream)
        return self

    def__exit__(self, exc_type, exc_val, exc_tb):
        global _CURRENT_CONTEXTS, _THREAD_ID_TO_CONTEXT
        _CURRENT_CONTEXTS[self.id] = None
        del _THREAD_ID_TO_CONTEXT[threading.get_ident()]
        self.maybe_run_recv_hook()
        self.cpu_signal_event.set()
        self.cpu_wait_event.clear()
        return False

    def_restore_context(self):
        forward_context._forward_context = self.forward_context

    defupdate_stream(self, stream):
        self.current_stream = stream
        if current_stream() != self.current_stream:
            torch.cuda.set_stream(self.current_stream)

    def_signal_comm_done(self):
        self.gpu_comm_done_event.record(self.comm_stream)

    def_signal_compute_done(self):
        self.gpu_compute_done_event.record(self.compute_stream)

    def_wait_compute_done(self):
        self.comm_stream.wait_event(self.gpu_compute_done_event)

    def_wait_comm_done(self):
        self.compute_stream.wait_event(self.gpu_comm_done_event)

    def_cpu_yield(self):
        # It is critical for correctness that only one thread is running
        # at a time. These asserts just make sure that this is the only
        # thread running before waking the other one up and going to sleep
        assert forward_context._forward_context == self.forward_context
        assert current_stream() == self.current_stream
        assert not self.cpu_wait_event.is_set()

        self.cpu_signal_event.set()
        self.cpu_wait_event.wait()
        self.cpu_wait_event.clear()
        self._restore_context()

    defswitch_to_comm(self):
        self.update_stream(self.comm_stream)

    defswitch_to_compute(self):
        self.update_stream(self.compute_stream)

    defswitch_to_comm_sync(self):
        self._signal_compute_done()
        self.update_stream(self.comm_stream)
        self._wait_compute_done()

    defswitch_to_compute_sync(self):
        self._signal_comm_done()
        self.update_stream(self.compute_stream)
        self._wait_comm_done()

    defmaybe_run_recv_hook(self):
        if self.recv_hook is not None:
            self.recv_hook()
            self.recv_hook = None

    defyield_(self):
        self.current_stream = current_stream()
        self._cpu_yield()
        self.update_stream(self.current_stream)

    defyield_and_switch_from_compute_to_comm(self):
        assert current_stream() == self.compute_stream
        self._signal_compute_done()
        self._cpu_yield()
        assert self.current_stream == self.compute_stream
        self.update_stream(self.comm_stream)
        self._wait_compute_done()

    defyield_and_switch_from_comm_to_compute(self):
        assert current_stream() == self.comm_stream
        self._signal_comm_done()
        self._cpu_yield()
        assert self.current_stream == self.comm_stream
        self.update_stream(self.compute_stream)
        self._wait_comm_done()
```