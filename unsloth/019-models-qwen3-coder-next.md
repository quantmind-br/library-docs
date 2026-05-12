---
title: 'Qwen3-Coder-Next: How to Run Locally'
url: https://unsloth.ai/docs/models/qwen3-coder-next.md
source: llms
fetched_at: 2026-04-27T18:13:44.129287851-03:00
rendered_js: false
word_count: 2045
summary: This document provides comprehensive guides on how to run the Qwen3-Coder-Next model locally, detailing setup instructions for both Unsloth Studio and llama.cpp. It also outlines optimal inference parameters for achieving high performance in coding tasks.
tags:
    - qwen3-coder-next
    - local-inference
    - unsloth
    - llama-cpp
    - llm-model
    - gguf
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Qwen3-Coder-Next: How to Run Locally

**Qwen3-Coder-Next** — 80B MoE model (3B active parameters), **256K context**, non-reasoning for ultra-quick code responses. Comparable to models with 10-20x more active parameters. Excels at long-horizon reasoning, complex tool use, and recovery from execution failures.

| Quant | RAM required |
|---|---|
| 4-bit | ~46 GB |
| 8-bit | ~85 GB |
| 3-bit | smaller (fits <46 GB devices) |

> [!tip] RAM fit rule
> `disk space + RAM + VRAM >= size of quant`. Fully on-device = 20+ tokens/s; offloading works but slower.

