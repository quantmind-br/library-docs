---
title: Image Generation | Mistral Docs
url: https://docs.mistral.ai/studio-api/agents/agent-tools/image_generation
source: sitemap
fetched_at: 2026-04-26T04:11:55.082537094-03:00
rendered_js: false
word_count: 439
summary: Configure and use the built-in image generation tool within agents, including handling tool execution responses and downloading generated files.
tags:
    - image-generation
    - agent-tools
    - api-integration
    - file-download
    - conversations-api
    - model-output
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Image Generation

Built-in tool that enables agents to generate images of all kinds and forms.

![Image Generation architecture](https://docs.mistral.ai/img/image_generation_connector.png)![Image Generation architecture dark](https://docs.mistral.ai/img/image_generation_connector_dark.png)

## Usage

Create an agent with the image generation tool enabled. Use the Conversations API to generate images, then download from the file ID in the response.

```python
from mistralai.client import MistralClient

client = MistralClient(api_key="your-api-key")

# Create agent with image generation
agent = client.agents.create(
    model="mistral-large-latest",
    tools=[{"type": "image_generation"}]
)

# Generate image
chat_response = client.agents.chat(
    agent_id=agent.id,
    inputs="Generate an image of a sunset over mountains"
)
```

## Response Structure

### `tool.execution`

Image generation execution metadata:

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Tool name: `image_generation` |
| `object` | string | Object type: `entry` |
| `type` | string | Entry type: `tool.execution` |
| `created_at` | datetime | Execution start timestamp |
| `completed_at` | datetime | Execution completion timestamp |
| `id` | string | Unique execution identifier |

### `message.output`

Agent response containing the generated file:

| Field | Type | Description |
|-------|------|-------------|
| `content` | list | List of chunks |
| `content[].tool` | string | Tool name: `image_generation` |
| `content[].file_id` | string | Unique file identifier |
| `content[].type` | string | Chunk type: `tool_file` |
| `content[].file_name` | string | Generated file name |
| `content[].file_type` | string | File type: `png` |

## Download Generated Images

```python
# Get file content from response
for chunk in chat_response.outputs[0].content:
    if chunk.type == "tool_file":
        file_content = client.files.retrieve_content(file_id=chunk.file_id)
        with open(chunk.file_name, "wb") as f:
            f.write(file_content)
```

![Generated image example](https://docs.mistral.ai/img/agent_generated.png)

#image-generation #agent-tools #api-integration #file-download #conversations-api #model-output
