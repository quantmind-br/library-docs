---
title: Outlines - Pydantic AI
url: https://ai.pydantic.dev/models/outlines/
source: sitemap
fetched_at: 2026-01-22T22:26:19.580568379-03:00
rendered_js: false
word_count: 429
summary: This document explains how to install, initialize, and run Outlines models within the Pydantic AI framework, focusing on structured output and multimodal capabilities.
tags:
    - pydantic-ai
    - outlines
    - structured-output
    - multimodal
    - installation
    - llm-integration
category: guide
---

## Install

As Outlines is a library allowing you to run models from various different providers, it does not include the necessary dependencies for any provider by default. As a result, to use the [`OutlinesModel`](https://ai.pydantic.dev/api/models/outlines/#pydantic_ai.models.outlines.OutlinesModel "OutlinesModel            dataclass   "), you must install `pydantic-ai-slim` with an optional group composed of outlines, a dash, and the name of the specific model provider you would use through Outlines. For instance:

pipuv

```
pipinstall"pydantic-ai-slim[outlines-transformers]"
```

```
uvadd"pydantic-ai-slim[outlines-transformers]"
```

Or

pipuv

```
pipinstall"pydantic-ai-slim[outlines-mlxlm]"
```

```
uvadd"pydantic-ai-slim[outlines-mlxlm]"
```

There are 5 optional groups for the 5 model providers supported through Outlines:

- `outlines-transformers`
- `outlines-llamacpp`
- `outlines-mlxlm`
- `outlines-sglang`
- `outlines-vllm-offline`

## Model Initialization

As Outlines is not an inference provider, but instead a library allowing you to run both local and API-based models, instantiating the model is a bit different from the other models available on Pydantic AI.

To initialize the `OutlinesModel` through the `__init__` method, the first argument you must provide has to be an `outlines.Model` or an `outlines.AsyncModel` instance.

For instance:

```
importoutlines
fromtransformersimport AutoModelForCausalLM, AutoTokenizer

frompydantic_ai.models.outlinesimport OutlinesModel

outlines_model = outlines.from_transformers(
    AutoModelForCausalLM.from_pretrained('erwanf/gpt2-mini'),
    AutoTokenizer.from_pretrained('erwanf/gpt2-mini')
)
model = OutlinesModel(outlines_model)
```

As you already providing an Outlines model instance, there is no need to provide an `OutlinesProvider` yourself.

### Model Loading Methods

Alternatively, you can use some `OutlinesModel` class methods made to load a specific type of Outlines model directly. To do so, you must provide as arguments the same arguments you would have given to the associated Outlines model loading function (except in the case of SGLang).

There are methods for the 5 Outlines models that are officially supported in the integration into Pydantic AI:

- [`from_transformers`](https://ai.pydantic.dev/api/models/outlines/#pydantic_ai.models.outlines.OutlinesModel.from_transformers "from_transformers            classmethod   ")
- [`from_llamacpp`](https://ai.pydantic.dev/api/models/outlines/#pydantic_ai.models.outlines.OutlinesModel.from_llamacpp "from_llamacpp            classmethod   ")
- [`from_mlxlm`](https://ai.pydantic.dev/api/models/outlines/#pydantic_ai.models.outlines.OutlinesModel.from_mlxlm "from_mlxlm            classmethod   ")
- [`from_sglang`](https://ai.pydantic.dev/api/models/outlines/#pydantic_ai.models.outlines.OutlinesModel.from_sglang "from_sglang            classmethod   ")
- [`from_vllm_offline`](https://ai.pydantic.dev/api/models/outlines/#pydantic_ai.models.outlines.OutlinesModel.from_vllm_offline "from_vllm_offline            classmethod   ")

#### Transformers

```
fromtransformersimport AutoModelForCausalLM, AutoTokenizer

frompydantic_ai.models.outlinesimport OutlinesModel

model = OutlinesModel.from_transformers(
    AutoModelForCausalLM.from_pretrained('microsoft/Phi-3-mini-4k-instruct'),
    AutoTokenizer.from_pretrained('microsoft/Phi-3-mini-4k-instruct')
)
```

#### LlamaCpp

```
fromllama_cppimport Llama

frompydantic_ai.models.outlinesimport OutlinesModel

model = OutlinesModel.from_llamacpp(
    Llama.from_pretrained(
        repo_id='TheBloke/Mistral-7B-Instruct-v0.2-GGUF',
        filename='mistral-7b-instruct-v0.2.Q5_K_M.gguf',
    )
)
```

#### MLXLM

```
frommlx_lmimport load

frompydantic_ai.models.outlinesimport OutlinesModel

model = OutlinesModel.from_mlxlm(
    *load('mlx-community/TinyLlama-1.1B-Chat-v1.0-4bit')
)
```

#### SGLang

```
frompydantic_ai.models.outlinesimport OutlinesModel

model = OutlinesModel.from_sglang(
    'http://localhost:11434',
    'api_key',
    'meta-llama/Llama-3.1-8B'
)
```

#### vLLM Offline

```
fromvllmimport LLM

frompydantic_ai.models.outlinesimport OutlinesModel

model = OutlinesModel.from_vllm_offline(
    LLM('microsoft/Phi-3-mini-4k-instruct')
)
```

## Running the model

Once you have initialized an `OutlinesModel`, you can use it with an Agent as with all other Pydantic AI models.

As Outlines is focused on structured output, this provider supports the `output_type` component through the [`NativeOutput`](https://ai.pydantic.dev/api/output/#pydantic_ai.output.NativeOutput "NativeOutput            dataclass   ") format. There is not need to include information on the required output format in your prompt, instructions based on the `output_type` will be included automatically.

```
frompydanticimport BaseModel
fromtransformersimport AutoModelForCausalLM, AutoTokenizer

frompydantic_aiimport Agent
frompydantic_ai.models.outlinesimport OutlinesModel
frompydantic_ai.settingsimport ModelSettings


classBox(BaseModel):
"""Class representing a box"""
    width: int
    height: int
    depth: int
    units: str

model = OutlinesModel.from_transformers(
    AutoModelForCausalLM.from_pretrained('microsoft/Phi-3-mini-4k-instruct'),
    AutoTokenizer.from_pretrained('microsoft/Phi-3-mini-4k-instruct')
)
agent = Agent(model, output_type=Box)

result = agent.run_sync(
    'Give me the dimensions of a box',
    model_settings=ModelSettings(extra_body={'max_new_tokens': 100})
)
print(result.output) # width=20 height=30 depth=40 units='cm'
```

Outlines does not support tools yet, but support for that feature will be added in the near future.

## Multimodal models

If the model you are running through Outlines and the provider selected supports it, you can include images in your prompts using [`ImageUrl`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ImageUrl "ImageUrl            dataclass   ") or [`BinaryImage`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryImage "BinaryImage"). In that case, the prompt you provide when running the agent should be a list containing a string and one or several images. See the [input documentation](https://ai.pydantic.dev/input/) for details and examples on using assets in model inputs.

This feature is supported in Outlines for the `SGLang` and `Transformers` models. If you want to run a multimodal model through `transformers`, you must provide a processor instead of a tokenizer as the second argument when initializing the model with the `OutlinesModel.from_transformers` method.

```
fromdatetimeimport date
fromtypingimport Literal

importtorch
frompydanticimport BaseModel
fromtransformersimport AutoProcessor, Qwen2VLForConditionalGeneration

frompydantic_aiimport Agent, ModelSettings
frompydantic_ai.messagesimport ImageUrl
frompydantic_ai.models.outlinesimport OutlinesModel

MODEL_NAME = 'Qwen/Qwen2-VL-7B-Instruct'

classItem(BaseModel):
    name: str
    quantity: int | None
    price_per_unit: float | None
    total_price: float | None

classReceiptSummary(BaseModel):
    store_name: str
    store_address: str
    store_number: int | None
    items: list[Item]
    tax: float | None
    total: float | None
    date: date
    payment_method: Literal['cash', 'credit', 'debit', 'check', 'other']

tf_model = Qwen2VLForConditionalGeneration.from_pretrained(
    MODEL_NAME,
    device_map='auto',
    dtype=torch.bfloat16
)
tf_processor = AutoProcessor.from_pretrained(
    MODEL_NAME,
    device_map='auto'
)
model = OutlinesModel.from_transformers(tf_model, tf_processor)

agent = Agent(model, output_type=ReceiptSummary)

result = agent.run_sync(
    [
        'You are an expert at extracting information from receipts. Please extract the information from the receipt. Be as detailed as possible, do not miss any information',
        ImageUrl('https://raw.githubusercontent.com/dottxt-ai/outlines/refs/heads/main/docs/examples/images/trader-joes-receipt.jpg')
    ],
    model_settings=ModelSettings(extra_body={'max_new_tokens': 1000})
)
print(result.output)
# store_name="Trader Joe's"
# store_address='401 Bay Street, San Francisco, CA 94133'
# store_number=0
# items=[
#   Item(name='BANANA EACH', quantity=7, price_per_unit=0.23, total_price=1.61),
#   Item(name='BAREBELLS CHOCOLATE DOUG',quantity=1, price_per_unit=2.29, total_price=2.29),
#   Item(name='BAREBELLS CREAMY CRISP', quantity=1, price_per_unit=2.29, total_price=2.29),
#   Item(name='BAREBELLS CHOCOLATE DOUG', quantity=1, price_per_unit=2.29, total_price=2.29),
#   Item(name='BAREBELLS CARAMEL CASHEW', quantity=2, price_per_unit=2.29, total_price=4.58),
#   Item(name='BAREBELLS CREAMY CRISP', quantity=1, price_per_unit=2.29, total_price=2.29),
#   Item(name='T SPINDRIFT ORANGE MANGO 8', quantity=1, price_per_unit=7.49, total_price=7.49),
#   Item(name='T Bottle Deposit', quantity=8, price_per_unit=0.05, total_price=0.4),
#   Item(name='MILK ORGANIC GALLON WHOL', quantity=1, price_per_unit=6.79, total_price=6.79),
#   Item(name='CLASSIC GREEK SALAD', quantity=1, price_per_unit=3.49, total_price=3.49),
#   Item(name='COBB SALAD', quantity=1, price_per_unit=5.99, total_price=5.99),
#   Item(name='PEPPER BELL RED XL EACH', quantity=1, price_per_unit=1.29, total_price=1.29),
#   Item(name='BAG FEE.', quantity=1, price_per_unit=0.25, total_price=0.25),
#   Item(name='BAG FEE.', quantity=1, price_per_unit=0.25, total_price=0.25)]
# tax=7.89
# total=41.98
# date='2023-04-01'
# payment_method='credit'
```