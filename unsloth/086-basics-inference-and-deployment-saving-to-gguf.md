---
title: Saving to GGUF
url: https://unsloth.ai/docs/basics/inference-and-deployment/saving-to-gguf.md
source: llms
fetched_at: 2026-04-27T18:14:41.01459536-03:00
rendered_js: false
word_count: 484
summary: Save models to GGUF format with various quantization methods.
tags:
    - gguf-saving
    - quantization
    - model-deployment
    - huggingface
    - llama-cpp
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Saving to GGUF

## Local save / push to Hub

```python
# Save locally
model.save_pretrained_gguf("directory", tokenizer, quantization_method = "q4_k_m")
model.save_pretrained_gguf("directory", tokenizer, quantization_method = "q8_0")
model.save_pretrained_gguf("directory", tokenizer, quantization_method = "f16")

# Push to Hugging Face Hub
model.push_to_hub_gguf("hf_username/directory", tokenizer, quantization_method = "q4_k_m")
model.push_to_hub_gguf("hf_username/directory", tokenizer, quantization_method = "q8_0")
```

## Quantization methods

Source: <https://github.com/ggml-org/llama.cpp/blob/master/examples/quantize/quantize.cpp#L19>

```python
ALLOWED_QUANTS = \
{
    "not_quantized"  : "Recommended. Fast conversion. Slow inference, big files.",
    "fast_quantized" : "Recommended. Fast conversion. OK inference, OK file size.",
    "quantized"      : "Recommended. Slow conversion. Fast inference, small files.",
    "f32"     : "Not recommended. Retains 100% accuracy, but super slow and memory hungry.",
    "f16"     : "Fastest conversion + retains 100% accuracy. Slow and memory hungry.",
    "q8_0"    : "Fast conversion. High resource use, but generally acceptable.",
    "q4_k_m"  : "Recommended. Uses Q6_K for half of the attention.wv and feed_forward.w2 tensors, else Q4_K",
    "q5_k_m"  : "Recommended. Uses Q6_K for half of the attention.wv and feed_forward.w2 tensors, else Q5_K",
    "q2_k"    : "Uses Q4_K for the attention.vw and feed_forward.w2 tensors, Q2_K for the other tensors.",
    "q3_k_l"  : "Uses Q5_K for the attention.wv, attention.wo, and feed_forward.w2 tensors, else Q3_K",
    "q3_k_m"  : "Uses Q4_K for the attention.wv, attention.wo, and feed_forward.w2 tensors, else Q3_K",
    "q3_k_s"  : "Uses Q3_K for all tensors",
    "q4_0"    : "Original quant method, 4-bit.",
    "q4_1"    : "Higher accuracy than q4_0 but not as high as q5_0. However has quicker inference than q5 models.",
    "q4_k_s"  : "Uses Q4_K for all tensors",
    "q4_k"    : "alias for q4_k_m",
    "q5_k"    : "alias for q5_k_m",
    "q5_0"    : "Higher accuracy, higher resource usage and slower inference.",
    "q5_1"    : "Even higher accuracy, resource usage and slower inference.",
    "q5_k_s"  : "Uses Q5_K for all tensors",
    "q6_k"    : "Uses Q8_K for all tensors",
    "iq2_xxs" : "2.06 bpw quantization",
    "iq2_xs"  : "2.31 bpw quantization",
    "iq3_xxs" : "3.06 bpw quantization",
    "q3_k_xs" : "3-bit extra small quantization",
}
```

## Manual saving

Save model to 16bit first:

```python
model.save_pretrained_merged("merged_model", tokenizer, save_method = "merged_16bit",)
```

Build llama.cpp and convert:

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

Convert to GGUF:

```bash
# F16
python llama.cpp/convert_hf_to_gguf.py merged_model \
    --outfile model-F16.gguf --outtype f16 \
    --split-max-size 50G

# BF16
python llama.cpp/convert_hf_to_gguf.py merged_model \
    --outfile model-BF16.gguf --outtype bf16 \
    --split-max-size 50G

# Q8_0
python llama.cpp/convert_hf_to_gguf.py merged_model \
    --outfile model-Q8_0.gguf --outtype q8_0 \
    --split-max-size 50G
```

Alternative: <https://rentry.org/llama-cpp-conversions#merging-loras-into-a-model> (use model name "merged_model").

## Poor results after exporting

Model works in Unsloth but produces gibberish/repeated output on Ollama, vLLM, etc.

> [!warning] Common causes
> - **Incorrect chat template** — use the SAME template used during training in Unsloth and when running in the target framework
> - **Wrong `eos token`** — causes gibberish on longer generations
> - **Unnecessary start-of-sequence token** — check if the inference engine adds/removes one
>
> **Fix:** Use conversational notebooks to force the chat template:
> - [Qwen-3 14B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(14B\)-Reasoning-Conversational.ipynb)
> - [Gemma-3 4B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3_\(4B\).ipynb)
> - [Llama-3.2 3B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.2_\(1B_and_3B\)-Conversational.ipynb)
> - [Phi-4 14B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Phi_4-Conversational.ipynb)
> - [Mistral v0.3 7B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Mistral_v0.3_\(7B\)-Conversational.ipynb)
> - [More notebooks](https://unsloth.ai/docs/get-started/unsloth-notebooks)

## Saving to GGUF / vLLM 16bit crashes

Reduce `maximum_memory_usage` to avoid OOM during saving:

```python
model.save_pretrained(..., maximum_memory_usage = 0.5)  # default is 0.75
```

#gguf #quantization #model-export #huggingface #llama-cpp
