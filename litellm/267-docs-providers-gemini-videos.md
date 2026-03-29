---
title: Gemini Video Generation (Veo) | liteLLM
url: https://docs.litellm.ai/docs/providers/gemini/videos
source: sitemap
fetched_at: 2026-01-21T19:49:10.251431349-03:00
rendered_js: false
word_count: 360
summary: This document provides a comprehensive guide on using Google's Veo video generation models via LiteLLM, including implementation details for generation, status tracking, and content retrieval.
tags:
    - litellm
    - google-veo
    - video-generation
    - python-sdk
    - api-integration
    - gemini-api
category: guide
---

LiteLLM supports Google's Veo video generation models through a unified API interface.

PropertyDetailsDescriptionGoogle's Veo AI video generation modelsProvider Route on LiteLLM`gemini/`Supported Models`veo-3.0-generate-preview`, `veo-3.1-generate-preview`Cost Tracking✅ Duration-based pricingLogging Support✅ Full request/response loggingProxy Server Support✅ Full proxy integration with virtual keysSpend Management✅ Budget tracking and rate limitingLink to Provider Doc[Google Veo Documentation ↗](https://ai.google.dev/gemini-api/docs/video)

## Quick Start[​](#quick-start "Direct link to Quick Start")

### Required API Keys[​](#required-api-keys "Direct link to Required API Keys")

```
import os 
os.environ["GEMINI_API_KEY"]="your-google-api-key"
# OR
os.environ["GOOGLE_API_KEY"]="your-google-api-key"
```

### Basic Usage[​](#basic-usage "Direct link to Basic Usage")

```
from litellm import video_generation, video_status, video_content
import os
import time

os.environ["GEMINI_API_KEY"]="your-google-api-key"

# Step 1: Generate video
response = video_generation(
    model="gemini/veo-3.0-generate-preview",
    prompt="A cat playing with a ball of yarn in a sunny garden"
)

print(f"Video ID: {response.id}")
print(f"Initial Status: {response.status}")# "processing"

# Step 2: Poll for completion
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

# Step 3: Download video content
video_bytes = video_content(
    video_id=response.id
)

# Save to file
withopen("generated_video.mp4","wb")as f:
    f.write(video_bytes)

print("Video downloaded successfully!")
```

## Supported Models[​](#supported-models "Direct link to Supported Models")

Model NameDescriptionMax DurationStatusveo-3.0-generate-previewVeo 3.0 video generation8 secondsPreviewveo-3.1-generate-previewVeo 3.1 video generation8 secondsPreview

## Video Generation Parameters[​](#video-generation-parameters "Direct link to Video Generation Parameters")

LiteLLM automatically maps OpenAI-style parameters to Veo's format:

OpenAI ParameterVeo ParameterDescriptionExample`prompt``prompt`Text description of the video"A cat playing"`size``aspectRatio`Video dimensions → aspect ratio"1280x720" → "16:9"`seconds``durationSeconds`Duration in seconds"8" → 8`input_reference``image`Reference image to animateFile object or path`model``model`Model to use"gemini/veo-3.0-generate-preview"

### Size to Aspect Ratio Mapping[​](#size-to-aspect-ratio-mapping "Direct link to Size to Aspect Ratio Mapping")

LiteLLM automatically converts size dimensions to Veo's aspect ratio format:

- `"1280x720"`, `"1920x1080"` → `"16:9"` (landscape)
- `"720x1280"`, `"1080x1920"` → `"9:16"` (portrait)

### Supported Veo Parameters[​](#supported-veo-parameters "Direct link to Supported Veo Parameters")

Based on Veo's API:

- **prompt** (required): Text description with optional audio cues
- **aspectRatio**: `"16:9"` (default) or `"9:16"`
- **resolution**: `"720p"` (default) or `"1080p"` (Veo 3.1 only, 16:9 aspect ratio only)
- **durationSeconds**: Video length (max 8 seconds for most models)
- **image**: Reference image for animation
- **negativePrompt**: What to exclude from the video (Veo 3.1)
- **referenceImages**: Style and content references (Veo 3.1 only)

## Complete Workflow Example[​](#complete-workflow-example "Direct link to Complete Workflow Example")

```
import litellm
import time

defgenerate_and_download_veo_video(
    prompt:str,
    output_file:str="video.mp4",
    size:str="1280x720",
    seconds:str="8"
):
"""
    Complete workflow for Veo video generation.

    Args:
        prompt: Text description of the video
        output_file: Where to save the video
        size: Video dimensions (e.g., "1280x720" for 16:9)
        seconds: Duration in seconds

    Returns:
        bool: True if successful
    """
print(f"🎬 Generating video: {prompt}")

# Step 1: Initiate generation
    response = litellm.video_generation(
        model="gemini/veo-3.0-generate-preview",
        prompt=prompt,
        size=size,# Maps to aspectRatio
        seconds=seconds  # Maps to durationSeconds
)

    video_id = response.id
print(f"✓ Video generation started (ID: {video_id})")

# Step 2: Wait for completion
    max_wait_time =600# 10 minutes
    start_time = time.time()

while time.time()- start_time < max_wait_time:
        status_response = litellm.video_status(video_id=video_id)

if status_response.status =="completed":
print("✓ Video generation completed!")
break
elif status_response.status =="failed":
print("✗ Video generation failed")
returnFalse

print(f"⏳ Status: {status_response.status}")
        time.sleep(10)
else:
print("✗ Timeout waiting for video generation")
returnFalse

# Step 3: Download video
print("⬇️  Downloading video...")
    video_bytes = litellm.video_content(video_id=video_id)

withopen(output_file,"wb")as f:
        f.write(video_bytes)

print(f"✓ Video saved to {output_file}")
returnTrue

# Use it
generate_and_download_veo_video(
    prompt="A serene lake at sunset with mountains in the background",
    output_file="sunset_lake.mp4"
)
```

