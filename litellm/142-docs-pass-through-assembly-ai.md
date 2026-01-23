---
title: Assembly AI | liteLLM
url: https://docs.litellm.ai/docs/pass_through/assembly_ai
source: sitemap
fetched_at: 2026-01-21T19:46:47.972868614-03:00
rendered_js: false
word_count: 90
summary: This document explains how to use LiteLLM Proxy as a pass-through for Assembly AI endpoints, enabling features like cost tracking and logging while using the native Assembly AI SDK.
tags:
    - litellm
    - assembly-ai
    - api-proxy
    - pass-through
    - cost-tracking
    - logging
category: guide
---

Pass-through endpoints for Assembly AI - call Assembly AI endpoints, in native format (no translation).

FeatureSupportedNotesCost Tracking✅works across all integrationsLogging✅works across all integrations

Supports **ALL** Assembly AI Endpoints

[**See All Assembly AI Endpoints**](https://www.assemblyai.com/docs/api-reference)

## Quick Start[​](#quick-start "Direct link to Quick Start")

Let's call the Assembly AI [`/v2/transcripts` endpoint](https://www.assemblyai.com/docs/api-reference/transcripts)

1. Add Assembly AI API Key to your environment

```
export ASSEMBLYAI_API_KEY=""
```

2. Start LiteLLM Proxy

```
litellm

# RUNNING on http://0.0.0.0:4000
```

3. Test it!

Let's call the Assembly AI `/v2/transcripts` endpoint

```
import assemblyai as aai

LITELLM_VIRTUAL_KEY ="sk-1234"# <your-virtual-key>
LITELLM_PROXY_BASE_URL ="http://0.0.0.0:4000/assemblyai"# <your-proxy-base-url>/assemblyai

aai.settings.api_key =f"Bearer {LITELLM_VIRTUAL_KEY}"
aai.settings.base_url = LITELLM_PROXY_BASE_URL

# URL of the file to transcribe
FILE_URL ="https://assembly.ai/wildfires.mp3"

# You can also transcribe a local file by passing in a file path
# FILE_URL = './path/to/file.mp3'

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL)
print(transcript)
print(transcript.id)
```

## Calling Assembly AI EU endpoints[​](#calling-assembly-ai-eu-endpoints "Direct link to Calling Assembly AI EU endpoints")

If you want to send your request to the Assembly AI EU endpoint, you can do so by setting the `LITELLM_PROXY_BASE_URL` to `<your-proxy-base-url>/eu.assemblyai`

```
import assemblyai as aai

LITELLM_VIRTUAL_KEY ="sk-1234"# <your-virtual-key>
LITELLM_PROXY_BASE_URL ="http://0.0.0.0:4000/eu.assemblyai"# <your-proxy-base-url>/eu.assemblyai

aai.settings.api_key =f"Bearer {LITELLM_VIRTUAL_KEY}"
aai.settings.base_url = LITELLM_PROXY_BASE_URL

# URL of the file to transcribe
FILE_URL ="https://assembly.ai/wildfires.mp3"

# You can also transcribe a local file by passing in a file path
# FILE_URL = './path/to/file.mp3'

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL)
print(transcript)
print(transcript.id)
```