GGUFs: [unsloth/Qwen3-Coder-Next-GGUF](https://huggingface.co/unsloth/Qwen3-Coder-Next-GGUF) ([Dynamic GGUFs](https://unsloth.ai/docs/basics/unsloth-dynamic-2.0-ggufs))

> [!note] Updates
> - **Feb 19**: Tool-calling improved after llama.cpp parsing fixes.
> - **Feb 4**: llama.cpp fixed `vectorized key_gdiff` calculation bug (looping/output issues). Re-download GGUFs and update llama.cpp.

## Inference Settings

| Parameter | Value | Notes |
|---|---|---|
| `temperature` | 1.0 | Qwen recommended |
| `top_p` | 0.95 | |
| `top_k` | 40 | |
| `min_p` | 0.01 | llama.cpp default is 0.05 |
| `repeat_penalty` | disabled / 1.0 | |
| Context | 262,144 (native) | Set 32,768 for less memory |

## Run Qwen3-Coder-Next

### Unsloth Studio Guide

1. **Install** — MacOS, Linux, WSL:
   ```bash
   curl -fsSL https://unsloth.ai/install.sh | sh
   ```
   Windows PowerShell:
   ```bash
   irm https://unsloth.ai/install.ps1 | iex
   ```

2. **Launch** — all platforms:
   ```bash
   unsloth studio -H 0.0.0.0 -p 8888
   ```
   Open `http://localhost:8888`.

3. **Download** — create password on first launch, skip onboarding wizard. In Studio Chat, search "Qwen3-Coder-Next" and download desired quant.

4. **Run** — inference auto-set; see [[099-new-studio-chat|Studio inference guide]].

### Llama.cpp Tutorial

#### Build llama.cpp

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

Set `-DGGML_CUDA=OFF` for CPU-only. For Apple Mac/Metal: set `-DGGML_CUDA=OFF` — Metal on by default.

#### Hugging Face Direct Pull

```bash
./llama.cpp/llama-cli \
    -hf unsloth/Qwen3-Coder-Next-GGUF:UD-Q4_K_XL \
    --ctx-size 16384 \
    --temp 1.0 --top-p 0.95 --min-p 0.01 --top-k 40
```

Use `--fit on` to auto-determine context length. Supports up to 256K if RAM/VRAM fits.

#### Download Model

```bash
pip install -U huggingface_hub
hf download unsloth/Qwen3-Coder-Next-GGUF \
    --local-dir unsloth/Qwen3-Coder-Next-GGUF \
    --include "*UD-Q4_K_XL*"
```

If downloads get stuck, see [[124-basics-troubleshooting-and-faqs-hugging-face-hub-xet-debugging|HF XET debugging]].

#### Run Conversation Mode

```bash
./llama.cpp/llama-cli \
    --model unsloth/Qwen3-Coder-Next-GGUF/Qwen3-Coder-Next-UD-Q4_K_XL.gguf \
    --seed 3407 \
    --temp 1.0 \
    --top-p 0.95 \
    --min-p 0.01 \
    --top-k 40
```

Adjust context up to 262,144 as needed.

> [!info] Non-thinking model
> Only supports non-thinking mode — does not generate `繁沁` blocks. `enable_thinking=False` no longer required.

## Llama-server Serving & Deployment

```bash
./llama.cpp/llama-server \
    --model unsloth/Qwen3-Coder-Next-GGUF/Qwen3-Coder-Next-UD-Q4_K_XL.gguf \
    --alias "unsloth/Qwen3-Coder-Next" \
    --seed 3407 \
    --temp 1.0 \
    --top-p 0.95 \
    --min-p 0.01 \
    --top-k 40 \
    --port 8001
```

Client usage (`pip install openai`):

```python
from openai import OpenAI
import json
openai_client = OpenAI(
    base_url = "http://127.0.0.1:8001/v1",
    api_key = "sk-no-key-required",
)
completion = openai_client.chat.completions.create(
    model = "unsloth/Qwen3-Coder-Next",
    messages = [{"role": "user", "content": "Create a Flappy Bird game in HTML"},],
)
print(completion.choices[0].message.content)
```

## OpenAI Codex & Claude Code

Run via local coding agentic workloads — follow [[077-basics-claude-code|Claude Code guide]] or [[078-basics-codex|Codex guide]]. Replace model name with `Qwen3-Coder-Next` and use correct parameters. Use the `llama-server` set up above.

> [!warning] Context size error
> If you see `exceed_context_size_error`, increase context length or reduce input size.

## FP8 Qwen3-Coder-Next in vLLM

Use [FP8 Dynamic quant](https://huggingface.co/unsloth/Qwen3-Coder-Next-FP8-Dynamic) for premium inference. FP8-Dynamic can boost throughput 25%+.

### Install vLLM

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv unsloth_fp8 --python 3.12 --seed
source unsloth_fp8/bin/activate
uv pip install --upgrade --force-reinstall vllm --torch-backend=auto --extra-index-url https://wheels.vllm.ai/nightly/cu130
uv pip install --upgrade --force-reinstall git+https://github.com/huggingface/transformers.git
uv pip install --force-reinstall numba
```

Change `cu130` to your CUDA version from `nvidia-smi` (only `cu129`/`cu130` supported).

### Serve Model

```bash
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:False
CUDA_VISIBLE_DEVICES='0,1,2,3' vllm serve unsloth/Qwen3-Coder-Next-FP8-Dynamic \
    --served-model-name unsloth/Qwen3-Coder-Next \
    --tensor-parallel-size 4 \
    --tool-call-parser qwen3_coder \
    --enable-auto-tool-choice \
    --dtype bfloat16 \
    --seed 3407 \
    --max-model-len 200000 \
    --gpu-memory-utilization 0.93 \
    --port 8001
```

For 1 GPU: use `CUDA_VISIBLE_DEVICES='0'` and `--tensor-parallel-size 1`. Add `--kv-cache-dtype fp8` to reduce KV cache memory by 50%.

## Tool Calling with Qwen3-Coder-Next

Works with both vLLM and llama-server via OpenAI API.

### Tool Definitions & Execution

```python
import json, subprocess, random
from typing import Any
def add_number(a: float | str, b: float | str) -> float:
    return float(a) + float(b)
def multiply_number(a: float | str, b: float | str) -> float:
    return float(a) * float(b)
def substract_number(a: float | str, b: float | str) -> float:
    return float(a) - float(b)
def write_a_story() -> str:
    return random.choice([
        "A long time ago in a galaxy far far away...",
        "There were 2 friends who loved sloths and code...",
        "The world was ending because every sloth evolved to have superhuman intelligence...",
        "Unbeknownst to one friend, the other accidentally coded a program to evolve sloths...",
    ])
def terminal(command: str) -> str:
    if "rm" in command or "sudo" in command or "dd" in command or "chmod" in command:
        msg = "Cannot execute 'rm, sudo, dd, chmod' commands since they are dangerous"
        print(msg); return msg
    print(f"Executing terminal command `{command}`")
    try:
        return str(subprocess.run(command, capture_output = True, text = True, shell = True, check = True).stdout)
    except subprocess.CalledProcessError as e:
        return f"Command failed: {e.stderr}"
def python(code: str) -> str:
    data = {}
    exec(code, data)
    del data["__builtins__"]
    return str(data)
MAP_FN = {
    "add_number": add_number,
    "multiply_number": multiply_number,
    "substract_number": substract_number,
    "write_a_story": write_a_story,
    "terminal": terminal,
    "python": python,
}
tools = [
    {
        "type": "function",
        "function": {
            "name": "add_number",
            "description": "Add two numbers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "string",
                        "description": "The first number.",
                    },
                    "b": {
                        "type": "string",
                        "description": "The second number.",
                    },
                },
                "required": ["a", "b"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "multiply_number",
            "description": "Multiply two numbers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "string",
                        "description": "The first number.",
                    },
                    "b": {
                        "type": "string",
                        "description": "The second number.",
                    },
                },
                "required": ["a", "b"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "substract_number",
            "description": "Substract two numbers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "string",
                        "description": "The first number.",
                    },
                    "b": {
                        "type": "string",
                        "description": "The second number.",
                    },
                },
                "required": ["a", "b"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "write_a_story",
            "description": "Writes a random story.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "terminal",
            "description": "Perform operations from the terminal.",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "The command you wish to launch, e.g `ls`, `rm`, ...",
                    },
                },
                "required": ["command"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "python",
            "description": "Call a Python interpreter with some Python code that will be ran.",
            "parameters": {
                "type": "object",
                "properties": {
                    "code": {
                        "type": "string",
                        "description": "The Python code to run",
                    },
                },
                "required": ["code"],
            },
        },
    },
]
```

### Inference Function (auto-parses tool calls)

```python
from openai import OpenAI
def unsloth_inference(
    messages,
    temperature = 1.0,
    top_p = 0.95,
    top_k = 40,
    min_p = 0.01,
    repetition_penalty = 1.0,
):
    messages = messages.copy()
    openai_client = OpenAI(
        base_url = "http://127.0.0.1:8001/v1",
        api_key = "sk-no-key-required",
    )
    model_name = next(iter(openai_client.models.list())).id
    print(f"Using model = {model_name}")
    has_tool_calls = True
    original_messages_len = len(messages)
    while has_tool_calls:
        print(f"Current messages = {messages}")
        response = openai_client.chat.completions.create(
            model = model_name,
            messages = messages,
            temperature = temperature,
            top_p = top_p,
            tools = tools if tools else None,
            tool_choice = "auto" if tools else None,
            extra_body = {"top_k": top_k, "min_p": min_p, "repetition_penalty" :repetition_penalty,}
        )
        tool_calls = response.choices[0].message.tool_calls or []
        content = response.choices[0].message.content or ""
        tool_calls_dict = [tc.to_dict() for tc in tool_calls] if tool_calls else tool_calls
        messages.append({"role": "assistant", "tool_calls": tool_calls_dict, "content": content,})
        for tool_call in tool_calls:
            fx, args, _id = tool_call.function.name, tool_call.function.arguments, tool_call.id
            out = MAP_FN[fx](**json.loads(args))
            messages.append({"role": "tool", "tool_call_id": _id, "name": fx, "content": str(out),})
        else:
            has_tool_calls = False
    return messages
