---
title: JSON Mode | Mistral Docs
url: https://docs.mistral.ai/capabilities/structured_output/json_mode
source: crawler
fetched_at: 2026-01-29T07:34:13.544870435-03:00
rendered_js: false
word_count: 94
---

Users have the option to set `response_format` to `{"type": "json_object"}` to enable JSON mode.

This mode ensures that the model's response is formatted as a valid JSON object regardless of the content of the prompt, however we still recommend to explicitly ask the model to return a JSON object and the format.

### How to generate JSON consistently

Below is an example of how to use JSON mode with the Mistral API.

The output will always be enforced to be valid JSON, and the `content` field will be a stringified JSON object. In this case: