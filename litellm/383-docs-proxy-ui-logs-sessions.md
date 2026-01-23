---
title: Session Logs | liteLLM
url: https://docs.litellm.ai/docs/proxy/ui_logs_sessions
source: sitemap
fetched_at: 2026-01-21T19:53:56.474131806-03:00
rendered_js: false
word_count: 155
summary: This document explains how to group related API requests into sessions using session IDs or previous response IDs to track and link conversation history.
tags:
    - litellm
    - session-management
    - request-grouping
    - api-integration
    - python-sdk
category: guide
---

Group requests into sessions. This allows you to group related requests together.

## Usage[​](#usage "Direct link to Usage")

### `/chat/completions`[​](#chatcompletions "Direct link to chatcompletions")

To group multiple requests into a single session, pass the same `litellm_session_id` in the metadata for each request. Here's how to do it:

- OpenAI Python v1.0.0+
- Langchain
- Curl
- LiteLLM Python SDK

**Request 1** Create a new session with a unique ID and make the first request. The session ID will be used to track all related requests.

```
import openai
import uuid

# Create a session ID
session_id =str(uuid.uuid4())

client = openai.OpenAI(
    api_key="<your litellm api key>",
    base_url="http://0.0.0.0:4000"
)

# First request in session
response1 = client.chat.completions.create(
    model="gpt-4o",
    messages=[
{
"role":"user",
"content":"Write a short story about a robot"
}
],
    extra_body={
"litellm_session_id": session_id  # Pass the session ID
}
)
```

**Request 2** Make another request using the same session ID to link it with the previous request. This allows tracking related requests together.

```
# Second request using same session ID
response2 = client.chat.completions.create(
    model="gpt-4o",
    messages=[
{
"role":"user",
"content":"Now write a poem about that robot"
}
],
    extra_body={
"litellm_session_id": session_id  # Reuse the same session ID
}
)
```

### `/responses`[​](#responses "Direct link to responses")

For the `/responses` endpoint, use `previous_response_id` to group requests into a session. The `previous_response_id` is returned in the response of each request.

- OpenAI Python v1.0.0+
- Curl
- LiteLLM Python SDK

**Request 1** Make the initial request and store the response ID for linking follow-up requests.

```
from openai import OpenAI

client = OpenAI(
    api_key="<your litellm api key>",
    base_url="http://0.0.0.0:4000"
)

# First request in session
response1 = client.responses.create(
    model="anthropic/claude-3-sonnet-20240229-v1:0",
input="Write a short story about a robot"
)

# Store the response ID for the next request
response_id = response1.id
```

**Request 2** Make a follow-up request using the previous response ID to maintain the conversation context.

```
# Second request using previous response ID
response2 = client.responses.create(
    model="anthropic/claude-3-sonnet-20240229-v1:0",
input="Now write a poem about that robot",
    previous_response_id=response_id  # Link to previous request
)
```