---
title: Basics of Function Calling - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/mistral-function_calling-function_calling
source: crawler
fetched_at: 2026-01-29T07:33:56.313247817-03:00
rendered_js: false
word_count: 574
---

Function calling allows Mistral models to connect to external tools. By integrating Mistral models with external tools such as user defined functions or APIs, users can easily build applications catering to specific use cases and practical problems. In this guide, for instance, we wrote two functions for tracking payment status and payment date. We can use these two tools to provide answers for payment-related queries.

At a glance, there are four steps with function calling:

- User: specify tools and query
- Model: Generate function arguments if applicable
- User: Execute function to obtain tool results
- Model: Generate final answer

In this guide, we will walk through a simple example to demonstrate how function calling works with Mistral models in these four steps.

Before we get started, let’s assume we have a dataframe consisting of payment transactions. When users ask questions about this dataframe, they can use certain tools to answer questions about this data. This is just an example to emulate an external database that the LLM cannot directly access.

## Step 1. User: specify tools and query

### Tools

Users can define all the necessary tools for their use cases.

- In many cases, we might have multiple tools at our disposal. For example, let’s consider we have two functions as our two tools: `retrieve_payment_status` and `retrieve_payment_date` to retrieve payment status and payment date given transaction ID.

<!--THE END-->

- In order for Mistral models to understand the functions, we need to outline the function specifications with a JSON schema. Specifically, we need to describe the type, function name, function description, function parameters, and the required parameter for the function. Since we have two functions here, let’s list two function specifications in a list.

<!--THE END-->

- Then we organize the two functions into a dictionary where keys represent the function name, and values are the function with the df defined. This allows us to call each function based on its function name.

### User query

Suppose a user asks the following question: “What’s the status of my transaction?” A standalone LLM would not be able to answer this question, as it needs to query the business logic backend to access the necessary data. But what if we have an exact tool we can use to answer this question? We could potentially provide an answer!

## Step 2. Model: Generate function arguments

How do Mistral models know about these functions and know which function to use? We provide both the user query and the tools specifications to Mistral models. The goal in this step is not for the Mistral model to run the function directly. It’s to 1) determine the appropriate function to use , 2) identify if there is any essential information missing for a function, and 3) generate necessary arguments for the chosen function.

## Step 3. User: Execute function to obtain tool results

How do we execute the function? Currently, it is the user’s responsibility to execute these functions and the function execution lies on the user side. In the future, we may introduce some helpful functions that can be executed server-side.

Let’s extract some useful function information from model response including function\_name and function\_params. It’s clear here that our Mistral model has chosen to use the function `retrieve_payment_status` with the parameter `transaction_id` set to T1001.

## Step 4. Model: Generate final answer

We can now provide the output from the tools to Mistral models, and in return, the Mistral model can produce a customised final response for the specific user.