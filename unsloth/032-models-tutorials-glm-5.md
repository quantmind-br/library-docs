---
title: 'GLM-5: How to Run Locally Guide'
url: https://unsloth.ai/docs/models/tutorials/glm-5.md
source: llms
fetched_at: 2026-04-27T18:14:00.56855652-03:00
rendered_js: false
word_count: 1153
summary: This guide explains how to run and utilize GLM-5, Z.ai's advanced reasoning model, locally using various configurations like llama.cpp or via a local Llama-server endpoint compatible with the OpenAI API.
tags:
    - glm-5
    - local-inference
    - gguf
    - llama-cpp
    - openai-api
    - model-guide
    - quantization
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# GLM-5: How to Run Locally Guide

GLM-5 is Z.ai's latest reasoning model with stronger coding, agent, and chat performance than [[004-models-tutorials-glm-4.7|GLM-4.7]], designed for long-context reasoning. Benchmarks vs GLM-4.7: Humanity's Last Exam 50.4% (+7.6%), BrowseComp 75.9% (+8.4%), Terminal-Bench-2.0 61.1% (+28.3%).

**Specs:** 744B params (40B active), 200K context window, pre-trained on 28.5T tokens. Full model = 1.65TB disk. Unsloth Dynamic 2-bit GGUF = 241GB (-85%), Dynamic 1-bit = 176GB (-89%): [GLM-5-GGUF](https://huggingface.co/unsloth/GLM-5-GGUF)

All uploads use Unsloth [[115-basics-unsloth-dynamic-2.0-ggufs|Dynamic 2.0]] for SOTA quantization performance -- 1-bit has important layers upcasted to 8 or 16-bit.

## Usage Guide

The 2-bit dynamic quant UD-IQ2_XXS uses 241GB disk -- fits on a 256GB unified memory Mac, or 1x24GB GPU + 256GB RAM with MoE offloading. 1-bit fits on 180GB RAM; 8-bit requires 805GB RAM.

> [!tip] Memory tip
> Total available memory (VRAM + RAM) should exceed the quantized model file size. llama.cpp can still run via SSD/HDD offloading if not, but inference will be slower.

### Recommended Settings

| Default Settings (Most Tasks) | SWE Bench Verified |
|---|---|
| temperature = 1.0 | temperature = 0.7 |
| top_p = 0.95 | top_p = 1.0 |
| max new tokens = 131072 | max new tokens = 16384 |
| repeat penalty = disabled or 1.0 | repeat penalty = disabled or 1.0 |

- **Min_P** = 0.01 (llama.cpp default is 0.05)
- **Maximum context window:** 202,752
- For multi-turn agentic tasks (tau^2-Bench, Terminal Bench 2): enable Preserved Thinking mode

## Run GLM-5 Tutorials

### Run in llama.cpp

#### Step 1 -- Build llama.cpp

Obtain the latest `llama.cpp` from [GitHub](https://github.com/ggml-org/llama.cpp). Change `-DGGML_CUDA=ON` to `-DGGML_CUDA=OFF` if no GPU. For Apple Mac/Metal: set `-DGGML_CUDA=OFF` (Metal on by default).

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

#### Step 2 -- Run via HF repo (general instruction)

`UD-IQ2_XXS` is the quantization type. Use `export LLAMA_CACHE="folder"` to force save location. Max context = 200K.

```bash
export LLAMA_CACHE="unsloth/GLM-5-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/GLM-5-GGUF:UD-IQ2_XXS \
    --ctx-size 16384 \
    --flash-attn on \
    --temp 0.7 \
    --top-p 1.0 \
    --min-p 0.01
```

#### Step 2 -- Run via HF repo (tool-calling)

```bash
export LLAMA_CACHE="unsloth/GLM-5-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/GLM-5-GGUF:UD-IQ2_XXS \
    --ctx-size 16384 \
    --flash-attn on \
    --temp 1.0 \
    --top-p 0.95 \
    --min-p 0.01
```

#### Step 3 -- Download the model

After `pip install huggingface_hub hf_transfer`. Choose `UD-Q2_K_XL` (dynamic 2-bit) or others. **Recommended: 2-bit dynamic quant `UD-Q2_K_XL`** for best size/accuracy balance. If downloads get stuck, see [[124-basics-troubleshooting-and-faqs-hugging-face-hub-xet-debugging|HF Hub XET debugging]].

```bash
pip install -U huggingface_hub
hf download unsloth/GLM-5-GGUF \
    --local-dir unsloth/GLM-5-GGUF \
    --include "*UD-IQ2_XXS*" # Use "*UD-TQ1_0*" for Dynamic 1bit
```

#### Step 4 -- Run with local file

Adjust `--threads 32` (CPU threads), `--ctx-size 16384` (context), `--n-gpu-layers 2` (GPU offload layers). Remove GPU flags for CPU-only inference.

```bash
./llama.cpp/llama-cli \
    --model unsloth/GLM-5-GGUF/UD-IQ2_XXS/GLM-5-UD-IQ2_XXS-00001-of-00006.gguf \
    --temp 1.0 \
    --top-p 0.95 \
    --min-p 0.01 \
    --ctx-size 16384 \
    --seed 3407
```

## Deploy with llama-server and OpenAI's completion library

Deploy via `llama-server` in a new terminal (e.g. tmux):

```bash
./llama.cpp/llama-server \
    --model unsloth/GLM-5-GGUF/UD-IQ2_XXS/GLM-5-UD-IQ2_XXS-00001-of-00006.gguf \
    --alias "unsloth/GLM-5" \
    --prio 3 \
    --temp 1.0 \
    --top-p 0.95 \
    --ctx-size 16384 \
    --port 8001
```

Then in a new terminal, after `pip install openai`:

```python
from openai import OpenAI
import json
openai_client = OpenAI(
    base_url = "http://127.0.0.1:8001/v1",
    api_key = "sk-no-key-required",
)
completion = openai_client.chat.completions.create(
    model = "unsloth/GLM-5",
    messages = [{"role": "user", "content": "Create a Snake game."},],
)
print(completion.choices[0].message.content)
```

## vLLM Deployment

Serve Z.ai's FP8 version via vLLM. Requires 860GB+ VRAM (recommended: 8xH200 = 1128GB, or 8xB200).

```bash
uv pip install --upgrade --force-reinstall vllm --torch-backend=auto --extra-index-url https://wheels.vllm.ai/nightly/cu130
uv pip install --upgrade --force-reinstall git+https://github.com/huggingface/transformers.git
uv pip install --force-reinstall numba
```

To disable FP8 KV Cache (reduces memory 50%), remove `--kv-cache-dtype fp8`:

```bash
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:False
vllm serve unsloth/GLM-5-FP8 \
    --served-model-name unsloth/GLM-5-FP8 \ \
    --kv-cache-dtype fp8 \
    --tensor-parallel-size 8 \
    --tool-call-parser glm47 \
    --reasoning-parser glm45 \
    --enable-auto-tool-choice \
    --dtype bfloat16 \
    --seed 3407 \
    --max-model-len 200000 \
    --gpu-memory-utilization 0.93 \
    --max_num_batched_tokens 4096 \
    --speculative-config.method mtp \
    --speculative-config.num_speculative_tokens 1 \
    --port 8001
```

Call via OpenAI API:

```python
from openai import AsyncOpenAI, OpenAI
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8001/v1"
client = OpenAI( # or AsyncOpenAI
    api_key = openai_api_key,
    base_url = openai_api_base,
)
```

## Tool Calling with GLM-5

See [[095-basics-tool-calling-guide-for-local-llms|Tool Calling Guide for Local LLMs]] for details. Define tool functions:

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

Inference function that parses tool calls and loops until done:

```python
from openai import OpenAI
def unsloth_inference(
    messages,
    temperature = 1.0,
    top_p = 0.95,
    top_k = -1,
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

Launch GLM-5 via `llama-server` (see above), then call `unsloth_inference()`. See [[095-basics-tool-calling-guide-for-local-llms|Tool Calling Guide]] for more details.

## Benchmarks

| Benchmark | GLM-5 | GLM-4.7 | DeepSeek-V3.2 | Kimi K2.5 | Claude Opus 4.5 | Gemini 3 Pro | GPT-5.2 (xhigh) |
|---|---|---|---|---|---|---|---|
| HLE | 30.5 | 24.8 | 25.1 | 31.5 | 28.4 | 37.2 | 35.4 |
| HLE (w/ Tools) | 50.4 | 42.8 | 40.8 | 51.8 | 43.4* | 45.8* | 45.5* |
| AIME 2026 I | 92.7 | 92.9 | 92.7 | 92.5 | 93.3 | 90.6 | - |
| HMMT Nov. 2025 | 96.9 | 93.5 | 90.2 | 91.1 | 91.7 | 93.0 | 97.1 |
| IMOAnswerBench | 82.5 | 82.0 | 78.3 | 81.8 | 78.5 | 83.3 | 86.3 |
| GPQA-Diamond | 86.0 | 85.7 | 82.4 | 87.6 | 87.0 | 91.9 | 92.4 |
| SWE-bench Verified | 77.8 | 73.8 | 73.1 | 76.8 | 80.9 | 76.2 | 80.0 |
| SWE-bench Multilingual | 73.3 | 66.7 | 70.2 | 73.0 | 77.5 | 65.0 | 72.0 |
| Terminal-Bench 2.0 (Terminus 2) | 56.2 / 60.7 dagger | 41.0 | 39.3 | 50.8 | 59.3 | 54.2 | 54.0 |
| Terminal-Bench 2.0 (Claude Code) | 56.2 / 61.1 dagger | 32.8 | 46.4 | - | 57.9 | - | - |
| CyberGym | 43.2 | 23.5 | 17.3 | 41.3 | 50.6 | 39.9 | - |
| BrowseComp | 62.0 | 52.0 | 51.4 | 60.6 | 37.0 | 37.8 | - |
| BrowseComp (w/ Context Manage) | 75.9 | 67.5 | 67.6 | 74.9 | 67.8 | 59.2 | 65.8 |
| BrowseComp-Zh | 72.7 | 66.6 | 65.0 | 62.3 | 62.4 | 66.8 | 76.1 |
| tau^2-Bench | 89.7 | 87.4 | 85.3 | 80.2 | 91.6 | 90.7 | 85.5 |
| MCP-Atlas (Public Set) | 67.8 | 52.0 | 62.2 | 63.8 | 65.2 | 66.6 | 68.0 |
| Tool-Decathlon | 38.0 | 23.8 | 35.2 | 27.8 | 43.5 | 36.4 | 46.3 |
| Vending Bench 2 | $4,432.12 | $2,376.82 | $1,034.00 | $1,198.46 | $4,967.06 | $5,478.16 | $3,591.33 |

*dagger = with Preserved Thinking mode

#glm-5 #local-inference #gguf #llama-cpp #openai-api
