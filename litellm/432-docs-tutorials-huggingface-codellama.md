---
title: CodeLlama - Code Infilling | liteLLM
url: https://docs.litellm.ai/docs/tutorials/huggingface_codellama
source: sitemap
fetched_at: 2026-01-21T19:55:28.008405717-03:00
rendered_js: false
word_count: 75
summary: This tutorial explains how to use LiteLLM to perform code infilling tasks with CodeLlama models hosted on Hugging Face Inference Endpoints.
tags:
    - code-infilling
    - litellm
    - codellama
    - hugging-face-inference
    - python
    - code-generation
category: tutorial
---

This tutorial shows how you can call CodeLlama (hosted on Huggingface PRO Inference Endpoints), to fill code.

This is a specialized task particular to code models. The model is trained to generate the code (including comments) that best matches an existing prefix and suffix.

This task is available in the base and instruction variants of the **7B** and **13B** CodeLlama models. It is not available for any of the 34B models or the Python versions.

```
import os
from litellm import longer_context_model_fallback_dict, ContextWindowExceededError, completion

os.environ["HUGGINGFACE_API_KEY"]="your-hf-token"# https://huggingface.co/docs/hub/security-tokens

## CREATE THE PROMPT
prompt_prefix ='def remove_non_ascii(s: str) -> str:\n    """ '
prompt_suffix ="\n    return result"

### set <pre> <suf> to indicate the string before and after the part you want codellama to fill 
prompt =f"<PRE> {prompt_prefix} <SUF>{prompt_suffix} <MID>"

messages =[{"content": prompt,"role":"user"}]
model ="huggingface/codellama/CodeLlama-34b-Instruct-hf"# specify huggingface as the provider 'huggingface/'
response = completion(model=model, messages=messages, max_tokens=500)
```