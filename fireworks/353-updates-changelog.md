---
title: Changelog
url: https://docs.fireworks.ai/updates/changelog
source: sitemap
fetched_at: 2026-04-27T20:12:39.092944129-03:00
rendered_js: false
word_count: 38
summary: This document provides JSON examples demonstrating conversational exchanges between a system assistant and a user, illustrating how dialogue turns are structured within message objects.
tags:
    - json-messages
    - chat-interaction
    - dialogue-flow
    - system-response
    - user-prompting
category: reference
optimized: true
optimized_at: 2026-04-27T20:12:39.092944129-03:00
---
# Changelog

> [!warning] Missing Content
> This document appears to contain example JSON code rather than actual changelog entries. The changelog may not have been properly populated or this page needs to be updated.

```json
{
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"}, 
    {"role": "assistant", "content": "Paris.", "reasoning_content": "The user is asking about the capital city of France, it should be Paris."}
  ]
}
{
  "messages": [
    {"role": "user", "content": "What is 1+1?"},
    {"role": "assistant", "content": "2", "weight": 0, "reasoning_content": "The user is asking about the result of 1+1, the answer is 2."},
    {"role": "user", "content": "Now what is 2+2?"},
    {"role": "assistant", "content": "4", "reasoning_content": "The user is asking about the result of 2+2, the answer should be 4."}
  ]
}
```

#changelog #api-reference #updates
