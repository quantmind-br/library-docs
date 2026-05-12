---
title: Tool Calling Guide for Local LLMs
url: https://unsloth.ai/docs/basics/tool-calling-guide-for-local-llms.md
source: llms
fetched_at: 2026-04-27T18:15:07.790069234-03:00
rendered_js: false
word_count: 825
summary: Guide to tool calling (function calling) with local LLMs via llama.cpp, llama-server, and OpenAI-compatible endpoints.
tags:
    - tool-calling
    - local-llm
    - inference-guide
    - function-calling
    - llama-cpp
    - python-tools
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:22:00Z
---

# Tool Calling Guide for Local LLMs

Tool calling lets an LLM emit structured requests to trigger functions (search, calculate, call APIs) instead of guessing in text. Benefits: more reliable/up-to-date outputs, real actions (query systems, validate facts, enforce schemas), reduced hallucination.

This tutorial covers tool calling with local LLMs via llama.cpp / llama-server / OpenAI endpoints, with math, story, Python code, and terminal function examples.

> [!tip] Unsloth Studio auto-setup
> Tool calling is automatic in [[099-new-studio-chat|Unsloth Studio]] — select model, toggle tool-calling on/off. Includes self-healing tool calling for [[007-models-gemma-4-train|Gemma 4]].

## Supported models

