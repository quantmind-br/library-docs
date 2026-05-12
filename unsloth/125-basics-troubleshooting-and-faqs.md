---
title: Troubleshooting & FAQs
url: https://unsloth.ai/docs/basics/troubleshooting-and-faqs.md
source: llms
fetched_at: 2026-04-27T18:15:10.181526713-03:00
rendered_js: false
word_count: 1171
summary: Troubleshooting guides and FAQs for Unsloth — model compatibility, export issues, GGUF conversion, memory management, evaluation setup, early stopping, and common errors.
tags:
    - troubleshooting
    - fine-tuning
    - unsloth-guide
    - gguf-conversion
    - evaluation-setup
    - model-compatibility
category: guide
optimized: true
optimized_at: 2026-04-27T21:15:00Z
---

# Troubleshooting & FAQs

> [!tip] Always update Unsloth first if you encounter issues.
> `pip install --upgrade --force-reinstall --no-cache-dir --no-deps unsloth unsloth_zoo`
>
> For persistent version/dependency issues, use the [Docker image](https://unsloth.ai/docs/get-started/install/docker) with everything pre-installed.

## Fine-Tuning a New/Unsupported Model

Unsloth works with any `transformers`-supported model. For unsupported or newer models, enable compatibility with `trust_remote_code=True`:

<pre class="language-python"><code class="lang-python">from huggingface_hub import snapshot_download
snapshot_download("unsloth/DeepSeek-OCR", local_dir = "deepseek_ocr")
model, tokenizer = FastVisionModel.from_pretrained(
    "./deepseek_ocr",
    load_in_4bit = False, # Use 4bit to reduce memory. False for 16bit LoRA.
    auto_model = AutoModel,
    trust_remote_code = True, # Enable to support new models
    unsloth_force_compile = True,
    use_gradient_checkpointing = "unsloth", # True or "unsloth" for long context
)
</code></pre>

See [[024-models-tutorials-deepseek-ocr-how-to-run-and-fine-tune|DeepSeek-OCR guide]] for full tutorial.

## Poor Results After Exporting to Other Platforms

Model works in Unsloth but produces gibberish/infinite/repeated output on Ollama or vLLM:

- **Incorrect chat template** (most common) — Use the SAME template from training when running in llama.cpp/Ollama.
- **Inference engine SoS token issues** — May add unnecessary start-of-sequence token (or lack thereof).
- **Fix:** Use conversational notebooks to force the chat template:
  - [Qwen-3 14B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(14B\)-Reasoning-Conversational.ipynb)
  - [Gemma-3 4B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3_\(4B\).ipynb)
  - [Llama-3.2 3B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.2_\(1B_and_3B\)-Conversational.ipynb)
  - [Phi-4 14B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Phi_4-Conversational.ipynb)
  - [Mistral v0.3 7B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Mistral_v0.3_\(7B\)-Conversational.ipynb)
  - More: [[073-get-started-unsloth-notebooks|Unsloth Notebooks]]

See also [[123-basics-inference-and-deployment-troubleshooting-inference|Troubleshooting Inference]] for dedicated export troubleshooting.

## GGUF / vLLM 16bit Save Crashes

Reduce GPU memory usage during save:

```python
model.save_pretrained(..., maximum_memory_usage = 0.5)  # Default 0.75; lower to reduce OOM
```

## Manual GGUF Conversion

1. Save model to 16bit:

```python
model.save_pretrained_merged("merged_model", tokenizer, save_method = "merged_16bit",)
```

2. Compile llama.cpp:

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggerganov/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=ON -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-quantize llama-cli llama-gguf-split llama-mtmd-cli
cp llama.cpp/build/bin/llama-* llama.cpp
```

3. Convert to desired format:

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

## Q8_K_XL Slower Than Q8_0 on Mac

Q8_K_XL upcasts some layers to BF16, which is slower than F16 on Mac. Unsloth is changing conversion to default Q8_K_XL to F16 to mitigate this.

## Evaluation Setup

### Dataset Split

Always shuffle when splitting:

```python
new_dataset = dataset.train_test_split(
    test_size = 0.01, # 1% for test (can be int for # of rows)
    shuffle = True,    # Always True!
    seed = 3407,
)

train_dataset = new_dataset["train"]
eval_dataset = new_dataset["test"]
```

### Training Arguments for Evaluation

```python
from trl import SFTTrainer, SFTConfig
trainer = SFTTrainer(
    args = SFTConfig(
        fp16_full_eval = True,         # Reduces memory by ~1/2
        per_device_eval_batch_size = 2,# Lower to reduce VRAM
        eval_accumulation_steps = 4,   # Can increase instead of batch_size
        eval_strategy = "steps",       # "steps" or "epochs"
        eval_steps = 1,                # Evaluate every N training steps
    ),
    train_dataset = new_dataset["train"],
    eval_dataset = new_dataset["test"],
    ...
)
trainer.train()
```

> [!warning] Evaluation can be very slow with `eval_steps = 1`. Reduce eval dataset to ~100 rows if needed.

### Evaluation OOM / Crashing

Lower `per_device_eval_batch_size` below 2 and ensure `fp16_full_eval=True` (or `bf16_full_eval=True` for bf16 machines). Unsloth enables these flags by default as of June 2025.

## Early Stopping

Stops training when `eval_loss` stops decreasing:

```python
from trl import SFTConfig, SFTTrainer
trainer = SFTTrainer(
    args = SFTConfig(
        fp16_full_eval = True,
        per_device_eval_batch_size = 2,
        eval_accumulation_steps = 4,
        output_dir = "training_checkpoints",
        save_strategy = "steps",
        save_steps = 10,
        save_total_limit = 3,
        eval_strategy = "steps",
        eval_steps = 10,
        load_best_model_at_end = True,       # Required for early stopping
        metric_for_best_model = "eval_loss",
        greater_is_better = False,           # Lower loss = better
    ),
    model = model,
    tokenizer = tokenizer,
    train_dataset = new_dataset["train"],
    eval_dataset = new_dataset["test"],
)
```

Add the callback:

```python
from transformers import EarlyStoppingCallback
early_stopping_callback = EarlyStoppingCallback(
    early_stopping_patience = 3,     # Steps to wait for loss decrease
    early_stopping_threshold = 0.0,  # Min loss decrease to trigger stop (e.g. 0.01)
)
trainer.add_callback(early_stopping_callback)
trainer.train()
```

## Download Stuck at 90-95%

Force synchronous downloads with more error output:

```python
import os
os.environ["UNSLOTH_STABLE_DOWNLOADS"] = "1"

from unsloth import FastLanguageModel
```

## CUDA Device-Side Assert

Restart and place before any Unsloth import. File a bug report if it persists.

```python
import os
os.environ["UNSLOTH_COMPILE_DISABLE"] = "1"
os.environ["UNSLOTH_DISABLE_FAST_GENERATION"] = "1"
```

## All Labels Are -100 / Training Losses All 0

Incorrect `train_on_responses_only` usage for the model. See [[061-get-started-fine-tuning-llms-guide-lora-hyperparameters-guide|LoRA Hyperparameters Guide]].

**Llama 3.1/3.2/3.3:**

```python
from unsloth.chat_templates import train_on_responses_only
trainer = train_on_responses_only(
    trainer,
    instruction_part = "<|start_header_id|>user<|end_header_id|>\n\n",
    response_part = "<|start_header_id|>assistant<|end_header_id|>\n\n",
)
```

**Gemma 2/3/3n:**

```python
from unsloth.chat_templates import train_on_responses_only
trainer = train_on_responses_only(
    trainer,
    instruction_part = "<start_of_turn>user\n",
    response_part = "<start_of_turn>model\n",
)
```

## Unsloth Slower Than Expected

`torch.compile` warmup takes ~5 minutes. Measure throughput only after full compilation. To disable:

```python
import os
os.environ["UNSLOTH_COMPILE_DISABLE"] = "1"
```

## Gemma3nForConditionalGeneration Weights Not Initialized

Critical error — weights not parsed correctly, causing incorrect output. Fix by upgrading:

```bash
pip install --upgrade --force-reinstall --no-cache-dir --no-deps unsloth unsloth_zoo
pip install --upgrade --force-reinstall --no-cache-dir --no-deps transformers timm
```

If issue persists, file a bug report.

## NotImplementedError: UTF-8 Locale Required (Got ANSI)

See <https://github.com/googlecolab/colabtools/issues/3409>

```python
import locale
locale.getpreferredencoding = lambda: "UTF-8"
```

## Citing Unsloth

**Model uploads** (e.g. Qwen3-30B-A3B-GGUF Q8_K_XL):

```bibtex
@misc{unsloth_2025_qwen3_30b_a3b,
  author       = {Unsloth AI and Han-Chen, Daniel and Han-Chen, Michael},
  title        = {Qwen3-30B-A3B-GGUF:Q8\_K\_XL},
  year         = {2025},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/unsloth/Qwen3-30B-A3B-GGUF}}
}
```

**GitHub package / general work:**

```bibtex
@misc{unsloth,
  author       = {Unsloth AI and Han-Chen, Daniel and Han-Chen, Michael},
  title        = {Unsloth},
  year         = {2025},
  publisher    = {Github},
  howpublished = {\url{https://github.com/unslothai/unsloth}}
}
```

#troubleshooting #unsloth #gguf #evaluation #fine-tuning