## Async Usage[​](#async-usage "Direct link to Async Usage")

```
from litellm import avideo_generation, avideo_status, avideo_content
import asyncio

asyncdefasync_video_workflow():
# Generate video
    response =await avideo_generation(
        model="gemini/veo-3.0-generate-preview",
        prompt="A cat playing with a ball of yarn"
)

# Poll for completion
whileTrue:
        status =await avideo_status(video_id=response.id)
if status.status =="completed":
break
await asyncio.sleep(10)

# Download content
    video_bytes =await avideo_content(video_id=response.id)

withopen("video.mp4","wb")as f:
        f.write(video_bytes)

# Run it
asyncio.run(async_video_workflow())
```

## LiteLLM Proxy Usage[​](#litellm-proxy-usage "Direct link to LiteLLM Proxy Usage")

### Configuration[​](#configuration "Direct link to Configuration")

Add Veo models to your `config.yaml`:

```
model_list:
-model_name: veo-3
litellm_params:
model: gemini/veo-3.0-generate-preview
api_key: os.environ/GEMINI_API_KEY
```

Start the proxy:

```
litellm --config config.yaml
# Server running on http://0.0.0.0:4000
```

### Making Requests[​](#making-requests "Direct link to Making Requests")

- Curl
- Python SDK

```
# Step 1: Generate video
curl --location 'http://0.0.0.0:4000/v1/videos' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer sk-1234' \
--data '{
    "model": "veo-3",
    "prompt": "A cat playing with a ball of yarn in a sunny garden"
}'

# Response: {"id": "gemini::operations/generate_12345::...", "status": "processing", ...}

# Step 2: Check status
curl --location 'http://localhost:4000/v1/videos/{video_id}' \
--header 'x-litellm-api-key: sk-1234'

# Step 3: Download video (when status is "completed")
curl --location 'http://localhost:4000/v1/videos/{video_id}/content' \
--header 'x-litellm-api-key: sk-1234' \
--output video.mp4
```

## Cost Tracking[​](#cost-tracking "Direct link to Cost Tracking")

LiteLLM automatically tracks costs for Veo video generation:

```
response = litellm.video_generation(
    model="gemini/veo-3.0-generate-preview",
    prompt="A beautiful sunset"
)

# Cost is calculated based on video duration
# Veo pricing: ~$0.10 per second (estimated)
# Default video duration: ~5 seconds
# Estimated cost: ~$0.50
```

## Differences from OpenAI Video API[​](#differences-from-openai-video-api "Direct link to Differences from OpenAI Video API")

FeatureOpenAI (Sora)Gemini (Veo)Reference Images✅ Supported❌ Not supportedSize Control✅ Supported❌ Not supportedDuration Control✅ Supported❌ Not supportedVideo Remix/Edit✅ Supported❌ Not supportedVideo List✅ Supported❌ Not supportedPrompt-based Generation✅ Supported✅ SupportedAsync Operations✅ Supported✅ Supported

## Error Handling[​](#error-handling "Direct link to Error Handling")

```
from litellm import video_generation, video_status, video_content
from litellm.exceptions import APIError, Timeout

try:
    response = video_generation(
        model="gemini/veo-3.0-generate-preview",
        prompt="A beautiful landscape"
)

# Poll with timeout
    max_attempts =60# 10 minutes (60 * 10s)
for attempt inrange(max_attempts):
        status = video_status(video_id=response.id)

if status.status =="completed":
            video_bytes = video_content(video_id=response.id)
withopen("video.mp4","wb")as f:
                f.write(video_bytes)
break
elif status.status =="failed":
raise APIError("Video generation failed")

        time.sleep(10)
else:
raise Timeout("Video generation timed out")

except APIError as e:
print(f"API Error: {e}")
except Timeout as e:
print(f"Timeout: {e}")
except Exception as e:
print(f"Unexpected error: {e}")
```

## Best Practices[​](#best-practices "Direct link to Best Practices")

1. **Always poll for completion**: Veo video generation is asynchronous and can take several minutes
2. **Set reasonable timeouts**: Allow at least 5-10 minutes for video generation
3. **Handle failures gracefully**: Check for `failed` status and implement retry logic
4. **Use descriptive prompts**: More detailed prompts generally produce better results
5. **Store video IDs**: Save the operation ID/video ID to resume polling if your application restarts

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### Video generation times out[​](#video-generation-times-out "Direct link to Video generation times out")

```
# Increase polling timeout
max_wait_time =900# 15 minutes instead of 10
```

### Video not found when downloading[​](#video-not-found-when-downloading "Direct link to Video not found when downloading")

```
# Make sure video is completed before downloading
status = video_status(video_id=video_id)
if status.status !="completed":
print("Video not ready yet!")
```

### API key errors[​](#api-key-errors "Direct link to API key errors")

```
# Verify your API key is set
import os
print(os.environ.get("GEMINI_API_KEY"))

# Or pass it explicitly
response = video_generation(
    model="gemini/veo-3.0-generate-preview",
    prompt="...",
    api_key="your-api-key-here"
)
```

## See Also[​](#see-also "Direct link to See Also")

- [OpenAI Video Generation](https://docs.litellm.ai/docs/providers/openai/videos)
- [Azure Video Generation](https://docs.litellm.ai/docs/providers/azure/videos)
- [Vertex AI Video Generation](https://docs.litellm.ai/docs/providers/vertex_ai/videos)
- [Video Generation API Reference](https://docs.litellm.ai/docs/videos)
- [Veo Pass-through Endpoints](https://docs.litellm.ai/docs/pass_through/google_ai_studio#example-4-video-generation-with-veo)