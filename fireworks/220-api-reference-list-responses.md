---
title: List Responses - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/list-responses
source: sitemap
fetched_at: 2026-04-27T20:19:07.458992881-03:00
rendered_js: false
word_count: 0
summary: This document provides a structural representation of a response object containing data from an API call, outlining fields for status, model information, output messages, and various configuration parameters.
tags:
    - api-response
    - json-structure
    - data-object
    - message-format
    - configuration
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
```
{
  "data": [
    {
      "created_at": 123,
      "status": "<string>",
      "model": "<string>",
      "output": [
        {
          "id": "<string>",
          "role": "<string>",
          "content": [
            {
              "type": "<string>",
              "text": "<string>"
            }
          ],
          "status": "<string>",
          "type": "message"
        }
      ],
      "id": "<string>",
      "object": "response",
      "previous_response_id": "<string>",
      "usage": {},
      "error": {},
      "incomplete_details": {},
      "instructions": "<string>",
      "max_output_tokens": 123,
      "max_tool_calls": 2,
      "parallel_tool_calls": true,
      "reasoning": {},
      "store": true,
      "temperature": 1,
      "text": {},
      "tool_choice": "auto",
      "tools": [
        {}
      ],
      "top_p": 1,
      "truncation": "disabled",
      "user": "<string>",
      "metadata": {}
    }
  ],
  "has_more": true,
  "object": "list",
  "first_id": "<string>",
  "last_id": "<string>"
}
```
