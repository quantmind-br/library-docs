---
title: Speculative Decoding - vLLM
url: https://docs.vllm.ai/en/latest/examples/features/speculative_decoding/
source: sitemap
fetched_at: 2026-05-07T21:13:01.801777549-03:00
rendered_js: false
word_count: 0
summary: This document provides various code examples for using vLLM, including extracting hidden states from models, performing speculative decoding, and benchmarking multimodal model inference.
tags:
    - vllm
    - speculative-decoding
    - hidden-states
    - inference-optimization
    - multimodal-models
    - benchmarking
category: tutorial
---

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
importtempfile

fromsafetensorsimport safe_open

fromvllmimport LLM, SamplingParams

# Example: Using the custom "extract_hidden_states" speculator method and
# ExampleHiddenStatesConnector to extract and save hidden states from vllm

with tempfile.TemporaryDirectory() as tmpdirname:
    llm = LLM(
        model="Qwen/Qwen3-8B",  # Your target model
        speculative_config={
            "method": "extract_hidden_states",
            "num_speculative_tokens": 1,
            "draft_model_config": {
                "hf_config": {
                    "eagle_aux_hidden_state_layer_ids": [  # Target model layer indices
                        1,
                        2,
                        3,
                        4,
                    ],
                }
            },
        },
        kv_transfer_config={
            "kv_connector": "ExampleHiddenStatesConnector",
            "kv_role": "kv_producer",
            "kv_connector_extra_config": {
                "shared_storage_path": tmpdirname,
            },
        },
    )

    prompts = ["Generate a sentence with hidden states", "Write a python function"]
    sampling_params = SamplingParams(max_tokens=1)
    outputs = llm.generate(prompts, sampling_params)

    for output in outputs:
        print("\nPrompt:", output.prompt)
        print("Prompt token ids:", output.prompt_token_ids)

        hidden_states_path = output.kv_transfer_params.get("hidden_states_path")
        assert hidden_states_path is not None
        print("Prompt hidden states path:", hidden_states_path)

        with safe_open(hidden_states_path, "pt") as f:
            token_ids = f.get_tensor("token_ids")
            hidden_states = f.get_tensor("hidden_states")

            print("Extracted token ids:", token_ids)  # Matches prompt token ids
            print(
                "Extracted hidden states shape:", hidden_states.shape
            )  # [prompt len, num_hidden_layers, hidden size]
            print("Extracted hidden states:", hidden_states)

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
This file demonstrates the usage of text generation with an LLM model,
comparing the performance with and without speculative decoding.

