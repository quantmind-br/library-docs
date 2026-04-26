---
title: Libraries | Mistral Docs
url: https://docs.mistral.ai/le-chat/knowledge-integrations/libraries
source: sitemap
fetched_at: 2026-04-26T04:07:59.387096632-03:00
rendered_js: false
word_count: 932
summary: This document explains how to create, manage, and share persistent knowledge bases in Le Chat using Libraries, which allow users to query uploaded documents and web pages across multiple sessions.
tags:
    - knowledge-base
    - document-management
    - le-chat
    - ai-assistant
    - data-retrieval
    - collaboration
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Libraries

Libraries are **persistent knowledge bases** you build from your own documents and web pages. Attach a Library to any conversation and Le Chat **searches its contents in real time**, returning answers **based on your data** with direct references to the source material.

Unlike [file uploads](https://docs.mistral.ai/le-chat/research-analysis/files-upload), which last for a single conversation, Libraries persist across sessions. Upload once, use everywhere.

## Use Cases

- **Internal documentation**: upload your company handbook, IT policies, or HR guidelines.
- **Product specs and release notes**: keep technical specifications so product, sales, and support teams can reference the same source of truth.
- **Research and reports**: build a Library from industry reports, white papers, or academic articles.
- **Client or project knowledge**: create a Library per client or project with contracts, briefs, and meeting notes.
- **Onboarding material**: pair a Library with an [Agent](https://docs.mistral.ai/le-chat/knowledge-integrations/agents) to build a self-serve onboarding assistant.

## Creating a Library

1. Click the toggle panel button to open the sidebar.
2. Expand `Intelligence` and select `Libraries`.
3. Click `New Library`.
4. Give it a descriptive name.

### Uploading Documents

Drag and drop files into the Library, or click `Upload`. You can upload up to **100 files at once**, with a maximum file size of **100 MB per file**.

A status indicator shows processing progress. Most standard documents process in seconds to a couple of minutes.

### Adding Web Pages

1. Click `Webpage` in the Library view.
2. Enter one or more URLs.
3. Click `Index`.

> [!note]
> Only the text content of the page is indexed. Child pages, images, and charts aren't included.

Libraries accept the same formats as [file uploads](https://docs.mistral.ai/le-chat/research-analysis/files-upload).

## Using a Library

### Attaching to a Conversation

Click `+` then select `Libraries` and search for the Library of your choice. You can attach **multiple Libraries** to a single conversation.

### Querying Your Documents

Once attached, Le Chat searches across all documents to answer your questions:
- *"What does our refund policy say about international orders?"*
- *"Summarize the key findings from the Q2 market analysis."*
- *"Find all references to data retention in the compliance docs."*

To query a single document, click `+`, select `Upload Files`, choose your Library, and pick the specific document.

### Verifying Sources

Each response includes **numbered footnotes** linked to the original source material. Click a footnote to jump to the relevant passage. Click the `Sources` button at the bottom of the message to see every reference used.

## Sharing

By default, a new Library is **private**.

### Sharing with Specific People

1. Open the `Libraries` page.
2. Select the Library you want to share.
3. Click `Share` and search for users by name or email:
   - **Collaborator**: can use the Library, upload or delete documents, and modify settings.
   - **Viewer**: can use the Library but can't modify it.

### Sharing with Your Entire Organization

Toggle `Entire organization` and choose whether everyone gets Collaborator or Viewer access.

## Managing Libraries

- **Viewing documents**: open a Library and click any document. The right panel shows processed content and an auto-generated summary.
- **Downloading**: click `Download` in the panel or use the three-dots menu.
- **Renaming**: rename from the Library's settings.
- **Deleting**: delete from the `Libraries` page.

> [!warning]
> Deleting a Library is permanent. All documents inside are removed from our systems.

## Limits

| Limit | Value |
|-------|-------|
| Number of Libraries | Unlimited |
| Files per upload | Up to 100 |
| Maximum file size | 100 MB per file |

Each document uses processing capacity based on its size. Your monthly allowance resets automatically and is shared across all your Libraries. If you've reached your processing limit, new uploads are paused until the allowance resets.

## Privacy

- Documents are stored securely in our European cloud infrastructure.
- Storage lasts as long as the Library exists in an active account.
- Training policies depend on your plan. You can [opt out](https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training) at any time.

## Related

- [[142-le-chat-knowledge-integrations-agents|Agents]]: attach Libraries to Agents for specialized, knowledge-backed assistants.
- [[143-le-chat-knowledge-integrations-connectors|Connectors]]: connect external data sources like Google Drive, Notion, or GitHub.
- [[149-le-chat-knowledge-integrations-projects|Projects]]: organize conversations and share files at the Project level.

#knowledge-base #document-management #le-chat #ai-assistant #data-retrieval
