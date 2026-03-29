---
title: RL for Multi-Hop Research - DSPy
url: https://dspy.ai/tutorials/rl_multihop/
source: sitemap
fetched_at: 2026-01-23T08:04:21.138446603-03:00
rendered_js: false
word_count: 99
summary: This document demonstrates how to configure and execute the ArborGRPO compiler to optimize a research program using specific training hyperparameters and hardware allocations. It provides a detailed example of setting up LoRA configurations, training arguments, and the compilation process.
tags:
    - arbor-grpo
    - lora-config
    - model-optimization
    - distributed-training
    - hyperparameter-tuning
    - machine-learning
category: configuration
---

```
program = ResearchHop(num_docs=4, num_hops=2)
program.set_lm(local_lm)

# NOTE: Training on 4 GPUs.
train_kwargs = {
    "per_device_train_batch_size": 2,
    "gradient_accumulation_steps": 24/6,
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
    metric=recall,
    num_dspy_examples_per_grpo_step=6,
    num_rollouts_per_grpo_step=24,
    exclude_demos=True,
    num_train_steps=1000,
    num_threads=16,
    use_train_as_val=False,
    num_steps_for_val=50,
    train_kwargs=train_kwargs,
    checkpoint="single-best",
)

optimized_program = compiler.compile(
    student=program,
    trainset=trainset,
    valset=devset,
)
```

program = ResearchHop(num\_docs=4, num\_hops=2) program.set\_lm(local\_lm) # NOTE: Training on 4 GPUs. train\_kwargs = { "per\_device\_train\_batch\_size": 2, "gradient\_accumulation\_steps": 24/6, "temperature": 1.0, "top\_k": -1, "top\_p": 1.0, "repetition\_penalty": 1.0, "beta": 0.00, "learning\_rate": 1e-6, "gradient\_checkpointing": True, "bf16": True, "lr\_scheduler\_type": "constant\_with\_warmup", "loss\_type": "dapo", "max\_steps": 1000, "report\_to": "wandb", "log\_completions": True, "logging\_steps": 1, "max\_prompt\_length": None, "max\_completion\_length": None, "scale\_rewards": False, "max\_grad\_norm": 1.0, "lora\_config": { "lora\_alpha": 16, "lora\_dropout": 0.05, "r": 8, "target\_modules": \["q\_proj", "k\_proj", "v\_proj", "o\_proj", "up\_proj", "down\_proj", "gate\_proj"], }, "num\_training\_gpus": 3, "num\_inference\_gpus": 1, "weight\_decay": 0.001, } compiler = ArborGRPO( metric=recall, num\_dspy\_examples\_per\_grpo\_step=6, num\_rollouts\_per\_grpo\_step=24, exclude\_demos=True, num\_train\_steps=1000, num\_threads=16, use\_train\_as\_val=False, num\_steps\_for\_val=50, train\_kwargs=train\_kwargs, checkpoint="single-best", ) optimized\_program = compiler.compile( student=program, trainset=trainset, valset=devset, )