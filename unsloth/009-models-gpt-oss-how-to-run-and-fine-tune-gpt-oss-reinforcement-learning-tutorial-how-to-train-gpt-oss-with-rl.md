---
title: 'Tutorial: How to Train gpt-oss with RL'
url: https://unsloth.ai/docs/models/gpt-oss-how-to-run-and-fine-tune/gpt-oss-reinforcement-learning/tutorial-how-to-train-gpt-oss-with-rl.md
source: llms
fetched_at: 2026-04-27T18:13:51.067574115-03:00
rendered_js: false
word_count: 815
summary: This tutorial details the process of training the gpt-oss Large Language Model using Reinforcement Learning (RL), specifically leveraging GRPO within the Unsloth framework to enable autonomous task completion, such as winning the 2048 game.
tags:
    - llm-training
    - reinforcement-learning
    - gpt-oss
    - unsloth
    - grpo
    - reward-functions
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Tutorial: How to Train gpt-oss with RL

Train [[010-models-gpt-oss-how-to-run-and-fine-tune-gpt-oss-reinforcement-learning|gpt-oss]] with [[072-get-started-reinforcement-learning-rl-guide|GRPO]] and Unsloth to autonomously beat 2048. Uses a custom [[072-get-started-reinforcement-learning-rl-guide#reward-functions-verifiers|reward function]] to overcome complex-environment tasks.

| Resource | Link |
|---|---|
| 2048 notebook (Official OpenAI example) | [Colab](https://colab.research.google.com/github/openai/gpt-oss/blob/main/examples/reinforcement-fine-tuning.ipynb) |
| Kernel generation notebook (Unsloth) | [Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-\(20B\)-GRPO.ipynb) |

**What you'll build:**

1. Train gpt-oss-20b to automatically win 2048
2. Create a minimal 2048 environment the model can interact with
3. Define reward functions: compilation check, anti-cheat, game success
4. Run inference and export (MXFP4 4-bit or merged FP16)

> [!info] Hardware
> The 2048 example runs on a free Colab T4 (slow). A100/H100 is much faster. 4-bit loading + LoRA fits a 20B model into modest VRAM.

## Install Unsloth

```bash
!pip install --upgrade -qqq uv
try: import numpy; get_numpy = f"numpy=={numpy.__version__}"
except: get_numpy = "numpy"
!uv pip install -qqq \
    "torch>=2.8.0" "triton>=3.4.0" {get_numpy} torchvision bitsandbytes "transformers==4.56.2" \
    "unsloth_zoo[base] @ git+https://github.com/unslothai/unsloth-zoo" \
    "unsloth[base] @ git+https://github.com/unslothai/unsloth" \
    git+https://github.com/triton-lang/triton.git@05b2c186c1b6c9a08375389d5efe9cb4c401c075#subdirectory=python/triton_kernels
!uv pip install --upgrade --no-deps transformers==4.56.2 tokenizers
!uv pip install --no-deps trl==0.22.2
```

## Load gpt-oss with Unsloth

Load the 20B model in 4-bit QLoRA for memory efficiency, then wrap with a LoRA adapter. 16-bit LoRA uses 4x more memory. See [[064-get-started-fine-tuning-llms-guide|configuration guide]] for more settings.

```python
from unsloth import FastLanguageModel
import torch

max_seq_length = 768        # Increase if your task needs longer outputs
lora_rank      = 4          # Higher rank → better but more VRAM/compute

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name        = "unsloth/gpt-oss-20b",  # or unsloth/gpt-oss-20b-BF16 on H100
    max_seq_length    = max_seq_length,
    load_in_4bit      = True,                    # False for 16-bit
    offload_embedding = True,                    # saves ~1GB VRAM
)

model = FastLanguageModel.get_peft_model(
    model,
    r = lora_rank,
    target_modules = [
        "q_proj", "k_proj", "v_proj", "o_proj",
        "gate_proj", "up_proj", "down_proj",
    ],
    lora_alpha = lora_rank * 2,
    use_gradient_checkpointing = "unsloth",     # big memory saver
    random_state = 3407,
)
```

> [!info] OOM mitigation
> Lower `max_seq_length`, `lora_rank`, or `num_generations` (later). Keep `load_in_4bit=True`.

## 2048 Game Environment (Minimal)

- `GameBoard` class supporting **W/A/S/D** moves
- Merge/score logic
- `execute_with_time_limit` wrapper to prevent hangs from poorly written strategies

Smoke test with a trivial policy:

```python
def always_move_left(board):
    return "W"

steps, outcome = execute_strategy(always_move_left, GameBoard(size=8, seed=42, target=2048, probability_fours=0.10))
```

## Safe Code Execution and Anti-Cheat

Generated strategies are Python functions. Execution safety and anti-reward-hacking measures:

- **Module whitelist check** — only allow Python stdlib symbols:

  ```python
  from unsloth import check_python_modules
  ok, info = check_python_modules("""
  def strategy(board):
      import math
      from typing import Callable
      return "W"
  """)
  # ok == True means only Python-level imports were used
  ```

- **Block disallowed imports** (e.g., NumPy):

  ```python
  sample = """
  def strategy(board):
      from numpy import matmul
      return "W"
  """
  ok, info = check_python_modules(sample)  # ok => False
  ```

- **Lock down execution** to a sandboxed function:

  ```python
  from unsloth import create_locked_down_function
  function = """
  def add(a, b):
      def adder(a):
          return a + b
      return adder(b) + b
  """
  f = create_locked_down_function(function)  # errors if globals / imports are used
  ```

- **Hard wall-clock limit** on strategy runs:

  ```python
  from unsloth import execute_with_time_limit
  @execute_with_time_limit(2)
  def execute_strategy(strategy, game):
      # loop until game ends or timeout
      ...
  ```

## Prompt and Dataset

Prompt the model to emit a short strategy function inside triple backticks:

````
Create a new short 2048 strategy using only native Python code.
You are given a list of list of numbers for the current board state.
Output one action for "W", "A", "S", "D" on what is the optimal next step.
Output your new short function in backticks using the format below:
```python
def strategy(board):
    return "W"  # Example
```
````

All helper functions should be inside `def strategy`. Only output the short function `strategy`.

Create a tiny synthetic dataset (reusing the same prompt) and compute the prompt length for GRPO completion token sampling:

```python
from datasets import Dataset

prompt = ...  # as above

maximum_length = len(tokenizer.apply_chat_template(
    [{"role": "user", "content": prompt}], add_generation_prompt=True
))

dataset = Dataset.from_list([
    {"prompt": [{"role": "user", "content": prompt}], "answer": 0, "reasoning_effort": "low"}
] * 1000)
```

> [!info] Replace this dataset with real prompts for your own RL task.

## Reward Functions

### 1. Extract the code block from model's reply

````python
def extract_function(text):
    if text.count("```") >= 2:
        first = text.find("```") + 3
        second = text.find("```", first)
        fx = text[first:second].strip()
        fx = fx.removeprefix("python\n")
        fx = fx[fx.find("def"):]
        if fx.startswith("def strategy(board):"):
            return fx
    return None
````

### 2. `function_works` — Does it compile and create a callable?

```python
from unsloth import create_locked_down_function, check_python_modules

def function_works(completions, **kwargs):
    scores = []
    for completion in completions:
        response = completion[0]["content"]
        function = extract_function(response)
        if function is None:
            scores.append(-2.0)
            continue
        ok, info = check_python_modules(function)
        if "error" in info:
            scores.append(-2.0)
            continue
        try:
            _ = create_locked_down_function(function)
            scores.append(1.0)
        except Exception:
            scores.append(-0.5)
    return scores
```

### 3. `no_cheating` — No non-stdlib imports allowed

```python
def no_cheating(completions, **kwargs):
    scores = []
    for completion in completions:
        response = completion[0]["content"]
        function = extract_function(response)
        if function is None:
            scores.append(-1.0)
            continue
        ok, _ = check_python_modules(function)
        scores.append(1.0 if ok else -20.0)  # heavy penalty if cheating
    return scores
```

### 4. `strategy_succeeds` — Play a random board; reward success

```python
import numpy as np

PRINTER = 0  # occasionally print for debugging

def strategy_succeeds(completions, **kwargs):
    global PRINTER
    scores = []
    seed = np.random.randint(10000)
    for completion in completions:
        response = completion[0]["content"]
        function = extract_function(response)
        if function is None:
            scores.append(-2.0)
            continue
        try:
            new_strategy = create_locked_down_function(function)
        except Exception:
            scores.append(0.0)
            continue
        try:
            game = GameBoard(size=6, seed=seed, target=2048, probability_fours=0.10)
            steps, state = execute_strategy(new_strategy, game)
            if PRINTER % 5 == 0:
                print(function)
                print(f"Steps={steps} State={state}")
                print(game.board().pretty())
            PRINTER += 1
            if state == "success":
                scores.append(20.0)
            else:
                scores.append(2.0)   # worked but didn't reach 2048
        except TimeoutError:
            scores.append(-1.0)      # timed out
        except Exception:
            scores.append(-3.0)      # crashed
    return scores
```

## Configure GRPO

Use `GRPOTrainer`. Set prompt/completion lengths, then build a `GRPOConfig`. Alternative RL algorithms: [[109-get-started-reinforcement-learning-rl-guide-advanced-rl-documentation-gspo-reinforcement-learning|GSPO]] or Dr. GRPO.

```python
from trl import GRPOConfig, GRPOTrainer

max_prompt_length     = maximum_length + 1
max_completion_length = max_seq_length - max_prompt_length

training_args = GRPOConfig(
    temperature=1.0,
    learning_rate=5e-5,
    weight_decay=0.01,
    warmup_ratio=0.1,
    lr_scheduler_type="linear",
    optim="adamw_8bit",
    logging_steps=1,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=1,    # bump to 4 for smoother reward signals
    num_generations=2,                # lower if you OOM
    max_prompt_length=max_prompt_length,
    max_completion_length=max_completion_length,
    max_steps=1000,                   # or set num_train_epochs=1
    save_steps=100,
    report_to="none",
    output_dir="outputs",
)

trainer = GRPOTrainer(
    model=model,
    processing_class=tokenizer,
    reward_funcs=[function_works, no_cheating, strategy_succeeds],
    args=training_args,
    train_dataset=dataset,
    # Optional eval split:
    # train_dataset=new_dataset["train"],
    # eval_dataset=new_dataset["test"],
)
```

> [!info] Reading logs
> Look at `reward` and `reward_std`. Low/zero rewards early is normal (first ~100-200 steps on small GPUs).

## Train

```python
trainer.train()
```

Full RL loop: sample completions -> score with rewards -> optimize the policy (LoRA).

## Inference (After Training)

Generate a fresh strategy with the trained adapter:

```python
from transformers import TextStreamer

text = tokenizer.apply_chat_template(
    [{"role": "user", "content": prompt}],
    tokenize=False,
    add_generation_prompt=True,
    reasoning_effort="low",
)

_ = model.generate(
    **tokenizer(text, return_tensors="pt").to("cuda"),
    temperature=1.0,
    max_new_tokens=1024,
    streamer=TextStreamer(tokenizer, skip_prompt=False)
```

## Save / Export

**Merge and save 4-bit (MXFP4):**

```python
model.save_pretrained_merged("finetuned_model", tokenizer, save_method="mxfp4")
# or push
model.push_to_hub_merged("<org_or_user>/", tokenizer, token="<hf_token>", save_method="mxfp4")
```

**Merge and save 16-bit:**

```python
model.save_pretrained_merged("finetuned_model", tokenizer, save_method="merged_16bit")
# or push
model.push_to_hub_merged("<org_or_user>/<repo>", tokenizer, token="<hf_token>", save_method="merged_16bit")
```

## Troubleshooting

- **OOM / slow** — reduce `max_seq_length`, `num_generations`, `lora_rank`; keep 4-bit; try A100 if available.
- **No reward improvement** — increase training steps, soften penalties, or add curriculum (start with smaller boards / lower targets).
- **Reward hacking** — keep `check_python_modules` strict; validate strategy behavior across multiple random seeds.
- **Unstable training** — raise `gradient_accumulation_steps` to smooth updates; lower `learning_rate` (e.g., 2e-5).
- **Long hangs** — ensure `execute_with_time_limit` wraps any strategy execution.

## Adapt to Your Own RL Task

1. Replace the 2048 env with your own environment and **three rewards**: (a) syntax/compilation, (b) anti-cheat/safety, (c) task success.
2. Update the prompt to request the kind of function or output you need.
3. Keep the same Unsloth + GRPO scaffolding; only swap the env and rewards.

#reinforcement-learning #grpo #gpt-oss #reward-functions #unsloth
