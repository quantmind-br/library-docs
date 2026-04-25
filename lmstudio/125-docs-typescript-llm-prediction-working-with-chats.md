---
title: Working with Chats
url: https://lmstudio.ai/docs/typescript/llm-prediction/working-with-chats
source: sitemap
fetched_at: 2026-04-07T21:31:42.558816752-03:00
rendered_js: false
word_count: 160
summary: This document outlines three different methods for passing chat context when calling SDK methods, including using an array of messages, providing a single string, or employing the recommended `Chat` helper class.
tags:
    - sdk-methods
    - chat-context
    - message-history
    - api-input
    - programming-guide
category: guide
---

SDK methods such as `model.respond()`, `model.applyPromptTemplate()`, or `model.act()` takes in a chat parameter as an input. There are a few ways to represent a chat in the SDK.

## Option 1: Array of Messages[](#option-1-array-of-messages "Link to 'Option 1: Array of Messages'")

You can use an array of messages to represent a chat. Here is an example with the `.respond()` method.

## Option 2: Input a Single String[](#option-2-input-a-single-string "Link to 'Option 2: Input a Single String'")

If your chat only has one single user message, you can use a single string to represent the chat. Here is an example with the `.respond` method.

## Option 3: Using the `Chat` Helper Class[](#option-3-using-the-chat-helper-class "Link to 'Option 3: Using the ,[object Object], Helper Class'")

For more complex tasks, it is recommended to use the `Chat` helper classes. It provides various commonly used methods to manage the chat. Here is an example with the `Chat` class.

You can also quickly construct a `Chat` object using the `Chat.from` method.