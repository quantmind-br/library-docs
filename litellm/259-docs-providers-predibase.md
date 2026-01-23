---
title: Predibase | liteLLM
url: https://docs.litellm.ai/docs/providers/predibase
source: sitemap
fetched_at: 2026-01-21T19:50:09.680933142-03:00
rendered_js: false
word_count: 85
summary: This document provides instructions for integrating Predibase models with LiteLLM, covering setup for both SDK and proxy configurations. It explains how to handle authentication, apply custom prompt templates, and pass provider-specific parameters such as adapter IDs.
tags:
    - litellm
    - predibase
    - llm-integration
    - api-configuration
    - prompt-templates
    - python-sdk
    - model-deployment
category: guide
---

LiteLLM supports all models on Predibase

## Usage[​](#usage "Direct link to Usage")

- SDK
- PROXY

### API KEYS[​](#api-keys "Direct link to API KEYS")

```
import os 
os.environ["PREDIBASE_API_KEY"]=""
```

### Example Call[​](#example-call "Direct link to Example Call")

```
from litellm import completion
import os
## set ENV variables
os.environ["PREDIBASE_API_KEY"]="predibase key"
os.environ["PREDIBASE_TENANT_ID"]="predibase tenant id"

# predibase llama-3 call
response = completion(
    model="predibase/llama-3-8b-instruct",
    messages =[{"content":"Hello, how are you?","role":"user"}]
)
```

## Advanced Usage - Prompt Formatting[​](#advanced-usage---prompt-formatting "Direct link to Advanced Usage - Prompt Formatting")

LiteLLM has prompt template mappings for all `meta-llama` llama3 instruct models. [**See Code**](https://github.com/BerriAI/litellm/blob/4f46b4c3975cd0f72b8c5acb2cb429d23580c18a/litellm/llms/prompt_templates/factory.py#L1360)

To apply a custom prompt template:

- SDK
- PROXY

```
import litellm

import os 
os.environ["PREDIBASE_API_KEY"]=""

# Create your own custom prompt template 
litellm.register_prompt_template(
	    model="togethercomputer/LLaMA-2-7B-32K",
        initial_prompt_value="You are a good assistant"# [OPTIONAL]
	    roles={
"system":{
"pre_message":"[INST] <<SYS>>\n",# [OPTIONAL]
"post_message":"\n<</SYS>>\n [/INST]\n"# [OPTIONAL]
},
"user":{
"pre_message":"[INST] ",# [OPTIONAL]
"post_message":" [/INST]"# [OPTIONAL]
},
"assistant":{
"pre_message":"\n"# [OPTIONAL]
"post_message":"\n"# [OPTIONAL]
}
}
        final_prompt_value="Now answer as best you can:"# [OPTIONAL]
)

defpredibase_custom_model():
    model ="predibase/togethercomputer/LLaMA-2-7B-32K"
    response = completion(model=model, messages=messages)
print(response['choices'][0]['message']['content'])
return response

predibase_custom_model()
```

## Passing additional params - max\_tokens, temperature[​](#passing-additional-params---max_tokens-temperature "Direct link to Passing additional params - max_tokens, temperature")

See all litellm.completion supported params [here](https://docs.litellm.ai/docs/completion/input)

```
# !pip install litellm
from litellm import completion
import os
## set ENV variables
os.environ["PREDIBASE_API_KEY"]="predibase key"

# predibae llama-3 call
response = completion(
    model="predibase/llama3-8b-instruct",
    messages =[{"content":"Hello, how are you?","role":"user"}],
    max_tokens=20,
    temperature=0.5
)
```

**proxy**

```
model_list:
-model_name: llama-3
litellm_params:
model: predibase/llama-3-8b-instruct
api_key: os.environ/PREDIBASE_API_KEY
max_tokens:20
temperature:0.5
```

## Passings Predibase specific params - adapter\_id, adapter\_source,[​](#passings-predibase-specific-params---adapter_id-adapter_source "Direct link to Passings Predibase specific params - adapter_id, adapter_source,")

Send params [not supported by `litellm.completion()`](https://docs.litellm.ai/docs/completion/input) but supported by Predibase by passing them to `litellm.completion`

Example `adapter_id`, `adapter_source` are Predibase specific param - [See List](https://github.com/BerriAI/litellm/blob/8a35354dd6dbf4c2fcefcd6e877b980fcbd68c58/litellm/llms/predibase.py#L54)

```
# !pip install litellm
from litellm import completion
import os
## set ENV variables
os.environ["PREDIBASE_API_KEY"]="predibase key"

# predibase llama3 call
response = completion(
    model="predibase/llama-3-8b-instruct",
    messages =[{"content":"Hello, how are you?","role":"user"}],
    adapter_id="my_repo/3",
    adapter_source="pbase",
)
```

**proxy**

```
model_list:
-model_name: llama-3
litellm_params:
model: predibase/llama-3-8b-instruct
api_key: os.environ/PREDIBASE_API_KEY
adapter_id: my_repo/3
adapter_source: pbase
```