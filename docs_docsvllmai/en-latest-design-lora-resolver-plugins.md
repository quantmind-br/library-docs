---
title: LoRA Resolver Plugins - vLLM
url: https://docs.vllm.ai/en/latest/design/lora_resolver_plugins/
source: sitemap
fetched_at: 2026-05-07T21:12:21.342833028-03:00
rendered_js: false
word_count: 565
summary: This document explains how to use and configure vLLM's LoRA resolver plugins to dynamically load LoRA adapters at runtime from various storage backends without restarting the server.
tags:
    - vllm
    - lora
    - adapter-loading
    - plugins
    - runtime-configuration
    - model-serving
category: configuration
---

[](https://github.com/vllm-project/vllm/edit/main/docs/design/lora_resolver_plugins.md "Edit this page")

This directory contains vLLM's LoRA resolver plugins built on the [`LoRAResolver`](https://docs.vllm.ai/en/latest/api/vllm/lora/resolver/#vllm.lora.resolver.LoRAResolver "            LoRAResolver") framework. They automatically discover and load LoRA adapters from a specified local storage path, eliminating the need for manual configuration or server restarts.

## Overview[¶](#overview "Permanent link")

LoRA Resolver Plugins provide a flexible way to dynamically load LoRA adapters at runtime. When vLLM receives a request for a LoRA adapter that hasn't been loaded yet, the resolver plugins will attempt to locate and load the adapter from their configured storage locations. This enables:

- **Dynamic LoRA Loading**: Load adapters on-demand without server restarts
- **Multiple Storage Backends**: Support for filesystem, S3, and custom backends. The built-in `lora_filesystem_resolver` requires a local storage path, while the built-in `hf_hub_resolver` will pull LoRA adapters from Huggingface Hub and proceed in an identical manner. In general, custom resolvers can be implemented to fetch from any source.
- **Automatic Discovery**: Seamless integration with existing LoRA workflows
- **Scalable Deployment**: Centralized adapter management across multiple vLLM instances

## Prerequisites[¶](#prerequisites "Permanent link")

Before using LoRA Resolver Plugins, ensure the following environment variables are configured:

### Required Environment Variables[¶](#required-environment-variables "Permanent link")

1. **`VLLM_ALLOW_RUNTIME_LORA_UPDATING`** : Must be set to `true` or `1` to enable dynamic LoRA loading
   
   ```
   exportVLLM_ALLOW_RUNTIME_LORA_UPDATING=true
   ```
2. **`VLLM_PLUGINS`** : Must include the desired resolver plugins (comma-separated list)
   
   ```
   exportVLLM_PLUGINS=lora_filesystem_resolver
   ```
3. **`VLLM_LORA_RESOLVER_CACHE_DIR`** : Must be set to a valid directory path for filesystem resolver
   
   ```
   exportVLLM_LORA_RESOLVER_CACHE_DIR=/path/to/lora/adapters
   ```

### Optional Environment Variables[¶](#optional-environment-variables "Permanent link")

- **`VLLM_PLUGINS`** : If not set, all available plugins will be loaded. If set to empty string, no plugins will be loaded.

## Available Resolvers[¶](#available-resolvers "Permanent link")

### lora\_filesystem\_resolver[¶](#lora_filesystem_resolver "Permanent link")

The filesystem resolver is installed with vLLM by default and enables loading LoRA adapters from a local directory structure.

#### Setup Steps[¶](#setup-steps "Permanent link")

1. **Create the LoRA adapter storage directory**:
   
   ```
   mkdir-p/path/to/lora/adapters
   ```
2. **Set environment variables**:
   
   ```
   exportVLLM_ALLOW_RUNTIME_LORA_UPDATING=true
   exportVLLM_PLUGINS=lora_filesystem_resolver
   exportVLLM_LORA_RESOLVER_CACHE_DIR=/path/to/lora/adapters
   ```
3. **Start vLLM server**: Your base model can be `meta-llama/Llama-2-7b-hf`. Please make sure you set up the Hugging Face token in your env var `export HF_TOKEN=xxx235`.
   
   ```
   python-mvllm.entrypoints.openai.api_server\
   --modelyour-base-model\
   --enable-lora
   ```

#### Directory Structure Requirements[¶](#directory-structure-requirements "Permanent link")

The filesystem resolver expects LoRA adapters to be organized in the following structure:

```
/path/to/lora/adapters/
├── adapter1/
│   ├── adapter_config.json
│   ├── adapter_model.bin
│   └── tokenizer files (if applicable)
├── adapter2/
│   ├── adapter_config.json
│   ├── adapter_model.bin
│   └── tokenizer files (if applicable)
└── ...
```

Each adapter directory must contain:

- **`adapter_config.json`** : Required configuration file with the following structure:
  
  ```
  {
  "peft_type":"LORA",
  "base_model_name_or_path":"your-base-model-name",
  "r":16,
  "lora_alpha":32,
  "target_modules":["q_proj","v_proj"],
  "bias":"none",
  "modules_to_save":null,
  "use_rslora":false,
  "use_dora":false
  }
  ```
- **`adapter_model.bin`** : The LoRA adapter weights file

#### Usage Example[¶](#usage-example "Permanent link")

1. **Prepare your LoRA adapter**:
   
   ```
   # Assuming you have a LoRA adapter in /tmp/my_lora_adapter
   cp-r/tmp/my_lora_adapter/path/to/lora/adapters/my_sql_adapter
   ```
2. **Verify the directory structure**:
   
   ```
   ls-la/path/to/lora/adapters/my_sql_adapter/
   # Should show: adapter_config.json, adapter_model.bin, etc.
   ```
3. **Make a request using the adapter**:
   
   ```
   curlhttp://localhost:8000/v1/completions\
   -H"Content-Type: application/json"\
   -d'{
           "model": "my_sql_adapter",
           "prompt": "Generate a SQL query for:",
           "max_tokens": 50,
           "temperature": 0.1
       }'
   ```

#### How It Works[¶](#how-it-works "Permanent link")

1. When vLLM receives a request for a LoRA adapter named `my_sql_adapter`
2. The filesystem resolver checks if `/path/to/lora/adapters/my_sql_adapter/` exists
3. If found, it validates the `adapter_config.json` file
4. If the configuration matches the base model and is valid, the adapter is loaded
5. The request is processed normally with the newly loaded adapter
6. The adapter remains available for future requests

## Advanced Configuration[¶](#advanced-configuration "Permanent link")

### Multiple Resolvers[¶](#multiple-resolvers "Permanent link")

You can configure multiple resolver plugins to load adapters from different sources:

'lora\_s3\_resolver' is an example of a custom resolver you would need to implement

```
exportVLLM_PLUGINS=lora_filesystem_resolver,lora_s3_resolver
```

All listed resolvers are enabled; at request time, vLLM tries them in order until one succeeds.

### Custom Resolver Implementation[¶](#custom-resolver-implementation "Permanent link")

To implement your own resolver plugin:

1. **Create a new resolver class**:
   
   ```
   fromvllm.lora.resolverimport LoRAResolver, LoRAResolverRegistry
   fromvllm.lora.requestimport LoRARequest
   
   classCustomResolver(LoRAResolver):
       async defresolve_lora(self, base_model_name: str, lora_name: str) -> Optional[LoRARequest]:
           # Your custom resolution logic here
           pass
   ```
2. **Register the resolver**:
   
   ```
   defregister_custom_resolver():
       resolver = CustomResolver()
       LoRAResolverRegistry.register_resolver("Custom Resolver", resolver)
   ```

## Troubleshooting[¶](#troubleshooting "Permanent link")

### Common Issues[¶](#common-issues "Permanent link")

01. **"VLLM\_LORA\_RESOLVER\_CACHE\_DIR must be set to a valid directory"**
02. Ensure the directory exists and is accessible
03. Check file permissions on the directory
04. **"LoRA adapter not found"**
05. Verify the adapter directory name matches the requested model name
06. Check that `adapter_config.json` exists and is valid JSON
07. Ensure `adapter_model.bin` exists in the directory
08. **"Invalid adapter configuration"**
09. Verify `peft_type` is set to "LORA"
10. Check that `base_model_name_or_path` matches your base model
11. Ensure `target_modules` is properly configured
12. **"LoRA rank exceeds maximum"**
13. Check that `r` value in `adapter_config.json` doesn't exceed `max_lora_rank` setting

### Debugging Tips[¶](#debugging-tips "Permanent link")

1. **Enable debug logging**:
   
   ```
   exportVLLM_LOGGING_LEVEL=DEBUG
   ```
2. **Verify environment variables**:
   
   ```
   echo$VLLM_ALLOW_RUNTIME_LORA_UPDATING
   echo$VLLM_PLUGINS
   echo$VLLM_LORA_RESOLVER_CACHE_DIR
   ```
3. **Test adapter configuration**:
   
   ```
   python-c"
   import json
   with open('/path/to/lora/adapters/my_adapter/adapter_config.json') as f:
       config = json.load(f)
   print('Config valid:', config)
   "
   ```