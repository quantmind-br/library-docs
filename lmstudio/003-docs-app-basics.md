---
title: Get started with LM Studio
url: https://lmstudio.ai/docs/app/basics
source: sitemap
fetched_at: 2026-04-07T21:27:40.881517814-03:00
rendered_js: false
word_count: 258
summary: This document provides a step-by-step guide on setting up and using a locally run Large Language Model (LLM) with LM Studio. It covers initial setup, downloading the model weights, loading the model into memory, and finally starting a chat session.
tags:
    - lm-studio
    - llm-setup
    - local-model
    - downloading-models
    - using-chat
category: tutorial
---

Double check computer meets the minimum [system requirements](https://lmstudio.ai/docs/system-requirements).

You might sometimes see terms such as `open-source models` or `open-weights models`. Different models might be released under different licenses and varying degrees of 'openness'. In order to run a model locally, you need to be able to get access to its "weights", often distributed as one or more files that end with `.gguf`, `.safetensors` etc.

* * *

## Getting up and running[](#getting-up-and-running "Link to 'Getting up and running'")

First, **install the latest version of LM Studio**. You can get it from [here](https://lmstudio.ai/download).

Once you're all set up, you need to **download your first LLM**.

### 1. Download an LLM to your computer[](#1-download-an-llm-to-your-computer)

Head over to the Discover tab to download models. Pick one of the curated options or search for models by search query (e.g. `"Llama"`). See more in-depth information about downloading models [here](https://lmstudio.ai/docs/basics/download-models).

![undefined](https://lmstudio.ai/assets/docs/discover.png)

The Discover tab in LM Studio

### 2. Load a model to memory[](#2-load-a-model-to-memory)

Head over to the **Chat** tab, and

- Open the model loader
- Select one of the models you downloaded (or [sideloaded](https://lmstudio.ai/docs/advanced/sideload)).
- Optionally, choose load configuration parameters.

![undefined](https://lmstudio.ai/assets/docs/loader.png)

Quickly open the model loader with `cmd` + `L` on macOS or `ctrl` + `L` on Windows/Linux

##### What does loading a model mean?

Loading a model typically means allocating memory to be able to accommodate the model's weights and other parameters in your computer's RAM.

### 3. Chat\![](#3-chat)

Once the model is loaded, you can start a back-and-forth conversation with the model in the Chat tab.

![undefined](https://lmstudio.ai/assets/docs/chat.png)

* * *

Chat with other LM Studio users, discuss LLMs, hardware, and more on the [LM Studio Discord server](https://discord.gg/aPQfnNkxGC).