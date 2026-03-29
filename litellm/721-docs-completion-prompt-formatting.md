---
title: Prompt Formatting | liteLLM
url: https://docs.litellm.ai/docs/completion/prompt_formatting
source: sitemap
fetched_at: 2026-01-21T19:44:40.998264883-03:00
rendered_js: false
word_count: 124
summary: This document explains how LiteLLM handles prompt template translation between models and provides instructions for registering custom prompt templates manually.
tags:
    - litellm
    - prompt-templating
    - huggingface
    - llm-integration
    - custom-configurations
category: guide
---

LiteLLM automatically translates the OpenAI ChatCompletions prompt format, to other models. You can control this by setting a custom prompt template for a model as well.

LiteLLM supports [Huggingface Chat Templates](https://huggingface.co/docs/transformers/main/chat_templating), and will automatically check if your huggingface model has a registered chat template (e.g. [Mistral-7b](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1/blob/main/tokenizer_config.json#L32)).

For popular models (e.g. meta-llama/llama2), we have their templates saved as part of the package.

You can also format the prompt yourself. Here's how:

```
import litellm
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

deftest_huggingface_custom_model():
    model ="huggingface/togethercomputer/LLaMA-2-7B-32K"
    response = completion(model=model, messages=messages, api_base="https://my-huggingface-endpoint")
print(response['choices'][0]['message']['content'])
return response

test_huggingface_custom_model()
```

This is currently supported for Huggingface, TogetherAI, Ollama, and Petals.

Other providers either have fixed prompt templates (e.g. Anthropic), or format it themselves (e.g. Replicate). If there's a provider we're missing coverage for, let us know!

Here's the code for how we format all providers. Let us know how we can improve this further