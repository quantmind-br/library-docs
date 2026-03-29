---
title: Building an LLM Agent to Find Relevant Research Papers from Arxiv - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-llamaindex-llamaindex_arxiv_agentic_rag_with_observability
source: crawler
fetched_at: 2026-01-29T07:33:50.165386043-03:00
rendered_js: false
word_count: 970
summary: A guide from the Mistral AI Cookbook demonstrating how to build an LLM-powered agent to search for and retrieve relevant research papers from the Arxiv database.
tags:
    - Mistral AI
    - LLM Agent
    - Arxiv
    - AI Research
    - Automation
category: guide
---

This notebook was created by Andrei Chernov ([Github](https://github.com/ChernovAndrey), [Linkedin](https://www.linkedin.com/in/andrei-chernov-58b157236/)) In this tutorial, we will create an LLM agent based on the **MistralAI** language model. The agent's primary purpose will be to find and summarize research papers from **Arxiv** that are relevant to the user's query. To build the agent, we will use the **LlamaIndex** framework.

## Tools Used by the Agent

The agent will utilize the following three tools:

1. **RAG Query Engine** This tool will store and retrieve recent papers from Arxiv, serving as a knowledge base for efficient and quick access to relevant information.
2. **Paper Fetch Tool** If the user specifies a topic that is not covered in the RAG Query Engine, this tool will fetch recent papers on the specified topic directly from Arxiv.
3. **PDF Download Tool** This tool allows the agent to download a research paper's PDF file locally using a link provided by Arxiv.

### First, let's install necessary libraries

### Additionally, You Need to Provide Your API Key to Access Mistral Models

You can obtain an API key [here](https://console.mistral.ai/api-keys/).

### To Build a RAG Query Engine, We Will Need an Embedding Model

For this tutorial, we will use the MistralAI embedding model.

### Now, We Will Download Recent Papers About Large Language Models from ArXiv

To keep this tutorial accessible with the free Mistral API version, we will download only the last 10 papers. Downloading more would exceed the limit later while building the RAG query engine. However, if you have a Mistral subscription, you can download additional papers.

### To Build a RAG Agent, We First Need to Index All Documents

This process creates a vector representation for each chunk of a document using the embedding model.

### Now, We Will Store the Index

Indexing a large number of texts can be time-consuming and costly since it requires making API calls to the embedding model. In real-world applications, it is better to store the index in a vector database to avoid reindexing. However, for simplicity, we will store the index locally in a directory in this tutorial, without using a vector database.

### We Are Ready to Build a RAG Query Engine for Our Agent

It is a good practice to provide a meaningful name and a clear description for each tool. This helps the agent select the most appropriate tool when needed.

### Let's Take a Look at the Prompts the RAG Tool Uses to Answer a Query Based on Context

Note that there are two prompts. By default, LlamaIndex uses a refine prompt before returning an answer. You can find more information about the response modes [here](https://docs.llamaindex.ai/en/v0.10.34/module_guides/deploying/query_engine/response_modes/).

### Building two other tools is straightforward because they are simply Python functions.

### Let's Chat with Our Agent

We built a ReAct agent, which operates in two main stages:

1. **Reasoning**: Upon receiving a query, the agent evaluates whether it has enough information to answer directly or if it needs to use a tool.
2. **Acting**: If the agent decides to use a tool, it executes the tool and then returns to the Reasoning stage to determine whether it can now answer the query or if further tool usage is necessary.

### The agent chose to use the RAG tool, found the relevant papers, and summarized them for us.

### Since the agent retains the chat history, we can request to download the papers without mentioning them explicitly.

### Let's see what happens if we ask about a topic that is not available in the RAG.

### As You Can See, the Agent Did Not Find the Papers in Storage and Fetched Them from ArXiv.

For a more detailed view of the agent's execution, check out your [Phoenix](https://app.phoenix.arize.com) dashboard.

## (Optional) Let's Trace and Evaluate the Agent

LlamaIndex has a built-in observability layer powered by Arize Phoenix. We can use this to trace the agent's execution and evaluate its performance.

If you don't have a Phoenix API key, you can get one [here](https://app.phoenix.arize.com/login/sign-up).

Now any calls we make to LlamaIndex will be traced and logged to your Phoenix instance.

Because we've just now turned on tracing, we'll need to run the agent again to see the trace data. Typically you would enable tracing earlier in the notebook to capture all the agent's execution.

Now if you go to your [Phoenix instance](https://app.phoenix.arize.com), you should see the trace data for the agent's execution.

## Evaluate the agent's performance

While it's easy to manually spot check the first few iterations of your agent's execution, it's not practical to do this for every iteration.

Let's add a more scalable way to evaluate the agent's performance.

There are infinite ways to evaluate the agent's performance. Let's look at two common ones:

1. Evaluating the agent's RAG skill
2. Evaluating the agent's function calling accuracy

We'll use an LLM as a Judge for both of these evaluations, with Mistral as our Judge.

### Evaluate the agent's RAG skill

With these three metrics calculated on our RAG skill, we can log them to Phoenix to view them alongside the trace data.

### Evaluate the agent's function calling accuracy

Now let's evaluate the agent's function calling accuracy, aka how often the agent uses the correct tool to answer a query.

Same as before, we'll start by retrieving the relevant trace data. In the previous section, we were able to use helper methods in the Phoenix SDK to retrieve the trace data. Here, we'll use the more general SpanQuery DSL to retrieve the trace data based on the filters we set.

We also need to pass in the tool definitions to the evaluator so it knows the possible tools available to the agent.

Now we're ready to run the evaluations. We'll use the `llm_classify` method to classify the tool calls as correct or incorrect.

And finally, we can log the evaluations to Phoenix to view them alongside the trace data.

Congratulations! You've now built an LLM agent with LlamaIndex and added evaluated it's performance using Phoenix.