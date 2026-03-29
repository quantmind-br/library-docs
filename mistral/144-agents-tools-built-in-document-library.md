---
title: Document Library | Mistral Docs
url: https://docs.mistral.ai/agents/tools/built-in/document_library
source: crawler
fetched_at: 2026-01-29T07:34:17.291043404-03:00
rendered_js: false
word_count: 631
summary: This document explains Mistral's Document Library tool, which provides built-in RAG capabilities for agents to access and retrieve external data. It covers library management, agent integration via API or Le Chat, and the structure of response outputs including citations.
tags:
    - document-library
    - mistral-ai
    - rag
    - ai-agents
    - built-in-tools
    - retrieval-augmented-generation
category: guide
---

Document Library is a built-in [tool](https://docs.mistral.ai/agents/tools/built-in) tool that enables agents to access documents from Mistral Cloud.

You can manage your libraries and upload your documents to them, enabling a seamless integration with your agents, letting them access external data of your choice.

![document_library_graph](https://docs.mistral.ai/img/document_library_connector.png)![document_library_graph](https://docs.mistral.ai/img/document_library_connector_dark.png)

It is a built-in RAG capability that enhances your agents' knowledge with the data you have uploaded.

To use the Document Library tool, you can create an agent or use the Conversations API directly.

However, you will need to create a library first, we provide a complete API allowing full control over your libraries.

You can create an agent with access to the document library by providing it as one of the tools. Note that you can still add more tools to the agent. The model is free to access and leverage the knowledge from the uploaded documents.

You specify the libraries that the agent has access to with `library_ids`, you can create and manage these libraries via API directly, see more about how to create and manage libraries in the **Manage Libraries** tab.

It is also possible to specify libraries created via Le Chat; these IDs are visible in the URL of the corresponding library created on Le Chat, for example: `https://chat.mistral.ai/libraries/<library_id>`; To enable the Agent to access Le Chat library, you have to be an Org admin and share it with the Organization.

The opposite is also possible, you can create a library via API and share it with your team on Le Chat.  
Find more on how to share and manage libraries [here](https://docs.mistral.ai/agents/tools/built-in/document_library?tab=manage-libraries#explorer-tabs-agent_creation_and_library_management).

As with other agents, when creating one, you will receive an agent ID corresponding to the created agent. You can use this ID to start a conversation.

Next, learn how you can manage your libraries and agents in the [**Manage Libraries**](https://docs.mistral.ai/agents/tools/built-in/document_library?tab=manage-libraries#explorer-tabs-agent_creation_and_library_management) tab.

Now that we have our document library agent ready, we can search them on demand at any point.

To start a conversation with our document library agent, we can use the following code:

Below we will explain the different outputs of the response of the previous snippet example:

- **`tool.execution`** : This entry corresponds to the execution of the document library tool. It includes metadata about the execution, such as:
  
  - `name`: The name of the tool, which in this case is `document_library`.
  - `object`: The type of object, which is `entry`.
  - `type`: The type of entry, which is `tool.execution`.
  - `created_at` and `completed_at`: Timestamps indicating when the tool execution started and finished.
  - `id`: A unique identifier for the tool execution.
- **`message.output`** : This entry corresponds to the generated answer from our agent. It includes metadata about the message, such as:
  
  - `content`: The actual content of the message, which in this case is a list of chunks. These chunks correspond to the text chunks, the actual message response of the model, sometimes interleaved with reference chunks. These reference chunks are used for citations during Retrieval-Augmented Generation (RAG) related tool usages. In this case, it provides the source of the information it just answered with, which is extremely useful for web search. This allows for transparent feedback on where the model got its response from for each section and fact answered with. The `content` section includes:
    
    - `type`: The type of chunk, which can be `text` or `tool_reference`.
    - `text`: The actual text content of the message.
  - `object`: The type of object, which is `entry`.
  - `type`: The type of entry, which is `message.output`.
  - `created_at` and `completed_at`: Timestamps indicating when the message was created and completed.
  - `id`: A unique identifier for the message.
  - `agent_id`: A unique identifier for the agent that generated the message.
  - `model`: The model used to generate the message, which in this case is `mistral-medium-2505`.
  - `role`: The role of the message, which is `assistant`.

Another tool that pro-actively uses references is the websearch tool, feel free to take a look [here](https://docs.mistral.ai/agents/tools/websearch).  
For more information regarding the use of citations, you can find more [here](https://docs.mistral.ai/capabilities/citations).