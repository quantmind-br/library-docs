---
title: Offline / Local | Mistral Docs
url: https://docs.mistral.ai/mistral-vibe/local
source: crawler
fetched_at: 2026-01-29T07:33:14.399607853-03:00
rendered_js: false
word_count: 488
summary: A guide for running Mistral AI models in local environments or offline settings, detailing deployment options and infrastructure requirements.
tags:
    - Mistral AI
    - local deployment
    - offline inference
    - LLM
    - infrastructure
category: guide
---

Vibe supports local models, meaning you can deploy Devstral on your own infrastructure and use it without an internet connection - your own personal coding assistant CLI stack.

We provide weights for some Devstral models that you can use to run a server. As long as the server API is compatible, you can run any model you want. We recommend using [**Devstral Small 2**](https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512) for local usage, as it is an efficient and open-source option. Due to the nature of the models and their use cases, we recommend having a GPU to run Devstral locally. For decent performance with long contexts, we recommend deploying at **FP8 precision** with a context length of around **128k**. You can adjust the context length based on your use case and hardware.

Under these conditions, you will need at least an **H100** or **A100 GPU** to run Devstral locally efficiently. You can also run the model at lower precision and context to reduce requirements. For example, at **4-bits precision** with a **32k context length**, you will need at least an **RTX 4090 GPU** or **24GB of VRAM**.

Alternatively, you can run Devstral by offloading the model to the CPU, though it will be significantly slower - this approach allows you to run Devstral on any machine, provided it has enough RAM.

As long as your server API is compatible with the OpenAI API, you can use any model you want.  
Once the server is running locally on port **8080**, you can quickly switch from the Devstral API to your local server by using `/config` in Vibe and changing the model to **"local"**. By default, Vibe uses port **8080** as the local server.  
For more information on configuring Vibe, please refer to the [configuration page](https://docs.mistral.ai/mistral-vibe/introduction/configuration).

We recommend running Devstral with [**vLLM**](https://github.com/vllm-project/vllm), as it is the most efficient and reliable way to deploy Devstral locally.

To run **Devstral Small 2**, use the following command:

Here, `--port` specifies the port for the server. We recommend using **8080**, as it is the default port for Vibe. Otherwise, you will need to configure Vibe to use the correct port.

Depending on your hardware, you may want to include the following flags:

- `--tensor-parallel-size`: To use multiple GPUs
- `--dtype`: To use a lower precision
- `--max-model-len`: To reduce the context length

Once the server is up and running, you can use Vibe to interact with your local model by typing `/config` and selecting the **"local"** model.

Once it's running, we recommend creating a specific preset for your local model. This way, you can easily switch between your local model and the Mistral AI API, or even have different models and providers for different use cases.

To learn how to create a preset or change providers and models, please refer to the [Change Providers and Models](https://docs.mistral.ai/mistral-vibe/introduction/configuration#change-providers) configuration section.

As mentionned preeviously, you can run Devstral anywhere you want. Below is a list of inference frameworks you can explore to deploy Devstral locally: