---
title: Quickstart
url: https://docs.ollama.com/quickstart.md
source: llms
fetched_at: 2026-02-04T11:35:03.11885242-03:00
rendered_js: false
word_count: 167
summary: This document provides a quickstart guide for installing Ollama and running large language models using the CLI, cURL, Python, and JavaScript. It also details how to configure coding integrations and use specialized models for development tasks.
tags:
    - ollama-setup
    - model-execution
    - cli
    - python-library
    - javascript-library
    - ai-coding
    - api-integration
category: tutorial
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ollama.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart

This quickstart will walk your through running your first model with Ollama. To get started, download Ollama on macOS, Windows or Linux.

<a href="https://ollama.com/download" target="_blank" className="inline-block px-6 py-2 bg-black rounded-full dark:bg-neutral-700 text-white font-normal border-none">
  Download Ollama
</a>

## Run a model

<Tabs>
  <Tab title="CLI">
    Open a terminal and run the command:

    ```sh  theme={"system"}
    ollama run gemma3
    ```
  </Tab>

  <Tab title="cURL">
    ```sh  theme={"system"}
    ollama pull gemma3
    ```

    Lastly, chat with the model:

    ```shell  theme={"system"}
    curl http://localhost:11434/api/chat -d '{
      "model": "gemma3",
      "messages": [{
        "role": "user",
        "content": "Hello there!"
      }],
      "stream": false
    }'
    ```
  </Tab>

  <Tab title="Python">
    Start by downloading a model:

    ```sh  theme={"system"}
    ollama pull gemma3
    ```

    Then install Ollama's Python library:

    ```sh  theme={"system"}
    pip install ollama
    ```

    Lastly, chat with the model:

    ```python  theme={"system"}
    from ollama import chat
    from ollama import ChatResponse

    response: ChatResponse = chat(model='gemma3', messages=[
      {
        'role': 'user',
        'content': 'Why is the sky blue?',
      },
    ])
    print(response['message']['content'])
    # or access fields directly from the response object
    print(response.message.content)
    ```
  </Tab>

  <Tab title="JavaScript">
    Start by downloading a model:

    ```
    ollama pull gemma3
    ```

    Then install the Ollama JavaScript library:

    ```
    npm i ollama
    ```

    Lastly, chat with the model:

    ```shell  theme={"system"}
    import ollama from 'ollama'

    const response = await ollama.chat({
      model: 'gemma3',
      messages: [{ role: 'user', content: 'Why is the sky blue?' }],
    })
    console.log(response.message.content)
    ```
  </Tab>
</Tabs>

See a full list of available models [here](https://ollama.com/models).

## Coding

For coding use cases, we recommend using the `glm-4.7-flash` model.

Note: this model requires 23 GB of VRAM with 64000 tokens context length.

```sh  theme={"system"}
ollama pull glm-4.7-flash 
```

Alternatively, you can use a more powerful cloud model (with full context length):

```sh  theme={"system"}
ollama pull glm-4.7:cloud
```

Use `ollama launch` to quickly set up a coding tool with Ollama models:

```sh  theme={"system"}
ollama launch
```

### Supported integrations

* [OpenCode](/integrations/opencode) - Open-source coding assistant
* [Claude Code](/integrations/claude-code) - Anthropic's agentic coding tool
* [Codex](/integrations/codex) - OpenAI's coding assistant
* [Droid](/integrations/droid) - Factory's AI coding agent

### Launch with a specific model

```sh  theme={"system"}
ollama launch claude --model glm-4.7-flash
```

### Configure without launching

```sh  theme={"system"}
ollama launch claude --config
```