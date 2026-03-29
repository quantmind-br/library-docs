---
title: Handoffs | Mistral Docs
url: https://docs.mistral.ai/agents/handoffs
source: crawler
fetched_at: 2026-01-29T07:33:11.910585121-03:00
rendered_js: false
word_count: 318
summary: A guide on implementing handoffs between different models or agents within the Mistral AI ecosystem to optimize task delegation and performance.
tags:
    - Mistral AI
    - handoffs
    - agent workflow
    - model delegation
category: guide
---

When creating and using Agents, often with access to specific tools, there are moments where it is desired to call other Agents mid-action. To elaborate and engineer workflows for diverse tasks that you may want automated, this ability to give Agents tasks or hand over a conversation to other agents is called **Handoffs**.

![handoffs_graph](https://docs.mistral.ai/img/handoffs.png)

When creating a workflow powered by Handoffs, we first need to create all the Agents that our workflow will use. There is no limit to how many chained Handoffs a workflow can have. You are free to create multiple Agents using diverse tools, models and handoffs, and orchestrate your own workflow using these Agents.

![handoffs_graph](https://docs.mistral.ai/img/multiple_agents_handoffs.png)

First things first, let's create diverse Agents with multiple tasks and capabilities.

![handoffs_graph](https://docs.mistral.ai/img/responsibilities_handoffs.png)

Once all our Agents created, we update our previous defined Agents with a list of `handoffs` available.

Our workflow and behavior are defined, now we can run it.

We created 5 agents, some of them have access to built-in tools, and others to local tools like `get_european_central_bank_interest_rate`.

It is now possible to have a chain of actions by sending a request to the `finance_agent`.

We also provide the parameter `handoff_execution`, which currently has two modes: `server` or `client`.

- `server`: Runs the handoff as expected internally on our cloud servers; this is the default setting.
- `client`: When a handoff is triggered, a response is provided directly to the user, enabling them to handle the handoff with control.

Let’s trigger two different behaviors as examples:

**"Fetch the current US bank interest rate and calculate the compounded effect if investing for the next 10y"**

The first example asks for the US central bank interest rate, so we expect to involve the `websearch-agent` and then to calculate the compounded interest over 10 years. This should use the `calculator-agent` to do this.

![handoffs_graph_examplea](https://docs.mistral.ai/img/examplea_handoffs.png)

Below, you can see the output events of the conversation in order of appearance for the example above.