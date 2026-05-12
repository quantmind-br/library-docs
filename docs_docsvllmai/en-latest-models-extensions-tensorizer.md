---
title: Loading models with CoreWeave's Tensorizer
url: https://docs.vllm.ai/en/latest/models/extensions/tensorizer/
source: sitemap
fetched_at: 2026-05-07T21:14:58.23535186-03:00
rendered_js: false
word_count: 434
summary: This document explains how to integrate CoreWeave's Tensorizer with vLLM to enable rapid model serialization and deserialization for faster startup times and reduced memory usage.
tags:
    - vllm
    - tensorizer
    - model-loading
    - serialization
    - inference-optimization
    - gpu-deployment
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/models/extensions/tensorizer.md "Edit this page")

vLLM supports loading models with [CoreWeave's Tensorizer](https://docs.coreweave.com/coreweave-machine-learning-and-ai/inference/tensorizer). vLLM model tensors that have been serialized to disk, an HTTP/HTTPS endpoint, or S3 endpoint can be deserialized at runtime extremely quickly directly to the GPU, resulting in significantly shorter Pod startup times and CPU memory usage. Tensor encryption is also supported.

vLLM fully integrates Tensorizer in to its model loading machinery. The following will give a brief overview on how to get started with using Tensorizer on vLLM.

## Installing Tensorizer[¶](#installing-tensorizer "Permanent link")

To install `tensorizer`, run `pip install vllm[tensorizer]`.

## The basics[¶](#the-basics "Permanent link")

To load a model using Tensorizer, the model first needs to be serialized by Tensorizer. [The example script](https://docs.vllm.ai/en/latest/examples/others/tensorize_vllm_model/) takes care of this process.

Let's walk through a basic example by serializing `facebook/opt-125m` using the script, and then loading it for inference.

## Serializing a vLLM model with Tensorizer[¶](#serializing-a-vllm-model-with-tensorizer "Permanent link")

To serialize a model with Tensorizer, call the example script with the necessary CLI arguments. The docstring for the script itself explains the CLI args and how to use it properly in great detail, and we'll use one of the examples from the docstring directly, assuming we want to serialize and save our model at our S3 bucket example `s3://my-bucket`:

```
pythonexamples/others/tensorize_vllm_model.py\
--modelfacebook/opt-125m\
serialize\
--serialized-directorys3://my-bucket\
--suffixv1
```

This saves the model tensors at `s3://my-bucket/vllm/facebook/opt-125m/v1`. If you intend on applying a LoRA adapter to your tensorized model, you can pass the HF id of the LoRA adapter in the above command, and the artifacts will be saved there too:

```
pythonexamples/others/tensorize_vllm_model.py\
--modelfacebook/opt-125m\
--lora-path<lora_id>\
serialize\
--serialized-directorys3://my-bucket\
--suffixv1
```

## Serving the model using Tensorizer[¶](#serving-the-model-using-tensorizer "Permanent link")

Once the model is serialized where you want it, you can load the model using `vllm serve` or the [`LLM`](https://docs.vllm.ai/en/latest/api/vllm/entrypoints/llm/#vllm.entrypoints.llm.LLM "            LLM") entrypoint. You can pass the directory where you saved the model to the `model` argument for `LLM()` and `vllm serve`. For example, to serve the tensorized model saved previously with the LoRA adapter, you'd do:

```
vllmserves3://my-bucket/vllm/facebook/opt-125m/v1\
--load-formattensorizer\
--enable-lora
```

Or, with `LLM()`:

```
fromvllmimport LLM
llm = LLM(
    "s3://my-bucket/vllm/facebook/opt-125m/v1", 
    load_format="tensorizer",
    enable_lora=True,
)
```

## Options for configuring Tensorizer[¶](#options-for-configuring-tensorizer "Permanent link")

`tensorizer`'s core objects that serialize and deserialize models are `TensorSerializer` and `TensorDeserializer` respectively. In order to pass arbitrary kwargs to these, which will configure the serialization and deserialization processes, you can provide them as keys to `model_loader_extra_config` with `serialization_kwargs` and `deserialization_kwargs` respectively. Full docstrings detailing all parameters for the aforementioned objects can be found in `tensorizer`'s [serialization.py](https://github.com/coreweave/tensorizer/blob/main/tensorizer/serialization.py) file.

As an example, CPU concurrency can be limited when serializing with `tensorizer` via the `limit_cpu_concurrency` parameter in the initializer for `TensorSerializer`. To set `limit_cpu_concurrency` to some arbitrary value, you would do so like this when serializing:

```
pythonexamples/others/tensorize_vllm_model.py\
--modelfacebook/opt-125m\
--lora-path<lora_id>\
serialize\
--serialized-directorys3://my-bucket\
--serialization-kwargs'{"limit_cpu_concurrency": 2}'\
--suffixv1
```

As an example when customizing the loading process via `TensorDeserializer`, you could limit the number of concurrency readers during deserialization with the `num_readers` parameter in the initializer via `model_loader_extra_config` like so:

```
vllmserves3://my-bucket/vllm/facebook/opt-125m/v1\
--load-formattensorizer\
--enable-lora\
--model-loader-extra-config'{"deserialization_kwargs": {"num_readers": 2}}'
```

Or with `LLM()`:

```
fromvllmimport LLM
llm = LLM(
    "s3://my-bucket/vllm/facebook/opt-125m/v1", 
    load_format="tensorizer",
    enable_lora=True,
    model_loader_extra_config={"deserialization_kwargs": {"num_readers": 2}},
)
```