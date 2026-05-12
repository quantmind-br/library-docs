---
title: Registering a Model - vLLM
url: https://docs.vllm.ai/en/latest/contributing/model/registration/
source: sitemap
fetched_at: 2026-05-07T21:11:29.829329241-03:00
rendered_js: false
word_count: 210
summary: This document outlines the procedures for registering new machine learning model architectures within the vLLM framework, covering both built-in library additions and out-of-tree plugin implementations.
tags:
    - vllm
    - model-registration
    - machine-learning
    - plugin-development
    - model-architecture
    - open-source
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/contributing/model/registration.md "Edit this page")

vLLM relies on a model registry to determine how to run each model. A list of pre-registered architectures can be found [here](https://docs.vllm.ai/en/latest/models/supported_models/).

If your model is not on this list, you must register it to vLLM. This page provides detailed instructions on how to do so.

## Built-in models[¶](#built-in-models "Permanent link")

To add a model directly to the vLLM library, start by forking our [GitHub repository](https://github.com/vllm-project/vllm) and then [build it from source](https://docs.vllm.ai/en/latest/getting_started/installation/gpu/#build-wheel-from-source). This gives you the ability to modify the codebase and test your model.

After you have implemented your model (see [tutorial](https://docs.vllm.ai/en/latest/contributing/model/basic/)), put it into the [vllm/model\_executor/models](https://github.com/vllm-project/vllm/tree/main/vllm/model_executor/models) directory. Then, add your model class to `_VLLM_MODELS` in [vllm/model\_executor/models/registry.py](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/registry.py) so that it is automatically registered upon importing vLLM. Finally, update our [list of supported models](https://docs.vllm.ai/en/latest/models/supported_models/) to promote your model!

Important

The list of models in each section should be maintained in alphabetical order.

## Out-of-tree models[¶](#out-of-tree-models "Permanent link")

You can load an external model [using a plugin](https://docs.vllm.ai/en/latest/design/plugin_system/) without modifying the vLLM codebase.

To register the model, use the following code:

```
# The entrypoint of your plugin
defregister():
    fromvllmimport ModelRegistry
    fromyour_codeimport YourModelForCausalLM

    ModelRegistry.register_model("YourModelForCausalLM", YourModelForCausalLM)
```

If your model imports modules that initialize CUDA, consider lazy-importing it to avoid errors like `RuntimeError: Cannot re-initialize CUDA in forked subprocess`:

```
# The entrypoint of your plugin
defregister():
    fromvllmimport ModelRegistry

    ModelRegistry.register_model(
        "YourModelForCausalLM",
        "your_code:YourModelForCausalLM",
    )
```

Important

If your model is a multimodal model, ensure the model class implements the [SupportsMultiModal](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsMultiModal "            SupportsMultiModal") interface. Read more about that [here](https://docs.vllm.ai/en/latest/contributing/model/multimodal/).