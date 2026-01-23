---
title: Manus | liteLLM
url: https://docs.litellm.ai/docs/providers/manus
source: sitemap
fetched_at: 2026-01-21T19:49:37.255404468-03:00
rendered_js: false
word_count: 0
summary: This document demonstrates how to manage files and use them with the Manus provider through the LiteLLM library, covering file upload, retrieval, deletion, and integration with the responses API.
tags:
    - litellm
    - manus-ai
    - file-management
    - python
    - async-api
    - agentic-ai
category: tutorial
---

```
import litellm
import os

# Set API key
os.environ["MANUS_API_KEY"]="your-manus-api-key"

# Upload file
file_content =b"This is a document for analysis."
created_file =await litellm.acreate_file(
file=("document.txt", file_content),
    purpose="assistants",
    custom_llm_provider="manus",
)
print(f"Uploaded file: {created_file.id}")

# Use file with Responses API
response =await litellm.aresponses(
    model="manus/manus-1.6",
input=[
{
"role":"user",
"content":[
{"type":"input_text","text":"Summarize this document."},
{"type":"input_file","file_id": created_file.id},
],
},
],
    extra_body={"task_mode":"agent","agent_profile":"manus-1.6-agent"},
)
print(f"Response: {response.id}")

# Retrieve file
retrieved_file =await litellm.afile_retrieve(
    file_id=created_file.id,
    custom_llm_provider="manus",
)
print(f"File details: {retrieved_file.filename}, {retrieved_file.bytes} bytes")

# Delete file
deleted_file =await litellm.afile_delete(
    file_id=created_file.id,
    custom_llm_provider="manus",
)
print(f"Deleted: {deleted_file.deleted}")
```