```

### Example: Execute Python Code

```python
messages = [{
    "role": "user",
    "content": [{"type": "text", "text": "Create a Fibonacci function in Python and find fib(20)."}],
}]
unsloth_inference(messages, temperature = 1.0, top_p = 0.95, top_k = 40, min_p = 0.00)
```

### Example: Execute Terminal Commands

```python
messages = [{
    "role": "user",
    "content": [{"type": "text", "text": "Write 'I'm a happy Sloth' to a file, then print it back to me."}],
}]
messages = unsloth_inference(messages, temperature = 1.0, top_p = 1.0, top_k = 40, min_p = 0.00)
```

See [[095-basics-tool-calling-guide-for-local-llms|Tool Calling Guide]] for more examples.

## Benchmarks

### GGUF Quantization Benchmarks

Third-party benchmarks (Aider Polyglot + Benjamin Marie 750-prompt suite):

- **3-bit `UD-IQ3_XXS`** comes close to BF16 performance — sensible minimum for most use cases
- Pattern: 1-bit → 2-bit → 3-bit → 6-bit steadily improving
- Unsloth Q4_K_M outperforms standard Q4_K_M; Q3_K_M better on HumanEval than standard Q4_K_M
- **Non-Unsloth FP8** performs worse than both `UD-IQ3_XXS` and `UD-Q6_K_XL`
- Recommended: at least Q4_K_M

### Qwen3-Coder-Next Benchmarks

Best performing model for its size; comparable to models with 10-20x more active parameters.

| Benchmark | Qwen3-Coder-Next (80B) | DeepSeek-V3.2 (671B) | GLM-4.7 (358B) | MiniMax M2.1 (229B) |
|---|---|---|---|---|
| SWE-Bench Verified (w/ SWE-Agent) | 70.6 | 70.2 | 74.2 | 74.8 |
| SWE-Bench Multilingual (w/ SWE-Agent) | 62.8 | 62.3 | 63.7 | 66.2 |
| SWE-Bench Pro (w/ SWE-Agent) | 44.3 | 40.9 | 40.6 | 34.6 |
| Terminal-Bench 2.0 (w/ Terminus-2 json) | 36.2 | 39.3 | 37.1 | 32.6 |
| Aider | 66.2 | 69.9 | 52.1 | 61.0 |

## Agent Instructions: Querying This Documentation

```
GET https://unsloth.ai/docs/models/qwen3-coder-next.md?ask=<question>
```

#qwen3-coder-next #local-inference #gguf #tool-calling #vllm
