---
title: Torchrun - vLLM
url: https://docs.vllm.ai/en/latest/examples/features/torchrun/
source: sitemap
fetched_at: 2026-05-07T21:13:03.795698252-03:00
rendered_js: false
word_count: 357
summary: This document provides examples and best practices for integrating vLLM with torchrun to achieve data-parallel and tensor-parallel inference using the external_launcher backend.
tags:
    - vllm
    - torchrun
    - distributed-inference
    - data-parallelism
    - tensor-parallelism
    - external-launcher
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/features/torchrun.md "Edit this page")

Source [https://github.com/vllm-project/vllm/tree/main/examples/features/torchrun](https://github.com/vllm-project/vllm/tree/main/examples/features/torchrun).

## Torchrun Dp Example Offline[¶](#torchrun-dp-example-offline "Permanent link")

````
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
experimental support for data-parallel inference with torchrun
Note the data load balancing and distribution is done out of the vllm engine,
no internal lb supported in external_launcher mode.

To run this example:
```bash
$ torchrun --nproc-per-node=2 examples/features/torchrun/torchrun_dp_example_offline.py
```

With custom parallelism settings:
```bash
$ torchrun --nproc-per-node=8 examples/features/torchrun/torchrun_dp_example_offline.py \
    --tp-size=2 --pp-size=1 --dp-size=4 --enable-ep
```
"""  # noqa: E501

importargparse

fromvllmimport LLM, SamplingParams


defparse_args():
    parser = argparse.ArgumentParser(
        description="Data-parallel inference with torchrun"
    )
    parser.add_argument(
        "--tp-size",
        type=int,
        default=1,
        help="Tensor parallel size (default: 1)",
    )
    parser.add_argument(
        "--pp-size",
        type=int,
        default=1,
        help="Pipeline parallel size (default: 1)",
    )
    parser.add_argument(
        "--dp-size",
        type=int,
        default=2,
        help="Data parallel size (default: 2)",
    )
    parser.add_argument(
        "--enable-ep",
        action="store_true",
        help="Enable expert parallel (default: False)",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="microsoft/Phi-mini-MoE-instruct",
        help="Model name or path (default: microsoft/Phi-mini-MoE-instruct)",
    )
    parser.add_argument(
        "--max-model-len",
        type=int,
        default=4096,
        help="Maximum model length (default: 4096)",
    )
    parser.add_argument(
        "--gpu-memory-utilization",
        type=float,
        default=0.6,
        help="GPU memory utilization (default: 0.6)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=1,
        help="Random seed (default: 1)",
    )
    return parser.parse_args()


args = parse_args()


# Create prompts, the same across all ranks
prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]

# Create sampling parameters, the same across all ranks
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

# Use `distributed_executor_backend="external_launcher"` so that
# this llm engine/instance only creates one worker.
# it is important to set an explicit seed to make sure that
# all ranks have the same random seed, so that sampling can be
# deterministic across ranks.
llm = LLM(
    model=args.model,
    tensor_parallel_size=args.tp_size,
    data_parallel_size=args.dp_size,
    pipeline_parallel_size=args.pp_size,
    enable_expert_parallel=args.enable_ep,
    distributed_executor_backend="external_launcher",
    max_model_len=args.max_model_len,
    gpu_memory_utilization=args.gpu_memory_utilization,
    seed=args.seed,
)

dp_rank = llm.llm_engine.vllm_config.parallel_config.data_parallel_rank
dp_size = llm.llm_engine.vllm_config.parallel_config.data_parallel_size

prompts = [
    f"{idx}.{prompt}" for idx, prompt in enumerate(prompts) if idx % dp_size == dp_rank
]

outputs = llm.generate(prompts, sampling_params)

for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(
        f"DP Rank: {dp_rank} Prompt: {prompt!r}\nGenerated text: {generated_text!r}\n"
    )

"""
Further tips:

1. to communicate control messages across all ranks, use the cpu group,
a PyTorch ProcessGroup with GLOO backend.

```python
from vllm.distributed.parallel_state import get_world_group
cpu_group = get_world_group().cpu_group
torch_rank = dist.get_rank(group=cpu_group)
if torch_rank == 0:
    # do something for rank 0, e.g. saving the results to disk.
```

2. to communicate data across all ranks, use the model's device group,
a PyTorch ProcessGroup with NCCL backend.
```python
from vllm.distributed.parallel_state import get_world_group
device_group = get_world_group().device_group
```

3. to access the model directly in every rank, use the following code:
```python
llm.llm_engine.model_executor.driver_worker.worker.model_runner.model
```
"""
````

## Torchrun Example Offline[¶](#torchrun-example-offline "Permanent link")

````
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
experimental support for tensor-parallel inference with torchrun,
see https://github.com/vllm-project/vllm/issues/11400 for
the motivation and use case for this example.
run the script with `torchrun --nproc-per-node=4 torchrun_example_offline.py`,
the argument `4` should match the product of `tensor_parallel_size` and
`pipeline_parallel_size` below. see `tests/distributed/test_torchrun_example.py`
for the unit test.
"""

importtorch.distributedasdist

fromvllmimport LLM, SamplingParams

# Create prompts, the same across all ranks
prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]

# Create sampling parameters, the same across all ranks
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

# Use `distributed_executor_backend="external_launcher"` so that
# this llm engine/instance only creates one worker.
# it is important to set an explicit seed to make sure that
# all ranks have the same random seed, so that sampling can be
# deterministic across ranks.
llm = LLM(
    model="meta-llama/Llama-3.1-8B",
    tensor_parallel_size=2,
    pipeline_parallel_size=2,
    distributed_executor_backend="external_launcher",
    max_model_len=32768,
    seed=1,
)

outputs = llm.generate(prompts, sampling_params)

# all ranks will have the same outputs
if dist.get_rank() == 0:
    print("-" * 50)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}\nGenerated text: {generated_text!r}\n")
        print("-" * 50)
"""
Further tips:

1. to communicate control messages across all ranks, use the cpu group,
a PyTorch ProcessGroup with GLOO backend.

```python
from vllm.distributed.parallel_state import get_world_group
cpu_group = get_world_group().cpu_group
torch_rank = dist.get_rank(group=cpu_group)
if torch_rank == 0:
    # do something for rank 0, e.g. saving the results to disk.
```

2. to communicate data across all ranks, use the model's device group,
a PyTorch ProcessGroup with NCCL backend.
```python
from vllm.distributed.parallel_state import get_world_group
device_group = get_world_group().device_group
```

3. to access the model directly in every rank, use the following code:
```python
llm.llm_engine.model_executor.driver_worker.worker.model_runner.model
```
"""
````