---
title: Text-to-Speech (TTS) Fine-tuning Guide
url: https://unsloth.ai/docs/basics/text-to-speech-tts-fine-tuning.md
source: llms
fetched_at: 2026-04-27T18:15:02.981555352-03:00
rendered_js: false
word_count: 2072
summary: This guide details how to fine-tune Text-to-Speech (TTS) models, specifically leveraging Unsloth for faster training, allowing customization of voice tone and style. It covers model selection, data preparation using audio/transcript pairs, and provides concrete examples of loading and configuring various TTS architectures.
tags:
    - tts
    - fine-tuning
    - unsloth
    - text-to-speech
    - voice-cloning
    - huggingface
    - model-adaptation
category: guide
optimized: true
optimized_at: 2026-04-27T21:36:00Z
---

# Text-to-Speech (TTS) Fine-tuning Guide

Fine-tune TTS models to clone voices, adapt speaking styles, support new languages, and handle specific tasks. Also supports STT models like OpenAI's Whisper.

Unsloth fine-tunes any `transformers`-compatible TTS model **1.5x faster with 50% less memory** via Flash Attention 2. Even unlisted models (e.g., Dia-TTS, Moshi) are supported.

> [!info] Zero-shot cloning captures tone but misses pacing and expression, sounding robotic. Fine-tuning delivers far more realistic voice replication. [See comparison below](#fine-tuning-voice-models-vs-zero-shot-voice-cloning).

## Fine-tuning Notebooks

TTS models (original + quantized) on [Hugging Face](https://huggingface.co/collections/unsloth/text-to-speech-tts-models-68007ab12522e96be1e02155):

| Model | Link |
|---|---|
| Sesame-CSM (1B) | [Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Sesame_CSM_\(1B\)-TTS.ipynb) |
| Orpheus-TTS (3B) | [Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Orpheus_\(3B\)-TTS.ipynb) |
| Spark-TTS (0.5B) | [Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Spark_TTS_\(0_5B\).ipynb) |
| Llasa-TTS (1B) | [Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llasa_TTS_\(1B\).ipynb) |
| Whisper Large V3 (STT) | [Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Whisper.ipynb) |
| Oute-TTS (1B) | [Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Oute_TTS_\(1B\).ipynb) |

> [!tip] If output duration caps at 10 seconds, increase `max_new_tokens` above its default of 125 (125 tokens = ~10s of audio).

## Choosing and Loading a TTS Model

Smaller models (< 3B params) preferred for lower latency and faster inference. Primary examples: Sesame-CSM (1B) and Orpheus-TTS (3B, Llama-based).

### Sesame-CSM (1B)

- **CSM-1B** -- base model, requires audio context per speaker for consistency
- **Orpheus-ft** -- fine-tuned on 8 professional voice actors, consistency built in
- CSM needs more compute for fine-tuning; Orpheus-ft gives better results out of the box
- New sampling options added for audio context in CSM

### Orpheus-TTS (3B)

Pre-trained on large speech corpus with built-in emotional cue support (laughs, sighs). Easiest TTS model to train -- exportable via llama.cpp for broad inference engine compatibility. Unsupported models can only save LoRA adapter safetensors.

### Loading Models

Voice models are small enough for LoRA 16-bit or full fine-tuning (FFT). LoRA 16-bit loading:

```python
from unsloth import FastModel

model_name = "unsloth/orpheus-3b-0.1-pretrained"
model, tokenizer = FastModel.from_pretrained(
    model_name,
    load_in_4bit=False  # use 4-bit precision (QLoRA)
)
```

- `load_in_8bit=True` for 8-bit
- `full_finetuning=True` for FFT (ensure sufficient VRAM)
- Replace `model_name` with any other TTS model

> [!info] Orpheus's tokenizer includes special tokens for audio output. No separate vocoder needed -- Orpheus outputs audio tokens directly, decodable to waveform.

## Preparing Your Dataset

Minimum requirement: **audio clips + corresponding transcripts**.

Example: [Elise dataset](https://huggingface.co/datasets/MrDragonFox/Elise) (~3h single-speaker English corpus, ~1200 samples, ~328MB):

- **`MrDragonFox/Elise`** -- augmented with emotion tags (`<sigh>`, `<laughs>`) embedded in transcripts
- **`Jinsaryko/Elise`** -- base version without special tags

Dataset fields: `audio` (waveform), `text` (transcription), metadata (speaker name, pitch stats, etc.).

> [!tip] Priority: fully annotated and properly normalized dataset, not just tone/cadence/pitch.

> [!info] With **Sesame-CSM-1B** (base model), speaker ID 0 causes voice variation across generations because fixed voice identities don't exist. Speaker ID tokens maintain consistency **within a conversation**, not across separate generations. Provide contextual examples (reference audio clips or prior utterances) for consistent voice.

### Option 1: Hugging Face Datasets

```python
from datasets import load_dataset, Audio

dataset = load_dataset("MrDragonFox/Elise", split="train")
print(len(dataset), "samples")  # ~1200 samples

# Ensure 24 kHz sampling rate (Orpheus expected rate)
dataset = dataset.cast_column("audio", Audio(sampling_rate=24000))
```

Each item: `"audio"` (waveform array + metadata), `"text"` (transcript string).

**Emotion tags** Orpheus supports: `<laugh>`, `<chuckle>`, `<sigh>`, `<cough>`, `<sniffle>`, `<groan>`, `<yawn>`, `<gasp>`. Example: `"I missed you <laugh> so much!"`. Tags in `<angle_brackets>` treated as special tokens. Elise dataset includes 336 "laughs", 156 "sighs", etc. Annotate manually if your dataset lacks them.

### Option 2: Custom Dataset

1. Organize audio clips (WAV/FLAC) in a folder
2. Create CSV/TSV with `filename,text` columns:

   ```
   filename,text
   0001.wav,Hello there!
   0002.wav,<sigh> I am very tired.
   ```

3. Load and cast audio column:

```python
from datasets import load_dataset, Audio
dataset = load_dataset("csv", data_files="mydata.csv", split="train")
dataset = dataset.cast_column("filename", Audio(sampling_rate=24000))
```

**Requirements:**
- List of (audio, text) pairs
- Consistent sampling rate (resample to model's expected rate, e.g., 24kHz for Orpheus)
- Normalized transcripts (no unusual characters except emotion tags in `<angle_brackets>`)
- Optional: speaker ID token for multi-speaker (beyond this guide)

## Fine-Tuning TTS with Unsloth

### Step 1: Load Model and Dataset

All TTS notebooks use LoRA 16-bit training (`load_in_4bit = False`) for better accuracy:

```python
from unsloth import FastLanguageModel
import torch
dtype = None # None for auto detection. Float16 for Tesla T4, V100, Bfloat16 for Ampere+
load_in_4bit = False # Use 4bit quantization to reduce memory usage. Can be False.

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/orpheus-3b-0.1-ft",
    max_seq_length= 2048, # Choose any for long context!
    dtype = dtype,
    load_in_4bit = load_in_4bit,
    #token = "hf_...", # use one if using gated models like meta-llama/Llama-2-7b-hf
)

from datasets import load_dataset
dataset = load_dataset("MrDragonFox/Elise", split = "train")
```

> [!info] If memory limited or dataset large, stream or load in chunks. 3h of audio fits in RAM.

### Step 2: Preprocess Data (Optional/Advanced)

Train in causal manner: concatenate text and audio token IDs as target sequence. Orpheus (decoder-only LLM) takes text as input and audio token IDs as labels. Unsloth may handle this automatically if model config identifies it as TTS.

```python
def preprocess_function(example):
    tokens = tokenizer(example["text"], return_tensors="pt")
    input_ids = tokens["input_ids"].squeeze(0)
    return {"input_ids": input_ids, "labels": input_ids}

train_data = dataset.map(preprocess_function, remove_columns=dataset.column_names)
```

> [!info] This is simplified. Proper Orpheus fine-tuning requires **audio tokens as training labels** -- audio encoded to discrete tokens via Orpheus's audio codec. The [Orpheus GitHub](https://github.com/canopyai/Orpheus-TTS) provides a script encoding audio into `<custom_token_x>` token sequences. Simply using text tokens won't teach the model actual audio patterns.

### Step 3: Set Up Trainer

```python
from transformers import TrainingArguments,Trainer,DataCollatorForSeq2Seq
from unsloth import is_bfloat16_supported

trainer = Trainer(
    model = model,
    train_dataset = dataset,
    args = TrainingArguments(
        per_device_train_batch_size = 1,
        gradient_accumulation_steps = 4,
        warmup_steps = 5,
        # num_train_epochs = 1, # Set this for 1 full training run.
        max_steps = 60,
        learning_rate = 2e-4,
        fp16 = not is_bfloat16_supported(),
        bf16 = is_bfloat16_supported(),
        logging_steps = 1,
        optim = "adamw_8bit",
        weight_decay = 0.01,
        lr_scheduler_type = "linear",
        seed = 3407,
        output_dir = "outputs",
        report_to = "none", # Use this for WandB etc
    ),
)
```

- 60 steps for speed; use `num_train_epochs=1` for full run (set `max_steps=None`)
- `per_device_train_batch_size > 1` may cause multi-GPU errors -- set `CUDA_VISIBLE_DEVICES=0`
- Colab T4: 1-2 hours for a few epochs on 3h data

### Step 4: Train

Start training. Loss logged every `logging_steps` steps.

### Step 5: Save Model

Saves LoRA adapters only (not full model). To save to 16-bit or GGUF, see deployment docs.

```python
model.save_pretrained("lora_model")  # Local saving
tokenizer.save_pretrained("lora_model")
# model.push_to_hub("your_name/lora_model", token = "...") # Online saving
# tokenizer.push_to_hub("your_name/lora_model", token = "...") # Online saving
```

## Fine-tuning Voice Models vs. Zero-shot Voice Cloning

- **Zero-shot cloning** (e.g., XTTS with 30s audio): captures general **tone and timbre** only. Misses speaking speed, phrasing, vocal quirks, prosody subtleties. Speech follows the **model's style**, not the speaker's.
- **Fine-tuning (LoRA)**: truly captures how someone speaks -- personality, expressiveness, full vocal range.

Use zero-shot if a different voice is sufficient. Use fine-tuning for personalized or expressive replication.

#tts #fine-tuning #voice-cloning #unsloth #huggingface
