---
title: RunwayML - Video Generation | liteLLM
url: https://docs.litellm.ai/docs/providers/runwayml/videos
source: sitemap
fetched_at: 2026-01-21T19:50:22.359985572-03:00
rendered_js: false
word_count: 150
summary: This document provides a comprehensive guide on using LiteLLM to generate videos via the RunwayML Gen-4 API, covering text-to-video, image-to-video, and status polling workflows.
tags:
    - litellm
    - runwayml
    - video-generation
    - python-sdk
    - api-integration
    - async-programming
    - cost-tracking
category: guide
---

LiteLLM supports RunwayML's Gen-4 video generation API, allowing you to generate videos from text prompts and images.

## Quick Start[​](#quick-start "Direct link to Quick Start")

Basic Video Generation

```
from litellm import video_generation
import os

os.environ["RUNWAYML_API_KEY"]="your-api-key"

# Generate video from text and image
response = video_generation(
    model="runwayml/gen4_turbo",
    prompt="A high quality demo video of litellm ai gateway",
    input_reference="https://media.licdn.com/dms/image/v2/D4D0BAQFqOrIAJEgtLw/company-logo_200_200/company-logo_200_200/0/1714076049190/berri_ai_logo?e=2147483647&v=beta&t=7tG_KRZZ4MPGc7Iin79PcFcrpvf5Hu6rBM4ptHGU1DY",
    seconds=5,
    size="1280x720"
)

print(f"Video ID: {response.id}")
print(f"Status: {response.status}")
```

## Authentication[​](#authentication "Direct link to Authentication")

Set your RunwayML API key:

Set API Key

```
import os

os.environ["RUNWAYML_API_KEY"]="your-api-key"
```

## Supported Parameters[​](#supported-parameters "Direct link to Supported Parameters")

ParameterTypeRequiredDescription`model`stringYesModel to use (e.g., `runwayml/gen4_turbo`)`prompt`stringYesText description for the video`input_reference`string/fileYesURL or file path to reference image`seconds`intNoVideo duration (5 or 10 seconds)`size`stringNoVideo dimensions (`1280x720` or `720x1280`). Can also use `ratio` format (`1280:720`)

## Complete Workflow[​](#complete-workflow "Direct link to Complete Workflow")

Complete Video Generation Workflow

```
from litellm import video_generation, video_status, video_content
import os
import time

os.environ["RUNWAYML_API_KEY"]="your-api-key"

# 1. Generate video
response = video_generation(
    model="runwayml/gen4_turbo",
    prompt="A high quality demo video of litellm ai gateway",
    input_reference="https://media.licdn.com/dms/image/v2/D4D0BAQFqOrIAJEgtLw/company-logo_200_200/company-logo_200_200/0/1714076049190/berri_ai_logo?e=2147483647&v=beta&t=7tG_KRZZ4MPGc7Iin79PcFcrpvf5Hu6rBM4ptHGU1DY",
    seconds=5,
    size="1280x720"
)

video_id = response.id
print(f"Video generation started: {video_id}")

# 2. Check status until completed
whileTrue:
    status_response = video_status(video_id=video_id)
print(f"Status: {status_response.status}")

if status_response.status =="completed":
print("Video generation completed!")
break
elif status_response.status =="failed":
print("Video generation failed")
break

    time.sleep(10)# Wait 10 seconds before checking again

# 3. Download video content
video_bytes = video_content(video_id=video_id)

# 4. Save to file
withopen("generated_video.mp4","wb")as f:
    f.write(video_bytes)

print("Video saved successfully!")
```

## Async Usage[​](#async-usage "Direct link to Async Usage")

Async Video Generation

```
from litellm import avideo_generation, avideo_status, avideo_content
import os
import asyncio

os.environ["RUNWAYML_API_KEY"]="your-api-key"

asyncdefgenerate_video():
# Generate video
    response =await avideo_generation(
        model="runwayml/gen4_turbo",
        prompt="A serene lake with mountains in the background",
        input_reference="https://example.com/lake.jpg",
        seconds=5,
        size="1280x720"
)

    video_id = response.id
print(f"Video generation started: {video_id}")

# Poll for completion
whileTrue:
        status_response =await avideo_status(video_id=video_id)
print(f"Status: {status_response.status}")

if status_response.status =="completed":
break
elif status_response.status =="failed":
print("Video generation failed")
return

await asyncio.sleep(10)

# Download video
    video_bytes =await avideo_content(video_id=video_id)

# Save to file
withopen("generated_video.mp4","wb")as f:
        f.write(video_bytes)

print("Video saved successfully!")

asyncio.run(generate_video())
```

