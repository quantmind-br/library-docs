---
title: /videos | liteLLM
url: https://docs.litellm.ai/docs/videos
source: sitemap
fetched_at: 2026-01-21T19:55:58.200476492-03:00
rendered_js: false
word_count: 393
summary: This document provides instructions and code examples for using LiteLLM to generate and manage videos using its Python SDK and Proxy server across multiple AI providers.
tags:
    - litellm
    - video-generation
    - python-sdk
    - proxy-server
    - ai-video-api
    - azure-openai
    - sora-2
category: guide
---

FeatureSupportedCost Tracking✅Logging✅ (Full request/response logging)Fallbacks✅ (Between supported models)Load Balancing✅Guardrails Support✅ Content moderation and safety checksProxy Server Support✅ Full proxy integration with virtual keysSpend Management✅ Budget tracking and rate limitingSupported Providers`openai`, `azure`, `gemini`, `vertex_ai`, `runwayml`

## **LiteLLM Python SDK Usage**[​](#litellm-python-sdk-usage "Direct link to litellm-python-sdk-usage")

### Quick Start[​](#quick-start "Direct link to Quick Start")

```
from litellm import video_generation, video_status, video_content
import os
import time

os.environ["OPENAI_API_KEY"]="sk-.."

# Generate video
response = video_generation(
    model="openai/sora-2",
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

### Async Usage[​](#async-usage "Direct link to Async Usage")

```
from litellm import avideo_generation, avideo_status, avideo_content
import os, asyncio

os.environ["OPENAI_API_KEY"]="sk-.."

asyncdeftest_async_video():
    response =await avideo_generation(
        model="openai/sora-2",
        prompt="A cat playing with a ball of yarn in a sunny garden",
        seconds="8",
        size="720x1280"
)

print(f"Video ID: {response.id}")
print(f"Initial Status: {response.status}")

# Check status until video is ready
whileTrue:
        status_response =await avideo_status(
            video_id=response.id
)

print(f"Current Status: {status_response.status}")

if status_response.status =="completed":
break
elif status_response.status =="failed":
print("Video generation failed")
break

await asyncio.sleep(10)# Wait 10 seconds before checking again

# Download video content when ready
    video_bytes =await avideo_content(
        video_id=response.id
)

# Save to file
withopen("generated_video.mp4","wb")as f:
        f.write(video_bytes)

asyncio.run(test_async_video())
```

### Video Status Checking[​](#video-status-checking "Direct link to Video Status Checking")

```
from litellm import video_status

status_response = video_status(
    video_id="video_1234567890"
)

print(f"Video Status: {status_response.status}")
print(f"Created At: {status_response.created_at}")
print(f"Model: {status_response.model}")
```

### List Videos[​](#list-videos "Direct link to List Videos")

For listing videos, you need to specify the provider since there's no video\_id to decode from:

```
from litellm import video_list

# List videos from OpenAI
videos = video_list(custom_llm_provider="openai")

for video in videos:
print(f"Video ID: {video['id']}")
```

### Video Generation with Reference Image[​](#video-generation-with-reference-image "Direct link to Video Generation with Reference Image")

```
from litellm import video_generation

# Video generation with reference image
response = video_generation(
    model="openai/sora-2",
    prompt="A cat playing with a ball of yarn in a sunny garden",
    input_reference=open("path/to/image.jpg","rb"),# Reference image as file object
    seconds="8",
    size="720x1280"
)

print(f"Video ID: {response.id}")
```

### Video Remix (Video Editing)[​](#video-remix-video-editing "Direct link to Video Remix (Video Editing)")

```
from litellm import video_remix

# Video remix with reference image
response = video_remix(
    model="openai/sora-2",
    prompt="Make the cat jump higher",
    input_reference=open("path/to/image.jpg","rb"),# Reference image as file object
    seconds="8"
)

print(f"Video ID: {response.id}")
```

### Optional Parameters[​](#optional-parameters "Direct link to Optional Parameters")

```
response = video_generation(
    model="openai/sora-2",
    prompt="A cat playing with a ball of yarn in a sunny garden",
    seconds="8",# Video duration in seconds
    size="720x1280",# Video dimensions
    input_reference=open("path/to/image.jpg","rb"),# Reference image as file object
    user="user_123"# User identifier for tracking
)
```

### Azure Video Generation[​](#azure-video-generation "Direct link to Azure Video Generation")

```
from litellm import video_generation
import os

os.environ["AZURE_OPENAI_API_KEY"]="your-azure-api-key"
os.environ["AZURE_OPENAI_API_BASE"]="https://your-resource.openai.azure.com/"
os.environ["AZURE_OPENAI_API_VERSION"]="2024-02-15-preview"

response = video_generation(
    model="azure/sora-2",
    prompt="A cat playing with a ball of yarn in a sunny garden",
    seconds="8",
    size="720x1280"
)

