---
title: Codestral with code interpreting and analyzing dataset - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-e2b_code_interpreting-codestral-code-interpreter-python-codestral_code_interpreter
source: crawler
fetched_at: 2026-01-29T07:34:05.308270754-03:00
rendered_js: false
word_count: 303
summary: This document provides a step-by-step tutorial on integrating Mistral's Codestral model with the E2B Code Interpreter SDK to build an AI assistant capable of executing Python code in a secure sandbox.
tags:
    - mistral-ai
    - codestral
    - e2b-sdk
    - code-interpreter
    - python-sdk
    - llm-tools
    - sandboxed-execution
category: tutorial
---

This AI assistant is powered by the open-source [Code Interpreter SDK](https://github.com/e2b-dev/code-interpreter) by [E2B](https://e2b.dev/docs). The SDK quickly creates a secure cloud sandbox powered by [Firecracker](https://github.com/firecracker-microvm/firecracker). Inside this sandbox is a running Jupyter server that the LLM can use.

Read more about Mistral's new Codestral model [here](https://mistral.ai/news/codestral/).

### Step 1: Install dependencies

We start with installing the [E2B code interpreter SDK](https://github.com/e2b-dev/code-interpreter) and [Mistral's Python SDK](https://console.mistral.ai/).

### Step 2: Define API keys and prompt

Let's define our variables with API keys for Mistral and E2B together with the model ID and prompt.

We won't be defining any tools, because this example is made to work universally, including Mistral's models that don't fully support tool usage (function calling) yet. To learn more about function calling with Mistral's LLMs, see [this docs page](https://docs.mistral.ai/capabilities/function_calling/).

We instruct the model to return messages in Markdown and then parse and extract the Python code block.

### Step 3: Implement the method for code interpreting

Here's the main function that uses the E2B code interpreter SDK. We'll be calling this function a little bit further in the code when we're parsing the Codestral's response with tool calls.

### Step 4: Implement the method for calling Codestral and parsing its response

Now we're going to define and implement `chat` method. In this method, we'll call the Codestral LLM, parse the output to extract any Python code block, and call our `code_interpret` method we defined above.

### Step 5: Implement the method for uploading dataset to code interpreter sandbox

The file gets uploaded to the E2B sandbox where our code interpreter is running. We get the file's remote path in the `remote_path` variable.

### Step 6: Put everything together

In this last step, we put all the pieces together. We instantiate a new code interpreter instance using

and then call the `chat` method with our user message and the `code_interpreter` instance.