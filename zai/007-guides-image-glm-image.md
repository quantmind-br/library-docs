---
title: GLM-Image - Overview - Z.AI DEVELOPER DOCUMENT
url: https://docs.z.ai/guides/image/glm-image
source: llms
fetched_at: 2026-01-24T11:22:10.441330151-03:00
rendered_js: false
word_count: 98
summary: This document introduces Z.AI's GLM-Image generation model and provides quick-start instructions for integrating it via API and SDKs in Python and Java.
tags:
    - image-generation
    - glm-image
    - ai-sdk
    - python
    - java
    - api-integration
category: tutorial
---

GLM-Image is Z.AI’s new flagship image generation model, which adopts an original hybrid architecture of “autoregressive + diffusion decoder”, taking into account both global instruction understanding and local detail portrayal, overcoming the challenges in generating knowledge-intensive scenarios such as posters, PPTs, and science popularization diagrams. It represents an important exploration of the new generation of “cognitive generative” technology paradigm represented by Nano Banana Pro.

## Usage

## Resources

- [API Documentation](https://docs.z.ai/api-reference/image/generate-image): Learn how to call the API.

## Introducting GLM-Image

## Examples

- High-Quality Portraits
- Commercial Poster

## Quick Start

- cURL
- Python
- Java

```
curl --request POST \
--url https://api.z.ai/api/paas/v4/images/generations \
--header 'Authorization: Bearer <token>' \
--header 'Content-Type: application/json' \
--data '{
    "model": "glm-image",
    "prompt": "A cute little kitten sitting on a sunny windowsill, with the background of blue sky and white clouds.",
    "size": "1280x1280"
}'
```

**Install SDK**

```
# Install latest version
pip install zai-sdk

# Or specify version
pip install zai-sdk==0.2.1
```

**Verify Installation**

```
import zai
print(zai.__version__)
```

**Call Example**

```
from zai import ZaiClient
client = ZaiClient(api_key="your-api-key")
response = client.images.generations(
    model="glm-image",
    prompt="A cute little kitten sitting on a sunny windowsill, with the background of blue sky and white clouds.",
)
print(response.data[0].url)
```

**Install SDK****Maven**

```
<dependency>
    <groupId>ai.z.openapi</groupId>
    <artifactId>zai-sdk</artifactId>
    <version>0.3.2</version>
</dependency>
```

**Gradle (Groovy)**

```
implementation 'ai.z.openapi:zai-sdk:0.3.2'
```

**Call Example**

```
import ai.z.openapi.ZaiClient;
import ai.z.openapi.core.Constants;
import ai.z.openapi.service.image.CreateImageRequest;
import ai.z.openapi.service.image.ImageResponse;

public class GlmImageExample {
    public static void main(String[] args) {
        ZaiClient client = ZaiClient.builder().ofZAI().apiKey("YOUR_API_KEY").build();
        // Create image generation request
        CreateImageRequest request = CreateImageRequest.builder()
                .model("glm-image")
                .prompt("A cute little kitten sitting on a sunny windowsill, with the background of blue sky and white clouds.")
                .size("1280x1280")
                .build();
        ImageResponse response = client.images().createImage(request);
        System.out.println(response.getData());
    }
}
```