---
title: Ring-2.5-1T - SGLang Documentation
url: https://docs.sglang.io/cookbook/autoregressive/InclusionAI/Ring-2.5-1T
source: sitemap
fetched_at: 2026-05-11T05:50:37.654691743-03:00
rendered_js: false
word_count: 335
summary: This document provides technical instructions for deploying and using the Ring-2.5-1T trillion-parameter reasoning model within the SGLang framework, covering hardware-specific configurations, tool calling, and reasoning parser setup.
tags:
    - llm
    - sglang
    - model-deployment
    - reasoning-model
    - trillion-parameter
    - tool-calling
    - fp8-quantization
category: guide
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

## 1. Model Introduction

[Ring-2.5-1T](https://huggingface.co/inclusionAI/Ring-2.5-1T) is the world’s first open-source trillion-parameter reasoning model based on hybrid linear attention architecture, developed by InclusionAI. Building on Ring-1T, Ring-2.5-1T demonstrates substantial improvements in generation efficiency, reasoning depth, and long-horizon task execution capabilities. **Key Features:**

- **Trillion-Scale Model**: ~1T total parameters with 63B activation parameters using a hybrid linear attention architecture (1:7 MLA + Lightning Linear Attention)
- **Generation Efficiency**: Reduces memory access overhead by over 10x and increases generation throughput by more than 3x for sequences exceeding 32K tokens
- **Deep Reasoning**: Achieves gold medal level for both IMO 2025 and CMO 2025, with dense rewards for rigorous reasoning process feedback
- **Long-horizon Task Execution**: Enhanced autonomous execution capability through large-scale fully-async agentic RL training
- **Tool Calling**: Supports function calling with XML-style tool call format
- **Context Length**: 128K -&gt; 256K (YaRN)

**Available Models:**

- **FP8 (8-bit quantized)**: [inclusionAI/Ring-2.5-1T](https://huggingface.co/inclusionAI/Ring-2.5-1T)

**License:** MIT

## 2. SGLang Installation

Ring-2.5-1T requires a specific SGLang Docker image:

```
# For H200/B200
docker pull lmsysorg/sglang:nightly-dev-20260213-a0ebaa64

# For GB200/GB300
docker pull lmsysorg/sglang:nightly-dev-cu13-20260213-a0ebaa64

# For MI300X/325X
docker pull lmsysorg/sglang:v0.5.9-rocm700-mi30x

# For MI355X
docker pull lmsysorg/sglang:v0.5.9-rocm700-mi35x
```

For other installation methods, please refer to the [official SGLang installation guide](https://docs.sglang.io/docs/get-started/install).

## 3. Model Deployment

This section provides deployment configurations optimized for different hardware platforms.

### 3.1 Basic Configuration

**Interactive Command Generator**: Use the configuration selector below to automatically generate the appropriate deployment command for your hardware platform.

Hardware Platform

H200B200GB200GB300MI300XMI325XMI355X

Reasoning Parser

DisabledEnabled

Tool Call Parser

DisabledEnabled

Run this Command:

```
sglang serve \
  --model-path inclusionAI/Ring-2.5-1T \
  --tp 8 \
  --trust-remote-code
```

### 3.2 Configuration Tips

- The `--trust-remote-code` flag is required for this model due to custom modeling code.
- The model uses FP8 quantization (compressed-tensors format).

## 4. Model Invocation

Deploy Ring-2.5-1T with the following command (on H200, all features enabled):

```
sglang serve \
  --model-path inclusionAI/Ring-2.5-1T \
  --tp 8 \
  --trust-remote-code \
  --host 0.0.0.0 \
  --port 30000
```

### 4.1 Basic Usage

For basic API usage and request examples, please refer to:

- [SGLang Basic Usage Guide](https://docs.sglang.io/docs/basic_usage/send_request)

### 4.2 Advanced Usage

#### 4.2.1 Reasoning Parser

To enable reasoning output separation, add `--reasoning-parser deepseek-r1` when launching the server. The thinking process is returned via `reasoning_content` in the streaming response.

```
sglang serve \
  --model-path inclusionAI/Ring-2.5-1T \
  --tp 8 \
  --trust-remote-code \
  --reasoning-parser deepseek-r1 \
  --host 0.0.0.0 \
  --port 30000

from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:30000/v1",
    api_key="EMPTY"
)

response = client.chat.completions.create(
    model="inclusionAI/Ring-2.5-1T",
    messages=[
        {"role": "user", "content": "Solve this problem step by step: What is 15% of 240?"}
    ],
    max_tokens=2048,
    stream=True
)

for chunk in response:
    if chunk.choices and len(chunk.choices) > 0:
        delta = chunk.choices[0].delta

        if hasattr(delta, 'reasoning_content') and delta.reasoning_content:
            print(delta.reasoning_content, end="", flush=True)

        if delta.content:
            print(delta.content, end="", flush=True)

print()
```

#### 4.2.2 Tool Calling

To enable tool calling, add `--tool-call-parser qwen` when launching the server.

```
sglang serve \
  --model-path inclusionAI/Ring-2.5-1T \
  --tp 8 \
  --trust-remote-code \
  --tool-call-parser qwen \
  --host 0.0.0.0 \
  --port 30000

from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:30000/v1",
    api_key="EMPTY"
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city name"
                    }
                },
                "required": ["location"]
            }
        }
    }
]

response = client.chat.completions.create(
    model="inclusionAI/Ring-2.5-1T",
    messages=[
        {"role": "user", "content": "What's the weather in Beijing?"}
    ],
    tools=tools
)

print(response.choices[0].message.tool_calls)
```

**Output Example:**

```
[ChatCompletionMessageFunctionToolCall(id='call_770360e31d194ed79d32cd8c', function=Function(arguments='{"location": "Beijing"}', name='get_weather'), type='function', index=0)]
```

## 5. Benchmark

### GSM8K

- Deployment Command

```
sglang serve \
  --model-path inclusionAI/Ring-2.5-1T \
  --tp-size 8 \
  --trust-remote-code
```

- Benchmark Command

```
python3 benchmark/gsm8k/bench_sglang.py --temperature 1.2 --top-p 0.8 --max-new-tokens 32768 --num-questions 200 --tokenizer-path inclusionAI/Ring-2.5-1T --enable-thinking
```

- Test Result

```
Accuracy: 0.955
Invalid: 0.010
Latency: 615.833 s
Output throughput: 412.360 token/s
```