print(f"Video ID: {response.id}")
```

## **LiteLLM Proxy Usage**[​](#litellm-proxy-usage "Direct link to litellm-proxy-usage")

LiteLLM provides OpenAI API compatible video endpoints for complete video generation workflow:

- `/videos` - Generate new videos
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
-model_name: azure-sora-2
litellm_params:
model: azure/sora-2
api_key: os.environ/AZURE_OPENAI_API_KEY
api_base: os.environ/AZURE_OPENAI_API_BASE
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
curl --location 'http://localhost:4000/v1/videos/{video_id}' \
--header 'x-litellm-api-key: sk-1234'
```

Test video retrieval request

```
curl --location 'http://localhost:4000/v1/videos/{video_id}/content' \
--header 'x-litellm-api-key: sk-1234' \
--output video.mp4
```

Test video remix request

```
curl --location --request POST 'http://localhost:4000/v1/videos/{video_id}/remix' \
--header 'Content-Type: application/json' \
--header 'x-litellm-api-key: sk-1234' \
--data '{
    "prompt": "New remix instructions"
}'
```

Test video list request (requires custom\_llm\_provider)

```
# Note: video_list requires custom_llm_provider since there's no video_id to decode from
curl --location 'http://localhost:4000/v1/videos?custom_llm_provider=openai' \
--header 'x-litellm-api-key: sk-1234'

# Or using header
curl --location 'http://localhost:4000/v1/videos' \
--header 'x-litellm-api-key: sk-1234' \
--header 'custom-llm-provider: azure'
```

Test Azure video generation request

```
curl http://localhost:4000/v1/videos \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "azure-sora-2",
    "prompt": "A cat playing with a ball of yarn in a sunny garden",
    "seconds": "8",
    "size": "720x1280"
  }'
```

## **Using OpenAI Client with LiteLLM Proxy**[​](#using-openai-client-with-litellm-proxy "Direct link to using-openai-client-with-litellm-proxy")

You can use the standard OpenAI Python client to interact with LiteLLM's video endpoints. This provides a familiar interface while leveraging LiteLLM's provider abstraction and proxy features.

### Setup[​](#setup "Direct link to Setup")

First, configure your OpenAI client to point to your LiteLLM proxy:

```
from openai import OpenAI

# Point the OpenAI client to your LiteLLM proxy
client = OpenAI(
    api_key="sk-1234",# Your LiteLLM proxy API key
    base_url="http://localhost:4000/v1"# Your LiteLLM proxy URL
)
```

### Video Generation[​](#video-generation "Direct link to Video Generation")

Generate a new video using the OpenAI client interface:

```
# Basic video generation
response = client.videos.create(
    model="sora-2",
    prompt="A cat playing with a ball of yarn in a sunny garden",
    seconds=8,
    size="720x1280"
)

print(f"Video ID: {response.id}")
print(f"Status: {response.status}")
```

### Video Generation with Reference Image[​](#video-generation-with-reference-image-1 "Direct link to Video Generation with Reference Image")

Create a video using a reference image:

```
# Video generation with reference image
response = client.videos.create(
    model="sora-2",
    prompt="Add clouds to the video",
    seconds=4,
    input_reference=open("/path/to/your/image.jpg","rb")
)

print(f"Video ID: {response.id}")
print(f"Status: {response.status}")
```

### Video Status Checking[​](#video-status-checking-1 "Direct link to Video Status Checking")

Check the status of a video generation:

```
# Check video status
status_response = client.videos.retrieve(
    video_id="video_6900378779308191a7359266e59b53fc01cd6bbd27a70763"
)

print(f"Status: {status_response.status}")
print(f"Progress: {status_response.progress}%")

# Poll until completion
import time

while status_response.status notin["completed","failed"]:
    time.sleep(10)# Wait 10 seconds
    status_response = client.videos.retrieve(
        video_id="video_6900378779308191a7359266e59b53fc01cd6bbd27a70763"
)
print(f"Current status: {status_response.status}")
```

### List Videos[​](#list-videos-1 "Direct link to List Videos")

Get a list of your videos:

```
# List all videos
videos = client.videos.list()

for video in videos.data:
print(f"Video ID: {video.id}, Status: {video.status}")
```

### Download Video Content[​](#download-video-content "Direct link to Download Video Content")

Download the completed video:

```
# Download video content
response = client.videos.download_content(
    video_id="video_68fa2938848c8190bb718f977503aba6092ab18d68938fed"
)

# Save the video to file
withopen("generated_video.mp4","wb")as f:
    f.write(response.content)

print("Video downloaded successfully!")
```

### Video Remix (Editing)[​](#video-remix-editing "Direct link to Video Remix (Editing)")

Edit an existing video with new instructions:

