---
title: 'FunctionGemma: How to Run & Fine-tune'
url: https://unsloth.ai/docs/models/tutorials/functiongemma.md
source: llms
fetched_at: 2026-04-27T18:14:20.36997865-03:00
rendered_js: false
word_count: 1197
summary: This document provides a comprehensive guide on how to run and fine-tune the FunctionGemma 270M model, detailing usage recommendations, chat template formats, and providing step-by-step instructions for local deployment via llama.cpp, as well as options for mobile device integration.
tags:
    - functiongemma-model
    - llm-fine-tuning
    - local-deployment
    - llama-cpp
    - tool-calling
    - inference-guide
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# FunctionGemma: How to Run & Fine-tune

FunctionGemma is a 270M parameter model by Google DeepMind for function-calling. Based on [Gemma 3](031-models-tutorials-gemma-3-how-to-run-and-fine-tune.md) 270M, text-only tool-calling. Runs full precision on **550MB RAM** (CPU). Fine-tunable with Unsloth.

- GGUF: [unsloth/functiongemma-270m-it-GGUF](https://huggingface.co/unsloth/functiongemma-270m-it-GGUF)

### Free Notebooks

- [Reason before Tool Calling](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/FunctionGemma_\(270M\).ipynb)
- [Multi-Turn Tool Calling](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/FunctionGemma_\(270M\)-Multi-Turn-Tool-Calling.ipynb)
- [Mobile Actions](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/FunctionGemma_\(270M\)-Mobile-Actions.ipynb)

## Usage Guide

Google recommended inference settings:

| Parameter            | Value   |
| -------------------- | ------- |
| `top_k`              | 64      |
| `top_p`              | 0.95    |
| `temperature`        | 1.0     |
| Max context length   | 32,768  |

Chat template usage:

```python
def get_today_date():
    """ Gets today's date """
    return {"today_date": "18 December 2025"}
    
tokenizer.apply_chat_template(
    [
        {"role" : "user", "content" : "what is today's date?"},
    ],
    tools = [get_today_date], add_generation_prompt = True, tokenize = False,
)
```

> [!info] Developer message
> FunctionGemma requires a system/developer message: `You are a model that can do function calling with the following functions`. Unsloth versions pre-build this if omitted — use [unsloth/functiongemma-270m-it](https://huggingface.co/unsloth/functiongemma-270m-it).

### Chat Template Format

```
<bos><start_of_turn>developer\nYou are a model that can do function calling with the following functions<start_function_declaration>declaration:get_today_date{description:<escape>Gets today's date<escape>,parameters:{type:<escape>OBJECT<escape>}}<end_function_declaration><end_of_turn>\n<start_of_turn>user\nwhat is today's date?<end_of_turn>\n<start_of_turn>model\n
```

## Running FunctionGemma in llama.cpp

### Build llama.cpp

From [GitHub](https://github.com/ggml-org/llama.cpp). Set `-DGGML_CUDA=OFF` for CPU-only or Apple Metal (on by default for Mac).

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

### Run from Hugging Face

Model is small enough for full-precision BF16:

```bash
./llama.cpp/llama-cli \
    -hf unsloth/functiongemma-270m-it-GGUF:BF16 \
    --jinja -ngl 99 --ctx-size 32768 \
    --top-k 64 --top-p 0.95 --temp 1.0
```

### Download Manually

After `pip install huggingface_hub hf_transfer`:

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/functiongemma-270m-it-GGUF",
    local_dir = "unsloth/functiongemma-270m-it-GGUF",
    allow_patterns = ["*BF16*"],
)
```

### Run in Conversation Mode

```bash
./llama.cpp/llama-cli \
    --model unsloth/functiongemma-270m-it-GGUF/functiongemma-270m-it-BF16.gguf \
    --ctx-size 32768 \
    --n-gpu-layers 99 \
    --seed 3407 \
    --prio 2 \
    --top-k 64 \
    --top-p 0.95 \
    --temp 1.0 \
    --jinja
```

## Phone Deployment

FunctionGemma runs on-device. Collaboration with PyTorch uses quantization-aware training ([QAT](108-blog-quantization-aware-training-qat.md)) to recover 70% accuracy on edge.

- **Pixel 8** and **iPhone 15 Pro**: ~50 tokens/s inference
- Privacy-first, instant, offline
- [Free Colab notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(0_6B\)-Phone_Deployment.ipynb) — change to Gemma3, follow [Gemma 3 Executorch docs](https://github.com/pytorch/executorch/tree/main/examples/models/gemma3)
- See [[082-basics-inference-and-deployment-deploy-llms-phone|iOS and Android deployment tutorials]]

## Fine-tuning FunctionGemma

Google designed FunctionGemma for fine-tuning on specific function-calling tasks including multi-turn. Unsloth supports full fine-tuning or LoRA via Colab notebooks.

### Chat Template Structure

| Turn Type                | Content                                                                                                          |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| **Developer Prompt**     | `<start_of_turn>developer` / `You can do function calling with the following functions:`                         |
| **Function Declaration** | `<start_function_declaration>declaration:get_weather{` / `description: "Get weather for city",` / `parameters: { city: STRING }` / `}` / `<end_function_declaration>` / `<end_of_turn>` |
| **User Turn**            | `<start_of_turn>user` / `What is the weather like in Paris?` / `<end_of_turn>`                                  |
| **Function Call**        | `<start_of_turn>model` / `<start_function_call>call:get_weather{` / `city: "paris"` / `}` / `<end_function_call>` |
| **Function Response**    | `<start_function_response>response:get_weather{temperature:26}` / `<end_function_response>`                     |
| **Assistant Closing**    | `The weather in Paris is 26 degrees Celsius.` / `<end_of_turn>`                                                 |

### Reasoning Before Tool Calling

Uses a single thinking block via `think` tokens — model reasons before calling:

| Thinking + Function Call | Content |
| --- | --- |
| `<start_of_turn>model` / `think` / `The user wants weather for Paris. I have the get_weather tool. I should call it with the city argument.` / `end_think` / `<start_function_call>call:get_weather{` / `city: "paris"` / `}` / `<end_function_call>` | Reasoning then structured function call |

## Fine-tuning for Mobile Actions

The [Mobile Actions notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/FunctionGemma_\(270M\)-Mobile-Actions.ipynb) enables on-device actions (calendar, reminders, etc.):

Input example:

```python
[{'role': 'developer',
  'content': 'Current date and time given in YYYY-MM-DDTHH:MM:SS format: 2025-06-04T15:29:23\nDay of week is Wednesday\nYou are a model that can do function calling with the following functions\n',
  'tool_calls': None},
 {'role': 'user',
  'content': 'Please set a reminder for a "Team Sync Meeting" this Friday, June 6th, 2025, at 2 PM.',
  'tool_calls': None}]
```

Expected output:

```
<start_of_turn>user
Please set a reminder for a "Team Sync Meeting" this Friday, June 6th, 2025, at 2 PM.<end_of_turn>
<start_of_turn>model
<start_function_call>call:create_calendar_event{body:None,datetime:2025-06-06 14:00:00,email:None,first_name:None,last_name:None,phone_number:None,query:None,subject:None,title:<escape>Team Sync Meeting<escape>,to:None}<end_function_call><start_function_response>
```

## Multi-Turn Tool Calling

The [Multi-Turn notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/FunctionGemma_\(270M\)-Multi-Turn-Tool-Calling.ipynb) shows FunctionGemma calling tools across long conversations.

### Define Tools

```python
def get_today_date():
    """
    Gets today's date

    Returns:
        today_date: Today's date in format 18 December 2025
    """
    from datetime import datetime
    today_date = datetime.today().strftime("%d %B %Y")
    return {"today_date": today_date}

def get_current_weather(location: str, unit: str = "celsius"):
    """
    Gets the current weather in a given location.

    Args:
        location: The city and state, e.g. "San Francisco, CA, USA" or "Sydney, Australia"
        unit: The unit to return the temperature in. (choices: ["celsius", "fahrenheit"])

    Returns:
        temperature: The current temperature in the given location
        weather: The current weather in the given location
    """
    if "San Francisco" in location.title():
        return {"temperature": 15, "weather": "sunny"}
    elif "Sydney" in location.title():
        return {"temperature": 25, "weather": "cloudy"}
    else:
        return {"temperature": 30, "weather": "rainy"}

def add_numbers(x: float | str, y: float | str):
    """
    Adds 2 numbers together

    Args:
        x: First number
        y: Second number

    Returns:
        result: x + y
    """
    return {"result" : float(x) + float(y)}

def multiply_numbers(x: float | str, y: float | str):
    """
    Multiplies 2 numbers together

    Args:
        x: First number
        y: Second number

    Returns:
        result: x * y
    """
    return {"result" : float(x) * float(y)}
```

### Tool Mapping

```python
FUNCTION_MAPPING = {
    "get_today_date" : get_today_date,
    "get_current_weather" : get_current_weather,
    "add_numbers": add_numbers,
    "multiply_numbers": multiply_numbers,
}
TOOLS = list(FUNCTION_MAPPING.values())
```

### Parsing and Invocation Code

```python
#@title FunctionGemma parsing code (expandible)
import re
def extract_tool_calls(text):
    def cast(v):
        try: return int(v)
        except:
            try: return float(v)
            except: return {'true': True, 'false': False}.get(v.lower(), v.strip("'\""))

    return [{
        "name": name,
        "arguments": {
            k: cast((v1 or v2).strip())
            for k, v1, v2 in re.findall(r"(\w+):(?:<escape>(.*?)<escape>|([^,}]*))", args)
        }
    } for name, args in re.findall(r"<start_function_call>call:(\w+)\{(.*?)\}<end_function_call>", text, re.DOTALL)]

def process_tool_calls(output, messages):
    calls = extract_tool_calls(output)
    if not calls: return messages
    messages.append({
        "role": "assistant",
        "tool_calls": [{"type": "function", "function": call} for call in calls]
    })
    results = [
        {"name": c['name'], "response": FUNCTION_MAPPING[c['name']](**c['arguments'])}
        for c in calls
    ]
    messages.append({ "role": "tool", "content": results })
    return messages

def _do_inference(model, messages, max_new_tokens = 128):
    inputs = tokenizer.apply_chat_template(
        messages, tools = TOOLS, add_generation_prompt = True, return_dict = True, return_tensors = "pt",
    )
    output = tokenizer.decode(inputs["input_ids"][0], skip_special_tokens = False)

    out = model.generate(**inputs.to(model.device), max_new_tokens = max_new_tokens,
                         top_p = 0.95, top_k = 64, temperature = 1.0,)
    generated_tokens = out[0][len(inputs["input_ids"][0]):]
    return tokenizer.decode(generated_tokens, skip_special_tokens = True)
    
def do_inference(model, messages, print_assistant = True, max_new_tokens = 128):
    output = _do_inference(model, messages, max_new_tokens = max_new_tokens)
    messages = process_tool_calls(output, messages)
    if messages[-1]["role"] == "tool":
        output = _do_inference(model, messages, max_new_tokens = max_new_tokens)
    messages.append({"role": "assistant", "content": output})
    if print_assistant: print(output)
    return messages
```

### Load Model and Run

```python
from unsloth import FastLanguageModel
import torch
max_seq_length = 4096 # Can choose any sequence length!
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/functiongemma-270m-it",
    max_seq_length = max_seq_length, # Choose any for long context!
    load_in_4bit = False,  # 4 bit quantization to reduce memory
    load_in_8bit = False, # [NEW!] A bit more accurate, uses 2x memory
    load_in_16bit = True, # [NEW!] Enables 16bit LoRA
    full_finetuning = False, # [NEW!] We have full finetuning now!
    # token = "hf_...", # use one if using gated models
)

messages = []
messages.append({"role": "user", "content": "What's today's date?"})
messages = do_inference(model, messages, max_new_tokens = 128)
```

### All Notebooks

| Notebook | Link |
| --- | --- |
| Reason before Tool Calling | [Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/FunctionGemma_\(270M\).ipynb) |
| Mobile Actions | [Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/FunctionGemma_\(270M\)-Mobile-Actions.ipynb) |
| Multi-Turn Tool Calling | [Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/FunctionGemma_\(270M\)-Multi-Turn-Tool-Calling.ipynb) |

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://unsloth.ai/docs/models/tutorials/functiongemma.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

#functiongemma #tool-calling #llm-fine-tuning #mobile-deployment #llama-cpp
