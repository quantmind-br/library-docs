---
title: OpenAI Video Generation | liteLLM
url: https://docs.litellm.ai/docs/providers/openai/videos
source: sitemap
fetched_at: 2026-01-21T19:50:01.209104722-03:00
rendered_js: false
word_count: 157
summary: This document provides a comprehensive guide on using LiteLLM to interface with OpenAI's video generation models, covering SDK usage, proxy configuration, and API endpoints for generating, editing, and retrieving videos.
tags:
    - litellm
    - openai-sora
    - video-generation
    - api-proxy
    - python-sdk
    - video-editing
    - rest-api
category: guide
---

LiteLLM supports OpenAI's video generation models including Sora.

## Quick Start[​](#quick-start "Direct link to Quick Start")

### Required API Keys[​](#required-api-keys "Direct link to Required API Keys")

```
import os 
os.environ["OPENAI_API_KEY"]="your-api-key"
```

### Basic Usage[​](#basic-usage "Direct link to Basic Usage")

```
from litellm import video_generation, video_content
import os

os.environ["OPENAI_API_KEY"]="your-api-key"

# Generate a video
response = video_generation(
    prompt="A cat playing with a ball of yarn in a sunny garden",
    model="sora-2",
    seconds="8",
    size="720x1280"
)

print(f"Video ID: {response.id}")
print(f"Status: {response.status}")

# Download video content when ready
video_bytes = video_content(
    video_id=response.id,
)

# Save to file
withopen("generated_video.mp4","wb")as f:
    f.write(video_bytes)
```

## **LiteLLM Proxy Usage**[​](#litellm-proxy-usage "Direct link to litellm-proxy-usage")

LiteLLM provides OpenAI API compatible video endpoints for complete video generation workflow:

- `/videos/generations` - Generate new videos
- `/videos/remix` - Edit existing videos with reference images
- `/videos/status` - Check video generation status
- `/videos/retrieval` - Download completed videos

**Setup**

Add this to your litellm proxy config.yaml

```
model_list:
-model_name: sora-2
litellm_params:
model: openai/sora-2
api_key: os.environ/OPENAI_API_KEY
```

Start litellm

```
litellm --config /path/to/config.yaml

# RUNNING on http://0.0.0.0:4000
```

Test video generation request

```
curl --location 'http://localhost:4000/v1/videos' \
--header 'Content-Type: application/json' \
--header 'x-litellm-api-key: sk-1234' \
--data '{
    "model": "sora-2",
    "prompt": "A beautiful sunset over the ocean"
}'
```

Test video status request

```
# Using custom-llm-provider header
curl --location 'http://localhost:4000/v1/videos/video_id' \
--header 'Accept: application/json' \
--header 'x-litellm-api-key: sk-1234' \
--header 'custom-llm-provider: openai'
```

Test video retrieval request

```
# Using custom-llm-provider header
curl --location 'http://localhost:4000/v1/videos/video_id/content' \
--header 'Accept: application/json' \
--header 'x-litellm-api-key: sk-1234' \
--header 'custom-llm-provider: openai' \
--output video.mp4

# Or using query parameter
curl --location 'http://localhost:4000/v1/videos/video_id/content?custom_llm_provider=openai' \
--header 'Accept: application/json' \
--header 'x-litellm-api-key: sk-1234' \
--output video.mp4
```

Test video remix request

```
# Using custom_llm_provider in request body
curl --location --request POST 'http://localhost:4000/v1/videos/video_id/remix' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'x-litellm-api-key: sk-1234' \
--data '{
    "prompt": "New remix instructions",
    "custom_llm_provider": "openai"
}'

# Or using custom-llm-provider header
curl --location --request POST 'http://localhost:4000/v1/videos/video_id/remix' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'x-litellm-api-key: sk-1234' \
--header 'custom-llm-provider: openai' \
--data '{
    "prompt": "New remix instructions"
}'
```

Test OpenAI video generation request

```
curl http://localhost:4000/v1/videos \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sora-2",
    "prompt": "A cat playing with a ball of yarn in a sunny garden",
    "seconds": "8",
    "size": "720x1280"
  }'
```

## Supported Models[​](#supported-models "Direct link to Supported Models")

Model NameDescriptionMax DurationSupported Sizessora-2OpenAI's latest video generation model8 seconds720x1280, 1280x720

## Video Generation Parameters[​](#video-generation-parameters "Direct link to Video Generation Parameters")

- `prompt` (required): Text description of the desired video
- `model` (optional): Model to use, defaults to "sora-2"
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
        model="sora-2",
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

## Video Editing with Reference Images[​](#video-editing-with-reference-images "Direct link to Video Editing with Reference Images")

```
# Video editing with reference image
response = litellm.video_generation(
    prompt="Make the cat jump higher",
    input_reference=open("path/to/image.jpg","rb"),# Reference image
    model="sora-2",
    seconds="8"
)

print(f"Video ID: {response.id}")
```

## Error Handling[​](#error-handling "Direct link to Error Handling")

```
from litellm.exceptions import BadRequestError, AuthenticationError

try:
    response = video_generation(
        prompt="A cat playing with a ball of yarn"
)
except AuthenticationError as e:
print(f"Authentication failed: {e}")
except BadRequestError as e:
print(f"Bad request: {e}")
```