---
title: 'Qwen3-Coder: How to Run Locally'
url: https://unsloth.ai/docs/models/tutorials/qwen3-coder-how-to-run-locally.md
source: llms
fetched_at: 2026-04-27T18:14:02.894844534-03:00
rendered_js: false
word_count: 1670
summary: This document serves as a guide and reference for running the Qwen3-Coder family of coding agent models locally, detailing recommended inference settings, different model variants (30B and 480B), and providing specific installation/run tutorials for Ollama and Llama.cpp.
tags:
    - qwen3-coder
    - local-inference
    - model-guide
    - llm-tuning
    - ollama-tutorial
    - llama-cpp
category: guide
optimized: true
optimized_at: 2026-04-27T21:25:00Z
---

# Qwen3-Coder: How to Run Locally

Qwen3-Coder is Qwen's coding agent model series: **30B (Qwen3-Coder-Flash)** and **480B** parameters. Qwen3-480B-A35B-Instruct achieves SOTA coding performance (61.8% Aider Polyglot) rivalling Claude Sonnet-4, GPT-4.1, and [Kimi K2](035-models-tutorials-kimi-k2-thinking-how-to-run-locally.md), with 256K context (extendable to 1M).

[Unsloth](https://github.com/unslothai/unsloth) supports fine-tuning and [[072-get-started-reinforcement-learning-rl-guide|RL]] of Qwen3-Coder. Native **1M context** GGUFs via YaRN scaling and full-precision 8bit/16bit versions are also uploaded.

> [!tip] Tool-calling fix
> Tool-calling for Qwen3-Coder is fixed in llama.cpp, Ollama, LMStudio, Open WebUI, Jan etc. The issue was universal across all uploads. See [Tool Calling Fixes](#tool-calling-fixes) for details.

> [!tip] Unsloth Dynamic Quants
> UD-Q4_K_XL (276GB) dynamic quant scored 60.9% vs bf16 (960GB) at 61.8% on Aider Polyglot — nearly matching full precision. [Details](https://huggingface.co/unsloth/Qwen3-Coder-480B-A35B-Instruct-GGUF/discussions/8).

#### Qwen3 Coder - Unsloth Dynamic 2.0 GGUFs

| Dynamic 2.0 GGUF (to run) | 1M Context Dynamic 2.0 GGUF |
|---|---|
| [30B-A3B-Instruct](https://huggingface.co/unsloth/Qwen3-Coder-30B-A3B-Instruct-GGUF) | [30B-A3B-Instruct](https://huggingface.co/unsloth/Qwen3-Coder-30B-A3B-Instruct-1M-GGUF) |
| [480B-A35B-Instruct](https://huggingface.co/unsloth/Qwen3-Coder-480B-A35B-Instruct-GGUF) | [480B-A35B-Instruct](https://huggingface.co/unsloth/Qwen3-Coder-480B-A35B-Instruct-1M-GGUF) |

## Running Qwen3-Coder

Guides for [30B-A3B](#run-qwen3-coder-30b-a3b-instruct) and [480B-A35B](#run-qwen3-coder-480b-a35b-instruct) variants.

### Recommended Settings

`temperature=0.7`, `top_p=0.8`, `top_k=20`, `repetition_penalty=1.05`

- **Temperature** — 0.7
- **Top_K** — 20
- **Min_P** — 0.00 (optional; 0.01 works well; llama.cpp default is 0.1)
- **Top_P** — 0.8
- **Repetition Penalty** — 1.05
- **Context output** — 65,536 tokens recommended (can be increased)
- **Chat template** (rendered):

```
<|im_start|>user
Hey there!<|im_end|>
<|im_start|>assistant
What is 1+1?<|im_end|>
<|im_start|>user
2<|im_end|>
<|im_start|>assistant
```

- **Chat template** (raw with `\n`):

```
<|im_start|>user\nHey there!<|im_end|>\n<|im_start|>assistant\nWhat is 1+1?<|im_end|>\n<|im_start|>user\n2<|im_end|>\n<|im_start|>assistant\n
```

- **Chat template for tool calling** (example: get temperature in San Francisco):

```
<|im_start|>user
What's the temperature in San Francisco now? How about tomorrow?<|im_end|>
<|im_start|>assistant
<tool_call>\n<function=get_current_temperature>\n<parameter=location>\nSan Francisco, CA, USA
</parameter>\n</function>\n(${tool_call_id})<|im_end|>
<|im_start|>user
```json
{"temperature": 26.1, "location": "San Francisco, CA, USA", "unit": "celsius"}
```<|im_end|>
```

> [!info] Non-thinking model only
> This model does not generate `thought` blocks. Specifying `enable_thinking=False` is no longer required.

### Run Qwen3-Coder-30B-A3B-Instruct

For 6+ tok/s with UD-Q4_K_XL: **18GB unified memory** (VRAM+RAM) or **18GB RAM** alone. Rule of thumb: available memory should match or exceed model size (e.g. UD_Q8_K_XL at 32.5GB needs ~33GB).

> [!warning] Memory note
> Model can run on less memory but inference slows down. Maximum memory needed only for fastest speeds.

No need to set `thinking=False`; model does not generate thinking blocks.

> [!info] Same best practices apply as the 480B model above.

#### Ollama: Run Qwen3-Coder-30B-A3B-Instruct

1. Install ollama (models up to 32B only):

```bash
apt-get update
apt-get install pciutils -y
curl -fsSL https://ollama.com/install.sh | sh
```

2. Run the model (call `ollama serve` in another terminal if it fails; fixes and parameters included in `params`):

```bash
ollama run hf.co/unsloth/Qwen3-Coder-30B-A3B-Instruct-GGUF:UD-Q4_K_XL
```

#### Llama.cpp: Run Qwen3-Coder-30B-A3B-Instruct

1. Build llama.cpp. Set `-DGGML_CUDA=OFF` for CPU-only or Apple Mac/Metal (on by default):

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

2. Pull directly from HuggingFace:

```bash
./llama.cpp/llama-cli \
    -hf unsloth/Qwen3-Coder-30B-A3B-Instruct-GGUF:Q4_K_XL \
    --jinja -ngl 99 --ctx-size 32768 \
    --temp 0.7 --min-p 0.0 --top-p 0.80 --top-k 20 --repeat-penalty 1.05
```

3. Or download via Python (`pip install huggingface_hub hf_transfer`). If downloads get stuck, see [[124-basics-troubleshooting-and-faqs-hugging-face-hub-xet-debugging|HF XET debugging]]:

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/Qwen3-Coder-30B-A3B-Instruct-GGUF",
    local_dir = "unsloth/Qwen3-Coder-30B-A3B-Instruct-GGUF",
    allow_patterns = ["*UD-Q4_K_XL*"],
)
```

### Run Qwen3-Coder-480B-A35B-Instruct

For 6+ tok/s with 1-bit quant: **150GB unified memory** or **150GB RAM** alone. E.g. Q2_K_XL (180GB) needs ~180GB.

> [!warning] Memory note
> Model can run on less memory but inference slows down. Maximum memory needed only for fastest speeds.

> [!info] Same best practices apply as the 30B model above.

#### Llama.cpp: Run Qwen3-Coder-480B-A35B-Instruct

> [!tip] Full precision available
> Use `Q8_K_XL`, `Q8_0` or `BF16` checkpoints for full precision.

1. Build llama.cpp:

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

2. Pull directly:

```bash
./llama.cpp/llama-cli \
    -hf unsloth/Qwen3-Coder-480B-A35B-Instruct-GGUF:Q2_K_XL \
    --ctx-size 16384 \
    --n-gpu-layers 99 \
    -ot ".ffn_.*_exps.=CPU" \
    --temp 0.7 \
    --min-p 0.0 \
    --top-p 0.8 \
    --top-k 20 \
    --repeat-penalty 1.05
```

3. Or download via Python (`pip install huggingface_hub hf_transfer`):

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "0" # Can sometimes rate limit, so set to 0 to disable
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/Qwen3-Coder-480B-A35B-Instruct-GGUF",
    local_dir = "unsloth/Qwen3-Coder-480B-A35B-Instruct-GGUF",
    allow_patterns = ["*UD-Q2_K_XL*"],
)
```

4. Run in conversation mode.

5. Tuning flags:
   - `--threads -1` — CPU thread count
   - `--ctx-size 262114` — context length
   - `--n-gpu-layers 99` — GPU offloading layers (adjust if OOM; remove for CPU-only)

> [!tip] MoE offloading
> Use `-ot ".ffn_.*_exps.=CPU"` to offload all MoE layers to CPU, fitting non-MoE layers on 1 GPU. Customize the regex if you have more GPU capacity. See [Improving generation speed](#improving-generation-speed).

```bash
./llama.cpp/llama-cli \
    --model unsloth/Qwen3-Coder-480B-A35B-Instruct-GGUF/UD-Q2_K_XL/Qwen3-Coder-480B-A35B-Instruct-UD-Q2_K_XL-00001-of-00004.gguf \
    --ctx-size 16384 \
    --n-gpu-layers 99 \
    -ot ".ffn_.*_exps.=CPU" \
    --temp 0.7 \
    --min-p 0.0 \
    --top-p 0.8 \
    --top-k 20 \
    --repeat-penalty 1.05
```

> [!tip] Qwen3 update
> Run [[048-models-tutorials-qwen3-next|Qwen3-235B-A22B-Instruct-2507]] locally with llama.cpp.

#### Improving Generation Speed

With more VRAM, offload more MoE layers or whole layers:

- `-ot ".ffn_.*_exps.=CPU"` — all MoE layers to CPU (fits non-MoE on 1 GPU)
- `-ot ".ffn_(up|down)_exps.=CPU"` — up and down projection MoE layers only (more GPU mem needed)
- `-ot ".ffn_(up)_exps.=CPU"` — up projection MoE layers only (most GPU mem)
- `-ot "\.(6|7|8|9|[0-9][0-9]|[0-9][0-9][0-9])\.ffn_(gate|up|down)_exps.=CPU"` — gate/up/down MoE from layer 6 onwards (customizable)

The [latest llama.cpp release](https://github.com/ggml-org/llama.cpp/pull/14363) introduces high throughput mode via `llama-parallel` ([docs](https://github.com/ggml-org/llama.cpp/tree/master/examples/parallel)). You can also **quantize KV cache to 4bits** to reduce VRAM/RAM movement and speed up generation.

#### How to Fit Long Context (256K to 1M)

Use **KV cache quantization** to quantize K and V caches to lower bits, reducing memory and potentially increasing speed.

K quantization options (default `f16`): `f32, f16, bf16, q8_0, q4_0, q4_1, iq4_nl, q5_0, q5_1`

Use `_1` variants (e.g. `q4_1, q5_1`) for somewhat increased accuracy (slightly slower).

For V cache quantization, compile llama.cpp with Flash Attention: `-DGGML_CUDA_FA_ALL_QUANTS=ON`, then use `--flash-attn`.

1M context GGUFs via YaRN scaling: [uploaded here](https://app.gitbook.com/o/HpyELzcNe0topgVLGCZY/s/xhOjnexMCB3dmuQFQ2Zq/).

## Tool Calling Fixes

Tool-calling fixed via `llama.cpp --jinja` for `llama-server`. 30B-A3B quants already include fixes. For 480B-A35B:

1. Download the first file at `https://huggingface.co/unsloth/Qwen3-Coder-480B-A35B-Instruct-GGUF/tree/main/UD-Q2_K_XL` for UD-Q2_K_XL, and replace your current file
2. Or use `snapshot_download` as usual — will auto-override old files
3. Use new chat template via `--chat-template-file`: see [GGUF chat template](https://huggingface.co/unsloth/Qwen3-Coder-480B-A35B-Instruct-GGUF?chat_template=default) or [chat_template.jinja](https://huggingface.co/unsloth/Qwen3-Coder-480B-A35B-Instruct-GGUF/blob/main/chat_template.jinja)
4. Single 150GB UD-IQ1_M file for Ollama: `https://huggingface.co/unsloth/Qwen3-Coder-480B-A35B-Instruct-GGUF/blob/main/Qwen3-Coder-480B-A35B-Instruct-UD-IQ1_M.gguf`

Resolves: <https://github.com/ggml-org/llama.cpp/issues/14915>

### Using Tool Calling

Example: a `get_current_temperature` function (placeholder returning 26.1C):

```python
def get_current_temperature(location: str, unit: str = "celsius"):
    """Get current temperature at a location.

    Args:
        location: The location to get the temperature for, in the format "City, State, Country".
        unit: The unit to return the temperature in. Defaults to "celsius". (choices: ["celsius", "fahrenheit"])

    Returns:
        the temperature, the location, and the unit in a dict
    """
    return {
        "temperature": 26.1, # PRE_CONFIGURED -> you change this!
        "location": location,
        "unit": unit,
    }
```

Build the full prompt with the tokenizer:

```python
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("unsloth/Qwen3-Coder-480B-A35B-Instruct")

messages = [
    {'role': 'user', 'content': "What's the temperature in San Francisco now? How about tomorrow?"},
    {'content': "", 'role': 'assistant', 'function_call': None, 'tool_calls': [
        {'id': 'ID', 'function': {'arguments': {"location": "San Francisco, CA, USA"}, 'name': 'get_current_temperature'}, 'type': 'function'},
    ]},
    {'role': 'tool', 'content': '{"temperature": 26.1, "location": "San Francisco, CA, USA", "unit": "celsius"}', 'tool_call_id': 'ID'},
]

prompt = tokenizer.apply_chat_template(messages, tokenize = False)
```

## Performance Benchmarks

> [!info] Benchmarks are for full BF16 checkpoint. Use `Q8_K_XL`, `Q8_0`, `BF16` checkpoints. MoE offloading tricks also work for these versions.

### Agentic Coding

| Benchmark | Qwen3-Coder 480B-A35B-Instruct | Kimi-K2 | DeepSeek-V3-0324 | Claude 4 Sonnet | GPT-4.1 |
|---|---|---|---|---|---|
| Terminal-Bench | **37.5** | 30.0 | 2.5 | 35.5 | 25.3 |
| SWE-bench Verified w/ OpenHands (500 turns) | **69.6** | - | - | 70.4 | - |
| SWE-bench Verified w/ OpenHands (100 turns) | **67.0** | 65.4 | 38.8 | 68.0 | 48.6 |
| SWE-bench Verified w/ Private Scaffolding | - | 65.8 | - | 72.7 | 63.8 |
| SWE-bench Live | **26.3** | 22.3 | 13.0 | 27.7 | - |
| SWE-bench Multilingual | **54.7** | 47.3 | 13.0 | 53.3 | 31.5 |
| Multi-SWE-bench mini | **25.8** | 19.8 | 7.5 | 24.8 | - |
| Multi-SWE-bench flash | **27.0** | 20.7 | - | 25.0 | - |
| Aider-Polyglot | **61.8** | 60.0 | 56.9 | 56.4 | 52.4 |
| Spider2 | **31.1** | 25.2 | 12.8 | 31.1 | 16.5 |

### Agentic Browser Use

| Benchmark | Qwen3-Coder 480B-A35B-Instruct | Kimi-K2 | DeepSeek-V3-0324 | Claude Sonnet-4 | GPT-4.1 |
|---|---|---|---|---|---|
| WebArena | **49.9** | 47.4 | 40.0 | 51.1 | 44.3 |
| Mind2Web | **55.8** | 42.7 | 36.0 | 47.4 | 49.6 |

### Agentic Tool-Use

| Benchmark | Qwen3-Coder 480B-A35B-Instruct | Kimi-K2 | DeepSeek-V3-0324 | Claude Sonnet-4 | GPT-4.1 |
|---|---|---|---|---|---|
| BFCL-v3 | **68.7** | 65.2 | 56.9 | 73.3 | 62.9 |
| TAU-Bench Retail | **77.5** | 70.7 | 59.1 | 80.5 | - |
| TAU-Bench Airline | **60.0** | 53.5 | 40.0 | 60.0 | - |

#qwen3-coder #local-inference #llama-cpp #ollama #gguf
