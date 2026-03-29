---
title: Build a Chainlit App with Mistral AI - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-chainlit-chainlit_mistral_reasoning
source: crawler
fetched_at: 2026-01-29T07:34:06.107470409-03:00
rendered_js: false
word_count: 417
---

The goal of this cookbook is to show how one can build a **Chainlit** application on top of **Mistral AI**'s APIs!

We will highlight the reasoning capabilities of Mistral's LLMs by letting a self-reflective agent assess whether it has gathered enough information to answer *nested* user questions, such as **"What is the weather in Napoleon's hometown?"**

To answer such questions, our application should go through multiple-step reasoning: first get Napoleon's hometown, then fetch the weather for that location.

You can read through this notebook or simply go with `chainlit run app.py` since the whole code is in `app.py`. You will find here a split of the whole application code with explanations:

- [Setup](#setup)
- [Define available tools](#define-tools)
- [Agent logic](#agent-logic)
- [On message callback](#on-message)
- [Starter questions](#starter-questions)

Here's a visual of what we will have built in a few minutes:

## Setup

### Requirements

We will install `mistralai`, `chainlit` and `python-dotenv`.

Be sure to create a `.env` file with the line `MISTRAL_API_KEY=` followed by your Mistral AI API key.

### Optional - Tracing

You can get a `LITERAL_API_KEY` from [Literal AI](https://docs.getliteral.ai/get-started/installation#how-to-get-my-api-key) to setup tracing and visualize the flow of your application.

Within the code, Chainlit offers the `@chainlit.step` decorators to trace your functions, along with an automatic instrumentation of Mistral's API via `chainlit.instrument_mistralai()`.

The trace for this notebook example is: [https://cloud.getliteral.ai/thread/ea173d7d-a53f-4eaf-a451-82090b07e6ff](https://cloud.getliteral.ai/thread/ea173d7d-a53f-4eaf-a451-82090b07e6ff).

## Define available tools

In the next cell, we define the tools, and their JSON definitions, which we will provide to the agent. We have two tools:

- `get_current_weather` -&gt; takes in a location
- `get_home_town` -&gt; takes in a person's name

Optionally, you can decorate your tool definitions with `@cl.step()`, specifying a type and name to organize the traces you can visualize from [Literal AI](https://literalai.com).

## Agent logic

For the agent logic, we simply repeat the following pattern (max. 5 times):

- ask the user question to Mistral, making both tools available
- execute tools if Mistral asks for it, otherwise return message

You will notice that we added an optional `@cl.step` of type `run` and with optional tags to trace the call accordingly in [Literal AI](https://literalai.com).

Visual trace: [https://cloud.getliteral.ai/thread/ea173d7d-a53f-4eaf-a451-82090b07e6ff](https://cloud.getliteral.ai/thread/ea173d7d-a53f-4eaf-a451-82090b07e6ff)

## On message callback

The callback below, properly annotated with `@cl.on_message`, ensures our `run_agent` function is called upon every new user message.

## Starter questions

You can define starter questions for your users to easily try out your application, which will look like this:

We have got many more Chainlit features in store (authentication, feedback, Slack/Discord integrations, etc.) to let you build custom LLM applications and really take advantage of Mistral's LLM capabilities.

Please visit the Chainlit documentation to learn more!