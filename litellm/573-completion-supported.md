---
title: Generation/Completion/Chat Completion Models | liteLLM
url: https://docs.litellm.ai/completion/supported
source: sitemap
fetched_at: 2026-01-21T19:41:05.113898652-03:00
rendered_js: false
word_count: 281
summary: This document outlines the supported AI models and providers for the liteLLM library, detailing the specific function calls and environment variables required for integration.
tags:
    - llm-providers
    - litellm
    - api-configuration
    - openai
    - azure-openai
    - anthropic
    - environment-variables
category: reference
---

### OpenAI Chat Completion Models[​](#openai-chat-completion-models "Direct link to OpenAI Chat Completion Models")

Model NameFunction CallRequired OS Variablesgpt-3.5-turbo`completion('gpt-3.5-turbo', messages)``os.environ['OPENAI_API_KEY']`gpt-3.5-turbo-16k`completion('gpt-3.5-turbo-16k', messages)``os.environ['OPENAI_API_KEY']`gpt-3.5-turbo-16k-0613`completion('gpt-3.5-turbo-16k-0613', messages)``os.environ['OPENAI_API_KEY']`gpt-4`completion('gpt-4', messages)``os.environ['OPENAI_API_KEY']`gpt-5-pro`completion('gpt-5-pro', messages)``os.environ['OPENAI_API_KEY']`

## Azure OpenAI Chat Completion Models[​](#azure-openai-chat-completion-models "Direct link to Azure OpenAI Chat Completion Models")

For Azure calls add the `azure/` prefix to `model`. If your azure deployment name is `gpt-v-2` set `model` = `azure/gpt-v-2`

Model NameFunction CallRequired OS Variablesgpt-3.5-turbo`completion('azure/gpt-3.5-turbo-deployment', messages)``os.environ['AZURE_API_KEY']`,`os.environ['AZURE_API_BASE']`,`os.environ['AZURE_API_VERSION']`gpt-4`completion('azure/gpt-4-deployment', messages)``os.environ['AZURE_API_KEY']`,`os.environ['AZURE_API_BASE']`,`os.environ['AZURE_API_VERSION']`

### OpenAI Text Completion Models[​](#openai-text-completion-models "Direct link to OpenAI Text Completion Models")

Model NameFunction CallRequired OS Variablestext-davinci-003`completion('text-davinci-003', messages)``os.environ['OPENAI_API_KEY']`

### Cohere Models[​](#cohere-models "Direct link to Cohere Models")

Model NameFunction CallRequired OS Variablescommand-nightly`completion('command-nightly', messages)``os.environ['COHERE_API_KEY']`

### Anthropic Models[​](#anthropic-models "Direct link to Anthropic Models")

Model NameFunction CallRequired OS Variablesclaude-instant-1`completion('claude-instant-1', messages)``os.environ['ANTHROPIC_API_KEY']`claude-2`completion('claude-2', messages)``os.environ['ANTHROPIC_API_KEY']`

### Hugging Face Inference API[​](#hugging-face-inference-api "Direct link to Hugging Face Inference API")

