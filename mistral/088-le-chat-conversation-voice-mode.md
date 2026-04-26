---
title: Voice mode | Mistral Docs
url: https://docs.mistral.ai/le-chat/conversation/voice-mode
source: sitemap
fetched_at: 2026-04-26T04:07:46.789883681-03:00
rendered_js: false
word_count: 310
summary: This document provides instructions on how to use Voice mode in Le Chat, including setup, configuration options, and data privacy policies.
tags:
    - voice-mode
    - speech-to-text
    - le-chat
    - transcription
    - audio-input
    - data-privacy
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Voice mode lets you chat with Le Chat using your voice instead of typing. Your speech is transcribed into text that you can review, edit, and send as a message.

Available on the web app and mobile apps ([iOS](https://apps.apple.com/us/app/le-chat-by-mistral-ai/id6740410176) and [Android](https://play.google.com/store/apps/details?id=ai.mistral.chat)) for all plans.

Voice mode is powered by [Voxtral](https://mistral.ai/news/voxtral-transcribe-2), Mistral's speech-to-text model for fast, accurate transcription across languages.

## How to Use

1. Click the **microphone icon** at the bottom right of the chat window.
2. Allow microphone access when prompted by your browser or device.
3. Speak naturally.

What happens next depends on the `Autosend` setting:

| Setting | Behavior |
|---------|----------|
| **Autosend ON** | Speech is transcribed and sent automatically — no manual step |
| **Autosend OFF** | Transcribed text appears in the message box; you can review, correct, attach tools, and click `Send` |

To discard a recording, click the cancel icon before sending.

> [!warning]
> If you previously denied microphone access, enable it in your browser's site settings or your device's app settings.

## Supported Languages

English, French, Spanish, German, Russian, Chinese, Japanese, Italian, Portuguese, Dutch, Arabic, Hindi, Korean.

## Data Privacy

How voice data is handled depends on your plan:

| Plan | Data Usage |
|------|------------|
| **Free, Pro, Student** | Voice messages may be used to improve models per data training policies. [Opt out](https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training) anytime. |
| **Team, Enterprise** | Voice messages aren't used for model training by default. Organization must explicitly opt in. |

## Troubleshooting

If your voice message wasn't transcribed correctly:
- **Speak clearly** and reduce background noise
- **Check microphone permissions** in your browser's site settings or device's app settings
- **Review and edit** the transcription in the message box before sending

## Related Features

- [**Chat**](https://docs.mistral.ai/le-chat/conversation/chat): the standard text-based conversation interface
- [**Libraries**](https://docs.mistral.ai/le-chat/knowledge-integrations/libraries): attach knowledge bases for context-aware responses
- [**Connectors**](https://docs.mistral.ai/le-chat/knowledge-integrations/connectors): connect external data sources

#voice-mode #speech-to-text #transcription