---
title: AI · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/realtimekit/ai/index.md
source: llms
fetched_at: 2026-01-24T15:35:53.203648151-03:00
rendered_js: false
word_count: 94
summary: This document provides an overview of how to enable and configure AI-powered transcription and summarization features for meetings using RealtimeKit.
tags:
    - realtime-kit
    - ai-features
    - transcription
    - summarization
    - cloudflare-ai
    - data-retention
category: guide
---

RealtimeKit provides AI-powered features using Cloudflare's AI infrastructure to enhance your meetings with transcription and summarization capabilities.

* [Transcription](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/)
* [Summary](https://developers.cloudflare.com/realtime/realtimekit/ai/summary/)

## Available features

| Feature | Description |
| - | - |
| [Transcription](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/) | Real-time and post-meeting speech-to-text |
| [Summary](https://developers.cloudflare.com/realtime/realtimekit/ai/summary/) | AI-generated meeting summaries |

## Quick start

Enable AI features when creating a meeting:

```json
{
  "title": "Team Standup",
  "ai_config": {
    "transcription": {
      "language": "en-US"
    },
    "summarization": {
      "summary_type": "team_meeting"
    }
  },
  "summarize_on_end": true
}
```

Ensure participants have `transcription_enabled: true` in their [preset](https://developers.cloudflare.com/realtime/realtimekit/concepts/preset/).

## Storage and retention

* Transcripts and summaries are stored for **7 days** from meeting start
* Files are stored in R2 with presigned URLs for secure access
* Delivered via [webhooks](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/webhooks/) or REST API