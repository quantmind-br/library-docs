---
title: Using Anthropic File API with LiteLLM Proxy | liteLLM
url: https://docs.litellm.ai/docs/tutorials/anthropic_file_usage
source: sitemap
fetched_at: 2026-01-21T19:54:58.046170873-03:00
rendered_js: false
word_count: 55
summary: This tutorial explains how to upload files and perform data analysis using Claude-4 through the LiteLLM Proxy's Anthropic passthrough and chat completion endpoints.
tags:
    - litellm-proxy
    - anthropic-claude
    - file-management
    - data-analysis
    - api-passthrough
category: tutorial
---

## Overview[​](#overview "Direct link to Overview")

This tutorial shows how to create and analyze files with Claude-4 on Anthropic via LiteLLM Proxy.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

- LiteLLM Proxy running
- Anthropic API key

Add the following to your `.env` file:

```
ANTHROPIC_API_KEY=sk-1234
```

## Usage[​](#usage "Direct link to Usage")

### 1. Setup config.yaml[​](#1-setup-configyaml "Direct link to 1. Setup config.yaml")

```
model_list:
-model_name: claude-opus
litellm_params:
model: anthropic/claude-opus-4-20250514
api_key: os.environ/ANTHROPIC_API_KEY
```

## 2. Create a file[​](#2-create-a-file "Direct link to 2. Create a file")

Use the `/anthropic` passthrough endpoint to create a file.

```
curl -L -X POST 'http://0.0.0.0:4000/anthropic/v1/files' \
-H 'x-api-key: sk-1234' \
-H 'anthropic-version: 2023-06-01' \
-H 'anthropic-beta: files-api-2025-04-14' \
-F 'file=@"/path/to/your/file.csv"'
```

Expected response:

```
{
"created_at":"2023-11-07T05:31:56Z",
"downloadable":false,
"filename":"file.csv",
"id":"file-1234",
"mime_type":"text/csv",
"size_bytes":1,
"type":"file"
}
```

## 3. Analyze the file with Claude-4 via `/chat/completions`[​](#3-analyze-the-file-with-claude-4-via-chatcompletions "Direct link to 3-analyze-the-file-with-claude-4-via-chatcompletions")

```
curl -L -X POST 'http://0.0.0.0:4000/v1/chat/completions' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer $LITELLM_API_KEY' \
-d '{
    "model": "claude-opus",
    "messages": [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What is in this sheet?"},
                {
                    "type": "file",
                    "file": {
                        "file_id": "file-1234",
                        "format": "text/csv" # 👈 IMPORTANT: This is the format of the file you want to analyze
                    }
                }
            ]
        }
    ]
}'
```