---
title: Amp Now Reads Threads
url: https://ampcode.com/news/read-threads
source: crawler
fetched_at: 2026-02-06T02:08:25.452558854-03:00
rendered_js: false
word_count: 190
summary: This document outlines how to use thread referencing in Amp to provide contextual information for AI agents through URLs, IDs, or the @ symbol. It details the process of using the read_thread tool to automatically extract relevant markdown from linked conversations.
tags:
    - amp-platform
    - thread-referencing
    - context-extraction
    - cli-tools
    - agentic-programming
category: guide
---

You can now reference threads in your messages, and Amp will fetch and extract the relevant context from them. For example:

- "Implement the plan we devised in [https://ampcode.com/threads/T-3f1beb2b-bded-4fda-96cc-1af7192f24b6](https://ampcode.com/threads/T-3f1beb2b-bded-4fda-96cc-1af7192f24b6)"
- "Do what we did in [https://ampcode.com/threads/T-f916b832-c070-4853-8ab8-5e7596953bec](https://ampcode.com/threads/T-f916b832-c070-4853-8ab8-5e7596953bec), but for the oracle tool"
- "Explain to me what my colleague Lily built in [https://ampcode.com/threads/T-330bd49a-2402-453c-bbf4-0c2f2ce7f2b9](https://ampcode.com/threads/T-330bd49a-2402-453c-bbf4-0c2f2ce7f2b9)"
- "Take the SQL queries from [https://ampcode.com/threads/T-95e73a95-f4fe-4f22-8d5c-6297467c97a5](https://ampcode.com/threads/T-95e73a95-f4fe-4f22-8d5c-6297467c97a5) and turn it into a reusable script I can run"
- "Figure out whether and how Keegan ended up using the function created in [https://ampcode.com/threads/T-e7ea6537-b3c6-4833-919c-45aa0af2d52f](https://ampcode.com/threads/T-e7ea6537-b3c6-4833-919c-45aa0af2d52f)"

To reference your own threads in the CLI and editor extensions, type `@` and the title of the thread you want to reference. For other threads to which you have access, such as workspace or public threads, simply paste the thread URL or the ID in your message.

Here's what that looks like in the Amp CLI:

Amp pulls in only what's needed using a new `read_thread` tool, which first fetches the thread as Markdown and then uses another model to extract the relevant context based on your instructions.

We think that threads as first-class entities — shareable, reusable, referenceable — has the potential to unlock new patterns for agentic programming.