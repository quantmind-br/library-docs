---
title: Long Context gpt-oss Training
url: https://unsloth.ai/docs/models/gpt-oss-how-to-run-and-fine-tune/long-context-gpt-oss-training.md
source: llms
fetched_at: 2026-04-27T18:13:53.641488122-03:00
rendered_js: false
word_count: 1818
summary: This document explains how Unsloth's Flex Attention implementation significantly enhances GPT-OSS training by enabling much longer context lengths, reducing VRAM usage, and increasing training speed compared to other methods. It details the mechanism of attention sinks and customizes Flex Attention using score modifiers and masking functions.
tags:
    - gpt-oss
    - flex-attention
    - context-length
    - unsloth
    - attention-sinks
    - lora-training
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:38:00Z
---

# Long Context gpt-oss Training

Unsloth Flex Attention for OpenAI gpt-oss training enables **>8x longer context lengths**, **>50% less VRAM usage**, and **>1.5x faster training** (no accuracy degradation) vs all implementations including Flash Attention 3 (FA3). A single 80GB H100 trains with **60K context** (BF16 LoRA) or **81K context** (QLoRA). Applies to both gpt-oss-20b and gpt-oss-120b. Gains scale with context length.

Other implementations max out at ~9K context on 80GB (15K with FA3). FA3 is **unsuitable for gpt-oss training** — it lacks backward pass support for attention sinks.