All [`text2text-generation`](https://huggingface.co/models?library=transformers&pipeline_tag=text2text-generation&sort=downloads) and [`text-generation`](https://huggingface.co/models?library=transformers&pipeline_tag=text-generation&sort=downloads) models are supported by liteLLM. You can use any text model from Hugging Face with the following steps:

- Copy the `model repo` URL from Hugging Face and set it as the `model` parameter in the completion call.
- Set `hugging_face` parameter to `True`.
- Make sure to set the hugging face API key

Here are some examples of supported models: **Note that the models mentioned in the table are examples, and you can use any text model available on Hugging Face by following the steps above.**

Model NameFunction CallRequired OS Variables[stabilityai/stablecode-completion-alpha-3b-4k](https://huggingface.co/stabilityai/stablecode-completion-alpha-3b-4k)`completion(model="stabilityai/stablecode-completion-alpha-3b-4k", messages=messages, hugging_face=True)``os.environ['HF_TOKEN']`[bigcode/starcoder](https://huggingface.co/bigcode/starcoder)`completion(model="bigcode/starcoder", messages=messages, hugging_face=True)``os.environ['HF_TOKEN']`[google/flan-t5-xxl](https://huggingface.co/google/flan-t5-xxl)`completion(model="google/flan-t5-xxl", messages=messages, hugging_face=True)``os.environ['HF_TOKEN']`[google/flan-t5-large](https://huggingface.co/google/flan-t5-large)`completion(model="google/flan-t5-large", messages=messages, hugging_face=True)``os.environ['HF_TOKEN']`

### OpenRouter Completion Models[​](#openrouter-completion-models "Direct link to OpenRouter Completion Models")

All the text models from [OpenRouter](https://openrouter.ai/docs) are supported by liteLLM.

Model NameFunction CallRequired OS Variablesopenai/gpt-3.5-turbo`completion('openai/gpt-3.5-turbo', messages)``os.environ['OR_SITE_URL']`,`os.environ['OR_APP_NAME']`,`os.environ['OR_API_KEY']`openai/gpt-3.5-turbo-16k`completion('openai/gpt-3.5-turbo-16k', messages)``os.environ['OR_SITE_URL']`,`os.environ['OR_APP_NAME']`,`os.environ['OR_API_KEY']`openai/gpt-4`completion('openai/gpt-4', messages)``os.environ['OR_SITE_URL']`,`os.environ['OR_APP_NAME']`,`os.environ['OR_API_KEY']`openai/gpt-4-32k`completion('openai/gpt-4-32k', messages)``os.environ['OR_SITE_URL']`,`os.environ['OR_APP_NAME']`,`os.environ['OR_API_KEY']`anthropic/claude-2`completion('anthropic/claude-2', messages)``os.environ['OR_SITE_URL']`,`os.environ['OR_APP_NAME']`,`os.environ['OR_API_KEY']`anthropic/claude-instant-v1`completion('anthropic/claude-instant-v1', messages)``os.environ['OR_SITE_URL']`,`os.environ['OR_APP_NAME']`,`os.environ['OR_API_KEY']`google/palm-2-chat-bison`completion('google/palm-2-chat-bison', messages)``os.environ['OR_SITE_URL']`,`os.environ['OR_APP_NAME']`,`os.environ['OR_API_KEY']`google/palm-2-codechat-bison`completion('google/palm-2-codechat-bison', messages)``os.environ['OR_SITE_URL']`,`os.environ['OR_APP_NAME']`,`os.environ['OR_API_KEY']`meta-llama/llama-2-13b-chat`completion('meta-llama/llama-2-13b-chat', messages)``os.environ['OR_SITE_URL']`,`os.environ['OR_APP_NAME']`,`os.environ['OR_API_KEY']`meta-llama/llama-2-70b-chat`completion('meta-llama/llama-2-70b-chat', messages)``os.environ['OR_SITE_URL']`,`os.environ['OR_APP_NAME']`,`os.environ['OR_API_KEY']`

## Novita AI Completion Models[​](#novita-ai-completion-models "Direct link to Novita AI Completion Models")

🚨 LiteLLM supports ALL Novita AI models, send `model=novita/<your-novita-model>` to send it to Novita AI. See all Novita AI models [here](https://novita.ai/models/llm?utm_source=github_litellm&utm_medium=github_readme&utm_campaign=github_link)

Model NameFunction CallRequired OS Variablesnovita/deepseek/deepseek-r1`completion('novita/deepseek/deepseek-r1', messages)``os.environ['NOVITA_API_KEY']`novita/deepseek/deepseek\_v3`completion('novita/deepseek/deepseek_v3', messages)``os.environ['NOVITA_API_KEY']`novita/meta-llama/llama-3.3-70b-instruct`completion('novita/meta-llama/llama-3.3-70b-instruct', messages)``os.environ['NOVITA_API_KEY']`novita/meta-llama/llama-3.1-8b-instruct`completion('novita/meta-llama/llama-3.1-8b-instruct', messages)``os.environ['NOVITA_API_KEY']`novita/meta-llama/llama-3.1-8b-instruct-max`completion('novita/meta-llama/llama-3.1-8b-instruct-max', messages)``os.environ['NOVITA_API_KEY']`novita/meta-llama/llama-3.1-70b-instruct`completion('novita/meta-llama/llama-3.1-70b-instruct', messages)``os.environ['NOVITA_API_KEY']`novita/meta-llama/llama-3-8b-instruct`completion('novita/meta-llama/llama-3-8b-instruct', messages)``os.environ['NOVITA_API_KEY']`novita/meta-llama/llama-3-70b-instruct`completion('novita/meta-llama/llama-3-70b-instruct', messages)``os.environ['NOVITA_API_KEY']`novita/meta-llama/llama-3.2-1b-instruct`completion('novita/meta-llama/llama-3.2-1b-instruct', messages)``os.environ['NOVITA_API_KEY']`novita/meta-llama/llama-3.2-11b-vision-instruct`completion('novita/meta-llama/llama-3.2-11b-vision-instruct', messages)``os.environ['NOVITA_API_KEY']`novita/meta-llama/llama-3.2-3b-instruct`completion('novita/meta-llama/llama-3.2-3b-instruct', messages)``os.environ['NOVITA_API_KEY']`novita/gryphe/mythomax-l2-13b`completion('novita/gryphe/mythomax-l2-13b', messages)``os.environ['NOVITA_API_KEY']`novita/google/gemma-2-9b-it`completion('novita/google/gemma-2-9b-it', messages)``os.environ['NOVITA_API_KEY']`novita/mistralai/mistral-nemo`completion('novita/mistralai/mistral-nemo', messages)``os.environ['NOVITA_API_KEY']`novita/mistralai/mistral-7b-instruct`completion('novita/mistralai/mistral-7b-instruct', messages)``os.environ['NOVITA_API_KEY']`novita/qwen/qwen-2.5-72b-instruct`completion('novita/qwen/qwen-2.5-72b-instruct', messages)``os.environ['NOVITA_API_KEY']`novita/qwen/qwen-2-vl-72b-instruct`completion('novita/qwen/qwen-2-vl-72b-instruct', messages)``os.environ['NOVITA_API_KEY']`

- [OpenAI Chat Completion Models](#openai-chat-completion-models)
- [Azure OpenAI Chat Completion Models](#azure-openai-chat-completion-models)
  
  - [OpenAI Text Completion Models](#openai-text-completion-models)
  - [Cohere Models](#cohere-models)
  - [Anthropic Models](#anthropic-models)
  - [Hugging Face Inference API](#hugging-face-inference-api)
  - [OpenRouter Completion Models](#openrouter-completion-models)
- [Novita AI Completion Models](#novita-ai-completion-models)