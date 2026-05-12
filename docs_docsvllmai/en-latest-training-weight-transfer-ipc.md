---
title: IPC Engine - vLLM
url: https://docs.vllm.ai/en/latest/training/weight_transfer/ipc/
source: sitemap
fetched_at: 2026-05-07T21:15:26.198459803-03:00
rendered_js: false
word_count: 291
summary: This document explains the IPC weight transfer engine in vLLM, which utilizes CUDA IPC handles to share GPU memory directly between colocated training and inference processes to eliminate data copying.
tags:
    - cuda-ipc
    - memory-sharing
    - weight-transfer
    - colocation
    - distributed-training
    - gpu-optimization
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/training/weight_transfer/ipc.md "Edit this page")

The IPC weight transfer engine uses **CUDA IPC** (Inter-Process Communication) handles to share GPU memory directly between the trainer and inference workers on the **same node and same GPU**. This avoids any data copying, making it a efficient option when colocating training and inference.

## When to Use IPC[¶](#when-to-use-ipc "Permanent link")

- Training and inference on the **same GPU** (colocated)
- You want to minimize memory overhead by sharing tensors in-place

## How It Works[¶](#how-it-works "Permanent link")

1. The trainer creates CUDA tensors for each weight and generates IPC handles using `torch.multiprocessing.reductions.reduce_tensor`.
2. IPC handles are sent to the inference engine via **Ray.remote()** or **HTTP POST**.
3. The inference worker reconstructs the tensors from the handles, reading directly from the trainer's GPU memory.

Warning

IPC handles involve sending serialized Python objects. When using HTTP transport, you must set `VLLM_ALLOW_INSECURE_SERIALIZATION=1` on both the server and client. This is because IPC handles are pickled and base64-encoded for HTTP transmission.

## Initialization[¶](#initialization "Permanent link")

The IPC backend requires no initialization on either side. The `init_transfer_engine` call is a no-op for IPC.

## Sending Weights[¶](#sending-weights "Permanent link")

IPC supports two transport modes for delivering the handles:

### Ray Mode[¶](#ray-mode "Permanent link")

Used when vLLM is running as a Ray actor:

```
fromvllm.distributed.weight_transfer.ipc_engineimport (
    IPCTrainerSendWeightsArgs,
    IPCWeightTransferEngine,
)

trainer_args = IPCTrainerSendWeightsArgs(
    mode="ray",
    llm_handle=llm_actor_handle,
)

IPCWeightTransferEngine.trainer_send_weights(
    iterator=model.named_parameters(),
    trainer_args=trainer_args,
)
```

In Ray mode, the engine calls `llm_handle.update_weights.remote(...)` directly, passing the IPC handles via Ray's serialization.

### HTTP Mode[¶](#http-mode "Permanent link")

Used when vLLM is running as an HTTP server:

```
trainer_args = IPCTrainerSendWeightsArgs(
    mode="http",
    url="http://localhost:8000",
)

IPCWeightTransferEngine.trainer_send_weights(
    iterator=model.named_parameters(),
    trainer_args=trainer_args,
)
```

In HTTP mode, IPC handles are pickled, base64-encoded, and sent as JSON to the `/update_weights` endpoint.

See [`IPCTrainerSendWeightsArgs`](https://github.com/vllm-project/vllm/blob/main/vllm/distributed/weight_transfer/ipc_engine.py) for the full list of configurable fields.

## Examples[¶](#examples "Permanent link")

- [RLHF with IPC weight syncing (offline, Ray)](https://docs.vllm.ai/en/latest/examples/rl/rlhf_ipc/) - Colocated training and inference on a single GPU using Ray placement groups and CUDA IPC handles
- [RLHF with IPC weight syncing (online serving, HTTP)](https://docs.vllm.ai/en/latest/examples/rl/rlhf_http_ipc/) - Weight transfer with a vLLM HTTP server where both server and trainer share the same GPU