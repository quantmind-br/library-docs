---
title: Gemma 4 - SGLang Documentation
url: https://docs.sglang.io/cookbook/autoregressive/Google/Gemma4
source: sitemap
fetched_at: 2026-05-11T05:50:36.187320292-03:00
rendered_js: false
word_count: 717
summary: This document provides a comprehensive guide for installing, configuring, and deploying Google's Gemma 4 model family using the SGLang framework, including support for multimodal inputs, reasoning, and speculative decoding.
tags:
    - gemma-4
    - sglang
    - llm-deployment
    - multimodal-models
    - speculative-decoding
    - model-inference
    - gpu-acceleration
category: guide
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

## 1. Model Introduction

Gemma 4 is Google’s next-generation family of open models, building on the Gemma 3 architecture with improved performance, MoE variants, and multimodal support for text, vision, and audio. **Key Features:**

- **Hybrid Attention**: Combines sliding window and full attention layers for efficient long-context processing
- **Multimodal**: Supports text, image, and audio inputs via dedicated vision and audio encoders
- **MoE Variant**: The 26B-A4B model uses a Mixture-of-Experts architecture for efficient inference
- **Per-Layer Embeddings (PLE)**: Layer-specific token embeddings for enhanced representations
- **Reasoning**: Built-in thinking mode with `gemma4` reasoning parser
- **Tool Calling**: Function call support with streaming via `gemma4` tool call parser
- **Fused Operations**: Triton-optimized RMSNorm + residual + scalar kernels

**Available Models:**

