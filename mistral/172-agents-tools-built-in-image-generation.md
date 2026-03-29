---
title: Image Generation | Mistral Docs
url: https://docs.mistral.ai/agents/tools/built-in/image_generation
source: crawler
fetched_at: 2026-01-29T07:34:16.435094896-03:00
rendered_js: false
word_count: 440
summary: A guide to using Mistral AI's image generation capabilities and APIs.
tags:
    - Mistral AI
    - Image Generation
    - AI Models
    - API Documentation
category: guide
---

Image Generation is a built-in [tool](https://docs.mistral.ai/agents/tools/built-in) tool that enables agents to generate images of all kinds and forms.

![image_generation_graph](https://docs.mistral.ai/img/image_generation_connector.png)![image_generation_graph](https://docs.mistral.ai/img/image_generation_connector_dark.png)

Enabling this tool allows models to create images at any given moment.

To use the image generation tool, you can create an agent with the image generation tool enabled and leverage the conversations API to generate images, note that you need to download the image from the file ID provided in the response.

You can create an agent with access to image generation by providing it as one of the tools. Note that you can still add more tools to the agent. The model is free to create images on demand.

As with other agents, when creating one, you will receive an agent ID corresponding to the created agent. You can use this ID to start a conversation.

Now that we have our image generation agent ready, we can create images on demand at any point.

To start a conversation with our image generation agent, we can use the following code:

Below we will explain the different outputs of the response of the previous snippet example:

- **`tool.execution`** : This entry corresponds to the execution of the image generation tool. It includes metadata about the execution, such as:
  
  - `name`: The name of the tool, which in this case is `image_generation`.
  - `object`: The type of object, which is `entry`.
  - `type`: The type of entry, which is `tool.execution`.
  - `created_at` and `completed_at`: Timestamps indicating when the tool execution started and finished.
  - `id`: A unique identifier for the tool execution.
- **`message.output`** : This entry corresponds to the generated answer from our agent. It includes metadata about the message, such as:
  
  - `content`: The actual content of the message, which in this case is a list of chunks. These chunks can be of different types, and the model can interleave different chunks, using `text` chunks and others to complete the message. In this case, we got a two chunks corresponding to a `text` chunk and a `tool_file`, which represents the generated file, specifically the generated image. The `content` section includes:
    
    - `tool`: The name of the tool used for generating the file, which in this case is `image_generation`.
    - `file_id`: A unique identifier for the generated file.
    - `type`: The type of chunk, which in this case is `tool_file`.
    - `file_name`: The name of the generated file.
    - `file_type`: The type of the generated file, which in this case is `png`.
  - `object`: The type of object, which is `entry`.
  - `type`: The type of entry, which is `message.output`.
  - `created_at` and `completed_at`: Timestamps indicating when the message was created and completed.
  - `id`: A unique identifier for the message.
  - `agent_id`: A unique identifier for the agent that generated the message.
  - `model`: The model used to generate the message, which in this case is `mistral-medium-2505`.
  - `role`: The role of the message, which is `assistant`.

To access that image you can download it via our files endpoint.

![generated_image](https://docs.mistral.ai/img/agent_generated.png)

A full code snippet to download all generated images from a response could look like so: