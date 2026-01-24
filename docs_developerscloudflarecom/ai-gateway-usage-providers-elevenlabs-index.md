---
title: ElevenLabs · Cloudflare AI Gateway docs
url: https://developers.cloudflare.com/ai-gateway/usage/providers/elevenlabs/index.md
source: llms
fetched_at: 2026-01-24T14:03:12.704365302-03:00
rendered_js: false
word_count: 53
summary: This document provides instructions on how to use ElevenLabs text-to-speech services through Cloudflare AI Gateway, including endpoint configuration and authentication requirements.
tags:
    - elevenlabs
    - text-to-speech
    - ai-gateway
    - cloudflare
    - voice-synthesis
    - api-integration
category: api
---

[ElevenLabs](https://elevenlabs.io/) offers advanced text-to-speech services, enabling high-quality voice synthesis in multiple languages.

## Endpoint

```txt
https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/elevenlabs
```

## Prerequisites

When making requests to ElevenLabs, ensure you have the following:

* Your AI Gateway Account ID.
* Your AI Gateway gateway name.
* An active ElevenLabs API token.
* The model ID of the ElevenLabs voice model you want to use.

## Example

### cURL

```bash
curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/elevenlabs/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb?output_format=mp3_44100_128 \
  --header 'Content-Type: application/json' \
  --header 'xi-api-key: {elevenlabs_api_token}' \
  --data '{
    "text": "Welcome to Cloudflare - AI Gateway!",
    "model_id": "eleven_multilingual_v2"
}'
```