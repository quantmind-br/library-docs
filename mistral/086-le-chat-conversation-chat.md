---
title: Chat | Mistral Docs
url: https://docs.mistral.ai/le-chat/conversation/chat
source: sitemap
fetched_at: 2026-04-26T04:07:41.143110247-03:00
rendered_js: false
word_count: 576
summary: This document provides an overview of the Le Chat interface, explaining how to interact with the AI assistant, manage conversation context, use integrated tools, and share conversations with others.
tags:
    - ai-assistant
    - chat-interface
    - conversation-management
    - collaboration-tools
    - multilingual-support
    - user-guide
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

The chat interface is where you interact with Le Chat. Type a message, press `Enter`, and Le Chat responds immediately.

When Le Chat generates a response, it draws on **context** from:
- Your current message
- Full conversation history
- Enabled tools (e.g., [web search](https://docs.mistral.ai/le-chat/research-analysis/web-search), [Code Interpreter](https://docs.mistral.ai/le-chat/content-creation/code-interpreter))
- [Uploaded files](https://docs.mistral.ai/le-chat/research-analysis/files-upload)
- [Connectors](https://docs.mistral.ai/le-chat/knowledge-integrations/connectors)
- [Library](https://docs.mistral.ai/le-chat/knowledge-integrations/libraries) content
- [Memories](https://docs.mistral.ai/le-chat/knowledge-integrations/memories)
- [Custom instructions](https://docs.mistral.ai/le-chat/knowledge-integrations/custom-instructions)

The richer the context, the more accurate and tailored the response.

## Sending Messages

Type in the chat box and press `Enter` to send. Le Chat responds in real time.

Le Chat keeps context across messages, so you can build on previous exchanges without repeating yourself.

Click the `+` icon or type `/` to enable capabilities for the current conversation.

![Le Chat chat interface](https://docs.mistral.ai/img/chat_interface.png)

## Use Cases

- **Draft and review documents**: write reports, proposals, client emails
- **Translate business content**: translate contracts, correspondence, documentation between languages. Le Chat detects the source language automatically.
- **Analyze data and run calculations**: work through formulas, financial models. Use [Code Interpreter](https://docs.mistral.ai/le-chat/content-creation/code-interpreter) for verified accuracy.
- **Write and debug code**: generate new code, troubleshoot snippets, get code reviews with best-practice suggestions
- **Research and summarize**: explanations, competitive analysis, quick summaries

> [!tip]
> Be specific about the format and depth you need. *"Summarize this contract in three bullet points, in French"* gives better results than a vague prompt. See [prompting guide](https://docs.mistral.ai/models/best-practices/prompt-engineering).

## Multilingual Support

Le Chat detects the language of your message and responds in that same language. Change interface language in account settings — this doesn't affect the model's response language, which is driven by your prompt.

**Supported languages include:**
English, French, Spanish, German, Italian, Portuguese, Dutch, Russian, Chinese (Simplified and Traditional), Japanese, Arabic, Hindi, Turkish, Korean, Polish, Indonesian, Swedish, Danish, Norwegian, Finnish, Greek, Czech, Hungarian, Romanian, Thai, Vietnamese, Ukrainian.

## Share Conversations

1. Click the **Share** icon in the top-right corner.
2. Choose:
   - **Direct share**: X, LinkedIn, Reddit, WhatsApp, email
   - **Share by link**: generate a URL you can copy and send

Shared conversations display a **green dot indicator** next to the `Share` button.

### How Sharing Works

- Conversations are **private by default**
- Sharing creates a **read-only copy** at the time of sharing; messages added afterward won't appear
- Shared links can be revoked using the `Link accessible to anyone` toggle

## Related Features

- [**Memories**](https://docs.mistral.ai/le-chat/knowledge-integrations/memories): store persistent context across conversations
- [**Web search**](https://docs.mistral.ai/le-chat/research-analysis/web-search): get up-to-date information from the web
- [**Code Interpreter**](https://docs.mistral.ai/le-chat/content-creation/code-interpreter): run Python for calculations and charts
- [**Canvas**](https://docs.mistral.ai/le-chat/content-creation/canvas): create and edit documents in a side-by-side editor
- [**Libraries**](https://docs.mistral.ai/le-chat/knowledge-integrations/libraries): give Le Chat access to your uploaded documents

#ai-assistant #chat-interface #conversation-management