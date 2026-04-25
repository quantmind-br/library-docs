---
title: '`lms` — LM Studio''s CLI'
url: https://lmstudio.ai/docs/cli
source: sitemap
fetched_at: 2026-04-07T21:28:41.713604466-03:00
rendered_js: false
word_count: 237
summary: This document serves as a guide for users on installing, verifying, and using the `lms` command-line interface to interact with local language models.
tags:
    - command-line
    - lms-usage
    - local-models
    - installation-guide
    - server-management
category: tutorial
---

## Install `lms`[](#install-lms "Link to 'Install ,[object Object]'")

`lms` ships with LM Studio, so you don't need to do any additional installation steps if you have LM Studio installed.

Just open a terminal window and run `lms`:


## Open source[](#open-source "Link to 'Open source'")

`lms` is **MIT Licensed** and is developed in this repository on GitHub: [https://github.com/lmstudio-ai/lms](https://github.com/lmstudio-ai/lms)

## Command quick links[](#command-quick-links "Link to 'Command quick links'")

CommandSyntaxDocsChat in the terminal`lms chat`[Guide](https://lmstudio.ai/docs/cli/local-models/chat)Download models`lms get`[Guide](https://lmstudio.ai/docs/cli/local-models/get)List your models`lms ls`[Guide](https://lmstudio.ai/docs/cli/local-models/ls)See models loaded into memory`lms ps`[Guide](https://lmstudio.ai/docs/cli/local-models/ps)Control the server`lms server start`[Guide](https://lmstudio.ai/docs/cli/serve/server-start)Manage the inference runtime`lms runtime`[Guide](https://lmstudio.ai/docs/cli/runtime)Manage the headless daemon`lms daemon`[Guide](https://lmstudio.ai/docs/cli/daemon/daemon-up)Manage LM Link`lms link`[Guide](https://lmstudio.ai/docs/cli/link/link-enable)

### Verify the installation[](#verify-the-installation)

👉 You need to run LM Studio *at least once* before you can use `lms`.

Open a terminal window and run `lms`.

## Use `lms` to automate and debug your workflows[](#use-lms-to-automate-and-debug-your-workflows "Link to 'Use ,[object Object], to automate and debug your workflows'")

### Start and stop the local server[](#start-and-stop-the-local-server)

```

lms server start
lms server stop
```

Learn more about [`lms server`](https://lmstudio.ai/docs/cli/serve/server-start).

### List the local models on the machine[](#list-the-local-models-on-the-machine)


Learn more about [`lms ls`](https://lmstudio.ai/docs/cli/local-models/ls).

This will reflect the current LM Studio models directory, which you set in **📂 My Models** tab in the app.

### List the currently loaded models[](#list-the-currently-loaded-models)


Learn more about [`lms ps`](https://lmstudio.ai/docs/cli/local-models/ps).

### Load a model (with options)[](#load-a-model-with-options)

```

lms load [--gpu=max|auto|0.0-1.0] [--context-length=1-N]
```

`--gpu=1.0` means 'attempt to offload 100% of the computation to the GPU'.

- Optionally, assign an identifier to your local LLM:

```

lms load openai/gpt-oss-20b --identifier="my-model-name"
```

This is useful if you want to keep the model identifier consistent.

### Unload a model[](#unload-a-model)


Learn more about [`lms load and unload`](https://lmstudio.ai/docs/cli/local-models/load).