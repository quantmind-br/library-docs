---
title: Together AI | liteLLM
url: https://docs.litellm.ai/docs/providers/togetherai
source: sitemap
fetched_at: 2026-01-21T19:50:30.38234247-03:00
rendered_js: false
word_count: 211
summary: This document provides instructions and code examples for integrating Together AI models with LiteLLM, covering authentication, model lists, and custom prompt template configuration.
tags:
    - together-ai
    - litellm
    - python-sdk
    - llm-integration
    - prompt-templates
    - api-configuration
category: reference
---

LiteLLM supports all models on Together AI.

## API Keys[​](#api-keys "Direct link to API Keys")

```
import os 
os.environ["TOGETHERAI_API_KEY"]="your-api-key"
```

## Sample Usage[​](#sample-usage "Direct link to Sample Usage")

```
from litellm import completion 

os.environ["TOGETHERAI_API_KEY"]="your-api-key"

messages =[{"role":"user","content":"Write me a poem about the blue sky"}]

completion(model="together_ai/togethercomputer/Llama-2-7B-32K-Instruct", messages=messages)
```

## Together AI Models[​](#together-ai-models "Direct link to Together AI Models")

liteLLM supports `non-streaming` and `streaming` requests to all models on [https://api.together.xyz/](https://api.together.xyz/)

Example TogetherAI Usage - Note: liteLLM supports all models deployed on TogetherAI

### Llama LLMs - Chat[​](#llama-llms---chat "Direct link to Llama LLMs - Chat")

Model NameFunction CallRequired OS Variablestogethercomputer/llama-2-70b-chat`completion('together_ai/togethercomputer/llama-2-70b-chat', messages)``os.environ['TOGETHERAI_API_KEY']`

### Llama LLMs - Language / Instruct[​](#llama-llms---language--instruct "Direct link to Llama LLMs - Language / Instruct")

Model NameFunction CallRequired OS Variablestogethercomputer/llama-2-70b`completion('together_ai/togethercomputer/llama-2-70b', messages)``os.environ['TOGETHERAI_API_KEY']`togethercomputer/LLaMA-2-7B-32K`completion('together_ai/togethercomputer/LLaMA-2-7B-32K', messages)``os.environ['TOGETHERAI_API_KEY']`togethercomputer/Llama-2-7B-32K-Instruct`completion('together_ai/togethercomputer/Llama-2-7B-32K-Instruct', messages)``os.environ['TOGETHERAI_API_KEY']`togethercomputer/llama-2-7b`completion('together_ai/togethercomputer/llama-2-7b', messages)``os.environ['TOGETHERAI_API_KEY']`

### Falcon LLMs[​](#falcon-llms "Direct link to Falcon LLMs")

Model NameFunction CallRequired OS Variablestogethercomputer/falcon-40b-instruct`completion('together_ai/togethercomputer/falcon-40b-instruct', messages)``os.environ['TOGETHERAI_API_KEY']`togethercomputer/falcon-7b-instruct`completion('together_ai/togethercomputer/falcon-7b-instruct', messages)``os.environ['TOGETHERAI_API_KEY']`

### Alpaca LLMs[​](#alpaca-llms "Direct link to Alpaca LLMs")

Model NameFunction CallRequired OS Variablestogethercomputer/alpaca-7b`completion('together_ai/togethercomputer/alpaca-7b', messages)``os.environ['TOGETHERAI_API_KEY']`

### Other Chat LLMs[​](#other-chat-llms "Direct link to Other Chat LLMs")

Model NameFunction CallRequired OS VariablesHuggingFaceH4/starchat-alpha`completion('together_ai/HuggingFaceH4/starchat-alpha', messages)``os.environ['TOGETHERAI_API_KEY']`

### Code LLMs[​](#code-llms "Direct link to Code LLMs")

Model NameFunction CallRequired OS Variablestogethercomputer/CodeLlama-34b`completion('together_ai/togethercomputer/CodeLlama-34b', messages)``os.environ['TOGETHERAI_API_KEY']`togethercomputer/CodeLlama-34b-Instruct`completion('together_ai/togethercomputer/CodeLlama-34b-Instruct', messages)``os.environ['TOGETHERAI_API_KEY']`togethercomputer/CodeLlama-34b-Python`completion('together_ai/togethercomputer/CodeLlama-34b-Python', messages)``os.environ['TOGETHERAI_API_KEY']`defog/sqlcoder`completion('together_ai/defog/sqlcoder', messages)``os.environ['TOGETHERAI_API_KEY']`NumbersStation/nsql-llama-2-7B`completion('together_ai/NumbersStation/nsql-llama-2-7B', messages)``os.environ['TOGETHERAI_API_KEY']`WizardLM/WizardCoder-15B-V1.0`completion('together_ai/WizardLM/WizardCoder-15B-V1.0', messages)``os.environ['TOGETHERAI_API_KEY']`WizardLM/WizardCoder-Python-34B-V1.0`completion('together_ai/WizardLM/WizardCoder-Python-34B-V1.0', messages)``os.environ['TOGETHERAI_API_KEY']`

### Language LLMs[​](#language-llms "Direct link to Language LLMs")

Model NameFunction CallRequired OS VariablesNousResearch/Nous-Hermes-Llama2-13b`completion('together_ai/NousResearch/Nous-Hermes-Llama2-13b', messages)``os.environ['TOGETHERAI_API_KEY']`Austism/chronos-hermes-13b`completion('together_ai/Austism/chronos-hermes-13b', messages)``os.environ['TOGETHERAI_API_KEY']`upstage/SOLAR-0-70b-16bit`completion('together_ai/upstage/SOLAR-0-70b-16bit', messages)``os.environ['TOGETHERAI_API_KEY']`WizardLM/WizardLM-70B-V1.0`completion('together_ai/WizardLM/WizardLM-70B-V1.0', messages)``os.environ['TOGETHERAI_API_KEY']`

## Prompt Templates[​](#prompt-templates "Direct link to Prompt Templates")

Using a chat model on Together AI with it's own prompt format?

### Using Llama2 Instruct models[​](#using-llama2-instruct-models "Direct link to Using Llama2 Instruct models")

If you're using Together AI's Llama2 variants( `model=togethercomputer/llama-2..-instruct`), LiteLLM can automatically translate between the OpenAI prompt format and the TogetherAI Llama2 one (`[INST]..[/INST]`).

```
from litellm import completion 

# set env variable 
os.environ["TOGETHERAI_API_KEY"]=""

messages =[{"role":"user","content":"Write me a poem about the blue sky"}]

completion(model="together_ai/togethercomputer/Llama-2-7B-32K-Instruct", messages=messages)
```

### Using another model[​](#using-another-model "Direct link to Using another model")

You can create a custom prompt template on LiteLLM (and we [welcome PRs](https://github.com/BerriAI/litellm) to add them to the main repo 🤗)

Let's make one for `OpenAssistant/llama2-70b-oasst-sft-v10`!

The accepted template format is: [Reference](https://huggingface.co/OpenAssistant/llama2-70b-oasst-sft-v10-)

```
"""
<|im_start|>system
{system_message}<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant
"""
```

Let's register our custom prompt template: [Implementation Code](https://github.com/BerriAI/litellm/blob/64f3d3c56ef02ac5544983efc78293de31c1c201/litellm/llms/prompt_templates/factory.py#L77)

```
import litellm 

litellm.register_prompt_template(
	    model="OpenAssistant/llama2-70b-oasst-sft-v10",
	    roles={
"system":{
"pre_message":"[<|im_start|>system",
"post_message":"\n"
},
"user":{
"pre_message":"<|im_start|>user",
"post_message":"\n"
},
"assistant":{
"pre_message":"<|im_start|>assistant",
"post_message":"\n"
}
}
)
```

Let's use it!

```
from litellm import completion 

# set env variable 
os.environ["TOGETHERAI_API_KEY"]=""

messages=[{"role":"user","content":"Write me a poem about the blue sky"}]

completion(model="together_ai/OpenAssistant/llama2-70b-oasst-sft-v10", messages=messages)
```

**Complete Code**

```
import litellm 
from litellm import completion

# set env variable 
os.environ["TOGETHERAI_API_KEY"]=""

litellm.register_prompt_template(
	    model="OpenAssistant/llama2-70b-oasst-sft-v10",
	    roles={
"system":{
"pre_message":"[<|im_start|>system",
"post_message":"\n"
},
"user":{
"pre_message":"<|im_start|>user",
"post_message":"\n"
},
"assistant":{
"pre_message":"<|im_start|>assistant",
"post_message":"\n"
}
}
)

messages=[{"role":"user","content":"Write me a poem about the blue sky"}]

response = completion(model="together_ai/OpenAssistant/llama2-70b-oasst-sft-v10", messages=messages)

print(response)
```

**Output**

```
{
"choices":[
{
"finish_reason":"stop",
"index":0,
"message":{
"content":".\n\nThe sky is a canvas of blue,\nWith clouds that drift and move,",
"role":"assistant",
"logprobs":null
}
}
],
"created":1693941410.482018,
"model":"OpenAssistant/llama2-70b-oasst-sft-v10",
"usage":{
"prompt_tokens":7,
"completion_tokens":16,
"total_tokens":23
},
"litellm_call_id":"f21315db-afd6-4c1e-b43a-0b5682de4b06"
}
```

## Rerank[​](#rerank "Direct link to Rerank")

### Usage[​](#usage "Direct link to Usage")

- LiteLLM SDK Usage
- LiteLLM Proxy Usage

```
from litellm import rerank
import os

os.environ["TOGETHERAI_API_KEY"]="sk-.."

query ="What is the capital of the United States?"
documents =[
"Carson City is the capital city of the American state of Nevada.",
"The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
"Washington, D.C. is the capital of the United States.",
"Capital punishment has existed in the United States since before it was a country.",
]

response = rerank(
    model="together_ai/rerank-english-v3.0",
    query=query,
    documents=documents,
    top_n=3,
)
print(response)
```