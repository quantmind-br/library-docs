---
title: Hunyuan 3 Preview - SGLang Documentation
url: https://docs.sglang.io/cookbook/autoregressive/Tencent/Hunyuan3-Preview
source: sitemap
fetched_at: 2026-05-11T05:50:11.882734394-03:00
rendered_js: false
word_count: 799
summary: This document provides technical instructions for deploying and utilizing the Tencent Hunyuan 3 (Hy3-preview) language model within the SGLang framework, covering hardware requirements, configuration parameters, and API integration.
tags:
    - sglang
    - hunyuan
    - moe-architecture
    - deployment
    - speculative-decoding
    - hybrid-thinking
    - llm-inference
category: guide
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

## 1. Model Introduction

Hunyuan 3 Preview (Hy3-preview) is Tencent’s preview of its third-generation flagship MoE language model, featuring hybrid thinking, native tool calling, long-context reasoning, and Multi-Token Prediction (MTP) for low-latency serving. **Key Features:**

- **MoE Architecture**: 192 routed experts + 1 shared expert, 8 experts activated per token. ~276B total parameters with ~20B active, delivering dense-model quality at MoE inference cost.
- **Hybrid Thinking**: Reasoning modes (`high`, `medium`, `low`, `none`) controllable via OpenAI-standard `reasoning_effort`, allowing the same weights to trade off latency and depth of reasoning.
- **Native Tool Calling**: Trained on structured `<tool_call>` / `<arg_key>` / `<arg_value>` grammar. Pairs with SGLang’s `hunyuan` tool-call parser for streaming OpenAI-compatible function-calling output.
- **Long Context**: 256K token context window (262,144 positions) for repository-scale code and document reasoning.
- **Multi-Token Prediction (MTP)**: Ships with a built-in MTP draft module enabling speculative decoding out of the box.

**Available Models:**

