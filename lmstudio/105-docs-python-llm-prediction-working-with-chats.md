---
title: Working with Chats
url: https://lmstudio.ai/docs/python/llm-prediction/working-with-chats
source: sitemap
fetched_at: 2026-04-07T21:31:14.666321989-03:00
rendered_js: false
word_count: 193
summary: This document explains the different methods for supplying chat input parameters to SDK methods like llm.respond(), detailing options including using a single string for simple chats, utilizing the recommended Chat helper class for complexity, and passing chat history data directly as a dictionary.
tags:
    - sdk-methods
    - chat-input
    - chat-history
    - string-array
    - helper-class
category: guide
---

SDK methods such as `llm.respond()`, `llm.applyPromptTemplate()`, or `llm.act()` take in a chat parameter as an input. There are a few ways to represent a chat when using the SDK.

## Option 1: Input a Single String[](#option-1-input-a-single-string "Link to 'Option 1: Input a Single String'")

If your chat only has one single user message, you can use a single string to represent the chat. Here is an example with the `.respond` method.

## Option 2: Using the `Chat` Helper Class[](#option-2-using-the-chat-helper-class "Link to 'Option 2: Using the ,[object Object], Helper Class'")

For more complex tasks, it is recommended to use the `Chat` helper class. It provides various commonly used methods to manage the chat. Here is an example with the `Chat` class, where the initial system prompt is supplied when initializing the chat instance, and then the initial user message is added via the corresponding method call.

You can also quickly construct a `Chat` object using the `Chat.from_history` method.

## Option 3: Providing Chat History Data Directly[](#option-3-providing-chat-history-data-directly "Link to 'Option 3: Providing Chat History Data Directly'")

As the APIs that accept chat histories use `Chat.from_history` internally, they also accept the chat history data format as a regular dictionary: