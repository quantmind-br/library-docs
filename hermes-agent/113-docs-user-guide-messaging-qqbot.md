---
title: QQ Bot | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot
source: crawler
fetched_at: 2026-04-24T17:00:16.247488243-03:00
rendered_js: false
word_count: 35
summary: This document provides instructions and a YAML configuration template for connecting the Hermes platform to the Official QQ Bot API (v2), detailing various supported communication modes like private, group, guild, and direct messaging.
tags:
    - hermes-qq
    - bot-api
    - configuration
    - qq-integration
    - chat-messaging
    - voice-transcription
category: guide
---

Connect Hermes to QQ via the **Official QQ Bot API (v2)** — supporting private (C2C), group @-mentions, guild, and direct messages with voice transcription.

Select **QQ Bot** from the platform list and follow the prompts.

```yaml
platforms:
qq:
enabled:true
extra:
app_id:"your-app-id"
client_secret:"your-secret"
markdown_support:true# enable QQ markdown (msg_type 2). Config-only; no env-var equivalent.
dm_policy:"open"# open | allowlist | disabled
allow_from:
-"user_openid_1"
group_policy:"open"# open | allowlist | disabled
group_allow_from:
-"group_openid_1"
stt:
provider:"zai"# zai (GLM-ASR), openai (Whisper), etc.
baseUrl:"https://open.bigmodel.cn/api/coding/paas/v4"
apiKey:"your-stt-key"
model:"glm-asr"
```