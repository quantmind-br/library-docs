---
title: CLI Arguments | liteLLM
url: https://docs.litellm.ai/docs/proxy/cli
source: sitemap
fetched_at: 2026-01-21T19:51:21.342963584-03:00
rendered_js: false
word_count: 296
summary: This document provides a comprehensive list of command-line interface arguments and environment variables available for configuring the litellm server and model parameters.
tags:
    - litellm
    - cli-arguments
    - server-configuration
    - command-line-interface
    - environment-variables
category: reference
---

Cli arguments, --host, --port, --num\_workers

## --host[​](#--host "Direct link to --host")

- **Default:** `'0.0.0.0'`
- The host for the server to listen on.
- **Usage:**
- **Usage - set Environment Variable:** `HOST`

```
export HOST=127.0.0.1
litellm
```

## --port[​](#--port "Direct link to --port")

- **Default:** `4000`
- The port to bind the server to.
- **Usage:**
- **Usage - set Environment Variable:** `PORT`

## --num\_workers[​](#--num_workers "Direct link to --num_workers")

- **Default:** `1`
- The number of uvicorn workers to spin up.
- **Usage:**
- **Usage - set Environment Variable:** `NUM_WORKERS`
  
  ```
  export NUM_WORKERS=4
  litellm
  ```

## --api\_base[​](#--api_base "Direct link to --api_base")

- **Default:** `None`
- The API base for the model litellm should call.
- **Usage:**
  
  ```
  litellm --model huggingface/tinyllama --api_base https://k58ory32yinf1ly0.us-east-1.aws.endpoints.huggingface.cloud
  ```

## --api\_version[​](#--api_version "Direct link to --api_version")

- **Default:** `None`
- For Azure services, specify the API version.
- **Usage:**
  
  ```
  litellm --model azure/gpt-deployment --api_version 2023-08-01 --api_base https://<your api base>"
  ```

## --model or -m[​](#--model-or--m "Direct link to --model or -m")

- **Default:** `None`
- The model name to pass to Litellm.
- **Usage:**
  
  ```
  litellm --model gpt-3.5-turbo
  ```

## --test[​](#--test "Direct link to --test")

- **Type:** `bool` (Flag)
- Proxy chat completions URL to make a test request.
- **Usage:**

## --health[​](#--health "Direct link to --health")

- **Type:** `bool` (Flag)
- Runs a health check on all models in config.yaml
- **Usage:**

## --alias[​](#--alias "Direct link to --alias")

- **Default:** `None`
- An alias for the model, for user-friendly reference.
- **Usage:**
  
  ```
  litellm --alias my-gpt-model
  ```

## --debug[​](#--debug "Direct link to --debug")

- **Default:** `False`
- **Type:** `bool` (Flag)
- Enable debugging mode for the input.
- **Usage:**
- **Usage - set Environment Variable:** `DEBUG`

## --detailed\_debug[​](#--detailed_debug "Direct link to --detailed_debug")

- **Default:** `False`
- **Type:** `bool` (Flag)
- Enable debugging mode for the input.
- **Usage:**
- **Usage - set Environment Variable:** `DETAILED_DEBUG`
  
  ```
  export DETAILED_DEBUG=True
  litellm
  ```

#### --temperature[​](#--temperature "Direct link to --temperature")

- **Default:** `None`
- **Type:** `float`
- Set the temperature for the model.
- **Usage:**
  
  ```
  litellm --temperature 0.7
  ```

## --max\_tokens[​](#--max_tokens "Direct link to --max_tokens")

- **Default:** `None`
- **Type:** `int`
- Set the maximum number of tokens for the model output.
- **Usage:**

## --request\_timeout[​](#--request_timeout "Direct link to --request_timeout")

- **Default:** `6000`
- **Type:** `int`
- Set the timeout in seconds for completion calls.
- **Usage:**
  
  ```
  litellm --request_timeout 300
  ```

## --drop\_params[​](#--drop_params "Direct link to --drop_params")

- **Type:** `bool` (Flag)
- Drop any unmapped params.
- **Usage:**

## --add\_function\_to\_prompt[​](#--add_function_to_prompt "Direct link to --add_function_to_prompt")

- **Type:** `bool` (Flag)
- If a function passed but unsupported, pass it as a part of the prompt.
- **Usage:**
  
  ```
  litellm --add_function_to_prompt
  ```

## --config[​](#--config "Direct link to --config")

- Configure Litellm by providing a configuration file path.
- **Usage:**
  
  ```
  litellm --config path/to/config.yaml
  ```

## --telemetry[​](#--telemetry "Direct link to --telemetry")

- **Default:** `True`
- **Type:** `bool`
- Help track usage of this feature.
- **Usage:**
  
  ```
  litellm --telemetry False
  ```

## --log\_config[​](#--log_config "Direct link to --log_config")

- **Default:** `None`
- **Type:** `str`
- Specify a log configuration file for uvicorn.
- **Usage:**
  
  ```
  litellm --log_config path/to/log_config.conf
  ```

## --skip\_server\_startup[​](#--skip_server_startup "Direct link to --skip_server_startup")

- **Default:** `False`
- **Type:** `bool` (Flag)
- Skip starting the server after setup (useful for DB migrations only).
- **Usage:**
  
  ```
  litellm --skip_server_startup
  ```