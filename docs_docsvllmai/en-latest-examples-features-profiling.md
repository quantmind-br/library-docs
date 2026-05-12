---
title: Profiling - vLLM
url: https://docs.vllm.ai/en/latest/examples/features/profiling/
source: sitemap
fetched_at: 2026-05-07T21:12:56.743027563-03:00
rendered_js: false
word_count: 13
summary: This document provides code examples demonstrating how to use the vLLM built-in profiler to analyze performance during prefill and decode phases of model execution.
tags:
    - vllm
    - profiling
    - performance-optimization
    - torch-profiler
    - model-inference
    - debugging
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/features/profiling.md "Edit this page")

Source [https://github.com/vllm-project/vllm/tree/main/examples/features/profiling](https://github.com/vllm-project/vllm/tree/main/examples/features/profiling).

## Run One Batch Offline[¶](#run-one-batch-offline "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

from__future__import annotations

fromvllmimport LLM, EngineArgs
fromvllm.configimport ProfilerConfig
fromvllm.utils.argparse_utilsimport FlexibleArgumentParser

DEFAULT_MAX_TOKENS = 16


defcreate_parser() -> FlexibleArgumentParser:
    parser = FlexibleArgumentParser()
    EngineArgs.add_cli_args(parser)
    parser.set_defaults(model="meta-llama/Llama-3.2-1B-Instruct")

    batch_group = parser.add_argument_group("Batch parameters")
    batch_group.add_argument("--batch-size", type=int, default=1)
    batch_group.add_argument("--prompt-size", type=int, default=128)
    batch_group.add_argument("--prompt-prefix", type=str, default="Hello, my name is")

    profile_group = parser.add_argument_group("Profiling parameters")
    profile_group.add_argument(
        "--profile",
        choices=["none", "prefill", "decode", "both"],
        default="none",
    )
    profile_group.add_argument(
        "--profile-dir",
        type=str,
        default="",
        help="Required when --profile is not 'none'.",
    )

    return parser


def_build_prompt(prefix: str, prompt_size: int) -> str:
    if prompt_size <= 0:
        return ""
    if not prefix:
        prefix = " "
    if len(prefix) >= prompt_size:
        return prefix[:prompt_size]
    repeat_count = (prompt_size + len(prefix) - 1) // len(prefix)
    return (prefix * repeat_count)[:prompt_size]


def_build_profiler_config(
    profile: str, profile_dir: str, max_tokens: int
) -> ProfilerConfig | None:
    if profile == "none":
        return None
    if not profile_dir:
        raise ValueError("--profile-dir must be set when profiling is enabled.")
    if profile == "prefill":
        delay_iterations = 0
        max_iterations = 1
    elif profile == "decode":
        delay_iterations = 1
        max_iterations = max(1, max_tokens)
    else:
        delay_iterations = 0
        max_iterations = 0

    return ProfilerConfig(
        profiler="torch",
        torch_profiler_dir=profile_dir,
        delay_iterations=delay_iterations,
        max_iterations=max_iterations,
    )


defmain(args: dict) -> None:
    max_tokens = DEFAULT_MAX_TOKENS
    batch_size = args.pop("batch_size")
    prompt_size = args.pop("prompt_size")
    prompt_prefix = args.pop("prompt_prefix")
    profile = args.pop("profile")
    profile_dir = args.pop("profile_dir")

    profiler_config = _build_profiler_config(profile, profile_dir, max_tokens)
    if profiler_config is not None:
        args["profiler_config"] = profiler_config

    llm = LLM(**args)

    sampling_params = llm.get_default_sampling_params()
    sampling_params.max_tokens = max_tokens
    sampling_params.min_tokens = max_tokens
    sampling_params.ignore_eos = True

    prompt = _build_prompt(prompt_prefix, prompt_size)
    prompts = [prompt] * batch_size

    if profile != "none":
        llm.start_profile()
    outputs = llm.generate(prompts, sampling_params)
    if profile != "none":
        llm.stop_profile()

    print("-" * 50)
    for output in outputs:
        generated_text = output.outputs[0].text
        print(f"Prompt: {output.prompt!r}\nGenerated text: {generated_text!r}")
        print("-" * 50)


if __name__ == "__main__":
    parser = create_parser()
    main(vars(parser.parse_args()))
```

## Simple Profiling Offline[¶](#simple-profiling-offline "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

importtime

fromvllmimport LLM, SamplingParams

# Sample prompts.
prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]
# Create a sampling params object.
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)


defmain():
    # Create an LLM.
    llm = LLM(
        model="facebook/opt-125m",
        tensor_parallel_size=1,
        profiler_config={
            "profiler": "torch",
            "torch_profiler_dir": "./vllm_profile",
        },
    )

    llm.start_profile()

    # Generate texts from the prompts. The output is a list of RequestOutput
    # objects that contain the prompt, generated text, and other information.
    outputs = llm.generate(prompts, sampling_params)

    llm.stop_profile()

    # Print the outputs.
    print("-" * 50)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}\nGenerated text: {generated_text!r}")
        print("-" * 50)

    # Add a buffer to wait for profiler in the background process
    # (in case MP is on) to finish writing profiling output.
    time.sleep(10)


if __name__ == "__main__":
    main()
```