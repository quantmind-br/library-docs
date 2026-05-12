---
title: Reinforcement Learning (RL) Guide
url: https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide.md
source: llms
fetched_at: 2026-04-27T18:13:08.393319918-03:00
rendered_js: false
word_count: 3980
summary: This guide introduces Reinforcement Learning (RL) by defining its core components like agent, environment, action, and reward. It details various RL methodologies including RLHF, PPO, GRPO, and RLVR, explaining how they optimize an agent's decision-making process.
tags:
    - reinforcement-learning
    - rl-guide
    - grpo
    - ppo
    - rlhf
    - reward-function
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Reinforcement Learning (RL) Guide

RL: an "agent" learns decisions by interacting with an environment, receiving **rewards** or **penalties** as feedback.

- **Action** — what the model generates (e.g. a sentence)
- **Reward** — signal indicating quality (followed instructions? helpful?)
- **Environment** — the scenario/task (e.g. answering a user's question)

**Topics covered:** RL, RLVR, PPO, GRPO, RLHF, RFT, reward functions. From beginner to advanced. Step-by-step GRPO tutorial: [[070-get-started-reinforcement-learning-rl-guide-tutorial-train-your-own-reasoning-model-with-grpo|Train your own Reasoning model with GRPO]].

> [!tip] Updates
> **Jan 15, 2026:** [[067-get-started-reinforcement-learning-rl-guide-grpo-long-context|Ultra long context RL]] — train gpt-oss with 380K context window.
>
> **Nov 26, 2025:** [[066-get-started-reinforcement-learning-rl-guide-fp8-reinforcement-learning|FP8 precision RL and GRPO]] in Unsloth.

## What is Reinforcement Learning (RL)?

**Goal:**
1. **Increase** probability of **good** outcomes
2. **Decrease** probability of **bad** outcomes

**Pacman example:**
- **Environment:** game world
- **Actions:** UP, LEFT, RIGHT, DOWN
- **Rewards:** +eat cookie, -hit enemy
- RL observes intermediate steps or final state (win/lose), cannot know the "best action" directly

**Math example ("What is 2+2?"):** Unaligned LLM outputs 3, 4, C, D, -10 randomly. Numbers > letters. 3 > 8. 4 is correct. That's a **reward function**.

## From RLHF, PPO to GRPO and RLVR

### RLHF

[RLHF](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback) (Reinforcement Learning from Human Feedback) — OpenAI popularized. Train an agent to produce outputs rated more useful by humans (e.g. ChatGPT thumbs up/down).

### PPO

[PPO](https://en.wikipedia.org/wiki/Proximal_policy_optimization) (Proximal Policy Optimization) — developed to do RLHF. The agent is the language model. Composed of 3 systems:

1. **Generating Policy** (current trained model)
2. **Reference Policy** (original model)
3. **Value Model** (average reward estimator)

Uses a **Reward Model** to calculate reward; goal is to **maximize** it. PPO formula uses `clip(..., 1-ε, 1+ε)` to limit change magnitude + KL divergence term (β > 0) to prevent deviation. See [AI Engineer talk](https://docs.unsloth.ai/ai-engineers-2025) for deeper maths.

### GRPO

[GRPO](https://unsloth.ai/blog/grpo) (Group Relative Policy Optimization) — DeepSeek developed for R1 reasoning models. Key differences from PPO:

1. **Value Model removed** — replaced with statistics from multiple reward function calls
2. **Reward Model removed** — replaced with custom reward functions (enabling **RLVR**)

Result: extremely efficient — saves memory and speed by removing 2 models.

### RLVR (Reinforcement Learning with Verifiable Rewards)

Reward based on tasks with easily verifiable solutions:

- Math equations (2+2=4)
- Code execution correctness
- Beyond math/code: email automation, database retrieval, law, medicine — define a **rubric** (list of smaller verifiable rewards, not one singular reward). OpenAI popularized this in [RFT](https://platform.openai.com/docs/guides/reinforcement-fine-tuning).

### "Group Relative" — How GRPO Estimates Average Reward

Sample the LLM multiple times, calculate average reward through statistics across different questions.

**Example ("What is 2+2?"):** Sample 4 times → 4, 3, D, C. Calculate reward for each, then **average reward** + **standard deviation** → **Z-score standardize** → creates **advantages A** replacing the value model. Saves significant memory.

## "Luck" (Patience) Is All You Need

RL needs only 2 things:

1. A question/instruction (e.g. "What is 2+2?")
2. A reward function/verifier

Call the LLM repeatedly until a good answer appears. An untrained model might output: 0, cat, -10, 1928, 3, A, B... **then suddenly 4**. Reward signals: 0, 0, 0... **then suddenly 1**.

**Core insight:** If the probability of the correct answer is > 0, you will eventually encounter it. RL provides efficiency — bad answers actively guide the model away from bad outputs, "pruning" the distribution toward correct answer space.

> [!danger] If probability is always 0, RL will never work
> This is why RL is typically applied to already instruction-finetuned models that can partially follow instructions, boosting probability above 0.

## What Unsloth Offers for RL

- **15GB VRAM:** transform models up to 17B parameters (Llama 3.1 8B, Phi-4 14B, Mistral 7B, Qwen2.5 7B) into reasoning models
- **Vision/multimodal RL** supported: [[071-get-started-reinforcement-learning-rl-guide-vision-reinforcement-learning-vlm-rl|Vision RL]]
- **Minimum 5GB VRAM** for models ≤ 1.5B parameters

> [!info] Advanced GRPO docs
> Batching, generation and training parameters: [[113-get-started-reinforcement-learning-rl-guide-advanced-rl-documentation|Advanced RL Documentation]].

### GRPO Notebooks

| [**Gemma 4 E2B**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma4_\(E2B\)_Reinforcement_Learning_Sudoku_Game.ipynb) **- new** | [Qwen3-VL-8B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_VL_\(8B\)-Vision-GRPO.ipynb) - Vision GSPO | [Gemma 3 (4B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3_\(4B\)-Vision-GRPO.ipynb) - Vision GSPO |
| --- | --- | --- |
| [**Qwen3.5 (4B)**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_\(4B\)_Vision_GRPO.ipynb) **- Vision - new** | [gpt-oss-20b](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-\(20B\)-GRPO.ipynb) GSPO | [Llama 3.2 (3B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Advanced_Llama3_2_\(3B\)_GRPO_LoRA.ipynb) - Advanced |
| [Qwen3 (4B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(4B\)-GRPO.ipynb) - Advanced | [Phi-4 (14B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Phi_4_\(14B\)-GRPO.ipynb) | [DeepSeek-R1-0528-Qwen3-8B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/DeepSeek_R1_0528_Qwen3_\(8B\)_GRPO.ipynb) |
| [Mistral v0.3 (7B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Mistral_v0.3_\(7B\)-GRPO.ipynb) | [Llama 3.1 (8B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.1_\(8B\)-GRPO.ipynb) | [Qwen3-8B - **FP8**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_8B_FP8_GRPO.ipynb) (L4) |

> [!tip] GSPO and other new GRPO techniques
>
> ```python
> epsilon=0.2,
> epsilon_high=0.28, # one sided
> delta=1.5 # two sided
>
> loss_type='gspo',
> # or:
> loss_type='grpo',
> # or:
> loss_type='dr_grpo',
>
> mask_truncated_completions=True,
> ```

**Key notes:**
- No reasoning? Ensure enough training steps + working [[#reward-functions-verifier|reward function/verifier]]
- Qwen2.5 (3B) "aha" moment: previously needed 2xA100 (160GB VRAM) — now single 5GB VRAM GPU via Unsloth
- GRPO now works with **QLoRA and LoRA** (not just full fine-tuning)
- **20K context, 8 generations:** Unsloth 54.3GB vs standard 510.8GB (**90% less**) for Llama 3.1 8B
- This is converting standard models into reasoning models via GRPO, not fine-tuning DeepSeek R1 distilled models

## Training with GRPO

Tutorial: [[070-get-started-reinforcement-learning-rl-guide-tutorial-train-your-own-reasoning-model-with-grpo|Train your own Reasoning model with GRPO]].

> [!info] Advanced GRPO
> See [[113-get-started-reinforcement-learning-rl-guide-advanced-rl-documentation|Advanced RL Documentation]].

### How GRPO Trains a Model

1. For each QA pair, generate multiple responses (e.g. 8 variations)
2. Evaluate each with reward functions
3. Training steps: 300 rows = 300 steps (or 900 for 3 epochs). Increase generations per question (8→16) for more signal
4. Model updates weights every step

> [!warning] Model not learning?
> Use [Advanced GRPO notebooks](https://unsloth.ai/docs/unsloth-notebooks#grpo-reasoning-notebooks) — better reward functions, faster results.

### Basics / Tips

- **Minimum 300 steps** for reward to increase. Optimal results may need 12+ hours. Can stop anytime.
- **At least 500 rows** of data recommended. 10 rows possible but less effective.
- Results vary by model, data, reward function — 300 steps is minimum, sometimes 1000+ needed.
- Local install: `pip install diffusers` if errors. Use latest vLLM.
- Apply GRPO to models **≥ 1.5B parameters** for correct thinking token generation.
- **VRAM (QLoRA 4-bit):** model parameters ≈ VRAM needed. More context = more VRAM. LoRA 16-bit uses ≥ 4x more.
- **Continuous fine-tuning** possible — leave GRPO running in background.
- Default dataset in notebooks: [GSM8K](#gsm8k-reward-functions) (most popular for R1-style training).
- Base models need a chat template.
- Training loss tracking built into Unsloth — no external tools (wandb) needed. Full logging for all reward functions.

### RL on Unsupported Models

For models not supported by vLLM (e.g. [Qwen3.5](https://unsloth.ai/docs/models/qwen3.5/fine-tune)), set `fast_inference=False`:

```python
from unsloth import FastLanguageModel

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/Qwen3.5-4B",
    fast_inference=False,
)
```

## Reward Functions / Verifiers

### Definitions

- **Verifier** — checks correctness (binary). Does not assign score. Can execute code to validate. Example: model outputs "5" for "2+2" → verifier labels "wrong".
- **Reward Function** — converts verification/criteria into numerical score. Correct → +1/+2, wrong → -1/-2. Can penalize length, readability, etc.
- **Key difference:** Verifier checks, Reward Function scores. Reward Function *can* use a Verifier but they are not the same.

### Understanding Reward Functions

GRPO maximizes reward and learns derivation, not memorization:

- Every step **adjusts model weights** to maximize reward
- Regular fine-tuning maximizes next-word prediction; GRPO **optimizes for a reward function**
- Data can be **reused across epochs**
- Default reward functions available, or generate custom ones via ChatGPT/local model
- Must be well-designed — poorly crafted rewards can degrade performance

### Reward Function Examples

#### Example #1: Simple Arithmetic

- **Question:** `"2 + 2"`
- **Answer:** `"4"`
- **Reward Function 1:** number detected → **+1**, no number → **-1**
- **Reward Function 2:** matches correct answer → **+3**, incorrect → **-3**
- **Total Reward:** sum of all reward functions

#### Example #2: Email Automation

- **Question:** Inbound email
- **Answer:** Outbound email
- **Reward Functions:** required keyword → **+1**, exact match → **+1**, too long → **-1**, recipient name → **+1**, signature block → **+1**

### Unsloth Proximity-Based Reward Function

Custom reward function in [[070-get-started-reinforcement-learning-rl-guide-tutorial-train-your-own-reasoning-model-with-grpo|Advanced GRPO Notebook]] — rewards answers closer to correct one:

- Enables reasoning in Qwen3 (Base)
- Pre-finetuning strategies to avoid learning only formatting
- Regex-based matching for evaluation accuracy
- Custom GRPO templates beyond generic `think` prompts (e.g. `<start_working_out></end_working_out>`)
- Proximity-based scoring — closer answers get more reward (9 vs 10 is better than 3 vs 10), outliers penalized

### GSM8K Reward Functions

By [@willccbb](https://x.com/willccbb) — popular and effective:

- **`correctness_reward_func`** — rewards exact label matches
- **`int_reward_func`** — encourages integer-only answers
- **`soft_format_reward_func`** — checks structure, allows minor newline mismatches
- **`strict_format_reward_func`** — ensures response structure matches prompt including newlines
- **`xmlcount_reward_func`** — ensures exactly one of each XML tag

## Using vLLM

[vLLM](https://github.com/vllm-project/vllm/) in finetuning stack for higher throughput + simultaneous inference. Performance: ~4000 tokens/s on 1x A100 40GB (Unsloth dynamic 4bit, Llama 3.2 3B Instruct), ~300 tokens/s on 16GB Tesla T4 (free Colab).

Unsloth removes double memory usage when loading vLLM + Unsloth together (saves ~5GB for Llama 3.1 8B, ~3GB for Llama 3.2 3B). Llama 3.3 70B finetuning fits in 1x 48GB GPU.

```python
# pip install unsloth vllm
from unsloth import FastLanguageModel
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/Llama-3.2-3B-Instruct",
    fast_inference = True,
)
```

## GRPO Requirement Guidelines

Unsloth reduces VRAM usage **90%+** vs standard implementations with Flash Attention 2.

### VRAM Rules

1. **QLoRA 4-bit:** model parameters ≈ VRAM needed (safe estimate). More context = more VRAM. LoRA 16-bit = ≥ 4x VRAM.
2. **Memory efficient linear kernels:** 8x+ memory reduction (saves 68.5GB), faster via `torch.compile`.
3. **Unsloth gradient checkpointing:** async offload of intermediate activations to RAM, only 1% slower (saves 52GB).
4. **Shared GPU/CUDA memory** with vLLM inference engine (saves 16GB vs separate allocations).

### Memory Comparison (Llama 3.1 8B, 20K context, 8 generations)

| Metric | Unsloth | Standard + FA2 |
| --- | --- | --- |
| Training Memory Cost (GB) | 42 | 414 |
| GRPO Memory Cost (GB) | 9.8 | 78.3 |
| Inference Cost (GB) | 0 | 16 |
| Inference KV Cache 20K (GB) | 2.5 | 2.5 |
| **Total Memory Usage (GB)** | **54.33 (90% less)** | **510.8** |

**Standard GRPO** needs 2 logits of size (8, 20K) for GRPO loss: 2 × 2 bytes × 8 × 20K × 128256 (vocab) = **78.3GB**. Unsloth shaves 8x → only **9.8GB** extra.

**KV Cache (16-bit):** Llama 3.1 8B = 32 layers, K/V = 1024. 20K context = 2 × 2 bytes × 32 × 20K × 1024 = **2.5GB** per batch (batch size 1; batch size 8 = ~20GB).

## Video Tutorials

- [Unsloth RL 3-hour Workshop](https://www.youtube.com/watch?v=OkEGJ5G3foU)
- [GRPO Overview](https://www.youtube.com/watch?v=9t-BAjzBWj8)
- [Dataset prep + RL/GRPO basics](https://www.youtube.com/watch?t=3289s&v=bbFEYPx9Hpo)
- [GRPO Tutorial](https://www.youtube.com/watch?v=oF0_eMhzRaQ)
- [GRPO Walkthrough](https://www.youtube.com/watch?v=juOh1afy-IE)
- [Local GRPO on your own device](https://www.youtube.com/watch?v=SoPE1cUz3Hs)

## Further Reading

1. Nathan Lambert's RLHF Book: <https://rlhfbook.com/c/11-policy-gradients.html>
2. Yannic Kilcher's GRPO video: <https://www.youtube.com/watch?v=bAWV_yrqx4w>
3. AI Engineer World's Fair 2025 workshop (3 hrs): <https://docs.unsloth.ai/ai-engineers-2025>
4. Advanced GRPO notebook: <https://docs.unsloth.ai/basics/reinforcement-learning-guide/tutorial-train-your-own-reasoning-model-with-grpo>
5. GRPO from base model: <https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_(4B)-GRPO.ipynb>

---

> [!info] Agent: Query this documentation dynamically
> `GET https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide.md?ask=<question>`

#reinforcement-learning #grpo #ppo #rlhf #reward-function #unsloth
