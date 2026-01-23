---
title: Customize Prompt Templates on OpenAI-Compatible server | liteLLM
url: https://docs.litellm.ai/docs/tutorials/model_config_proxy
source: sitemap
fetched_at: 2026-01-21T19:55:38.860479567-03:00
rendered_js: false
word_count: 291
summary: This tutorial explains how to define and implement custom prompt templates for specific models within a LiteLLM OpenAI-compatible server. It covers creating a configuration file to specify start and end tokens for system, user, and assistant messages to ensure correct model formatting.
tags:
    - litellm
    - prompt-templates
    - llm-configuration
    - openai-proxy
    - codellama
    - huggingface-tgi
category: tutorial
---

**You will learn:** How to set a custom prompt template on our OpenAI compatible server. **How?** We will modify the prompt template for CodeLlama

## Step 1: Start OpenAI Compatible server[​](#step-1-start-openai-compatible-server "Direct link to Step 1: Start OpenAI Compatible server")

Let's spin up a local OpenAI-compatible server, to call a deployed `codellama/CodeLlama-34b-Instruct-hf` model using Huggingface's [Text-Generation-Inference (TGI)](https://github.com/huggingface/text-generation-inference) format.

```
$ litellm --model huggingface/codellama/CodeLlama-34b-Instruct-hf --api_base https://my-endpoint.com

# OpenAI compatible server running on http://0.0.0.0/8000
```

In a new shell, run:

This will send a test request to our endpoint.

Now, let's see what got sent to huggingface. Run:

This will return the most recent log (by default logs are stored in a local file called 'api\_logs.json').

As we can see, this is the formatting sent to huggingface:

This follows [our formatting](https://github.com/BerriAI/litellm/blob/9932371f883c55fd0f3142f91d9c40279e8fe241/litellm/llms/prompt_templates/factory.py#L10) for CodeLlama (based on the [Huggingface's documentation](https://huggingface.co/blog/codellama#conversational-instructions)).

But this lacks BOS(`<s>`) and EOS(`</s>`) tokens.

So instead of using the LiteLLM default, let's use our own prompt template to use these in our messages.

## Step 2: Create Custom Prompt Template[​](#step-2-create-custom-prompt-template "Direct link to Step 2: Create Custom Prompt Template")

Our litellm server accepts prompt templates as part of a config file. You can save api keys, fallback models, prompt templates etc. in this config. [See a complete config file](https://docs.litellm.ai/docs/proxy_server)

For now, let's just create a simple config file with our prompt template, and tell our server about it.

Create a file called `litellm_config.toml`:

```
$ touch litellm_config.toml
```

We want to add:

- BOS (`<s>`) tokens at the start of every System and Human message
- EOS (`</s>`) tokens at the end of every assistant message.

Let's open our file in our terminal:

paste our prompt template:

```
[model."huggingface/codellama/CodeLlama-34b-Instruct-hf".prompt_template] 
MODEL_SYSTEM_MESSAGE_START_TOKEN = "<s>[INST]  <<SYS>>\n]" 
MODEL_SYSTEM_MESSAGE_END_TOKEN = "\n<</SYS>>\n [/INST]\n"

MODEL_USER_MESSAGE_START_TOKEN = "<s>[INST] " 
MODEL_USER_MESSAGE_END_TOKEN = " [/INST]\n"

MODEL_ASSISTANT_MESSAGE_START_TOKEN = ""
MODEL_ASSISTANT_MESSAGE_END_TOKEN = "</s>"
```

save our file (in vim):

## Step 3: Run new template[​](#step-3-run-new-template "Direct link to Step 3: Run new template")

Let's save our custom template to our litellm server by running:

```
$ litellm --config -f ./litellm_config.toml 
```

LiteLLM will save a copy of this file in it's package, so it can persist these settings across restarts.

Re-start our server:

```
$ litellm --model huggingface/codellama/CodeLlama-34b-Instruct-hf --api_base https://my-endpoint.com
```

In a new shell, run:

See our new input prompt to Huggingface!

Congratulations 🎉