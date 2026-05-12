---
title: Fine-tuning LLMs on Intel GPUs with Unsloth
url: https://unsloth.ai/docs/get-started/install/intel.md
source: llms
fetched_at: 2026-04-27T18:13:01.595523883-03:00
rendered_js: false
word_count: 594
summary: This document serves as a guide detailing how to set up and fine-tune Large Language Models (LLMs) using Unsloth specifically tailored for Intel GPUs. It provides step-by-step instructions for installation, environment verification, configuration on Windows, and examples covering QLoRA (SFT) and Reinforcement Learning (GRPO).
tags:
    - llm-fine-tuning
    - intel-gpu
    - unsloth
    - qlora
    - reinforcement-learning
    - model-training
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Fine-tuning LLMs on Intel GPUs with Unsloth

## Prerequisites

- **Intel GPU**: Data Center GPU Max Series, Arc Series, or Intel Ultra AIPC
- **OS**: Linux (Ubuntu 22.04+) or Windows 11
- **Windows only**: Intel oneAPI Base Toolkit 2025.2.1
- **Driver**: Latest recommended for Windows/Linux
- **Python**: 3.10+

## Build Unsloth with Intel Support

### 1. Create Conda Environment (Optional)

```bash
conda create -n unsloth-xpu python==3.10
conda activate unsloth-xpu
```

### 2. Install Unsloth

```bash
git clone https://github.com/unslothai/unsloth.git
cd unsloth
pip install .[intel-gpu-torch290]
```

