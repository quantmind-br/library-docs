---
title: Function Calling | Mistral Docs
url: https://docs.mistral.ai/capabilities/function_calling
source: crawler
fetched_at: 2026-01-29T07:33:10.475006245-03:00
rendered_js: false
word_count: 1031
summary: This guide explains the five-step process for implementing function calling with Mistral models to connect them with external tools and APIs.
tags:
    - mistral-ai
    - function-calling
    - tool-calling
    - api-integration
    - llm-agents
    - json-schema
category: guide
---

Function calling, under the Tool Calling umbrela, allows Mistral models to connect to external local tools. By integrating Mistral models with external tools such as user defined functions or APIs, users can easily build applications catering to specific use cases and practical problems. In this guide, for instance, we wrote two functions for tracking payment status and payment date. We can use these two tools to provide answers for payment-related queries.

Before continuing, we recommend reading the [Chat Competions](https://docs.mistral.ai/capabilities/completion) documentation to learn more about the chat completions API and how to use it before proceeding.

### Available Models

Currently, among the function calling capable models, we have the following non-exhaustive list:

For more exhaustive information about all our models, visit the [Models Page](https://docs.mistral.ai/getting-started/models).

[Open in Colab ↗](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/function_calling/function_calling.ipynb)

At a glance, there are five main steps with function calling:

- [**1. Developer:**](#step-1) Specify Functions/Tools, and a System Prompt (optional)
- [**2. User:**](#step-2) Query the Model powered with the new Functions/Tools
- [**3. Model:**](#step-3) Generates function arguments if applicable when necessary
- [**4. Developer:**](#step-4) Executes the corresponding function to obtain tool results
- [**5. Model:**](#step-5) Generates an answer based on the tool results

In general, a chat with function calling will always look like the following:

In this guide, we will walk through a **simple function calling example** to demonstrate how function calling works with Mistral models in these five steps.

![functioncalling_steps](https://docs.mistral.ai/img/fc_steps.png)

Before we get started, let’s assume we have a dataframe consisting of payment transactions. When users ask questions about this dataframe, they can use certain tools to answer questions about this data. This is just an example to emulate an external database that the LLM cannot directly access.

### Functions and System Definitions

![functioncalling_step1](https://docs.mistral.ai/img/fc_step1.png)

Developers can define all the necessary tools for their use cases. Often, we might have multiple tools at our disposal. For this example, let’s consider we have two functions as our two tools:

- `retrieve_payment_status`: To retrieve payment status given a transaction ID.
- `retrieve_payment_date`: To retrieve payment date given a transaction ID.

For ease of use, we will organize the two functions into a dictionary where keys represent the functions names, and values are the functions themselves.  
**This allows us to dynamically call each function based on its function name.**

When seting up a model capable of function calling and agentic workflows, it's **recommended to provide context and custom instructions** under the `system` role umbrela, this can be done by adding a `system` message to the chat history.  
For this example, we will define a very simple system prompt to guide the model on how to use the provided tools.

In order for models to understand these functions, we need to outline the **function specifications with a JSON schema**. Specifically, we need to describe the type, function name, function description, function parameters, and the required parameter for the function. Since we have two functions here, let’s list two function specifications in a list.

### Query the Model

![functioncalling_step2](https://docs.mistral.ai/img/fc_step2.png)

With our functions and instructions ready, lets Suppose a user asks the following question: “What’s the status of my transaction T1001?” A standalone LLM would not be able to answer this question, as it needs to query the business logic backend to access the necessary data. **But with function calling, we can use the tools we have defined to answer accordingly.**

The previous question expects the model to use the `retrieve_payment_status` function to get the payment status of transaction T1001.

### Generate Function Arguments

![functioncalling_step3](https://docs.mistral.ai/img/fc_step3.png)

How do models know about these functions and know which function to use? We provide both the user query and the tools specifications to models. The goal in this step is not for the Mistral model to run the function directly. It’s to:

- Determine the appropriate function to use.
- Identify if there is any essential information missing for a function.
- Generate necessary arguments for the chosen function.

Developers can use `tool_choice` to specify how tools are used:

- "auto": default mode. Model decides if it uses the tool or not.
- "any": forces tool use.
- "none": prevents tool use.

And `parallel_tool_calls` to specify whether parallel tool calling is allowed.

- true: default mode. The model decides if it uses parallel tool calls or not.
- false: forces the model to use single tool calling.

With all our tools, system and query ready, we can call the model to **either reply or use the tools, generating the necessary arguments for the chosen function**.

The model provided a tool call as a response, visit the raw output for more information:

Let’s add the response message to the `messages` list history to continue the conversation.

Here, we got the response including `tool_calls` with the chosen function name `retrieve_payment_status` and the arguments for this function, the next step is to execute the function.

### Execute Functions

![functioncalling_step4](https://docs.mistral.ai/img/fc_step4.png)

How do we execute the function? Currently, it is the developer's responsibility to execute these functions and the function execution lies on the user/developer side. We have also introduced some tools executed server side for our Agents and Conversations API, visit [Tools](https://docs.mistral.ai/agents/tools).

To execute it, we extract some useful function information from the model response including `function_name` and `function_params`. It’s clear here that our model has chosen to use `retrieve_payment_status` with the parameter `transaction_id` set to T1001.

We then execute the corresponding function and we get the function output `'{"status": "Paid"}'`.

### Generate Followup Answer

![functioncalling_step5](https://docs.mistral.ai/img/fc_step5.png)

We can now provide the output from the tools/functions to our model, and in return, the model can produce a customised final response for the specific user (or in some cases, another tool call)

Our model has successfully generated a response using the output from the tool, providing the final answer:

- **"The status of your transaction with ID T1001 is Paid. Is there anything else I can assist you with?"**

A model is allowed to followup a tool call with another tool call. To handle such scenarios, you should **recursively call the model with the new tool call until it generates a final answer**.

Below you can find a full example of the above steps looping to simulate a chat session, interactivelly handling successive and/or parallel tool calls.

If you are interested in function calling and want to explore built-in solutions, MCP, and other agentic use cases, we invite you to visit the Agents documentation [here](https://docs.mistral.ai/agents/introduction).