```
# Remix/edit an existing video
response = client.videos.remix(
    video_id="video_68fa2574bdd88190873a8af06a370ff407094ddbc4bbb91b",
    prompt="Slow the cloud movement",
    seconds=8
)

print(f"Remix Video ID: {response.id}")
print(f"Status: {response.status}")
```

### Complete Workflow Example[​](#complete-workflow-example "Direct link to Complete Workflow Example")

Here's a complete example showing the full video generation workflow:

```
from openai import OpenAI
import time

# Initialize client
client = OpenAI(
    api_key="sk-1234",
    base_url="http://localhost:4000/v1"
)

# 1. Generate video
print("Generating video...")
response = client.videos.create(
    model="sora-2",
    prompt="A serene lake with mountains in the background",
    seconds=8,
    size="1280x720"
)

video_id = response.id
print(f"Video generation started. ID: {video_id}")

# 2. Poll for completion
print("Waiting for video to complete...")
whileTrue:
    status = client.videos.retrieve(video_id=video_id)
print(f"Status: {status.status}")

if status.status =="completed":
print("Video generation completed!")
break
elif status.status =="failed":
print("Video generation failed!")
break

    time.sleep(10)

# 3. Download video
if status.status =="completed":
print("Downloading video...")
    video_content = client.videos.download_content(video_id=video_id)

withopen(f"video_{video_id}.mp4","wb")as f:
        f.write(video_content.content)

print("Video saved successfully!")

# 4. Optional: Remix the video
print("Creating a remix...")
remix_response = client.videos.remix(
    video_id=video_id,
    prompt="Add gentle ripples to the lake surface"
)

print(f"Remix started. ID: {remix_response.id}")
```

## **Request/Response Format**[​](#requestresponse-format "Direct link to requestresponse-format")

### Example Request[​](#example-request "Direct link to Example Request")

```
{
"model":"openai/sora-2",
"prompt":"A cat playing with a ball of yarn in a sunny garden",
"seconds":"8",
"size":"720x1280",
"user":"user_123"
}
```

### Request Parameters[​](#request-parameters "Direct link to Request Parameters")

ParameterTypeRequiredDescription`model`stringYesThe video generation model to use (e.g., `"openai/sora-2"`)`prompt`stringYesText description of the desired video`seconds`stringNoVideo duration in seconds (e.g., "8", "16")`size`stringNoVideo dimensions (e.g., "720x1280", "1280x720")`input_reference`file objectNoReference image for video generation or editing (both generation and remix)`user`stringNoUser identifier for tracking`video_id`stringYes (status/retrieval)Video ID for status checking or retrieval

#### Video Generation Request Example[​](#video-generation-request-example "Direct link to Video Generation Request Example")

**For video generation:**

```
{
"model":"sora-2",
"prompt":"A cat playing with a ball of yarn in a sunny garden",
"seconds":"8",
"size":"720x1280"
}
```

**For video generation with reference image:**

```
{
"model":"sora-2",
"prompt":"A cat playing with a ball of yarn in a sunny garden",
"input_reference":open("path/to/image.jpg","rb"),# File object
"seconds":"8",
"size":"720x1280"
}
```

**For video status check:**

```
{
"video_id":"video_1234567890",
"model":"sora-2"
}
```

**For video retrieval:**

```
{
"video_id":"video_1234567890",
"model":"sora-2"
}
```

### Response Format[​](#response-format "Direct link to Response Format")

The response follows OpenAI's video generation format with the following structure:

```
{
"id":"video_6900378779308191a7359266e59b53fc01cd6bbd27a70763",
"object":"video",
"status":"queued",
"created_at":1761621895,
"completed_at":null,
"expires_at":null,
"error":null,
"progress":0,
"remixed_from_video_id":null,
"seconds":"4",
"size":"720x1280",
"model":"sora-2",
"usage":{
"duration_seconds":4.0
}
}
```

#### Response Fields[​](#response-fields "Direct link to Response Fields")

FieldTypeDescription`id`stringUnique identifier for the video`object`stringAlways `"video"` for video responses`status`stringVideo processing status (`"queued"`, `"processing"`, `"completed"`)`created_at`integerUnix timestamp when the video was created`model`stringThe model used for video generation`size`stringVideo dimensions`seconds`stringVideo duration in seconds`usage`objectToken usage and duration information

## **Supported Providers**[​](#supported-providers "Direct link to supported-providers")

ProviderLink to UsageOpenAI[Usage](https://docs.litellm.ai/docs/providers/openai/videos)Azure[Usage](https://docs.litellm.ai/docs/providers/azure/videos)Gemini[Usage](https://docs.litellm.ai/docs/providers/gemini/videos)Vertex AI[Usage](https://docs.litellm.ai/docs/providers/vertex_ai/videos)RunwayML[Usage](https://docs.litellm.ai/docs/providers/runwayml/videos)