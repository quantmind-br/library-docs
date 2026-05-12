---
title: Quickstart - vLLM
url: https://docs.vllm.ai/en/latest/getting_started/quickstart/
source: sitemap
fetched_at: 2026-05-07T21:14:44.947803734-03:00
rendered_js: false
word_count: 1127
summary: This guide provides instructions for installing vLLM on various hardware platforms and performing offline batched inference for text generation models.
tags:
    - vllm
    - llm
    - inference
    - installation
    - python
    - gpu
    - batched-inference
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/getting_started/quickstart.md "Edit this page")

This guide will help you quickly get started with vLLM to perform:

- [Offline batched inference](#offline-batched-inference)
- [Online serving using OpenAI-compatible server](#openai-compatible-server)

## Prerequisites[¶](#prerequisites "Permanent link")

- OS: Linux
- Python: 3.10 -- 3.13

## Installation[¶](#installation "Permanent link")

NVIDIA CUDAAMD ROCmGoogle TPU

If you are using NVIDIA GPUs, you can install vLLM using [pip](https://pypi.org/project/vllm/) directly.

It's recommended to use [uv](https://docs.astral.sh/uv/), a very fast Python environment manager, to create and manage Python environments. Please follow the [documentation](https://docs.astral.sh/uv/#getting-started) to install `uv`. After installing `uv`, you can create a new Python environment and install vLLM using the following commands:

```
uvvenv--python3.12--seed
source.venv/bin/activate
uvpipinstallvllm--torch-backend=auto
```

`uv` can [automatically select the appropriate PyTorch index at runtime](https://docs.astral.sh/uv/guides/integration/pytorch/#automatic-backend-selection) by inspecting the installed CUDA driver version via `--torch-backend=auto` (or `UV_TORCH_BACKEND=auto`). To select a specific backend (e.g., `cu126`), set `--torch-backend=cu126` (or `UV_TORCH_BACKEND=cu126`).

Another delightful way is to use `uv run` with `--with [dependency]` option, which allows you to run commands such as `vllm serve` without creating any permanent environment:

```
uvrun--withvllmvllm--help
```

You can also use [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html) to create and manage Python environments. You can install `uv` to the conda environment through `pip` if you want to manage it within the environment.

```
condacreate-nmyenvpython=3.12-y
condaactivatemyenv
pipinstall--upgradeuv
uvpipinstallvllm--torch-backend=auto
```

If you are using AMD GPUs, you can install vLLM using `uv`.

It's recommended to use [uv](https://docs.astral.sh/uv/), as it gives the extra index [higher priority than the default index](https://docs.astral.sh/uv/pip/compatibility/#packages-that-exist-on-multiple-indexes). `uv` is also a very fast Python environment manager, to create and manage Python environments. Please follow the [documentation](https://docs.astral.sh/uv/#getting-started) to install `uv`. After installing `uv`, you can create a new Python environment and install vLLM using the following commands:

```
uvvenv--python3.12--seed
source.venv/bin/activate
uvpipinstallvllm--extra-index-urlhttps://wheels.vllm.ai/rocm/
```

Note

It currently supports Python 3.12, ROCm 7.0 and `glibc >= 2.35`.

Note

Note that, previously, docker images were published using AMD's docker release pipeline and were located `rocm/vllm-dev`. This is being deprecated by using vLLM's docker release pipeline.

To run vLLM on Google TPUs, you need to install the `vllm-tpu` package.

Note

For more detailed instructions, including Docker, installing from source, and troubleshooting, please refer to the [vLLM on TPU documentation](https://docs.vllm.ai/projects/tpu/en/latest/).

Note

For more detail and non-CUDA platforms, please refer to the [installation guide](https://docs.vllm.ai/en/latest/getting_started/installation/) for specific instructions on how to install vLLM.

## Offline Batched Inference[¶](#offline-batched-inference "Permanent link")

With vLLM installed, you can start generating texts for list of input prompts (i.e. offline batch inferencing). See the example script: [examples/basic/offline\_inference/basic.py](https://github.com/vllm-project/vllm/blob/main/examples/basic/offline_inference/basic.py)

The first line of this example imports the classes [LLM](https://docs.vllm.ai/en/latest/api/vllm/#vllm.LLM "            LLM") and [SamplingParams](https://docs.vllm.ai/en/latest/api/vllm/#vllm.SamplingParams "            SamplingParams"):

- [LLM](https://docs.vllm.ai/en/latest/api/vllm/#vllm.LLM "            LLM") is the main class for running offline inference with vLLM engine.
- [SamplingParams](https://docs.vllm.ai/en/latest/api/vllm/#vllm.SamplingParams "            SamplingParams") specifies the parameters for the sampling process.

```
fromvllmimport LLM, SamplingParams
```

The next section defines a list of input prompts and sampling parameters for text generation. The [sampling temperature](https://arxiv.org/html/2402.05201v1) is set to `0.8` and the [nucleus sampling probability](https://en.wikipedia.org/wiki/Top-p_sampling) is set to `0.95`. You can find more information about the sampling parameters [here](https://docs.vllm.ai/en/latest/api/#inference-parameters).

Important

By default, vLLM will use sampling parameters recommended by model creator by applying the `generation_config.json` from the Hugging Face model repository if it exists. In most cases, this will provide you with the best results by default if [SamplingParams](https://docs.vllm.ai/en/latest/api/vllm/#vllm.SamplingParams "            SamplingParams") is not specified.

However, if vLLM's default sampling parameters are preferred, please set `generation_config="vllm"` when creating the [LLM](https://docs.vllm.ai/en/latest/api/vllm/#vllm.LLM "            LLM") instance.

```
prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
```

The [LLM](https://docs.vllm.ai/en/latest/api/vllm/#vllm.LLM "            LLM") class initializes vLLM's engine and the [OPT-125M model](https://arxiv.org/abs/2205.01068) for offline inference. The list of supported models can be found [here](https://docs.vllm.ai/en/latest/models/supported_models/).

```
llm = LLM(model="facebook/opt-125m")
```

Note

By default, vLLM downloads models from [Hugging Face](https://huggingface.co/). If you would like to use models from [ModelScope](https://www.modelscope.cn), set the environment variable `VLLM_USE_MODELSCOPE` before initializing the engine.

```
exportVLLM_USE_MODELSCOPE=True
```

Now, the fun part! The outputs are generated using `llm.generate`. It adds the input prompts to the vLLM engine's waiting queue and executes the vLLM engine to generate the outputs with high throughput. The outputs are returned as a list of [`RequestOutput`](https://docs.vllm.ai/en/latest/api/vllm/outputs/#vllm.outputs.RequestOutput "            RequestOutput") objects, which include all of the output tokens.

```
outputs = llm.generate(prompts, sampling_params)

for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```

Note

The `llm.generate` method does not automatically apply the model's chat template to the input prompt. Therefore, if you are using an Instruct model or Chat model, you should manually apply the corresponding chat template to ensure the expected behavior. Alternatively, you can use the `llm.chat` method and pass a list of messages which have the same format as those passed to OpenAI's `client.chat.completions`:

Code

```
# Using tokenizer to apply chat template
fromtransformersimport AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("/path/to/chat_model")
messages_list = [
    [{"role": "user", "content": prompt}]
    for prompt in prompts
]
texts = tokenizer.apply_chat_template(
    messages_list,
    tokenize=False,
    add_generation_prompt=True,
)

# Generate outputs
outputs = llm.generate(texts, sampling_params)

# Print the outputs.
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")

# Using chat interface.
outputs = llm.chat(messages_list, sampling_params)
for idx, output in enumerate(outputs):
    prompt = prompts[idx]
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```

## OpenAI-Compatible Server[¶](#openai-compatible-server "Permanent link")

vLLM can be deployed as a server that implements the OpenAI API protocol. This allows vLLM to be used as a drop-in replacement for applications using OpenAI API. By default, it starts the server at `http://localhost:8000`. You can specify the address with `--host` and `--port` arguments. The server currently hosts one model at a time and implements endpoints such as [list models](https://platform.openai.com/docs/api-reference/models/list), [create chat completion](https://platform.openai.com/docs/api-reference/chat/completions/create), and [create completion](https://platform.openai.com/docs/api-reference/completions/create) endpoints.

Run the following command to start the vLLM server with the [Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct) model:

```
vllmserveQwen/Qwen2.5-1.5B-Instruct
```

Note

By default, the server uses a predefined chat template stored in the tokenizer. You can learn about overriding it [here](https://docs.vllm.ai/en/latest/serving/openai_compatible_server/#chat-template).

Important

By default, the server applies `generation_config.json` from the huggingface model repository if it exists. This means the default values of certain sampling parameters can be overridden by those recommended by the model creator.

To disable this behavior, please pass `--generation-config vllm` when launching the server.

This server can be queried in the same format as OpenAI API. For example, to list the models:

```
curlhttp://localhost:8000/v1/models
```

You can pass in the argument `--api-key` or environment variable `VLLM_API_KEY` to enable the server to check for API key in the header. You can pass multiple keys after `--api-key`, and the server will accept any of the keys passed, this can be useful for key rotation.

### OpenAI Completions API with vLLM[¶](#openai-completions-api-with-vllm "Permanent link")

Once your server is started, you can query the model with input prompts:

```
curlhttp://localhost:8000/v1/completions\
-H"Content-Type: application/json"\
-d'{
        "model": "Qwen/Qwen2.5-1.5B-Instruct",
        "prompt": "San Francisco is a",
        "max_tokens": 7,
        "temperature": 0
    }'
```

Since this server is compatible with OpenAI API, you can use it as a drop-in replacement for any applications using OpenAI API. For example, another way to query the server is via the `openai` Python package:

Code

```
fromopenaiimport OpenAI

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"
client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)
completion = client.completions.create(
    model="Qwen/Qwen2.5-1.5B-Instruct",
    prompt="San Francisco is a",
)
print("Completion result:", completion)
```

A more detailed client example can be found here: [examples/basic/offline\_inference/basic.py](https://github.com/vllm-project/vllm/blob/main/examples/basic/offline_inference/basic.py)

### OpenAI Chat Completions API with vLLM[¶](#openai-chat-completions-api-with-vllm "Permanent link")

vLLM is designed to also support the OpenAI Chat Completions API. The chat interface is a more dynamic, interactive way to communicate with the model, allowing back-and-forth exchanges that can be stored in the chat history. This is useful for tasks that require context or more detailed explanations.

You can use the [create chat completion](https://platform.openai.com/docs/api-reference/chat/completions/create) endpoint to interact with the model:

```
curlhttp://localhost:8000/v1/chat/completions\
-H"Content-Type: application/json"\
-d'{
        "model": "Qwen/Qwen2.5-1.5B-Instruct",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"}
        ]
    }'
```

Alternatively, you can use the `openai` Python package:

Code

```
fromopenaiimport OpenAI
# Set OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

chat_response = client.chat.completions.create(
    model="Qwen/Qwen2.5-1.5B-Instruct",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke."},
    ],
)
print("Chat response:", chat_response)
```

## On Attention Backends[¶](#on-attention-backends "Permanent link")

Currently, vLLM supports multiple backends for efficient Attention computation across different platforms and accelerator architectures. It automatically selects the most performant backend compatible with your system and model specifications.

If desired, you can also manually set the backend of your choice using the `--attention-backend` CLI argument:

```
# For online serving
vllmserveQwen/Qwen2.5-1.5B-Instruct--attention-backendFLASH_ATTN

# For offline inference
pythonscript.py--attention-backendFLASHINFER
```

Some of the available backend options include:

- On NVIDIA CUDA: `FLASH_ATTN` or `FLASHINFER`.
- On AMD ROCm: `TRITON_ATTN`, `ROCM_ATTN`, `ROCM_AITER_FA`, `ROCM_AITER_UNIFIED_ATTN`, `TRITON_MLA`, `ROCM_AITER_MLA` or `ROCM_AITER_TRITON_MLA`.

Warning

There are no pre-built vllm wheels containing Flash Infer, so you must install it in your environment first. Refer to the [Flash Infer official docs](https://docs.flashinfer.ai/) or see [docker/Dockerfile](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile) for instructions on how to install it.