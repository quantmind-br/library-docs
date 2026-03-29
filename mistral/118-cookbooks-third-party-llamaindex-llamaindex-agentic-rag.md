---
title: Using Mistral AI with LlamaIndex - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-llamaindex-llamaindex_agentic_rag
source: crawler
fetched_at: 2026-01-29T07:34:04.835804554-03:00
rendered_js: false
word_count: 474
---

In this notebook we're going to show how you can use LlamaIndex with the Mistral API to perform complex queries over multiple documents including answering questions that require multiple documents simultaneously. We'll do this using a ReAct agent, an autonomous LLM-powered agent capable of using tools.

First we install our dependencies. We need LlamaIndex, Mistral, and a PDF parser for later.

Now we set up our connection to Mistral. We need two things:

1. An LLM, to answer questions
2. An embedding model, to convert our data into vectors for retrieval by our index. Luckily, Mistral provides both!

Once we have them, we put them into a ServiceContext, an object LlamaIndex uses to pass configuration around.

Now let's download our dataset, 3 very large PDFs containing Lyft's annual reports from 2020-2022.

Now we have our data, we're going to do three things:

1. Load the PDF data into memory. It will be parsed into text as we do this. That's the `load_data()` line.
2. Index the data. This will create a vector representation of each document. That's the `from_documents()` line. It stores the vectors in memory.
3. Set up a query engine to retrieve information from the vector store and pass it to the LLM. That's the `as_query_engine()` line.

We're going to do this once for each of the three documents. If we had more than 3 we would do this programmatically with a loop, but this keeps the code very simple if a little repetitive. We've included a query to one of the indexes at the end as a test.

Success! The 2022 index knows facts about 2022. We're almost ready to create our agent. Before we do, let's set up an array of tools for our agent to use. This turns each of the query engines we set up above into a tool, and indicates what each engine is best at answering questions about. The LLM will read these descriptions when deciding what tool to use.

Now we create our agent from the tools we've set up and we can ask it complicated questions. It will reason through the process step by step, creating simpler questions, and use different tools to answer them. Then it'll take the information it gathers from each tool and combine it into a single answer to the more complex question.

Cool! As you can see it got the 2022 profit from the 2022 10-K form and the 2020 data from the 2020 report. It took both those answers and combined them into the difference we asked for. Let's try another question, this time asking about textual answers rather than numbers:

Great! It correctly itemized the risks, noticed the differences, and summarized them.

You can try this on any number of documents with any number of query engines to answer really complex questions. You can even have the query engines themselves be agents.