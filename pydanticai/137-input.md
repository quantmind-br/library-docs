---
title: Image, Audio, Video & Document Input - Pydantic AI
url: https://ai.pydantic.dev/input/
source: sitemap
fetched_at: 2026-01-22T22:23:29.0300498-03:00
rendered_js: false
word_count: 550
summary: This document explains how to provide multimodal inputs such as images, audio, video, and documents to LLMs using Pydantic AI. It details how to handle both URL-based and local binary content across different model providers.
tags:
    - pydantic-ai
    - multimodal-input
    - binary-content
    - image-processing
    - llm-integration
    - python
category: guide
---

Some LLMs are now capable of understanding audio, video, image and document content.

## Image Input

Info

Some models do not support image input. Please check the model's documentation to confirm whether it supports image input.

If you have a direct URL for the image, you can use [`ImageUrl`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ImageUrl "ImageUrl            dataclass   "):

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) image\_input.py

```
frompydantic_aiimport Agent, ImageUrl

agent = Agent(model='gateway/openai:gpt-5')
result = agent.run_sync(
    [
        'What company is this logo from?',
        ImageUrl(url='https://iili.io/3Hs4FMg.png'),
    ]
)
print(result.output)
#> This is the logo for Pydantic, a data validation and settings management library in Python.
```

image\_input.py

```
frompydantic_aiimport Agent, ImageUrl

agent = Agent(model='openai:gpt-5')
result = agent.run_sync(
    [
        'What company is this logo from?',
        ImageUrl(url='https://iili.io/3Hs4FMg.png'),
    ]
)
print(result.output)
#> This is the logo for Pydantic, a data validation and settings management library in Python.
```

If you have the image locally, you can also use [`BinaryContent`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent            dataclass   "):

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) local\_image\_input.py

```
importhttpx

frompydantic_aiimport Agent, BinaryContent

image_response = httpx.get('https://iili.io/3Hs4FMg.png')  # Pydantic logo

agent = Agent(model='gateway/openai:gpt-5')
result = agent.run_sync(
    [
        'What company is this logo from?',
        BinaryContent(data=image_response.content, media_type='image/png'),  # (1)!
    ]
)
print(result.output)
#> This is the logo for Pydantic, a data validation and settings management library in Python.
```

1. To ensure the example is runnable we download this image from the web, but you can also use `Path().read_bytes()` to read a local file's contents.

local\_image\_input.py

```
importhttpx

frompydantic_aiimport Agent, BinaryContent

image_response = httpx.get('https://iili.io/3Hs4FMg.png')  # Pydantic logo

agent = Agent(model='openai:gpt-5')
result = agent.run_sync(
    [
        'What company is this logo from?',
        BinaryContent(data=image_response.content, media_type='image/png'),  # (1)!
    ]
)
print(result.output)
#> This is the logo for Pydantic, a data validation and settings management library in Python.
```

1. To ensure the example is runnable we download this image from the web, but you can also use `Path().read_bytes()` to read a local file's contents.

## Audio Input

Info

Some models do not support audio input. Please check the model's documentation to confirm whether it supports audio input.

