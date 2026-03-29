---
title: Building a Text-to-SQL conversion system with Mistral AI, Neon, and LangChain - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-neon-neon_text_to_sql
source: crawler
fetched_at: 2026-01-29T07:34:06.364713332-03:00
rendered_js: false
word_count: 1144
summary: This document explains how to build a text-to-SQL system using Retrieval Augmented Generation (RAG) to translate natural language into database queries. It demonstrates the integration of Mistral AI for embeddings, Neon Postgres for vector storage, and LangChain for orchestration.
tags:
    - text-to-sql
    - rag
    - mistral-ai
    - neon-postgres
    - langchain
    - vector-database
    - postgresql
category: tutorial
---

Translating natural language queries into SQL statements is a powerful application of large language models (LLMs). While it's possible to ask an LLM directly to generate SQL based on a natural language prompt, it comes with limitations.

1. The LLM may generate SQL that is syntactically incorrect since the SQL dialect varies across relational databases.
2. The LLM doesn't have access to the full database schema, table and column names or indexes, which limits its ability to generate accurate/efficient queries. Passing in the full schema as input to the LLM everytime can get expensive.
3. Pretrained LLMs can't adapt to user feedback and evolving text queries.

### Finetuning

An alternative is to finetune the LLM on your specific text-to-SQL dataset, which might includes query logs from your database and other relevant context. While this approach can improve the LLM's ability to generate accurate SQL queries, it still has limitations adapting continuously. Finetuning can also be expensive which might limit how frequently you can update the model.

### RAG systems

LLMs are great at in-context learning, so by feeding them relevant information in the prompt, we can improve their outputs. This is the idea behind Retrieval Augmented Generation (RAG) systems, which combine information retrieval with LLMs to generate more informed and contextual responses to queries.

By retrieving relevant information from a knowledge base - database schemas, which tables to query, and previously generated SQL queries, we can leverage LLMs to generate SQL queries that are more accurate and efficient.

### RAG for text-to-sql

In this post, we'll walk through building a RAG system using [Mistral AI](https://mistral.ai/) for embeddings and language modeling, [Neon Postgres](https://neon.tech/) for the vector database. `Neon` is a fully managed serverless PostgreSQL database. It separates storage and compute to offer features such as instant branching and automatic scaling. With the `pgvector` extension, Neon can be used as a vector database to store text embeddings and query them.

We'll set up a sample database, generate and store embeddings for a knowledge-base about it, and then retrieve relevant snippets to answer a query. We use the popular [LangChain](https://www.langchain.com/) library to tie it all together.

Let's dive in!

## Setup and Dependencies

### Mistral AI API

Sign up at [Mistral AI](https://mistral.ai/) and navigate to the console. From the sidebar, go to the `API keys` section and create a new API key.

You'll need this key to access Mistral AI's embedding and language models. Set the variable below to it.

### Neon Database

Sign up at [Neon](https://neon.tech/) if you don't already have an account. Your Neon project comes with a ready-to-use Postgres database named `neondb` which we'll use in this notebook.

Log in to the Neon Console and navigate to the Connection Details section to find your database connection string. It should look similar to this:

Set the variable below to the Neon connection string.

### Python Libraries

Install the necessary libraries to create the RAG system.

`langchain-postgres` provides a `vectorstore` module that allows us to store and query embeddings in a Postgres database with `pgvector` installed. While, we need `langchain-mistralai` to interact with `Mistral` models.

### Preparing the Data

For our example, we'll leverage the commonly used Northwind sample dataset. It models a fictional trading company called `Northwind Traders` that sells products to customers. It has tables representing entities such as `Customers`, `Orders`, `Products`, and `Employees`, interconnected through relationships, allowing users to query and analyze data related to sales, inventory and other business operations.

We want to provide two pieces of information as context when calling the Mistral LLM:

- Relevant tables/index information from the Northwind database schema
- Some sample (text-question, sql query) pairs for the LLM to learn from.

We will set up retrieval by leveraging a vector database to store the schema and the sample (text, sql) pairs. We create embeddings using the `mistral-embed` LLM model for each piece of information and at query time, retrieve the relevant snippets by comparing the query embedding with the stored embeddings.

We'll use the `langchain-postgres` library to store embeddings of the data in the database.

Next, we generate embeddings for the Northwind schema and sample queries.

The `add_documents` method on a langchain vector store, like `PGVector` here uses the specified embeddings model to generate embeddings for the input text and stores them in the database.

**NOTE**: If working in Colab, download the database setup and sample query scripts by running this

We will also create the Northwind tables in our Neon database, so we can execute the LLM output and have a working natural-language to query results pipeline.

### Retrieving Relevant Information

With our knowledge base set up, we can now retrieve relevant information for a given query.

Consider a user asking the query below.

We use the `similarity search` method on the vector store to retrieve the most similar snippets to the query.

We also fetch some similar queries from our example corpus to add to the LLM prompt. `Few shot` prompting by providing examples of the text-to-sql conversion task in this manner helps the LLM generate more relevant output.

### Generating the SQL output

Finally, we'll use Mistral AI's chat model to generate a SQL statement based on the retrieved context.

We first construct the prompt we pass to the Mistral AI model. The prompt includes the query, the retrieved schema snippets, and some similar queries from the corpus.

Prompting the LLM to think step by step improves the quality of the generated output. Hence, we instruct the LLM to output its reasoning and the SQL query in separate blocks in the output text.

We then call the Mistral AI model to generate the SQL statement.

We extract the SQL statement from the Mistral AI model's output and execute it on the Neon database to verify if it is valid.

## Conclusion

Thus, we have a working text-question-to-SQL query system by leveraging the `Mistral AI` API for both chat and embedding models, and `Neon` as the vector database.

To use it in production, there are some other considerations to keep in mind:

1. Validate the generated SQL query, especially for destructive operations like `DELETE` and `UPDATE` before executing them. Since the text input comes from a user, it might also cause SQL injection attacks by prompting the system with malicious input.
2. Monitor the system's performance and accuracy over time. We might need to update the LLM model used and the knowledge base embeddings as the data evolves.
3. Better metadata. While similar examples and database schema are useful, information like data lineage and dashboard logs can add more context to the LLM API calls.
4. Improving retrieval. For complex queries, we might need to increase the schema information passed to the LLM model. Further, our similarity search heuristic is pretty naive in that we are matching text queries to SQL statements. Using techniques like HyDE (Hypothetical Document Expansion) can improve the quality of the retrieved snippets.

## Appendix

We fetched the Northwind database setup script and some sample queries from the following helpful repositories: