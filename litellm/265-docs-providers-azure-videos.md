---
title: Azure Video Generation | liteLLM
url: https://docs.litellm.ai/docs/providers/azure/videos
source: sitemap
fetched_at: 2026-01-21T19:48:21.620167661-03:00
rendered_js: false
word_count: 237
summary: This document provides instructions for integrating Azure OpenAI's video generation models, including Sora, using the LiteLLM SDK and proxy server.
tags:
    - azure-openai
    - video-generation
    - sora
    - litellm-proxy
    - python-sdk
    - observability
category: guide
---

LiteLLM supports Azure OpenAI's video generation models including Sora with full end-to-end integration.

PropertyDetailsDescriptionAzure OpenAI's video generation models including Sora-2Provider Route on LiteLLM`azure/`Supported Models`sora-2`Cost Tracking✅ Duration-based pricing ($0.10/second)Logging Support✅ Full request/response loggingGuardrails Support✅ Content moderation and safety checksProxy Server Support✅ Full proxy integration with virtual keysSpend Management✅ Budget tracking and rate limitingLink to Provider Doc[Azure OpenAI Video Generation ↗](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/video-generation)

## Quick Start[​](#quick-start "Direct link to Quick Start")

### Required API Keys[​](#required-api-keys "Direct link to Required API Keys")

```
import os 
os.environ["AZURE_OPENAI_API_KEY"]="your-azure-api-key"
os.environ["AZURE_OPENAI_API_BASE"]="https://your-resource.openai.azure.com/"
```

### Basic Usage[​](#basic-usage "Direct link to Basic Usage")

```
from litellm import video_generation, video_status, video_content
import os
import time

os.environ["AZURE_OPENAI_API_KEY"]="your-azure-api-key"
os.environ["AZURE_OPENAI_API_BASE"]="https://your-resource.openai.azure.com/"

# Generate video
response = video_generation(
    model="azure/sora-2",
    prompt="A cat playing with a ball of yarn in a sunny garden",
    seconds="8",
    size="720x1280"
)

print(f"Video ID: {response.id}")
print(f"Initial Status: {response.status}")

# Check status until video is ready
whileTrue:
    status_response = video_status(
        video_id=response.id
)

print(f"Current Status: {status_response.status}")

if status_response.status =="completed":
break
elif status_response.status =="failed":
print("Video generation failed")
break

    time.sleep(10)# Wait 10 seconds before checking again

# Download video content when ready
video_bytes = video_content(
    video_id=response.id
)

# Save to file
withopen("generated_video.mp4","wb")as f:
    f.write(video_bytes)
```

## Usage - LiteLLM Proxy Server[​](#usage---litellm-proxy-server "Direct link to Usage - LiteLLM Proxy Server")

Here's how to call Azure video generation models with the LiteLLM Proxy Server

### 1. Save key in your environment[​](#1-save-key-in-your-environment "Direct link to 1. Save key in your environment")

```
export AZURE_OPENAI_API_KEY="your-azure-api-key"
export AZURE_OPENAI_API_BASE="https://your-resource.openai.azure.com/"
```

### 2. Start the proxy[​](#2-start-the-proxy "Direct link to 2. Start the proxy")

- config.yaml
- CLI

```
model_list:
-model_name: azure-sora-2
litellm_params:
model: azure/sora-2
api_key: os.environ/AZURE_OPENAI_API_KEY
api_base: os.environ/AZURE_OPENAI_API_BASE
```

### 3. Test it[​](#3-test-it "Direct link to 3. Test it")

- Curl Request
- OpenAI v1.0.0+

```
curl --location 'http://0.0.0.0:4000/videos/generations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer sk-1234' \
--data '{
    "model": "azure-sora-2",
    "prompt": "A cat playing with a ball of yarn in a sunny garden",
    "seconds": "8",
    "size": "720x1280"
}'
```

## Supported Models[​](#supported-models "Direct link to Supported Models")

Model Namesora-2sora-2-prosora-2-pro-high-res

## Logging & Observability[​](#logging--observability "Direct link to Logging & Observability")

### Request/Response Logging[​](#requestresponse-logging "Direct link to Request/Response Logging")

All video generation requests are automatically logged with:

- **Request details**: prompt, model, duration, size
- **Response details**: video ID, status, creation time
- **Cost tracking**: duration-based pricing calculation
- **Performance metrics**: request latency, processing time

### Logging Providers[​](#logging-providers "Direct link to Logging Providers")

Video generation works with all LiteLLM logging providers:

- **Datadog**: Real-time monitoring and alerting
- **Helicone**: Request tracing and debugging
- **LangSmith**: LangChain integration and tracing
- **Custom webhooks**: Send logs to your own endpoints

**Example: Enable Datadog logging**

```
general_settings:
alerting:["datadog"]
datadog_api_key: os.environ/DATADOG_API_KEY
```

## Video Generation Parameters[​](#video-generation-parameters "Direct link to Video Generation Parameters")

- `prompt` (required): Text description of the desired video
- `model` (optional): Model to use, defaults to "azure/sora-2"
- `seconds` (optional): Video duration in seconds (e.g., "8", "16")
- `size` (optional): Video dimensions (e.g., "720x1280", "1280x720")
- `input_reference` (optional): Reference image for video editing
- `user` (optional): User identifier for tracking

## Video Content Retrieval[​](#video-content-retrieval "Direct link to Video Content Retrieval")

```
# Download video content
video_bytes = video_content(
    video_id="video_1234567890"
)

# Save to file
withopen("video.mp4","wb")as f:
    f.write(video_bytes)
```

## Complete Workflow[​](#complete-workflow "Direct link to Complete Workflow")

```
import litellm
import time

defgenerate_and_download_video(prompt):
# Step 1: Generate video
    response = litellm.video_generation(
        prompt=prompt,
        model="azure/sora-2",
        seconds="8",
        size="720x1280"
)

    video_id = response.id
print(f"Video ID: {video_id}")

# Step 2: Wait for processing (in practice, poll status)
    time.sleep(30)

# Step 3: Download video
    video_bytes = litellm.video_content(
        video_id=video_id
)

# Step 4: Save to file
withopen(f"video_{video_id}.mp4","wb")as f:
        f.write(video_bytes)

returnf"video_{video_id}.mp4"

# Usage
video_file = generate_and_download_video(
"A cat playing with a ball of yarn in a sunny garden"
)
```

## Video Remix (Video Editing)[​](#video-remix-video-editing "Direct link to Video Remix (Video Editing)")

```
# Video editing with reference image
response = litellm.video_remix(
    video_id="video_456",
    prompt="Make the cat jump higher",
    input_reference=open("path/to/image.jpg","rb"),# Reference image as file object
    seconds="8"
)

print(f"Video ID: {response.id}")
```

## Error Handling[​](#error-handling "Direct link to Error Handling")

```
from litellm.exceptions import BadRequestError, AuthenticationError

try:
    response = video_generation(
        prompt="A cat playing with a ball of yarn",
        model="azure/sora-2"
)
except AuthenticationError as e:
print(f"Authentication failed: {e}")
except BadRequestError as e:
print(f"Bad request: {e}")
```