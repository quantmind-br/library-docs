---
title: RAG with Mistral AI and MongoDB - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-mongodb-mongodb_mistral
source: crawler
fetched_at: 2026-01-29T07:33:58.10136276-03:00
rendered_js: false
word_count: 542
---

Creating a LLM GenAI application integrates the power of Mistral AI with the robustness of an enterprise-grade vector store like MongoDB. Below is a detailed step-by-step guide to implementing this innovative system:

![MongoDB - Mistral](https://docs.mistral.ai/cookbooks/images/mongomistral5.jpg)

- Set `MISTRAL_API_KEY` and set up Subscription to activate it.
- Get `MONGO_URI` from MongoDB Atlas cluster.

## Import needed libraries

This section shows the versions of the required libraries. Personally, I run my code in VScode. So you need to install the following libraries beforehand. Here is the version at the moment I’m running the following code.

mistralai 0.0.8

pymongo 4.3.3

gradio 4.10.0

gradio\_client 0.7.3

langchain 0.0.348

langchain-core 0.0.12

pandas 2.0.3

These include libraries for data processing, web scraping, AI models, and database interactions.

You can use your API keys exported from shell commande.

## Data preparation

The data\_prep() function loads data from a PDF, a document, or a specified URL. It extracts text content from a webpage/documentation, removes unwanted elements, and then splits the data into manageable chunks. Once the data is chunked, we use the Mistral AI embedding endpoint to compute embeddings for every chunk and save them in the document. Afterward, each document is added to a MongoDB collection.

![MongoDB - Mistral](https://docs.mistral.ai/cookbooks/images/mongomistral1.jpg)

## Connecting to MongoDB server

The connect\_mongodb() function establishes a connection to a MongoDB server. It returns a collection object that can be used to interact with the database. This function will be called in the data\_prep() function. In order to get your MongoDB connection string, you can go to your MongoDB Atlas console, click the “Connect” button on your cluster, and choose the Python driver. ![MongoDB - Mistral](https://docs.mistral.ai/cookbooks/images/mongomistral2.jpg) ![MongoDB - Mistral](https://docs.mistral.ai/cookbooks/images/mongomistral3.jpg)

## Getting the embeddings

The get\_embedding(text) function generates an embedding for a given text. It replaces newline characters and then uses Mistral AI “La plateforme” embedding endpoints to get the embedding. This function will be called in both data preparation and question and answering processes.

## The last configuration on the MongoDB vector search index

In order to run a vector search query, you only need to create a vector search index in MongoDB Atlas as follows. (You can also learn more about how to create a vector search index [https://www.mongodb.com/docs/atlas/atlas-vector-search/vector-search-type/](https://www.mongodb.com/docs/atlas/atlas-vector-search/vector-search-type/) .)

## Finding similar documents

The find\_similar\_documents(embedding) function runs the vector search query in a MongoDB collection. This function will be called when the user asks a question. We will use this function to find similar documents to the questions in the question and answering process.

## Question and answer function

This function is the core of the program. It processes a user's question and creates a response using the context supplied by Mistral AI. Question and answer process This process involves several key steps. Here’s how it works: Firstly, we generate a numerical representation, called an embedding, through a Mistral AI embedding endpoint, for the user’s question. Next, we run a vector search in the MongoDB collection to identify the documents similar to the user’s question. It then constructs a contextual background by combining chunks of text from these similar documents. We prepare an assistant instruction by combining all this information. The user’s question and the assistant’s instruction are prepared into a prompt for the Mistral AI model. Finally, Mistral AI will generate responses to the user thanks to the retrieval-augmented generation process. ![MongoDB - Mistral](https://docs.mistral.ai/cookbooks/third_party/MongoDB/images/mongomistral4.jpg)