- [tencent/Hy3-preview](https://huggingface.co/tencent/Hy3-preview) — BF16 instruct
- [tencent/Hy3-preview-Base](https://huggingface.co/tencent/Hy3-preview-Base) — BF16 base

**Recommended Generation Parameters:**

ParameterValue`temperature`0.7`top_p`0.9`reasoning_effort``high` / `medium` / `low` (thinking) or `none` (instant)

**License:** TODO — verify on HuggingFace model card.

## 2. SGLang Installation

SGLang offers multiple installation methods. You can choose the most suitable installation method based on your hardware platform and requirements. Please refer to the [official SGLang installation guide](https://docs.sglang.io/docs/get-started/install) for installation instructions. **Docker Images by Hardware Platform:**

Hardware PlatformDocker ImageNVIDIA H200 / B200`lmsysorg/sglang:hy3-preview`NVIDIA B300 / GB300`lmsysorg/sglang:hy3-preview-cu130`

The `hy3-preview` tag bundles the HYV3 model code, the `hunyuan` tool-call / reasoning parsers, and the MTP draft-module runtime.

## 3. Model Deployment

This section provides deployment configurations optimized for different hardware platforms and use cases.

### 3.1 Basic Configuration

**Interactive Command Generator**: Use the configuration selector below to automatically generate the appropriate deployment command for your hardware platform, quantization, and feature capabilities.

Hardware Platform

H200B200B300GB300

Reasoning Parser

DisabledEnabled

Tool Call Parser

DisabledEnabled

Speculative Decoding (MTP)

DisabledEnabledLow Latency

Run this Command:

```
sglang serve \
  --model-path tencent/Hy3-preview \
  --tp 8 \
  --reasoning-parser hunyuan \
  --tool-call-parser hunyuan \
  --trust-remote-code \
  --mem-fraction-static 0.9
```

### 3.2 Configuration Tips

**Key Parameters:**

ParameterDescriptionRecommended Value`--tool-call-parser`Tool call parser for function-calling support`hunyuan``--reasoning-parser`Reasoning parser for hybrid thinking modes`hunyuan``--trust-remote-code`Required for Hunyuan model loadingAlways enabled`--mem-fraction-static`Static memory fraction (KV + activations)`0.9``--tp`Tensor parallelism size`2` / `4` / `8` depending on hardware`--attention-backend`Attention backend (Blackwell only)`trtllm_mha``--speculative-algorithm`Speculative decoding via the bundled MTP draft`EAGLE` + `--speculative-num-steps 3 --speculative-eagle-topk 1 --speculative-num-draft-tokens 4` (set env `SGLANG_ENABLE_SPEC_V2=1`)

**Hardware Requirements: NVIDIA BF16 (`Hy3-preview`, ~552GB weights)**

- **H200 (141GB) / B200 (180GB)**: TP=8 (minimum for BF16 to fit single-node).
- **B300 (275GB) / GB300**: TP=4.
- **A100 / H100 (80GB)**: not supported single-node — BF16 requires multi-node TP=16+ on 80GB-class GPUs.

**Blackwell (B200 / B300 / GB300):** Auto-selected attention backend can mis-route for HYV3 on Blackwell. Always pass `--attention-backend trtllm_mha` explicitly on Blackwell hardware (the config generator above enforces this). **Multi-Token Prediction (MTP):** The `Hy3-preview` release bundles an MTP draft module. SGLang runs it via its EAGLE speculative-decoding path — the draft module auto-loads from the same `--model-path`. Enable with the `SGLANG_ENABLE_SPEC_V2=1` env var and the standard MTP flags:

```
SGLANG_ENABLE_SPEC_V2=1 sglang serve \
  --model-path tencent/Hy3-preview \
  --tp 8 \
  --speculative-algorithm EAGLE \
  --speculative-num-steps 3 \
  --speculative-eagle-topk 1 \
  --speculative-num-draft-tokens 4 \
  --reasoning-parser hunyuan \
  --tool-call-parser hunyuan \
  --trust-remote-code \
  --mem-fraction-static 0.85
```

Toggle the “Speculative Decoding (MTP)” option in the generator above to add these flags automatically. Tune `num-steps` / `num-draft-tokens` based on acceptance rate in your workload.

## 4. Model Invocation

### 4.1 Basic Usage

For basic API usage and request examples, please refer to:

- [SGLang Basic Usage Guide](https://docs.sglang.io/docs/basic_usage/send_request)

**Deployment Command (H200 × 8, BF16 default):**

```
sglang serve \
  --model-path tencent/Hy3-preview \
  --tp 8 \
  --reasoning-parser hunyuan \
  --tool-call-parser hunyuan \
  --trust-remote-code \
  --mem-fraction-static 0.9
```

**Testing Deployment:** After startup, you can test the SGLang OpenAI-compatible API with the following command:

```
curl http://localhost:30000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "tencent/Hy3-preview",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"}
        ]
    }'
```

**Simple Completion Example:**

```
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:30000/v1",
    api_key="EMPTY"
)

response = client.chat.completions.create(
    model="tencent/Hy3-preview",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"}
    ],
    max_tokens=1024
)

print("Reasoning:", response.choices[0].message.reasoning_content)
print("Content:  ", response.choices[0].message.content)
```

**Output Example:**

```
Reasoning: None
Content:   The Los Angeles Dodgers won the 2020 World Series. They defeated the Tampa Bay Rays in six games (4-2). This was the Dodgers' first World Series championship since 1988. The series was notable for being played in a neutral-site bubble at Globe Life Field in Arlington, Texas, due to the COVID-19 pandemic.
```

When `reasoning_effort` is not set, the server defaults to instant mode (no thinking, `reasoning_content=None`). To opt into thinking, pass `reasoning_effort="high" / "medium" / "low"` on the request — see the Hybrid Thinking section below.

### 4.2 Advanced Usage

#### 4.2.1 Reasoning Parser (Hybrid Thinking)

Hy3-preview is a hybrid-thinking model. Control the thinking budget via the OpenAI-standard `reasoning_effort`:

- `high` / `medium` / `low` — increasing amounts of chain-of-thought in `reasoning_content`
- `none` — skip thinking entirely (instant responses, content-only)

Enable the reasoning parser during deployment so that the thinking section (`<think>...</think>`) is separated into `reasoning_content`:

```
sglang serve \
  --model-path tencent/Hy3-preview \
  --tp 8 \
  --reasoning-parser hunyuan \
  --trust-remote-code \
  --mem-fraction-static 0.9
```

**Thinking Mode — High Effort:**

```
from openai import OpenAI

client = OpenAI(base_url="http://localhost:30000/v1", api_key="EMPTY")

response = client.chat.completions.create(
    model="tencent/Hy3-preview",
    messages=[{"role": "user", "content": "Solve step by step: What is 15% of 240?"}],
    reasoning_effort="high",
    max_tokens=2048,
)

msg = response.choices[0].message
print("=============== Thinking =================")
print(msg.reasoning_content)
print("=============== Content =================")
print(msg.content)
```

**Output Example:**

```
=============== Thinking =================
We need to solve: "What is 15% of 240?" Step by step. So we need to compute 15% of 240. The process: 15% means 15 per hundred, i.e., 15/100 = 0.15. Multiply 0.15 by 240. Or we can do: 10% of 240 = 24, 5% is half of 10% = 12, so sum = 36. Or do multiplication: 15/100 * 240 = (15*240)/100 = (3600)/100 = 36. So answer is 36.

We need to produce step-by-step explanation. The instruction: "Solve step by step: What is 15% of 240?" So we should provide a clear solution with steps. The final answer: 36. Also maybe include units? No units.

We'll output the solution in a clear manner.
=============== Content =================
To find 15% of 240, follow these steps:

1. **Understand that percent means "per hundred."**
   So, 15% = 15/100 or 0.15.

2. **Multiply the number (240) by the percentage in decimal form.**
   0.15 × 240.

   Alternatively, you can use fractions:
   (15/100) × 240.

3. **Perform the multiplication.**
   0.15 × 240 = 36.
   Or:
   (15 × 240) / 100 = 3600 / 100 = 36.

4. **Check using an alternative method:**
   - 10% of 240 = 24.
   - 5% of 240 = half of 10% = 12.
   - 15% = 10% + 5% = 24 + 12 = 36.

Thus, **15% of 240 is 36**.
```

**Instant Mode — No Thinking:**

```
response = client.chat.completions.create(
    model="tencent/Hy3-preview",
    messages=[{"role": "user", "content": "Give me a one-line summary of relativity."}],
    reasoning_effort="none",
    max_tokens=256,
)

print("Content:", response.choices[0].message.content)
```

**Output Example:**

```
Content: Relativity is Einstein's theory that space, time, mass, and gravity are interconnected and relative, not fixed, fundamentally changing our understanding of the universe.
```

#### 4.2.2 Tool Calling

Hy3-preview supports streaming OpenAI-compatible tool calls. Enable both parsers together — the reasoning parser strips thinking tokens before the tool-call parser runs:

```
sglang serve \
  --model-path tencent/Hy3-preview \
  --tp 8 \
  --reasoning-parser hunyuan \
  --tool-call-parser hunyuan \
  --trust-remote-code \
  --mem-fraction-static 0.9
```

**Non-Streaming Example:**

```
from openai import OpenAI

client = OpenAI(base_url="http://localhost:30000/v1", api_key="EMPTY")

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string"},
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                "required": ["city"],
            },
        },
    }
]

response = client.chat.completions.create(
    model="tencent/Hy3-preview",
    messages=[{"role": "user", "content": "What's the weather in Beijing? Use fahrenheit."}],
    tools=tools,
)

msg = response.choices[0].message
print("Reasoning:", msg.reasoning_content)
print("Content:  ", msg.content)
for tc in msg.tool_calls or []:
    print(f"Tool Call: {tc.function.name}")
    print(f"  Arguments: {tc.function.arguments}")
```

**Output Example:**

```
Reasoning: None
Content:   I'll get the current weather for Beijing in Fahrenheit for you.
Tool Call: get_weather
  Arguments: {"city": "Beijing", "unit": "fahrenheit"}
```

**Streaming Example (incremental argument deltas):** Hy3-preview’s `hunyuan` tool-call parser emits tool names first, then argument JSON in incremental fragments — matching the OpenAI streaming contract:

```
from openai import OpenAI

client = OpenAI(base_url="http://localhost:30000/v1", api_key="EMPTY")

stream = client.chat.completions.create(
    model="tencent/Hy3-preview",
    messages=[{"role": "user", "content": "What's the weather in Beijing? Use fahrenheit."}],
    tools=tools,
    stream=True,
)

tool_buffer = {}
for chunk in stream:
    delta = chunk.choices[0].delta
    if delta.content:
        print(delta.content, end="", flush=True)
    for tc in delta.tool_calls or []:
        buf = tool_buffer.setdefault(tc.index, {"name": "", "args": ""})
        if tc.function and tc.function.name:
            buf["name"] += tc.function.name
        if tc.function and tc.function.arguments:
            buf["args"] += tc.function.arguments

for idx, buf in tool_buffer.items():
    print(f"\nTool[{idx}] {buf['name']}({buf['args']})")
```

**Output Example:**

```
I'll check the current weather in Beijing for you using Fahrenheit.
Tool[0] get_weather({"city": "Beijing", "unit": "fahrenheit"})
```

## 5. Benchmark

### 5.1 Accuracy Benchmark

**Test Environment:**

- Hardware: 8× NVIDIA H200 (141GB)
- Docker Image: `lmsysorg/sglang:hy3-preview`
- Model: `tencent/Hy3-preview` (BF16)
- Tensor Parallelism: 8
- SGLang version: latest `main`

#### 5.1.1 GSM8K

- Benchmark Method: 5-shot CoT on 200 questions, evaluated via SGLang native backend
- Benchmark Command:

```
python3 benchmark/gsm8k/bench_sglang.py --num-questions 200 --parallel 64
```

- Test Results:

```
TODO — replace with real GSM8K accuracy after benchmark run on Hy3-preview (BF16).
```

#### 5.1.2 MMLU

- Benchmark Method: 5-shot, all 57 subjects
- Benchmark Command:

```
python3 benchmark/mmlu/bench_sglang.py --nsub 60 --parallel 64
```

- Test Results:

```
TODO — replace with real MMLU accuracy after benchmark run on Hy3-preview (BF16).
```

#### 5.1.3 Tool-Call Accuracy (MiniMax-Provider-Verifier)

- Benchmark Tool: [MiniMax-Provider-Verifier](https://github.com/MiniMax-AI/MiniMax-Provider-Verifier)
- Metric: function-call schema validity, argument match, and end-to-end response correctness
- Test Results:

```
TODO — replace with real tool-call accuracy after benchmark run on Hy3-preview (BF16).
```

### 5.2 Speed Benchmark

#### 5.2.1 Low Concurrency

- Benchmark Command:

```
python3 -m sglang.bench_serving \
  --backend sglang \
  --model tencent/Hy3-preview \
  --dataset-name random \
  --random-input-len 1000 \
  --random-output-len 1000 \
  --num-prompts 10 \
  --max-concurrency 1
```

- Test Results:

```
TODO — replace with real low-concurrency output on Hy3-preview (BF16).
```

#### 5.2.2 High Concurrency

- Benchmark Command:

```
python3 -m sglang.bench_serving \
  --backend sglang \
  --model tencent/Hy3-preview \
  --dataset-name random \
  --random-input-len 1000 \
  --random-output-len 1000 \
  --num-prompts 500 \
  --max-concurrency 100
```

- Test Results:

```
TODO — replace with real high-concurrency output on Hy3-preview (BF16).
```