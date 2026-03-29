---
title: Microsoft AutoGen & Mistral Large 2407 - Retrieve information from a Postgresql Database - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-ms_autogen_pgsql-mistral_pgsql_function_calling
source: crawler
fetched_at: 2026-01-29T07:33:59.718038096-03:00
rendered_js: false
word_count: 388
summary: A technical tutorial demonstrating how to integrate Microsoft AutoGen with Mistral Large 2407 to query and retrieve data from a PostgreSQL database using AI agents.
tags:
    - Microsoft AutoGen
    - Mistral AI
    - PostgreSQL
    - AI Agents
    - Database Integration
category: guide
---

This tutorial is written as example how to use Microsoft AutoGen in Combination with Mistral Large V2 to query a Postgres Database. It gives a short and simple overview how to do this, it is also possible to write extra tools and add them to query other DB's or maybe VectorDB's with a perfect prompt ;)!

Besides query's and prompting a good context is also really important, thats why I added a extra function to always provide the context of all avaible tables.

**PLEASE NOTE:** Try to prevent using to many tools and contexts together, but use different 'chat models' instead of a single big model to do everything.

## Preparation steps:

In the first few steps we will install Postgresql, after that we will import a database dumb. I did go for the following database dumb; name.basics.tsv, found here; [https://datasets.imdbws.com/](https://datasets.imdbws.com/)

## Import all required packages

Lets importat all required packages, in this case we need autogen, the postgresql package and some other libraries.

## The Postgress Function

The Postgress function takes a valid json input, based on this input the query is executed. After that the function returns the output to the LLM, which will respond on that with a message to the user.

Because we pre-defined how to use the tool, it is not possible to delete , update or create any records, read access only!

## Define API keys

Fill in your Mistral API key to access Mistral-large-2407!

## Get All tables

We want to prompt the LLM with the context of all tables, this has to be up to date, so we create a sepperate function which queries the postgres tool but with pre defined input to query all tables.

## Execute user queries

Now everything is set to use the chat and query Postgresql Database using Mistral-Large-2407

## Example questions & Conclusion

Some good example questions to ask this model are;

- Get me all people named Mistral
- Get me all actors born in 2000, limit them to 10
- Get me all actors from before 1950, limit them to 13

So like you can see Mistral Large V2 or any equivelant model it is relatively easy to create a function to query a Postgres DB without giving it full access to delete records.

This can give people a safer way to access different databases, without having to worry to make mistakes.