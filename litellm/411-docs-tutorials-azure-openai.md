---
title: Replacing OpenAI ChatCompletion with Completion() | liteLLM
url: https://docs.litellm.ai/docs/tutorials/azure_openai
source: sitemap
fetched_at: 2026-01-21T19:55:02.075275253-03:00
rendered_js: false
word_count: 34
summary: This document provides a quick-start guide for implementing chat completions using LiteLLM with OpenAI and Azure OpenAI across various modes including streaming, async, and multi-threading.
tags:
    - litellm
    - openai
    - azure-openai
    - streaming
    - async-completion
    - multi-threading
    - python
category: tutorial
---

- [Supported OpenAI LLMs](https://docs.litellm.ai/docs/providers/openai)
- [Supported Azure OpenAI LLMs](https://docs.litellm.ai/docs/providers/azure)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BerriAI/litellm/blob/main/cookbook/LiteLLM_Azure_and_OpenAI_example.ipynb)

## Completion() - Quick Start[​](#completion---quick-start "Direct link to Completion() - Quick Start")

```
import os 
from litellm import completion

# openai configs
os.environ["OPENAI_API_KEY"]=""

# azure openai configs
os.environ["AZURE_API_KEY"]=""
os.environ["AZURE_API_BASE"]="https://openai-gpt-4-test-v-1.openai.azure.com/"
os.environ["AZURE_API_VERSION"]="2023-05-15"


# openai call
response = completion(
    model ="gpt-3.5-turbo",
    messages =[{"content":"Hello, how are you?","role":"user"}]
)
print("Openai Response\n")
print(response)

# azure call
response = completion(
    model ="azure/<your-azure-deployment>",
    messages =[{"content":"Hello, how are you?","role":"user"}]
)
print("Azure Response\n")
print(response)
```

## Completion() with Streaming[​](#completion-with-streaming "Direct link to Completion() with Streaming")

```
import os 
from litellm import completion

# openai configs
os.environ["OPENAI_API_KEY"]=""

# azure openai configs
os.environ["AZURE_API_KEY"]=""
os.environ["AZURE_API_BASE"]="https://openai-gpt-4-test-v-1.openai.azure.com/"
os.environ["AZURE_API_VERSION"]="2023-05-15"


# openai call
response = completion(
    model ="gpt-3.5-turbo",
    messages =[{"content":"Hello, how are you?","role":"user"}],
    stream=True
)
print("OpenAI Streaming response")
for chunk in response:
print(chunk)

# azure call
response = completion(
    model ="azure/<your-azure-deployment>",
    messages =[{"content":"Hello, how are you?","role":"user"}],
    stream=True
)
print("Azure Streaming response")
for chunk in response:
print(chunk)

```

## Completion() with Streaming + Async[​](#completion-with-streaming--async "Direct link to Completion() with Streaming + Async")

```
import os 
from litellm import acompletion

# openai configs
os.environ["OPENAI_API_KEY"]=""

# azure openai configs
os.environ["AZURE_API_KEY"]=""
os.environ["AZURE_API_BASE"]="https://openai-gpt-4-test-v-1.openai.azure.com/"
os.environ["AZURE_API_VERSION"]="2023-05-15"


# openai call
response = acompletion(
    model ="gpt-3.5-turbo",
    messages =[{"content":"Hello, how are you?","role":"user"}],
    stream=True
)

# azure call
response = acompletion(
    model ="azure/<your-azure-deployment>",
    messages =[{"content":"Hello, how are you?","role":"user"}],
    stream=True
)

```

## Completion() multi-threaded[​](#completion-multi-threaded "Direct link to Completion() multi-threaded")

```
import os
import threading
from litellm import completion

# Function to make a completion call
defmake_completion(model, messages):
    response = completion(
        model=model,
        messages=messages,
        stream=True
)

print(f"Response for {model}: {response}")

# Set your API keys
os.environ["OPENAI_API_KEY"]="YOUR_OPENAI_API_KEY"
os.environ["AZURE_API_KEY"]="YOUR_AZURE_API_KEY"

# Define the messages for the completions
messages =[{"content":"Hello, how are you?","role":"user"}]

# Create threads for making the completions
thread1 = threading.Thread(target=make_completion, args=("gpt-3.5-turbo", messages))
thread2 = threading.Thread(target=make_completion, args=("azure/your-azure-deployment", messages))

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both completions are done.")
```