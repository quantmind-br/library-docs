---
title: Offline Inference - vLLM
url: https://docs.vllm.ai/en/latest/examples/basic/offline_inference/
source: sitemap
fetched_at: 2026-05-07T21:12:35.707543945-03:00
rendered_js: false
word_count: 334
summary: This document introduces the vLLM LLM class, which serves as the primary Python interface for performing offline model inference without requiring a dedicated server.
tags:
    - vllm
    - offline-inference
    - python-api
    - llm-deployment
    - model-quantization
    - cpu-offloading
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/basic/offline_inference.md "Edit this page")

Source [https://github.com/vllm-project/vllm/tree/main/examples/basic/offline\_inference](https://github.com/vllm-project/vllm/tree/main/examples/basic/offline_inference).

The [`LLM`](https://docs.vllm.ai/en/latest/api/vllm/entrypoints/llm/#vllm.entrypoints.llm.LLM "            LLM") class provides the primary Python interface for doing offline inference, which is interacting with a model without using a separate model inference server.

## Usage[¶](#usage "Permanent link")

The first script in this example shows the most basic usage of vLLM. If you are new to Python and vLLM, you should start here.

```
pythonexamples/basic/offline_inference/basic.py
```

The rest of the scripts include an [argument parser](https://docs.python.org/3/library/argparse.html), which you can use to pass any arguments that are compatible with [`LLM`](https://docs.vllm.ai/en/latest/api/offline_inference/llm.html). Try running the script with `--help` for a list of all available arguments.

```
pythonexamples/basic/offline_inference/classify.py

pythonexamples/basic/offline_inference/embed.py

pythonexamples/basic/offline_inference/score.py
```

The chat and generate scripts also accept the [sampling parameters](https://docs.vllm.ai/en/latest/api/inference_params.html#sampling-parameters): `max_tokens`, `temperature`, `top_p` and `top_k`.

```
pythonexamples/basic/offline_inference/chat.py

pythonexamples/basic/offline_inference/generate.py
```

## Features[¶](#features "Permanent link")

In the scripts that support passing arguments, you can experiment with the following features.

### Default generation config[¶](#default-generation-config "Permanent link")

The `--generation-config` argument specifies where the generation config will be loaded from when calling `LLM.get_default_sampling_params()`. If set to ‘auto’, the generation config will be loaded from model path. If set to a folder path, the generation config will be loaded from the specified folder path. If it is not provided, vLLM defaults will be used.

> If max\_new\_tokens is specified in generation config, then it sets a server-wide limit on the number of output tokens for all requests.

Try it yourself with the following argument:

### Quantization[¶](#quantization "Permanent link")

#### GGUF[¶](#gguf "Permanent link")

vLLM supports models that are quantized using GGUF.

Try one yourself using the `repo_id:quant_type` format to load directly from HuggingFace:

```
--modelunsloth/Qwen3-0.6B-GGUF:Q4_K_M--tokenizerQwen/Qwen3-0.6B
```

### CPU offload[¶](#cpu-offload "Permanent link")

The `--cpu-offload-gb` argument can be seen as a virtual way to increase the GPU memory size. For example, if you have one 24 GB GPU and set this to 10, virtually you can think of it as a 34 GB GPU. Then you can load a 13B model with BF16 weight, which requires at least 26GB GPU memory. Note that this requires fast CPU-GPU interconnect, as part of the model is loaded from CPU memory to GPU memory on the fly in each model forward pass.

Try it yourself with the following arguments:

```
--modelmeta-llama/Llama-2-13b-chat-hf--cpu-offload-gb10
```

## Example materials[¶](#example-materials "Permanent link")

basic.py

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

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
    llm = LLM(model="facebook/opt-125m")
    # Generate texts from the prompts.
    # The output is a list of RequestOutput objects
    # that contain the prompt, generated text, and other information.
    outputs = llm.generate(prompts, sampling_params)
    # Print the outputs.
    print("\nGenerated Outputs:\n" + "-" * 60)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt:    {prompt!r}")
        print(f"Output:    {generated_text!r}")
        print("-" * 60)


if __name__ == "__main__":
    main()
```

chat.py

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

fromvllmimport LLM, EngineArgs
fromvllm.outputsimport RequestOutput
fromvllm.utils.argparse_utilsimport FlexibleArgumentParser


defcreate_parser():
    parser = FlexibleArgumentParser()
    # Add engine args
    EngineArgs.add_cli_args(parser)
    parser.set_defaults(model="meta-llama/Llama-3.2-1B-Instruct")
    # Add sampling params
    sampling_group = parser.add_argument_group("Sampling parameters")
    sampling_group.add_argument("--max-tokens", type=int)
    sampling_group.add_argument("--temperature", type=float)
    sampling_group.add_argument("--top-p", type=float)
    sampling_group.add_argument("--top-k", type=int)
    # Add example params
    parser.add_argument("--chat-template-path", type=str)

    return parser


defmain(args: dict):
    # Pop arguments not used by LLM
    max_tokens = args.pop("max_tokens")
    temperature = args.pop("temperature")
    top_p = args.pop("top_p")
    top_k = args.pop("top_k")
    chat_template_path = args.pop("chat_template_path")

    # Create an LLM
    llm = LLM(**args)

    # Create sampling params object
    sampling_params = llm.get_default_sampling_params()
    if max_tokens is not None:
        sampling_params.max_tokens = max_tokens
    if temperature is not None:
        sampling_params.temperature = temperature
    if top_p is not None:
        sampling_params.top_p = top_p
    if top_k is not None:
        sampling_params.top_k = top_k

    defprint_outputs(outputs: list[RequestOutput], prompts: list):
        assert len(outputs) == len(prompts)
        print("\nGenerated Outputs:\n" + "-" * 80)
        for i, output in enumerate(outputs):
            generated_text = output.outputs[0].text
            print(f"Prompt: {prompts[i]!r}\n")
            print(f"Generated text: {generated_text!r}")
            print("-" * 80)

    print("=" * 80)

    # In this script, we demonstrate how to pass input to the chat method:
    conversation = [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hello! How can I assist you today?"},
        {
            "role": "user",
            "content": "Write an essay about the importance of higher education.",
        },
    ]
    outputs = llm.chat(conversation, sampling_params, use_tqdm=False)
    print_outputs(
        outputs,
        [
            conversation,
        ],
    )

    # You can run batch inference with llm.chat API
    conversations = [conversation for _ in range(10)]

    # We turn on tqdm progress bar to verify it's indeed running batch inference
    outputs = llm.chat(conversations, sampling_params, use_tqdm=True)
    print_outputs(outputs, conversations)

    # A chat template can be optionally supplied.
    # If not, the model will use its default chat template.
    if chat_template_path is not None:
        with open(chat_template_path) as f:
            chat_template = f.read()

        outputs = llm.chat(
            conversations,
            sampling_params,
            use_tqdm=False,
            chat_template=chat_template,
        )
        print_outputs(outputs, conversations)


if __name__ == "__main__":
    parser = create_parser()
    args: dict = vars(parser.parse_args())
    main(args)
```

classify.py

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

fromargparseimport Namespace

fromvllmimport LLM, EngineArgs
fromvllm.utils.argparse_utilsimport FlexibleArgumentParser


defparse_args():
    parser = FlexibleArgumentParser()
    parser = EngineArgs.add_cli_args(parser)
    # Set example specific arguments
    parser.set_defaults(
        model="jason9693/Qwen2.5-1.5B-apeach",
        runner="pooling",
        enforce_eager=True,
    )
    return parser.parse_args()


defmain(args: Namespace):
    # Sample prompts.
    prompts = [
        "Hello, my name is",
        "The president of the United States is",
        "The capital of France is",
        "The future of AI is",
    ]

    # Create an LLM.
    # You should pass runner="pooling" for classification models
    llm = LLM(**vars(args))

    # Generate logits. The output is a list of ClassificationRequestOutputs.
    outputs = llm.classify(prompts)

    # Print the outputs.
    print("\nGenerated Outputs:\n" + "-" * 60)
    for prompt, output in zip(prompts, outputs):
        probs = output.outputs.probs
        probs_trimmed = (str(probs[:16])[:-1] + ", ...]") if len(probs) > 16 else probs
        print(
            f"Prompt: {prompt!r}\n"
            f"Class Probabilities: {probs_trimmed} (size={len(probs)})"
        )
        print("-" * 60)


if __name__ == "__main__":
    args = parse_args()
    main(args)
```

embed.py

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

fromargparseimport Namespace

fromvllmimport LLM, EngineArgs
fromvllm.utils.argparse_utilsimport FlexibleArgumentParser
fromvllm.utils.print_utilsimport print_embeddings


defparse_args():
    parser = FlexibleArgumentParser()
    parser = EngineArgs.add_cli_args(parser)
    # Set example specific arguments
    parser.set_defaults(
        model="intfloat/e5-small",
        runner="pooling",
        enforce_eager=True,
    )
    return parser.parse_args()


defmain(args: Namespace):
    # Sample prompts.
    prompts = [
        "Hello, my name is",
        "The president of the United States is",
        "The capital of France is",
        "The future of AI is",
    ]

    # Create an LLM.
    # You should pass runner="pooling" for embedding models
    llm = LLM(**vars(args))

    # Generate embedding. The output is a list of EmbeddingRequestOutputs.
    outputs = llm.embed(prompts)

    # Print the outputs.
    print("\nGenerated Outputs:\n" + "-" * 60)
    for prompt, output in zip(prompts, outputs):
        embeds = output.outputs.embedding
        print(f"Prompt: {prompt!r}")
        print_embeddings(embeds)
        print("-" * 60)


if __name__ == "__main__":
    args = parse_args()
    main(args)
```

generate.py

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

fromvllmimport LLM, EngineArgs
fromvllm.utils.argparse_utilsimport FlexibleArgumentParser


defcreate_parser():
    parser = FlexibleArgumentParser()
    # Add engine args
    EngineArgs.add_cli_args(parser)
    parser.set_defaults(model="meta-llama/Llama-3.2-1B-Instruct")
    # Add sampling params
    sampling_group = parser.add_argument_group("Sampling parameters")
    sampling_group.add_argument("--max-tokens", type=int)
    sampling_group.add_argument("--temperature", type=float)
    sampling_group.add_argument("--top-p", type=float)
    sampling_group.add_argument("--top-k", type=int)

    return parser


defmain(args: dict):
    # Pop arguments not used by LLM
    max_tokens = args.pop("max_tokens")
    temperature = args.pop("temperature")
    top_p = args.pop("top_p")
    top_k = args.pop("top_k")

    # Create an LLM
    llm = LLM(**args)

    # Create a sampling params object
    sampling_params = llm.get_default_sampling_params()
    if max_tokens is not None:
        sampling_params.max_tokens = max_tokens
    if temperature is not None:
        sampling_params.temperature = temperature
    if top_p is not None:
        sampling_params.top_p = top_p
    if top_k is not None:
        sampling_params.top_k = top_k

    # Generate texts from the prompts. The output is a list of RequestOutput
    # objects that contain the prompt, generated text, and other information.
    prompts = [
        "Hello, my name is",
        "The president of the United States is",
        "The capital of France is",
        "The future of AI is",
    ]
    outputs = llm.generate(prompts, sampling_params)
    # Print the outputs.
    print("-" * 50)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}\nGenerated text: {generated_text!r}")
        print("-" * 50)


if __name__ == "__main__":
    parser = create_parser()
    args: dict = vars(parser.parse_args())
    main(args)
```

score.py

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

fromargparseimport Namespace

fromvllmimport LLM, EngineArgs
fromvllm.utils.argparse_utilsimport FlexibleArgumentParser


defparse_args():
    parser = FlexibleArgumentParser()
    parser = EngineArgs.add_cli_args(parser)
    # Set example specific arguments
    parser.set_defaults(
        model="BAAI/bge-reranker-v2-m3",
        runner="pooling",
        enforce_eager=True,
    )
    return parser.parse_args()


defmain(args: Namespace):
    # Sample prompts.
    query = "What is the capital of France?"
    documents = [
        "The capital of Brazil is Brasilia.",
        "The capital of France is Paris.",
    ]

    # Create an LLM.
    # You should pass runner="pooling" for cross-encoder models
    llm = LLM(**vars(args))

    # Generate scores. The output is a list of ScoringRequestOutputs.
    outputs = llm.score(query, documents)

    # Print the outputs.
    print("\nGenerated Outputs:\n" + "-" * 60)
    for document, output in zip(documents, outputs):
        score = output.outputs.score
        print(f"Pair: {[query,document]!r}\nScore: {score}")
        print("-" * 60)


if __name__ == "__main__":
    args = parse_args()
    main(args)
```