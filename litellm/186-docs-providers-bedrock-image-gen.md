---
title: AWS Bedrock - Image Generation | liteLLM
url: https://docs.litellm.ai/docs/providers/bedrock_image_gen
source: sitemap
fetched_at: 2026-01-21T19:48:29.558344329-03:00
rendered_js: false
word_count: 132
summary: This document provides instructions on using the LiteLLM library to perform image generation through AWS Bedrock, covering supported models, parameter configuration, and authentication.
tags:
    - aws-bedrock
    - image-generation
    - litellm
    - stable-diffusion
    - amazon-titan
    - amazon-nova
category: guide
---

Use Bedrock for image generation with Stable Diffusion, Amazon Titan Image Generator, and Amazon Nova Canvas models.

## Supported Models[​](#supported-models "Direct link to Supported Models")

Model NameFunction CallCost TrackingStable Diffusion 3 - v0`image_generation(model="bedrock/stability.stability.sd3-large-v1:0", prompt=prompt)`✅Stable Diffusion - v0`image_generation(model="bedrock/stability.stable-diffusion-xl-v0", prompt=prompt)`✅Stable Diffusion - v1`image_generation(model="bedrock/stability.stable-diffusion-xl-v1", prompt=prompt)`✅Amazon Titan Image Generator - v1`image_generation(model="bedrock/amazon.titan-image-generator-v1", prompt=prompt)`✅Amazon Titan Image Generator - v2`image_generation(model="bedrock/amazon.titan-image-generator-v2:0", prompt=prompt)`✅Amazon Nova Canvas - v1`image_generation(model="bedrock/amazon.nova-canvas-v1:0", prompt=prompt)`✅

## Usage[​](#usage "Direct link to Usage")

- SDK
- PROXY

### Basic Usage[​](#basic-usage "Direct link to Basic Usage")

```
import os
from litellm import image_generation

os.environ["AWS_ACCESS_KEY_ID"]=""
os.environ["AWS_SECRET_ACCESS_KEY"]=""
os.environ["AWS_REGION_NAME"]=""

response = image_generation(
    prompt="A cute baby sea otter",
    model="bedrock/stability.stable-diffusion-xl-v0",
)
print(f"response: {response}")
```

### Set Optional Parameters[​](#set-optional-parameters "Direct link to Set Optional Parameters")

```
import os
from litellm import image_generation

os.environ["AWS_ACCESS_KEY_ID"]=""
os.environ["AWS_SECRET_ACCESS_KEY"]=""
os.environ["AWS_REGION_NAME"]=""

response = image_generation(
    prompt="A cute baby sea otter",
    model="bedrock/stability.stable-diffusion-xl-v0",
### OPENAI-COMPATIBLE ###
    size="128x512",# width=128, height=512
### PROVIDER-SPECIFIC ### see `AmazonStabilityConfig` in bedrock.py for all params
    seed=30
)
print(f"response: {response}")
```

## Using Inference Profiles with Image Generation[​](#using-inference-profiles-with-image-generation "Direct link to Using Inference Profiles with Image Generation")

For AWS Bedrock Application Inference Profiles with image generation, use the `model_id` parameter to specify the inference profile ARN:

- SDK
- PROXY

```
from litellm import image_generation

response = image_generation(
    model="bedrock/amazon.nova-canvas-v1:0",
    model_id="arn:aws:bedrock:eu-west-1:000000000000:application-inference-profile/a0a0a0a0a0a0",
    prompt="A cute baby sea otter"
)
print(f"response: {response}")
```

## Authentication[​](#authentication "Direct link to Authentication")

All standard Bedrock authentication methods are supported for image generation. See [Bedrock Authentication](https://docs.litellm.ai/docs/providers/bedrock#boto3---authentication) for details.