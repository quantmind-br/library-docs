---
title: Agents & Conversations | Mistral Docs
url: https://docs.mistral.ai/agents/agents
source: crawler
fetched_at: 2026-01-29T07:33:13.299918066-03:00
rendered_js: false
word_count: 725
summary: Documentation providing an overview of building and interacting with AI agents and managing conversation flows within the Mistral AI ecosystem.
tags:
    - Mistral AI
    - AI Agents
    - Conversational AI
    - LLM Documentation
category: guide
---

Agents is a feature that allows developers to create predefined models with their own system prompts and tools. In the other hand, Conversations is a feature that allows developers to create a history of interactions with an assistant that leverage Agents or our models directly.

We introduce three new main objects that our API makes use of:

- **Agents**: A set of pre-selected values to augment model abilities, such as tools, instructions, and completion parameters.
- **Conversation**: A history of interactions, past events and entries with an assistant, such as messages and tool executions, Conversations can be started by an Agent or a Model.
- **Entry**: An action that can be created by the user or an assistant. It brings a more flexible and expressive representation of interactions between a user and one or multiple assistants. This allows for more control over describing events.

You can create Conversations without creating Agents. These two APIs are independent.

To find all details visit our [Agents](https://docs.mistral.ai/api/#tag/beta.agents) and [Conversations](https://docs.mistral.ai/api/#tag/beta.conversations) API spec.

## Agent Creation and Management

Agents are a set of pre-selected values, such as tools, instructions, and completion parameters, that will define the behavior of the model.

When creating an Agent, there are multiple parameters and values that need to be set in advance. These are:

- `model`: The model your agent will use among our available models for chat completion.
- `description`: The agent description, related to the task it must accomplish or the use case at stake.
- `name`: The name of your agent.
- `instructions` *optional*: The main instructions of the agent, also known as the system prompt. This must accurately describe the main task of your agent.
- `tools` *optional*: A list of tools the model can make use of. There are currently different `types` of tools:
  
  - `function`: User-defined tools, with similar usage to the standard function calling used with chat completion.
  - `web_search`/`web_search_premium`: Our built-in tool for web search.
  - `code_interpreter`: Our built-in tool for code execution.
  - `image_generation`: Our built-in tool for image generation.
  - `document_library`: Our built-in RAG tool for knowledge grounding and search on custom data.
- `completion_args` *optional*: Standard chat completion sampler arguments. All chat completion arguments are accepted.

When creating an agent, you will receive an Agent object with an agent ID. You can then use that ID to have conversations.

Here is an example of a Web Search Agent using our built-in tool:

You can find more information [here](https://docs.mistral.ai/connectors/websearch).

## Conversations

In the other hand, Conversations are a history of interactions with an assistant. They are more flexible and expressive than the Chat Completion API, allowing for more control over describing events.

Once your agent is created, you can **start** conversations at any point while keeping the same conversation persistent. You first start a conversation by providing:

- `agent_id`: The ID of the agent, created during the Agent creation.
- `inputs`: The message to start the conversation with. It can be either a string with the first user message or question, or the history of messages.

You can start and continue conversations without creating Agents. These two APIs are independent, in that case you can use the `model` parameter instead of `agent_id`.

Creating a Conversation will return a conversation ID.

To **continue** the conversation and append the exchanges as you go, you provide two values:

- `conversation_id`: The ID created during the conversation start or append that maps to the internally stored conversation history.
- `inputs`: The next message or reply. It can be either a string or a list of messages.

A new Conversation ID is provided at each append.

You can also **opt out** from the automatic storing with `store=False`; this will make the new history not being stored on our cloud.

We also provide the parameter `handoff_execution`, which currently has two modes: `server` or `client`.

- `server`: Runs the handoff as expected internally on our cloud servers; this is the default setting.
- `client`: When a handoff is triggered, a response is provided directly to the user, enabling them to handle the handoff with control.

For more information regarding handoffs visit [this section](https://docs.mistral.ai/agents/handoffs).

Below you can find examples of how to create and manage conversations.

As previously mentionned, you can start a conversation at any given point with your custom Agent or with a specific model of your choice.

To start a conversation with an Agent, you need to provide the Agent ID and the inputs.

Without an Agent, querying Conversations would look like so: