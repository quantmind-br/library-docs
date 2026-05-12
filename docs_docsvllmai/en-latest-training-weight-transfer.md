---
title: Weight Transfer - vLLM
url: https://docs.vllm.ai/en/latest/training/weight_transfer/
source: sitemap
fetched_at: 2026-05-07T21:15:24.312592628-03:00
rendered_js: false
word_count: 320
summary: This document outlines the vLLM weight transfer system designed to synchronize model weights between training processes and inference engines during reinforcement learning workflows. It details the architecture, supported transport backends, configuration methods, and API endpoints for managing weight updates.
tags:
    - weight-transfer
    - vllm
    - reinforcement-learning
    - model-synchronization
    - nccl
    - ipc
    - distributed-training
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/training/weight_transfer/README.md "Edit this page")

vLLM provides a pluggable weight transfer system for synchronizing model weights from a training process to the inference engine during reinforcement learning (RL) workflows. This is essential for RLHF, GRPO, and other online RL methods where the policy model is iteratively updated during training and the updated weights must be reflected in the inference engine for rollout generation.

## Architecture[¶](#architecture "Permanent link")

The weight transfer system follows a **two-phase protocol** with a pluggable backend design:

1. **Initialization** (`init_weight_transfer_engine`): Establishes the communication channel between the trainer and inference workers. Called once before the training loop begins.
2. **Weight Update** (`update_weights`): Transfers updated weights from the trainer to the inference engine. Called after each training step (or batch of steps).

## Available Backends[¶](#available-backends "Permanent link")

Backend Transport Use Case [NCCL](https://docs.vllm.ai/en/latest/training/weight_transfer/nccl/) NCCL broadcast Separate GPUs for training and inference [IPC](https://docs.vllm.ai/en/latest/training/weight_transfer/ipc/) CUDA IPC handles Colocated training and inference on same GPU

## Configuration[¶](#configuration "Permanent link")

Specify the weight transfer backend through [`WeightTransferConfig`](https://docs.vllm.ai/en/latest/api/vllm/config/weight_transfer/#vllm.config.weight_transfer.WeightTransferConfig "            WeightTransferConfig"). The backend determines which engine handles the weight synchronization.

### Programmatic (Offline Inference)[¶](#programmatic-offline-inference "Permanent link")

```
fromvllmimport LLM
fromvllm.configimport WeightTransferConfig

llm = LLM(
    model="my-model",
    weight_transfer_config=WeightTransferConfig(backend="nccl"),  # or "ipc"
)
```

### CLI (Online Serving)[¶](#cli-online-serving "Permanent link")

```
vllmservemy-model\
--weight-transfer-config'{"backend": "nccl"}'
```

The `backend` field accepts `"nccl"` (default) or `"ipc"`.

## API Endpoints[¶](#api-endpoints "Permanent link")

When running vLLM as an HTTP server, the following endpoints are available for weight transfer:

Endpoint Method Description `/init_weight_transfer_engine` POST Initialize the weight transfer engine with backend-specific info `/update_weights` POST Trigger a weight update with backend-specific metadata `/pause` POST Pause generation before weight sync to handle inflight requests `/resume` POST Resume generation after weight sync `/get_world_size` GET Get the number of inference workers (useful for NCCL world size calculation)

Note

The HTTP weight transfer endpoints require `VLLM_SERVER_DEV_MODE=1` to be set.

## Trainer-Side API[¶](#trainer-side-api "Permanent link")

Both backends provide static methods that the trainer calls to send weights. The general pattern is:

```
# 1. Initialize the transfer engine (backend-specific)
EngineClass.trainer_init(init_info)

# 2. Send weights to inference workers
EngineClass.trainer_send_weights(
    iterator=model.named_parameters(),
    trainer_args=backend_specific_args,
)
```

See the [NCCL](https://docs.vllm.ai/en/latest/training/weight_transfer/nccl/) and [IPC](https://docs.vllm.ai/en/latest/training/weight_transfer/ipc/) pages for backend-specific trainer APIs and full examples.

## Extending the System[¶](#extending-the-system "Permanent link")

The weight transfer system is designed to be extensible. You can implement custom backends by subclassing [`WeightTransferEngine`](https://docs.vllm.ai/en/latest/api/vllm/distributed/weight_transfer/base/#vllm.distributed.weight_transfer.base.WeightTransferEngine "            WeightTransferEngine") and registering them with the factory. See the [Base Class](https://docs.vllm.ai/en/latest/training/weight_transfer/base/) page for details.