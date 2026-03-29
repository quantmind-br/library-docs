---
title: Chat with your PDF using Mistral and Panel - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-panel-readme
source: crawler
fetched_at: 2026-01-29T07:34:09.259450847-03:00
rendered_js: false
word_count: 518
summary: This guide explains how to create a conversational AI interface using the Panel library and Mistral AI, including steps for implementing chat history and PDF-based retrieval-augmented generation.
tags:
    - panel-framework
    - mistral-ai
    - chatbot-ui
    - rag
    - pdf-reading
    - vector-store
    - python
category: guide
---

In this guide, we will introduce the basics of building a chatbot with chat and PDF reading capabilities using `panel`!

**Watch our demo by clicking this image:**

[![Panel Demo](https://img.youtube.com/vi/UpNxJ6wvS2A/0.jpg)](https://docs.mistral.ai/cookbooks/third_party-panel-readme)

## Basic Chat Interface

First, let's implement a simple chat interface. To do this, we will need to import the `panel` and `mistralai` libraries.

*This demo uses `panel===1.4.4` and `mistralai===0.4.0`*

Before proceeding, we must run `pn.extension()` to properly configure `panel`.

Next, create your `MistralClient` instance using your Mistral API key.

With the client ready, it's time to build the interface. For this, we will use the `ChatInterface` from `panel`!

In this code, we define a `callback` function that is called every time the user sends a message. This function uses Mistral's models to generate a response.

To run this code, enter `panel serve basic_chat.py` in the console.

## Chat History

Currently, the model only has access to the most recent message and does not know about the entire conversation.

To solve this, we need to keep track of the entire chat and provide it to the model. Fortunately, `panel` does this for us!

While we're at it, let's add a welcoming message for the user. We'll need to ignore this message in the callback.

We can now have a full conversation with Mistral: `panel serve chat_history.py`

## Chatting with PDFs

To enable our model to read PDFs, we need to convert the content, extract the text, and then use Mistral's embedding model to retrieve chunks of our document(s) to feed to the model. We will need to implement some basic RAG (Retrieval-Augmented Generation)!

For this task, we will require `faiss`, `PyPDF2`, and other libraries. Let's import them:

**For CPU only please install faiss-cpu instead.**

*This demo uses `numpy===1.26.4`, `PyPDF2===0.4.0` and `faiss-cpu===1.8.0`*

First, we need to add the option to upload files. For this, we will specify the possible inputs for our `ChatInterface`:

Now the user can both chat and upload a PDF file. Let's handle this new possibility in the callback:

In `pdf_objects`, we will have all previously uploaded PDFs, which will be the documents subject to the RAG.

Let's define a function that will handle all the RAG for us. This function will take the PDFs and the question being asked by the user as input and will return the retrieved chunks concatenated as a string:

But before continuing, we will need to get the embeddings for all the chunks. Let's quickly create a new function for this:

We can now apply the embeddings to the entirety of the chunks, and with `faiss`, we will make a vector store where we will search for the most relevant chunks. Here, we retrieve the best 4 chunks among them:

With our RAG function ready, we can implement it in the chat interface. For this, we will use `PyPDF2` to read the PDFs and then use our `rag_pdf` to retrieve the essential text:

If there are PDFs in the chat, it will read them and retrieve the necessary information, which will be concatenated to the original user message.

With this ready, we can now fully chat with Mistral and our PDFs: `panel serve chat_with_pdfs.py`