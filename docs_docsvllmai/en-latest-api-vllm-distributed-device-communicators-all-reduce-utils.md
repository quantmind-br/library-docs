---
title: all_reduce_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/device_communicators/all_reduce_utils/
source: sitemap
fetched_at: 2026-05-07T21:17:26.860877206-03:00
rendered_js: false
word_count: 246
summary: This document explains how to perform reliable GPU peer-to-peer (P2P) connectivity checks by combining CUDA IPC with inter-process testing to bypass potential driver reporting errors.
tags:
    - gpu-communication
    - cuda-ipc
    - p2p-access
    - distributed-computing
    - process-management
    - vllm
category: concept
---

Usually, checking if P2P access is enabled can be done by `torch.cuda.can_device_access_peer(src, tgt)`. However, sometimes the driver might be broken, and `torch.cuda.can_device_access_peer(src, tgt)` returns `True` even if P2P access is not actually possible. See https://github.com/vllm-project/vllm/issues/2728 and https://forums.developer.nvidia.com/t/direct-gpu-gpu-communication-does-not-seem-to-work-properly/283264/10 Therefore, we have to perform a real P2P access to check if it is actually possible.

Note on p2p and cuda IPC: Usually, one process uses one GPU: GPU src --&gt; cuda context src --&gt; tensor src --&gt; process src

We need to combine p2p and cuda IPC, so that: GPU src --&gt; cuda context src --&gt; tensor src --&gt; process src |shared| GPU tgt --&gt; cuda context tgt --&gt; tensor tgt --&gt; process tgt That is to say, process src creates a tensor in GPU src, passes IPC handle to process tgt, and process tgt accesses the tensor in GPU tgt. Any operation on the tensor in process tgt will be reflected in the tensor in process src, because they are the same memory segment. It is important to note that process tgt accesses the tensor in GPU tgt, not GPU src. That's why we need p2p access.

The most time-consuming part is the process creation. To avoid creating processes for every pair of GPUs, we use batched testing. We create two processes for testing all pairs of GPUs in batch. The trick is to reset the device after each test (which is not available in PyTorch).

Source code in `vllm/distributed/device_communicators/all_reduce_utils.py`

```
defcan_actually_p2p(
    batch_src: Sequence[int],
    batch_tgt: Sequence[int],
) -> Sequence[bool]:
"""
    Usually, checking if P2P access is enabled can be done by
    `torch.cuda.can_device_access_peer(src, tgt)`. However, sometimes
    the driver might be broken, and `torch.cuda.can_device_access_peer(src, tgt)`
    returns `True` even if P2P access is not actually possible.
    See https://github.com/vllm-project/vllm/issues/2728 and
    https://forums.developer.nvidia.com/t/direct-gpu-gpu-communication-does-not-seem-to-work-properly/283264/10
    Therefore, we have to perform a real P2P access to check if it is actually
    possible.

    Note on p2p and cuda IPC:
    Usually, one process uses one GPU:
    GPU src --> cuda context src --> tensor src --> process src

    We need to combine p2p and cuda IPC, so that:
    GPU src --> cuda context src --> tensor src --> process src
                                      |shared|
    GPU tgt --> cuda context tgt --> tensor tgt --> process tgt
    That is to say, process src creates a tensor in GPU src, passes IPC handle to
    process tgt, and process tgt accesses the tensor in GPU tgt. Any operation on the
    tensor in process tgt will be reflected in the tensor in process src, because
    they are the same memory segment.
    It is important to note that process tgt accesses the tensor in GPU tgt, not
    GPU src. That's why we need p2p access.

    The most time-consuming part is the process creation. To avoid creating
    processes for every pair of GPUs, we use batched testing. We create two
    processes for testing all pairs of GPUs in batch. The trick is to reset
    the device after each test (which is not available in PyTorch).
    """  # noqa
    cuda_visible_devices = envs.CUDA_VISIBLE_DEVICES
    # pass the CUDA_VISIBLE_DEVICES to the child process
    # to make sure they see the same set of GPUs

    # make sure the processes are spawned
    smp = mp.get_context("spawn")
    producer_queue = smp.Queue()
    consumer_queue = smp.Queue()
    result_queue = smp.Queue()
    p_src = smp.Process(
        target=producer,
        args=(
            batch_src,
            producer_queue,
            consumer_queue,
            result_queue,
            cuda_visible_devices,
        ),
    )
    p_tgt = smp.Process(
        target=consumer,
        args=(
            batch_tgt,
            producer_queue,
            consumer_queue,
            result_queue,
            cuda_visible_devices,
        ),
    )
    p_src.start()
    p_tgt.start()
    p_src.join()
    p_tgt.join()
    assert p_src.exitcode == 0 and p_tgt.exitcode == 0
    result: list[bool] = []
    for src, tgt in zip(batch_src, batch_tgt):
        a = result_queue.get()
        b = result_queue.get()
        if a != b:
            logger.warning(
                "Two processes do not agree on the P2P access"
                " status on %d -> %d, treat as disabled.",
                src,
                tgt,
            )
            result.append(False)
        else:
            result.append(a)
    return result
```