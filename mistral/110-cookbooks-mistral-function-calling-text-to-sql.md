---
title: Text to SQL on multi-tables database - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/mistral-function_calling-text_to_sql
source: crawler
fetched_at: 2026-01-29T07:33:51.931372399-03:00
rendered_js: false
word_count: 296
summary: This cookbook demonstrates how to build a scalable text-to-SQL architecture using Mistral models and function calling. It also covers performance evaluation using the DeepEval framework and the Chinook sample database.
tags:
    - mistral-ai
    - text-to-sql
    - function-calling
    - deepeval
    - llm-evaluation
    - database-querying
category: tutorial
---

![image.png](https://docs.mistral.ai/cookbooks/images/text_to_sql1.png)

In this cookbook we will show you how to :

- Use the function calling capabilities of Mistral models
- Build a text2SQL architecture that scales more efficiently than a naive approach where all schemas are integrally injected in the system prompt
- Evaluate your system with Mistral models and leveraging the DeepEval framework

## Imports

## Load the Chinook database

"Chinook is a sample database available for SQL Server, Oracle, MySQL, etc. It can be created by running a single SQL script. Chinook database is an alternative to the Northwind database, being ideal for demos and testing ORM tools targeting single and multiple database servers."

To run this notebook you will need to download the Chinook datase. You will find more information about this database by clicking on this [github link](https://github.com/lerocha/chinook-database).

To create the `Chinook.db` in the same directory as this notebook you have several options :

- You can download and build the database via the command line :

<!--THE END-->

- Another strategy consists in running the following script `https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_Sqlite.sql`.

Firstly save the script to a folder/directory on your computer. Then create a database called Chinook with `sqlite3 Chinook.db`. Ultimately run the script with the command `.read Chinook_Sqlite.sql`

![image.png](https://docs.mistral.ai/cookbooks/images/text_to_sql2.png)

## Set up clients

## Interract with the Chinook database

We are defining two functions :

- run\_sql\_query that runs sql code on Chinook
- get\_sql\_schema\_of\_table that returns the schema of a table specified as input

## Build agent

## Test the agent

Let's test the agent and ask a few random questions of increasing complexity

## Evaluating

Let's try to evaluate the agent in a more formal way.

We will build a test set based on the questions from this Medium article [Chinook question/answers](https://medium.com/@raufrukayat/chinook-database-querying-a-digital-music-store-database-8c98cf0f8611)

We will evaluate answers via LLM as a judge through the framework [DeepEval](https://docs.confident-ai.com/) from which the image here below is taken.

![image.png](https://docs.mistral.ai/cookbooks/images/text_to_sql3.png)