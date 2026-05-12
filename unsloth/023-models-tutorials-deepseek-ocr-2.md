---
title: 'DeepSeek-OCR 2: How to Run & Fine-tune Guide'
url: https://unsloth.ai/docs/models/tutorials/deepseek-ocr-2.md
source: llms
fetched_at: 2026-04-27T18:14:06.888602969-03:00
rendered_js: false
word_count: 755
summary: This guide explains how to run and fine-tune DeepSeek-OCR 2, a state-of-the-art 3B parameter model for document understanding. It details recommended inference settings, provides code examples for running the model in Unsloth and Transformers environments, and shows performance benchmarks after fine-tuning.
tags:
    - deepseek-ocr-2
    - document-understanding
    - model-guide
    - fine-tuning
    - vision-llm
    - inference
category: tutorial
optimized: true
optimized_at: 2026-04-27T22:10:00Z
---

# DeepSeek-OCR 2: How to Run & Fine-tune Guide

DeepSeek-OCR 2 is a 3B-parameter vision/document-understanding model (released Jan 27, 2026). It uses **DeepEncoder V2** to build global understanding first, then learn a human-like reading order -- improving OCR on complex layouts (columns, linked labels, tables, mixed text + structure).

Inference & training enabled on latest `transformers` via [Unsloth's custom upload](https://huggingface.co/unsloth/DeepSeek-OCR-2) (no accuracy change). Fine-tuning: [free Colab notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Deepseek_OCR_2_\(3B\).ipynb) -- demonstrated 88.6% CER improvement for Persian.

## Running DeepSeek-OCR 2

### Recommended Settings

- **Temperature = 0.0**
- `max_tokens = 8192`
- `ngram_size = 30`
- `window_size = 90`

**Dynamic resolution:** (0-6)x768x768 + 1x1024x1024 -- (0-6)x144 + 256 visual tokens

**Prompt examples:**

```
# document: <image>\n<|grounding|>Convert the document to markdown.
# other image: <image>\n<|grounding|>OCR this image.
# without layouts: <image>\nFree OCR.
# figures in document: <image>\nParse the figure.
# general: <image>\nDescribe this image in detail.
# rec: <image>\nLocate <|ref|>xxxx<|/ref|> in the image.
```

### Unsloth: Run DeepSeek-OCR 2

1. Install: `pip install --upgrade unsloth` (or `pip install --upgrade --force-reinstall --no-deps --no-cache-dir unsloth unsloth_zoo`)
2. Run:

```python
from unsloth import FastVisionModel
import torch
from transformers import AutoModel
import os
os.environ["UNSLOTH_WARN_UNINITIALIZED"] = '0'

from huggingface_hub import snapshot_download
snapshot_download("unsloth/DeepSeek-OCR-2", local_dir = "deepseek_ocr")
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

### Transformers: Run DeepSeek-OCR 2

Inference via Huggingface transformers on NVIDIA GPUs. Tested on python 3.12.9 + CUDA 11.8:

```bash
torch==2.6.0
transformers==4.46.3
tokenizers==0.20.3
einops
addict
easydict
pip install flash-attn==2.7.3 --no-build-isolation
```

```python
from transformers import AutoModel, AutoTokenizer
import torch
import os
os.environ["CUDA_VISIBLE_DEVICES"] = '0'
model_name = 'unsloth/DeepSeek-OCR-2'

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModel.from_pretrained(model_name, _attn_implementation='flash_attention_2', trust_remote_code=True, use_safetensors=True)
model = model.eval().cuda().to(torch.bfloat16)

# prompt = "<image>\nFree OCR. "
prompt = "<image>\n<|grounding|>Convert the document to markdown. "
image_file = 'your_image.jpg'
output_path = 'your/output/dir'

res = model.infer(tokenizer, prompt=prompt, image_file=image_file, output_path = output_path, base_size = 1024, image_size = 768, crop_mode=True, save_results = True)
```

## Fine-tuning DeepSeek-OCR 2

Unsloth trains DeepSeek-OCR-2 **1.4x faster** with **40% less VRAM** and **5x longer context** -- no accuracy degradation. Uses [custom upload](https://huggingface.co/unsloth/DeepSeek-OCR-2) for `transformers` compatibility.

Colab notebook: [Fine-tuning only](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Deepseek_OCR_2_\(3B\).ipynb)

### CER Results (Persian, 10 samples)

| idx  | OCR1 before | OCR1 after | OCR2 before | OCR2 after |
| ---- | ----------: | ---------: | ----------: | ---------: |
| 1520 |      1.0000 |     0.8000 |     10.4000 |     1.0000 |
| 1521 |      0.0000 |     0.0000 |      2.6809 |     0.0213 |
| 1522 |      2.0833 |     0.5833 |      4.4167 |     1.0000 |
| 1523 |      0.2258 |     0.0645 |      0.8710 |     0.0968 |
| 1524 |      0.0882 |     0.1176 |      2.7647 |     0.0882 |
| 1525 |      0.1111 |     0.1111 |      0.9444 |     0.2222 |
| 1526 |      2.8571 |     0.8571 |      4.2857 |     0.7143 |
| 1527 |      3.5000 |     1.5000 |     13.2500 |     1.0000 |
| 1528 |      2.7500 |     1.5000 |      1.0000 |     1.0000 |
| 1529 |      2.2500 |     0.8750 |      1.2500 |     0.8750 |

**Average CER (10 samples):**

- **OCR1:** before **1.4866**, after **0.6409** (**-57%**)
- **OCR2:** before **4.1863**, after **0.6018** (**-86%**)

## Benchmarks

From the official research paper.

**Table 1:** Comprehensive evaluation on OmniDocBench v1.5. V-token_max = max visual tokens per page. R-order = reading order. Other model results sourced from OmniDocBench repository.

![OmniDocBench Table 1](https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2F7CjBxsi10P3kqyF3utpq%2FScreenshot%202026-01-27%20at%201.14.02%E2%80%AFAM.png?alt=media&token=08fc9963-15d1-4d7a-9fb5-93749913928c)

**Table 2:** Edit Distances for document-element categories in OmniDocBench v1.5. Outperforms Gemini-3 Pro.

![OmniDocBench Table 2](https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FcTVu52ugTwQAqLdnQLLz%2FScreenshot%202026-01-27%20at%201.14.15%E2%80%AFAM.png?alt=media&token=ec92a4a1-facb-4b63-90cd-73d23a41dcfb)

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://unsloth.ai/docs/models/tutorials/deepseek-ocr-2.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

#deepseek-ocr-2 #fine-tuning #vision-model #document-understanding
