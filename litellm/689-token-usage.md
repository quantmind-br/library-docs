---
title: Token Usage | liteLLM
url: https://docs.litellm.ai/token_usage
source: sitemap
fetched_at: 2026-01-21T19:43:41.85945764-03:00
rendered_js: false
word_count: 127
summary: This document details LiteLLM's helper functions for calculating token usage and the financial costs associated with LLM API calls across different providers.
tags:
    - litellm
    - token-usage
    - cost-calculation
    - token-counter
    - api-monitoring
    - usage-tracking
category: reference
---

By default LiteLLM returns token usage in all completion requests ([See here](https://litellm.readthedocs.io/en/latest/output/))

However, we also expose 3 public helper functions to calculate token usage across providers:

- `token_counter`: This returns the number of tokens for a given input - it uses the tokenizer based on the model, and defaults to tiktoken if no model-specific tokenizer is available.
- `cost_per_token`: This returns the cost (in USD) for prompt (input) and completion (output) tokens. It utilizes our model\_cost map which can be found in `__init__.py` and also as a [community resource](https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json).
- `completion_cost`: This returns the overall cost (in USD) for a given LLM API Call. It combines `token_counter` and `cost_per_token` to return the cost for that query (counting both cost of input and output).

## Example Usage[​](#example-usage "Direct link to Example Usage")

1. `token_counter`

```
from litellm import token_counter

messages =[{"role":"user","content":"Hey, how's it going"}]
print(token_counter(model="gpt-3.5-turbo", messages=messages))
```

2. `cost_per_token`

```
from litellm import cost_per_token

prompt_tokens =5
completion_tokens =10
prompt_tokens_cost_usd_dollar, completion_tokens_cost_usd_dollar = cost_per_token(model="gpt-3.5-turbo", prompt_tokens=prompt_tokens, completion_tokens=completion_tokens)

print(prompt_tokens_cost_usd_dollar, completion_tokens_cost_usd_dollar)
```

3. `completion_cost`

```
from litellm import completion_cost

prompt ="Hey, how's it going"
completion ="Hi, I'm gpt - I am doing well"
cost_of_query = completion_cost(model="gpt-3.5-turbo", prompt=prompt, completion=completion))

print(cost_of_query)
```

- [Example Usage](#example-usage)