ModelArchitectureParameters[google/gemma-4-E2B-it](https://huggingface.co/google/gemma-4-E2B-it)Dense~2B[google/gemma-4-E4B-it](https://huggingface.co/google/gemma-4-E4B-it)Dense~4B[google/gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)Dense31B[google/gemma-4-26B-A4B-it](https://huggingface.co/google/gemma-4-26B-A4B-it)MoE26B total / 4B active

## 2. SGLang Installation

Gemma 4 support requires [sgl-project/sglang#21952](https://github.com/sgl-project/sglang/pull/21952) and a specific transformers commit:

```
# Install SGLang from main branch (after sglang#21952 is merged)
pip install 'git+https://github.com/sgl-project/sglang.git#subdirectory=python'

# Install transformers with Gemma 4 support
pip install 'git+https://github.com/huggingface/transformers.git@91b1ab1fdfa81a552644a92fbe3e8d88de40e167'

# Or use Docker AMD64
docker pull lmsysorg/sglang:gemma4 # CUDA 12.9
docker pull lmsysorg/sglang:cu13-gemma4 # CUDA 13

# For ARM64 (GB200 / GB300)
docker pull lmsysorg/sglang:dev-gemma4 # CUDA 12.9
docker pull lmsysorg/sglang:dev-cu13-gemma4 # CUDA 13
```

For the full Docker setup and other installation methods, please refer to the [official SGLang installation guide](https://docs.sglang.io/docs/get-started/install).

## 3. Model Deployment

### 3.1 Basic Configuration

**Interactive Command Generator**: Use the configuration selector below to automatically generate the appropriate deployment command for your hardware platform and model variant.

Model Variant

E2B (~2B)E4B (~4B)31B (Dense)26B-A4B (MoE)

Hardware Platform

H200B200MI300X

Reasoning Parser

DisabledEnabled

Tool Call Parser

DisabledEnabled

Speculative Decoding (MTP)

DisabledBaselineEnabledLower Latency

Run this Command:

```
sglang serve --model-path google/gemma-4-E4B-it \
  --reasoning-parser gemma4 \
  --tool-call-parser gemma4 \
  --mem-fraction-static 0.85 \
  --host 0.0.0.0 --port 30000
```

### 3.2 Configuration Tips

- SGLang automatically selects the Triton attention backend for Gemma 4 models (required for bidirectional image-token attention during prefill).
- For the 26B-A4B MoE model, consider `--tp 2` for high-throughput workloads.
- **Speculative Decoding (MTP)**: Each Gemma 4 variant ships with a paired `*-assistant` draft model that enables NEXTN multi-token prediction. Enable it via the selector above, or pass `--speculative-algorithm NEXTN --speculative-draft-model-path google/gemma-4-<variant>-it-assistant --speculative-num-steps 5 --speculative-num-draft-tokens 6 --speculative-eagle-topk 1`. MTP can significantly reduce latency for interactive use cases. The 26B-A4B MoE model requires `--tp 2` when MTP is enabled.
- Hardware requirements:

ModelHardwareTPgemma-4-E2B-it1x H200 / 1x MI300X / 1x MI325X / 1x MI355X1gemma-4-E4B-it1x H200 / 1x MI300X / 1x MI325X / 1x MI355X1gemma-4-31B-it2x H200 / 1x MI300X / 1x MI325X / 1x MI355X2 (H200) / 1 (AMD)gemma-4-26B-A4B-it1x H200 / 1x MI300X / 1x MI325X / 1x MI355X1

### 3.3 AMD GPU Deployment (MI300X / MI325X / MI355X)

SGLang automatically selects the correct attention backend on AMD GPUs. For the small E-models (`gemma-4-E2B-it`, `gemma-4-E4B-it`), disable AITER on AMD GPUs and use the same command line otherwise:

```
SGLANG_USE_AITER=0 sglang serve --model-path google/gemma-4-E4B-it \
  --reasoning-parser gemma4 \
  --tool-call-parser gemma4 \
  --host 0.0.0.0 --port 30000
```

For `gemma-4-31B-it` and `gemma-4-26B-A4B-it`, the same commands above work on MI300X, MI325X, and MI355X without additional command-line changes.

> **Status**: AMD benchmarks are available in [Section 5.1](#51-speed-benchmark).

## 4. Model Invocation

Deploy gemma-4-26B-A4B-it (MoE) with all features enabled:

```
sglang serve --model-path google/gemma-4-26B-A4B-it \
  --reasoning-parser gemma4 \
  --tool-call-parser gemma4 \
  --host 0.0.0.0 --port 30000
```

#### Speculative Decoding (MTP) Server Commands

Each Gemma 4 variant ships with a paired `*-assistant` draft model for NEXTN multi-token prediction. Use the commands below to enable MTP for the corresponding target model. These match the configuration generated when you toggle **Speculative Decoding (MTP) → Enabled** in the [interactive selector](#31-basic-configuration).

```
# Gemma 4 E2B + MTP
sglang serve \
  --model-path google/gemma-4-E2B-it \
  --speculative-algorithm NEXTN \
  --speculative-draft-model-path google/gemma-4-E2B-it-assistant \
  --speculative-num-steps 5 \
  --speculative-num-draft-tokens 6 \
  --speculative-eagle-topk 1 \
  --mem-fraction-static 0.85

# Gemma 4 E4B + MTP
sglang serve \
  --model-path google/gemma-4-E4B-it \
  --speculative-algorithm NEXTN \
  --speculative-draft-model-path google/gemma-4-E4B-it-assistant \
  --speculative-num-steps 5 \
  --speculative-num-draft-tokens 6 \
  --speculative-eagle-topk 1 \
  --mem-fraction-static 0.85

# Gemma 4 31B + MTP
sglang serve \
  --model-path google/gemma-4-31B-it \
  --tp-size 2 \
  --speculative-algorithm NEXTN \
  --speculative-draft-model-path google/gemma-4-31B-it-assistant \
  --speculative-num-steps 5 \
  --speculative-num-draft-tokens 6 \
  --speculative-eagle-topk 1 \
  --mem-fraction-static 0.85

# Gemma 4 26B-A4B + MTP
sglang serve \
  --model-path google/gemma-4-26B-A4B-it \
  --tp-size 2 \
  --speculative-algorithm NEXTN \
  --speculative-draft-model-path google/gemma-4-26B-A4B-it-assistant \
  --speculative-num-steps 5 \
  --speculative-num-draft-tokens 6 \
  --speculative-eagle-topk 1 \
  --mem-fraction-static 0.85
```

### 4.1 Basic Usage

```
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:30000/v1",
    api_key="EMPTY"
)

response = client.chat.completions.create(
    model="google/gemma-4-26B-A4B-it",
    messages=[
        {"role": "user", "content": "What are the key differences between TCP and UDP?"}
    ],
    max_tokens=1024
)

print(response.choices[0].message.content)
```

### 4.2 Vision Input

Gemma 4 multimodal variants accept images alongside text:

```
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:30000/v1",
    api_key="EMPTY"
)

response = client.chat.completions.create(
    model="google/gemma-4-26B-A4B-it",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://farm4.staticflickr.com/3175/2653711032_804ff86d81_z.jpg"
                    }
                },
                {
                    "type": "text",
                    "text": "Describe this image in detail."
                }
            ]
        }
    ],
    max_tokens=1024
)

print(response.choices[0].message.content)
```

### 4.3 Reasoning (Thinking Mode)

Gemma 4 supports hybrid reasoning. Thinking is **not enabled by default** — pass `chat_template_kwargs: {"enable_thinking": true}` via `extra_body` to activate it. The reasoning parser separates thinking and content, returning the thinking process via `reasoning_content` in the streaming response.

```
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:30000/v1",
    api_key="EMPTY"
)

response = client.chat.completions.create(
    model="google/gemma-4-26B-A4B-it",
    messages=[
        {"role": "user", "content": "Solve step by step: If a train travels at 60 km/h for 2.5 hours, how far does it go?"}
    ],
    max_tokens=4096,
    stream=True,
    extra_body={"chat_template_kwargs": {"enable_thinking": True}}
)

thinking_started = False
has_thinking = False
has_answer = False

for chunk in response:
    if chunk.choices and len(chunk.choices) > 0:
        delta = chunk.choices[0].delta

        # Print thinking process
        if hasattr(delta, 'reasoning_content') and delta.reasoning_content:
            if not thinking_started:
                print("=============== Thinking =================", flush=True)
                thinking_started = True
            has_thinking = True
            print(delta.reasoning_content, end="", flush=True)

        # Print answer content
        if delta.content:
            if has_thinking and not has_answer:
                print("\n=============== Content =================", flush=True)
                has_answer = True
            print(delta.content, end="", flush=True)

print()
```

### 4.4 Tool Calling

Gemma 4 supports function calling with the `gemma4` tool call parser. Enable it during deployment with `--tool-call-parser gemma4`.

```
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
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "Temperature unit"
                    }
                },
                "required": ["location"]
            }
        }
    }
]

response = client.chat.completions.create(
    model="google/gemma-4-26B-A4B-it",
    messages=[
        {"role": "user", "content": "What's the weather in Tokyo?"}
    ],
    tools=tools,
    stream=True
)

thinking_started = False
has_thinking = False

for chunk in response:
    if chunk.choices and len(chunk.choices) > 0:
        delta = chunk.choices[0].delta

        if hasattr(delta, 'reasoning_content') and delta.reasoning_content:
            if not thinking_started:
                print("=============== Thinking =================", flush=True)
                thinking_started = True
            has_thinking = True
            print(delta.reasoning_content, end="", flush=True)

        if hasattr(delta, 'tool_calls') and delta.tool_calls:
            if has_thinking and thinking_started:
                print("\n=============== Tool Calls ================", flush=True)
                thinking_started = False
            for tool_call in delta.tool_calls:
                if tool_call.function:
                    print(f"Tool Call: {tool_call.function.name}")
                    print(f"   Arguments: {tool_call.function.arguments}")

        if delta.content:
            print(delta.content, end="", flush=True)

print()
```

## 5. Benchmark

### 5.1 Speed Benchmark

**Test Environment:**

- Hardware: H200
- SGLang Version: gemma4 branch

#### gemma-4-E2B-it (1x H200, TP=1)

Server Launch Command:

```
sglang serve --model-path google/gemma-4-E2B-it
```

**Latency Benchmark (Text)**

```
python3 -m sglang.bench_serving --backend sglang \
  --host 0.0.0.0 --port 30000 \
  --dataset-name random --num-prompts 10 --max-concurrency 1

============ Serving Benchmark Result ============
Backend:                                 sglang
Traffic request rate:                    inf
Max request concurrency:                 1
Successful requests:                     10
Benchmark duration (s):                  17.44
Total input tokens:                      6101
Total generated tokens:                  4220
Request throughput (req/s):              0.57
Output token throughput (tok/s):         242.03
Total token throughput (tok/s):          591.94
Mean TTFT (ms):                          50.19
Median TTFT (ms):                        54.22
Mean TPOT (ms):                          3.99
Median ITL (ms):                         4.05
==================================================
```

**Latency Benchmark (Image)**

```
python3 -m sglang.bench_serving --backend sglang-oai-chat \
  --host 0.0.0.0 --port 30000 \
  --dataset-name image --image-count 2 --image-resolution 720p \
  --random-input-len 128 --random-output-len 1024 \
  --num-prompts 10 --max-concurrency 1

============ Serving Benchmark Result ============
Backend:                                 sglang-oai-chat
Traffic request rate:                    inf
Max request concurrency:                 1
Successful requests:                     10
Benchmark duration (s):                  18.05
Total input tokens:                      6097
Total input vision tokens:               5340
Total generated tokens:                  4220
Request throughput (req/s):              0.55
Output token throughput (tok/s):         233.84
Total token throughput (tok/s):          571.69
Mean TTFT (ms):                          109.59
Median TTFT (ms):                        112.62
Mean TPOT (ms):                          4.01
Median ITL (ms):                         4.04
==================================================
```

**Throughput Benchmark (Text)**

```
python3 -m sglang.bench_serving --backend sglang \
  --host 0.0.0.0 --port 30000 \
  --dataset-name random --num-prompts 1000 --max-concurrency 100

============ Serving Benchmark Result ============
Backend:                                 sglang
Traffic request rate:                    inf
Max request concurrency:                 100
Successful requests:                     1000
Benchmark duration (s):                  51.73
Total input tokens:                      512842
Total generated tokens:                  510855
Request throughput (req/s):              19.33
Output token throughput (tok/s):         9876.36
Peak output token throughput (tok/s):    13863.00
Total token throughput (tok/s):          19791.14
Mean TTFT (ms):                          86.57
Mean TPOT (ms):                          9.56
Median ITL (ms):                         5.99
==================================================
```

**Throughput Benchmark (Image)**

```
python3 -m sglang.bench_serving --backend sglang-oai-chat \
  --host 0.0.0.0 --port 30000 \
  --dataset-name image --image-count 2 --image-resolution 720p \
  --random-input-len 128 --random-output-len 1024 \
  --num-prompts 1000 --max-concurrency 100

============ Serving Benchmark Result ============
Backend:                                 sglang-oai-chat
Traffic request rate:                    inf
Max request concurrency:                 100
Successful requests:                     1000
Benchmark duration (s):                  89.07
Total input tokens:                      617799
Total input vision tokens:               534000
Total generated tokens:                  510855
Request throughput (req/s):              11.23
Output token throughput (tok/s):         5735.75
Peak output token throughput (tok/s):    12823.00
Total token throughput (tok/s):          12672.23
Mean TTFT (ms):                          636.46
Mean TPOT (ms):                          16.34
Median ITL (ms):                         5.68
==================================================
```

#### gemma-4-E4B-it (1x H200, TP=1)

Server Launch Command:

```
sglang serve --model-path google/gemma-4-E4B-it
```

**Latency Benchmark (Text)**

```
============ Serving Benchmark Result ============
Backend:                                 sglang
Traffic request rate:                    inf
Max request concurrency:                 1
Successful requests:                     10
Benchmark duration (s):                  24.49
Total input tokens:                      6101
Total generated tokens:                  4220
Request throughput (req/s):              0.41
Output token throughput (tok/s):         172.32
Total token throughput (tok/s):          421.45
Mean TTFT (ms):                          52.76
Median TTFT (ms):                        53.66
Mean TPOT (ms):                          5.64
Median ITL (ms):                         5.74
==================================================
```

**Latency Benchmark (Image)**

```
============ Serving Benchmark Result ============
Backend:                                 sglang-oai-chat
Traffic request rate:                    inf
Max request concurrency:                 1
Successful requests:                     10
Benchmark duration (s):                  25.04
Total input tokens:                      6124
Total input vision tokens:               5340
Total generated tokens:                  4220
Request throughput (req/s):              0.40
Output token throughput (tok/s):         168.54
Total token throughput (tok/s):          413.13
Mean TTFT (ms):                          110.15
Median TTFT (ms):                        108.24
Mean TPOT (ms):                          5.66
Median ITL (ms):                         5.73
==================================================
```

**Throughput Benchmark (Text)**

```
============ Serving Benchmark Result ============
Backend:                                 sglang
Traffic request rate:                    inf
Max request concurrency:                 100
Successful requests:                     1000
Benchmark duration (s):                  72.95
Total input tokens:                      512842
Total generated tokens:                  510855
Request throughput (req/s):              13.71
Output token throughput (tok/s):         7002.68
Peak output token throughput (tok/s):    9878.00
Total token throughput (tok/s):          14032.60
Mean TTFT (ms):                          166.33
Mean TPOT (ms):                          13.36
Median ITL (ms):                         8.88
==================================================
```

**Throughput Benchmark (Image)**

```
============ Serving Benchmark Result ============
Backend:                                 sglang-oai-chat
Traffic request rate:                    inf
Max request concurrency:                 100
Successful requests:                     1000
Benchmark duration (s):                  108.99
Total input tokens:                      616952
Total input vision tokens:               534000
Total generated tokens:                  510855
Request throughput (req/s):              9.18
Output token throughput (tok/s):         4687.38
Peak output token throughput (tok/s):    9277.00
Total token throughput (tok/s):          10348.25
Mean TTFT (ms):                          626.17
Mean TPOT (ms):                          20.00
Median ITL (ms):                         8.64
==================================================
```

#### gemma-4-31B-it (2x H200, TP=2)

Server Launch Command:

```
sglang serve --model-path google/gemma-4-31B-it --tp 2
```

**Latency Benchmark (Text)**

```
============ Serving Benchmark Result ============
Backend:                                 sglang
Traffic request rate:                    inf
Max request concurrency:                 1
Successful requests:                     10
Benchmark duration (s):                  53.05
Total input tokens:                      6101
Total generated tokens:                  4220
Request throughput (req/s):              0.19
Output token throughput (tok/s):         79.55
Total token throughput (tok/s):          194.55
Mean TTFT (ms):                          72.77
Median TTFT (ms):                        75.05
Mean TPOT (ms):                          12.32
Median ITL (ms):                         12.53
==================================================
```

**Latency Benchmark (Image)**

```
============ Serving Benchmark Result ============
Backend:                                 sglang-oai-chat
Traffic request rate:                    inf
Max request concurrency:                 1
Successful requests:                     10
Benchmark duration (s):                  53.78
Total input tokens:                      6162
Total input vision tokens:               5340
Total generated tokens:                  4220
Request throughput (req/s):              0.19
Output token throughput (tok/s):         78.46
Total token throughput (tok/s):          193.03
Mean TTFT (ms):                          143.35
Median TTFT (ms):                        146.85
Mean TPOT (ms):                          12.37
Median ITL (ms):                         12.48
==================================================
```

**Throughput Benchmark (Text)**

```
============ Serving Benchmark Result ============
Backend:                                 sglang
Traffic request rate:                    inf
Max request concurrency:                 100
Successful requests:                     1000
Benchmark duration (s):                  182.00
Total input tokens:                      512842
Total generated tokens:                  510855
Request throughput (req/s):              5.49
Output token throughput (tok/s):         2806.82
Peak output token throughput (tok/s):    3798.00
Total token throughput (tok/s):          5624.56
Mean TTFT (ms):                          324.67
Mean TPOT (ms):                          33.95
Median ITL (ms):                         25.44
==================================================
```

**Throughput Benchmark (Image)**

```
============ Serving Benchmark Result ============
Backend:                                 sglang-oai-chat
Traffic request rate:                    inf
Max request concurrency:                 100
Successful requests:                     1000
Benchmark duration (s):                  236.46
Total input tokens:                      621630
Total input vision tokens:               534000
Total generated tokens:                  510855
Request throughput (req/s):              4.23
Output token throughput (tok/s):         2160.42
Peak output token throughput (tok/s):    3745.00
Total token throughput (tok/s):          4789.30
Mean TTFT (ms):                          952.02
Mean TPOT (ms):                          44.17
Median ITL (ms):                         26.81
==================================================
```

#### gemma-4-26B-A4B-it (MoE, 1x H200, TP=1)

Server Launch Command:

```
sglang serve --model-path google/gemma-4-26B-A4B-it
```

> **Tip**: Consider `--tp 2` for high-throughput workloads.

**Latency Benchmark (Text)**

```
============ Serving Benchmark Result ============
Backend:                                 sglang
Traffic request rate:                    inf
Max request concurrency:                 1
Successful requests:                     10
Benchmark duration (s):                  25.00
Total input tokens:                      6101
Total generated tokens:                  4220
Request throughput (req/s):              0.40
Output token throughput (tok/s):         168.81
Total token throughput (tok/s):          412.85
Mean TTFT (ms):                          103.74
Median TTFT (ms):                        46.57
Mean TPOT (ms):                          5.60
Median ITL (ms):                         5.78
==================================================
```

**Latency Benchmark (Image)**

```
============ Serving Benchmark Result ============
Backend:                                 sglang-oai-chat
Traffic request rate:                    inf
Max request concurrency:                 1
Successful requests:                     10
Benchmark duration (s):                  25.31
Total input tokens:                      6164
Total input vision tokens:               5340
Total generated tokens:                  4220
Request throughput (req/s):              0.40
Output token throughput (tok/s):         166.70
Total token throughput (tok/s):          410.20
Mean TTFT (ms):                          129.22
Median TTFT (ms):                        132.54
Mean TPOT (ms):                          5.68
Median ITL (ms):                         5.75
==================================================
```

**Throughput Benchmark (Text)**

```
============ Serving Benchmark Result ============
Backend:                                 sglang
Traffic request rate:                    inf
Max request concurrency:                 100
Successful requests:                     1000
Benchmark duration (s):                  138.98
Total input tokens:                      512842
Total generated tokens:                  510855
Request throughput (req/s):              7.20
Output token throughput (tok/s):         3675.81
Peak output token throughput (tok/s):    4799.00
Total token throughput (tok/s):          7365.91
Mean TTFT (ms):                          153.77
Mean TPOT (ms):                          25.95
Median ITL (ms):                         20.23
==================================================
```

**Throughput Benchmark (Image)**

```
============ Serving Benchmark Result ============
Backend:                                 sglang-oai-chat
Traffic request rate:                    inf
Max request concurrency:                 100
Successful requests:                     1000
Benchmark duration (s):                  186.38
Total input tokens:                      621146
Total input vision tokens:               534000
Total generated tokens:                  510855
Request throughput (req/s):              5.37
Output token throughput (tok/s):         2740.86
Peak output token throughput (tok/s):    4962.00
Total token throughput (tok/s):          6073.47
Mean TTFT (ms):                          854.71
Mean TPOT (ms):                          34.64
Median ITL (ms):                         19.08
==================================================
```

#### gemma-4-31B-it (1x MI300X, TP=1)

Server Launch Command:

```
sglang serve --model-path google/gemma-4-31B-it
```

> **Note**: The 31B dense model fits on a single MI300X (192 GB VRAM) at TP=1, unlike H200 (141 GB) which requires TP=2.

**Latency Benchmark (Text)**

```
python3 -m sglang.bench_serving --backend sglang \
  --host 0.0.0.0 --port 30000 \
  --dataset-name random --num-prompts 10 --max-concurrency 1

============ Serving Benchmark Result ============
Backend:                                 sglang
Traffic request rate:                    inf
Max request concurrency:                 1
Successful requests:                     10
Benchmark duration (s):                  103.55
Total input tokens:                      6101
Total generated tokens:                  4220
Request throughput (req/s):              0.10
Output token throughput (tok/s):         40.75
Total token throughput (tok/s):          99.67
Mean TTFT (ms):                          152.35
Median TTFT (ms):                        169.66
Mean TPOT (ms):                          24.13
Median ITL (ms):                         24.23
==================================================
```

**Throughput Benchmark (Text)**

```
python3 -m sglang.bench_serving --backend sglang \
  --host 0.0.0.0 --port 30000 \
  --dataset-name random --num-prompts 1000 --max-concurrency 100

============ Serving Benchmark Result ============
Backend:                                 sglang
Traffic request rate:                    inf
Max request concurrency:                 100
Successful requests:                     1000
Benchmark duration (s):                  441.59
Total input tokens:                      512842
Total generated tokens:                  510855
Request throughput (req/s):              2.26
Output token throughput (tok/s):         1156.85
Peak output token throughput (tok/s):    1759.00
Total token throughput (tok/s):          2318.19
Mean TTFT (ms):                          819.22
Mean TPOT (ms):                          82.51
Median ITL (ms):                         63.45
==================================================
```

#### gemma-4-26B-A4B-it (MoE, 1x MI300X, TP=1)

Server Launch Command:

```
sglang serve --model-path google/gemma-4-26B-A4B-it
```

**Latency Benchmark (Text)**

```
python3 -m sglang.bench_serving --backend sglang \
  --host 0.0.0.0 --port 30000 \
  --dataset-name random --num-prompts 10 --max-concurrency 1

============ Serving Benchmark Result ============
Backend:                                 sglang
Traffic request rate:                    inf
Max request concurrency:                 1
Successful requests:                     10
Benchmark duration (s):                  43.73
Total input tokens:                      6101
Total generated tokens:                  4220
Request throughput (req/s):              0.23
Output token throughput (tok/s):         96.49
Total token throughput (tok/s):          236.00
Mean TTFT (ms):                          185.58
Median TTFT (ms):                        90.18
Mean TPOT (ms):                          9.78
Median ITL (ms):                         9.57
==================================================
```

**Throughput Benchmark (Text)**

```
python3 -m sglang.bench_serving --backend sglang \
  --host 0.0.0.0 --port 30000 \
  --dataset-name random --num-prompts 1000 --max-concurrency 100

============ Serving Benchmark Result ============
Backend:                                 sglang
Traffic request rate:                    inf
Max request concurrency:                 100
Successful requests:                     1000
Benchmark duration (s):                  219.43
Total input tokens:                      512842
Total generated tokens:                  510855
Request throughput (req/s):              4.56
Output token throughput (tok/s):         2328.05
Peak output token throughput (tok/s):    3500.00
Total token throughput (tok/s):          4665.16
Mean TTFT (ms):                          168.44
Mean TPOT (ms):                          41.23
Median ITL (ms):                         29.31
==================================================
```

### 5.2 Accuracy Benchmark

**Test Environment:**

- Hardware: H200
- SGLang Version: gemma4 branch

#### MMLU

ModelHumanitiesSocial SciencesSTEMOtherOverallgemma-4-E2B-it0.6210.7390.8300.736**0.720**gemma-4-E4B-it0.7030.8620.9020.825**0.810**gemma-4-31B-it0.8780.9210.8840.911**0.896**gemma-4-26B-A4B-it0.8530.9060.9380.886**0.891**

#### GSM8K

ModelAccuracyInvalidLatency (s)Output Throughput (tok/s)gemma-4-E2B-it0.1700.0003.9908041.739gemma-4-E4B-it0.7450.0004.1744672.030gemma-4-31B-it0.8050.00516.1481559.914gemma-4-26B-A4B-it0.4500.01013.0014089.457

#### MMMU

ModelOverallgemma-4-E2B-it**0.307**gemma-4-E4B-it**0.396**gemma-4-31B-it**0.589**gemma-4-26B-A4B-it**0.549**