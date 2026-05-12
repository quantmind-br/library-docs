---
title: Fine-tuning LLMs Guide
url: https://unsloth.ai/docs/get-started/fine-tuning-llms-guide.md
source: llms
fetched_at: 2026-04-27T18:13:02.472642178-03:00
rendered_js: false
word_count: 2277
summary: This guide explains the concept of fine-tuning Large Language Models (LLMs), detailing various training methods like Supervised Fine-Tuning (SFT), Reinforcement Learning (RL), LoRA, and QLoRA. It advises users on selecting the right model and configuration settings for effective customization.
tags:
    - llm-fine-tuning
    - lora-qlora
    - supervised-finetuning
    - reinforcement-learning
    - model-customization
    - training-methods
category: guide
optimized: true
optimized_at: 2026-04-27T21:15:00Z
---

# Fine-tuning LLMs Guide

## 1. What Is Fine-tuning?

Fine-tuning / post-training customizes model behavior, injects knowledge, and optimizes performance for specific domains and tasks.

- OpenAI's GPT-5 was post-trained to improve instruction following and chat behavior.
- Standard method: **Supervised Fine-Tuning (SFT)**. Other methods: preference optimization (DPO, ORPO), distillation, and [Reinforcement Learning (RL)](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide) (GRPO, GSPO) where an agent learns via reward/penalty feedback.
- With [Unsloth](https://github.com/unslothai/unsloth), fine-tune or do RL for free on Colab, Kaggle, or locally with just 3GB VRAM using [notebooks](https://docs.unsloth.ai/get-started/unsloth-notebooks).

**Benefits of fine-tuning:**
- **Update + Learn New Knowledge** — inject domain-specific information.
- **Customize Behavior** — adjust tone, personality, response style.
- **Optimize for Tasks** — improve accuracy for specific use cases.

**Example use-cases:**
- Predict if a headline impacts a company positively or negatively.
- Use historical customer interactions for custom responses.
- Fine-tune on legal texts for contract analysis, case law research, compliance.

A fine-tuned model is a specialized agent for specific tasks. **Fine-tuning can replicate all of RAG's capabilities, but not vice versa.**

### What is LoRA/QLoRA?

LLMs have model weights (e.g., Llama 70B has 70B numbers). Instead of changing all weights, LoRA adds thin matrices A and B to each weight and optimizes those — only ~1% of weights. LoRA uses 16-bit unquantized base model; QLoRA quantizes to 4-bit, saving 75% memory.

### Fine-tuning misconceptions

Claims that fine-tuning doesn't teach new knowledge or that RAG outperforms fine-tuning are **false**. Fine-tuning changes model weights; RAG only augments inference-time input. See [[122-get-started-fine-tuning-for-beginners-faq-+-is-fine-tuning-right-for-me|FAQ + Is Fine-tuning Right For Me?]].

> [!tip] **Introducing Unsloth Studio:** Open-source web UI for no-code training and running models with observability and automatic dataset creation. See [[097-new-studio|Introducing Unsloth Studio]].

## 2. Choose the Right Model + Method

Start with a small instruct model like Llama 3.1 (8B) and experiment.

### Training methods

- **RL** — for specific behaviors (e.g., tool-calling) via environment + reward function. Most use-cases are served by SFT. See [notebook examples](https://unsloth.ai/docs/unsloth-notebooks#grpo-reasoning-rl-notebooks).
- **LoRA** — parameter-efficient: freezes base weights, trains small low-rank adapters (16-bit).
- **QLoRA** — LoRA + 4-bit precision for large models with minimal resources.
- **Full Fine-Tuning (FFT)** / pretraining — requires significantly more resources; usually unnecessary. LoRA can match FFT when done correctly.
- Unsloth also supports: [[094-basics-text-to-speech-tts-fine-tuning|TTS]], [[079-basics-embedding-finetuning|embedding]], GRPO, RL, [[096-basics-vision-fine-tuning|vision]], multimodal.

> [!info] **Train and serve in the same precision** to preserve accuracy (4-bit train → 4-bit serve, etc.)

**Recommendation:** Start with QLoRA — most accessible and effective. Unsloth's [dynamic 4-bit](https://unsloth.ai/blog/dynamic-4bit) quants largely recover the accuracy gap vs LoRA.

Change model name to match Hugging Face, e.g., `unsloth/llama-3.1-8b-unsloth-bnb-4bit`.

### Instruct vs Base models

Start with **Instruct models** — use conversational chat templates (ChatML, ShareGPT) and require less data. Base models use Alpaca, Vicuna etc. See [[063-get-started-fine-tuning-llms-guide-what-model-should-i-use|What Model Should I Use for Fine-tuning?]].

### Model naming conventions

| Suffix | Meaning |
|--------|---------|
| `unsloth-bnb-4bit` | Unsloth dynamic 4-bit quant (higher accuracy, slightly more VRAM than standard) |
| `bnb-4bit` (without "unsloth") | Standard BitsAndBytes 4-bit quantization |
| No suffix | Original 16-bit or 8-bit (may include chat template/tokenizer fixes) |

### Configuration settings

| Parameter | Description |
|-----------|-------------|
| `max_seq_length = 2048` | Context length. Llama-3 supports 8192; 2048 recommended for testing. Unsloth enables 4x longer context fine-tuning. |
| `dtype = None` | Default; use `torch.float16` or `torch.bfloat16` for newer GPUs. |
| `load_in_4bit = True` | 4-bit quantization, 4x memory reduction. Disable for 16-bit LoRA. Use `load_in_16bit = True` for explicit 16-bit LoRA. |
| `full_finetuning = True` | Enable FFT. Use `load_in_8bit = True` for 8-bit fine-tuning. |

> [!info] Only one training method can be `True` at a time. Avoid jumping to FFT — test LoRA/QLoRA first. If LoRA fails, FFT won't magically fix it.

Additional training: [[094-basics-text-to-speech-tts-fine-tuning|TTS]], [[072-get-started-reinforcement-learning-rl-guide|GRPO/RL]], [[096-basics-vision-fine-tuning|vision]], [[069-get-started-reinforcement-learning-rl-guide-preference-dpo-orpo-and-kto|DPO/ORPO/KTO]], [[111-basics-continued-pretraining|continued pretraining]], text completion.

- Model selection guide: [[063-get-started-fine-tuning-llms-guide-what-model-should-i-use|What Model Should I Use for Fine-tuning?]]
- Per-model tutorials: [[050-models-tutorials|Large language model (LLMs) Tutorials]]

## 3. Your Dataset

Datasets are collections of tokenizable text data for training.

- Create a dataset with 2 columns (question + answer). Quality and amount directly reflect fine-tune results.
- [Synthetically generate data](https://unsloth.ai/docs/get-started/datasets-guide#synthetic-data-generation) via ChatGPT or local LLMs.
- Use the [Synthetic Dataset notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Meta_Synthetic_Data_Llama3_2_\(3B\).ipynb) to auto-parse documents (PDFs, videos), generate QA pairs, and clean data using local models.
- For most use-cases, curate well-structured QA pairs. Exception: code fine-tuning can work well with raw code dumps.

More: [[060-get-started-fine-tuning-llms-guide-datasets-guide|Datasets Guide]]

Most notebook examples use the [Alpaca dataset](https://docs.unsloth.ai/basics/tutorial-how-to-finetune-llama-3-and-use-in-ollama#id-6.-alpaca-dataset); vision notebooks use different datasets with images.

## 4. Understand Training Hyperparameters

See [[061-get-started-fine-tuning-llms-guide-lora-hyperparameters-guide|LoRA fine-tuning Hyperparameters Guide]] for best practices on how each hyperparameter affects model performance.

## 5. Install + Requirements

### Unsloth Notebooks

Beginners: use pre-made [[073-get-started-unsloth-notebooks|Unsloth Notebooks]] with guided steps. Export to local later. Covers TTS, embedding, GRPO, RL, vision, multimodal, and more.

### Local Installation

Install via [Docker](https://unsloth.ai/docs/get-started/install/docker) or `pip install unsloth` (Linux, WSL, [Windows](https://unsloth.ai/docs/get-started/install/windows-installation)).

- Requirements: [[112-get-started-fine-tuning-for-beginners-unsloth-requirements|Unsloth Requirements]]
- Install guide: [[058-get-started-install|Unsloth Installation]]

## 6. Training + Evaluation

### Training

Training loss shows learning progress. Loss ~0.5–1.0 is generally good (dataset/task dependent). If loss isn't decreasing, adjust settings. Loss going to 0 may indicate overfitting — check validation.

**Default training parameters:**

| Parameter | Description |
|-----------|-------------|
| `per_device_train_batch_size = 2` | Increase for better GPU utilization (beware padding slowdown). Increase `gradient_accumulation_steps` instead for smoother training. |
| `gradient_accumulation_steps = 4` | Simulates larger batch size without more memory. |
| `max_steps = 60` | Speeds up training. For full runs use `num_train_epochs = 1` (1–3 epochs recommended). |
| `learning_rate = 2e-4` | Lower for slower, more precise fine-tuning. Try `1e-4`, `5e-5`, `2e-5`. |

### Evaluation

- Manual: chat with the model and judge quality.
- Enable Unsloth evaluation (can be time-consuming). Speed up by reducing eval dataset size or setting `evaluation_steps = 100`.
- Test split: use 20% of training data. If all data was used for training, manual eval is required.
- Automated eval tools may not align with your criteria.

## 7. Running + Deploying the Model

After training, use the model for inference. For multi-turn chatbots, pass conversation history.

Always call `FastLanguageModel.for_inference(model)` for **2x faster inference**. Set `max_new_tokens = 128` (or larger like 256, 1024) for longer responses.

### Saving + Deployment

Save the LoRA adapter (~100MB) on top of the base model, or push to Hugging Face Hub (requires [token](https://huggingface.co/settings/tokens)).

- Deployment overview: [[091-basics-inference-and-deployment|Inference & Deployment]]
- Single device (laptop/Mac) → convert to GGUF for Ollama, llama.cpp, LM Studio: [[086-basics-inference-and-deployment-saving-to-gguf|Saving to GGUF]]
- Enterprise/multi-user (FP8, AWQ) → use vLLM: [[090-basics-inference-and-deployment-vllm-guide|vLLM Deployment & Inference Guide]]

After saving, reload with `FastLanguageModel` for inference.

## 8. We're Done!

Successfully fine-tuned and exported a language model with Unsloth.

- More tips: <https://unsloth.ai/blog/>
- Help: [Discord](https://discord.gg/unsloth) or [Reddit r/unsloth](https://www.reddit.com/r/unsloth/)

---

# Agent Instructions: Querying This Documentation

For info not on this page, query dynamically:

```
GET https://unsloth.ai/docs/get-started/fine-tuning-llms-guide.md?ask=<question>
```

Specific, self-contained natural language question. Returns direct answer with excerpts and sources.

#llm-fine-tuning #lora-qlora #supervised-finetuning #reinforcement-learning
