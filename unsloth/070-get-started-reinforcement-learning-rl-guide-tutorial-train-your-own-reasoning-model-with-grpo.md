---
title: 'Tutorial: Train your own Reasoning model with GRPO'
url: https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/tutorial-train-your-own-reasoning-model-with-grpo.md
source: llms
fetched_at: 2026-04-27T18:13:13.38714143-03:00
rendered_js: false
word_count: 1366
summary: This tutorial guides the reader through the process of training their own reasoning Large Language Model (LLM) using Group Relative Policy Optimization (GRPO) developed by DeepSeek. It walks users through setup, configuration, data preparation with structured prompts, and applying reward functions for model evaluation.
tags:
    - grpo-training
    - llm-tuning
    - reinforcement-learning
    - model-development
    - dataset-preparation
    - unsloth-guide
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Tutorial: Train your own Reasoning model with GRPO

[GRPO](https://unsloth.ai/blog/grpo) (Group Relative Policy Optimization) — developed by DeepSeek to train R1 reasoning models.

## Quickstart

Pre-made Colab [notebooks](https://unsloth.ai/docs/get-started/unsloth-notebooks) available. For local install, copy notebooks into your editor. See [[064-get-started-fine-tuning-llms-guide|Fine-tuning Guide]] first.

| [**Qwen3.5 (4B)**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_\(4B\)_Vision_GRPO.ipynb) **- Vision - new** | [**gpt-oss-20b**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-\(20B\)-GRPO.ipynb) GSPO | [Gemma 3 (4B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3_\(4B\)-Vision-GRPO.ipynb) - Vision GSPO |
| --- | --- | --- |
| [**Qwen3 (4B)**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(4B\)-GRPO.ipynb) - Advanced | [Qwen3-VL-8B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_VL_\(8B\)-Vision-GRPO.ipynb) - Vision GSPO | [Llama 3.2 (3B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Advanced_Llama3_2_\(3B\)_GRPO_LoRA.ipynb) - Advanced |

### 1. Install Unsloth

- **Colab:** Runtime > Run all
- **Local:** Ensure correct [[112-get-started-fine-tuning-for-beginners-unsloth-requirements|requirements]], then `pip install unsloth` (Linux) or follow [[057-get-started-install-windows-installation|Windows install]]

### 2. Learn GRPO & Reward Functions

Read about GRPO, reward functions, and [tips & tricks](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/..#basics-tips) before starting.

**VRAM requirement:** model parameters ≈ VRAM needed. Colab free tier (16GB) supports models up to 16B parameters.

### 3. Configure Settings

Pre-selected optimal settings provided. Change model via [[114-get-started-unsloth-model-catalog|supported models]]. Beginners should not change other settings.

> [!tip] Advanced GRPO
> For batching, generation and training parameters, see [[113-get-started-reinforcement-learning-rl-guide-advanced-rl-documentation|Advanced RL Documentation]].

### 4. Data Preparation

Pre-selected: OpenAI's [GSM8K](https://huggingface.co/datasets/openai/gsm8k) (grade school math). Swap for any HF dataset. See [[060-get-started-fine-tuning-llms-guide-datasets-guide|Datasets Guide]].

**Requirements:** at least 2 columns (question/answer). Answer must NOT reveal reasoning — only the final result.

Structure data to prompt reasoning before the answer:

```
# Define the system prompt that instructs the model to use a specific format
SYSTEM_PROMPT = """
Respond in the following format:
<reasoning>
...
</reasoning>
<answer>
...
</answer>
"""

XML_COT_FORMAT = """\
<reasoning>
{reasoning}
</reasoning>
<answer>
{answer}
</answer>
"""
```

```
import re
from datasets import load_dataset, Dataset


# Helper functions to extract answers from different formats
def extract_xml_answer(text: str) -> str:
    answer = text.split("<answer>")[-1]
    answer = answer.split("</answer>")[0]
    return answer.strip()


def extract_hash_answer(text: str) -> str | None:
    if "####" not in text:
        return None
    return text.split("####")[1].strip()


# Function to prepare the GSM8K dataset
def get_gsm8k_questions(split="train") -> Dataset:
    data = load_dataset("openai/gsm8k", "main")[split]
    data = data.map(
        lambda x: {
            "prompt": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": x["question"]},
            ],
            "answer": extract_hash_answer(x["answer"]),
        }
    )
    return data


dataset = get_gsm8k_questions()
```

### 5. Reward Functions / Verifiers

[Reward Functions/Verifiers](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/..#reward-functions-verifier) score each generation against the dataset average of other generations. Pre-selected: [Will's GSM8K](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/..#gsm8k-reward-functions) reward functions (5 reward criteria).

**Design your own:** feed generations into an LLM (ChatGPT 4o, Llama 3.1 8B) and define rules. [More examples here](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/..#reward-function-examples).

**Example — Email Automation Task:**

- **Question:** Inbound email
- **Answer:** Outbound email
- **Reward Functions:**
  - Contains required keyword → **+1**
  - Exactly matches ideal response → **+1**
  - Response too long → **-1**
  - Recipient's name included → **+1**
  - Signature block present (phone, email, address) → **+1**

### 6. Train Your Model

Pre-selected hyperparameters provided. See [[061-get-started-fine-tuning-llms-guide-lora-hyperparameters-guide|parameters guide]] and [[113-get-started-reinforcement-learning-rl-guide-advanced-rl-documentation|advanced GRPO docs]].

**GRPOConfig key parameters:**

- **`use_vllm`** — activates fast inference via vLLM
- **`learning_rate`** — model learning speed
- **`num_generations`** — completions per prompt
- **`max_steps`** — total training steps

> [!tip] DAPO, Dr. GRPO, and other new GRPO techniques now supported
>
> ```python
> epsilon=0.2,
> epsilon_high=0.28, # one sided
> delta=1.5 # two sided
>
> loss_type='bnpo',
> # or:
> loss_type='grpo',
> # or:
> loss_type='dr_grpo',
> # or:
> loss_type='dapo',
>
> mask_truncated_completions=True,
> ```

**Training tips:**

- Reward should increase over time. Minimum **300 steps** (~30 min on Colab); longer = better.
- Sample answers show learning progress (XML tags, reasoning steps, etc.).

> [!warning] Model not learning?
> Use the [Advanced GRPO notebooks](https://unsloth.ai/docs/unsloth-notebooks#grpo-reasoning-notebooks) — better reward functions, faster results.

### 7. Run & Evaluate

Save LoRA weights first:

```python
model.save_lora("grpo_saved_lora")
```

First inference without loading LoRA will show no reasoning. After loading LoRA, reasoning appears. Extend sequence length and train longer for better accuracy.

Save to GGUF/Ollama: see [[091-basics-inference-and-deployment|Inference & Deployment guide]].

> [!info] No reasoning appearing?
> Likely causes: too few training steps, or suboptimal reward function/verifier.

### 8. Save Your Model

See [[091-basics-inference-and-deployment|Inference & Deployment]] for all options.

**16-bit precision:**

```python
# Save to 16-bit precision
model.save_pretrained_merged("model", tokenizer, save_method="merged_16bit")
```

**Push to Hugging Face Hub:**

```python
# Push to Hugging Face Hub (requires a token)
model.push_to_hub_merged(
    "your-username/model-name", tokenizer, save_method="merged_16bit", token="your-token"
)
```

**GGUF format (llama.cpp / Ollama):**

```python
model.push_to_hub_gguf(
    "your-username/model-name",
    tokenizer,
    quantization_method=["q4_k_m", "q8_0", "q5_k_m"],
    token="your-token",
)
```

## Video Tutorials

- [GRPO Overview](https://www.youtube.com/watch?v=9t-BAjzBWj8)
- [Dataset prep + RL/GRPO basics](https://www.youtube.com/watch?t=3289s&v=bbFEYPx9Hpo)
- [GRPO Tutorial](https://www.youtube.com/watch?v=oF0_eMhzRaQ)
- [GRPO Walkthrough](https://www.youtube.com/watch?v=juOh1afy-IE)
- [Local GRPO on your own device](https://www.youtube.com/watch?v=SoPE1cUz3Hs)

---

> [!info] Agent: Query this documentation dynamically
> `GET https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/tutorial-train-your-own-reasoning-model-with-grpo.md?ask=<question>`

#grpo-training #reinforcement-learning #llm-tuning #unsloth
