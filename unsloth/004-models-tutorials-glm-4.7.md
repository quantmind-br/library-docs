---
title: 'GLM-4.7: How to Run Locally Guide'
url: https://unsloth.ai/docs/models/tutorials/glm-4.7.md
source: llms
fetched_at: 2026-04-27T18:14:08.247986473-03:00
rendered_js: false
word_count: 1514
summary: This guide explains how to run Z.ai's GLM-4.7 thinking model locally using various methods including `llama.cpp`, Ollama, and `llama-server`. It provides detailed configuration settings, recommended parameters, and step-by-step instructions for optimal performance.
tags:
    - glm-4-7
    - local-llm
    - gguf
    - ollama
    - llama-cpp
    - deployment
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# GLM-4.7: How to Run Locally Guide

GLM-4.7 is Z.ai's latest thinking model. SOTA on SWE-bench (73.8%, +5.8), SWE-bench Multilingual (66.7%, +12.9), Terminal Bench 2.0 (41.0%, +16.5). Stronger coding, agent, and chat vs [[005-models-tutorials-glm-4.6-how-to-run-locally|GLM-4.6]].

- **Full 355B** — 400GB disk; **Unsloth Dynamic 2-bit GGUF** — 134GB (−75%). [GLM-4.7-GGUF](https://huggingface.co/unsloth/GLM-4.7-GGUF)
- All uploads use Unsloth [[115-basics-unsloth-dynamic-2.0-ggufs|Dynamic 2.0]] for SOTA 5-shot MMLU and Aider performance — minimal accuracy loss.

## Usage Guide

UD-Q2_K_XL (2-bit dynamic quant) uses 135GB disk — works in **1x24GB GPU + 128GB RAM** with MoE offloading. UD-TQ1 (1-bit) **works natively in Ollama**.

> [!warning] Must use `--jinja` for llama.cpp quants
> Uses fixed chat templates and enables correct template. Incorrect results without `--jinja`.

4-bit quants fit in **1x40GB GPU** (MoE offloaded to RAM). ~5 tok/s with 165GB+ RAM. Recommended: 205GB+ RAM for 4-bit. For optimal 5+ tok/s need 205GB unified memory or combined RAM+VRAM.

> [!tip] VRAM + RAM = quant size (best performance)
> If not, SSD offloading works with llama.cpp (slower). Use `--fit on` for maximum GPU usage.

## Recommended Settings

| Default (Most Tasks) | Terminal Bench / SWE Bench |
|---|---|
| **temperature = 1.0** | **temperature = 0.7** |
| **top_p = 0.95** | **top_p = 1.0** |
| **max new tokens = 131072** | **max new tokens = 16384** |

- Use `--jinja` for llama.cpp — chat template fixes included.
- **Max context window:** 131,072

## Run GLM-4.7 Tutorials

Step-by-step guides for [Ollama](#run-in-ollama) and [llama.cpp](#run-in-llamacpp).

### Run in llama.cpp

**1. Build llama.cpp** — [GitHub](https://github.com/ggml-org/llama.cpp). Set `-DGGML_CUDA=OFF` for CPU-only. Metal (Apple) is on by default.

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

**2. Run directly** — `:Q2_K_XL` is the quant type. Use `export LLAMA_CACHE="folder"` to force save location. Max 128K context.

```bash
export LLAMA_CACHE="unsloth/GLM-4.7-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/GLM-4.7-GGUF:UD-Q2_K_XL \
    --jinja \
    --ctx-size 16384 \
    --flash-attn on \
    --temp 1.0 \
    --top-p 0.95 \
    --fit on
```

> [!info] `--fit on` (introduced 15 Dec 2025) — maximum GPU+CPU usage
> MoE offloading via `-ot` regex:
> - `-ot ".ffn_.*_exps.=CPU"` — all MoE layers to CPU (least VRAM)
> - `-ot ".ffn_(up|down)_exps.=CPU"` — up+down projection only
> - `-ot ".ffn_(up)_exps.=CPU"` — up projection only (most VRAM)
> - Custom: `-ot "\.(6|7|8|9|[0-9][0-9]|[0-9][0-9][0-9])\.ffn_(gate|up|down)_exps.=CPU"` — from layer 6+

**3. Download via Hugging Face** — recommend **2.7-bit dynamic quant `UD-Q2_K_XL`** for size/accuracy balance.

```bash
pip install -U huggingface_hub
hf download unsloth/GLM-4.7-GGUF \
    --local-dir unsloth/GLM-4.7-GGUF \
    --include "*UD-Q2_K_XL*" # Use "*UD-TQ1_0*" for Dynamic 1bit
```

**4. Run from local file** — adjust `--threads`, `--ctx-size`, `--n-gpu-layers` as needed.

```bash
./llama.cpp/llama-cli \
    --model unsloth/GLM-4.7-GGUF/UD-Q2_K_XL/GLM-4.7-UD-Q2_K_XL-00001-of-00003.gguf \
    --jinja \
    --temp 1.0 \
    --top-p 0.95 \
    --ctx-size 16384 \
    --seed 3407 \
    --fit on
```

### Run in Ollama

**1. Install Ollama:**

```bash
apt-get update
apt-get install pciutils -y
curl -fsSL https://ollama.com/install.sh | sh
```

**2. Run the model:**

```bash
OLLAMA_MODELS=unsloth ollama serve &

OLLAMA_MODELS=unsloth ollama run hf.co/unsloth/GLM-4.7-GGUF:TQ1_0
```

**3. Other quants** — merge split GGUF files first:

```bash
./llama.cpp/llama-gguf-split --merge \
  GLM-4.7-GGUF/GLM-4.7-UD-Q2_K_XL/GLM-4.7-UD-Q2_K_XL-00001-of-00003.gguf \
	merged_file.gguf
```

```bash
OLLAMA_MODELS=unsloth ollama serve &

OLLAMA_MODELS=unsloth ollama run merged_file.gguf
```

### Deploy with llama-server and OpenAI completion library

```bash
./llama.cpp/llama-server \
    --model unsloth/GLM-4.7-GGUF/UD-Q2_K_XL/GLM-4.7-UD-Q2_K_XL-00001-of-00003.gguf \
    --alias "unsloth/GLM-4.7" \
    --fit on \
    --prio 3 \
    --temp 1.0 \
    --top-p 0.95 \
    --ctx-size 16384 \
    --port 8001 \
    --jinja
```

Then use OpenAI Python library (`pip install openai`):

```python
from openai import OpenAI
import json
openai_client = OpenAI(
    base_url = "http://127.0.0.1:8001/v1",
    api_key = "sk-no-key-required",
)
completion = openai_client.chat.completions.create(
    model = "unsloth/GLM-4.7",
    messages = [{"role": "user", "content": "What is 2+2?"},],
)
print(completion.choices[0].message.content)
```

### Tool Calling with GLM 4.7

See [[095-basics-tool-calling-guide-for-local-llms|Tool Calling Guide for Local LLMs]] for details. Example tools (add, multiply, subtract, story, terminal, python):

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

Auto-parsing inference function (calls OpenAI endpoint, loops on tool calls):

```python
from openai import OpenAI
def unsloth_inference(
    messages,
    temperature = 0.7,
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

**Example — math tool call:**

```python
messages = [{
    "role": "user",
    "content": [{"type": "text", "text": "What is today's date plus 3 days?"}],
}]
unsloth_inference(messages, temperature = 0.7, top_p = 1.0, top_k = -1, min_p = 0.00)
```

**Example — Python code execution:**

```python
messages = [{
    "role": "user",
    "content": [{"type": "text", "text": "Create a Fibonacci function in Python and find fib(20)."}],
}]
unsloth_inference(messages, temperature = 0.7, top_p = 1.0, top_k = -1, min_p = 0.00)
```

### Improving generation speed

`--fit on` (15 Dec 2025) auto offloads max to GPU, rest to CPU. [PR #16653](https://github.com/ggml-org/llama.cpp/pull/16653).

MoE offloading `-ot` options (more VRAM = fewer layers offloaded):
- `-ot ".ffn_.*_exps.=CPU"` — all MoE layers (least VRAM)
- `-ot ".ffn_(up|down)_exps.=CPU"` — up+down projection
- `-ot ".ffn_(up)_exps.=CPU"` — up projection only
- Custom regex: `-ot "\.(6|7|8|9|[0-9][0-9]|[0-9][0-9][0-9])\.ffn_(gate|up|down)_exps.=CPU"` — from layer 6+

High throughput mode: `llama-parallel` ([docs](https://github.com/ggml-org/llama.cpp/tree/master/examples/parallel)). KV cache quantization to 4-bit reduces VRAM/RAM movement and speeds generation.

### How to fit long context (full 128K)

**KV cache quantization** reduces K/V caches to lower bits, enabling longer context and faster generation.

K quant options (default `f16`): `f32, f16, bf16, q8_0, q4_0, q4_1, iq4_nl, q5_0, q5_1`

- Use `_1` variants (`q4_1, q5_1`) for better accuracy (slightly slower).

V cache quantization requires **Flash Attention**: compile llama.cpp with `-DGGML_CUDA_FA_ALL_QUANTS=ON`, use `--flash-attn`.

V quant options: `f32, f16, bf16, q8_0, q4_0, q4_1, iq4_nl, q5_0, q5_1`

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://unsloth.ai/docs/models/tutorials/glm-4.7.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

#glm-4-7 #local-llm #gguf #ollama #llama-cpp
