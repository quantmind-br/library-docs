---
title: Computer Use | liteLLM
url: https://docs.litellm.ai/docs/completion/computer_use
source: sitemap
fetched_at: 2026-01-21T19:44:21.295804488-03:00
rendered_js: false
word_count: 51
summary: This document explains how to implement computer use capabilities via LiteLLM to enable AI models to interact with desktop environments through screenshots, bash commands, and text editing.
tags:
    - litellm
    - computer-use
    - tool-calling
    - automation
    - anthropic-claude
    - python
category: guide
---

Computer use allows models to interact with computer interfaces by taking screenshots and performing actions like clicking, typing, and scrolling. This enables AI models to autonomously operate desktop environments.

LiteLLM will standardize the computer use tools across all supported providers.

Computer use supports several different tool types for various interaction modes:

```
import os 
from litellm import completion

os.environ["ANTHROPIC_API_KEY"]="your-api-key"

tools =[
{
"type":"computer_20241022",
"name":"computer",
"display_height_px":768,
"display_width_px":1024,
"display_number":0,
},
{
"type":"bash_20241022",
"name":"bash"
},
{
"type":"text_editor_20250124",
"name":"str_replace_editor"
}
]

messages =[
{
"role":"user",
"content":[
{
"type":"text",
"text":"Take a screenshot, then create a file describing what you see, and finally use bash to show the file contents"
},
{
"type":"image_url",
"image_url":{
"url":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8/5+hHgAHggJ/PchI7wAAAABJRU5ErkJggg=="
}
}
]
}
]

response = completion(
    model="anthropic/claude-3-5-sonnet-latest",
            messages=messages,
            tools=tools,
)

print(response)
```