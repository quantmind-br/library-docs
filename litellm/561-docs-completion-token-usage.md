---
title: Completion Token Usage & Cost | liteLLM
url: https://docs.litellm.ai/docs/completion/token_usage
source: sitemap
fetched_at: 2026-01-21T19:44:46.198345294-03:00
rendered_js: false
word_count: 459
summary: This document outlines LiteLLM's helper functions for tokenization, token counting, and cost estimation across various LLM providers.
tags:
    - litellm
    - tokenization
    - cost-tracking
    - token-counter
    - llm-api
    - pricing-management
category: reference
---

By default LiteLLM returns token usage in all completion requests ([See here](https://litellm.readthedocs.io/en/latest/output/))

LiteLLM returns `response_cost` in all calls.

```
from litellm import completion 

response = litellm.completion(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content":"Hey, how's it going?"}],
            mock_response="Hello world",
)

print(response._hidden_params["response_cost"])
```

LiteLLM also exposes some helper functions:

- `encode`: This encodes the text passed in, using the model-specific tokenizer. [**Jump to code**](#1-encode)
- `decode`: This decodes the tokens passed in, using the model-specific tokenizer. [**Jump to code**](#2-decode)
- `token_counter`: This returns the number of tokens for a given input - it uses the tokenizer based on the model, and defaults to tiktoken if no model-specific tokenizer is available. [**Jump to code**](#3-token_counter)
- `create_pretrained_tokenizer` and `create_tokenizer`: LiteLLM provides default tokenizer support for OpenAI, Cohere, Anthropic, Llama2, and Llama3 models. If you are using a different model, you can create a custom tokenizer and pass it as `custom_tokenizer` to the `encode`, `decode`, and `token_counter` methods. [**Jump to code**](#4-create_pretrained_tokenizer-and-create_tokenizer)
- `cost_per_token`: This returns the cost (in USD) for prompt (input) and completion (output) tokens. Uses the live list from `api.litellm.ai`. [**Jump to code**](#5-cost_per_token)
- `completion_cost`: This returns the overall cost (in USD) for a given LLM API Call. It combines `token_counter` and `cost_per_token` to return the cost for that query (counting both cost of input and output). [**Jump to code**](#6-completion_cost)
- `get_max_tokens`: This returns the maximum number of tokens allowed for the given model. [**Jump to code**](#7-get_max_tokens)
- `model_cost`: This returns a dictionary for all models, with their max\_tokens, input\_cost\_per\_token and output\_cost\_per\_token. It uses the `api.litellm.ai` call shown below. [**Jump to code**](#8-model_cost)
- `register_model`: This registers new / overrides existing models (and their pricing details) in the model cost dictionary. [**Jump to code**](#9-register_model)
- `api.litellm.ai`: Live token + price count across [all supported models](https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json). [**Jump to code**](#10-apilitellmai)

📣 [This is a community maintained list](https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json). Contributions are welcome! ❤️

## Example Usage[​](#example-usage "Direct link to Example Usage")

### 1. `encode`[​](#1-encode "Direct link to 1-encode")

Encoding has model-specific tokenizers for anthropic, cohere, llama2 and openai. If an unsupported model is passed in, it'll default to using tiktoken (openai's tokenizer).

```
from litellm import encode, decode

sample_text ="Hellö World, this is my input string!"
# openai encoding + decoding
openai_tokens = encode(model="gpt-3.5-turbo", text=sample_text)
print(openai_tokens)
```

### 2. `decode`[​](#2-decode "Direct link to 2-decode")

Decoding is supported for anthropic, cohere, llama2 and openai.

```
from litellm import encode, decode

sample_text ="Hellö World, this is my input string!"
# openai encoding + decoding
openai_tokens = encode(model="gpt-3.5-turbo", text=sample_text)
openai_text = decode(model="gpt-3.5-turbo", tokens=openai_tokens)
print(openai_text)
```

### 3. `token_counter`[​](#3-token_counter "Direct link to 3-token_counter")

```
from litellm import token_counter

messages =[{"user":"role","content":"Hey, how's it going"}]
print(token_counter(model="gpt-3.5-turbo", messages=messages))
```

### 4. `create_pretrained_tokenizer` and `create_tokenizer`[​](#4-create_pretrained_tokenizer-and-create_tokenizer "Direct link to 4-create_pretrained_tokenizer-and-create_tokenizer")

```
from litellm import create_pretrained_tokenizer, create_tokenizer

# get tokenizer from huggingface repo
custom_tokenizer_1 = create_pretrained_tokenizer("Xenova/llama-3-tokenizer")

# use tokenizer from json file
withopen("tokenizer.json")as f:
    json_data = json.load(f)

json_str = json.dumps(json_data)

custom_tokenizer_2 = create_tokenizer(json_str)
```

### 5. `cost_per_token`[​](#5-cost_per_token "Direct link to 5-cost_per_token")

```
from litellm import cost_per_token

prompt_tokens =5
completion_tokens =10
prompt_tokens_cost_usd_dollar, completion_tokens_cost_usd_dollar = cost_per_token(model="gpt-3.5-turbo", prompt_tokens=prompt_tokens, completion_tokens=completion_tokens)

print(prompt_tokens_cost_usd_dollar, completion_tokens_cost_usd_dollar)
```

### 6. `completion_cost`[​](#6-completion_cost "Direct link to 6-completion_cost")

- Input: Accepts a `litellm.completion()` response **OR** prompt + completion strings
- Output: Returns a `float` of cost for the `completion` call

**litellm.completion()**

```
from litellm import completion, completion_cost

response = completion(
            model="bedrock/anthropic.claude-v2",
            messages=messages,
            request_timeout=200,
)
# pass your response from completion to completion_cost
cost = completion_cost(completion_response=response)
formatted_string =f"${float(cost):.10f}"
print(formatted_string)
```

**prompt + completion string**

```
from litellm import completion_cost
cost = completion_cost(model="bedrock/anthropic.claude-v2", prompt="Hey!", completion="How's it going?")
formatted_string =f"${float(cost):.10f}"
print(formatted_string)
```

### 7. `get_max_tokens`[​](#7-get_max_tokens "Direct link to 7-get_max_tokens")

Input: Accepts a model name - e.g., gpt-3.5-turbo (to get a complete list, call litellm.model\_list). Output: Returns the maximum number of tokens allowed for the given model

```
from litellm import get_max_tokens 

model ="gpt-3.5-turbo"

print(get_max_tokens(model))# Output: 4097
```

### 8. `model_cost`[​](#8-model_cost "Direct link to 8-model_cost")

- Output: Returns a dict object containing the max\_tokens, input\_cost\_per\_token, output\_cost\_per\_token for all models on [community-maintained list](https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json)

```
from litellm import model_cost 

print(model_cost)# {'gpt-3.5-turbo': {'max_tokens': 4000, 'input_cost_per_token': 1.5e-06, 'output_cost_per_token': 2e-06}, ...}
```

### 9. `register_model`[​](#9-register_model "Direct link to 9-register_model")

- Input: Provide EITHER a model cost dictionary or a url to a hosted json blob
- Output: Returns updated model\_cost dictionary + updates litellm.model\_cost with model details.

**Dictionary**

```
import litellm

litellm.register_model({
"gpt-4":{
"max_tokens":8192,
"input_cost_per_token":0.00002,
"output_cost_per_token":0.00006,
"litellm_provider":"openai",
"mode":"chat"
},
})
```

**URL for json blob**

```
import litellm

litellm.register_model(model_cost=
"https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json")
```

**Don't pull hosted model\_cost\_map**  
If you have firewalls, and want to just use the local copy of the model cost map, you can do so like this:

```
export LITELLM_LOCAL_MODEL_COST_MAP="True"
```

Note: this means you will need to upgrade to get updated pricing, and newer models.