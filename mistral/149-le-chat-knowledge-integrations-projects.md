---
title: Projects | Mistral Docs
url: https://docs.mistral.ai/le-chat/knowledge-integrations/projects
source: sitemap
fetched_at: 2026-04-26T04:08:03.315912667-03:00
rendered_js: false
word_count: 434
summary: This document explains how to organize conversations into Projects, manage their shared context and instructions, and handle the movement or deletion of chats within the platform.
tags:
    - project-management
    - conversation-organization
    - user-interface
    - custom-instructions
    - shared-context
    - chat-history
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Projects

Projects let you **group conversations** into distinct, manageable collections. Use them to keep client work, internal research, and product launches organized and easy to find.

Projects are available on all plans. Limits may apply. See our [pricing page](https://mistral.ai/pricing).

## Creating a Project

1. Click `New Project` next to the `Projects` header in the left sidebar.
2. Choose a name and an icon.
3. Click `Create`.

## Project Settings

Each Project can have its own instructions and shared context:

- **Instructions**: set a tone, define formatting rules, or provide domain-specific guidance. These apply to every conversation within the Project.
- **Additional context**: upload files shared across all chats in the Project. Every conversation can reference these files without re-uploading.
- **Cross-chat context**: include other chats from the Project as context.

> [!note]
> Adding a Library to a Project isn't supported yet. You can still attach Libraries to individual chats within the Project.

## Managing Chats

### Adding a Chat

**Drag and drop:**
1. Locate the chat in the sidebar.
2. Drag it over the target Project name and release.

**Folder icon:**
1. Open the chat.
2. Click the folder icon in the chat header.
3. Select a Project from the dropdown.

### Moving a Chat

Open the chat, click the folder icon, and select a different Project. The chat moves there automatically.

### Removing a Chat

**From the Project overview:**
1. Open the Project.
2. Click the three-dots menu on the chat card.
3. Select `Remove from project`.

**From the chat itself:**
1. Open the chat.
2. Click the folder icon.
3. Deselect the current Project.

> [!note]
> Removing a chat from a Project doesn't delete it. The chat stays in your main chat history and can be reassigned at any time. A chat can only belong to one Project at a time.

## Deleting a Project

1. Open the Project.
2. Click the three-dots menu in the top-right corner.
3. Select `Delete` and confirm.

> [!warning]
> Deleting a Project is permanent. The chats inside aren't deleted—they return to your main chat history.

## Related

- [[146-le-chat-knowledge-integrations-custom-instructions|Custom instructions]]: set persistent behavior rules across all your conversations.
- [[147-le-chat-knowledge-integrations-libraries|Libraries]]: build persistent knowledge bases from your own documents.
- [[142-le-chat-knowledge-integrations-agents|Agents]]: create specialized assistants with custom instructions and tools.

#project-management #conversation-organization #shared-context #chat-history
