---
title: RLHF IPC - vLLM
url: https://docs.vllm.ai/en/latest/examples/rl/rlhf_ipc/
source: sitemap
fetched_at: 2026-05-07T21:13:46.926019279-03:00
rendered_js: false
word_count: 0
summary: This document demonstrates how to implement reinforcement learning from human feedback (RLHF) by synchronizing model weights between a training process and a vLLM inference engine using CUDA IPC handles within a Ray cluster.
tags:
    - vllm
    - ray
    - rlhf
    - ipc-weight-transfer
    - distributed-inference
    - model-training
    - gpu-colocation
category: tutorial
---

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
Demonstrates reinforcement learning from human feedback (RLHF) using vLLM and Ray,
with IPC-based weight syncing APIs

The script colocates the training and inference workloads onto the same GPU using Ray.

The example performs the following steps:

* Request a placement group of 1 GPU.
* Place the inference model on the above GPU using the placement group.
* Place and load the training model on the same GPU using the placement group.
* Generate text from a list of prompts using the inference engine.
* Update the weights of the training model and broadcast the updated weights
  to the inference engine by using CUDA IPC handles. Note that
  for demonstration purposes we simply zero out the weights.

This example assumes a single-node cluster with a single GPU,
but can be extended to multiple GPUs.
"""

importos

importray
fromray.util.placement_groupimport placement_group
fromray.util.scheduling_strategiesimport PlacementGroupSchedulingStrategy
fromtransformersimport AutoModelForCausalLM

fromvllmimport LLM, SamplingParams
fromvllm.configimport WeightTransferConfig
fromvllm.distributed.weight_transfer.ipc_engineimport (
    IPCTrainerSendWeightsArgs,
    IPCWeightTransferEngine,
)


classMyLLM(LLM):
"""Configure the vLLM worker for Ray placement group execution."""

    def__init__(self, *args, **kwargs):
        # Remove the top-level CUDA_VISIBLE_DEVICES variable set by Ray
        # so that vLLM can manage its own device placement within the worker.
        os.environ.pop("CUDA_VISIBLE_DEVICES", None)
        # Each worker uses 0.4 GPU so that two instances fit on the same GPU.
        os.environ["VLLM_RAY_PER_WORKER_GPUS"] = "0.4"
        os.environ["VLLM_RAY_BUNDLE_INDICES"] = "0"
        # needed for ipc handle serialization
        os.environ["VLLM_ALLOW_INSECURE_SERIALIZATION"] = "1"
        super().__init__(*args, **kwargs)


# Load the OPT-125M model onto GPU 0 for the training workload.

MODEL_NAME = "facebook/opt-125m"


@ray.remote
classTrainModel:
    def__init__(self, llm_handle: ray.actor.ActorHandle):
        self.train_model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
        )
        self.train_model.to("cuda:0")
        self.llm_handle = llm_handle

    definit_weight_transfer(self):
        # IPC backend doesn't need initialization info
        ray.get(
            self.llm_handle.init_weight_transfer_engine.remote(dict(init_info=dict()))
        )

    defbroadcast_weights(self, llm_handle: ray.actor.ActorHandle):
"""Broadcast weights to the inference engine using IPC."""
        self.llm_handle = llm_handle
        trainer_args = IPCTrainerSendWeightsArgs(mode="ray", llm_handle=llm_handle)
        IPCWeightTransferEngine.trainer_send_weights(
            iterator=self.train_model.named_parameters(),
            trainer_args=trainer_args,
        )


ray.init()

pg_colocate = placement_group([{"GPU": 1, "CPU": 0}])
ray.get(pg_colocate.ready())


llm = ray.remote(
    num_cpus=0,
    num_gpus=0,
    scheduling_strategy=PlacementGroupSchedulingStrategy(
        placement_group=pg_colocate,
        placement_group_capture_child_tasks=True,
    ),
)(MyLLM).remote(
    model=MODEL_NAME,
    enforce_eager=True,
    tensor_parallel_size=1,
    distributed_executor_backend="ray",
    gpu_memory_utilization=0.7,
    weight_transfer_config=WeightTransferConfig(backend="ipc"),
    load_format="dummy",
)

train_model = TrainModel.options(
    num_gpus=0.1,
    num_cpus=0,
    scheduling_strategy=PlacementGroupSchedulingStrategy(
        placement_group=pg_colocate, placement_group_capture_child_tasks=True
    ),
).remote(llm)


# Generate text from the prompts.
prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]

sampling_params = SamplingParams(temperature=0)

outputs = ray.get(llm.generate.remote(prompts, sampling_params))

print("-" * 50)
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}\nGenerated text: {generated_text!r}")
    print("-" * 50)

ray.get(llm.sleep.remote(level=0))

ray.get(train_model.init_weight_transfer.remote())
# Synchronize the updated weights to the inference engine using batched API.
ray.get(train_model.broadcast_weights.remote(llm))

ray.get(llm.wake_up.remote(tags=["scheduling"]))

# Generate text with the updated model.
outputs_updated = ray.get(llm.generate.remote(prompts, sampling_params))
print("-" * 50)
for output in outputs_updated:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}\nGenerated text: {generated_text!r}")
    print("-" * 50)
```