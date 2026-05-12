---
title: 'Tutorial: How to Finetune Llama-3 and Use In Ollama'
url: https://unsloth.ai/docs/get-started/fine-tuning-llms-guide/tutorial-how-to-finetune-llama-3-and-use-in-ollama.md
source: llms
fetched_at: 2026-04-27T18:13:07.457882144-03:00
rendered_js: false
word_count: 3192
summary: This tutorial guides the user through the process of finetuning the Llama-3 language model using Unsloth, enabling it to run locally or in Google Colab via Ollama. It details setup steps and explains various parameters for customizing the finetuning process.
tags:
    - llama-3
    - finetuning
    - ollama
    - unsloth
    - llm-tutorial
    - google-colab
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:22:00Z
---

# Tutorial: How to Finetune Llama-3 and Use In Ollama

Finetune Llama-3 with [Unsloth](https://github.com/unslothai/unsloth) for free, then run it locally via [Ollama](https://github.com/ollama/ollama) or in a free Google Colab GPU instance. Unsloth automatically exports to Ollama with integrated `Modelfile` creation.

> [!warning] Full code available in the [Ollama Colab notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3_\(8B\)-Ollama.ipynb) -- copy directly or adapt for local setup.

Help: [Unsloth Discord](https://discord.com/invite/unsloth) | [Ollama Discord](https://discord.gg/ollama)

## 1. What is Unsloth?

[Unsloth](https://github.com/unslothai/unsloth) makes finetuning LLMs (Llama-3, Mistral, Phi-3, Gemma) 2x faster with 70% less memory, no accuracy degradation. Free notebooks:

- [Ollama Llama-3 Alpaca](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3_\(8B\)-Ollama.ipynb) (used in this tutorial)
- [CSV/Excel Ollama Guide](https://colab.research.google.com/drive/1VYkncZMfGFkeCEgN2IzbZIKEDkyQuJAS?usp=sharing)

Requires Google account login.

## 2. What is Ollama?

[Ollama](https://github.com/ollama/ollama) runs LLMs locally. Launches a background process that serves a model like Llama-3 -- submit requests and get responses. Used as inference engine in this tutorial.

## 3. Install Unsloth

**Colab notebook basics:**

1. **Play button** at each cell -- run cells in order, no skipping. `CTRL + ENTER` as alternative.
2. **Runtime > Run all** -- runs entire notebook (skips customization steps, good first try).
3. **Connect / Reconnect T4** -- advanced system stats.

First cell installs the open-source Unsloth package plus dependencies.

## 4. Selecting a Model

Default: Llama-3 (Meta), trained on 15T tokens (~350K encyclopedias). Other supported models: Mistral, Phi-3 (GPT-4 trained), Gemma (13T tokens). Unsloth supports Hugging Face model hub models -- errors if incompatible.

**Toggle settings:**

1. ```python
   max_seq_length = 2048
   ```
   Context length. Llama-3 native: 8192. Set 2048 for testing. Unsloth supports very long context finetuning (4x longer than alternatives).

2. ```python
   dtype = None
   ```
   Keep as `None`. Can set `torch.float16` or `torch.bfloat16` for newer GPUs.

3. ```python
   load_in_4bit = True
   ```
   4-bit quantization: 4x less memory, enables finetuning on free 16GB GPU. Trade-off: 1-2% accuracy degradation. Set `False` on larger GPUs (e.g., H100) for maximum accuracy.

## 5. Finetuning Parameters

Default values work well. Adjust to increase accuracy while preventing overfitting.

1. ```python
   r = 16, # Choose any number > 0 ! Suggested 8, 16, 32, 64, 128
   ```
   Rank. Larger = more memory, slower, more accuracy on hard tasks. Suggested: 8 (fast), up to 128. Too large causes overfitting.

2. ```python
   target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                     "gate_proj", "up_proj", "down_proj",],
   ```
   All modules finetuned. Removing some reduces memory but is not recommended.

3. ```python
   lora_alpha = 16,
   ```
   Scaling factor. Larger = learns more about dataset, but promotes overfitting. Suggest equal to `r` or `r * 2`.

4. ```python
   lora_dropout = 0, # Supports any, but = 0 is optimized
   ```
   Leave at 0 for faster training. Can reduce overfitting slightly.

5. ```python
   bias = "none",    # Supports any, but = "none" is optimized
   ```
   Leave as `"none"` for faster, less over-fit training.

6. ```python
   use_gradient_checkpointing = "unsloth", # True or "unsloth" for very long context
   ```
   Options: `True`, `False`, `"unsloth"`. `"unsloth"` reduces memory 30% extra and supports very long context. See [long-context blog](https://unsloth.ai/blog/long-context).

7. ```python
   random_state = 3407,
   ```
   Seed for deterministic, reproducible runs.

8. ```python
   use_rslora = False,  # We support rank stabilized LoRA
   ```
   Advanced: auto-sets effective `lora_alpha = 16` scaling.

9. ```python
   loftq_config = None, # And LoftQ
   ```
   Advanced: initializes LoRA matrices to top `r` singular vectors of weights. Can improve accuracy but may explode memory at start.

## 6. Alpaca Dataset

52,000 instruction-output pairs created by GPT-4. Made base LLM competitive with ChatGPT when Llama-1 released.

- GPT4 version: <https://huggingface.co/datasets/vicgalle/alpaca-gpt4>
- Original version: <https://github.com/tatsu-lab/stanford_alpaca>

Each row has 3 columns: **instruction**, **input**, **output**. Combined into 1 large prompt for **supervised instruction finetuning**.

## 7. Multiple Columns for Finetuning

ChatGPT-style finetuning requires 1 prompt, not multiple inputs. Multi-column datasets (e.g., Titanic: age, class, fare) must be merged into a single prompt.

Unsloth provides `to_sharegpt()` to merge columns in 1 call (other libraries require manual preparation).

**`to_sharegpt()` rules:**

- Enclose column names in curly braces `{}` -- these reference actual CSV/Excel columns
- Optional text in `[[]]` -- skipped if column is empty (handles missing values)
- Set `output_column_name` to the target/prediction column

**Optional column example** (Titanic with missing data):

| Embarked | Age | Fare |
|----------|-----|------|
| S | 23 | |
| | 18 | 7.25 |

Without `[[]]`: "Their fare is **EMPTY**"
With `[[]]`: empty columns are excluded entirely, producing clean prompts.

Titanic finetuning notebook: <https://colab.research.google.com/drive/1VYkncZMfGFkeCEgN2IzbZIKEDkyQuJAS?usp=sharing>

## 8. Multi-turn Conversations

Alpaca is single-turn; ChatGPT is multi-turn. Use `conversation_extension` parameter to merge random single-turn rows into multi-turn conversations. Set to 3 = merge 3 random rows into 1 conversation. Too long = slower training but potentially better chatbot.

Set `output_column_name` to the prediction column, then call `standardize_sharegpt()` to format the dataset correctly. Always call this.

## 9. Customizable Chat Templates

After merging columns, templates use 1 input and 1 output.

**Required fields:**
- `{INPUT}` -- instruction
- `{OUTPUT}` -- model output
- `{SYSTEM}` -- optional system prompt (like ChatGPT)

Supported formats: Alpaca, ChatML (OpenAI), Llama-3 (instruct version), custom templates for specific tasks (e.g., Titanic survival prediction).

## 10. Train the Model

Defaults work well. Only adjust for longer training or larger batch sizes.

1. ```python
   per_device_train_batch_size = 2,
   ```
   Increase for more GPU utilization and smoother training. May slow training due to padding. Prefer increasing `gradient_accumulation_steps` instead.

2. ```python
   gradient_accumulation_steps = 4,
   ```
   Simulates larger batch size without extra VRAM. Increase for smoother training loss curves.

3. ```python
   max_steps = 60, # num_train_epochs = 1,
   ```
   60 steps for fast demo. For full training: comment out `max_steps`, set `num_train_epochs = 1`. Suggest 1-3 epochs; more risks overfitting.

4. ```python
   learning_rate = 2e-4,
   ```
   Reduce for slower but higher-accuracy convergence. Suggested values: `2e-4`, `1e-4`, `5e-5`, `2e-5`.

**Training loss:** 0.5-1.0 is good for many tasks. Loss not decreasing = adjust settings. Loss at 0 = likely overfitting (check validation).

## 11. Inference

After training, call `FastLanguageModel.for_inference(model)` for 2x faster inference (Unsloth native). Set `max_new_tokens` higher (e.g., 256 or 1024) for longer responses. Supports multi-turn conversation context.

## 12. Saving the Model

Save as ~100MB LoRA adapter locally, or push to Hugging Face hub (requires [token](https://huggingface.co/settings/tokens)). Reload with `FastLanguageModel` for inference.

## 13. Exporting to Ollama

1. Install Ollama in Colab
2. Export to llama.cpp GGUF format

Set `False` to `True` for **1 row only** (not all rows). First row exports to `Q8_0` (8-bit). Popular alternative: `q4_k_m`. Export takes 5-10 minutes.

GGUF details: <https://github.com/ggerganov/llama.cpp>
Manual GGUF export: <https://github.com/unslothai/unsloth/wiki#manually-saving-to-gguf>

## 14. Automatic Modelfile Creation

Unsloth auto-generates the `Modelfile` Ollama requires, including the chat template used during finetuning. Then Ollama creates a compatible model from the Modelfile.

## 15. Ollama Inference

Call the model via the Ollama server running locally or in Colab background.

## 16. Interactive ChatGPT Style

1. Open terminal (left sidebar icon)
2. Press ENTER twice to clear output
3. Type `ollama run unsloth_model` and hit ENTER
4. Interact with the chatbot. `CTRL + D` to exit.

## Summary

Finetuned Llama-3 exported to Ollama with Unsloth (2x faster, 70% less VRAM), free in Google Colab.

- Alpaca dataset example: [Colab](https://colab.research.google.com/drive/1WZDi7APtQ9VsvOrQSSC5DDtxq159j8iZ?usp=sharing)
- CSV/Excel finetuning: [Colab](https://colab.research.google.com/drive/1VYkncZMfGFkeCEgN2IzbZIKEDkyQuJAS?usp=sharing)
- Full docs: [GitHub](https://github.com/unslothai/unsloth#-finetune-for-free)

---
# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://unsloth.ai/docs/get-started/fine-tuning-llms-guide/tutorial-how-to-finetune-llama-3-and-use-in-ollama.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

#llama-3 #finetuning #ollama #unsloth #tutorial