Note that this example is out of date and not supported in vLLM v1.
"""

importgc
importtime

fromvllmimport LLM, SamplingParams


deftime_generation(
    llm: LLM, prompts: list[str], sampling_params: SamplingParams, title: str
):
    # Generate texts from the prompts. The output is a list of RequestOutput
    # objects that contain the prompt, generated text, and other information.
    # Warmup first
    llm.generate(prompts, sampling_params)
    llm.generate(prompts, sampling_params)
    start = time.time()
    outputs = llm.generate(prompts, sampling_params)
    end = time.time()
    print("-" * 50)
    print(title)
    print("time: ", (end - start) / sum(len(o.outputs[0].token_ids) for o in outputs))
    # Print the outputs.
    for output in outputs:
        generated_text = output.outputs[0].text
        print(f"text: {generated_text!r}")
        print("-" * 50)


defmain():
    template = (
        "Below is an instruction that describes a task. Write a response "
        "that appropriately completes the request.\n\n### Instruction:\n{}"
        "\n\n### Response:\n"
    )

    # Sample prompts.
    prompts = [
        "Write about the president of the United States.",
    ]
    prompts = [template.format(prompt) for prompt in prompts]
    # Create a sampling params object.
    sampling_params = SamplingParams(temperature=0.0, max_tokens=200)

    # Create an LLM without spec decoding
    llm = LLM(model="meta-llama/Llama-2-13b-chat-hf")

    time_generation(llm, prompts, sampling_params, "Without speculation")

    del llm
    gc.collect()

    # Create an LLM with spec decoding
    llm = LLM(
        model="meta-llama/Llama-2-13b-chat-hf",
        speculative_config={
            "model": "ibm-ai-platform/llama-13b-accelerator",
        },
    )

    time_generation(llm, prompts, sampling_params, "With speculation")


if __name__ == "__main__":
    main()

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

fromtransformersimport AutoTokenizer

fromvllmimport LLM, SamplingParams
fromvllm.benchmarks.datasetsimport add_dataset_parser, get_samples
fromvllm.utils.argparse_utilsimport FlexibleArgumentParser
fromvllm.v1.metrics.readerimport Counter, Vector

QUESTION = "What is the content of each image?"
IMAGE_URLS = [
    "https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/duck.jpg",
    "https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/lion.jpg",
    "https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/flycatcher.jpeg",
    "https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/somefish.jpg",
    "https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/starfish.jpg",
    "https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/snail.jpg",
    "https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/thistle.jpg",
    "https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/husky.jpg",
    "https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/orangetabbycat.jpg",
    "https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/guineapig.jpg",
    "https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/rabbit.jpg",
    "https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/horsepony.jpg",
]


defget_custom_mm_prompts(num_prompts):
    prompts = []
    for url in IMAGE_URLS:
        prompts.append(
            [
                {"type": "image_url", "image_url": {"url": url}},
                {"type": "text", "text": QUESTION},
            ]
        )
    if num_prompts > len(IMAGE_URLS):
        prompts = prompts * (num_prompts // len(IMAGE_URLS) + 1)

    return [[{"role": "user", "content": prompt}] for prompt in prompts[:num_prompts]]


defparse_args():
    parser = FlexibleArgumentParser()
    add_dataset_parser(parser)
    parser.add_argument("--test", action="store_true")
    parser.add_argument(
        "--method",
        type=str,
        default="eagle",
        choices=["ngram", "eagle", "eagle3", "mtp", "draft_model"],
    )
    parser.add_argument("--backend", type=str, default="openai")
    parser.add_argument("--num-spec-tokens", type=int, default=2)
    parser.add_argument("--prompt-lookup-max", type=int, default=5)
    parser.add_argument("--prompt-lookup-min", type=int, default=2)
    parser.add_argument("--tp", type=int, default=1)
    parser.add_argument("--enforce-eager", action="store_true")
    parser.add_argument("--enable-chunked-prefill", action="store_true")
    parser.add_argument("--max-model-len", type=int, default=16384)
    parser.add_argument("--temp", type=float, default=0)
    parser.add_argument("--top-p", type=float, default=1.0)
    parser.add_argument("--top-k", type=int, default=-1)
    parser.add_argument("--print-output", action="store_true")
    parser.add_argument("--output-len", type=int, default=256)
    parser.add_argument("--model-dir", type=str, default=None)
    parser.add_argument("--eagle-dir", type=str, default=None)
    parser.add_argument("--draft-model", type=str, default=None)
    parser.add_argument("--custom-mm-prompts", action="store_true")
    parser.add_argument("--gpu-memory-utilization", type=float, default=0.9)
    parser.add_argument("--disable-padded-drafter-batch", action="store_true")
    parser.add_argument("--max-num-seqs", type=int, default=None)
    parser.add_argument("--parallel-drafting", action="store_true")
    parser.add_argument("--allowed-local-media-path", type=str, default="")
    return parser.parse_args()


defmain(args):
    model_dir = args.model_dir
    if args.model_dir is None:
        if args.custom_mm_prompts:
            raise ValueError(
                "custom_mm_prompts requires mm based models"
                "default llama3.1-8b-instruct is not mm based"
                "please specify model_dir to give a mm based model"
            )
        model_dir = "meta-llama/Llama-3.1-8B-Instruct"
    tokenizer = AutoTokenizer.from_pretrained(model_dir)

    if args.custom_mm_prompts:
        prompts = llm_prompts = get_custom_mm_prompts(args.num_prompts)
    else:
        prompts = get_samples(args, tokenizer)
        if args.enable_multimodal_chat:
            llm_prompts = [p.prompt for p in prompts]
        else:
            # add_special_tokens is False to avoid adding bos twice
            # when using chat templates
            llm_prompts = [
                {
                    "prompt_token_ids": tokenizer.encode(
                        prompt.prompt, add_special_tokens=False
                    ),
                    "multi_modal_data": prompt.multi_modal_data,
                }
                for prompt in prompts
            ]
    if args.method == "eagle" or args.method == "eagle3":
        eagle_dir = args.eagle_dir
        if args.method == "eagle" and eagle_dir is None:
            eagle_dir = "yuhuili/EAGLE-LLaMA3.1-Instruct-8B"

        elif args.method == "eagle3" and eagle_dir is None:
            eagle_dir = "yuhuili/EAGLE3-LLaMA3.1-Instruct-8B"
        speculative_config = {
            "method": args.method,
            "model": eagle_dir,
            "num_speculative_tokens": args.num_spec_tokens,
            "disable_padded_drafter_batch": args.disable_padded_drafter_batch,
            "parallel_drafting": args.parallel_drafting,
        }
    elif args.method == "ngram":
        speculative_config = {
            "method": "ngram",
            "num_speculative_tokens": args.num_spec_tokens,
            "prompt_lookup_max": args.prompt_lookup_max,
            "prompt_lookup_min": args.prompt_lookup_min,
        }
    elif args.method == "draft_model":
        assert args.draft_model is not None and args.draft_model != ""
        speculative_config = {
            "method": args.method,
            "model": args.draft_model,
            "num_speculative_tokens": args.num_spec_tokens,
            "enforce_eager": args.enforce_eager,
            "max_model_len": args.max_model_len,
            "parallel_drafting": args.parallel_drafting,
        }
    elif args.method == "mtp":
        speculative_config = {
            "method": "mtp",
            "num_speculative_tokens": args.num_spec_tokens,
        }
    else:
        raise ValueError(f"unknown method: {args.method}")

    llm = LLM(
        model=model_dir,
        trust_remote_code=True,
        tensor_parallel_size=args.tp,
        enable_chunked_prefill=args.enable_chunked_prefill,
        enforce_eager=args.enforce_eager,
        gpu_memory_utilization=args.gpu_memory_utilization,
        speculative_config=speculative_config,
        disable_log_stats=False,
        max_model_len=args.max_model_len,
        limit_mm_per_prompt={"image": 5},
        disable_chunked_mm_input=True,
        max_num_seqs=args.max_num_seqs,
        allowed_local_media_path=args.allowed_local_media_path,
    )

    sampling_params = SamplingParams(temperature=args.temp, max_tokens=args.output_len)
    if args.backend == "openai-chat":
        outputs = llm.chat(llm_prompts, sampling_params=sampling_params)
    else:
        outputs = llm.generate(
            llm_prompts,
            sampling_params=sampling_params,
        )

    # print the generated text
    if args.print_output:
        for i, output in enumerate(outputs):
            print("-" * 50)
            if not args.custom_mm_prompts:
                print(f"prompt: {prompts[i].prompt}")
            else:
                print(f"prompt: {prompts[i]}")
            print(f"generated text: {output.outputs[0].text}")
            print("-" * 50)

    metrics = llm.get_metrics()

    total_num_output_tokens = sum(
        len(output.outputs[0].token_ids) for output in outputs
    )
    num_drafts = 0
    num_draft_tokens = 0
    num_accepted_tokens = 0
    acceptance_counts = [0] * args.num_spec_tokens
    for metric in metrics:
        if metric.name == "vllm:spec_decode_num_drafts":
            assert isinstance(metric, Counter)
            num_drafts += metric.value
        elif metric.name == "vllm:spec_decode_num_draft_tokens":
            assert isinstance(metric, Counter)
            num_draft_tokens += metric.value
        elif metric.name == "vllm:spec_decode_num_accepted_tokens":
            assert isinstance(metric, Counter)
            num_accepted_tokens += metric.value
        elif metric.name == "vllm:spec_decode_num_accepted_tokens_per_pos":
            assert isinstance(metric, Vector)
            for pos in range(len(metric.values)):
                acceptance_counts[pos] += metric.values[pos]

    print("-" * 50)
    print(f"total_num_output_tokens: {total_num_output_tokens}")
    print(f"num_drafts: {num_drafts}")
    print(f"num_draft_tokens: {num_draft_tokens}")
    print(f"num_accepted_tokens: {num_accepted_tokens}")
    acceptance_length = 1 + (num_accepted_tokens / num_drafts) if num_drafts > 0 else 1
    print(f"mean acceptance length: {acceptance_length:.2f}")
    print("-" * 50)

    # print acceptance at each token position
    for i in range(len(acceptance_counts)):
        acceptance_rate = acceptance_counts[i] / num_drafts if num_drafts > 0 else 0
        print(f"acceptance at token {i}: {acceptance_rate:.2f}")

    return acceptance_length


if __name__ == "__main__":
    args = parse_args()
    args.enable_multimodal_chat = args.backend == "openai-chat"

    acceptance_length = main(args)

    if args.test:
        # takes ~30s to run on 1xH100
        assert args.method in ["eagle", "eagle3"]
        assert args.tp == 1
        assert args.num_spec_tokens == 3
        assert args.dataset_name == "hf"
        assert args.dataset_path == "philschmid/mt-bench"
        assert args.num_prompts == 80
        assert args.temp == 0
        assert args.top_p == 1.0
        assert args.top_k == -1
        assert args.enable_chunked_prefill

        # check acceptance length is within 2% of expected value
        rtol = 0.02
        expected_acceptance_length = 2.296 if args.method == "eagle" else 2.811

        assert (
            acceptance_length <= (1 + rtol) * expected_acceptance_length
            and acceptance_length >= (1 - rtol) * expected_acceptance_length
        ), (
            f"acceptance_length {acceptance_length} is not "
            f"within {rtol*100}% of {expected_acceptance_length}"
        )

        print(
            f"Test passed! Expected AL: "
            f"{expected_acceptance_length}, got {acceptance_length}"
        )
```