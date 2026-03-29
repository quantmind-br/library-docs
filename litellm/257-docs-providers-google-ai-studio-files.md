---
title: '[BETA] Google AI Studio (Gemini) Files API | liteLLM'
url: https://docs.litellm.ai/docs/providers/google_ai_studio/files
source: sitemap
fetched_at: 2026-01-21T19:49:15.46696212-03:00
rendered_js: false
word_count: 0
summary: This document demonstrates how to upload audio files and perform multimodal completions using the LiteLLM library with the Gemini API.
tags:
    - litellm
    - gemini-api
    - audio-processing
    - multimodal
    - python-sdk
    - file-upload
category: tutorial
---

```
import base64
import requests
from litellm import completion, create_file
import os


### UPLOAD FILE ### 

# Fetch the audio file and convert it to a base64 encoded string
url ="https://cdn.openai.com/API/docs/audio/alloy.wav"
response = requests.get(url)
response.raise_for_status()
wav_data = response.content
encoded_string = base64.b64encode(wav_data).decode('utf-8')


file= create_file(
file=wav_data,
    purpose="user_data",
    extra_headers={"custom-llm-provider":"gemini"},
    api_key=os.getenv("GEMINI_API_KEY"),
)

print(f"file: {file}")

assertfileisnotNone


### GENERATE CONTENT ### 
completion = completion(
    model="gemini-2.0-flash",
    messages=[
{
"role":"user",
"content":[
{
"type":"text",
"text":"What is in this recording?"
},
{
"type":"file",
"file":{
"file_id":file.id,
"filename":"my-test-name",
"format":"audio/wav"
}
}
]
},
]
)

print(completion.choices[0].message)
```