---
title: SGLang Deployment & Inference Guide
url: https://unsloth.ai/docs/basics/inference-and-deployment/sglang-guide.md
source: llms
fetched_at: 2026-04-27T18:14:50.913462267-03:00
rendered_js: false
word_count: 920
summary: Deploy LLMs via SGLang for low-latency, high-throughput inference with GGUF support.
tags:
    - sglang-deployment
    - llm-inference
    - unsloth-guide
    - model-serving
    - docker-setup
    - quantization
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# SGLang Deployment & Inference Guide

[SGLang](https://github.com/sgl-project/sglang) — low-latency, high-throughput inference for text, image/video models on any GPU. Supports some GGUFs.

## Installation

```shellscript
# OPTIONAL: virtual environment
python -m venv unsloth_env
source unsloth_env/bin/activate

# Install Rust, outlines-core then SGLang
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env && sudo apt-get install -y pkg-config libssl-dev
pip install --upgrade pip && pip install uv
uv pip install "sglang" && uv pip install unsloth
```

**Docker:**

```shellscript
docker run --gpus all \
    --shm-size 32g \
    -p 30000:30000 \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HF_TOKEN=<secret>" \
    --ipc=host \
    lmsysorg/sglang:latest \
    python3 -m sglang.launch_server --model-path unsloth/Llama-3.1-8B-Instruct --host 0.0.0.0 --port 30000
```

## Debugging installation

> [!warning] outlines-core build failure
> If you see `outlines-core (v0.1.26) was included because sglang depends on outlines`, update Rust and outlines-core per the installation steps above.

> [!warning] Flashinfer compilation error
> `fatal error: flashinfer/attention/prefill.cuh: No such file or directory`
>
> **Fix:** `rm -rf .cache/flashinfer` and `rm -rf ~/.cache/flashinfer`
>
> Alternative workarounds:
> - `--mem-fraction-static 0.8` or `0.7`
> - `--cuda-graph-max-bs 16`
> - Omit `--enable-torch-compile`
> - `--disable-cuda-graph` (not recommended — huge performance loss)

## Deploying models

Launch in a separate terminal (or tmux):

```shellscript
python3 -m sglang.launch_server \
    --model-path unsloth/Llama-3.2-1B-Instruct \
    --host 0.0.0.0 --port 30000
```

Query via OpenAI SDK (another terminal):

```python
from openai import OpenAI
import json
openai_client = OpenAI(
    base_url = "http://0.0.0.0:30000/v1",
    api_key = "sk-no-key-required",
)
completion = openai_client.chat.completions.create(
    model = "unsloth/Llama-3.2-1B-Instruct",
    messages = [{"role": "user", "content": "What is 2+2?"},],
)
print(completion.choices[0].message.content)
```

## Deploying Unsloth finetunes

After fine-tuning (see [[064-get-started-fine-tuning-llms-guide|Fine-tuning LLMs Guide]] or [[073-get-started-unsloth-notebooks|Unsloth Notebooks]]):

```python
from unsloth import FastLanguageModel
import torch
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/gpt-oss-20b",
    max_seq_length = 2048,
    load_in_4bit = True,
)
model = FastLanguageModel.get_peft_model(model)
```

**Save to 16-bit:**

```python
model.save_pretrained_merged("finetuned_model", tokenizer, save_method = "merged_16bit")
# Or push to HuggingFace:
model.push_to_hub_merged("hf/model", tokenizer, save_method = "merged_16bit", token = "")
```

**Save LoRA adapters:**

```python
model.save_pretrained("finetuned_model")
tokenizer.save_pretrained("finetuned_model")

# Or via builtin:
model.save_pretrained_merged("model", tokenizer, save_method = "lora")
model.push_to_hub_merged("hf/model", tokenizer, save_method = "lora", token = "")
```

### gpt-oss-20b walkthrough

1. **Fine-tune** per [[013-models-gpt-oss-how-to-run-and-fine-tune|gpt-oss guide]] or [[064-get-started-fine-tuning-llms-guide|Fine-tuning Guide]]
2. **Export:**

```python
model.save_pretrained_merged(
    "finetuned_model",
    tokenizer,
    save_method = "merged_16bit",
)
# gpt-oss specific mxfp4:
model.save_pretrained_merged(
    "finetuned_model",
    tokenizer,
    save_method = "mxfp4",  # ONLY for gpt-oss
)
```

3. **Serve:**

```shellscript
python -m sglang.launch_server \
    --model-path finetuned_model \
    --host 0.0.0.0 --port 30002
```

4. **Query:**

```python
from openai import OpenAI
import json
openai_client = OpenAI(
    base_url = "http://0.0.0.0:30002/v1",
    api_key = "sk-no-key-required",
)
completion = openai_client.chat.completions.create(
    model = "finetuned_model",
    messages = [{"role": "user", "content": "What is 2+2?"},],
)
print(completion.choices[0].message.content)
```

## FP8 Online Quantization

30-50% more throughput, 50% less memory, 2x longer context:

```shellscript
python -m sglang.launch_server \
    --model-path unsloth/Llama-3.2-1B-Instruct \
    --host 0.0.0.0 --port 30002 \
    --quantization fp8 \
    --kv-cache-dtype fp8_e4m3
```

Use `--kv-cache-dtype fp8_e5m2` for larger dynamic range if you hit FP8 inference issues. Pre-quantized models: <https://huggingface.co/unsloth/models?search=-fp8>.

## Benchmarking

```shellscript
# Terminal 1: serve
python -m sglang.launch_server \
    --model-path finetuned_model \
    --host 0.0.0.0 --port 30002

# Terminal 2: benchmark (batch=8, input=1024, output=1024)
python -m sglang.bench_one_batch_server \
    --model finetuned_model \
    --base-url http://0.0.0.0:30002 \
    --batch-size 8 \
    --input-len 1024 \
    --output-len 1024
```

B200x1 GPU with gpt-oss-20b (~2,500 tok throughput):

| Batch/Input/Output | TTFT (s) | ITL (s) | Input Throughput | Output Throughput |
| ------------------ | -------- | ------- | ---------------- | ----------------- |
| 8/1024/1024        | 0.40     | 3.59    | 20,718.95        | 2,562.87          |
| 8/8192/1024        | 0.42     | 3.74    | 154,459.01       | 2,473.84          |

Server arguments: <https://docs.sglang.ai/advanced_features/server_arguments.html>.

## Offline mode (Python engine)

```python
import sglang as sgl
engine = sgl.Engine(model_path = "unsloth/Qwen3-0.6B", random_seed = 42)

prompt = "Today is a sunny day and I like"
sampling_params = {"temperature": 0, "max_new_tokens": 256}
outputs = engine.generate(prompt, sampling_params)["text"]
print(outputs)
engine.shutdown()
```

## GGUF support

SGLang supports GGUFs. Most dense models (Llama 3, Qwen 3, Mistral) are supported; Qwen3 MoE is under construction.

Install GGUF Python package:

```shellscript
pip install -e "git+https://github.com/ggml-org/llama.cpp.git#egg=gguf&subdirectory=gguf-py"
```

**Offline mode with GGUF:**

```python
from huggingface_hub import hf_hub_download
model_path = hf_hub_download(
    "unsloth/Qwen3-32B-GGUF",
    filename = "Qwen3-32B-UD-Q4_K_XL.gguf",
)
import sglang as sgl
engine = sgl.Engine(model_path = model_path, random_seed = 42)

prompt = "Today is a sunny day and I like"
sampling_params = {"temperature": 0, "max_new_tokens": 256}
outputs = engine.generate(prompt, sampling_params)["text"]
print(outputs)
engine.shutdown()
```

**High-throughput GGUF serving:**

```python
from huggingface_hub import hf_hub_download
hf_hub_download("unsloth/Qwen3-32B-GGUF", filename="Qwen3-32B-UD-Q4_K_XL.gguf", local_dir=".")
```

```shellscript
python -m sglang.launch_server \
    --model-path Qwen3-32B-UD-Q4_K_XL.gguf \
    --host 0.0.0.0 --port 30002 \
    --served-model-name unsloth/Qwen3-32B \
    --tokenizer-path unsloth/Qwen3-32B
```

`--served-model-name` sets the API model name; `--tokenizer-path` provides the HF-compatible tokenizer.

#sglang #inference #deployment #gguf #fp8 #benchmarking
