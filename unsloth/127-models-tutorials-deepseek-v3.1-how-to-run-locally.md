---
title: 'DeepSeek-V3.1: How to Run Locally'
url: https://unsloth.ai/docs/models/tutorials/deepseek-v3.1-how-to-run-locally.md
source: llms
fetched_at: 2026-04-27T18:14:22.518979215-03:00
rendered_js: false
word_count: 1835
summary: Guide for running DeepSeek-V3.1 LLM locally across various platforms with specific settings for optimal performance.
tags:
    - deepseek-v3.1
    - gguf-quantization
    - local-inference
    - ollama-setup
    - chat-template
    - llm-guide
category: guide
optimized: true
optimized_at: 2026-04-27T21:27:00Z
---

# DeepSeek-V3.1: How to Run Locally

DeepSeek V3.1 and **Terminus** update: hybrid reasoning inference (think + non-think in one model). Full 671B params = 715GB disk. Quantized dynamic 2-bit = 245GB (-75%).

- GGUF: [**DeepSeek-V3.1-GGUF**](https://huggingface.co/unsloth/DeepSeek-V3.1-GGUF)
- Terminus GGUF: [**DeepSeek-V3.1-Terminus-GGUF**](https://huggingface.co/unsloth/DeepSeek-V3.1-Terminus-GGUF)
- Dynamic 3-bit V3.1 GGUF scores **75.6%** on Aider Polyglot, surpassing many full-precision SOTA LLMs ([read more](https://unsloth.ai/docs/basics/unsloth-dynamic-2.0-ggufs/unsloth-dynamic-ggufs-on-aider-polyglot))

All uploads use Unsloth [Dynamic 2.0](https://unsloth.ai/docs/basics/unsloth-dynamic-2.0-ggufs) for SOTA 5-shot MMLU and KL Divergence performance. GGUFs include Unsloth [chat template fixes](#chat-template-bug-fixes) for llama.cpp backends.

## Recommended Settings

TQ1\_0 (1-bit dynamic quant: 1bit unimportant MoE, 2-4bit important MoE, 6-8bit rest) = 170GB. Works on **1x24GB GPU + 128GB RAM** with MoE offloading. **Works natively in Ollama.**

> [!info] llama.cpp requires `--jinja`
> You must use `--jinja` for llama.cpp quants to enable the fixed chat templates. Incorrect results without it.

2-bit quants fit 1x24GB GPU (MoE offloaded to RAM), ~5 tok/s with 128GB RAM. Recommend 226GB+ unified memory (RAM+VRAM) for 5+ tok/s.

> [!tip] Memory rule
> For best performance, VRAM + RAM should equal the quant download size. If not, SSD offloading works via llama.cpp but inference is slower.

## Chat Template Bug Fixes

Fixed issues with DeepSeek V3.1's chat template in llama.cpp and other engines:

1. **Hybrid reasoning keyword**: Template used `thinking = True` but other models use `enable_thinking = True`. Added `enable_thinking` as alias.
2. **minja `.split()` fix**: llama.cpp's jinja renderer ([minja](https://github.com/google/minja)) doesn't allow extra arguments in `.split()`. Python `.split(text, 1)` fails in minja with:
   ```
   terminate called after throwing an instance of 'std::runtime_error' what(): split method must have between 1 and 1 positional arguments and between 0 and 0 keyword arguments at row 3, column 1908
   ```
   Fixed in all Unsloth quants.

### Official Recommended Settings

Per [DeepSeek](https://huggingface.co/deepseek-ai/DeepSeek-V3.1):

- **Temperature**: 0.6 (reduce repetition)
- **top_p**: 0.95
- **Context length**: 128K max
- **llama.cpp**: use `--jinja` (includes chat template fixes)
- **Reasoning mode**: `enable_thinking = True` (default: non-reasoning)

#### Chat Template / Prompt Format

No need to force `甄\n`; prefix alone triggers non-thinking mode. Unlike V3, V3.1 adds token `凝`.

```
<｜begin▁of▁sentence｜>{system prompt}<｜User｜>{query}<｜Assistant｜>凝
```

BOS is forcibly added; EOS separates each interaction. Use `tokenizer.encode(..., add_special_tokens = False)` to avoid double BOS. For llama.cpp/GGUF, skip BOS (auto-added).

#### Non-Thinking Mode (`thinking = False` / `enable_thinking = False`, default)

**First-Turn**

Prefix: `<｜begin▁of▁sentence｜>{system prompt}<｜User｜>{query}<｜Assistant｜>凝`

Generates non-thinking responses. Introduces additional token `凝` vs V3.

**Multi-Turn**

- Context: `<｜begin▁of▁sentence｜>{system prompt}<｜User｜>{query}<｜Assistant｜>凝{response}<｜end▁of▁sentence｜>...<｜User｜>{query}<｜Assistant｜>凝{response}<｜end▁of▁sentence｜>`
- Prefix: `<｜User｜>{query}<｜Assistant｜>凝`

Concatenate context + prefix for correct prompt.

#### Thinking Mode (`thinking = True` / `enable_thinking = True`)

**First-Turn**

Prefix: `<｜begin▁of▁sentence｜>{system prompt}<｜User｜>{query}<｜Assistant｜>甄`

Similar to DeepSeek-R1.

**Multi-Turn**

- Context: `<｜begin▁of▁sentence｜>{system prompt}<｜User｜>{query}<｜Assistant｜>凝{response}<｜end▁of▁sentence｜>...<｜User｜>{query}<｜Assistant｜>凝{response}<｜end▁of▁sentence｜>`
- Prefix: `<｜User｜>{query}<｜Assistant｜>甄`

Multi-turn context same as non-thinking. Thinking token dropped in last turn; `凝` retained in every context turn.

#### Tool Calling

Supported in non-thinking mode only:

`<｜begin▁of▁sentence｜>{system prompt}{tool_description}<｜User｜>{query}<｜Assistant｜>凝`

Populate `tool_description` after system prompt.

## Run DeepSeek-V3.1 Tutorials

### Run in Ollama/Open WebUI

1. Install Ollama:

```bash
apt-get update
apt-get install pciutils -y
curl -fsSL https://ollama.com/install.sh | sh
```

2. Run the model (call `ollama serve` in another terminal if it fails). For full Terminus TQ1\_0 (170GB):

```bash
OLLAMA_MODELS=unsloth ollama serve &

OLLAMA_MODELS=unsloth ollama run hf.co/unsloth/DeepSeek-V3.1-Terminus-GGUF:TQ1_0
```

3. For other quants, merge GGUF split files first:

```bash
./llama.cpp/llama-gguf-split --merge \
  DeepSeek-V3.1-Terminus-GGUF/DeepSeek-V3.1-Terminus-UD-Q2_K_XL/DeepSeek-V3.1-Terminus-UD-Q2_K_XL-00001-of-00006.gguf \
	merged_file.gguf
```

```bash
OLLAMA_MODELS=unsloth ollama serve &

OLLAMA_MODELS=unsloth ollama run merged_file.gguf
```

4. Open WebUI [step-by-step tutorial](https://docs.openwebui.com/tutorials/integrations/deepseekr1-dynamic/) for R1; replace R1 with V3.1 quant for V3.1.

### Run in llama.cpp

1. Build llama.cpp from [GitHub](https://github.com/ggml-org/llama.cpp). Use `-DGGML_CUDA=OFF` for CPU-only:

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggerganov/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-quantize llama-cli llama-gguf-split llama-mtmd-cli llama-server
cp llama.cpp/build/bin/llama-* llama.cpp
```

2. Run directly via HF (use `export LLAMA_CACHE="folder"` to force save location; max 128K context):

> [!tip] MoE offloading regex options
> `-ot ".ffn_.*_exps.=CPU"` — offload all MoE layers to CPU (least VRAM, fits non-MoE on 1 GPU)
> `-ot ".ffn_(up|down)_exps.=CPU"` — offload up + down projection MoE only
> `-ot ".ffn_(up)_exps.=CPU"` — offload only up projection MoE (most VRAM)
> `-ot "\.(6|7|8|9|[0-9][0-9]|[0-9][0-9][0-9])\.ffn_(gate|up|down)_exps.=CPU"` — gate/up/down MoE from layer 6+

```bash
export LLAMA_CACHE="unsloth/DeepSeek-V3.1-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/DeepSeek-V3.1-Terminus-GGUF:UD-Q2_K_XL \
    --jinja \
    --n-gpu-layers 99 \
    --temp 0.6 \
    --top-p 0.95 \
    --min-p 0.01 \
    --ctx-size 16384 \
    --seed 3407 \
    -ot ".ffn_.*_exps.=CPU"
```

3. Download via Python (`pip install huggingface_hub hf_transfer`):

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "0" # Can sometimes rate limit, so set to 0 to disable
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/DeepSeek-V3.1-Terminus-GGUF",
    local_dir = "unsloth/DeepSeek-V3.1-Terminus-GGUF",
    allow_patterns = ["*UD-Q2_K_XL*"], # Dynamic 2bit Use "*UD-TQ1_0*" for Dynamic 1bit
)
```

   Recommended: **UD-Q2_K_XL** (2.7-bit dynamic quant) for size/accuracy balance.

4. Adjust `--threads 32` (CPU threads), `--ctx-size 16384` (context), `--n-gpu-layers 2` (GPU offload layers). Remove GPU flags for CPU-only:

```bash
./llama.cpp/llama-cli \
    --model unsloth/DeepSeek-V3.1-Terminus-GGUF/UD-Q2_K_XL/DeepSeek-V3.1-Terminus-UD-Q2_K_XL-00001-of-00006.gguf \
    --jinja \
    --n-gpu-layers 99 \
    --temp 0.6 \
    --top-p 0.95 \
    --min-p 0.01 \
    --ctx-size 16384 \
    --seed 3407 \
    -ot ".ffn_.*_exps.=CPU"
```

5. 1-bit version (170GB) for limited RAM/VRAM:

```python
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/DeepSeek-V3.1-Terminus-GGUF",
    local_dir = "unsloth/DeepSeek-V3.1-Terminus-GGUF",
    allow_patterns = ["*UD-TQ1_0*"], # Use "*UD-Q2_K_XL*" for Dynamic 2bit
)
```

### Deploy with llama-server and OpenAI's completion library

```bash
./llama.cpp/llama-server \
    --model unsloth/DeepSeek-V3.1-Terminus-GGUF/DeepSeek-V3.1-Terminus-UD-TQ1_0.gguf \
    --alias "unsloth/DeepSeek-V3.1-Terminus" \
    --n-gpu-layers 999 \
    -ot ".ffn_.*_exps.=CPU" \
    --prio 3 \
    --min_p 0.01 \
    --ctx-size 16384 \
    --port 8001 \
    --jinja
```

OpenAI Python client (`pip install openai`):

```python
from openai import OpenAI
import json
openai_client = OpenAI(
    base_url = "http://127.0.0.1:8001/v1",
    api_key = "sk-no-key-required",
)
completion = openai_client.chat.completions.create(
    model = "unsloth/DeepSeek-V3.1-Terminus",
    messages = [{"role": "user", "content": "What is 2+2?"},],
)
print(completion.choices[0].message.content)
```

## Model Uploads

All uploads (including non-imatrix/non-dynamic) use Unsloth calibration dataset optimized for conversational, coding, and language tasks.

Also: [IQ4\_NL](https://huggingface.co/unsloth/DeepSeek-V3.1-GGUF/tree/main/IQ4_NL) (faster on ARM) and [Q4\_1](https://huggingface.co/unsloth/DeepSeek-V3.1-GGUF/tree/main/Q4_1) (faster on Apple).

| MoE Bits | Type + Link | Disk Size | Details |
|----------|-------------|-----------|---------|
| 1.66bit | [TQ1_0](https://huggingface.co/unsloth/DeepSeek-V3.1-GGUF?show_file_info=DeepSeek-V3.1-UD-TQ1_0.gguf) | **170GB** | 1.92/1.56bit |
| 1.78bit | [IQ1_S](https://huggingface.co/unsloth/DeepSeek-V3.1-GGUF/tree/main/UD-IQ1_S) | **185GB** | 2.06/1.56bit |
| 1.93bit | [IQ1_M](https://huggingface.co/unsloth/DeepSeek-V3.1-GGUF/tree/main/UD-IQ1_M) | **200GB** | 2.5/2.06/1.56 |
| 2.42bit | [IQ2_XXS](https://huggingface.co/unsloth/DeepSeek-V3.1-GGUF/tree/main/UD-IQ2_XXS) | **216GB** | 2.5/2.06bit |
| 2.71bit | [Q2_K_XL](https://huggingface.co/unsloth/DeepSeek-V3.1-GGUF/tree/main/UD-Q2_K_XL) | **251GB** | 3.5/2.5bit |
| 3.12bit | [IQ3_XXS](https://huggingface.co/unsloth/DeepSeek-V3.1-GGUF/tree/main/UD-IQ3_XXS) | **273GB** | 3.5/2.06bit |
| 3.5bit | [Q3_K_XL](https://huggingface.co/unsloth/DeepSeek-V3.1-GGUF/tree/main/UD-Q3_K_XL) | **296GB** | 4.5/3.5bit |
| 4.5bit | [Q4_K_XL](https://huggingface.co/unsloth/DeepSeek-V3.1-GGUF/tree/main/UD-Q4_K_XL) | **384GB** | 5.5/4.5bit |
| 5.5bit | [Q5_K_XL](https://huggingface.co/unsloth/DeepSeek-V3.1-GGUF/tree/main/UD-Q5_K_XL) | **481GB** | 6.5/5.5bit |

Also available: [BF16](https://huggingface.co/unsloth/DeepSeek-V3.1-BF16) and [FP8](https://huggingface.co/unsloth/DeepSeek-V3.1).

## Improving Generation Speed

More VRAM = offload more MoE layers or whole layers.

- **All MoE to CPU**: `-ot ".ffn_.*_exps.=CPU"` (fits non-MoE on 1 GPU)
- **Up+down projection MoE**: `-ot ".ffn_(up|down)_exps.=CPU"`
- **Up projection only**: `-ot ".ffn_(up)_exps.=CPU"` (needs most VRAM)
- **Custom**: `-ot "\.(6|7|8|9|[0-9][0-9]|[0-9][0-9][0-9])\.ffn_(gate|up|down)_exps.=CPU"` (layer 6+)

[Latest llama.cpp](https://github.com/ggml-org/llama.cpp/pull/14363) introduces high throughput mode via `llama-parallel` ([docs](https://github.com/ggml-org/llama.cpp/tree/master/examples/parallel)). Also: **quantize KV cache to 4bits** to reduce VRAM/RAM movement.

## How to Fit Long Context (Full 128K)

Use **KV cache quantization** to quantize K/V caches to lower bits. Reduces RAM/VRAM data movement and can increase generation speed.

**K cache options** (`--cache-type-k`, default `f16`): `f32, f16, bf16, q8_0, q4_0, q4_1, iq4_nl, q5_0, q5_1`

Use `_1` variants (e.g., `q4_1, q5_1`) for slightly better accuracy at slight speed cost.

**V cache options** (`--cache-type-v`): same types as K. Requires compiling llama.cpp with Flash Attention support (`-DGGML_CUDA_FA_ALL_QUANTS=ON`) and `--flash-attn` flag.

---

# Agent Instructions: Querying This Documentation

If you need additional information not on this page, query dynamically:

```
GET https://unsloth.ai/docs/models/tutorials/deepseek-v3.1-how-to-run-locally.md?ask=<question>
```

Question should be specific, self-contained, natural language. Returns direct answer with relevant excerpts and sources.

#deepseek-v3.1 #gguf-quantization #local-inference #ollama #chat-template
