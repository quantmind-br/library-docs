---
title: File Management | liteLLM
url: https://docs.litellm.ai/docs/proxy/config_management
source: sitemap
fetched_at: 2026-01-21T19:51:25.477180712-03:00
rendered_js: false
word_count: 82
summary: This document explains how to use the include directive in LiteLLM configuration files to import and merge external YAML files. It demonstrates how to modularize settings by splitting model lists and parameters into multiple separate files.
tags:
    - litellm
    - yaml-configuration
    - include-directive
    - proxy-server
    - modular-config
    - config-management
category: configuration
---

## `include` external YAML files in a config.yaml[​](#include-external-yaml-files-in-a-configyaml "Direct link to include-external-yaml-files-in-a-configyaml")

You can use `include` to include external YAML files in a config.yaml.

**Quick Start Usage:**

To include a config file, use `include` with either a single file or a list of files.

Contents of `parent_config.yaml`:

```
include:
- model_config.yaml # 👈 Key change, will include the contents of model_config.yaml

litellm_settings:
callbacks:["prometheus"]
```

Contents of `model_config.yaml`:

```
model_list:
-model_name: gpt-4o
litellm_params:
model: openai/gpt-4o
api_base: https://exampleopenaiendpoint-production.up.railway.app/
-model_name: fake-anthropic-endpoint
litellm_params:
model: anthropic/fake
api_base: https://exampleanthropicendpoint-production.up.railway.app/

```

Start proxy server

This will start the proxy server with config `parent_config.yaml`. Since the `include` directive is used, the server will also include the contents of `model_config.yaml`.

```
litellm --config parent_config.yaml --detailed_debug
```

## Examples using `include`[​](#examples-using-include "Direct link to examples-using-include")

Include a single file:

```
include:
- model_config.yaml
```

Include multiple files:

```
include:
- model_config.yaml
- another_config.yaml
```