---
title: Chat Templates
url: https://unsloth.ai/docs/basics/chat-templates.md
source: llms
fetched_at: 2026-04-27T18:15:13.386648866-03:00
rendered_js: false
word_count: 840
summary: This document details how Unsloth manages and utilizes various chat templates for fine-tuning language models, covering techniques like adding new tokens, handling multi-turn conversations, defining custom formats (Alpaca, ChatML), and the step-by-step process of applying these templates to a dataset.
tags:
    - chat-templates
    - finetuning
    - multi-turn
    - dataset-formatting
    - token-addition
    - unsloth-api
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Chat Templates

All chat templates used by Unsloth (Llama, Mistral, Phi-4, etc.) are in [`unsloth/chat_templates.py`](https://github.com/unslothai/unsloth/blob/main/unsloth/chat_templates.py).

**Colab notebooks:**

| Notebook | Author |
|---|---|
| [Conversational](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.2_\(1B_and_3B\)-Conversational.ipynb) | Unsloth |
| [ChatML](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3_\(8B\)-Ollama.ipynb) | Unsloth |
| [Ollama](https://colab.research.google.com/drive/1WZDi7APtQ9VsvOrQSSC5DDtxq159j8iZ?usp=sharing) | Unsloth |
| [Text Classification](https://github.com/timothelaborie/text_classification_scripts/blob/main/unsloth_classification.ipynb) | Timotheeee |
| [Multiple Datasets](https://colab.research.google.com/drive/1njCCbE1YVal9xC83hjdo2hiGItpY_D6t?usp=sharing) | Flail |

## Adding New Tokens

Use `add_new_tokens` to inject custom tokens (e.g. `<CHARACTER_1>`, `<THINKING>`, `<SCRATCH_PAD>`):

```python
model, tokenizer = FastLanguageModel.from_pretrained(...)
from unsloth import add_new_tokens
add_new_tokens(model, tokenizer, new_tokens = ["<CHARACTER_1>", "<THINKING>", "<SCRATCH_PAD>"])
model = FastLanguageModel.get_peft_model(...)
```

> [!warning] Always call `add_new_tokens` **before** `FastLanguageModel.get_peft_model`.

## Multi-Turn Conversations

The Alpaca dataset is single-turn. To teach multi-turn behavior, use the `conversation_extension` parameter: it randomly selects N rows from a single-turn dataset and merges them into one conversation. Higher values improve chat quality but slow training.

Set `output_column_name` to the prediction/output column. Always call `standardize_sharegpt` to format the dataset correctly for fine-tuning.

## Customizable Chat Templates

Define a chat template with `{INPUT}`, `{OUTPUT}`, and optional `{SYSTEM}` fields. Supported named templates:

```
from unsloth.chat_templates import CHAT_TEMPLATES
print(list(CHAT_TEMPLATES.keys()))
```

Output: `['unsloth', 'zephyr', 'chatml', 'mistral', 'llama', 'vicuna', 'vicuna_old', 'alpaca', 'gemma', 'gemma2', 'llama-3', 'llama-3.1', 'llama-3.2', 'llama-3.3', 'qwen-2.5', 'phi-3', 'phi-3.5', 'phi-4', 'gemma-3']` (plus aliases).

## Applying Chat Templates with Unsloth

**Step 1** — Apply template to tokenizer:

```python
from unsloth.chat_templates import get_chat_template
tokenizer = get_chat_template(
    tokenizer,
    chat_template = "gemma-3",
)
```

**Step 2** — Define formatting function:

```python
def formatting_prompts_func(examples):
    convos = examples["conversations"]
    texts = [tokenizer.apply_chat_template(convo, tokenize = False, add_generation_prompt = False) for convo in convos]
    return { "text" : texts, }
```

**Step 3** — Load dataset and apply formatting:

```python
from datasets import load_dataset
dataset = load_dataset("repo_name/dataset_name", split = "train")
dataset = dataset.map(formatting_prompts_func, batched = True,)
```

> [!tip] ShareGPT format conversion
> If your dataset uses `"from"/"value"` keys instead of `"role"/"content"`, convert first:

```python
from unsloth.chat_templates import standardize_sharegpt
dataset = load_dataset("mlabonne/FineTome-100k", split = "train")
dataset = standardize_sharegpt(dataset)
dataset = dataset.map(formatting_prompts_func, batched = True,)
```

## ShareGPT Mapping

For ShareGPT-style datasets (`from`/`value` keys), use the `mapping` parameter. `map_eos_token=True` maps `<|im_end|>` to EOS without training.

```python
tokenizer = get_chat_template(
    tokenizer,
    chat_template = "chatml",
    mapping = {"role" : "from", "content" : "value", "user" : "human", "assistant" : "gpt"},
    map_eos_token = True,
)
```

## Custom Templates

Pass a `tuple` of `(custom_template, eos_token)` — the `eos_token` must appear inside the template:

```python
unsloth_template = \
    "{{ bos_token }}"\
    "{{ 'You are a helpful assistant to the user\n' }}"\
    "{% for message in messages %}"\
        "{% if message['role'] == 'user' %}"\
            "{{ '>>> User: ' + message['content'] + '\n' }}"\
        "{% elif message['role'] == 'assistant' %}"\
            "{{ '>>> Assistant: ' + message['content'] + eos_token + '\n' }}"\
        "{% endif %}"\
    "{% endfor %}"\
    "{% if add_generation_prompt %}"\
        "{{ '>>> Assistant: ' }}"\
    "{% endif %}"
unsloth_eos_token = "eos_token"

tokenizer = get_chat_template(
    tokenizer,
    chat_template = (unsloth_template, unsloth_eos_token,),
    mapping = {"role" : "from", "content" : "value", "user" : "human", "assistant" : "gpt"},
    map_eos_token = True,
)
```

#chat-templates #finetuning #multi-turn #dataset-formatting #unsloth