## LiteLLM Proxy Usage[​](#litellm-proxy-usage "Direct link to LiteLLM Proxy Usage")

Add RunwayML to your proxy configuration:

config.yaml

```
model_list:
-model_name: gen4-turbo
litellm_params:
model: runwayml/gen4_turbo
api_key: os.environ/RUNWAYML_API_KEY
```

Start the proxy:

```
litellm --config /path/to/config.yaml
```

Generate videos through the proxy:

Proxy Request

```
curl --location 'http://localhost:4000/v1/videos' \
--header 'Content-Type: application/json' \
--header 'x-litellm-api-key: sk-1234' \
--data '{
    "model": "runwayml/gen4_turbo",
    "prompt": "A high quality demo video of litellm ai gateway",
    "input_reference": "https://media.licdn.com/dms/image/v2/D4D0BAQFqOrIAJEgtLw/company-logo_200_200/company-logo_200_200/0/1714076049190/berri_ai_logo?e=2147483647&v=beta&t=7tG_KRZZ4MPGc7Iin79PcFcrpvf5Hu6rBM4ptHGU1DY",
    "ratio": "1280:720"
}'
```

Check video status:

Check Status

```
curl --location 'http://localhost:4000/v1/videos/{video_id}' \
--header 'x-litellm-api-key: sk-1234'
```

Download video content:

Download Video

```
curl --location 'http://localhost:4000/v1/videos/{video_id}/content' \
--header 'x-litellm-api-key: sk-1234' \
--output video.mp4
```

## Supported Models[​](#supported-models "Direct link to Supported Models")

ModelDescriptionDurationAspect Ratios`runwayml/gen4_turbo`Fast video generation5-10s1280x720, 720x1280

## Error Handling[​](#error-handling "Direct link to Error Handling")

Error Handling

```
from litellm import video_generation, video_status
import time

try:
    response = video_generation(
        model="runwayml/gen4_turbo",
        prompt="A scenic mountain view",
        input_reference="https://example.com/mountain.jpg",
        seconds=5
)

# Poll for completion
    max_attempts =60# 10 minutes max
    attempts =0

while attempts < max_attempts:
        status_response = video_status(video_id=response.id)

if status_response.status =="completed":
print("Video generation completed!")
break
elif status_response.status =="failed":
            error = status_response.error or{}
print(f"Video generation failed: {error.get('message','Unknown error')}")
break

        time.sleep(10)
        attempts +=1

if attempts >= max_attempts:
print("Video generation timed out")

except Exception as e:
print(f"Error: {str(e)}")
```

## Cost Tracking[​](#cost-tracking "Direct link to Cost Tracking")

LiteLLM automatically tracks RunwayML video generation costs:

Cost Tracking

```
from litellm import video_generation, completion_cost

response = video_generation(
    model="runwayml/gen4_turbo",
    prompt="A high quality demo video of litellm ai gateway",
    input_reference="https://media.licdn.com/dms/image/v2/D4D0BAQFqOrIAJEgtLw/company-logo_200_200/company-logo_200_200/0/1714076049190/berri_ai_logo?e=2147483647&v=beta&t=7tG_KRZZ4MPGc7Iin79PcFcrpvf5Hu6rBM4ptHGU1DY",
    seconds=5,
    size="1280x720"
)

# Calculate cost
cost = completion_cost(completion_response=response)
print(f"Video generation cost: ${cost}")
```

## API Reference[​](#api-reference "Direct link to API Reference")

For complete API details, see the [OpenAI Video Generation API specification](https://platform.openai.com/docs/guides/video-generation) which LiteLLM follows.

## Supported Features[​](#supported-features "Direct link to Supported Features")

FeatureSupportedVideo Generation✅Image-to-Video✅Status Checking✅Content Download✅Cost Tracking✅Logging✅Fallbacks✅Load Balancing✅