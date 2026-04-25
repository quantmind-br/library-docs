---
title: Run LM Studio as a service (headless)
url: https://lmstudio.ai/docs/developer/core/headless
source: sitemap
fetched_at: 2026-04-07T21:29:56.827700793-03:00
rendered_js: false
word_count: 416
summary: This document explains two methods for running LM Studio as a background service—the recommended standalone daemon, llmster, or using the desktop app in headless mode—and details advanced features like Just-In-Time (JIT) model loading.
tags:
    - llmstudio
    - background-service
    - daemon
    - headless-mode
    - model-loading
    - api-setup
category: guide
---

LM Studio can be run as a background service without the GUI. There are two ways to do this:

- **llmster** (recommended) — a standalone daemon, no GUI required
- **Desktop app in headless mode** — hide the UI and run the desktop app as a service

## Option 1: llmster (recommended)[](#option-1-llmster-recommended "Link to 'Option 1: llmster (recommended)'")

llmster is the core of the LM Studio desktop app, packaged to be server-native, without reliance on the GUI. It can run on Linux boxes, cloud servers, GPU rigs, or your local machine without the GUI. See the [LM Studio 0.4.0 release post](https://lmstudio.ai/blog/0.4.0) for more details.

![llmster](https://lmstudio.ai/assets/blog/0.4.0/llmster@2x.png)

### Install llmster[](#install-llmster)

**Linux / Mac**

```

curl -fsSL https://lmstudio.ai/install.sh | bash
```

**Windows**

```

irm https://lmstudio.ai/install.ps1 | iex
```

### Start llmster[](#start-llmster)


See the [daemon CLI docs](https://lmstudio.ai/docs/cli/daemon/daemon-up) for full reference.

For setting up llmster as a startup task on Linux, see [Linux Startup Task](https://lmstudio.ai/docs/developer/core/headless_llmster).

## Option 2: Desktop app in headless mode[](#option-2-desktop-app-in-headless-mode "Link to 'Option 2: Desktop app in headless mode'")

This works on Mac, Windows, and Linux machines with a graphical user interface. It's useful if you already have the desktop app installed and want it to run as a background service.

### Run the LLM service on machine login[](#run-the-llm-service-on-machine-login)

Head to app settings (`Cmd` / `Ctrl` + `,`) and check the box to run the LLM server on login.

![undefined](https://lmstudio.ai/assets/docs/headless-settings.webp)

Enable the LLM server to start on machine login

When this setting is enabled, exiting the app will minimize it to the system tray, and the LLM server will continue to run in the background.

### Auto Server Start[](#auto-server-start)

Your last server state will be saved and restored on app or service launch.

To achieve this programmatically:


## Just-In-Time (JIT) model loading for REST endpoints[](#just-in-time-jit-model-loading-for-rest-endpoints "Link to 'Just-In-Time (JIT) model loading for REST endpoints'")

Applies to both options. Useful when using LM Studio as an LLM service with other frontends or applications.

![undefined](https://lmstudio.ai/assets/docs/jit-loading.webp)

#### When JIT loading is ON:

- Calls to OpenAI-compatible `/v1/models` will return all downloaded models, not only the ones loaded into memory
- Calls to inference endpoints will load the model into memory if it's not already loaded

#### When JIT loading is OFF:

- Calls to OpenAI-compatible `/v1/models` will return only the models loaded into memory
- You have to first load the model into memory before being able to use it

#### What about auto unloading?

JIT loaded models will be auto-unloaded from memory by default after a set period of inactivity ([learn more](https://lmstudio.ai/docs/developer/core/ttl-and-auto-evict)).

Chat with other LM Studio developers, discuss LLMs, hardware, and more on the [LM Studio Discord server](https://discord.gg/aPQfnNkxGC).

Please report bugs and issues in the [lmstudio-bug-tracker](https://github.com/lmstudio-ai/lmstudio-bug-tracker/issues) GitHub repository.