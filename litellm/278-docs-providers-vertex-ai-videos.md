---
title: Vertex AI Video Generation (Veo) | liteLLM
url: https://docs.litellm.ai/docs/providers/vertex_ai/videos
source: sitemap
fetched_at: 2026-01-21T19:50:38.922997437-03:00
rendered_js: false
word_count: 28
summary: This document provides instructions and code examples for integrating LiteLLM with Google Cloud's Vertex AI Veo models for video generation. It details authentication procedures, synchronous and asynchronous generation workflows, status polling, and retrieving generated video content.
tags:
    - litellm
    - vertex-ai
    - veo
    - video-generation
    - google-cloud-platform
    - python
    - asyncio
category: guide
---

LiteLLM supports Vertex AI's Veo video generation models using the unified OpenAI video API surface.

```
import json
import os

os.environ["VERTEXAI_PROJECT"]="your-gcp-project-id"
os.environ["VERTEXAI_LOCATION"]="us-central1"

# Option 1: Point to a service account file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/path/to/service_account.json"

# Option 2: Store the service account JSON directly
withopen("/path/to/service_account.json","r", encoding="utf-8")as f:
    os.environ["VERTEXAI_CREDENTIALS"]= f.read()
```

```
from litellm import video_generation, video_status, video_content
import json
import os
import time

withopen("/path/to/service_account.json","r", encoding="utf-8")as f:
    vertex_credentials = f.read()

response = video_generation(
    model="vertex_ai/veo-3.0-generate-preview",
    prompt="A cat playing with a ball of yarn in a sunny garden",
    vertex_project="your-gcp-project-id",
    vertex_location="us-central1",
    vertex_credentials=vertex_credentials,
    seconds="8",
    size="1280x720",
)

print(f"Video ID: {response.id}")
print(f"Initial Status: {response.status}")

# Poll for completion
whileTrue:
    status = video_status(
        video_id=response.id,
        vertex_project="your-gcp-project-id",
        vertex_location="us-central1",
        vertex_credentials=vertex_credentials,
)

print(f"Current Status: {status.status}")

if status.status =="completed":
break
if status.status =="failed":
raise RuntimeError("Video generation failed")

    time.sleep(10)

# Download the rendered video
video_bytes = video_content(
    video_id=response.id,
    vertex_project="your-gcp-project-id",
    vertex_location="us-central1",
    vertex_credentials=vertex_credentials,
)

withopen("generated_video.mp4","wb")as f:
    f.write(video_bytes)
```

```
from litellm import avideo_generation, avideo_status, avideo_content
import asyncio
import json

withopen("/path/to/service_account.json","r", encoding="utf-8")as f:
    vertex_credentials = f.read()


asyncdefworkflow():
    response =await avideo_generation(
        model="vertex_ai/veo-3.1-generate-preview",
        prompt="Slow motion water droplets splashing into a pool",
        seconds="10",
        vertex_project="your-gcp-project-id",
        vertex_location="us-central1",
        vertex_credentials=vertex_credentials,
)

whileTrue:
        status =await avideo_status(
            video_id=response.id,
            vertex_project="your-gcp-project-id",
            vertex_location="us-central1",
            vertex_credentials=vertex_credentials,
)

if status.status =="completed":
break
if status.status =="failed":
raise RuntimeError("Video generation failed")

await asyncio.sleep(10)

    video_bytes =await avideo_content(
        video_id=response.id,
        vertex_project="your-gcp-project-id",
        vertex_location="us-central1",
        vertex_credentials=vertex_credentials,
)

withopen("veo_water.mp4","wb")as f:
        f.write(video_bytes)

asyncio.run(workflow())
```

LiteLLM records the duration returned by Veo so you can apply duration-based pricing.

```
withopen("/path/to/service_account.json","r", encoding="utf-8")as f:
    vertex_credentials = f.read()

response = video_generation(
    model="vertex_ai/veo-2.0-generate-001",
    prompt="Flowers blooming in fast forward",
    seconds="5",
    vertex_project="your-gcp-project-id",
    vertex_location="us-central1",
    vertex_credentials=vertex_credentials,
)

print(response.usage)# {"duration_seconds": 5.0}
```