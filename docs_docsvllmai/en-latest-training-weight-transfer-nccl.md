---
title: NCCL Engine - vLLM
url: https://docs.vllm.ai/en/latest/training/weight_transfer/nccl/
source: sitemap
fetched_at: 2026-05-07T21:15:26.720237564-03:00
rendered_js: false
word_count: 350
summary: This document explains how to utilize the NCCL weight transfer engine in vLLM to synchronize model weights between a trainer and inference workers across multi-GPU or multi-node environments.
tags:
    - nccl
    - weight-transfer
    - distributed-training
    - model-parallelism
    - vllm
    - high-performance-computing
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/training/weight_transfer/nccl.md "Edit this page")

The NCCL weight transfer engine uses [NCCL](https://developer.nvidia.com/nccl) broadcast operations to transfer weights from the trainer to inference workers. It supports **multi-node** and **multi-GPU** setups where the trainer and inference engine run on separate GPUs.

## When to Use NCCL[¶](#when-to-use-nccl "Permanent link")

- Training and inference on **separate GPUs** (possibly across nodes)
- **Tensor-parallel** inference with multiple workers that all need the updated weights
- You need high-bandwidth, low-latency weight transfer over NVLink or InfiniBand

## How It Works[¶](#how-it-works "Permanent link")

1. The trainer and all inference workers join a shared NCCL process group using [`StatelessProcessGroup`](https://docs.vllm.ai/en/latest/api/vllm/distributed/utils/#vllm.distributed.utils.StatelessProcessGroup "            StatelessProcessGroup            dataclass   ") (vLLM's torch.distributed-independent group abstraction).
2. The trainer broadcasts weights to all workers simultaneously. Each worker receives and loads weights incrementally.
3. Optionally, **packed tensor broadcasting** batches multiple small tensors into larger buffers with double/triple buffering and CUDA stream overlap for higher throughput. This implementation is based on [NeMo-RL's packed tensor](https://github.com/NVIDIA-NeMo/RL/blob/main/nemo_rl/utils/packed_tensor.py).

## Initialization[¶](#initialization "Permanent link")

NCCL requires explicit process group setup. The trainer and inference workers must agree on a master address, port, and world size.

### Inference Side[¶](#inference-side "Permanent link")

```
fromvllm.distributed.weight_transfer.baseimport WeightTransferInitRequest

# rank_offset accounts for the trainer occupying rank 0
llm.init_weight_transfer_engine(
    WeightTransferInitRequest(
        init_info=dict(
            master_address=master_address,
            master_port=master_port,
            rank_offset=1,
            world_size=world_size,  # trainer + all inference workers
        )
    )
)
```

### Trainer Side[¶](#trainer-side "Permanent link")

```
fromvllm.distributed.weight_transfer.nccl_engineimport (
    NCCLWeightTransferEngine,
)

group = NCCLWeightTransferEngine.trainer_init(
    dict(
        master_address=master_address,
        master_port=master_port,
        world_size=world_size,
    )
)
```

Note

`trainer_init` always assigns the trainer to rank 0. Inference workers start at `rank_offset` (typically 1).

## Sending Weights[¶](#sending-weights "Permanent link")

```
fromvllm.distributed.weight_transfer.nccl_engineimport (
    NCCLTrainerSendWeightsArgs,
    NCCLWeightTransferEngine,
)

trainer_args = NCCLTrainerSendWeightsArgs(
    group=group,
    packed=True,  # use packed broadcasting for efficiency
)

NCCLWeightTransferEngine.trainer_send_weights(
    iterator=model.named_parameters(),
    trainer_args=trainer_args,
)
```

See [`NCCLTrainerSendWeightsArgs`](https://github.com/vllm-project/vllm/blob/main/vllm/distributed/weight_transfer/nccl_engine.py) for the full list of configurable fields.

### Packed Tensor Broadcasting[¶](#packed-tensor-broadcasting "Permanent link")

When `packed=True`, multiple weight tensors are packed into large contiguous buffers before broadcasting. This reduces the number of NCCL operations and uses double/triple buffering with dedicated CUDA streams for overlap between packing, broadcasting, and unpacking.

Both the trainer ([`NCCLTrainerSendWeightsArgs`](https://docs.vllm.ai/en/latest/api/vllm/distributed/weight_transfer/nccl_engine/#vllm.distributed.weight_transfer.nccl_engine.NCCLTrainerSendWeightsArgs "            NCCLTrainerSendWeightsArgs            dataclass   ")) and inference side ([`NCCLWeightTransferUpdateInfo`](https://docs.vllm.ai/en/latest/api/vllm/distributed/weight_transfer/nccl_engine/#vllm.distributed.weight_transfer.nccl_engine.NCCLWeightTransferUpdateInfo "            NCCLWeightTransferUpdateInfo            dataclass   ")) must use matching `packed_buffer_size_bytes` and `packed_num_buffers` values.

## Receiving Weights (Inference Side)[¶](#receiving-weights-inference-side "Permanent link")

The inference side triggers weight reception by calling `update_weights`:

```
fromvllm.distributed.weight_transfer.baseimport WeightTransferUpdateRequest

llm.update_weights(
    WeightTransferUpdateRequest(
        update_info=dict(
            names=names,
            dtype_names=dtype_names,
            shapes=shapes,
            packed=True,
        )
    )
)
```

The `names`, `dtype_names`, and `shapes` lists describe each parameter. These must match the order in which the trainer iterates over its parameters.

## Examples[¶](#examples "Permanent link")

- [RLHF with NCCL weight syncing (offline, Ray)](https://docs.vllm.ai/en/latest/examples/rl/rlhf_nccl/) - Trainer on one GPU, 2x tensor-parallel vLLM engine on two others, with packed NCCL weight broadcast
- [RLHF with async weight syncing (offline, Ray)](https://docs.vllm.ai/en/latest/examples/rl/rlhf_async_new_apis/) - Async generation with mid-flight pause, weight sync, resume, and validation against a fresh model
- [RLHF with NCCL weight syncing (online serving, HTTP)](https://docs.vllm.ai/en/latest/examples/rl/rlhf_http_nccl/) - Weight transfer with a running vLLM HTTP server using HTTP control plane and NCCL data plane