---
title: Web Search with References - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/mistral-rag-mistral-reference-rag
source: crawler
fetched_at: 2026-01-29T07:33:54.729182772-03:00
rendered_js: false
word_count: 748
---

## Introduction

The primary objective of this cookbook is to illustrate how to effectively use the lastest [Mistral Large 2](https://docs.mistral.ai/getting-started/models/models_overview/#premier-models) model to conduct **web searches** and incorporate relevant sources into your responses. A common challenge with chatbots and Retrieval-Augmented Generation (RAG) systems is their **tendency to hallucinate sources or improperly format URLs**. Mistral's advanced capabilities address these issues, ensuring accurate and reliable information retrieval.

## Mistral's Web Search Capabilities

The new Mistral model `mistral-large-latest` integrates web search capabilities, allowing it to **reference sources accurately in its responses**. This feature enables you to retrieve the source content and present it correctly in your responses, enhancing the reliability and credibility of the information provided. By leveraging Mistral's advanced natural language processing and web search integration, you can build more robust and trustworthy applications.

![image info](https://docs.mistral.ai/cookbooks/images/reference_rag.png)

Here is a step-by-step description of the process depicted in the image above:

1. **Query Initiation**: The process begins with a user query.
2. **Function Calling with Mistral Large**: The query is processed by the Mistral Large model, which identifies that it needs to perform a function call to gather more information. This step involves determining the appropriate tool to use for the query.
3. **Tool Identification**: The Mistral model identifies the relevant tool for the query, which in this case is `web_search_wikipedia`. The tool has the user query as an argument.
4. **Wikipedia Search**: The tool is called and performs a search on Wikipedia using the query.
5. **Extract Relevant Chunks**: The results from the Wikipedia search are processed to extract relevant chunks of information. These chunks are then prepared to be used as references in the final answer.
6. **Final Answer with References**: The chat history is sent to the Mistral Large model which uses the extracted chunks to generate a final answer. The answer includes references to the Wikipedia articles, ensuring that the information provided is accurate and well-sourced.

## Step 1: Initialize the Mistral client

In this step, we initialize the Mistral client with your API key. You can get or create your API key from the [Mistral API dashboard](https://console.mistral.ai/api-keys/). **Warning**: API Key can take up to 1 minute to be activated.

\[SystemMessage(content='You are a helpful assistant that can search the web for information. Use context to answer the question.', role='system'), UserMessage(content='Who won the Nobel Peace Prize in 2024?', role='user')]

## Step 2 : Define the function calling tool to search Wikipedia.

[Function calling](https://docs.mistral.ai/capabilities/function_calling/) allows Mistral models to connect to external tools. By integrating Mistral models with external tools such as user defined functions or APIs, users can easily build applications catering to specific use cases and practical problems.

First, we create a tool that will search the Wikipedia API and return the results in a specific format. Once we have the tool, we can use it in a chat completion request to Mistral. The result should contain:

- Name of the tool
- Tool call ID
- Arguments which contains the user query

function=FunctionCall(name='web\_search', arguments='{"query": "Who won the Nobel Peace Prize in 2024?"}') id='3xdgHbIKY' type='function'

## Step 3: Define Method to Search Wikipedia Associated with the Tool

In the previous step, we created a tool called `web_search_wikipedia`. We need to create a function that will take the tool call ID and the arguments and return the results in the specific format.

The format of the results should be:

## Step 4: Perform the Tool Call and Search Wikipedia

Now that we have the tool call ID and the arguments, we can perform the tool call and search Wikipedia.

## Step 5: Call Mistral with the Tool Call Result

The chat history now contains:

- The `System` message which contains the instructions for the assistant
- The `User` message which contains the original question
- The `Assistant` message which contains a tool call to search Wikipedia
- The `Tool call` result which contains the results of the Wikipedia search

See more information about types of messages [here](https://docs.mistral.ai/capabilities/completion/#chat-messages).

🤖 Answer:

The 2024 Nobel Peace Prize was awarded to Nihon Hidankyo, the Japan Confederation of A- and H-Bomb Sufferers Organizations, for their activism against nuclear weapons, supported by survivors of the 1945 atomic bombings of Hiroshima and Nagasaki. The award ceremony will take place on December 10, 2024, in Oslo, Norway.

📚 Sources:

1. 2024 Nobel Peace Prize : [https://en.wikipedia.org/wiki/2024\_Nobel\_Peace\_Prize](https://en.wikipedia.org/wiki/2024_Nobel_Peace_Prize)
2. Nobel Peace Prize: [https://en.wikipedia.org/wiki/Nobel\_Peace\_Prize](https://en.wikipedia.org/wiki/Nobel_Peace_Prize)

## Step 6 : Streaming completion with references

The 2024 Nobel Peace Prize was awarded to Nihon Hidankyo (the Japan Confederation of A- and H-Bomb Sufferers Organizations) for their activism against nuclear weapons, assisted by victim/survivors (known as Hibakusha) of the atomic bombings of Hiroshima and Nagasaki in 1945 [1](https://en.wikipedia.org/wiki/2024_Nobel_Peace_Prize), [2](https://en.wikipedia.org/wiki/Nobel_Peace_Prize).