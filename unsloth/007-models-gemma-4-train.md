---
title: Gemma 4 Fine-tuning Guide
url: https://unsloth.ai/docs/models/gemma-4/train.md
source: llms
fetched_at: 2026-04-27T18:13:32.201284526-03:00
rendered_js: false
word_count: 2578
summary: This document serves as a guide detailing how to fine-tune various sizes of the Gemma 4 model (E2B, E4B, 26B-A4B, and 31B) using Unsloth. It highlights performance improvements, bug fixes, hardware requirements, and offers tips for successful training, including managing loss values and enabling thinking mode.
tags:
    - gemma-4
    - fine-tuning
    - unsloth
    - training-guide
    - multimodal
    - vram
category: guide
optimized: true
optimized_at: 2026-04-27T21:40:00Z
---

# Gemma 4 Fine-tuning Guide

Train Google's Gemma 4 E2B, E4B, 26B-A4B and 31B with [[001-get-started-readme|Unsloth]]. Supports all vision, text, audio and RL fine-tuning.

- **~1.5x faster** training with **~60% less VRAM** vs FA2 (no accuracy loss)
- Many universal Gemma 4 training [bugs fixed](#bug-fixes--tips) (not Unsloth-derived)
- E2B trains on 8GB VRAM, E4B on 10GB VRAM

**Colab notebooks:**

| [**E4B + E2B** (Studio)](https://colab.research.google.com/github/unslothai/unsloth/blob/main/studio/Unsloth_Studio_Colab.ipynb) | [**31B** (Kaggle)](https://www.kaggle.com/code/danielhanchen/gemma4-31b-unsloth) | [E4B **(Vision + Text)**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma4_\(E4B\)-Vision.ipynb) | [E4B **(Audio)**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma4_\(E4B\)-Audio.ipynb) | [E2B **(RL GRPO)**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma4_\(E2B\)_Reinforcement_Learning_Sudoku_Game.ipynb) |
| --- | --- | --- | --- | --- |

UI-based training: [[097-new-studio|Unsloth Studio]] notebook: [Unsloth Studio Colab](https://colab.research.google.com/github/unslothai/unsloth/blob/main/studio/Unsloth_Studio_Colab.ipynb)

**VRAM requirements:**

| Variant | LoRA | QLoRA | RL |
| --- | --- | --- | --- |
| **E2B** | 8-10 GB | 8 GB | 9 GB |
| **E4B** | 17 GB | 10 GB | -- |
| **26B-A4B** | >40 GB | -- | -- |
| **31B** | -- | 22 GB | -- |

Exporting to GGUF and full fine-tuning (FFT) also supported.

## Bug fixes + Tips

> [!success] Normal loss values
> E2B/E4B loss of 13-15 is normal (multimodal model quirk, same as Gemma-3N, Llama Vision, Mistral vision).
> Gemma 26B/31B loss is lower at 1-3; vision loss is ~2x higher (3-5).

### Gradient accumulation inflating losses

Losses > 13-15 (e.g., 100 or 300) likely mean gradient accumulation is not being accounted for properly. **Fixed in Unsloth and Unsloth Studio.**

See: <https://unsloth.ai/blog/gradient>

### IndexError on Gemma-4 31B and 26B-A4B inference

```python
File "/.../cache_utils.py", line 937, in update
    keys, values = self.layers[layer_idx].update(...)
IndexError: list index out of range
```

**Cause:** Gemma-4 31B and 26B-A4B ship with `num_kv_shared_layers = 0`. In Python, `-0 == 0`, so `layer_types[:-0]` collapses to `layer_types[:0] == []`. Cache is built with zero layer slots and the first attention forward crashes inside `Cache.update`.

```python
if hasattr(decoder_config, "num_kv_shared_layers"):
    layer_types = layer_types[: -decoder_config.num_kv_shared_layers]
```

### use_cache = True generation was gibberish for E2B, E4B

[Issue #45242](https://github.com/huggingface/transformers/issues/45242) -- `use_cache=False` corrupts attention computation.

Gemma-4 E2B and E4B share KV state across layers (`num_kv_shared_layers = 20` and `18`). When `use_cache=False` (as every QLoRA tutorial sets, and as `gradient_checkpointing=True` forces), `Gemma4TextModel.forward` skips cache construction, so KV-shared layers recompute K and V locally from current hidden states. Logits become garbage and training loss diverges.

**Before** (`unsloth/gemma-4-E2B-it`, prompt "What is 1+1?"):

```
use_cache=True  -> '1 + 1 = **2**'
use_cache=False -> 'BROAD\肯. Specificallyboard K supposed\_n통  \'
max_abs_logit_diff: 48.937500
```

**After fix:**

```
use_cache=True  -> '1 + 1 = **2**'
use_cache=False -> '1 + 1 = **2**'
max_abs_logit_diff: 0.000000     (bit-exact parity, all 9 tokens identical)
```

### Audio float16 overflow

`Gemma4AudioAttention` uses `config.attention_invalid_logits_value = -1e9` in a `masked_fill` call. On fp16 (Tesla T4), -1e9 overflows the fp16 max of 65504:

```python
RuntimeError: value cannot be converted to type c10::Half without overflow
```

Cause in `self.config.attention_invalid_logits_value`:

```python
attn_weights = attn_weights.masked_fill(
    attention_mask.logical_not(), self.config.attention_invalid_logits_value
)
```

### Tips for Gemma-4

1. **Preserve reasoning ability:** mix reasoning-style examples with direct answers (minimum 75% reasoning). Use `gemma-4` for non-thinking chat-template, `gemma-4-thinking` for thinking variant. Use thinking for 26B/31B, non-thinking for small ones.

   ```python
   from unsloth.chat_templates import get_chat_template
   tokenizer = get_chat_template(
       tokenizer,
       chat_template = "gemma-4-thinking", # Or "gemma-4"
   )
   ```

2. **Enable thinking mode** with `enable_thinking = True / False` in `tokenizer.apply_chat_template`:

   ```python
   processor.tokenizer.apply_chat_template([
       {"role" : "user", "content" : "What is 2+2?"},
   ], tokenize = False, enable_thinking = True, add_generation_prompt = True)
   ```

   Prints: `<bos><|turn>system\n<|think|><turn|>\n<|turn>user\nWhat is 2+2?<turn|>\n<|turn>model\n`

   Thinking disabled:

   ```python
   processor.tokenizer.apply_chat_template([
       {"role" : "user", "content" : "What is 2+2?"},
   ], tokenize = False, enable_thinking = False, add_generation_prompt = True)
   ```

   Prints: `<bos><|turn>user\nWhat is 2+2?<turn|>\n<|turn>model\n<|channel>thought\n<channel|>`

3. Gemma 4 supports **140 languages** -- good for multilingual fine-tuning.
4. **Recommended:** train E4B QLoRA over E2B LoRA (E4B is bigger, quantization accuracy difference is negligible). E4B LoRA is even better.
5. After fine-tuning, export to [[083-basics-inference-and-deployment-llama-server-and-openai-endpoint|GGUF]]/Ollama/etc.

## Quickstart

### Unsloth Studio Guide

[[097-new-studio|Unsloth Studio]] -- open-source web UI for local AI. Run models locally on MacOS, Windows, Linux and train on NVIDIA GPUs. Intel, MLX, AMD training support coming.

**1. Install Unsloth**

MacOS, Linux, WSL:

```bash
curl -fsSL https://unsloth.ai/install.sh | sh
```

Windows PowerShell:

```bash
irm https://unsloth.ai/install.ps1 | iex
```

> [!success] Installation takes ~1-2 mins.

**2. Launch Unsloth**

```bash
unsloth studio -H 0.0.0.0 -p 8888
```

Open `http://localhost:8888` in browser.

**3. Train Gemma 4**

Create password on first launch, complete onboarding wizard (skippable). Search for Gemma 4, select model and dataset, adjust hyperparameters and context length.

**4. Monitor training progress**

Training loss should decrease steadily. Model auto-saves when done.

**5. Export fine-tuned model**

Export to GGUF, safetensor etc. formats.

**6. Compare fine-tuned vs original**

Click `Compare Mode` to compare LoRA adapter and original model.

### Unsloth Core (code-based) Guide

**Notebooks:**

| [E4B **(Inference + Text)**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma4_\(E4B\)-Text.ipynb) | [E4B **(Vision + Text)**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma4_\(E4B\)-Vision.ipynb) | [E4B **(Audio)**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma4_\(E4B\)-Audio.ipynb) |
| --- | --- | --- |
| [**31B** (Kaggle)](https://www.kaggle.com/code/danielhanchen/gemma4-31b-unsloth) | [E2B **(Vision + Text)**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma4_\(E2B\)-Vision.ipynb) | [E2B **(Audio)**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma4_\(E2B\)-Audio.ipynb) |

RL notebook: [E2B **(RL GRPO)**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma4_\(E2B\)_Reinforcement_Learning_Sudoku_Game.ipynb)

Larger models need A100:

| [Gemma-4-26B-A4B (A100)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma4_\(26B_A4B\)-Vision.ipynb) | [Gemma-4-31B (A100)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma4_\(31B\)-Vision.ipynb) |
| --- | --- |

> [!info] GRPO works in Unsloth if you disable fast vLLM inference and use Unsloth inference instead. Follow [[071-get-started-reinforcement-learning-rl-guide-vision-reinforcement-learning-vlm-rl|Vision RL]] notebook examples.

#### Text SFT recipe (26B-A4B-it)

Text only -- for vision see [[096-basics-vision-fine-tuning|vision fine-tuning]].

````python
from unsloth import FastModel
import torch

model, tokenizer = FastModel.from_pretrained(
    model_name = "unsloth/gemma-4-26B-A4B-it", # Change to unsloth/gemma-4-E2B-it etc
    dtype = None, # None for auto detection
    max_seq_length = 8192, # Choose any for long context!
    load_in_4bit = True,  # 4 bit quantization to reduce memory
    full_finetuning = False, # [NEW!] We have full finetuning now!
    # token = "YOUR_HF_TOKEN", # HF Token for gated models
)

"""# Gemma 4 can process Text, Vision and Audio!

Let's first experience how Gemma 4 can handle multimodal inputs. We use Gemma 4's recommended settings of `temperature = 1.0, top_p = 0.95, top_k = 64`
"""

from transformers import TextStreamer
# Helper function for inference
def do_gemma_4_inference(messages, max_new_tokens = 128):
    _ = model.generate(
        **tokenizer.apply_chat_template(
            messages,
            add_generation_prompt = True, # Must add for generation
            tokenize = True,
            return_dict = True,
            return_tensors = "pt",
        ).to("cuda"),
        max_new_tokens = max_new_tokens,
        use_cache=True,
        temperature = 1.0, top_p = 0.95, top_k = 64,
        streamer = TextStreamer(tokenizer, skip_prompt = True),
    )

"""# Gemma 4 can see images!

<img src="https://files.worldwildlife.org/wwfcmsprod/images/Sloth_Sitting_iStock_3_12_2014/story_full_width/8l7pbjmj29_iStock_000011145477Large_mini__1_.jpg" alt="Alt text" height="256">
"""

sloth_link = "https://files.worldwildlife.org/wwfcmsprod/images/Sloth_Sitting_iStock_3_12_2014/story_full_width/8l7pbjmj29_iStock_000011145477Large_mini__1_.jpg"

messages = [{
    "role" : "user",
    "content": [
        { "type": "image", "image" : sloth_link },
        { "type": "text",  "text" : "Which films does this animal feature in?" }
    ]
}]
# You might have to wait 1 minute for Unsloth's auto compiler
do_gemma_4_inference(messages, max_new_tokens = 256)

"""Let's make a poem about sloths!"""

messages = [{
    "role": "user",
    "content": [{ "type" : "text",
                  "text" : "Write a poem about sloths." }]
}]
do_gemma_4_inference(messages)

"""# Let's finetune Gemma 4!

You can finetune the vision and text parts for now through selection - the audio part can also be finetuned - we're working to make it selectable as well!

We now add LoRA adapters so we only need to update a small amount of parameters!
"""

model = FastModel.get_peft_model(
    model,
    finetune_vision_layers     = False, # Turn off for just text!
    finetune_language_layers   = True,  # Should leave on!
    finetune_attention_modules = True,  # Attention good for GRPO
    finetune_mlp_modules       = True,  # Should leave on always!

    r = 8,           # Larger = higher accuracy, but might overfit
    lora_alpha = 8,  # Recommended alpha == r at least
    lora_dropout = 0,
    bias = "none",
    random_state = 3407,
)

"""<a name="Data"></a>
### Data Prep
We now use the `Gemma-4` format for conversation style finetunes. We use [Maxime Labonne's FineTome-100k](https://huggingface.co/datasets/mlabonne/FineTome-100k) dataset in ShareGPT style. Gemma-4 renders multi turn conversations like below:

```
<bos><|turn>user
Hello<turn|>
<|turn>model
Hey there!<turn|>
```
We use our `get_chat_template` function to get the correct chat template. We support `zephyr, chatml, mistral, llama, alpaca, vicuna, vicuna_old, phi3, llama3, phi4, qwen2.5, gemma3, gemma-4` and more.
"""

from unsloth.chat_templates import get_chat_template
tokenizer = get_chat_template(
    tokenizer,
    chat_template = "gemma-4-thinking",
)

"""We get the first 3000 rows of the dataset"""

from datasets import load_dataset
dataset = load_dataset("mlabonne/FineTome-100k", split = "train[:3000]")

"""We now use `standardize_data_formats` to try converting datasets to the correct format for finetuning purposes!"""

from unsloth.chat_templates import standardize_data_formats
dataset = standardize_data_formats(dataset)

"""Let's see how row 100 looks like!"""

dataset[100]

"""We now have to apply the chat template for `Gemma-3` onto the conversations, and save it to `text`. We remove the `<bos>` token using removeprefix(`'<bos>'`) since we're finetuning. The Processor will add this token before training and the model expects only one."""

def formatting_prompts_func(examples):
   convos = examples["conversations"]
   texts = [tokenizer.apply_chat_template(convo, tokenize = False, add_generation_prompt = False).removeprefix('<bos>') for convo in convos]
   return { "text" : texts, }

dataset = dataset.map(formatting_prompts_func, batched = True)

"""Let's see how the chat template did! Notice there is no `<bos>` token as the processor tokenizer will be adding one."""

dataset[100]["text"]

"""<a name="Train"></a>
### Train the model
Now let's train our model. We do 60 steps to speed things up, but you can set `num_train_epochs=1` for a full run, and turn off `max_steps=None`.
"""

from trl import SFTTrainer, SFTConfig
trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset,
    eval_dataset = None, # Can set up evaluation!
    args = SFTConfig(
        dataset_text_field = "text",
        per_device_train_batch_size = 1,
        gradient_accumulation_steps = 4, # Use GA to mimic batch size!
        warmup_steps = 5,
        # num_train_epochs = 1, # Set this for 1 full training run.
        max_steps = 60,
        learning_rate = 2e-4, # Reduce to 2e-5 for long training runs
        logging_steps = 1,
        optim = "adamw_8bit",
        weight_decay = 0.001,
        lr_scheduler_type = "linear",
        seed = 3407,
        report_to = "none", # Use TrackIO/WandB etc
    ),
)

"""We also use Unsloth's `train_on_completions` method to only train on the assistant outputs and ignore the loss on the user's inputs. This helps increase accuracy of finetunes!"""

from unsloth.chat_templates import train_on_responses_only
trainer = train_on_responses_only(
    trainer,
    instruction_part = "<|turn>user\n",
    response_part = "<|turn>model\n",
)

"""Let's verify masking the instruction part is done! Let's print the 100th row again.  Notice how the sample only has a single `<bos>` as expected!"""

tokenizer.decode(trainer.train_dataset[100]["input_ids"])

"""Now let's print the masked out example - you should see only the answer is present:"""

tokenizer.decode([tokenizer.pad_token_id if x == -100 else x for x in trainer.train_dataset[100]["labels"]]).replace(tokenizer.pad_token, " ")

"""# Let's train the model!

To resume a training run, set `trainer.train(resume_from_checkpoint = True)`
"""

trainer_stats = trainer.train()
````

> [!info] OOM mitigation
> - Drop `per_device_train_batch_size` to **1** and/or reduce `max_seq_length`.
> - Keep `use_gradient_checkpointing="unsloth"` on (designed to reduce VRAM and extend context).

**Loader example for MoE (bf16 LoRA):**

```python
import os
import torch
from unsloth import FastModel

model, tokenizer = FastModel.from_pretrained(
    model_name = "unsloth/Gemma-4-26B-A4B-it",
    max_seq_length = 2048,
    load_in_4bit = False,     # MoE QLoRA not recommended, dense 31B is fine
    load_in_16bit = True,     # bf16/16-bit LoRA
    full_finetuning = False,
)
```

Attach LoRA adapters and train similarly to the SFT example above.

## Reinforcement Learning (RL)

Train Gemma 4 with RL, GSPO, GRPO etc: [free notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_\(4B\)_Vision_GRPO.ipynb).

E2B RL works on 9GB. Goal: make Gemma 4 learn to solve Sudoku puzzles using [[072-get-started-reinforcement-learning-rl-guide|GRPO]]. Model devises strategy to fill cells; reward for correct placements and completing valid puzzles.

Run Gemma 4 RL with Unsloth (not supported by vLLM) by setting `fast_inference=False`:

```python
from unsloth import FastLanguageModel

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/gemma-4-E2B-it",
    fast_inference=False,
)
```

## MoE fine-tuning (26B-A4B)

26B-A4B is the speed/quality middle ground. MoE model with subset of parameters active per token.

- Use **LoRA** rather than full fine-tuning
- Prefer **16-bit / bf16 LoRA** if memory allows
- Start with shorter contexts and smaller ranks first
- Scale up only after pipeline is stable
- For highest quality with more memory, use **31B** instead

## Multimodal fine-tuning (E2B / E4B)

E2B and E4B support image and audio -- main multimodal variants.

- Load multimodal model with `FastVisionModel`
- Keep `finetune_vision_layers = False` first
- Fine-tune language, attention, and MLP layers only
- Enable vision/audio layers later if task needs it

### Gemma 4 Multimodal LoRA example

````python
from unsloth import FastVisionModel # FastLanguageModel for LLMs
import torch

model, processor = FastVisionModel.from_pretrained(
    "unsloth/gemma-4-26B-A4B-it",
    load_in_4bit = True, # Use 4bit to reduce memory use. False for 16bit LoRA.
    use_gradient_checkpointing = "unsloth", # True or "unsloth" for long context
)

"""We now add LoRA adapters for parameter efficient fine-tuning, allowing us to train only 1% of all model parameters efficiently.

**[NEW]** We also support fine-tuning only the vision component, only the language component, or both. Additionally, you can choose to fine-tune the attention modules, the MLP layers, or both!
"""

model = FastVisionModel.get_peft_model(
    model,
    finetune_vision_layers     = True, # False if not finetuning vision layers
    finetune_language_layers   = True, # False if not finetuning language layers
    finetune_attention_modules = True, # False if not finetuning attention layers
    finetune_mlp_modules       = True, # False if not finetuning MLP layers

    r = 32,                           # The larger, the higher the accuracy, but might overfit
    lora_alpha = 32,                  # Recommended alpha == r at least
    lora_dropout = 0,
    bias = "none",
    random_state = 3407,
    use_rslora = False,               # We support rank stabilized LoRA
    loftq_config = None,               # And LoftQ
    target_modules = "all-linear",    # Optional now! Can specify a list if needed
)

"""<a name="Data"></a>
### Data Prep
We'll use a sampled dataset of handwritten math formulas. The objective is to convert these images into a computer-readable format—specifically LaTeX—so they can be rendered. This is particularly useful for complex expressions.

You can access the dataset [here](https://huggingface.co/datasets/unsloth/LaTeX_OCR). The full dataset is [here](https://huggingface.co/datasets/linxy/LaTeX_OCR).
"""

from datasets import load_dataset
dataset = load_dataset("unsloth/LaTeX_OCR", split = "train")

"""Let's take an overview of the dataset. We'll examine the second image and its corresponding caption."""

dataset

dataset[2]["image"]

dataset[2]["text"]

"""We can also render LaTeX directly in the browser!"""

from IPython.display import display, Math, Latex

latex = dataset[3]["text"]
display(Math(latex))

"""To format the dataset, all vision fine-tuning tasks should follow this format:

```python
[
    {
        "role": "user",
        "content": [
            {"type": "text", "text": instruction},
            {"type": "image", "image": sample["image"]},
        ],
    },
    {
        "role": "user",
        "content": [
            {"type": "text", "text": instruction},
            {"type": "image", "image": sample["image"]},
        ],
    },
]
```
"""

instruction = "Write the LaTeX representation for this image."

def convert_to_conversation(sample):
    conversation = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": instruction},
                {"type": "image", "image": sample["image"]},
            ],
        },
        {"role": "assistant", "content": [{"type": "text", "text": sample["text"]}]},
    ]
    return {"messages": conversation}
pass

"""Let's convert the dataset into the "correct" format for finetuning:"""

converted_dataset = [convert_to_conversation(sample) for sample in dataset]

"""The first example is now structured like below:"""

converted_dataset[0]

"""Lets take the Gemma 4 instruction chat template and use it in our base model"""

from unsloth import get_chat_template

processor = get_chat_template(
    processor,
    "gemma-4-thinking"
)

"""Before fine-tuning, let us evaluate the base model's performance. We do not expect strong results, as it has not encountered this chat template before."""

image = dataset[2]["image"]
instruction = "Write the LaTeX representation for this image."

messages = [
    {
        "role": "user",
        "content": [{"type": "image"}, {"type": "text", "text": instruction}],
    }
]
input_text = processor.apply_chat_template(messages, add_generation_prompt = True)
inputs = processor(
    image,
    input_text,
    add_special_tokens = False,
    return_tensors = "pt",
).to("cuda")

from transformers import TextStreamer

text_streamer = TextStreamer(processor, skip_prompt = True)
result = model.generate(**inputs, streamer = text_streamer, max_new_tokens = 128,
                        use_cache = True, temperature = 1.0, top_p = 0.95, top_k = 64)

"""You can see it's absolutely terrible! It doesn't follow instructions at all

<a name="Train"></a>
### Train the model
Now let's train our model. We do 60 steps to speed things up, but you can set `num_train_epochs=1` for a full run, and turn off `max_steps=None`. We also support `DPOTrainer` and `GRPOTrainer` for reinforcement learning!!

We use our new `UnslothVisionDataCollator` which will help in our vision finetuning setup.
"""

from unsloth.trainer import UnslothVisionDataCollator
from trl import SFTTrainer, SFTConfig

trainer = SFTTrainer(
    model = model,
    train_dataset = converted_dataset,
    processing_class = processor.tokenizer,
    data_collator = UnslothVisionDataCollator(model, processor),
    args = SFTConfig(
        per_device_train_batch_size = 1,
        gradient_accumulation_steps = 4,
        max_grad_norm = 0.3,
        warmup_ratio = 0.03,
        max_steps = 60,
        # num_train_epochs = 2, # Set this instead of max_steps for full training runs
        learning_rate = 2e-4,
        logging_steps = 1,
        save_strategy = "steps",
        optim = "adamw_8bit",
        weight_decay = 0.001,
        lr_scheduler_type = "cosine",
        seed = 3407,
        output_dir = "outputs",
        report_to = "none", # For Weights and Biases or others

        # You MUST put the below items for vision finetuning:
        remove_unused_columns = False,
        dataset_text_field = "",
        dataset_kwargs = {"skip_prepare_dataset": True},
        max_length = 2048,
    )
)

trainer_stats = trainer.train()
````

### Image example format

For Gemma 4 multimodal prompts, put image **before** text instruction.

```json
{
  "messages": [
    {
      "role": "user",
      "content": [
        {"type": "image", "image": "/path/to/image OR object"},
        {"type": "text", "text": "Extract all text from this receipt. Return line items, total, merchant, and date as JSON."}
      ]
    },
    {
      "role": "assistant",
      "content": [
        {"type": "text", "text": "{\"merchant\": \"Example Store\", \"total\": \"19.99\"}"}
      ]
    }
  ]
}
```

### Audio example format

Audio is for **E2B / E4B** only. Keep clips short and task-specific.

```json
{
  "messages": [
    {
      "role": "user",
      "content": [
        {"type": "audio", "audio": "/path/to/audio OR object"},
        {"type": "text", "text": "Transcribe the following speech segment in English into English text. Only output the transcription."}
      ]
    },
    {
      "role": "assistant",
      "content": [
        {"type": "text", "text": "Hello everyone and welcome back."}
      ]
    }
  ]
}
```

## Saving / export fine-tuned model

Deployment guides: [[097-new-studio|Unsloth Studio]], [[086-basics-inference-and-deployment-saving-to-gguf|llama.cpp]], [[090-basics-inference-and-deployment-vllm-guide|vLLM]], [[083-basics-inference-and-deployment-llama-server-and-openai-endpoint|llama-server]], [[087-basics-inference-and-deployment-saving-to-ollama|Ollama]], [[088-basics-inference-and-deployment-sglang-guide|SGLang]].

### Save to GGUF

```python
model.save_pretrained_gguf("directory", tokenizer, quantization_method = "q4_k_m")
model.save_pretrained_gguf("directory", tokenizer, quantization_method = "q8_0")
model.save_pretrained_gguf("directory", tokenizer, quantization_method = "f16")
```

Push GGUFs to Hugging Face:

```python
model.push_to_hub_gguf("hf_username/directory", tokenizer, quantization_method = "q4_k_m")
model.push_to_hub_gguf("hf_username/directory", tokenizer, quantization_method = "q8_0")
```

> [!warning] If exported model behaves worse in another runtime, most common cause: **wrong chat template / EOS token at inference time** (must use same chat template trained with).

## Gemma 4 data best practices

### 1. Use standard chat roles

Gemma 4 uses: `system`, `user`, `assistant`. SFT dataset should use regular chat format, not older Gemma-specific role formats.

### 2. Thinking mode is explicit

To preserve thinking-style behavior during SFT:

- Keep format consistent
- Decide: train on **visible thought blocks** or **final answers only**
- Do **not** mix incompatible thought formats in same dataset

For most production assistants: fine-tune on **final visible answer only**.

### 3. Multi-turn rule

Only keep **final visible answer** in conversation history. Do **not** feed earlier thought blocks back into later turns.

---

## Agent Instructions: Querying This Documentation

If you need additional information not on this page, query dynamically:

```
GET https://unsloth.ai/docs/models/gemma-4/train.md?ask=<question>
```

Question should be specific, self-contained, natural language. Response contains direct answer with relevant excerpts and sources.

#gemma-4 #fine-tuning #unsloth #multimodal #vr