- You can [now export/save](#new-saving-to-gguf-vllm-after-gpt-oss-training) QLoRA fine-tuned gpt-oss to llama.cpp, vLLM, Ollama, or HF
- [Fixed gpt-oss training](#bug-fixes-for-gpt-oss) losses diverging on float16 GPUs (T4 Colab)
- Fixed `swiglu_limit = 7.0` during MXFP4 inference in transformers

## Unsloth Flex Attention Support

With Unsloth Flex Attention, an 80GB H100 handles up to 81K context (QLoRA) and 60K context (BF16 LoRA) for both gpt-oss-20b and gpt-oss-120b. Longer context = bigger VRAM/time savings. Minimum 1.3x speedup, up to 2x at high context lengths.

Thanks to Rohan Pandey for his [Flex Attention implementation](https://x.com/khoomeik/status/1955693558914310608) which inspired Unsloth's version.

## Attention Sinks

OpenAI's GPT OSS uses an alternating pattern: sliding window attention (SWA, 128 tokens), full attention (FA), SWA, FA, etc. Small sliding windows break long-context retrieval. Most labs expand to 2048-4096 tokens; OpenAI instead uses **Attention Sinks** from [Efficient Streaming Language Models with Attention Sinks](https://arxiv.org/abs/2309.17453): keep a small sliding window but add **global attention on the first token**.

Key findings from the paper:

- Attention assigns heavy weight to first 1-4 tokens; removing them during SWA degrades long-context retrieval
- [Attention Is Off By One](https://www.evanmiller.org/attention-is-off-by-one.html) partially works but needs extra sink tokens
- **A single learnable sink token works remarkably well** — that's what OpenAI did for GPT-OSS

## Unsloth's Flex Attention Implementation

Flex Attention (<https://pytorch.org/blog/flexattention/>) provides two customization routes:

- **Score modifier (f)** — edits attention logits before softmax
- **Masking function (M)** — skips unnecessary operations (e.g., SWA only sees last 128 tokens)

**Key advantage**: Flex Attention auto-generates fast Triton kernels for arbitrary score modifiers and masking functions.

$$\sigma\bigg(s\times\bold{f}(QK^T+\bold{M})\bigg)$$

### Sink Attention via Flex Attention

A single attention sink is implemented in both [OpenAI's GPT-OSS repo](#implementations-for-sink-attention) and HuggingFace transformers:

```python
combined_logits = torch.cat([attn_weights, sinks], dim=-1)
probs = F.softmax(combined_logits, dim=-1)
scores = probs[..., :-1]
```

Concatenate sink at end of `Q @ K.T`, softmax, then drop the last sink column.

**Unsloth moves the sink to index 0** (first column) instead of the default end position. Training loss remains consistent with standard HuggingFace runs.

### Sliding Window: Off-by-One Fix

The official Flex Attention sliding window counts the current token (window = last N+1 tokens). HuggingFace and GPT-OSS strictly attend to last N tokens only. Confirmed via [OpenAI's implementation](https://github.com/openai/gpt-oss/blob/main/gpt_oss/torch/model.py):

```python
mask = torch.triu(Q.new_full((n_tokens, n_tokens), -float("inf")), diagonal=1)
if sliding_window > 0:
    mask += torch.tril(
        mask.new_full((n_tokens, n_tokens), -float("inf")), diagonal=-sliding_window
    )
```

Fix — use `<` instead of `<=`:

```python
def sliding_window_causal(b, h, q_idx, kv_idx):
    causal_mask = q_idx >= kv_idx
    window_mask = q_idx - kv_idx <  SLIDING_WINDOW # GPT-OSS version (not <=)
    return causal_mask & window_mask
```

### Causal Mask with Sink at Index 0

Since sink moved to column 0, add 1 to `q_idx`:

```python
def causal_mask_with_sink(batch, head, q_idx, kv_idx):
    """
      0 1 2 3     0 1 2 3
    0 X X       1   X
    1 X X X     2   X X
    2 X X X X   3   X X X
    """
    # We add (q_idx + 1) since first column is sink token
    causal_mask = (q_idx + 1) >= kv_idx
    sink_first_column = kv_idx == 0
    return causal_mask | sink_first_column
```

## Mathematical Derivation for Attention Sinks

Alternative approach without padding K and V, using `return_lse = True` from Flex Attention for logsumexp:

$$A(x) = \frac{\exp(x_i)}{\sum{\exp{(x_i)}}}$$
$$A_{sink}(x) = \frac{\exp(x_i)}{\exp{(s)}+ \sum{\exp{(x_i)}}}$$

Derivation:

$$A_{sink}(x) = A(x) \cdot \frac{\sum\exp(x_i)}{\exp(s)+\sum\exp(x_i)}$$
$$\text{LSE}(x) = \log\sum\exp(x_i), \quad \exp(\text{LSE}(x)) = \sum\exp(x_i)$$

This approach has somewhat higher error than the zero-padding approach, so Unsloth defaults to the original version.

## Saving to GGUF, vLLM after gpt-oss Training

QLoRA fine-tuned gpt-oss can now be saved/exported/merged to **llama.cpp**, **vLLM**, or **HF** — not just Unsloth.

Previously QLoRA fine-tuned gpt-oss was restricted to Unsloth. Now supports:

- **MXFP4 native merge** via `save_method="mxfp4"` — 75% less disk, 50% less VRAM, 5-10x faster merge, faster GGUF conversion
- **bf16 export** via `save_method="merged_16bit"` with on-demand MXFP4 dequantization

### Merge commands

```python
model.save_pretrained_merged(save_directory, tokenizer, save_method="mxfp4")
```

```python
model.push_to_hub_merged(repo_name, tokenizer=tokenizer, token=hf_token, save_method="mxfp4")
```

### Saving to Llama.cpp

1. Build llama.cpp (set `-DGGML_CUDA=OFF` for CPU-only):

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cp
```

2. Convert MXFP4 merged model:

```bash
python3 llama.cpp/convert_hf_to_gguf.py gpt-oss-finetuned-merged/ --outfile gpt-oss-finetuned-mxfp4.gguf
```

3. Run inference (recommended settings: `temperature=1.0`, `top_p=1.0`, `top_k=0`):

```bash
llama.cpp/llama-cli --model gpt-oss-finetuned-mxfp4.gguf \
    --jinja -ngl 99 --threads -1 --ctx-size 16384 \
    --temp 1.0 --top-p 1.0 --top-k 0 \
     -p "The meaning to life and the universe is"
```

### Saving to SGLang

<details>

<summary>SGLang build and inference</summary>

1. Build SGLang from source:

```bash
# build from source
git clone https://github.com/sgl-project/sglang
cd sglang
pip3 install pip --upgrade
pip3 install -e "python[all]"

# ROCm 6.3
pip3 install torch==2.8.0 torchvision torchaudio --index-url https://download.pytorch.org/whl/test/rocm6.3
git clone https://github.com/triton-lang/triton
cd python/triton_kernels
pip3 install .

# hopper
pip3 install torch==2.8.0 torchvision torchaudio --index-url https://download.pytorch.org/whl/test/cu126
pip3 install sgl-kernel==0.3.2

# blackwell cu128
pip3 install torch==2.8.0 torchvision torchaudio --index-url https://download.pytorch.org/whl/test/cu128
pip3 install https://github.com/sgl-project/whl/releases/download/v0.3.2/sgl_kernel-0.3.2+cu128-cp39-abi3-manylinux2014_x86_64.whl

# blackwell cu129
pip3 install torch==2.8.0 torchvision torchaudio --index-url https://download.pytorch.org/whl/test/cu129
pip3 install https://github.com/sgl-project/whl/releases/download/v0.3.2/sgl_kernel-0.3.2-cp39-abi3-manylinux2014_x86_64.whl
```

2. Launch server:

```bash
python3 -m sglang.launch_server --model-path ./gpt-oss-finetuned-merged/
```

3. Run inference:

```python
import requests
from sglang.utils import print_highlight

url = f"http://localhost:8000/v1/chat/completions"

data = {
    "model": "gpt-oss-finetuned-merged",
    "messages": [{"role": "user", "content": "What is the capital of France?"}],
}

response = requests.post(url, json=data)
print_highlight(response.json())
```

</details>

### Fine-tuning gpt-oss directly

Load native MXFP4 quantized format with <24GB VRAM for QLoRA:

```python
model, tokenizer = FastLanguageModel.from_pretrained(
    # model_name = "unsloth/gpt-oss-20b-BF16",
    model_name = "unsloth/gpt-oss-20b",
    dtype = dtype, # None for auto detection
    max_seq_length = max_seq_length, # Choose any for long context!
    load_in_4bit = True,  # 4 bit quantization to reduce memory
    full_finetuning = False, # [NEW!] We have full finetuning now!
    # token = "hf_...", # use one if using gated models
)
```

Add Peft layer via `FastLanguageModel.get_peft_model`, then run SFT fine-tuning.

## Bug Fixes for gpt-oss

Collaborated with [HuggingFace](https://github.com/huggingface/transformers/pull/40197) to fix MXFP4 inference — ensured `swiglu_limit = 7.0` is correctly applied using OpenAI's kernels.

### Float16 Loss Divergence Fix

Extended QLoRA training (>60 steps) caused loss divergence on non-BF16 GPUs (T4). Did **not** affect A100/H100 QLoRA or f16 LoRA training. Now fixed — all GPU setups produce aligned training loss.

Root causes found:

1. Pure float16 overflows at step 50
2. MoE down projections produce huge activation outliers
3. Activations must be saved in bfloat16 or float32

float16 max range is 65504 — some GPT-OSS 20B activations spike beyond this. **Fixed in Unsloth — float16 training works out of the box.**

## Implementations for Sink Attention

### OpenAI implementation

Source: [gpt-oss/torch/model.py](https://github.com/openai/gpt-oss/blob/main/gpt_oss/torch/model.py)

```python
def sdpa(Q, K, V, S, sm_scale, sliding_window=0):
    # sliding_window == 0 means no sliding window
    n_tokens, n_heads, q_mult, d_head = Q.shape
    assert K.shape == (n_tokens, n_heads, d_head)
    assert V.shape == (n_tokens, n_heads, d_head)
    K = K[:, :, None, :].expand(-1, -1, q_mult, -1)
    V = V[:, :, None, :].expand(-1, -1, q_mult, -1)
    S = S.reshape(n_heads, q_mult, 1, 1).expand(-1, -1, n_tokens, -1)
    mask = torch.triu(Q.new_full((n_tokens, n_tokens), -float("inf")), diagonal=1)
    if sliding_window > 0:
        mask += torch.tril(
            mask.new_full((n_tokens, n_tokens), -float("inf")), diagonal=-sliding_window
        )
    QK = torch.einsum("qhmd,khmd->hmqk", Q, K) * sm_scale
    QK += mask[None, None, :, :]
    QK = torch.cat([QK, S], dim=-1)
    W = torch.softmax(QK, dim=-1)
    W = W[..., :-1]
    attn = torch.einsum("hmqk,khmd->qhmd", W, V)
    return attn.reshape(n_tokens, -1)
```

### HuggingFace transformers implementation

Source: [modeling_gpt_oss.py](https://github.com/huggingface/transformers/blob/main/src/transformers/models/gpt_oss/modeling_gpt_oss.py)

```python
def eager_attention_forward(
    module: nn.Module,
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    attention_mask: Optional[torch.Tensor],
    scaling: float,
    dropout: float = 0.0,
    **kwargs,
):
    key_states = repeat_kv(key, module.num_key_value_groups)
    value_states = repeat_kv(value, module.num_key_value_groups)
    attn_weights = torch.matmul(query, key_states.transpose(2, 3)) * scaling
    if attention_mask is not None:
        causal_mask = attention_mask[:, :, :, : key_states.shape[-2]]
        attn_weights = attn_weights + causal_mask

    sinks = module.sinks.reshape(1, -1, 1, 1).expand(query.shape[0], -1, query.shape[-2], -1)
    combined_logits = torch.cat([attn_weights, sinks], dim=-1)

    # This was not in the original implementation and slightly affect results; it prevents overflow in BF16/FP16
    # when training with bsz>1 we clamp max values.

    combined_logits = combined_logits - combined_logits.max(dim=-1, keepdim=True).values
    probs = F.softmax(combined_logits, dim=-1, dtype=combined_logits.dtype)
    scores = probs[..., :-1]  # we drop the sink here
    attn_weights = nn.functional.dropout(scores, p=dropout, training=module.training)
    attn_output = torch.matmul(attn_weights, value_states)
    attn_output = attn_output.transpose(1, 2).contiguous()
    return attn_output, attn_weights
```

---

# Agent Instructions: Querying This Documentation

If you need additional information not on this page, query dynamically via:

```
GET https://unsloth.ai/docs/models/gpt-oss-how-to-run-and-fine-tune/long-context-gpt-oss-training.md?ask=<question>
```

The question should be specific, self-contained, and in natural language. Returns a direct answer with relevant excerpts and sources.

#gpt-oss #flex-attention #long-context #attention-sinks #lora-training
