---
title: Function Calling Rest API with Mistral7Bv3 using Ollama - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-ollama-function_calling_local
source: crawler
fetched_at: 2026-01-29T07:34:07.962890215-03:00
rendered_js: false
word_count: 560
summary: A tutorial on implementing function calling via REST APIs using the Mistral 7B v3 model integrated with Ollama.
tags:
    - Mistral AI
    - Ollama
    - Function Calling
    - REST API
    - Mistral 7B v3
category: guide
---

Function calling allows Mistral models to connect to external tools. By integrating Mistral models with external tools such as user defined functions or APIs, users can easily build applications catering to specific use cases and practical problems. In this guide, for instance, we wrote two functions for tracking a Pet Store's Pets and User info. We can use these two tools to provide answers for pet-related queries.

At a glance, there are four steps with function calling:

- User: specify tools and query
- Model: Generate function arguments if applicable
- User: Execute function to obtain tool results
- Model: Generate final answer

In this guide, we will walk through a simple example to demonstrate how function calling works with Mistral models in these four steps.

Before we get started, let’s assume we have an OpenAPI spec end-points consisting of Pet store information. When users ask questions about this API, they can use certain tools to answer questions about this data. This is just an example to emulate an external database via API that the LLM cannot directly access.

Setup functions to make REST API call. We take example of pet store from [Swagger Editor](https://editor.swagger.io/)  
We download the openapi.json specification.

Example curl query to get information of a Pet by PetID

`curl -X 'GET' \ 'https://petstore3.swagger.io/api/v3/pet/1' \ -H 'accept: application/json'`

Example curl query to get information of a User by username `curl -X 'GET' \ 'https://petstore3.swagger.io/api/v3/user/user1' \ -H 'accept: application/json'`

## Function Calling for REST API

## Step 1. User: specify tools and query

### Tools

Users can define all the necessary tools for their use cases.

- In many cases, we might have multiple tools at our disposal. For example, let’s consider we have two functions as our two tools: `retrieve_pet_info` and `retreive_user_info` to retrieve pet and user info given `petID` and `username`.
- Then we organize the two functions into a dictionary where keys represent the function name, and values are the function with the df defined. This allows us to call each function based on its function name.

<!--THE END-->

- In order for Mistral models to understand the functions, we need to outline the function specifications with a JSON schema. Specifically, we need to describe the type, function name, function description, function parameters, and the required parameter for the function. Since we have two functions here, let’s list two function specifications in a list.
- Tool Generator - parse open api spec for dynamic tool definition creation. Download openai.json from [https://editor.swagger.io/](https://editor.swagger.io/)

### User query

Suppose a user asks the following question: “What’s the status of my Pet 1?” A standalone LLM would not be able to answer this question, as it needs to query the business logic backend to access the necessary data. But what if we have an exact tool we can use to answer this question? We could potentially provide an answer!

For external ollama endpoint, set the environment variable "OLLAMA\_ENDPOINT"

export OLLAMA\_ENDPOINT="YOUR-Ollama-IP

"

## Step 3. User: Execute function to obtain tool results

How do we execute the function? Currently, it is the user’s responsibility to execute these functions and the function execution lies on the user side. In the future, we may introduce some helpful functions that can be executed server-side.

Let’s extract some useful function information from model response including function\_name and function\_params. It’s clear here that our Mistral model has chosen to use the function `getPetId` with the parameter `petId` set to 1.