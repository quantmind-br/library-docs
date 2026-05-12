---
title: Server Arguments - vLLM
url: https://docs.vllm.ai/en/latest/configuration/serve_args/
source: sitemap
fetched_at: 2026-05-07T21:11:15.927444944-03:00
rendered_js: false
word_count: 123
summary: This document explains how to launch the vLLM server using CLI arguments and how to utilize YAML configuration files for managing server deployment settings.
tags:
    - vllm
    - server-configuration
    - cli-arguments
    - yaml-config
    - deployment
category: configuration
---

[](https://github.com/vllm-project/vllm/edit/main/docs/configuration/serve_args.md "Edit this page")

The `vllm serve` command is used to launch the OpenAI-compatible server.

## CLI Arguments[¶](#cli-arguments "Permanent link")

The `vllm serve` command is used to launch the OpenAI-compatible server. To see the available options, take a look at the [CLI Reference](https://docs.vllm.ai/en/latest/cli/)!

## Configuration file[¶](#configuration-file "Permanent link")

You can load CLI arguments via a [YAML](https://yaml.org/) config file. The argument names must be the long form of those outlined [above](https://docs.vllm.ai/en/latest/configuration/serve_args/).

For example:

```
# config.yaml

model:meta-llama/Llama-3.1-8B-Instruct
host:"127.0.0.1"
port:6379
uvicorn-log-level:"info"
```

To use the above config file:

```
vllmserve--configconfig.yaml
```

Note

In case an argument is supplied simultaneously using command line and the config file, the value from the command line will take precedence. The order of priorities is `command line > config file values > defaults`. e.g. `vllm serve SOME_MODEL --config config.yaml`, SOME\_MODEL takes precedence over `model` in config file.