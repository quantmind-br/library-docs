---
title: Sharded State - vLLM
url: https://docs.vllm.ai/en/latest/examples/features/sharded_state/
source: sitemap
fetched_at: 2026-05-07T21:13:00.866256914-03:00
rendered_js: false
word_count: 14
summary: This document provides scripts and guidance for saving and loading vLLM model checkpoints using a sharded state format to optimize performance for large tensor-parallel models.
tags:
    - vllm
    - model-checkpointing
    - tensor-parallelism
    - sharded-state
    - offline-loading
    - model-loading
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/features/sharded_state.md "Edit this page")

Source [https://github.com/vllm-project/vllm/tree/main/examples/features/sharded\_state](https://github.com/vllm-project/vllm/tree/main/examples/features/sharded_state).

## Load Sharded State Offline[¶](#load-sharded-state-offline "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
Validates the loading of a model saved with the sharded_state format.
This script demonstrates how to load a model that was previously saved
using save_sharded_state_offline.py and validates it by running inference.
Example usage:
(First need to save a sharded_state mode)

python save_sharded_state_offline.py \
    --model /path/to/load \
    --tensor-parallel-size 8 \
    --output /path/to/save/sharded/model

python load_sharded_state_offline.py \
    --model /path/to/saved/sharded/model \
    --load-format sharded_state \
    --tensor-parallel-size 8 \
    --prompt "Hello, my name is" \
    --max-tokens 50
"""

fromvllmimport LLM, EngineArgs, SamplingParams
fromvllm.utils.argparse_utilsimport FlexibleArgumentParser


defparse_args():
    parser = FlexibleArgumentParser()
    # Add engine arguments
    EngineArgs.add_cli_args(parser)

    # Override default load_format for clarity
    parser.set_defaults(load_format="sharded_state")

    # Add validation arguments
    parser.add_argument(
        "--prompt", type=str, default="Hello, world!", help="Prompt for validation"
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=100,
        help="Maximum number of tokens to generate",
    )
    parser.add_argument(
        "--temperature", type=float, default=0.7, help="Sampling temperature"
    )
    parser.add_argument(
        "--top-p", type=float, default=1.0, help="Top-p sampling parameter"
    )

    return parser.parse_args()


defmain():
    args = parse_args()
    engine_args = EngineArgs.from_cli_args(args)

    print(
        f"Loading model from {engine_args.model} using format {engine_args.load_format}"
    )
    print(f"Tensor parallel size: {engine_args.tensor_parallel_size}")

    # Load the model using engine args
    llm = LLM.from_engine_args(engine_args)

    # Prepare sampling parameters
    sampling_params = SamplingParams(
        temperature=args.temperature,
        top_p=args.top_p,
        max_tokens=args.max_tokens,
    )

    print("\nRunning inference:")
    print(f"Prompt: {args.prompt}")

    # Generate completion
    outputs = llm.generate(args.prompt, sampling_params)

    # Display generated text
    print("\nGenerated outputs:")
    for output in outputs:
        generated_text = output.outputs[0].text
        print("-" * 50)
        print(f"Full output: {args.prompt}{generated_text}")
        print("-" * 50)


if __name__ == "__main__":
    main()
```

## Save Sharded State Offline[¶](#save-sharded-state-offline "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
Saves each worker's model state dict directly to a checkpoint, which enables a
fast load path for large tensor-parallel models where each worker only needs to
read its own shard rather than the entire checkpoint.

Example usage:

python save_sharded_state_offline.py \
    --model /path/to/load \
    --tensor-parallel-size 8 \
    --output /path/to/save

Then, the model can be loaded with

llm = LLM(
    model="/path/to/save",
    load_format="sharded_state",
    tensor_parallel_size=8,
)
"""

importos
importshutil
frompathlibimport Path

fromvllmimport LLM, EngineArgs
fromvllm.model_executor.model_loaderimport ShardedStateLoader
fromvllm.utils.argparse_utilsimport FlexibleArgumentParser


defparse_args():
    parser = FlexibleArgumentParser()
    EngineArgs.add_cli_args(parser)
    parser.add_argument(
        "--output", "-o", required=True, type=str, help="path to output checkpoint"
    )
    parser.add_argument(
        "--file-pattern",
        type=str,
        default=ShardedStateLoader.DEFAULT_PATTERN,
        help="string pattern of saved filenames",
    )
    parser.add_argument(
        "--max-file-size",
        type=int,
        default=5 * 1024**3,
        help="max size (in bytes) of each safetensors file",
    )
    return parser.parse_args()


defmain(args):
    engine_args = EngineArgs.from_cli_args(args)
    if engine_args.enable_lora:
        raise ValueError("Saving with enable_lora=True is not supported!")
    model_path = engine_args.model
    if not Path(model_path).is_dir():
        raise ValueError("model path must be a local directory")
    # Create LLM instance from arguments
    llm = LLM.from_engine_args(engine_args)
    # Prepare output directory
    Path(args.output).mkdir(exist_ok=True)
    # Dump worker states to output directory

    llm.llm_engine.engine_core.save_sharded_state(
        path=args.output, pattern=args.file_pattern, max_size=args.max_file_size
    )

    # Copy metadata files to output directory
    for file in os.listdir(model_path):
        if os.path.splitext(file)[1] not in (".bin", ".pt", ".safetensors"):
            if os.path.isdir(os.path.join(model_path, file)):
                shutil.copytree(
                    os.path.join(model_path, file), os.path.join(args.output, file)
                )
            else:
                shutil.copy(os.path.join(model_path, file), args.output)


if __name__ == "__main__":
    args = parse_args()
    main(args)
```