Works with nearly [any model](https://unsloth.ai/docs/get-started/unsloth-model-catalog) including:

- **Qwen** family: [[019-models-qwen3-coder-next|Qwen3-Coder-Next]], [[044-models-tutorials-qwen3-coder-how-to-run-locally|Qwen3-Coder]], others
- **GLM** family: [[004-models-tutorials-glm-4.7|GLM-4.7]], 4.6, [[003-models-glm-4.7-flash|GLM-4.7-Flash]]; **Kimi**: [[014-models-kimi-k2.5|Kimi K2.5]], [[035-models-tutorials-kimi-k2-thinking-how-to-run-locally|Kimi K2 Thinking]]
- **DeepSeek**: [[127-models-tutorials-deepseek-v3.1-how-to-run-locally|DeepSeek-V3.1]], V3.2; **MiniMax**
- [[013-models-gpt-oss-how-to-run-and-fine-tune|gpt-oss]], [[017-models-nemotron-3-nemotron-3-super|NVIDIA Nemotron 3 Nano]], [[027-models-tutorials-devstral-2|Devstral 2]]

## Tool Calling Setup

### Build llama.cpp

Clone from [GitHub](https://github.com/ggml-org/llama.cpp) and build. Set `-DGGML_CUDA=OFF` for CPU-only or Apple Mac/Metal (Metal on by default).

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

### Define tool functions

In a new terminal (CTRL+B+D in tmux), create tool functions:

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

### Inference function (Devstral 2 example)

> [!info] When switching models, use correct sampling parameters. See [[050-models-tutorials|model guides]].

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

### Use-case examples (Devstral 2: temp=0.15, top_p=1.0, top_k=-1, min_p=0.00)

#### Writing a story

```python
messages = [{
    "role": "user",
    "content": [{"type": "text", "text": "Could you write me a story ?"}],
}]
unsloth_inference(messages, temperature = 0.15, top_p = 1.0, top_k = -1, min_p = 0.00)
```

#### Mathematical operations

```python
messages = [{
    "role": "user",
    "content": [{"type": "text", "text": "What is today's date plus 3 days?"}],
}]
unsloth_inference(messages, temperature = 0.15, top_p = 1.0, top_k = -1, min_p = 0.00)
```

#### Execute generated Python code

```python
messages = [{
    "role": "user",
    "content": [{"type": "text", "text": "Create a Fibonacci function in Python and find fib(20)."}],
}]
unsloth_inference(messages, temperature = 0.15, top_p = 1.0, top_k = -1, min_p = 0.00)
```

#### Execute arbitrary terminal functions

```python
messages = [{
    "role": "user",
    "content": [{"type": "text", "text": "Write 'I'm a happy Sloth' to a file, then print it back to me."}],
}]
messages = unsloth_inference(messages, temperature = 0.15, top_p = 1.0, top_k = -1, min_p = 0.00)
```

## Qwen3-Coder-Next Tool Calling

Same tool definitions as above (identical `MAP_FN` and `tools`). Inference function differs in defaults: `temperature=1.0`, `top_p=0.95`, `top_k=40`, `min_p=0.01`.

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

### Qwen3-Coder-Next examples

#### Execute generated Python code

```python
messages = [{
    "role": "user",
    "content": [{"type": "text", "text": "Create a Fibonacci function in Python and find fib(20)."}],
}]
unsloth_inference(messages, temperature = 1.0, top_p = 0.95, top_k = 40, min_p = 0.00)
```

#### Execute arbitrary terminal functions

```python
messages = [{
    "role": "user",
    "content": [{"type": "text", "text": "Write 'I'm a happy Sloth' to a file, then print it back to me."}],
}]
messages = unsloth_inference(messages, temperature = 1.0, top_p = 1.0, top_k = 40, min_p = 0.00)
```

## GLM-4.7-Flash + GLM 4.7 Calling

### Download model

Download [[004-models-tutorials-glm-4.7|GLM-4.7]] or [[003-models-glm-4.7-flash|GLM-4.7-Flash]], then launch via llama-server.

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/GLM-4.7-GGUF",
    local_dir = "unsloth/GLM-4.7-GGUF",
    allow_patterns = ["*UD-Q2_K_XL*",], # For Q2_K_XL
)
```

### Launch llama-server

```bash
./llama.cpp/llama-server \
    --model unsloth/GLM-4.7-GGUF/UD-Q2_K_XL/GLM-4.7-UD-Q2_K_XL-00001-of-00003.gguf \
    --alias "unsloth/GLM-4.7" \
    --threads -1 \
    --fit on \
    --prio 3 \
    --min_p 0.01 \
    --ctx-size 16384 \
    --port 8001 \
    --jinja
```

### GLM 4.7 examples (temp=0.7, top_p=1.0, top_k=-1, min_p=0.00)

Use the same `unsloth_inference` function from [[#tool-calling-setup]].

#### Mathematical operations

```python
messages = [{
    "role": "user",
    "content": [{"type": "text", "text": "What is today's date plus 3 days?"}],
}]
unsloth_inference(messages, temperature = 0.7, top_p = 1.0, top_k = -1, min_p = 0.00)
```

#### Execute generated Python code

```python
messages = [{
    "role": "user",
    "content": [{"type": "text", "text": "Create a Fibonacci function in Python and find fib(20)."}],
}]
unsloth_inference(messages, temperature = 0.7, top_p = 1.0, top_k = -1, min_p = 0.00)
```

## Devstral 2 Tool Calling

### Download model

Download [[027-models-tutorials-devstral-2|Devstral 2]], then launch via llama-server.

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

### Launch llama-server

```bash
./llama.cpp/llama-server \
    --model unsloth/Devstral-Small-2-24B-Instruct-2512-GGUF/Devstral-Small-2-24B-Instruct-2512-UD-Q4_K_XL.gguf \
    --mmproj unsloth/Devstral-Small-2-24B-Instruct-2512-GGUF/mmproj-F16.gguf \
    --alias "unsloth/Devstral-Small-2-24B-Instruct-2512" \
    --threads -1 \
    --fit on \
    --prio 3 \
    --min_p 0.01 \
    --ctx-size 16384 \
    --port 8001 \
    --jinja
```

### Call model

Use the `unsloth_inference` function from [[#tool-calling-setup]] with Devstral's suggested parameters: `temperature=0.15` only.

#tool-calling #local-llm #llama-cpp #function-calling #inference
