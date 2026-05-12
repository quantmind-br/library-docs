---
title: Sagemaker-Entrypoint - vLLM
url: https://docs.vllm.ai/en/latest/examples/online_serving/sagemaker-entrypoint/
source: sitemap
fetched_at: 2026-05-07T21:13:21.30736436-03:00
rendered_js: false
word_count: 6
summary: This script provides an entrypoint for deploying vLLM on Amazon SageMaker by dynamically converting environment variables into command-line arguments for the inference server.
tags:
    - aws-sagemaker
    - vllm
    - environment-variables
    - deployment
    - inference-server
    - shell-scripting
category: configuration
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/online_serving/sagemaker-entrypoint.md "Edit this page")

Source [https://github.com/vllm-project/vllm/blob/main/examples/online\_serving/sagemaker-entrypoint.sh](https://github.com/vllm-project/vllm/blob/main/examples/online_serving/sagemaker-entrypoint.sh).

```
#!/bin/bash

# Define the prefix for environment variables to look for
PREFIX="SM_VLLM_"
ARG_PREFIX="--"

# Initialize an array for storing the arguments
# port 8080 required by sagemaker, https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html#your-algorithms-inference-code-container-response
ARGS=(--port8080)

# Loop through all environment variables
whileIFS='='read-rkeyvalue;do
# Remove the prefix from the key, convert to lowercase, and replace underscores with dashes
arg_name=$(echo"${key#"${PREFIX}"}"|tr'[:upper:]''[:lower:]'|tr'_''-')

# Add the argument name and value to the ARGS array
ARGS+=("${ARG_PREFIX}${arg_name}")
if[-n"$value"];then
ARGS+=("$value")
fi
done<<(env|grep"^${PREFIX}")

# Pass the collected arguments to the main entrypoint
execstandard-supervisorvllmserve"${ARGS[@]}"
```