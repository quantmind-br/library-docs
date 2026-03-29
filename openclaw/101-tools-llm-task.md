---
title: Llm task - OpenClaw
url: https://docs.openclaw.ai/tools/llm-task
source: sitemap
fetched_at: 2026-01-30T20:21:34.9843794-03:00
rendered_js: false
word_count: 170
summary: This document explains how to configure and use the llm-task plugin for executing structured JSON-only LLM tasks with optional schema validation, particularly for workflow engines like Lobster.
tags:
    - llm-task
    - plugin
    - json-schema
    - workflow-engine
    - api-reference
    - configuration
category: reference
---

`llm-task` is an **optional plugin tool** that runs a JSON-only LLM task and returns structured output (optionally validated against JSON Schema). This is ideal for workflow engines like Lobster: you can add a single LLM step without writing custom OpenClaw code for each workflow.

## Enable the plugin

1. Enable the plugin:

```
{
  "plugins": {
    "entries": {
      "llm-task": { "enabled": true }
    }
  }
}
```

2. Allowlist the tool (it is registered with `optional: true`):

```
{
  "agents": {
    "list": [
      {
        "id": "main",
        "tools": { "allow": ["llm-task"] }
      }
    ]
  }
}
```

## Config (optional)

```
{
  "plugins": {
    "entries": {
      "llm-task": {
        "enabled": true,
        "config": {
          "defaultProvider": "openai-codex",
          "defaultModel": "gpt-5.2",
          "defaultAuthProfileId": "main",
          "allowedModels": ["openai-codex/gpt-5.2"],
          "maxTokens": 800,
          "timeoutMs": 30000
        }
      }
    }
  }
}
```

`allowedModels` is an allowlist of `provider/model` strings. If set, any request outside the list is rejected.

- `prompt` (string, required)
- `input` (any, optional)
- `schema` (object, optional JSON Schema)
- `provider` (string, optional)
- `model` (string, optional)
- `authProfileId` (string, optional)
- `temperature` (number, optional)
- `maxTokens` (number, optional)
- `timeoutMs` (number, optional)

## Output

Returns `details.json` containing the parsed JSON (and validates against `schema` when provided).

## Example: Lobster workflow step

```
openclaw.invoke --tool llm-task --action json --args-json '{
  "prompt": "Given the input email, return intent and draft.",
  "input": {
    "subject": "Hello",
    "body": "Can you help?"
  },
  "schema": {
    "type": "object",
    "properties": {
      "intent": { "type": "string" },
      "draft": { "type": "string" }
    },
    "required": ["intent", "draft"],
    "additionalProperties": false
  }
}'
```

## Safety notes

- The tool is **JSON-only** and instructs the model to output only JSON (no code fences, no commentary).
- No tools are exposed to the model for this run.
- Treat output as untrusted unless you validate with `schema`.
- Put approvals before any side-effecting step (send, post, exec).