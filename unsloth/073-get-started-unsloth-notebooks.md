---
title: Unsloth Notebooks
url: https://unsloth.ai/docs/get-started/unsloth-notebooks.md
source: llms
fetched_at: 2026-04-27T18:12:49.070004945-03:00
rendered_js: false
word_count: 897
summary: This document serves as a hub and guide to Unsloth Notebooks, providing users with access to pre-configured Colab notebooks for training various large language models using free GPU compute. It organizes these notebooks by functionality such as SFT training, GRPO (Reinforcement Learning), Text-to-Speech, and Vision tasks.
tags:
    - notebook-guide
    - model-training
    - unsloth-studio
    - llm-examples
    - gpu-compute
    - gemma-4
    - reinforcement-learning
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Unsloth Notebooks

Pre-configured Colab notebooks for training LLMs with free GPU compute. Click **Run all** (or save locally), add your dataset, train, and deploy. Any model works in any notebook.

GitHub repo: [github.com/unslothai/notebooks](https://github.com/unslothai/notebooks/)

## Colab notebooks

[[097-new-studio|Unsloth Studio]] — train and run models under 22B parameters:

[Unsloth Studio Colab](https://colab.research.google.com/github/unslothai/unsloth/blob/main/studio/Unsloth_Studio_Colab.ipynb)

### Standard SFT notebooks

- [**Gemma 4**](https://unsloth.ai/docs/models/gemma-4/train): [E4B (Vision)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma4_\(E4B\)-Vision.ipynb) | [E2B (Text)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma4_\(E2B\)-Text.ipynb) | [E2B (Audio)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma4_\(E2B\)-Audio.ipynb) | [31B (Kaggle)](https://www.kaggle.com/code/danielhanchen/gemma4-31b-unsloth) | [Inference](https://colab.research.google.com/github/unslothai/unsloth/blob/main/studio/Unsloth_Studio_Colab.ipynb)
- [**Qwen3.5**](https://unsloth.ai/docs/models/qwen3.5/fine-tune): [0.8B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_\(0_8B\)_Vision.ipynb) | [2B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_\(2B\)_Vision.ipynb) | [4B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_\(4B\)_Vision.ipynb)
- [gpt-oss (20B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-\(20B\)-Fine-tuning.ipynb) | [Inference](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/GPT_OSS_MXFP4_\(20B\)-Inference.ipynb) | [Fine-tuning](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-\(20B\)-Fine-tuning.ipynb)
- [EmbeddingGemma (300M)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/EmbeddingGemma_\(300M\).ipynb)
- [Qwen3 (14B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(14B\)-Reasoning-Conversational.ipynb) | [Qwen3-VL (8B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_VL_\(8B\)-Vision.ipynb)
- [Qwen3-2507-4B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(4B\)-Instruct.ipynb) | [Thinking](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(4B\)-Thinking.ipynb) | [Instruct](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(4B\)-Instruct.ipynb)
- [Gemma 3 (4B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3_\(4B\).ipynb) | [Text](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3_\(4B\).ipynb) | [Vision](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3_\(4B\)-Vision.ipynb) | [270M](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3_\(270M\).ipynb) | [FunctionGemma](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/FunctionGemma_\(270M\).ipynb)
- [Gemma 3n (E4B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3N_\(4B\)-Conversational.ipynb) | [Text](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3N_\(4B\)-Conversational.ipynb) | [Vision](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3N_\(4B\)-Vision.ipynb) | [Audio](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3N_\(4B\)-Audio.ipynb)
- [Mistral Ministral 3](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Ministral_3_VL_\(3B\)_Vision.ipynb)
- [DeepSeek-OCR 2](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Deepseek_OCR_2_\(3B\).ipynb)
- [IBM Granite-4.0-H](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Granite4.0.ipynb)
- [Phi-4 (14B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Phi_4-Conversational.ipynb)
- [Llama 3.1 (8B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.1_\(8B\)-Alpaca.ipynb) | [Llama 3.2 (1B + 3B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.2_\(1B_and_3B\)-Conversational.ipynb)

### GRPO (Reasoning RL)

- [Gemma 4 E2B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma4_\(E2B\)_Reinforcement_Learning_Sudoku_Game.ipynb) — new
- [Qwen3.5 (4B) Vision GRPO](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_\(4B\)_Vision_GRPO.ipynb)
- [gpt-oss-20b](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-\(20B\)-GRPO.ipynb) (automatic kernels creation)
- [Mistral Ministral 3 Sudoku](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Ministral_3_\(3B\)_Reinforcement_Learning_Sudoku_Game.ipynb) — new
- [Qwen3-8B FP8](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_8B_FP8_GRPO.ipynb) (L4) — new
- [Llama-3.2-1B FP8](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama_FP8_GRPO.ipynb) (L4) — new
- [gpt-oss-20b 2048](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt_oss_\(20B\)_Reinforcement_Learning_2048_Game.ipynb) (auto win 2048)
- [Qwen3-VL (8B) Vision GSPO](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_VL_\(8B\)-Vision-GRPO.ipynb)
- [Qwen3 (4B) Advanced GRPO LoRA](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(4B\)-GRPO.ipynb)
- [Gemma 3 (4B) Vision GSPO](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3_\(4B\)-Vision-GRPO.ipynb)
- [gpt-oss-20b 2048 OpenEnv](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/OpenEnv_gpt_oss_\(20B\)_Reinforcement_Learning_2048_Game.ipynb)
- [DeepSeek-R1-0528-Qwen3 (8B) multilingual](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/DeepSeek_R1_0528_Qwen3_\(8B\)_GRPO.ipynb)
- [Gemma 3 (1B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3_\(1B\)-GRPO.ipynb)
- [Llama 3.2 (3B) Advanced GRPO LoRA](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Advanced_Llama3_2_\(3B\)_GRPO_LoRA.ipynb)
- [Llama 3.1 (8B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.1_\(8B\)-GRPO.ipynb)
- [Phi-4 (14B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Phi_4_\(14B\)-GRPO.ipynb)
- [Mistral v0.3 (7B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Mistral_v0.3_\(7B\)-GRPO.ipynb)
- [NeMo Gym Multi Agents](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/NeMo-Gym-Multi-Environment.ipynb)

### Text-to-Speech (TTS)

- [Sesame-CSM (1B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Sesame_CSM_\(1B\)-TTS.ipynb)
- [Orpheus-TTS (3B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Orpheus_\(3B\)-TTS.ipynb)
- [Whisper Large V3 STT](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Whisper.ipynb)
- [Llasa-TTS (1B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llasa_TTS_\(1B\).ipynb)
- [Spark-TTS (0.5B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Spark_TTS_\(0_5B\).ipynb)
- [Oute-TTS (1B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Oute_TTS_\(1B\).ipynb)

**Speech-to-Text (STT):**

- [Gemma 4 (E2B) Audio](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma4_\(E2B\)-Audio.ipynb) — new
- [Whisper-Large-V3](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Whisper.ipynb)
- [Gemma 3n (E4B) Audio](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3N_\(4B\)-Audio.ipynb)

### Vision (Multimodal)

- [Gemma 4 E2B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma4_\(E2B\)-Vision.ipynb) — new
- [Qwen3.5](https://unsloth.ai/docs/models/qwen3.5/fine-tune): [0.8B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_\(0_8B\)_Vision.ipynb) | [2B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_\(2B\)_Vision.ipynb) | [4B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_\(4B\)_Vision.ipynb) — new
- [Qwen3-VL (8B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_VL_\(8B\)-Vision.ipynb)
- [Mistral Ministral 3](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Ministral_3_VL_\(3B\)_Vision.ipynb)
- [DeepSeek-OCR](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Deepseek_OCR_\(3B\).ipynb)
- [Paddle-OCR (1B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Paddle_OCR_\(1B\)_Vision.ipynb)
- [Gemma 3n (E4B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3N_\(4B\)-Vision.ipynb)
- [Gemma 3 (4B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3_\(4B\)-Vision.ipynb)
- [Llama 3.2 Vision (11B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.2_\(11B\)-Vision.ipynb)
- [Qwen2.5-VL (7B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen2.5_VL_\(7B\)-Vision.ipynb)
- [Pixtral (12B) 2409](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Pixtral_\(12B\)-Vision.ipynb)
- [Qwen3-VL Vision GSPO](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_VL_\(8B\)-Vision-GRPO.ipynb) — new
- [Qwen2.5-VL Vision GSPO](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen2_5_7B_VL_GRPO.ipynb)
- [Gemma 3 (4B) Vision GSPO](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3_\(4B\)-Vision-GRPO.ipynb)

### Embedding models

- [EmbeddingGemma (300M)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/EmbeddingGemma_\(300M\).ipynb) — new
- [Qwen3-Embedding 4B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_Embedding_\(4B\).ipynb) — new
- [Qwen3-Embedding 0.6B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_Embedding_\(0_6B\).ipynb) — new
- [BGE M3](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/BGE_M3.ipynb) — new
- [ModernBERT-large](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/bert_classification.ipynb) — new
- [All-MiniLM-L6-v2](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/All_MiniLM_L6_v2.ipynb) — new
- [GTE ModernBert](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/ModernBert.ipynb) — new

### Large LLMs

Exceed Colab's free 15 GB VRAM tier. With Colab's 80 GB GPUs, fine-tune up to 120B parameter models.

> [!info] Colab subscription or credits required. Unsloth earns nothing from these notebooks.

- [Gemma-4-31B (Kaggle)](https://www.kaggle.com/code/danielhanchen/gemma4-31b-unsloth) — new, FREE
- [Gemma-4-26B-A4B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma4_\(26B_A4B\)-Vision.ipynb) — new
- [Gemma-4-31B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma4_\(31B\)-Vision.ipynb) — new
- [Qwen3.5-35B-A3B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_MoE.ipynb)
- [Qwen3.5-27B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen_3_5_27B_A100\(80GB\).ipynb)
- [GLM-4.7-Flash](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/GLM_Flash_A100\(80GB\).ipynb)
- [gpt-oss-20b (500K context)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt_oss_\(20B\)_500K_Context_Fine_tuning.ipynb)
- [Qwen3-30B-A3B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_MoE.ipynb)
- [Nemotron-3-Nano-30B-A3B LoRA](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Nemotron-3-Nano-30B-A3B_A100.ipynb)
- [NeMo Gym Sudoku GRPO](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/NeMo-Gym-Sudoku.ipynb)
- [NeMo Gym Multi Environment GRPO](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/NeMo-Gym-Multi-Environment.ipynb)
- [gpt-oss-120b](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-\(120B\)_A100-Fine-tuning.ipynb)
- [Qwen3 (32B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(32B\)_A100-Reasoning-Conversational.ipynb)
- [Llama 3.3 (70B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.3_\(70B\)_A100-Conversational.ipynb)
- [Gemma 3 (27B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3_\(27B\)_A100-Conversational.ipynb)
- [Baidu ERNIE 4.5 VL (28B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/ERNIE_4_5_VL_28B_A3B_PT_Vision.ipynb) — new

### Other important notebooks

- [Customer support agent](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Granite4.0.ipynb)
- [Mistral Ministral 3 Sudoku](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Ministral_3_\(3B\)_Reinforcement_Learning_Sudoku_Game.ipynb) — new
- [Deploy on LM Studio](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/FunctionGemma_\(270M\)-LMStudio.ipynb) — new
- [Quantization-Aware Training (QAT)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(4B\)_Instruct-QAT.ipynb) — new
- [Phone Deployment](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(0_6B\)-Phone_Deployment.ipynb) — new
- [Reason before Tool Calling](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/FunctionGemma_\(270M\).ipynb) — new
- [Mobile Actions](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/FunctionGemma_\(270M\)-Mobile-Actions.ipynb) — new
- [Automatic Kernel Creation with RL](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-\(20B\)-GRPO.ipynb)
- [ModernBERT-large](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/bert_classification.ipynb) — new
- [Synthetic Data Generation Llama 3.2 (3B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Meta_Synthetic_Data_Llama3_2_\(3B\).ipynb)
- [gpt-oss-20b (500K context)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt_oss_\(20B\)_500K_Context_Fine_tuning.ipynb) — A100
- [Tool Calling](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen2.5_Coder_\(1.5B\)-Tool_Calling.ipynb)
- [Mistral v0.3 Instruct (7B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Mistral_v0.3_\(7B\)-Conversational.ipynb)
- [Ollama](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3_\(8B\)-Ollama.ipynb)
- [ORPO](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3_\(8B\)-ORPO.ipynb)
- [Continued Pretraining](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Mistral_v0.3_\(7B\)-CPT.ipynb)
- [DPO Zephyr](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Zephyr_\(7B\)-DPO.ipynb)
- [Inference only](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.1_\(8B\)-Inference.ipynb)
- [Llama 3 (8B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3_\(8B\)-Alpaca.ipynb)

### Specific use-case notebooks

- [Phone Deployment](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(0_6B\)-Phone_Deployment.ipynb) — new
- [Deploy on LM Studio](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/FunctionGemma_\(270M\)-LMStudio.ipynb) — new
- [Reason before Tool Calling](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/FunctionGemma_\(270M\).ipynb) — new
- [Mobile Actions](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/FunctionGemma_\(270M\)-Mobile-Actions.ipynb) — new
- [Customer support agent](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Granite4.0.ipynb)
- [Quantization-Aware Training (QAT)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(4B\)_Instruct-QAT.ipynb) — new
- [Automatic Kernel Creation with RL](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-\(20B\)-GRPO.ipynb) — new
- [DPO Zephyr](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Zephyr_\(7B\)-DPO.ipynb)
- [BERT Text Classification](https://colab.research.google.com/github/timothelaborie/text_classification_scripts/blob/main/unsloth_classification.ipynb) (AutoModelForSequenceClassification)
- [Ollama](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3_\(8B\)-Ollama.ipynb)
- [Tool Calling](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen2.5_Coder_\(1.5B\)-Tool_Calling.ipynb)
- [Continued Pretraining (CPT)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Mistral_v0.3_\(7B\)-CPT.ipynb)
- [Multiple Datasets](https://colab.research.google.com/drive/1njCCbE1YVal9xC83hjdo2hiGItpY_D6t?usp=sharing) by Flail
- [KTO](https://colab.research.google.com/drive/1MRgGtLWuZX4ypSfGguFgC-IblTvO2ivM?usp=sharing) by Jeffrey
- [Inference chat UI](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Unsloth_Studio.ipynb)
- [Conversational](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.2_\(1B_and_3B\)-Conversational.ipynb)
- [ChatML](https://colab.research.google.com/drive/15F1xyn8497_dUbxZP4zWmPZ3PJx1Oymv?usp=sharing)
- [Text Completion](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Mistral_\(7B\)-Text_Completion.ipynb)

### Rest of notebooks

- [Qwen2.5 (3B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen2.5_\(3B\)-GRPO.ipynb)
- [Gemma 2 (9B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma2_\(9B\)-Alpaca.ipynb)
- [Mistral NeMo (12B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Mistral_Nemo_\(12B\)-Alpaca.ipynb)
- [Phi-3.5 (mini)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Phi_3.5_Mini-Conversational.ipynb)
- [Phi-3 (medium)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Phi_3_Medium-Conversational.ipynb)
- [Gemma 2 (2B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma2_\(2B\)-Alpaca.ipynb)
- [Qwen 2.5 Coder (14B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen2.5_Coder_\(14B\)-Conversational.ipynb)
- [Mistral Small (22B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Mistral_Small_\(22B\)-Alpaca.ipynb)
- [TinyLlama](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/TinyLlama_\(1.1B\)-Alpaca.ipynb)
- [CodeGemma (7B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/CodeGemma_\(7B\)-Conversational.ipynb)
- [Mistral v0.3 (7B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Mistral_v0.3_\(7B\)-Alpaca.ipynb)
- [Qwen2 (7B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen2_\(7B\)-Alpaca.ipynb)

## Kaggle notebooks

#### Standard notebooks

- [Gemma-4-31B (Kaggle)](https://www.kaggle.com/code/danielhanchen/gemma4-31b-unsloth) — new, FREE
- [gpt-oss (20B)](https://www.kaggle.com/notebooks/welcome?src=https://github.com/unslothai/notebooks/blob/main/nb/Kaggle-gpt-oss-\(20B\)-Fine-tuning.ipynb\&accelerator=nvidiaTeslaT4)
- [Gemma 3n (E4B)](https://www.kaggle.com/code/danielhanchen/gemma-3n-4b-multimodal-finetuning-inference)
- [Qwen3 (14B)](https://www.kaggle.com/notebooks/welcome?src=https%3A%2F%2Fgithub.com%2Funslothai%2Fnotebooks%2Fblob%2Fmain%2Fnb%2FKaggle-Qwen3_\(14B\).ipynb)
- [Magistral-2509 (24B)](https://www.kaggle.com/notebooks/welcome?src=https://github.com/unslothai/notebooks/blob/main/nb/Kaggle-Magistral_\(24B\)-Reasoning-Conversational.ipynb\&accelerator=nvidiaTeslaT4)
- [Gemma 3 (4B)](https://www.kaggle.com/notebooks/welcome?src=https%3A%2F%2Fgithub.com%2Funslothai%2Fnotebooks%2Fblob%2Fmain%2Fnb%2FKaggle-Gemma3_\(4B\).ipynb)
- [Phi-4 (14B)](https://www.kaggle.com/notebooks/welcome?src=https%3A%2F%2Fgithub.com%2Funslothai%2Fnotebooks%2Fblob%2Fmain%2Fnb%2FKaggle-Phi_4-Conversational.ipynb)
- [Llama 3.1 (8B)](https://www.kaggle.com/notebooks/welcome?src=https%3A%2F%2Fgithub.com%2Funslothai%2Fnotebooks%2Fblob%2Fmain%2Fnb%2FKaggle-Llama3.1_\(8B\)-Alpaca.ipynb)
- [Llama 3.2 (1B + 3B)](https://www.kaggle.com/notebooks/welcome?src=https%3A%2F%2Fgithub.com%2Funslothai%2Fnotebooks%2Fblob%2Fmain%2Fnb%2FKaggle-Llama3.2_\(1B_and_3B\)-Conversational.ipynb)
- [Qwen 2.5 (7B)](https://www.kaggle.com/notebooks/welcome?src=https%3A%2F%2Fgithub.com%2Funslothai%2Fnotebooks%2Fblob%2Fmain%2Fnb%2FKaggle-Qwen2.5_\(7B\)-Alpaca.ipynb)

#### GRPO (Reasoning) notebooks

- [Qwen2.5-VL Vision GRPO](https://www.kaggle.com/notebooks/welcome?src=https://github.com/unslothai/notebooks/blob/main/nb/Kaggle-Qwen2_5_7B_VL_GRPO.ipynb\&accelerator=nvidiaTeslaT4) — new
- [Qwen3 (4B)](https://www.kaggle.com/notebooks/welcome?src=https://github.com/unslothai/notebooks/blob/main/nb/Kaggle-Qwen3_\(4B\)-GRPO.ipynb\&accelerator=nvidiaTeslaT4)
- [Gemma 3 (1B)](https://www.kaggle.com/notebooks/welcome?src=https://github.com/unslothai/notebooks/blob/main/nb/Kaggle-Gemma3_\(1B\)-GRPO.ipynb)
- [Llama 3.1 (8B)](https://www.kaggle.com/notebooks/welcome?src=https://github.com/unslothai/notebooks/blob/main/nb/Kaggle-Llama3.1_\(8B\)-GRPO.ipynb)
- [Phi-4 (14B)](https://www.kaggle.com/notebooks/welcome?src=https://github.com/unslothai/notebooks/blob/main/nb/Kaggle-Phi_4_\(14B\)-GRPO.ipynb)
- [Qwen 2.5 (3B)](https://www.kaggle.com/notebooks/welcome?src=https://github.com/unslothai/notebooks/blob/main/nb/Kaggle-Qwen2.5_\(3B\)-GRPO.ipynb)

#### Text-to-Speech (TTS) notebooks

- [Sesame-CSM (1B)](https://www.kaggle.com/notebooks/welcome?src=https%3A%2F%2Fgithub.com%2Funslothai%2Fnotebooks%2Fblob%2Fmain%2Fnb%2FKaggle-Sesame_CSM_\(1B\)-TTS.ipynb)
- [Orpheus-TTS (3B)](https://www.kaggle.com/notebooks/welcome?src=https%3A%2F%2Fgithub.com%2Funslothai%2Fnotebooks%2Fblob%2Fmain%2Fnb%2FKaggle-Orpheus_\(3B\)-TTS.ipynb)
- [Whisper Large V3 STT](https://www.kaggle.com/notebooks/welcome?src=https%3A%2F%2Fgithub.com%2Funslothai%2Fnotebooks%2Fblob%2Fmain%2Fnb%2FKaggle-Whisper.ipynb)
- [Llasa-TTS (1B)](https://www.kaggle.com/notebooks/welcome?src=https%3A%2F%2Fgithub.com%2Funslothai%2Fnotebooks%2Fblob%2Fmain%2Fnb%2FKaggle-Llasa_TTS_\(1B\).ipynb)
- [Spark-TTS (0.5B)](https://www.kaggle.com/notebooks/welcome?src=https%3A%2F%2Fgithub.com%2Funslothai%2Fnotebooks%2Fblob%2Fmain%2Fnb%2FKaggle-Spark_TTS_\(0_5B\).ipynb)
- [Oute-TTS (1B)](https://www.kaggle.com/notebooks/welcome?src=https%3A%2F%2Fgithub.com%2Funslothai%2Fnotebooks%2Fblob%2Fmain%2Fnb%2FKaggle-Oute_TTS_\(1B\).ipynb)

#### Vision (Multimodal) notebooks

- [Llama 3.2 Vision (11B)](https://www.kaggle.com/notebooks/welcome?src=https%3A%2F%2Fgithub.com%2Funslothai%2Fnotebooks%2Fblob%2Fmain%2Fnb%2FKaggle-Llama3.2_\(11B\)-Vision.ipynb)
- [Qwen 2.5-VL (7B)](https://www.kaggle.com/notebooks/welcome?src=https%3A%2F%2Fgithub.com%2Funslothai%2Fnotebooks%2Fblob%2Fmain%2Fnb%2FKaggle-Qwen2.5_VL_\(7B\)-Vision.ipynb)
- [Pixtral (12B) 2409](https://www.kaggle.com/notebooks/welcome?src=https%3A%2F%2Fgithub.com%2Funslothai%2Fnotebooks%2Fblob%2Fmain%2Fnb%2FKaggle-Pixtral_\(12B\)-Vision.ipynb)

#### Specific use-case notebooks

- [Tool Calling](https://www.kaggle.com/notebooks/welcome?src=https://github.com/unslothai/notebooks/blob/main/nb/Kaggle-Qwen2.5_Coder_\(1.5B\)-Tool_Calling.ipynb\&accelerator=nvidiaTeslaT4)
- [ORPO](https://www.kaggle.com/notebooks/welcome?src=https://github.com/unslothai/notebooks/blob/main/nb/Kaggle-Llama3_\(8B\)-ORPO.ipynb)
- [Continued Pretraining](https://www.kaggle.com/notebooks/welcome?src=https://github.com/unslothai/notebooks/blob/main/nb/Kaggle-Mistral_v0.3_\(7B\)-CPT.ipynb)
- [DPO Zephyr](https://www.kaggle.com/notebooks/welcome?src=https://github.com/unslothai/notebooks/blob/main/nb/Kaggle-Zephyr_\(7B\)-DPO.ipynb)
- [Inference only](https://www.kaggle.com/notebooks/welcome?src=https://github.com/unslothai/notebooks/blob/main/nb/Kaggle-Llama3.1_\(8B\)-Inference.ipynb)
- [Ollama](https://www.kaggle.com/notebooks/welcome?src=https://github.com/unslothai/notebooks/blob/main/nb/Kaggle-Llama3_\(8B\)-Ollama.ipynb)
- [Text Completion](https://www.kaggle.com/notebooks/welcome?src=https://github.com/unslothai/notebooks/blob/main/nb/Kaggle-Mistral_\(7B\)-Text_Completion.ipynb)
- [CodeForces-cot (Reasoning)](https://www.kaggle.com/notebooks/welcome?src=https://github.com/unslothai/notebooks/blob/main/nb/Kaggle-CodeForces-cot-Finetune_for_Reasoning_on_CodeForces.ipynb)
- [Unsloth Studio (chat UI)](https://www.kaggle.com/notebooks/welcome?src=https://github.com/unslothai/notebooks/blob/main/nb/Kaggle-Unsloth_Studio.ipynb)

#### Rest of notebooks

- [Gemma 2 (9B)](https://www.kaggle.com/notebooks/welcome?src=https%3A%2F%2Fgithub.com%2Funslothai%2Fnotebooks%2Fblob%2Fmain%2Fnb%2FKaggle-Gemma2_\(9B\)-Alpaca.ipynb)
- [Gemma 2 (2B)](https://www.kaggle.com/notebooks/welcome?src=https%3A%2F%2Fgithub.com%2Funslothai%2Fnotebooks%2Fblob%2Fmain%2Fnb%2FKaggle-Gemma2_\(2B\)-Alpaca.ipynb)
- [CodeGemma (7B)](https://www.kaggle.com/notebooks/welcome?src=https%3A%2F%2Fgithub.com%2Funslothai%2Fnotebooks%2Fblob%2Fmain%2Fnb%2FKaggle-CodeGemma_\(7B\)-Conversational.ipynb)
- [Mistral NeMo (12B)](https://www.kaggle.com/notebooks/welcome?src=https%3A%2F%2Fgithub.com%2Funslothai%2Fnotebooks%2Fblob%2Fmain%2Fnb%2FKaggle-Mistral_Nemo_\(12B\)-Alpaca.ipynb)
- [Mistral Small (22B)](https://www.kaggle.com/notebooks/welcome?src=https%3A%2F%2Fgithub.com%2Funslothai%2Fnotebooks%2Fblob%2Fmain%2Fnb%2FKaggle-Mistral_Small_\(22B\)-Alpaca.ipynb)
- [TinyLlama (1.1B)](https://www.kaggle.com/notebooks/welcome?src=https%3A%2F%2Fgithub.com%2Funslothai%2Fnotebooks%2Fblob%2Fmain%2Fnb%2FKaggle-TinyLlama_\(1.1B\)-Alpaca.ipynb)

Full Kaggle list: [github.com/unslothai/notebooks#kaggle-notebooks](https://github.com/unslothai/notebooks#-kaggle-notebooks)

> [!info] Contribute to notebooks at the [repo](https://github.com/unslothai/notebooks).

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://unsloth.ai/docs/get-started/unsloth-notebooks.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

#unsloth-notebooks #colab #kaggle #grpo #llm-training
