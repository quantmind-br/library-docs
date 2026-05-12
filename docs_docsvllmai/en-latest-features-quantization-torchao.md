---
title: TorchAO - vLLM
url: https://docs.vllm.ai/en/latest/features/quantization/torchao/
source: sitemap
fetched_at: 2026-05-07T21:14:35.390861738-03:00
rendered_js: false
word_count: 96
summary: This document provides an overview of integrating the TorchAO architecture optimization library with PyTorch for model quantization, including installation instructions and implementation examples for HuggingFace models.
tags:
    - torchao
    - model-quantization
    - pytorch
    - huggingface
    - inference-optimization
    - deep-learning
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/features/quantization/torchao.md "Edit this page")

TorchAO is an architecture optimization library for PyTorch, it provides high performance dtypes, optimization techniques and kernels for inference and training, featuring composability with native PyTorch features like torch.compile, FSDP etc.. Some benchmark numbers can be found [here](https://github.com/pytorch/ao/tree/main/torchao/quantization#benchmarks).

We recommend installing the latest torchao nightly with

```
# Install the latest TorchAO nightly build
# Choose the CUDA version that matches your system (cu126, cu128, etc.)
pipinstall\
--pretorchao>=10.0.0\
--index-urlhttps://download.pytorch.org/whl/nightly/cu126
```

## Quantizing HuggingFace Models[¶](#quantizing-huggingface-models "Permanent link")

You can quantize your own huggingface model with torchao, e.g. [transformers](https://huggingface.co/docs/transformers/main/en/quantization/torchao) and [diffusers](https://huggingface.co/docs/diffusers/en/quantization/torchao), and save the checkpoint to huggingface hub like [this](https://huggingface.co/jerryzh168/llama3-8b-int8wo) with the following example code:

Code

```
importtorch
fromtransformersimport TorchAoConfig, AutoModelForCausalLM, AutoTokenizer
fromtorchao.quantizationimport Int8WeightOnlyConfig

model_name = "meta-llama/Meta-Llama-3-8B"
quantization_config = TorchAoConfig(Int8WeightOnlyConfig())
quantized_model = AutoModelForCausalLM.from_pretrained(
    model_name,
    dtype="auto",
    device_map="auto",
    quantization_config=quantization_config
)
tokenizer = AutoTokenizer.from_pretrained(model_name)
input_text = "What are we having for dinner?"
input_ids = tokenizer(input_text, return_tensors="pt").to("cuda")

hub_repo = # YOUR HUB REPO ID
tokenizer.push_to_hub(hub_repo)
quantized_model.push_to_hub(hub_repo, safe_serialization=False)
```

Alternatively, you can use the [TorchAO Quantization space](https://huggingface.co/spaces/medmekk/TorchAO_Quantization) for quantizing models with a simple UI.