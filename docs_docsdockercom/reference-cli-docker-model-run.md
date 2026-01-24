---
title: docker model run
url: https://docs.docker.com/reference/cli/docker/model/run/
source: llms
fetched_at: 2026-01-24T14:38:37.848018537-03:00
rendered_js: false
word_count: 172
summary: This document explains the usage, options, and interaction modes of the 'docker model run' command for executing and interacting with AI models.
tags:
    - docker-cli
    - ai-models
    - model-runner
    - inference
    - interactive-chat
    - command-line-interface
category: reference
---

DescriptionRun a model and interact with it using a submitted prompt or chat modeUsage`docker model run MODEL [PROMPT]`

## [Description](#description)

When you run a model, Docker calls an inference server API endpoint hosted by the Model Runner through Docker Desktop. The model stays in memory until another model is requested, or until a pre-defined inactivity timeout is reached (currently 5 minutes).

You do not have to use Docker model run before interacting with a specific model from a host process or from within a container. Model Runner transparently loads the requested model on-demand, assuming it has been pulled and is locally available.

You can also use chat mode in the Docker Desktop Dashboard when you select the model in the **Models** tab.

## [Options](#options)

OptionDefaultDescription`--color``no`Use colored output (auto|yes|no)`--debug`Enable debug logging`-d, --detach`Load the model in the background without interaction`--ignore-runtime-memory-check`Do not block pull if estimated runtime memory for model exceeds system resources.

## [Examples](#examples)

### [One-time prompt](#one-time-prompt)

```
docker model run ai/smollm2 "Hi"
```

Output:

```
Hello! How can I assist you today?
```

### [Interactive chat](#interactive-chat)

```
docker model run ai/smollm2
```

Output:

```
> Hi
Hi there! It's SmolLM, AI assistant. How can I help you today?
> /bye
```

### [Pre-load a model](#pre-load-a-model)

```
docker model run --detach ai/smollm2
```

This loads the model into memory without interaction, ensuring maximum performance for subsequent requests.