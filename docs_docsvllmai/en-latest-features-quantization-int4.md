---
title: INT4 W4A16 - vLLM
url: https://docs.vllm.ai/en/latest/features/quantization/int4/
source: sitemap
fetched_at: 2026-05-07T21:14:27.919794042-03:00
rendered_js: false
word_count: 419
summary: This document provides a guide on how to quantize large language models to INT4 format using the llm-compressor library to achieve memory optimization and improved inference performance in vLLM.
tags:
    - int4-quantization
    - llm-compression
    - vllm
    - model-optimization
    - gptq
    - inference-acceleration
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/features/quantization/int4.md "Edit this page")

vLLM supports quantizing weights to INT4 for memory savings and inference acceleration. This quantization method is particularly useful for reducing model size and maintaining low latency in workloads with low queries per second (QPS).

Please visit the HF collection of [quantized INT4 checkpoints of popular LLMs ready to use with vLLM](https://huggingface.co/collections/neuralmagic/int4-llms-for-vllm-668ec34bf3c9fa45f857df2c).

Note

INT4 computation is supported on NVIDIA GPUs with compute capability &gt; 8.0 (Ampere, Ada Lovelace, Hopper, Blackwell).

## Prerequisites[¶](#prerequisites "Permanent link")

To use INT4 quantization with vLLM, you'll need to install the [llm-compressor](https://github.com/vllm-project/llm-compressor/) library:

```
pipinstallllmcompressor
```

Additionally, install `vllm` and `lm-evaluation-harness` for evaluation:

```
pipinstallvllm"lm-eval[api]>=0.4.11"
```

## Quantization Process[¶](#quantization-process "Permanent link")

The quantization process involves four main steps:

1. Loading the model
2. Preparing calibration data
3. Applying quantization
4. Evaluating accuracy in vLLM

### 1. Loading the Model[¶](#1-loading-the-model "Permanent link")

Load your model and tokenizer using the standard `transformers` AutoModel classes:

```
fromtransformersimport AutoTokenizer, AutoModelForCausalLM

MODEL_ID = "meta-llama/Meta-Llama-3-8B-Instruct"
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    device_map="auto",
    dtype="auto",
)
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
```

### 2. Preparing Calibration Data[¶](#2-preparing-calibration-data "Permanent link")

When quantizing weights to INT4, you need sample data to estimate the weight updates and calibrated scales. It's best to use calibration data that closely matches your deployment data. For a general-purpose instruction-tuned model, you can use a dataset like `ultrachat`:

Code

```
fromdatasetsimport load_dataset

NUM_CALIBRATION_SAMPLES = 512
MAX_SEQUENCE_LENGTH = 2048

# Load and preprocess the dataset
ds = load_dataset("HuggingFaceH4/ultrachat_200k", split="train_sft")
ds = ds.shuffle(seed=42).select(range(NUM_CALIBRATION_SAMPLES))

defpreprocess(example):
    return {"text": tokenizer.apply_chat_template(example["messages"], tokenize=False)}
ds = ds.map(preprocess)

deftokenize(sample):
    return tokenizer(sample["text"], padding=False, max_length=MAX_SEQUENCE_LENGTH, truncation=True, add_special_tokens=False)
ds = ds.map(tokenize, remove_columns=ds.column_names)
```

### 3. Applying Quantization[¶](#3-applying-quantization "Permanent link")

Now, apply the quantization algorithms:

Code

```
fromllmcompressorimport oneshot
fromllmcompressor.modifiers.quantizationimport GPTQModifier
fromllmcompressor.modifiers.smoothquantimport SmoothQuantModifier

# Configure the quantization algorithms
recipe = GPTQModifier(targets="Linear", scheme="W4A16", ignore=["lm_head"])

# Apply quantization
oneshot(
    model=model,
    dataset=ds,
    recipe=recipe,
    max_seq_length=MAX_SEQUENCE_LENGTH,
    num_calibration_samples=NUM_CALIBRATION_SAMPLES,
)

# Save the compressed model: Meta-Llama-3-8B-Instruct-W4A16-G128
SAVE_DIR = MODEL_ID.split("/")[1] + "-W4A16-G128"
model.save_pretrained(SAVE_DIR, save_compressed=True)
tokenizer.save_pretrained(SAVE_DIR)
```

This process creates a W4A16 model with weights quantized to 4-bit integers.

### 4. Evaluating Accuracy[¶](#4-evaluating-accuracy "Permanent link")

After quantization, you can load and run the model in vLLM:

```
fromvllmimport LLM

llm = LLM("./Meta-Llama-3-8B-Instruct-W4A16-G128")
```

To evaluate accuracy, you can use `lm_eval`:

```
lm_eval--modelvllm\
--model_argspretrained="./Meta-Llama-3-8B-Instruct-W4A16-G128",add_bos_token=true\
--tasksgsm8k\
--num_fewshot5\
--limit250\
--batch_size'auto'
```

Note

Quantized models can be sensitive to the presence of the `bos` token. Make sure to include the `add_bos_token=True` argument when running evaluations.

## Best Practices[¶](#best-practices "Permanent link")

- Start with 512 samples for calibration data, and increase if accuracy drops
- Ensure the calibration data contains a high variety of samples to prevent overfitting towards a specific use case
- Use a sequence length of 2048 as a starting point
- Employ the chat template or instruction template that the model was trained with
- If you've fine-tuned a model, consider using a sample of your training data for calibration
- Tune key hyperparameters to the quantization algorithm:
  
  - `dampening_frac` sets how much influence the GPTQ algorithm has. Lower values can improve accuracy, but can lead to numerical instabilities that cause the algorithm to fail.
  - `actorder` sets the activation ordering. When compressing the weights of a layer weight, the order in which channels are quantized matters. Setting `actorder="weight"` can improve accuracy without added latency.

The following is an example of an expanded quantization recipe you can tune to your own use case:

Code

```
fromcompressed_tensors.quantizationimport (
    QuantizationArgs,
    QuantizationScheme,
    QuantizationStrategy,
    QuantizationType,
) 
recipe = GPTQModifier(
    targets="Linear",
    config_groups={
        "config_group": QuantizationScheme(
            targets=["Linear"],
            weights=QuantizationArgs(
                num_bits=4,
                type=QuantizationType.INT,
                strategy=QuantizationStrategy.GROUP,
                group_size=128,
                symmetric=True,
                dynamic=False,
                actorder="weight",
            ),
        ),
    },
    ignore=["lm_head"],
    update_size=NUM_CALIBRATION_SAMPLES,
    dampening_frac=0.01,
)
```

## Troubleshooting and Support[¶](#troubleshooting-and-support "Permanent link")

If you encounter any issues or have feature requests, please open an issue on the [vllm-project/llm-compressor](https://github.com/vllm-project/llm-compressor/issues) GitHub repository. The full INT4 quantization example in `llm-compressor` is available [here](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w4a16/llama3_example.py).