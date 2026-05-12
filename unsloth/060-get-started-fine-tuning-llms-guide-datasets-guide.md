---
title: Datasets Guide
url: https://unsloth.ai/docs/get-started/fine-tuning-llms-guide/datasets-guide.md
source: llms
fetched_at: 2026-04-27T18:13:04.168383898-03:00
rendered_js: false
word_count: 3038
summary: This document serves as a guide to understanding and creating datasets for Large Language Models (LLMs), detailing required data formats, preparation steps, and showcasing various recipe workflows available in Unsloth.
tags:
    - dataset-guide
    - llm-training
    - data-formats
    - tokenization
    - unsloth-recipes
    - chat-template
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Datasets Guide

## What is a Dataset?

Datasets are tokenizable text collections for model training. Key considerations: [chat template](https://unsloth.ai/docs/basics/chat-templates) design and tokenization (text into tokens/words/sub-words for embedding adjustment).

### Data Format

| Format | Description | Training Type |
|--------|-------------|---------------|
| Raw Corpus | Raw text from a source (website, book, article) | Continued Pretraining (CPT) |
| Instruct | Instructions with example outputs | Supervised fine-tuning (SFT) |
| Conversation | Multi-turn user/AI dialogue | Supervised fine-tuning (SFT) |
| RLHF | Ranked assistant responses (by script, model, or human) | Reinforcement Learning (RL) |

> [!info] Different style variants exist within each format type.

## Getting Started

Before formatting data, identify:

1. **Purpose** -- determines data needs and format. Examples: chat dialogues (Q&A, language learning, support), structured tasks ([classification](https://colab.research.google.com/github/timothelaborie/text_classification_scripts/blob/main/unsloth_classification.ipynb), summarization, generation), domain-specific data (medical, finance, technical).
2. **Output style** -- target format (JSON, HTML, text, code) and language.
3. **Data source** -- CSV, PDF, website, Hugging Face, Wikipedia. Analyze quality and [quantity](#how-big-should-my-dataset-be). You can also [synthetically generate](#synthetic-data-generation) data (ensure quality and relevance).

> [!tip] Combine your dataset with a generalized one (e.g., ShareGPT from Hugging Face) for diversity. Add [synthetic data](#synthetic-data-generation) to augment.

## Unsloth Data Recipes

[Unsloth Data Recipes](https://unsloth.ai/docs/new/studio/data-recipe) lets you upload documents (PDFs, CSVs) and transforms them into usable datasets via a graph-node visual workflow. Recipes are stored locally in the browser.

Workflow:

1. Open recipes page (create new or open existing).
2. Add blocks to define dataset workflow.
3. Click **Validate** to catch configuration issues.
4. Run a preview to inspect sample rows.
5. Run a full dataset build when ready.
6. Review progress in graph or **Executions** view.
7. Select the resulting dataset in **Studio** and fine-tune.

See also: [[100-new-studio-data-recipe|Unsloth Data Recipes]]

## Formatting the Data

### Common Data Formats for LLM Training

**Continued pretraining** ([[111-basics-continued-pretraining|continued pretraining]]): raw text, no specific structure.

```json
  "text": "Pasta carbonara is a traditional Roman pasta dish. The sauce is made by mixing raw eggs with grated Pecorino Romano cheese and black pepper..."
```

**Instruction format** (Alpaca style) for single-turn task adaptation:

```json
"Instruction": "Task we want the model to perform."

"Input": "Optional, but useful, it will essentially be the user's query."

"Output": "The expected result of the task and the output of the model."
```

**ShareGPT format** for multi-turn conversations:

```json
{
  "conversations": [
    {
      "from": "human",
      "value": "Can you help me make pasta carbonara?"
    },
    {
      "from": "gpt",
      "value": "Would you like the traditional Roman recipe, or a simpler version?"
    },
    {
      "from": "human",
      "value": "The traditional version please"
    },
    {
      "from": "gpt",
      "value": "The authentic Roman carbonara uses just a few ingredients: pasta, guanciale, eggs, Pecorino Romano, and black pepper. Would you like the detailed recipe?"
    }
  ]
}
```

Uses `"from"`/`"value"` keys, alternating between `human` and `gpt`.

**OpenAI ChatML format** (Hugging Face default, most common): `"role"`/`"content"` keys, alternating between `user` and `assistant`.

```
{
  "messages": [
    {
      "role": "user",
      "content": "What is 1+1?"
    },
    {
      "role": "assistant",
      "content": "It's 2!"
    },
  ]
}
```

### Applying Chat Templates with Unsloth

Four steps for ChatML-format datasets:

**Step 1 -- Check supported templates:**

```
from unsloth.chat_templates import CHAT_TEMPLATES
print(list(CHAT_TEMPLATES.keys()))
```

Output: `['unsloth', 'zephyr', 'chatml', 'mistral', 'llama', 'vicuna', 'vicuna_old', 'vicuna old', 'alpaca', 'gemma', 'gemma_chatml', 'gemma2', 'gemma2_chatml', 'llama-3', 'llama3', 'phi-3', 'phi-35', 'phi-3.5', 'llama-3.1', 'llama31', 'llama-3.2', 'llama-3.3', 'llama-32', 'llama-33', 'qwen-2.5', 'qwen-25', 'qwen25', 'qwen2.5', 'phi-4', 'gemma-3', 'gemma3']`

**Step 2 -- Apply template to tokenizer:**

```
from unsloth.chat_templates import get_chat_template

tokenizer = get_chat_template(
    tokenizer,
    chat_template = "gemma-3", # change this to the right chat_template name
)
```

**Step 3 -- Define formatting function:**

```
def formatting_prompts_func(examples):
   convos = examples["conversations"]
   texts = [tokenizer.apply_chat_template(convo, tokenize = False, add_generation_prompt = False) for convo in convos]
   return { "text" : texts, }
```

**Step 4 -- Load dataset and apply formatting:**

```
# Import and load dataset
from datasets import load_dataset
dataset = load_dataset("repo_name/dataset_name", split = "train")

# Apply the formatting function to your dataset using the map method
dataset = dataset.map(formatting_prompts_func, batched = True,)
```

If your dataset uses ShareGPT format (`"from"`/`"value"`), convert first with `standardize_sharegpt`:

```
# Import dataset
from datasets import load_dataset
dataset = load_dataset("mlabonne/FineTome-100k", split = "train")

# Convert your dataset to the "role"/"content" format if necessary
from unsloth.chat_templates import standardize_sharegpt
dataset = standardize_sharegpt(dataset)

# Apply the formatting function to your dataset using the map method
dataset = dataset.map(formatting_prompts_func, batched = True,)
```

### Formatting Data Q&A

**Q: How to use Alpaca instruct format?**

If already in Alpaca format, follow the [Llama3.1 notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.1_\(8B\)-Alpaca.ipynb#scrollTo=LjY75GoYUCB8). To convert, create a Python script to process raw data. For summarization, use a local LLM to generate instructions/outputs per example.

**Q: Should I always use `standardize_sharegpt`?**

Only when the dataset is in ShareGPT format but the model expects ChatML format.

**Q: Why not use the tokenizer's own `apply_chat_template`?**

Model owners' `chat_template` attributes sometimes contain errors that take time to fix. Unsloth checks and fixes `chat_template` for every quantized model upload. Unsloth's `get_chat_template`/`apply_chat_template` also offer advanced data manipulation features. See [[076-basics-chat-templates|Chat Templates]].

**Q: Template not supported?**

Submit a feature request at https://github.com/unslothai/unsloth/issues. Temporary workaround: use the tokenizer's own `apply_chat_template`.

## Synthetic Data Generation

Use a larger local LLM (e.g., Llama 3.3 70B) or GPT 4.5 for best quality. Inference engines: vLLM, Ollama, llama.cpp (requires manual collection/prompting).

Goals of synthetic data:

- Produce entirely new data (from scratch or existing dataset)
- Diversify to prevent [overfitting](https://unsloth.ai/docs/get-started/lora-hyperparameters-guide#avoiding-overfitting-and-underfitting)
- Augment existing data (auto-structure in chosen format)

### Using Unsloth for synthetic data

Upload unstructured or structured data into Studio's [Data Recipes](https://unsloth.ai/docs/new/studio/data-recipe) for automatic conversion. See [[100-new-studio-data-recipe|Unsloth Data Recipes]].

### Using a local LLM or ChatGPT

Ensure at least 10 existing examples for context. Example prompts:

- **Generate more dialogue from existing dataset:** "Using the dataset example I provided, follow the structure and generate conversations based on the examples."
- **No existing dataset:** "Create 10 examples of product reviews for Coca-Cola classified as either positive, negative, or neutral."
- **Dataset without formatting:** "Structure my dataset so it is in a QA ChatML format for fine-tuning. Then generate 5 synthetic data examples with the same topic and format."

Check quality, remove irrelevant responses, balance the dataset. Feed cleaned data back into the LLM to regenerate with more guidance.

## Dataset FAQ + Tips

### How big should my dataset be?

- **Minimum:** 100 rows for reasonable results.
- **Optimal:** 1,000+ rows (more data generally = better outcomes).
- If too small: add synthetic data or a Hugging Face dataset for diversity.
- Quality matters more than quantity -- clean and prepare thoroughly.

### How should I structure my dataset for a reasoning model?

- **Model with existing reasoning** (e.g., DeepSeek-R1-Distill-Llama-8B): include reasoning/chain-of-thought steps in answers.
- **Model without reasoning**: use standard dataset without reasoning in answers; train via [[072-get-started-reinforcement-learning-rl-guide|Reinforcement Learning and GRPO]].

### Multiple datasets

Options:

- Standardize formats, combine into one dataset, fine-tune on the unified set.
- Use the [Multiple Datasets notebook](https://colab.research.google.com/drive/1njCCbE1YVal9xC83hjdo2hiGItpY_D6t?usp=sharing).

### Can I fine-tune the same model multiple times?

Possible but not recommended. Best to combine all datasets and fine-tune in a single process. Re-finetuning can alter quality and knowledge from previous training.

## Using Datasets in Unsloth

### Alpaca Dataset

52,000 instruction-output pairs created by GPT-4, from https://huggingface.co/datasets/vicgalle/alpaca-gpt4. Each row has 3 columns: `instruction`, `input`, `output`. Combined into 1 large prompt for **supervised instruction finetuning**.

### Multiple columns for finetuning

Chat-style assistants require 1 instruction/prompt per interaction, not multiple columns. For datasets with many columns (e.g., Titanic: age, class, fare), columns must be "merged" into 1 prompt.

Unsloth provides `to_sharegpt` to automate this in one call.

Rules for `to_sharegpt`:

- **Column references** in curly braces `{}` (actual CSV/Excel column names).
- **Optional text** in double brackets `[[]]` -- skipped if the column is empty (handles missing values).
- **`output_column_name`** -- the target/prediction column (e.g., `output` for Alpaca).

Example with missing data (Titanic):

| Embarked | Age | Fare |
| -------- | --- | ---- |
| S        | 23  |      |
|          | 18  | 7.25 |

Without `[[]]` optionals, empty values produce "EMPTY" text. With `[[]]`:

```
[[The passenger embarked from S.]] [[Their age is 23.]] [[Their fare is EMPTY.]]
```
becomes:
```
The passenger embarked from S. Their age is 23.
```

### Multi-turn conversations

Alpaca is single-turn. Use the `conversation_extension` parameter to randomly select N rows and merge them into 1 multi-turn conversation. Higher values improve chatbot quality but slow training. Always set `output_column_name` to the output column, then call `standardize_sharegpt`.

## Vision Fine-tuning

Vision/multimodal datasets include image inputs. Example: [Llama 3.2 Vision Notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.2_\(11B\)-Vision.ipynb#scrollTo=vITh0KVJ10qX) with the [ROCO radiography dataset](https://huggingface.co/datasets/unsloth/Radiology_mini) (1,978 rows: X-rays, CT scans, ultrasounds with expert captions).

Format for all vision finetuning tasks:

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

Example conversion function:

```python
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

Apply conversion:

```python
converted_dataset = [convert_to_conversation(sample) for sample in dataset]
```

Quick inference test before finetuning:

```python
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

More details in the [vision notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.2_\(11B\)-Vision.ipynb#scrollTo=vITh0KVJ10qX).

#llm-datasets #fine-tuning #data-formatting #unsloth #chat-templates #synthetic-data
