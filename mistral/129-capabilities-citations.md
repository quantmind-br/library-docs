---
title: Citations & References | Mistral Docs
url: https://docs.mistral.ai/capabilities/citations
source: crawler
fetched_at: 2026-01-29T07:33:10.560966309-03:00
rendered_js: false
word_count: 362
summary: This document explains how to use citations and references to ground model responses in external data sources using tool calls and RAG workflows.
tags:
    - citations
    - references
    - rag
    - tool-calling
    - document-grounding
    - mistral-api
category: guide
---

Citations enable models to ground their responses and provide references, making them a powerful feature for Retrieval-Augmented Generation (RAG) and agentic applications. This feature allows the model to provide the source of the information extracted from a document or chunk of data from a tool call.

Our models have been deeply trained to ground on documents and provide sources, with a built-in feature to extract references and citations.

Before continuing, we recommend reading the [Chat Competions](https://docs.mistral.ai/capabilities/completion) documentation to learn more about the chat completions API and how to use it before proceeding.

### How to use Citations and References

To provide documents to the model, you can include the sources as a function call response.  
Below is an example of references, in this case from Wikipedia, using tool calls.

To use citations and references, you need to set up a tool call that will return the references.

**References Example**

Next, you need to define the tool that will be used to retrieve information from the external source. In this case, we will create a `get_information` tool that will return the references mentioned previously.

To get started, you need to initialize the client with your API key like usual.

## Set Up Chat History

You can set up the chat history with the initial user message and the optional system message.

You can make the initial chat request to the model with the chat history and the tool.

The model desires to call the `get_information` tool to retrieve the information from the external source.

Now, on our end we can handle the tool call and append the result to the chat history.

Finally, you can make the final chat request to the model with the updated chat history, providing the **original query**, the models **tool call** and the **tool result**.

As you can see, the model has provided the answer to the user's query and the reference to the source of the information.

You can extract and print these references from the response as you like.

You can find a comprehensive cookbook exploring Citations and References leveraging RAG with Wikipedia [here](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/rag/mistral-reference-rag.ipynb).  
This template will help get started with web search and document grounding with citations.