---
title: RL for Privacy-Conscious Delegation - DSPy
url: https://dspy.ai/tutorials/rl_papillon/
source: sitemap
fetched_at: 2026-01-23T08:04:23.736161583-03:00
rendered_js: false
word_count: 99
summary: This document demonstrates how to configure and execute the compilation process for a PAPILLON model using the ArborGRPO compiler. It details training hyperparameters, LoRA settings, and hardware resource allocation for model optimization.
tags:
    - papillon
    - arborgrpo
    - model-optimization
    - lora-config
    - training-parameters
    - gpu-allocation
category: configuration
---

```
papillon = PAPILLON(untrusted_model=openai_lm)
papillon.set_lm(local_lm)

# NOTE: Training on 4 GPUs.
train_kwargs = {
    "per_device_train_batch_size": 8,
    "gradient_accumulation_steps": 4,
    "temperature": 1.0,
    "top_k": -1,
    "top_p": 1.0,
    "repetition_penalty": 1.0,
    "beta": 0.00,
    "learning_rate": 1e-6,
    "gradient_checkpointing": True,
    "bf16": True,
    "lr_scheduler_type": "constant_with_warmup",
    "loss_type": "dapo",
    "max_steps": 1000,
    "report_to": "wandb",
    "log_completions": True,
    "logging_steps": 1,
    "max_prompt_length": None,
    "max_completion_length": None,
    "scale_rewards": False,
    "max_grad_norm": 1.0,
    "lora_config": {
        "lora_alpha": 16,
        "lora_dropout": 0.05,
        "r": 8,
        "target_modules": ["q_proj", "k_proj", "v_proj", "o_proj", "up_proj", "down_proj", "gate_proj"],
    },
    "num_training_gpus": 3,
    "num_inference_gpus": 1,
    "weight_decay": 0.001,
}

compiler = ArborGRPO(
    metric=compute_overall_score,
    multitask=True,
    num_dspy_examples_per_grpo_step=4,
    num_samples_per_input=8,
    exclude_demos=True,
    num_train_steps=500,
    num_threads=24,
    use_train_as_val=False,
    num_steps_for_val=10,
    train_kwargs=train_kwargs,
    report_train_scores=False,
)

optimized_papillon = compiler.compile(
    student=papillon,
    trainset=trainset,
    valset=devset,
)
```

papillon = PAPILLON(untrusted\_model=openai\_lm) papillon.set\_lm(local\_lm) # NOTE: Training on 4 GPUs. train\_kwargs = { "per\_device\_train\_batch\_size": 8, "gradient\_accumulation\_steps": 4, "temperature": 1.0, "top\_k": -1, "top\_p": 1.0, "repetition\_penalty": 1.0, "beta": 0.00, "learning\_rate": 1e-6, "gradient\_checkpointing": True, "bf16": True, "lr\_scheduler\_type": "constant\_with\_warmup", "loss\_type": "dapo", "max\_steps": 1000, "report\_to": "wandb", "log\_completions": True, "logging\_steps": 1, "max\_prompt\_length": None, "max\_completion\_length": None, "scale\_rewards": False, "max\_grad\_norm": 1.0, "lora\_config": { "lora\_alpha": 16, "lora\_dropout": 0.05, "r": 8, "target\_modules": \["q\_proj", "k\_proj", "v\_proj", "o\_proj", "up\_proj", "down\_proj", "gate\_proj"], }, "num\_training\_gpus": 3, "num\_inference\_gpus": 1, "weight\_decay": 0.001, } compiler = ArborGRPO( metric=compute\_overall\_score, multitask=True, num\_dspy\_examples\_per\_grpo\_step=4, num\_samples\_per\_input=8, exclude\_demos=True, num\_train\_steps=500, num\_threads=24, use\_train\_as\_val=False, num\_steps\_for\_val=10, train\_kwargs=train\_kwargs, report\_train\_scores=False, ) optimized\_papillon = compiler.compile( student=papillon, trainset=trainset, valset=devset, )