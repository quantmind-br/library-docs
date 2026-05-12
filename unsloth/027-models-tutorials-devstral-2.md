---
title: Devstral 2 - How to Run Guide
url: https://unsloth.ai/docs/models/tutorials/devstral-2.md
source: llms
fetched_at: 2026-04-27T18:14:12.696186247-03:00
rendered_js: false
word_count: 1050
summary: This document serves as a comprehensive guide on how to run the Devstral 2 LLMs (both the 24B and 123B versions), detailing setup steps, recommended inference parameters, and providing specific code examples for running text-only models and utilizing vision capabilities.
tags:
    - devstral-2
    - llm-guide
    - llama-cpp
    - model-running
    - unsloth
    - vision-support
category: tutorial
optimized: true
optimized_at: 2026-04-27T22:15:00Z
---

# Devstral 2 - How to Run Guide

Mistral's coding/agentic LLMs for software engineering: [24B](#devstral-small-2-24b) and [123B](#devstral-2-123b). 123B = SOTA in SWE-bench, coding, tool-calling, agent use-cases. 24B fits in 25GB RAM/VRAM; 123B fits in 128GB.

> [!tip] 13 Dec 2025: Chat template issues resolved. 24B & 123B updated. Install latest llama.cpp.

Supports vision, 256k context, same architecture as [[040-models-tutorials-ministral-3|Ministral 3]]. Run and fine-tune locally with Unsloth. All uploads use [Dynamic 2.0](https://unsloth.ai/docs/basics/unsloth-dynamic-2.0-ggufs) for best [Aider Polyglot](https://unsloth.ai/docs/basics/unsloth-dynamic-2.0-ggufs/unsloth-dynamic-ggufs-on-aider-polyglot) and 5-shot MMLU benchmarks.

### Unsloth Dynamic GGUFs

| Devstral-Small-2-24B-Instruct-2512 | Devstral-2-123B-Instruct-2512 |
|---|---|
| [Devstral-Small-2-**24B**-Instruct-2512-GGUF](https://huggingface.co/unsloth/Devstral-Small-2-24B-Instruct-2512-GGUF) | [Devstral-2-**123B**-Instruct-2512-GGUF](https://huggingface.co/unsloth/Devstral-2-123B-Instruct-2512-GGUF) |

## Running Devstral 2

Both models support vision but **vision is not currently supported in llama.cpp**.

### Usage Guide

- **Temperature ~0.15**
- Min_P 0.01 (optional; llama.cpp default is 0.1)
- Use `--jinja` to enable system prompt
- Max context: 262,144; recommended minimum: 16,384
- Install latest llama.cpp -- [Dec 13 2025 PR](https://github.com/ggml-org/llama.cpp/pull/17945) fixes issues

### Devstral-Small-2-24B

Full precision (Q8) fits in 25GB RAM/VRAM. Text only for now.

#### Run Devstral-Small-2-24B-Instruct-2512 in llama.cpp

1. Build llama.cpp. Change `-DGGML_CUDA=ON` to `-DGGML_CUDA=OFF` for CPU-only. **Apple Mac / Metal**: set `-DGGML_CUDA=OFF` -- Metal on by default.

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

2. Pull from HuggingFace and run (`Q4_K_XL` quant):

```bash
./llama.cpp/llama-cli \
    -hf unsloth/Devstral-Small-2-24B-Instruct-2512-GGUF:UD-Q4_K_XL \
    --jinja -ngl 99 --ctx-size 16384 \
    --temp 0.15
```

3. Download via Python (`pip install huggingface_hub hf_transfer`):

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/Devstral-Small-2-24B-Instruct-2512-GGUF",
    local_dir = "unsloth/Devstral-Small-2-24B-Instruct-2512-GGUF",
    allow_patterns = ["*UD-Q4_K_XL*", "*mmproj-F16*"], # For Q4_K_XL
)
```

4. Run in conversation mode:

```bash
./llama.cpp/llama-cli \
    --model unsloth/Devstral-Small-2-24B-Instruct-2512-GGUF/Devstral-Small-2-24B-Instruct-2512-UD-Q4_K_XL.gguf \
    --mmproj unsloth/Devstral-Small-2-24B-Instruct-2512-GGUF/mmproj-F16.gguf \
    --ctx-size 16384 \
    --n-gpu-layers 99 \
    --seed 3407 \
    --prio 2 \
    --temp 0.15 \
    --jinja
```

#### Devstral and vision

1. Download a test image: `wget https://unsloth.ai/cgi/image/fp8grpolarge_KharloZxEEaHAY2X97CEX.png?width=3840%26quality=80%26format=auto -O unsloth_fp8.png`
2. Load image after model loads: `/image unsloth_fp8.png`
3. Prompt: `Describe this image`

### Devstral-2-123B

Full precision (Q8) fits in 128GB RAM/VRAM. Text only for now.

#### Run Devstral-2-123B-Instruct-2512 Tutorial

1. Build llama.cpp (same as 24B above).

2. Pull from HuggingFace:

```bash
./llama.cpp/llama-cli \
    -hf unsloth/Devstral-2-123B-Instruct-2512-GGUF:UD-Q2_K_XL \
    --jinja -ngl 99 --ctx-size 16384 \
    --temp 0.15
```

3. Download via Python:

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/Devstral-2-123B-Instruct-2512-GGUF",
    local_dir = "unsloth/Devstral-2-123B-Instruct-2512-GGUF",
    allow_patterns = ["*UD-Q2_K_XL*", "*mmproj-F16*"],
)
```

4. Run in conversation mode:

```bash
./llama.cpp/llama-cli \
    --model unsloth/Devstral-2-123B-Instruct-2512-GGUF/Devstral-2-123B-Instruct-2512-UD-Q2_K_XL.gguf \
    --mmproj unsloth/Devstral-2-123B-Instruct-2512-GGUF/mmproj-F16.gguf \
    --ctx-size 16384 \
    --n-gpu-layers 99 \
    --seed 3407 \
    --prio 2 \
    --temp 0.15 \
    --jinja
```

## Fine-tuning Devstral 2 with Unsloth

Like [[040-models-tutorials-ministral-3|Ministral 3]] -- 2x faster training, 70% less VRAM, 8x longer context. Fits in 24GB VRAM L4 GPU. Exceeds 16GB VRAM -- cannot fine-tune free on Colab. Use [Kaggle notebook](https://www.kaggle.com/notebooks/welcome?src=https://github.com/unslothai/notebooks/blob/main/nb/Kaggle-Magistral_\(24B\)-Reasoning-Conversational.ipynb\&accelerator=nvidiaTeslaT4) (dual GPUs) -- change model name to `unsloth/Devstral-Small-2-24B-Instruct-2512`.

> [!tip] Free Ministral 3 notebooks directly support Devstral 2 (same architecture). Change model name.

- Ministral-3B-Instruct [Vision notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Ministral_3_VL_\(3B\)_Vision.ipynb) -- change model name to Devstral 2
- Ministral-3B-Instruct [GRPO notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Ministral_3_\(3B\)_Reinforcement_Learning_Sudoku_Game.ipynb) -- change model name to Devstral 2

### llama-server serving & deployment

Deploy via `llama-server` (e.g., in tmux):

```bash
./llama.cpp/llama-server \
    --model unsloth/Devstral-Small-2-24B-Instruct-2512-GGUF/Devstral-Small-2-24B-Instruct-2512-UD-Q4_K_XL.gguf \
    --mmproj unsloth/Devstral-Small-2-24B-Instruct-2512-GGUF/mmproj-F16.gguf \
    --alias "unsloth/Devstral-Small-2-24B-Instruct-2512" \
    --n-gpu-layers 999 \
    --prio 3 \
    --min_p 0.01 \
    --ctx-size 16384 \
    --port 8001 \
    --jinja
```

Then connect via OpenAI client (`pip install openai`):

```python
from openai import OpenAI
import json
openai_client = OpenAI(
    base_url = "http://127.0.0.1:8001/v1",
    api_key = "sk-no-key-required",
)
completion = openai_client.chat.completions.create(
    model = "unsloth/Devstral-Small-2-24B-Instruct-2512",
    messages = [{"role": "user", "content": "What is 2+2?"},],
)
print(completion.choices[0].message.content)
```

### Tool Calling with Devstral 2 Tutorial

After [deploying via llama-server](#llama-server-serving--deployment), load tools and test. Define tool functions:

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

Send a test message:

```python
import random
messages = [{
    "role": "user",
    "content": [random.choice([
        {"type": "text", "text": "Could you write me a story ?"},
        {"type": "text", "text": "What is today's date plus 3 days?"},
        {"type": "text", "text": "Get the current time in nanoseconds."},
        {"type": "text", "text": "Create a Fibonacci function in Python and find fib(20)."},
    ])],
}]
```

Parse tool calls automatically -- Devstral 2 may make multiple in tandem:

```python
temperature = 0.15
from openai import OpenAI
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
        tools = tools if tools else None,
        tool_choice = "auto" if tools else None,
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
print(json.dumps(messages[original_messages_len:], indent = 2))
```

Expected JSON output structure:

```json
[
  {
    "role": "assistant",
    "tool_calls": [
      {
        "id": "JviLK0wUveWguuKQHgZdFdYI2adu85jy",
        "function": {
          "arguments": "{}",
          "name": "write_a_story"
        },
        "type": "function"
      }
    ],
    "content": null
  },
  {
    "role": "tool",
    "tool_call_id": "JviLK0wUveWguuKQHgZdFdYI2adu85jy",
    "name": "write_a_story",
    "content": "A long time ago in a galaxy far far away..."
  },
  {
    "role": "assistant",
    "tool_calls": null,
    "content": "In a distant galaxy, where the stars burned with an otherworldly glow, there was a planet named Eldoria..."
  }
]
```

---

# Agent Instructions: Querying This Documentation

For additional information not on this page, query dynamically via HTTP GET:

```
GET https://unsloth.ai/docs/models/tutorials/devstral-2.md?ask=<question>
```

Question should be specific, self-contained, natural language. Response includes direct answer with relevant excerpts and sources.

#devstral-2 #llama-cpp #local-deployment #tool-calling
