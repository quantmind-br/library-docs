---
title: 'DeepSeek-OCR: How to Run & Fine-tune'
url: https://unsloth.ai/docs/models/tutorials/deepseek-ocr-how-to-run-and-fine-tune.md
source: llms
fetched_at: 2026-04-27T18:14:15.094871239-03:00
rendered_js: false
word_count: 688
summary: This document provides a guide and reference for utilizing DeepSeek-OCR, a 3B vision model, detailing how to run it using vLLM and Unsloth. It also explains the process of fine-tuning the model, showcasing performance improvements achieved on Persian text datasets.
tags:
    - deepseek-ocr
    - vision-model
    - ocr
    - fine-tuning
    - vllm
    - unsloth
    - document-understanding
category: guide
optimized: true
optimized_at: 2026-04-27T22:10:00Z
---

# DeepSeek-OCR: How to Run & Fine-tune

DeepSeek-OCR is a 3B-parameter vision model for OCR and document understanding. Uses *context optical compression* to convert 2D layouts into vision tokens -- 10x fewer vision tokens than text tokens. Handles tables, papers, handwriting; achieves 97% precision.

Unsloth's [custom upload](https://huggingface.co/unsloth/DeepSeek-OCR) enables fine-tuning + inference on latest `transformers` (no accuracy change). Fine-tuning demo: 88.26% CER improvement on Persian.

## Running DeepSeek-OCR

### Recommended Settings

- **Temperature = 0.0**
- `max_tokens = 8192`
- `ngram_size = 30`
- `window_size = 90`

### vLLM: Run DeepSeek-OCR

1. Install vLLM:

```bash
uv venv
source .venv/bin/activate
# Until v0.11.1 release, you need to install vLLM from nightly build
uv pip install -U vllm --pre --extra-index-url https://wheels.vllm.ai/nightly
```

2. Run:

```python
from vllm import LLM, SamplingParams
from vllm.model_executor.models.deepseek_ocr import NGramPerReqLogitsProcessor
from PIL import Image

# Create model instance
llm = LLM(
    model="unsloth/DeepSeek-OCR",
    enable_prefix_caching=False,
    mm_processor_cache_gb=0,
    logits_processors=[NGramPerReqLogitsProcessor]
)

# Prepare batched input with your image file
image_1 = Image.open("path/to/your/image_1.png").convert("RGB")
image_2 = Image.open("path/to/your/image_2.png").convert("RGB")
prompt = "<image>\nFree OCR."

model_input = [
    {
        "prompt": prompt,
        "multi_modal_data": {"image": image_1}
    },
    {
        "prompt": prompt,
        "multi_modal_data": {"image": image_2}
    }
]

sampling_param = SamplingParams(
    temperature=0.0,
    max_tokens=8192,
    # ngram logit processor args
    extra_args=dict(
        ngram_size=30,
        window_size=90,
        whitelist_token_ids={128821, 128822},  # whitelist: <td>, </td>
    ),
    skip_special_tokens=False,
)
# Generate output
model_outputs = llm.generate(model_input, sampling_param)

# Print output
for output in model_outputs:
    print(output.outputs[0].text)
```

### Unsloth: Run DeepSeek-OCR

1. Install: `pip install --upgrade unsloth` (or `pip install --upgrade --force-reinstall --no-deps --no-cache-dir unsloth unsloth_zoo`)
2. Run:

```python
from unsloth import FastVisionModel
import torch
from transformers import AutoModel
import os
os.environ["UNSLOTH_WARN_UNINITIALIZED"] = '0'

from huggingface_hub import snapshot_download
snapshot_download("unsloth/DeepSeek-OCR", local_dir = "deepseek_ocr")
model, tokenizer = FastVisionModel.from_pretrained(
    "./deepseek_ocr",
    load_in_4bit = False, # Use 4bit to reduce memory use. False for 16bit LoRA.
    auto_model = AutoModel,
    trust_remote_code = True,
    unsloth_force_compile = True,
    use_gradient_checkpointing = "unsloth", # True or "unsloth" for long context
)

prompt = "<image>\nFree OCR. "
image_file = 'your_image.jpg'
output_path = 'your/output/dir'
res = model.infer(tokenizer, prompt=prompt, image_file=image_file, output_path = output_path, base_size = 1024, image_size = 640, crop_mode=True, save_results = True, test_compress = False)
```

## Fine-tuning DeepSeek-OCR

Unsloth trains **1.4x faster** with **40% less VRAM** and **5x longer context** -- no accuracy degradation.

Colab notebooks:
- [Fine-tuning only](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Deepseek_OCR_\(3B\).ipynb)
- [Fine-tuning + Evaluation (A100)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Deepseek_OCR_\(3B\)-Eval.ipynb)

### Persian Dataset Results

Fine-tuned on 200K Persian samples, evaluated on 200 transcript samples:

| Metric | Baseline | Fine-tuned (60 steps, batch=8) |
| ------ | -------: | -----------------------------: |
| Mean CER | 149.07% | 60.81% |
| Accuracy gain | -- | **88.26% absolute improvement** |

> [!tip] Replace the Persian dataset with your own to improve DeepSeek-OCR for other use-cases.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://unsloth.ai/docs/models/tutorials/deepseek-ocr-how-to-run-and-fine-tune.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

#deepseek-ocr #fine-tuning #vision-model #ocr
