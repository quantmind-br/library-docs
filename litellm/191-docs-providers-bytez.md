---
title: Bytez | liteLLM
url: https://docs.litellm.ai/docs/providers/bytez
source: sitemap
fetched_at: 2026-01-21T19:48:36.773469607-03:00
rendered_js: false
word_count: 106
summary: This document provides instructions for integrating LiteLLM with Bytez models, covering SDK and proxy configurations for chat and multi-modal tasks.
tags:
    - litellm
    - bytez
    - multi-modal
    - python-sdk
    - api-integration
    - proxy-configuration
category: guide
---

LiteLLM supports all chat models on [Bytez](https://www.bytez.com)!

That also means multi-modal models are supported 🔥

Tasks supported: `chat`, `image-text-to-text`, `audio-text-to-text`, `video-text-to-text`

## Usage[​](#usage "Direct link to Usage")

- SDK
- PROXY

### API KEYS[​](#api-keys "Direct link to API KEYS")

```
import os
os.environ["BYTEZ_API_KEY"]="YOUR_BYTEZ_KEY_GOES_HERE"
```

### Example Call[​](#example-call "Direct link to Example Call")

```
from litellm import completion
import os
## set ENV variables
os.environ["BYTEZ_API_KEY"]="YOUR_BYTEZ_KEY_GOES_HERE"

response = completion(
    model="bytez/google/gemma-3-4b-it",
    messages =[{"content":"Hello, how are you?","role":"user"}]
)
```

## Automatic Prompt Template Handling[​](#automatic-prompt-template-handling "Direct link to Automatic Prompt Template Handling")

All prompt formatting is handled automatically by our API when you send a messages list to it!

If you wish to use custom formatting, please let us know via either [help@bytez.com](mailto:help@bytez.com) or on our [Discord](https://discord.com/invite/Z723PfCFWf) and we will work to provide it!

## Passing additional params - max\_tokens, temperature[​](#passing-additional-params---max_tokens-temperature "Direct link to Passing additional params - max_tokens, temperature")

See all litellm.completion supported params [here](https://docs.litellm.ai/docs/completion/input)

```
# !pip install litellm
from litellm import completion
import os
## set ENV variables
os.environ["BYTEZ_API_KEY"]="YOUR_BYTEZ_KEY_HERE"

# bytez gemma-3 call
response = completion(
    model="bytez/google/gemma-3-4b-it",
    messages =[{"content":"Hello, how are you?","role":"user"}],
    max_tokens=20,
    temperature=0.5
)
```

**proxy**

```
model_list:
-model_name: gemma-3
litellm_params:
model: bytez/google/gemma-3-4b-it
api_key: os.environ/BYTEZ_API_KEY
max_tokens:20
temperature:0.5
```

## Passing Bytez-specific params[​](#passing-bytez-specific-params "Direct link to Passing Bytez-specific params")

Any kwarg supported by huggingface we also support! (Provided the model supports it.)

Example `repetition_penalty`

```
# !pip install litellm
from litellm import completion
import os
## set ENV variables
os.environ["BYTEZ_API_KEY"]="YOUR_BYTEZ_KEY_HERE"

# bytez llama3 call with additional params
response = completion(
    model="bytez/google/gemma-3-4b-it",
    messages =[{"content":"Hello, how are you?","role":"user"}],
    repetition_penalty=1.2,
)
```

**proxy**

```
model_list:
-model_name: gemma-3
litellm_params:
model: bytez/google/gemma-3-4b-it
api_key: os.environ/BYTEZ_API_KEY
repetition_penalty:1.2
```