> [!info] Linux only: optionally install [vLLM](https://docs.vllm.ai/en/latest/getting_started/installation/gpu/#intel-xpu) for [[091-basics-inference-and-deployment|inference]] and [[072-get-started-reinforcement-learning-rl-guide|RL]].

### 3. Verify Environment

```python
import torch
print(f"PyTorch version: {torch.__version__}")
print(f"XPU available: {torch.xpu.is_available()}")
print(f"XPU device count: {torch.xpu.device_count()}")
print(f"XPU device name: {torch.xpu.get_device_name(0)}")
```

### 4. Start Fine-tuning

Use [[073-get-started-unsloth-notebooks|Unsloth notebooks]], [[064-get-started-fine-tuning-llms-guide|fine-tuning guide]], or [[072-get-started-reinforcement-learning-rl-guide|RL guide]].

## Windows Runtime Configuration

Enable long path support (run once, admin Command Prompt):

```bash
powershell -Command "Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\FileSystem" -Name "LongPathsEnabled" -Value 1
```

Then:

1. Download [level-zero-win-sdk-1.20.2.zip](https://github.com/oneapi-src/level-zero/releases/tag/v1.20.2)
2. Unzip the file
3. In Command Prompt, under conda env `unsloth-xpu`:

```bash
call "C:\Program Files (x86)\Intel\oneAPI\setvars.bat" -
set ZE_PATH=path\to\the\unzipped\level-zero-win-sdk-1.20.2
```

## Example 1: QLoRA Fine-tuning (SFT)

4-bit QLoRA on Intel GPU using Qwen3-32B.

```python
from unsloth import FastLanguageModel, FastModel
from trl import SFTTrainer, SFTConfig
from datasets import load_dataset
max_seq_length = 2048 # Supports RoPE Scaling internally, so choose any!
# Get LAION dataset
url = "https://huggingface.co/datasets/laion/OIG/resolve/main/unified_chip2.jsonl"
dataset = load_dataset("json", data_files = {"train" :
url}, split = "train")

# 4bit pre quantized models we support for fast downloading + no OOMs.
fourbit_models = [
"unsloth/Qwen3-32B-bnb-4bit",
"unsloth/Qwen3-14B-bnb-4bit",
"unsloth/Qwen3-8B-bnb-4bit",
"unsloth/Qwen3-4B-bnb-4bit",
"unsloth/Qwen3-1.7B-bnb-4bit",
"unsloth/Qwen3-0.6B-bnb-4bit",
# "unsloth/Qwen2.5-32B-bnb-4bit",
# "unsloth/Qwen2.5-14B-bnb-4bit",
# "unsloth/Qwen2.5-7B-bnb-4bit",
# "unsloth/Qwen2.5-3B-bnb-4bit",
# "unsloth/Qwen2.5-1.5B-bnb-4bit",
# "unsloth/Qwen2.5-0.5B-bnb-4bit",
# "unsloth/Llama-3.2-3B-bnb-4bit",
# "unsloth/Llama-3.2-1B-bnb-4bit",
# "unsloth/Llama-3.1-8B-bnb-4bit",
# "unsloth/Llama-3.1-70B-bnb-4bit",
# "unsloth/mistral-7b-bnb-4bit",
# "unsloth/Phi-4",
# "unsloth/Phi-3.5-mini-instruct",
# "unsloth/Phi-3-medium-4k-instruct",
# "unsloth/Phi-3-mini-4k-instruct",
# "unsloth/gemma-2-9b-bnb-4bit",
# "unsloth/gemma-2-27b-bnb-4bit",
] # More models at https://huggingface.co/unsloth

model, tokenizer = FastLanguageModel.from_pretrained(
model_name = "unsloth/Qwen3-32B-bnb-4bit",
max_seq_length = max_seq_length,
load_in_4bit = True,
# token = "hf_...", # use one if using gated models like meta-llama/Llama-2-7b-hf
)

model = FastLanguageModel.get_peft_model(
model,
r = 16, # Choose any number > 0 ! Suggested 8, 16, 32, 64, 128
target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
"gate_proj", "up_proj", "down_proj",
],
lora_alpha = 16,
lora_dropout = 0, # Supports any, but = 0 is optimized
bias = "none", # Supports any, but = "none" is optimized
use_gradient_checkpointing = "unsloth", # True or "unsloth" for very long context
random_state = 3407,
use_rslora = False, # We support rank stabilized LoRA
loftq_config = None, # And LoftQ
)

trainer = SFTTrainer(
model = model,
tokenizer = tokenizer,
train_dataset = dataset,
dataset_text_field = "text",
max_seq_length = max_seq_length,
dataset_num_proc = 1, # Recommended on Windows
packing = False, # Can make training 5x faster for short sequences.
args = SFTConfig(
per_device_train_batch_size = 2,
gradient_accumulation_steps = 4,
warmup_steps = 5,
max_steps = 60,
learning_rate = 2e-4,
logging_steps = 1,
optim = "adamw_8bit",
weight_decay = 0.01,
lr_scheduler_type = "linear",
seed = 3407,
dataset_num_proc=1, # Recommended on Windows
),
)

trainer.train()
```

## Example 2: Reinforcement Learning (GRPO)

GRPO — group-based normalization RL for aligning LLMs with human preferences. More memory efficient than PPO, supports multiple reward functions.

```python
from unsloth import FastLanguageModel
import re
from trl import GRPOConfig, GRPOTrainer
from datasets import load_dataset, Dataset

max_seq_length = 1024  # Can increase for longer reasoning traces
lora_rank = 32  # Larger rank = smarter, but slower
max_prompt_length = 256

# Load and prep dataset
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


def extract_xml_answer(text: str) -> str:
    answer = text.split("<answer>")[-1]
    answer = answer.split("</answer>")[0]
    return answer.strip()


def extract_hash_answer(text: str) -> str | None:
    if "####" not in text:
        return None
    return text.split("####")[1].strip()


# uncomment middle messages for 1-shot prompting
def get_gsm8k_questions(split: str = "train") -> Dataset:
    data = load_dataset("openai/gsm8k", "main")[split]  # type: ignore
    data = data.map(
        lambda x: {  # type: ignore
            "prompt": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": x["question"]},
            ],
            "answer": extract_hash_answer(x["answer"]),
        }
    )  # type: ignore
    return data  # type: ignore


# Reward functions
def correctness_reward_func(prompts, completions, answer, **kwargs) -> list[float]:
    responses = [completion[0]["content"] for completion in completions]
    q = prompts[0][-1]["content"]
    extracted_responses = [extract_xml_answer(r) for r in responses]
    print(
        "-" * 20,
        f"Question:\n{q}",
        f"\nAnswer:\n{answer[0]}",
        f"\nResponse:\n{responses[0]}",
        f"\nExtracted:\n{extracted_responses[0]}",
    )
    return [2.0 if r == a else 0.0 for r, a in zip(extracted_responses, answer)]


def int_reward_func(completions, **kwargs) -> list[float]:
    responses = [completion[0]["content"] for completion in completions]
    extracted_responses = [extract_xml_answer(r) for r in responses]
    return [0.5 if r.isdigit() else 0.0 for r in extracted_responses]


def strict_format_reward_func(completions, **kwargs) -> list[float]:
    """Reward function that checks if the completion has a specific format."""
    pattern = r"^<reasoning>\n.*?\n</reasoning>\n<answer>\n.*?\n</answer>\n$"
    responses = [completion[0]["content"] for completion in completions]
    matches = [re.match(pattern, r) for r in responses]
    return [0.5 if match else 0.0 for match in matches]


def soft_format_reward_func(completions, **kwargs) -> list[float]:
    """Reward function that checks if the completion has a specific format."""
    pattern = r"<reasoning>.*?</reasoning>\s*<answer>.*?</answer>"
    responses = [completion[0]["content"] for completion in completions]
    matches = [re.match(pattern, r) for r in responses]
    return [0.5 if match else 0.0 for match in matches]


def count_xml(text: str) -> float:
    count = 0.0
    if text.count("<reasoning>\n") == 1:
        count += 0.125
    if text.count("\n</reasoning>\n") == 1:
        count += 0.125
    if text.count("\n<answer>\n") == 1:
        count += 0.125
    count -= len(text.split("\n</answer>\n")[-1]) * 0.001
    if text.count("\n</answer>") == 1:
        count += 0.125
    count -= (len(text.split("\n</answer>")[-1]) - 1) * 0.001
    return count


def xmlcount_reward_func(completions, **kwargs) -> list[float]:
    contents = [completion[0]["content"] for completion in completions]
    return [count_xml(c) for c in contents]


if __name__ == "__main__":
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name="unsloth/Qwen3-0.6B",
        max_seq_length=max_seq_length,
        load_in_4bit=False,  # False for LoRA 16bit
        fast_inference=False,  # Enable vLLM fast inference
        max_lora_rank=lora_rank,
        gpu_memory_utilization=0.7,  # Reduce if out of memory
        device_map="xpu:0",
    )

    model = FastLanguageModel.get_peft_model(
        model,
        r=lora_rank,  # Choose any number > 0 ! Suggested 8, 16, 32, 64, 128
        target_modules=[
            "q_proj",
            "k_proj",
            "v_proj",
            "o_proj",
            "gate_proj",
            "up_proj",
            "down_proj",
        ],  # Remove QKVO if out of memory
        lora_alpha=lora_rank,
        use_gradient_checkpointing="unsloth",  # Enable long context finetuning
        random_state=3407,
    )

    dataset = get_gsm8k_questions()

    training_args = GRPOConfig(
        learning_rate=5e-6,
        adam_beta1=0.9,
        adam_beta2=0.99,
        weight_decay=0.1,
        warmup_ratio=0.1,
        lr_scheduler_type="cosine",
        optim="adamw_torch",
        logging_steps=1,
        per_device_train_batch_size=1,
        gradient_accumulation_steps=1,  # Increase to 4 for smoother training
        num_generations=4,  # Decrease if out of memory
        max_prompt_length=max_prompt_length,
        max_completion_length=max_seq_length - max_prompt_length,
        # num_train_epochs=1,  # Set to 1 for a full training run
        max_steps=20,
        save_steps=250,
        max_grad_norm=0.1,
        report_to="none",  # Can use Weights & Biases
        output_dir="outputs",
    )

    trainer = GRPOTrainer(
        model=model,
        processing_class=tokenizer,
        reward_funcs=[
            xmlcount_reward_func,
            soft_format_reward_func,
            strict_format_reward_func,
            int_reward_func,
            correctness_reward_func,
        ],
        args=training_args,
        train_dataset=dataset,
        dataset_num_proc=1,  # Recommended on Windows
    )

    trainer.train()

```

## Troubleshooting

### Out of Memory (OOM)

1. Lower `per_device_train_batch_size`
2. Use a smaller model
3. Lower `max_seq_length`
4. Reduce LoRA rank (`r=8` instead of 16/32)
5. For GRPO, lower `num_generations`

### Windows: Intel Ultra AIPC iGPU Shared Memory

Default shared GPU memory is **57%** of system RAM. For larger models (e.g. Qwen3-32B) or longer sequences, increase via registry:

- **Path**: `Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers\MemoryManager`
- **Key**: `SystemPartitionCommitLimitPercentage` — set to a larger percentage

#unsloth #intel #xpu #fine-tuning #qlora #grpo
