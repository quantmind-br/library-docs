---
title: Vision Fine-tuning
url: https://unsloth.ai/docs/basics/vision-fine-tuning.md
source: llms
fetched_at: 2026-04-27T18:15:09.039806227-03:00
rendered_js: false
word_count: 813
summary: This document serves as a guide to vision fine-tuning for models like VLMs, explaining techniques such as training with RL and demonstrating various model applications. It details how to configure which layers (vision, language, attention, MLP) are fine-tuned, describes the specialized Vision Data Collator arguments, and outlines methods for handling multi-image datasets.
tags:
    - vision-fine-tuning
    - vlm-training
    - layer-selection
    - data-collator
    - multimodal-llms
    - reinforcement-learning
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Vision Fine-tuning

Fine-tuning vision models (VLMs) enables object/movement detection and similar visual tasks. You can also train [VLMs with RL](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/vision-reinforcement-learning-vlm-rl).

## Available Notebooks

| Model | Task | Notebook |
|-------|------|----------|
| [Qwen3-VL (8B)](https://unsloth.ai/docs/models/tutorials/qwen3-how-to-run-and-fine-tune/qwen3-vl-how-to-run-and-fine-tune) | Vision | [Notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_VL_\(8B\)-Vision.ipynb) |
| [Ministral 3](https://unsloth.ai/docs/models/tutorials/ministral-3) | General Q&A | [Notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Pixtral_\(12B\)-Vision.ipynb) |
| Gemma 3 (4B) | Vision | [Notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3_\(4B\)-Vision.ipynb) |
| Llama 3.2 Vision (11B) | Radiography | [Notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.2_\(11B\)-Vision.ipynb) |
| Qwen2.5 VL (7B) | Handwriting to LaTeX | [Notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen2.5_VL_\(7B\)-Vision.ipynb) |

> [!tip] Use images of uniform size (300-1000px) to keep training fast and resource-efficient.
> Concatenate general Q&A datasets with niche datasets to prevent forgetting base model skills.

## Layer Selection

Choose which layers to fine-tune. All enabled by default.

```python
model = FastVisionModel.get_peft_model(
    model,
    finetune_vision_layers     = True, # False if not finetuning vision layers
    finetune_language_layers   = True, # False if not finetuning language layers
    finetune_attention_modules = True, # False if not finetuning attention layers
    finetune_mlp_modules       = True, # False if not finetuning MLP layers

    r = 16,                           # The larger, the higher the accuracy, but might overfit
    lora_alpha = 16,                  # Recommended alpha == r at least
    lora_dropout = 0,
    bias = "none",
    random_state = 3407,
    use_rslora = False,               # We support rank stabilized LoRA
    loftq_config = None,               # And LoftQ
    target_modules = "all-linear",    # Optional now! Can specify a list if needed
    modules_to_save=[
        "lm_head",
        "embed_tokens",
    ],
)
```

## Vision Data Collator

```python
from unsloth.trainer import UnslothVisionDataCollator
from trl import SFTTrainer, SFTConfig
trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    data_collator = UnslothVisionDataCollator(model, tokenizer),
    train_dataset = dataset,
    args = SFTConfig(...),
)
```

### UnslothVisionDataCollator Arguments

| Parameter | Default | Description |
|-----------|---------|-------------|
| `model` | required | The vision model |
| `processor` | required | The model's processor |
| `max_seq_length` | `None` | Auto-detected from `FastVisionModel.from_pretrained(max_seq_length=...)` |
| `formatting_func` | `None` | Function for transforming text |
| `resize` | `"min"` | `"min"` = fit model's default image_size; `"max"` = no resize; `(10, 10)` = tuple |
| `ignore_index` | `-100` | Loss ignore index |
| `train_on_responses_only` | `False` | Equivalent to `train_on_responses_only` for LLMs |
| `instruction_part` | `None` | Equivalent to `train_on_responses_only(instruction_part=...)` |
| `response_part` | `None` | Equivalent to `train_on_responses_only(response_part=...)` |
| `force_match` | `True` | Match newlines as well |
| `num_proc` | `None` | Auto-selects number of GPUs |
| `completion_only_loss` | `True` | Ignores padding vision tokens -- should always be `True` |
| `pad_to_multiple_of` | `None` | Data collator padding |
| `resize_dimension` | `0` | `0` = first dim, `1` = second dim, `'max'` = max of h/w, `'min'` = min of h/w |
| `snap_to_patch_size` | `False` | Force image to be a multiple of the patch size |

## Multi-image Training

Swap `ds.map()` with a list comprehension to avoid dataset standardization/arrow rules:

```python
# Instead of:
ds_converted = ds.map(convert_to_conversation)

# Use:
ds_converted = [convert_to_conversation(sample) for sample in dataset]
```

## Dataset Format

Vision datasets follow the standard Q&A format from [[060-get-started-fine-tuning-llms-guide-datasets-guide|Datasets Guide]] but include image inputs.

### Required Conversation Format

```python
[
{ "role": "user",
  "content": [{"type": "text",  "text": instruction}, {"type": "image", "image": image} ]
},
{ "role": "assistant",
  "content": [{"type": "text",  "text": answer} ]
},
]
```

### Example: ROCO Radiography Dataset

Dataset: [unsloth/Radiology_mini](https://huggingface.co/datasets/unsloth/Radiology_mini) (1978 rows, features: `image`, `image_id`, `caption`, `cui`)

```notebook-python
instruction = "You are an expert radiographer. Describe accurately what you see in this image."

def convert_to_conversation(sample):
    conversation = [
        { "role": "user",
          "content" : [
            {"type" : "text",  "text"  : instruction},
            {"type" : "image", "image" : sample["image"]} ]
        },
        { "role" : "assistant",
          "content" : [
            {"type" : "text",  "text"  : sample["caption"]} ]
        },
    ]
    return { "messages" : conversation }
pass
```

```notebook-python
converted_dataset = [convert_to_conversation(sample) for sample in dataset]
```

### Quick Inference Test

```notebook-python
FastVisionModel.for_inference(model) # Enable for inference!

image = dataset[0]["image"]
instruction = "You are an expert radiographer. Describe accurately what you see in this image."

messages = [
    {"role": "user", "content": [
        {"type": "image"},
        {"type": "text", "text": instruction}
    ]}
]
input_text = tokenizer.apply_chat_template(messages, add_generation_prompt = True)
inputs = tokenizer(
    image,
    input_text,
    add_special_tokens = False,
    return_tensors = "pt",
).to("cuda")

from transformers import TextStreamer
text_streamer = TextStreamer(tokenizer, skip_prompt = True)
_ = model.generate(**inputs, streamer = text_streamer, max_new_tokens = 128,
                   use_cache = True, temperature = 1.5, min_p = 0.1)
```

## Training on Assistant Responses Only

For vision models, use `UnslothVisionDataCollator` arguments instead of `train_on_responses_only`:

```python
UnslothVisionDataCollator(
    model, tokenizer,
    ...
    train_on_responses_only = True,
    instruction_part = "<|start_header_id|>user<|end_header_id|>\n\n",
    response_part = "<|start_header_id|>assistant<|end_header_id|>\n\n",
    ...
)
```

For Llama 3.2 Vision example:

```python
UnslothVisionDataCollator(
    model, tokenizer,
    ...
    train_on_responses_only = True,
    instruction_part = "<|start_header_id|>user<|end_header_id|>\n\n",
    response_part = "<|start_header_id|>assistant<|end_header_id|>\n\n",
    ...
)
```

## Agent Query Endpoint

```
GET https://unsloth.ai/docs/basics/vision-fine-tuning.md?ask=<question>
```

#vision-fine-tuning #vlm #multimodal
