---
title: Vision Reinforcement Learning (VLM RL)
url: https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/vision-reinforcement-learning-vlm-rl.md
source: llms
fetched_at: 2026-04-27T18:13:10.871203343-03:00
rendered_js: false
word_count: 873
summary: This document outlines the support for Vision Reinforcement Learning (VLM RL) within Unsloth, highlighting performance improvements like speed and memory efficiency. It details how to utilize this feature with models like Qwen3-VL and Gemma 3, provides code examples for setup and fine-tuning, and addresses common issues such as 'addCriterion' gibberish outputs by suggesting reward function adjustments.
tags:
    - vlm-rl
    - unsloth
    - vision-language
    - reinforcement-learning
    - qwen3-vl
    - gemma-3
    - finetuning
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Vision Reinforcement Learning (VLM RL)

Unsloth supports vision/multimodal RL with [Qwen3-VL](https://unsloth.ai/docs/models/tutorials/qwen3-how-to-run-and-fine-tune/qwen3-vl-how-to-run-and-fine-tune), [Gemma 3](https://unsloth.ai/docs/models/tutorials/gemma-3-how-to-run-and-fine-tune) and more. Via [weight sharing](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/..#what-unsloth-offers-for-rl) and custom kernels: **1.5-2x faster**, **90% less VRAM**, **15x longer context** vs FA2, no accuracy loss.

Qwen3-VL-8B trains with GSPO/GRPO on a free Colab T4. Other VLMs may need larger GPUs. Gemma requires newer GPUs than T4 (vLLM [restricts to Bfloat16](https://unsloth.ai/docs/models/tutorials/gemma-3-how-to-run-and-fine-tune#unsloth-fine-tuning-fixes)); recommend NVIDIA L4 on Colab.

## Notebooks

| Model | Inference | Link |
|---|---|---|
| Qwen-3 VL-8B | vLLM | [Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_VL_\(8B\)-Vision-GRPO.ipynb) |
| Qwen-2.5 VL-7B | vLLM | [Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen2_5_7B_VL_GRPO.ipynb) / [Kaggle](https://www.kaggle.com/notebooks/welcome?src=https://github.com/unslothai/notebooks/blob/main/nb/Kaggle-Qwen2_5_7B_VL_GRPO.ipynb\&accelerator=nvidiaTeslaT4) |
| Gemma-3-4B | Unsloth | [Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3_\(4B\)-Vision-GRPO.ipynb) |

vLLM VLM integration is native — enable `fast_inference=True`. Integrates the [Standby feature](https://unsloth.ai/docs/get-started/memory-efficient-rl#unsloth-standby) for more memory-efficient + faster RL. Credit: [Sinoue GAD](https://github.com/unslothai/unsloth/pull/2752).

> [!info] fast_inference Compatibility
> Only for VLMs supported by vLLM. Some models (e.g., Llama 3.2 Vision) run without vLLM but still work in Unsloth.

## Setup

```python
os.environ['UNSLOTH_VLLM_STANDBY'] = '1' # To enable memory efficient GRPO with vLLM
model, tokenizer = FastVisionModel.from_pretrained(
    model_name = "Qwen/Qwen2.5-VL-7B-Instruct",
    max_seq_length = 16384, #Must be this large to fit image in context
    load_in_4bit = True, # False for LoRA 16bit
    fast_inference = True, # Enable vLLM fast inference
    gpu_memory_utilization = 0.8, # Reduce if out of memory
)
```

vLLM does not support LoRA for vision/encoder layers — set `finetune_vision_layers = False` with `fast_inference`. You CAN train vision layers with Unsloth/transformers inference.

```python
# Add LoRA adapter to the model for parameter efficient fine tuning
model = FastVisionModel.get_peft_model(
    model,

    finetune_vision_layers     = False,# fast_inference doesn't support finetune_vision_layers yet :(
    finetune_language_layers   = True, # False if not finetuning language layers
    finetune_attention_modules = True, # False if not finetuning attention layers
    finetune_mlp_modules       = True, # False if not finetuning MLP layers

    r = lora_rank, # Choose any number > 0 ! Suggested 8, 16, 32, 64, 128
    lora_alpha = lora_rank*2, # *2 speeds up training
    use_gradient_checkpointing = "unsloth", # Reduces memory usage
    random_state = 3407,
)
```

## Qwen 2.5 VL Vision RL Issues and Quirks

During RL, you may see gibberish output like repeated `addCriterion` lines ([Qwen issue #759](https://github.com/QwenLM/Qwen2.5-VL/issues/759)). Observed on both Unsloth and non-Unsloth setups, across bfloat16/float16. Example: item 165 from [AI4Math/MathVista](https://huggingface.co/datasets/AI4Math/MathVista).

### Mitigations

- Add a reward function to penalize `addCriterion` / gibberish outputs
- Train for longer (~60+ steps before model learns via RL)
- Force `\`` during generation to reduce occurrences (Instruct model), but reward function is preferred

## Reward Functions to Reduce Gibberish

```python
def formatting_reward_func(completions,**kwargs):
    import re
    thinking_pattern = f'{REASONING_START}(.*?){REASONING_END}'
    answer_pattern = f'{SOLUTION_START}(.*?){SOLUTION_END}'

    scores = []
    for completion in completions:
        score = 0
        thinking_matches = re.findall(thinking_pattern, completion, re.DOTALL)
        answer_matches = re.findall(answer_pattern, completion, re.DOTALL)
        if len(thinking_matches) == 1:
            score += 1.0
        if len(answer_matches) == 1:
            score += 1.0

        # Fix up addCriterion issues
        # See https://docs.unsloth.ai/new/vision-reinforcement-learning-vlm-rl#qwen-2.5-vl-vision-rl-issues-and-quirks
        # Penalize on excessive addCriterion and newlines
        if len(completion) != 0:
            removal = completion.replace("addCriterion", "").replace("\n", "")
            if (len(completion)-len(removal))/len(completion) >= 0.5:
                score -= 2.0

        scores.append(score)
    return scores
```

## GSPO Reinforcement Learning

GSPO ([Group Sequence Policy Optimization](https://arxiv.org/abs/2507.18071)) by Qwen/Alibaba — a GRPO variant. GRPO implicitly assigns importance weights per token, but advantages don't scale per token. GSPO assigns importance on **sequence likelihood** rather than individual token likelihoods.

- **GRPO (Eq. 1)**: Advantages scale each row of token logprobs before summation — same scaling for every token despite being computed on the full sequence.
- **GSPO (Eq. 2)**: Logprob ratios per sequence are summed and exponentiated first; only the resulting sequence ratios get row-wise multiplied by advantages.

Enable by setting `importance_sampling_level = "sequence"` in GRPOConfig.

```python
training_args = GRPOConfig(
    output_dir = "vlm-grpo-unsloth",
    per_device_train_batch_size = 8,
    gradient_accumulation_steps = 4,
    learning_rate = 5e-6,
    adam_beta1 = 0.9,
    adam_beta2 = 0.99,
    weight_decay = 0.1,
    warmup_ratio = 0.1,
    lr_scheduler_type = "cosine",
    optim = "adamw_8bit",
    # beta = 0.00,
    epsilon = 3e-4,
    epsilon_high = 4e-4,
    num_generations = 8,
    max_prompt_length = 1024,
    max_completion_length = 1024,
    log_completions = False,
    max_grad_norm = 0.1,
    temperature = 0.9,
    # report_to = "none", # Set to "wandb" if you want to log to Weights & Biases
    num_train_epochs = 2, # For a quick test run, increase for full training
    report_to = "none"

    # GSPO is below:
    importance_sampling_level = "sequence",

    # Dr GRPO / GAPO etc
    loss_type = "dr_grpo",
)
```

See also: [[072-get-started-reinforcement-learning-rl-guide|Reinforcement Learning Guide]]

#vlm-rl #vision-language #reinforcement-learning #gspo #grpo #unsloth
