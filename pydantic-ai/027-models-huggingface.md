---
title: Hugging Face - Pydantic AI
url: https://ai.pydantic.dev/models/huggingface/
source: sitemap
fetched_at: 2026-01-22T22:26:14.088480276-03:00
rendered_js: false
word_count: 245
summary: This document explains how to integrate Hugging Face models with PydanticAI, covering installation, authentication, and advanced provider configuration.
tags:
    - pydantic-ai
    - hugging-face
    - llm-integration
    - inference-providers
    - python-library
    - model-hosting
category: guide
---

[Hugging Face](https://huggingface.co/) is an AI platform with all major open source models, datasets, MCPs, and demos. You can use [Inference Providers](https://huggingface.co/docs/inference-providers) to run open source models like DeepSeek R1 on scalable serverless infrastructure.

## Install

To use `HuggingFaceModel`, you need to either install `pydantic-ai`, or install `pydantic-ai-slim` with the `huggingface` optional group:

pipuv

```
pipinstall"pydantic-ai-slim[huggingface]"
```

```
uvadd"pydantic-ai-slim[huggingface]"
```

## Configuration

To use [Hugging Face](https://huggingface.co/) inference, you'll need to set up an account which will give you [free tier](https://huggingface.co/docs/inference-providers/pricing) allowance on [Inference Providers](https://huggingface.co/docs/inference-providers). To setup inference, follow these steps:

1. Go to [Hugging Face](https://huggingface.co/join) and sign up for an account.
2. Create a new access token in [Hugging Face](https://huggingface.co/settings/tokens).
3. Set the `HF_TOKEN` environment variable to the token you just created.

Once you have a Hugging Face access token, you can set it as an environment variable:

```
exportHF_TOKEN='hf_token'
```

## Usage

You can then use [`HuggingFaceModel`](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface.HuggingFaceModel "HuggingFaceModel            dataclass   ") by name:

```
frompydantic_aiimport Agent

agent = Agent('huggingface:Qwen/Qwen3-235B-A22B')
...
```

Or initialise the model directly with just the model name:

```
frompydantic_aiimport Agent
frompydantic_ai.models.huggingfaceimport HuggingFaceModel

model = HuggingFaceModel('Qwen/Qwen3-235B-A22B')
agent = Agent(model)
...
```

By default, the [`HuggingFaceModel`](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface.HuggingFaceModel "HuggingFaceModel            dataclass   ") uses the [`HuggingFaceProvider`](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.huggingface.HuggingFaceProvider) that will select automatically the first of the inference providers (Cerebras, Together AI, Cohere..etc) available for the model, sorted by your preferred order in https://hf.co/settings/inference-providers.

## Configure the provider

If you want to pass parameters in code to the provider, you can programmatically instantiate the [`HuggingFaceProvider`](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.huggingface.HuggingFaceProvider) and pass it to the model:

```
frompydantic_aiimport Agent
frompydantic_ai.models.huggingfaceimport HuggingFaceModel
frompydantic_ai.providers.huggingfaceimport HuggingFaceProvider

model = HuggingFaceModel('Qwen/Qwen3-235B-A22B', provider=HuggingFaceProvider(api_key='hf_token', provider_name='nebius'))
agent = Agent(model)
...
```

## Custom Hugging Face client

[`HuggingFaceProvider`](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.huggingface.HuggingFaceProvider) also accepts a custom [`AsyncInferenceClient`](https://huggingface.co/docs/huggingface_hub/v0.29.3/en/package_reference/inference_client#huggingface_hub.AsyncInferenceClient) client via the `hf_client` parameter, so you can customise the `headers`, `bill_to` (billing to an HF organization you're a member of), `base_url` etc. as defined in the [Hugging Face Hub python library docs](https://huggingface.co/docs/huggingface_hub/package_reference/inference_client).

```
fromhuggingface_hubimport AsyncInferenceClient

frompydantic_aiimport Agent
frompydantic_ai.models.huggingfaceimport HuggingFaceModel
frompydantic_ai.providers.huggingfaceimport HuggingFaceProvider

client = AsyncInferenceClient(
    bill_to='openai',
    api_key='hf_token',
    provider='fireworks-ai',
)

model = HuggingFaceModel(
    'Qwen/Qwen3-235B-A22B',
    provider=HuggingFaceProvider(hf_client=client),
)
agent = Agent(model)
...
```