You can provide audio input using either [`AudioUrl`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AudioUrl "AudioUrl            dataclass   ") or [`BinaryContent`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent            dataclass   "). The process is analogous to the examples above.

## Video Input

Info

Some models do not support video input. Please check the model's documentation to confirm whether it supports video input.

You can provide video input using either [`VideoUrl`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.VideoUrl "VideoUrl            dataclass   ") or [`BinaryContent`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent            dataclass   "). The process is analogous to the examples above.

## Document Input

Info

Some models do not support document input. Please check the model's documentation to confirm whether it supports document input.

You can provide document input using either [`DocumentUrl`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.DocumentUrl "DocumentUrl            dataclass   ") or [`BinaryContent`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent            dataclass   "). The process is similar to the examples above.

If you have a direct URL for the document, you can use [`DocumentUrl`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.DocumentUrl "DocumentUrl            dataclass   "):

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) document\_input.py

```
frompydantic_aiimport Agent, DocumentUrl

agent = Agent(model='gateway/anthropic:claude-sonnet-4-5')
result = agent.run_sync(
    [
        'What is the main content of this document?',
        DocumentUrl(url='https://storage.googleapis.com/cloud-samples-data/generative-ai/pdf/2403.05530.pdf'),
    ]
)
print(result.output)
#> This document is the technical report introducing Gemini 1.5, Google's latest large language model...
```

document\_input.py

```
frompydantic_aiimport Agent, DocumentUrl

agent = Agent(model='anthropic:claude-sonnet-4-5')
result = agent.run_sync(
    [
        'What is the main content of this document?',
        DocumentUrl(url='https://storage.googleapis.com/cloud-samples-data/generative-ai/pdf/2403.05530.pdf'),
    ]
)
print(result.output)
#> This document is the technical report introducing Gemini 1.5, Google's latest large language model...
```

The supported document formats vary by model.

You can also use [`BinaryContent`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent            dataclass   ") to pass document data directly:

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) binary\_content\_input.py

```
frompathlibimport Path
frompydantic_aiimport Agent, BinaryContent

pdf_path = Path('document.pdf')
agent = Agent(model='gateway/anthropic:claude-sonnet-4-5')
result = agent.run_sync(
    [
        'What is the main content of this document?',
        BinaryContent(data=pdf_path.read_bytes(), media_type='application/pdf'),
    ]
)
print(result.output)
#> The document discusses...
```

binary\_content\_input.py

```
frompathlibimport Path
frompydantic_aiimport Agent, BinaryContent

pdf_path = Path('document.pdf')
agent = Agent(model='anthropic:claude-sonnet-4-5')
result = agent.run_sync(
    [
        'What is the main content of this document?',
        BinaryContent(data=pdf_path.read_bytes(), media_type='application/pdf'),
    ]
)
print(result.output)
#> The document discusses...
```

## User-side download vs. direct file URL

When using one of `ImageUrl`, `AudioUrl`, `VideoUrl` or `DocumentUrl`, Pydantic AI will default to sending the URL to the model provider, so the file is downloaded on their side.

Support for file URLs varies depending on type and provider:

Model Send URL directly Download and send bytes Unsupported [`OpenAIChatModel`](https://ai.pydantic.dev/api/models/openai/#pydantic_ai.models.openai.OpenAIChatModel "OpenAIChatModel            dataclass   ") `ImageUrl` `AudioUrl`, `DocumentUrl` `VideoUrl` [`OpenAIResponsesModel`](https://ai.pydantic.dev/api/models/openai/#pydantic_ai.models.openai.OpenAIResponsesModel "OpenAIResponsesModel            dataclass   ") `ImageUrl`, `AudioUrl`, `DocumentUrl` — `VideoUrl` [`AnthropicModel`](https://ai.pydantic.dev/api/models/anthropic/#pydantic_ai.models.anthropic.AnthropicModel "AnthropicModel            dataclass   ") `ImageUrl`, `DocumentUrl` (PDF) `DocumentUrl` (`text/plain`) `AudioUrl`, `VideoUrl` [`GoogleModel`](https://ai.pydantic.dev/api/models/google/#pydantic_ai.models.google.GoogleModel "GoogleModel            dataclass   ") (Vertex) All URL types — — [`GoogleModel`](https://ai.pydantic.dev/api/models/google/#pydantic_ai.models.google.GoogleModel "GoogleModel            dataclass   ") (GLA) [YouTube](https://ai.pydantic.dev/models/google/#document-image-audio-and-video-input), [Files API](https://ai.pydantic.dev/models/google/#document-image-audio-and-video-input) All other URLs — [`XaiModel`](https://ai.pydantic.dev/api/models/xai/#pydantic_ai.models.xai.XaiModel "XaiModel") `ImageUrl` `DocumentUrl` `AudioUrl`, `VideoUrl` [`MistralModel`](https://ai.pydantic.dev/api/models/mistral/#pydantic_ai.models.mistral.MistralModel "MistralModel            dataclass   ") `ImageUrl`, `DocumentUrl` (PDF) — `AudioUrl`, `VideoUrl`, `DocumentUrl` (non-PDF) [`BedrockConverseModel`](https://ai.pydantic.dev/api/models/bedrock/#pydantic_ai.models.bedrock.BedrockConverseModel "BedrockConverseModel            dataclass   ") S3 URLs (`s3://`) `ImageUrl`, `DocumentUrl`, `VideoUrl` `AudioUrl` [`OpenRouterModel`](https://ai.pydantic.dev/api/models/openrouter/#pydantic_ai.models.openrouter.OpenRouterModel "OpenRouterModel") `ImageUrl`, `DocumentUrl` `AudioUrl` `VideoUrl`

A model API may be unable to download a file (e.g., because of crawling or access restrictions) even if it supports file URLs. For example, [`GoogleModel`](https://ai.pydantic.dev/api/models/google/#pydantic_ai.models.google.GoogleModel "GoogleModel            dataclass   ") on Vertex AI limits YouTube video URLs to one URL per request. In such cases, you can instruct Pydantic AI to download the file content locally and send that instead of the URL by setting `force_download` on the URL object:

force\_download.py

```
frompydantic_aiimport ImageUrl, AudioUrl, VideoUrl, DocumentUrl

ImageUrl(url='https://example.com/image.png', force_download=True)
AudioUrl(url='https://example.com/audio.mp3', force_download=True)
VideoUrl(url='https://example.com/video.mp4', force_download=True)
DocumentUrl(url='https://example.com/doc.pdf', force_download=True)
```

## Uploaded Files

Some model providers support passing URLs to files hosted on their platform:

- [`GoogleModel`](https://ai.pydantic.dev/api/models/google/#pydantic_ai.models.google.GoogleModel "GoogleModel            dataclass   ") supports the [Files API](https://ai.pydantic.dev/models/google/#document-image-audio-and-video-input) for uploading and referencing files.
- [`BedrockConverseModel`](https://ai.pydantic.dev/api/models/bedrock/#pydantic_ai.models.bedrock.BedrockConverseModel "BedrockConverseModel            dataclass   ") supports `s3://<bucket-name>/<object-key>` URIs, provided that the assumed role has the `s3:GetObject` permission. An optional `bucketOwner` query parameter must be specified if the bucket is not owned by the account making the request. For example: `s3://my-bucket/my-file.png?bucketOwner=123456789012`.