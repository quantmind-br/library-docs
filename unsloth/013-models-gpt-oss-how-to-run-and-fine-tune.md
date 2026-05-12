---
title: 'gpt-oss: How to Run Guide'
url: https://unsloth.ai/docs/models/gpt-oss-how-to-run-and-fine-tune.md
source: llms
fetched_at: 2026-04-27T18:13:47.534642765-03:00
rendered_js: false
word_count: 3045
summary: This guide explains how users can run and fine-tune the state-of-the-art open language models, gpt-oss-120b and gpt-oss-20b, using Unsloth. It also details important implementation specifics like chat template fixes and precision handling for optimal performance.
tags:
    - gpt-oss
    - unsloth
    - model-guide
    - fine-tuning
    - chat-template
    - inference
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# gpt-oss: How to Run Guide

OpenAI released **gpt-oss-120b** and **gpt-oss-20b** (Apache 2.0). Both 128k context models outperform similarly sized open models in reasoning, tool use, and agentic tasks. Run & fine-tune locally with Unsloth.

- [Fine-tune gpt-oss-20b (Colab)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-\(20B\)-Fine-tuning.ipynb) — free notebook
- [[012-models-gpt-oss-how-to-run-and-fine-tune-tutorial-how-to-fine-tune-gpt-oss|Fine-tune tutorial]]
- [gpt-oss RL guide](https://unsloth.ai/docs/models/gpt-oss-how-to-run-and-fine-tune/gpt-oss-reinforcement-learning)

Trained with [[072-get-started-reinforcement-learning-rl-guide|RL]], **gpt-oss-120b** rivals o4-mini and **gpt-oss-20b** rivals o3-mini. Both excel at function calling and CoT reasoning, surpassing o1 and GPT-4o.

For best performance, total available memory (unified + VRAM + RAM) should exceed the quantized model file size. If not, llama.cpp can run via SSD/HDD offloading (slower inference).

### Unsloth GGUFs

> [!tip] Includes Unsloth's [chat template fixes](#unsloth-fixes-for-gpt-oss). Use our uploads & train with Unsloth for best results.

- **20B**: [unsloth/gpt-oss-20b-GGUF](https://huggingface.co/unsloth/gpt-oss-20b-GGUF)
- **120B**: [unsloth/gpt-oss-120b-GGUF](https://huggingface.co/unsloth/gpt-oss-120b-GGUF)

## Unsloth fixes for gpt-oss

> [!info] Some fixes were pushed upstream to OpenAI's official Hugging Face model. [See discussion](https://huggingface.co/openai/gpt-oss-20b/discussions/94/files)

OpenAI released [Harmony](https://github.com/openai/harmony), a standalone parsing/tokenization library for gpt-oss conversations. Inference engines use jinja chat templates instead. We found discrepancies between Harmony's output and current jinja templates.

Unsloth provides `encode_conversations_with_harmony` to use Harmony directly:

```python
messages = [
    {"role" : "user", "content" : "What is 1+1?"},
    {"role" : "assistant", "content" : "2"},
    {"role": "user",  "content": "What's the temperature in San Francisco now? How about tomorrow? Today's date is 2024-09-30."},
    {"role": "assistant",  "content": "User asks: 'What is the weather in San Francisco?' We need to use get_current_temperature tool.", "thinking" : ""},
    {"role": "assistant", "content": "", "tool_calls": [{"name": "get_current_temperature", "arguments": '{"location": "San Francisco, California, United States", "unit": "celsius"}'}]},
    {"role": "tool", "name": "get_current_temperature", "content": '{"temperature": 19.9, "location": "San Francisco, California, United States", "unit": "celsius"}'},
]
```

```python
from unsloth_zoo import encode_conversations_with_harmony

def encode_conversations_with_harmony(
    messages,
    reasoning_effort = "medium",
    add_generation_prompt = True,
    tool_calls = None,
    developer_instructions = None,
    model_identity = "You are ChatGPT, a large language model trained by OpenAI.",
)
```

**Harmony format features:**

1. `reasoning_effort = "medium"` — select low/medium/high; controls reasoning budget (higher = better accuracy)
2. `developer_instructions` — system prompt equivalent
3. `model_identity` — best left as default; custom values untested

**Jinja chat template issues found (multiple implementations exist):**

1. Function/tool calls rendered with `tojson` — fine for dicts but **backslashes symbols** in strings
2. **Extra newlines** on some boundaries
3. Tool calling thoughts should use **`analysis` tag, not `final` tag**
4. Some templates don't use `<|channel|>final` for the final assistant message (required; not for thinking traces/tool calls)

Our GGUF, BnB, and BF16 uploads have fixed chat templates — zero character difference vs Harmony.

### Precision issues

Model trained in BF16; Tesla T4 and float16 machines hit outliers/overflows. MXFP4 not natively supported on Ampere+ older GPUs — Triton provides `tl.dot_scaled` which upcasts to BF16 internally.

- [MXFP4 inference notebook (Tesla T4 Colab)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/GPT_OSS_MXFP4_\(20B\)-Inference.ipynb)

> [!info] [Software emulation](https://triton-lang.org/main/python-api/generated/triton.language.dot_scaled.html) enables targeting hardware without native microscaling support. Microscaled lhs/rhs are upcasted to `bf16` beforehand for dot computation.

**Fixes applied:**

- float16 autocast causes infinities over time — do MoE in bfloat16 (or float32 on T4)
- All operation precisions (including router) set to float32 for float16 machines

## Running gpt-oss

> [!info] Any quant smaller than F16 (including 2-bit) has minimal accuracy loss — only some layers (e.g. attention) are lower bit while most stay full-precision. Sizes are close to F16 (e.g. 2-bit = 11.5 GB vs F16 = 14 GB). Once llama.cpp supports better quantization, new uploads will follow.

**Reasoning effort** — adjustable trade-off between performance and latency (token budget for thinking):

- **Low** — fast responses, simple tasks
- **Medium** — balanced performance/speed
- **High** — strongest reasoning, higher latency

### Recommended Settings

| Parameter | Value |
|---|---|
| temperature | 1.0 |
| top_p | 1.0 |
| top_k | 0 (or experiment with 100) |
| Min context | 16,384 |
| Max context | 131,072 |

**Chat template:**

```
<|start|>system<|message|>You are ChatGPT, a large language model trained by OpenAI.\nKnowledge cutoff: 2024-06\nCurrent date: 2025-08-05\n\nReasoning: medium\n\n# Valid channels: analysis, commentary, final. Channel must be included for every message.<|end|><|start|>user<|message|>Hello<|end|><|start|>assistant<|channel|>final<|message|>Hi there!<|end|><|start|>user<|message|>What is 1+1?<|end|><|start|>assistant
```

**EOS token:** `<|return|>`

### Run gpt-oss-20B

6+ tok/s for Dynamic 4-bit quant requires **14GB unified memory** (or 14GB RAM alone). GGUF: [unsloth/gpt-oss-20b-GGUF](https://huggingface.co/unsloth/gpt-oss-20b-GGUF)

> [!info] Model can run on less memory but inference slows. Max memory needed for fastest speeds. Same [best practices](#recommended-settings) as 120B.

#### Unsloth Studio

1. **Install** — MacOS, Linux, WSL:

```bash
curl -fsSL https://unsloth.ai/install.sh | sh
```

   Windows PowerShell:

```bash
irm https://unsloth.ai/install.ps1 | iex
```

2. **Launch** — MacOS, Linux, WSL, Windows:

```bash
unsloth studio -H 0.0.0.0 -p 8888
```

   Open `http://localhost:8888`

3. **Search & download** — Go to [Studio Chat](https://unsloth.ai/docs/new/studio/chat), search "gpt-oss", download desired model/quant
4. **Run** — Inference parameters auto-set; see [[099-new-studio-chat|Studio inference guide]] for details

#### Docker

```bash
docker model run hf.co/unsloth/gpt-oss-20b-GGUF:F16
```

#### llama.cpp

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

2. Run directly from Hugging Face:

```bash
./llama.cpp/llama-cli \
    -hf unsloth/gpt-oss-20b-GGUF:F16 \
    --jinja -ngl 99 --ctx-size 16384 \
    --temp 1.0 --top-p 1.0 --top-k 0
```

3. Download via Python:

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/gpt-oss-20b-GGUF",
    local_dir = "unsloth/gpt-oss-20b-GGUF",
    allow_patterns = ["*F16*"],
)
```

If downloads get stuck, see [[124-basics-troubleshooting-and-faqs-hugging-face-hub-xet-debugging|HF XET debugging]].

### Run gpt-oss-120B

6+ tok/s for 1-bit quant requires **66GB unified memory** (or 66GB RAM alone). GGUF: [unsloth/gpt-oss-120b-GGUF](https://huggingface.co/unsloth/gpt-oss-120b-GGUF)

> [!info] Same [best practices](#recommended-settings) as 20B. Model can run on less memory (slower inference).

#### Unsloth Studio

1. **Install** — same commands as 20B above
2. **Setup** (one-time) — auto-installs Node.js (nvm), builds frontend, Python deps, and llama.cpp with CUDA

> [!warning] First install may take 5-10 minutes (llama.cpp binary compilation). Do not cancel.

> [!info] WSL users: prompted for `sudo` password for build dependencies (`cmake`, `git`, `libcurl4-openssl-dev`).

3. **Launch** — MacOS, Linux, WSL:

```bash
source unsloth_studio/bin/activate
unsloth studio -H 0.0.0.0 -p 8888
```

   Windows PowerShell:

```bash
& .\unsloth_studio\Scripts\unsloth.exe studio -H 0.0.0.0 -p 8888
```

   Open `http://localhost:8888`

4. **Search & download** — Go to [Studio Chat](https://unsloth.ai/docs/new/studio/chat), search "gpt-oss", download desired model/quant
5. **Run** — Inference parameters auto-set; see [[099-new-studio-chat|Studio inference guide]] for details

#### llama.cpp

> [!tip] For full precision unquantized, use `F16` versions.

1. Build llama.cpp (same as 20B)
2. Run directly from Hugging Face:

```bash
./llama.cpp/llama-cli \
    -hf unsloth/gpt-oss-120b-GGUF:F16 \
    --ctx-size 16384 \
    --n-gpu-layers 99 \
    -ot ".ffn_.*_exps.=CPU" \
    --temp 1.0 \
    --min-p 0.0 \
    --top-p 1.0 \
    --top-k 0.0 \
```

3. Download via Python:

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "0" # Disable if rate-limited
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/gpt-oss-120b-GGUF",
    local_dir = "unsloth/gpt-oss-120b-GGUF",
    allow_patterns = ["*F16*"],
)
```

4. Run with local file:

```bash
./llama.cpp/llama-cli \
    --model unsloth/gpt-oss-120b-GGUF/gpt-oss-120b-F16.gguf \
    --ctx-size 16384 \
    --n-gpu-layers 99 \
    -ot ".ffn_.*_exps.=CPU" \
    --temp 1.0 \
    --min-p 0.0 \
    --top-p 1.0 \
    --top-k 0.0 \
```

5. Tuning: `--threads -1` (CPU threads), `--ctx-size 262114` (context length), `--n-gpu-layers 99` (GPU offload). Remove if CPU-only inference.

> [!tip] Use `-ot ".ffn_.*_exps.=CPU"` to offload all MoE layers to CPU — fits all non-MoE layers on 1 GPU. Customize the regex if you have more GPU capacity. See [improving generation speed](#improving-generation-speed).

### Improving generation speed

With more VRAM, offload fewer MoE layers or whole layers:

- `-ot ".ffn_.*_exps.=CPU"` — offload all MoE layers (least VRAM, baseline)
- `-ot ".ffn_(up|down)_exps.=CPU"` — offload up + down projection MoE layers only (more VRAM needed)
- `-ot ".ffn_(up)_exps.=CPU"` — offload only up projection MoE layers (most VRAM needed)
- Custom regex: `-ot "\.(6|7|8|9|[0-9][0-9]|[0-9][0-9][0-9])\.ffn_(gate|up|down)_exps.=CPU"` — offloads gate/up/down MoE layers from layer 6 onward

Latest llama.cpp: high throughput mode via `llama-parallel` ([read more](https://github.com/ggml-org/llama.cpp/tree/master/examples/parallel)). Also: **quantize KV cache to 4bits** to reduce VRAM/RAM movement.

## Fine-tuning gpt-oss with Unsloth

> [!tip] Aug 28 update: You can now export/save QLoRA fine-tuned gpt-oss to llama.cpp, vLLM, HF etc. [Unsloth Flex Attention](https://unsloth.ai/docs/models/long-context-gpt-oss-training#introducing-unsloth-flex-attention-support) enables >8x longer context, >50% less VRAM, >1.5x faster training.

Unsloth gpt-oss fine-tuning: 1.5x faster, 70% less VRAM, 10x longer context lengths.

| Method | gpt-oss-20B | gpt-oss-120B |
|---|---|---|
| QLoRA | 14 GB VRAM | 65 GB VRAM |
| BF16 LoRA | 44 GB VRAM | 210 GB VRAM |

See [[012-models-gpt-oss-how-to-run-and-fine-tune-tutorial-how-to-fine-tune-gpt-oss|Fine-tune tutorial]]

Free notebooks:
- gpt-oss-20b [Reasoning + Conversational](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-\(20B\)-Fine-tuning.ipynb)

### Reinforcement Learning (GRPO)

Unsloth supports RL for gpt-oss. See [gpt-oss RL guide](https://unsloth.ai/docs/models/gpt-oss-how-to-run-and-fine-tune/gpt-oss-reinforcement-learning).

| Notebook | Link |
|---|---|
| 2048 (Official OpenAI) | [Colab](https://colab.research.google.com/github/openai/gpt-oss/blob/main/examples/reinforcement-fine-tuning.ipynb) |
| Kernel generation (Unsloth) | [Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-\(20B\)-GRPO.ipynb) |

### Saving to GGUF, vLLM after training

QLoRA fine-tuned gpt-oss can now be exported to **llama.cpp**, **vLLM**, or **HF** — not just Unsloth. Previously restricted to Unsloth only. On-demand MXFP4 dequantization during LoRA merge enables **bf16 export**.

Merge and save locally:

```python
model.save_pretrained_merged(save_directory, tokenizer)
```

Merge and push to HF Hub:

```python
model.push_to_hub_merged(repo_name, tokenizer=tokenizer, token=hf_token)
```

### Efficient gpt-oss fine-tuning

MXFP4 does not natively support training. Unsloth works around this by mimicking MXFP4 via `Bitsandbytes` NF4 quantization for training, while using OpenAI's Triton Kernels for inference.

- Training other libraries require upcasting weights to bf16 — **300% more memory usage** and significantly longer training
- Unsloth: 20b model trains in **14 GB VRAM** (-80% vs other methods' 65 GB minimum)

Both models use MoE architecture: 20B selects 4/32 experts, 120B selects 4/128 per token. Weights stored in MXFP4 as `nn.Parameter` objects, converted to `nn.Linear` layers for BitsandBytes compatibility (slight slowdown, enables limited-VRAM fine-tuning).

### Datasets fine-tuning guide

gpt-oss supports reasoning datasets natively. Non-reasoning datasets work but may affect reasoning ability. To maintain reasoning:

- Use **75% reasoning + 25% non-reasoning** in your dataset
- Our Conversational notebook uses Hugging Face's Multilingual-Thinking dataset (4 languages)

---

# Agent Instructions: Querying This Documentation

If you need additional information not directly available on this page, query the documentation dynamically:

```
GET https://unsloth.ai/docs/models/gpt-oss-how-to-run-and-fine-tune.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language. The response will contain a direct answer with relevant excerpts and sources.

#model-guide #gpt-oss #unsloth #fine-tuning #llm
