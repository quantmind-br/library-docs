---
title: GLM-5.1 - How to Run Locally
url: https://unsloth.ai/docs/models/glm-5.1.md
source: llms
fetched_at: 2026-04-27T18:13:38.659077007-03:00
rendered_js: false
word_count: 1732
summary: This document serves as a comprehensive guide detailing how to run the new GLM-5.1 open model locally, outlining recommended settings, quantization options, and providing detailed instructions for using both Unsloth Studio and llama.cpp environments.
tags:
    - glm-5-1
    - local-running
    - gguf-quantization
    - unsloth-studio
    - llama-cpp
    - model-guide
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# GLM-5.1 - How to Run Locally

GLM-5.1 is Z.ai's open model. Compared with [[032-models-tutorials-glm-5|GLM-5]], it improves coding, agentic tool use, reasoning, role-play, long-horizon agentic tasks, and chat quality.

- **Full params:** 744B (40B active), 200K context, 1.65TB disk
- **Unsloth Dynamic 2-bit GGUF:** 220GB (-80%)
- **Dynamic 1-bit:** 200GB (-85%)
- GGUF: [unsloth/GLM-5.1-GGUF](https://huggingface.co/unsloth/GLM-5.1-GGUF)
- All uploads use Unsloth [[115-basics-unsloth-dynamic-2.0-ggufs|Dynamic 2.0]] for SOTA quantization (lower bits have important layers upcasted to 8/16-bit)

> [!danger]
> Do NOT use CUDA 13.2 runtime for any GGUF — causes poor outputs.

## Usage Guide

| Quant | Disk | Fits On |
|-------|------|---------|
| `UD-IQ2_M` (medium 2-bit dynamic) | 236GB | 256GB unified Mac; 1x24GB GPU + 256GB RAM (MoE offload) |
| Dynamic 1-bit | 200GB | 220GB RAM |
| 8-bit | 805GB RAM | 805GB RAM |

> [!tip]
> For best performance, ensure total available memory (VRAM + system RAM) exceeds the quantized model file size. If not, llama.cpp can still run via SSD/HDD offloading but inference will be slower.

## Recommended Settings

| Use Case | `temperature` | `top_p` | Max New Tokens |
|----------|--------------|---------|----------------|
| Default (most tasks) | 1.0 | 0.95 | 131072 |
| Terminal Bench | 0.7 | 1.0 | 16384 |

- **Maximum context window:** `202,752`
- Thinking is enabled by default. To disable:

```bash
    --chat-template-kwargs '{"enable_thinking":false}'
```

## Chat Template Update

GLM-5.1 uses the same architecture as GLM-5 with a different `chat_template.jinja`:

- Supports Claude's search tool. Tools with `defer_loading=True` are omitted from system prompt, shown in tool results instead.
- Allows empty reasoning blocks (`💭`) in assistant messages. Consecutive assistant messages must remain in same mode (thinking or non-thinking).
- Mainly improves: tool exposure, reasoning-history reconstruction, tool-message rendering.

## Run GLM-5.1

### Unsloth Studio

[[097-new-studio|Unsloth Studio]] is an open-source web UI for local AI on macOS, Windows, and Linux. Features: search/download/run GGUFs and safetensors, self-healing tool calling + web search, code execution (Python/Bash), automatic inference parameter tuning, llama.cpp CPU+GPU inference.

**1. Install Unsloth**

```bash
# MacOS, Linux, WSL:
curl -fsSL https://unsloth.ai/install.sh | sh
# Windows PowerShell:
irm https://unsloth.ai/install.ps1 | iex
```

**2. Launch Unsloth**

```bash
unsloth studio -H 0.0.0.0 -p 8888
```

Then open `http://localhost:8888` in your browser.

**3. Search and download GLM-5.1**

On first launch, create a password and sign in. You can skip the onboarding wizard.

Go to the [[099-new-studio-chat|Studio Chat]] tab, search for GLM-5.1, and download your desired quant. Recommended: `UD-Q2_K_XL` (dynamic 2-bit) for best size/accuracy balance. If downloads get stuck, see [[124-basics-troubleshooting-and-faqs-hugging-face-hub-xet-debugging|HF XET debugging]].

**4. Run GLM-5.1**

Inference parameters are auto-set in Unsloth Studio but can be changed manually. You can also edit context length, chat template, and other settings. See the [[099-new-studio-chat|Unsloth Studio inference guide]].

### llama.cpp

**1. Build llama.cpp**

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

Use `-DGGML_CUDA=OFF` for CPU-only or Apple Mac/Metal (Metal is on by default).

**2. Run via HuggingFace pull**

General instruction use-case:

```bash
export LLAMA_CACHE="unsloth/GLM-5.1-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/GLM-5.1-GGUF:UD-IQ2_M \
    --ctx-size 16384 \
    --temp 0.7 \
    --top-p 1.0
```

Tool-calling use-case:

```bash
export LLAMA_CACHE="unsloth/GLM-5.1-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/GLM-5.1-GGUF:UD-IQ2_M \
    --ctx-size 16384 \
    --temp 1.0 \
    --top-p 0.95
```

**3. Download manually**

```bash
pip install -U huggingface_hub
hf download unsloth/GLM-5.1-GGUF \
    --local-dir unsloth/GLM-5.1-GGUF \
    --include "*UD-IQ2_M*" # Use "*UD-TQ1_0*" for Dynamic 1bit
```

Recommended: `UD-Q2_K_XL` (dynamic 2-bit) for best size/accuracy balance. If downloads get stuck, see [[124-basics-troubleshooting-and-faqs-hugging-face-hub-xet-debugging|HF XET debugging]].

**4. Run local file**

```bash
./llama.cpp/llama-cli \
    --model unsloth/GLM-5.1-GGUF/UD-IQ2_M/GLM-5.1-UD-IQ2_M-00001-of-00006.gguf \
    --temp 1.0 \
    --top-p 0.95 \
    --ctx-size 16384 \
    --seed 3407
```

Adjust `--threads 32` (CPU threads), `--ctx-size 16384` (context length), `--n-gpu-layers 2` (GPU offloading layers). Remove `--n-gpu-layers` for CPU-only inference.

### Llama-server serving & OpenAI completion library

Deploy via `llama-server`:

```bash
./llama.cpp/llama-server \
    --model unsloth/GLM-5.1-GGUF/UD-IQ2_M/GLM-5.1-UD-IQ2_M-00001-of-00006.gguf \
    --alias "unsloth/GLM-5.1" \
    --prio 3 \
    --temp 1.0 \
    --top-p 0.95 \
    --ctx-size 16384 \
    --port 8001
```

Then call via OpenAI API (`pip install openai`):

```python
from openai import OpenAI
import json
openai_client = OpenAI(
    base_url = "http://127.0.0.1:8001/v1",
    api_key = "sk-no-key-required",
)
completion = openai_client.chat.completions.create(
    model = "unsloth/GLM-5.1",
    messages = [{"role": "user", "content": "Create a Snake game."},],
)
print(completion.choices[0].message.content)
```

Or set up a reusable client:

```python
from openai import AsyncOpenAI, OpenAI
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8001/v1"
client = OpenAI( # or AsyncOpenAI
    api_key = openai_api_key,
    base_url = openai_api_base,
)
```

## Tool Calling with GLM-5.1

See [[095-basics-tool-calling-guide-for-local-llms|Tool Calling Guide for Local LLMs]] for details. After launching GLM-5.1 via `llama-server` (above), define tools and run inference:

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

Inference loop (parses tool calls automatically, calls OpenAI endpoint):

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

## Benchmarks

| Benchmark | GLM-5.1 | GLM-5 | Qwen3.6-Plus | Minimax M2.7 | DeepSeek-V3.2 | Kimi K2.5 | Claude Opus 4.6 | Gemini 3.1 Pro | GPT-5.4 |
|-----------|---------|-------|-------------|-------------|---------------|-----------|-----------------|----------------|---------|
| HLE | 31.0 | 30.5 | 28.8 | 28.0 | 25.1 | 31.5 | 36.7 | **45.0** | 39.8 |
| HLE (w/ Tools) | 52.3 | 50.4 | 50.6 | - | 40.8 | 51.8 | **53.1**\* | 51.4\* | 52.1\* |
| AIME 2026 | 95.3 | 95.4 | 95.1 | 89.8 | 95.1 | 94.5 | 95.6 | 98.2 | **98.7** |
| HMMT Nov. 2025 | 94.0 | **96.9** | 94.6 | 81.0 | 90.2 | 91.1 | 96.3 | 94.8 | 95.8 |
| HMMT Feb. 2026 | 82.6 | 82.8 | 87.8 | 72.7 | 79.9 | 81.3 | 84.3 | 87.3 | **91.8** |
| IMOAnswerBench | 83.8 | 82.5 | 83.8 | 66.3 | 78.3 | 81.8 | 75.3 | 81.0 | **91.4** |
| GPQA-Diamond | 86.2 | 86.0 | 90.4 | 87.0 | 82.4 | 87.6 | 91.3 | **94.3** | 92.0 |
| SWE-Bench Pro | **58.4** | 55.1 | 56.6 | 56.2 | - | 53.8 | 57.3 | 54.2 | 57.7 |
| NL2Repo | 42.7 | 35.9 | 37.9 | 39.8 | - | 32.0 | **49.8** | 33.4 | 41.3 |
| Terminal-Bench 2.0 (Terminus-2) | 63.5 | 56.2 | 61.6 | - | 39.3 | 50.8 | 65.4 | **68.5** | - |
| Terminal-Bench 2.0 (Best self-reported) | 66.5 (Claude Code) | 56.2 (Claude Code) | - | 57.0 (Claude Code) | 46.4 (Claude Code) | - | - | - | **75.1** (Codex) |
| CyberGym | **68.7** | 48.3 | - | - | 17.3 | 41.3 | 66.6 | - | - |
| BrowseComp | **68.0** | 62.0 | - | - | 51.4 | 60.6 | - | - | - |
| BrowseComp (w/ Context Manage) | 79.3 | 75.9 | - | - | 67.6 | 74.9 | 84.0 | **85.9** | 82.7 |
| τ³-Bench | 70.6 | 69.2 | 70.7 | 67.6 | 69.2 | 66.0 | 72.4 | 67.1 | **72.9** |
| MCP-Atlas (Public Set) | 71.8 | 69.2 | **74.1** | 48.8 | 62.2 | 63.8 | 73.8 | 69.2 | 67.2 |
| Tool-Decathlon | 40.7 | 38.0 | 39.8 | 46.3 | 35.2 | 27.8 | 47.2 | 48.8 | **54.6** |
| Vending Bench 2 | $5,634.00 | $4,432.12 | $5,114.87 | - | $1,034.00 | $1,198.46 | **$8,017.59** | $911.21 | $6,144.18 |

---

# Agent Instructions: Querying This Documentation

If you need additional information not on this page, query the documentation dynamically:

```
GET https://unsloth.ai/docs/models/glm-5.1.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language. The response contains a direct answer with relevant excerpts and sources.

#glm-5-1 #local-inference #gguf #unsloth-studio #llama-cpp
