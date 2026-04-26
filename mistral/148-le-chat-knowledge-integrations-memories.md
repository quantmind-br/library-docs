---
title: Memories | Mistral Docs
url: https://docs.mistral.ai/le-chat/knowledge-integrations/memories
source: sitemap
fetched_at: 2026-04-26T04:08:01.210947061-03:00
rendered_js: false
word_count: 457
summary: This document explains how the Memories feature in Le Chat functions, enabling the assistant to store and recall user preferences and context across conversations.
tags:
    - le-chat
    - personalization
    - user-preferences
    - data-privacy
    - ai-assistant
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Memories

Memories lets Le Chat **remember key details about you**—preferences, interests, and working context—based on your past interactions. Instead of repeating yourself every conversation, Memories keeps that information available so responses stay relevant and personalized.

## How Memories Work

Le Chat can save details in two ways:
- **Explicit saving**: ask Le Chat to save something specific (e.g., *"Remember that I prefer concise answers"*).
- **Automatic saving**: Le Chat may pick up useful details from your conversations on its own.

Saved Memories are recalled automatically when they're relevant to a new conversation.

> [!warning]
> Memories only stores information you've explicitly included in your prompts. Le Chat is designed not to remember sensitive data such as social security numbers or banking information.

## Enabling Memories

1. Click the `Enable Memories` button in the pop-up that appears the first time you log in, **or**
2. Open the `Memories` tab under the `Intelligence` menu, click three dots `...`, and toggle `Memories in Le Chat` on.

## Managing Memories

All your Memories appear in the `Memories` tab, listed newest to oldest:

| Action | How |
|--------|-----|
| **View** | Open the `Memories` tab |
| **Edit** | Click the pencil icon next to a memory |
| **Delete one** | Click the trash icon next to a memory |
| **Delete all** | Click `...`, select `Clear all Memories` |

You can also ask Le Chat to remove specific Memories (e.g., *"Forget that I mentioned my location"*).

## Disabling Memories

Open the `Memories` tab and toggle the Memories button off.

> [!warning]
> Turning off Memories doesn't automatically delete your stored Memories. Click `Clear all Memories` before deactivating if you want removal.

## Privacy

| Plan | Training |
|------|----------|
| **Free, Pro, Student** | Prompts with Memories may be used to train models. You can opt out in account settings. |
| **Team, Enterprise** | Opted out of model training by default. |

- Memories are private to your account and never shared with or sold to anyone.
- Memories are stored for the duration of your subscription.
- We don't use Memories data for advertising, ad profiles, or data selling.

## Related

- [[146-le-chat-knowledge-integrations-custom-instructions|Custom instructions]]: set persistent preferences that apply across all conversations.
- [[142-le-chat-knowledge-integrations-agents|Agents]]: build specialized assistants with their own instructions and knowledge.
- [[149-le-chat-knowledge-integrations-projects|Projects]]: organize conversations within scoped work areas.

#le-chat #personalization #user-preferences #data-privacy
