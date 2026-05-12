---
title: Llama-3.3-70B - SGLang Documentation
url: https://docs.sglang.io/cookbook/autoregressive/Llama/Llama3.3-70B
source: sitemap
fetched_at: 2026-05-11T05:50:27.202167284-03:00
rendered_js: false
word_count: 421
summary: This document provides guidelines for deploying and utilizing the Llama 3.3 70B Instruct model within the SGLang framework, specifically optimized for AMD GPU hardware. It covers deployment configurations, tool calling implementation, long-context processing, and performance benchmarking.
tags:
    - sglang
    - llama-3-3
    - amd-gpu
    - model-deployment
    - tool-calling
    - benchmarking
    - rocm
category: guide
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

## 1. Model Introduction

[Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) is Meta’s latest 70 billion parameter instruction-tuned language model, featuring improved performance and efficiency over Llama 3.1. With a 128K token context window and enhanced capabilities across reasoning, coding, and multilingual tasks, Llama 3.3 delivers state-of-the-art results while maintaining accessibility for production deployment. **Key Features:**

- **Enhanced Performance**: Improved instruction following, reasoning, and task completion over Llama 3.1
- **Tool Calling**: Native support for function calling and tool use scenarios
- **Multilingual Support**: Optimized for 8 languages (English, German, French, Italian, Portuguese, Hindi, Spanish, and Thai)
- **Extended Context**: 128K token context window for processing long documents and complex tasks
- **Efficient Deployment**: 70B parameters enable deployment on single GPU with AMD MI300X

**License:** Llama 3.3 is licensed under the Llama 3.3 Community License. See [LICENSE](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct/blob/main/LICENSE) for details. For more details, please refer to the [official Llama models repository](https://github.com/meta-llama/llama-models).

## 2. SGLang Installation

Please refer to the [official SGLang installation guide](https://docs.sglang.io/docs/get-started/install) for installation instructions.

## 3. Model Deployment

This section provides deployment configurations optimized for AMD GPUs (MI300X, MI325X, MI355X).

### 3.1 Interactive Configuration

**Interactive Command Generator**: Use the configuration selector below to automatically generate the appropriate deployment command for your AMD GPU setup.

Hardware Platform

MI300XMI325XMI355X

Tool Calling

EnabledDisabled

Run this Command:

```
python -m sglang.launch_server \
  --model-path meta-llama/Llama-3.3-70B-Instruct \
  --tp 1 \
  --tool-call-parser llama3 \
  --host 0.0.0.0 \
  --port 30000
```

### 3.2 Configuration Tips

**AMD GPU Deployment:**

- All AMD GPUs (MI300X, MI325X, MI355X) support TP=1 for both BF16 and FP8 variants
- **FP8 Model Variant**: Use AMD’s optimized `amd/Llama-3.3-70B-Instruct-FP8-KV`
- **Tool Calling**: Enable with `--tool-call-parser llama3` for function calling support
- **Higher Throughput**: Optional TP=2 or TP=4 can be used for increased throughput

## 4. Model Invocation

### 4.1 Basic Usage

For basic API usage and request examples, please refer to:

- [SGLang Basic Usage Guide](https://docs.sglang.io/docs/basic_usage/send_request)

### 4.2 Advanced Usage

#### 4.2.1 Tool Calling

Llama 3.3 70B Instruct supports native tool calling. Enable the tool parser during deployment:

```
python -m sglang.launch_server \
  --model-path meta-llama/Llama-3.3-70B-Instruct \
  --tool-call-parser llama3 \
  --tp 1 \
  --host 0.0.0.0 \
  --port 30000
```

**Python Example:**

```
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:30000/v1",
    api_key="EMPTY"
)

# Define available tools
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

# Make request
response = client.chat.completions.create(
    model="meta-llama/Llama-3.3-70B-Instruct",
    messages=[
        {"role": "user", "content": "What's the weather in Tokyo?"}
    ],
    tools=tools,
    temperature=0.7
)

# Check for tool calls
message = response.choices[0].message
if message.tool_calls:
    tool_call = message.tool_calls[0]
    print(f"Function: {tool_call.function.name}")
    print(f"Arguments: {tool_call.function.arguments}")
```

**Handling Tool Call Results:**

```
# After executing the function, send the result back
def get_weather(location, unit="celsius"):
    # Your weather API call here
    return f"The weather in {location} is 22°{unit[0].upper()} and sunny."

# Build conversation with tool result
messages = [
    {"role": "user", "content": "What's the weather in Tokyo?"},
    {
        "role": "assistant",
        "content": None,
        "tool_calls": [{
            "id": "call_123",
            "type": "function",
            "function": {
                "name": "get_weather",
                "arguments": '{"location": "Tokyo", "unit": "celsius"}'
            }
        }]
    },
    {
        "role": "tool",
        "tool_call_id": "call_123",
        "content": get_weather("Tokyo", "celsius")
    }
]

final_response = client.chat.completions.create(
    model="meta-llama/Llama-3.3-70B-Instruct",
    messages=messages,
    temperature=0.7
)

print(final_response.choices[0].message.content)
# Output: "The current weather in Tokyo is 22°C and sunny. A perfect day!"
```

#### 4.2.2 Long Context Processing

Leverage the 128K context window for processing long documents:

```
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:30000/v1",
    api_key="EMPTY"
)

# Example with long document
long_document = "..." * 10000  # Your long document here

response = client.chat.completions.create(
    model="meta-llama/Llama-3.3-70B-Instruct",
    messages=[
        {"role": "user", "content": f"Summarize this document:\n\n{long_document}"}
    ],
    temperature=0.7,
    max_tokens=1000
)

print(response.choices[0].message.content)
```

## 5. Benchmarking

Use the SGLang benchmarking suite to test model performance with different workload patterns:

### 5.1 Basic Benchmark Command

```
python -m sglang.bench_serving \
  --backend sglang \
  --dataset-name random \
  --num-prompts 1000 \
  --random-input 1024 \
  --random-output 1024 \
  --max-concurrency 16
```

### 5.2 Adjusting Benchmark Parameters

**Input/Output Length**: Adjust `--random-input` and `--random-output` to test different workload patterns:

- Short conversations: `--random-input 1024 --random-output 1024`
- Long outputs: `--random-input 1024 --random-output 8192`
- Long inputs: `--random-input 8192 --random-output 1024`

**Concurrency Levels**: Adjust `--max-concurrency` to test different load scenarios:

- Low concurrency (latency-focused): `--max-concurrency 1 --num-prompts 100`
- Medium concurrency (balanced): `--max-concurrency 16 --num-prompts 1000`
- High concurrency (throughput-focused): `--max-concurrency 100 --num-prompts 2000`

* * *

## 📚 Additional Resources

- [Meta Llama Models Repository](https://github.com/meta-llama/llama-models)
- [Llama 3.3 Model Card](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct)
- [SGLang Documentation](https://docs.sglang.io/)
- [AMD ROCm Documentation](https://rocm.docs.amd.com/)