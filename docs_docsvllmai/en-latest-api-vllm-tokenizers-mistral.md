---
title: mistral - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/tokenizers/mistral/
source: sitemap
fetched_at: 2026-05-07T21:35:44.864513742-03:00
rendered_js: false
word_count: 12
summary: This document describes a utility function that truncates tool call IDs to nine characters to ensure compatibility with Mistral's API requirements.
tags:
    - mistral-api
    - tool-calls
    - id-truncation
    - data-normalization
    - vllm-utils
category: api
---

Truncates tool call IDs for Mistral's ID requirements.

Source code in `vllm/tokenizers/mistral.py`

```
deftruncate_tool_call_ids(request: "MistralChatCompletionRequest"):
"""Truncates tool call IDs for Mistral's ID requirements."""
    for i, message in enumerate(request.messages):
        if message.get("role") == "assistant":
            tool_calls = message.get("tool_calls", [])
            for tool_call in tool_calls:
                if len(tool_call["id"]) > 9:
                    logger.warning(
                        "Truncating tool call ID: %s to %s",
                        tool_call["id"],
                        tool_call["id"][-9:],
                    )
                    tool_call["id"] = tool_call["id"][-9:]

            request.messages[i]["tool_calls"] = tool_calls

        elif message.get("role") in {"tool_results", "tool"}:
            if "tool_call_id" in message:
                tool_call_id = message["tool_call_id"]

                if len(tool_call_id) > 9:
                    logger.warning(
                        "Truncating tool_call_id: %s to %s",
                        tool_call_id,
                        tool_call_id[-9:],
                    )
                    tool_call_id = tool_call_id[-9:]
                request.messages[i]["tool_call_id"] = tool_call_id
```