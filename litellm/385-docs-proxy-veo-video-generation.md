---
title: Veo Video Generation with Google AI Studio | liteLLM
url: https://docs.litellm.ai/docs/proxy/veo_video_generation
source: sitemap
fetched_at: 2026-01-21T19:54:05.386984562-03:00
rendered_js: false
word_count: 0
summary: This document provides a Python script demonstrating the workflow for generating videos with the Gemini Veo 3.0 model via a LiteLLM proxy, including polling and downloading.
tags:
    - python
    - video-generation
    - gemini-api
    - litellm
    - rest-api
    - asynchronous-processing
category: tutorial
---

```
import requests
import time
import json

# Configuration
BASE_URL ="http://localhost:4000/gemini/v1beta"
API_KEY ="anything"# Use "anything" as the key

headers ={
"x-goog-api-key": API_KEY,
"Content-Type":"application/json"
}

# Step 1: Initiate video generation
defgenerate_video(prompt):
    url =f"{BASE_URL}/models/veo-3.0-generate-preview:predictLongRunning"
    payload ={
"instances":[{
"prompt": prompt
}]
}

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()

    data = response.json()
return data.get("name")# Operation name

# Step 2: Poll for completion
defwait_for_completion(operation_name):
    operation_url =f"{BASE_URL}/{operation_name}"

whileTrue:
        response = requests.get(operation_url, headers=headers)
        response.raise_for_status()

        data = response.json()

if data.get("done",False):
# Extract video URI
            video_uri = data["response"]["generateVideoResponse"]["generatedSamples"][0]["video"]["uri"]
return video_uri

        time.sleep(10)# Wait 10 seconds before next poll

# Step 3: Download video
defdownload_video(video_uri, filename="generated_video.mp4"):
# Replace Google URL with LiteLLM proxy URL
    litellm_url = video_uri.replace(
"https://generativelanguage.googleapis.com/v1beta",
        BASE_URL
)

    response = requests.get(litellm_url, headers=headers, stream=True)
    response.raise_for_status()

withopen(filename,'wb')as f:
for chunk in response.iter_content(chunk_size=8192):
if chunk:
                f.write(chunk)

return filename

# Complete workflow
prompt ="A cat playing with a ball of yarn in a sunny garden"

print("Generating video...")
operation_name = generate_video(prompt)

print("Waiting for completion...")
video_uri = wait_for_completion(operation_name)

print("Downloading video...")
filename = download_video(video_uri)

print(f"Video saved as: {filename}")
```