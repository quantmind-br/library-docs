---
title: Image Attachments
url: https://docs.perplexity.ai/docs/grounded-llm/media/image-attachments.md
source: llms
fetched_at: 2026-02-04T07:23:59.20343638-03:00
rendered_js: false
word_count: 357
summary: This document explains how to analyze images by attaching them to API requests via base64 encoding or HTTPS URLs. It details supported formats, file size limits, and provides implementation examples for both the Agentic Research and Chat Completions APIs.
tags:
    - image-analysis
    - base64-encoding
    - api-integration
    - vision-capabilities
    - file-attachments
    - image-upload
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Image Attachments

> Learn how to upload and analyze images using base64 encoding or HTTPS URLs

## Overview

Both the Agentic Research API and Chat Completions API support image analysis through direct image uploads. Images can be provided either as base64 encoded strings within a data URI or as standard HTTPS URLs.

<Warning>
  * When using base64 encoding, the API currently only supports images up to 50 MB per image.
  * Supported formats for base64 encoded images: PNG (image/png), JPEG (image/jpeg), WEBP (image/webp), and GIF (image/gif).
  * When using an HTTPS URL, the model will attempt to fetch the image from the provided URL. Ensure the URL is publicly accessible.
</Warning>

## Examples

<Tabs>
  <Tab title="Agentic Research API">
    <Tabs>
      <Tab title="Base64 Encoded Data">
        <Info>Use this method when you have the image file locally and want to embed it directly into the request payload. Remember the 50MB size limit and supported formats (PNG, JPEG, WEBP, GIF).</Info>

        <CodeGroup>
          ```python Python theme={null}
          import base64
          from perplexity import Perplexity

          client = Perplexity(api_key="pplx-KEY")

          # Read and encode image as base64
          def encode_image(image_path):
              with open(image_path, "rb") as image_file:
                  return base64.b64encode(image_file.read()).decode("utf-8")

          image_path = "image.png"
          base64_image = encode_image(image_path)

          # Analyze the image
          response = client.responses.create(
              model="openai/gpt-5-mini",
              input=[
                  {
                      "role": "user",
                      "content": [
                          {"type": "input_text", "text": "what's in this image?"},
                          {
                              "type": "input_image",
                              "image_url": f"data:image/png;base64,{base64_image}",
                          },
                      ],
                  }
              ],
          )

          print(response.output_text)
          ```

          ```typescript TypeScript theme={null}
          import Perplexity from '@perplexity-ai/perplexity_ai';
          import * as fs from 'fs';

          const client = new Perplexity();

          // Read and encode image as base64
          const imageBuffer = fs.readFileSync('image.png');
          const base64Image = imageBuffer.toString('base64');
          const imageDataUri = `data:image/png;base64,${base64Image}`;

          // Analyze the image
          const response = await client.responses.create({
              model: 'openai/gpt-5-mini',
              input: [
                  {
                      role: 'user',
                      content: [
                          { type: 'input_text', text: "What's in this image?" },
                          { type: 'input_image', image_url: imageDataUri }
                      ]
                  }
              ],
          });

          console.log(response.output_text);
          ```

          ```bash cURL theme={null}
          curl https://api.perplexity.ai/v1/responses \
            -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
            -H "Content-Type: application/json" \
            -d '{
              "model": "openai/gpt-5-mini",
              "input": [
                {
                  "role": "user",
                  "content": [
                    {
                      "type": "input_text",
                      "text": "What'\''s in this image?"
                    },
                    {
                      "type": "input_image",
                      "image_url": "data:image/png;base64,$BASE64_ENCODED_IMAGE"
                    }
                  ]
                }
              ]
            }' | jq
          ```
        </CodeGroup>
      </Tab>

      <Tab title="HTTPS URL">
        <Info>Use this method when you have a publicly accessible image URL. The model will fetch the image from the provided URL.</Info>

        <CodeGroup>
          ```python Python theme={null}
          from perplexity import Perplexity

          client = Perplexity(api_key="pplx-KEY")

          image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"

          # Analyze the image
          response = client.responses.create(
              model="openai/gpt-5-mini",
              input=[
                  {
                      "role": "user",
                      "content": [
                          {"type": "input_text", "text": "Can you describe the image at this URL?"},
                          {
                              "type": "input_image",
                              "image_url": image_url,
                          },
                      ],
                  }
              ],
          )

          print(response.output_text)
          ```

          ```typescript TypeScript theme={null}
          import Perplexity from '@perplexity-ai/perplexity_ai';

          const client = new Perplexity();

          const imageHttpsUrl = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg";

          // Analyze the image
          const response = await client.responses.create({
              model: 'openai/gpt-5-mini',
              input: [
                  {
                      role: 'user',
                      content: [
                          { type: 'input_text', text: 'Can you describe the image at this URL?' },
                          { type: 'input_image', image_url: imageHttpsUrl }
                      ]
                  }
              ],
          });

          console.log(response.output_text);
          ```

          ```bash cURL theme={null}
          curl https://api.perplexity.ai/v1/responses \
            -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
            -H "Content-Type: application/json" \
            -d '{
              "model": "openai/gpt-5-mini",
              "input": [
                {
                  "role": "user",
                  "content": [
                    {
                      "type": "input_text",
                      "text": "Can you describe the image at this URL?"
                    },
                    {
                      "type": "input_image",
                      "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
                    }
                  ]
                }
              ]
            }' | jq
          ```
        </CodeGroup>
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Chat Completions API">
    <Tabs>
      <Tab title="Base64 Encoded Data">
        <Info>Use this method when you have the image file locally and want to embed it directly into the request payload. Remember the 50MB size limit and supported formats (PNG, JPEG, WEBP, GIF).</Info>

        <CodeGroup>
          ```python Python theme={null}
          from perplexity import Perplexity
          import base64

          client = Perplexity()

          # Read and encode image as base64
          try:
              with open("path/to/your/image.png", "rb") as image_file:
                  base64_image = base64.b64encode(image_file.read()).decode("utf-8")
              image_data_uri = f"data:image/png;base64,{base64_image}"
          except FileNotFoundError:
              print("Error: Image file not found.")
              exit()

          # Analyze the image
          try:
              completion = client.chat.completions.create(
                  model="sonar-pro",
                  messages=[
                      {
                          "role": "user",
                          "content": [
                              {"type": "text", "text": "Can you describe this image?"},
                              {"type": "image_url", "image_url": {"url": image_data_uri}}
                          ]
                      }
                  ]
              )
              print(completion.choices[0].message.content)
          except Exception as e:
              print(f"API Request failed: {e}")
          ```

          ```typescript TypeScript theme={null}
          import Perplexity from '@perplexity-ai/perplexity_ai';
          import * as fs from 'fs';

          const client = new Perplexity();

          // Read and encode image as base64
          try {
              const imageBuffer = fs.readFileSync('path/to/your/image.png');
              const base64Image = imageBuffer.toString('base64');
              const imageDataUri = `data:image/png;base64,${base64Image}`;
              
              // Analyze the image
              const completion = await client.chat.completions.create({
                  model: 'sonar-pro',
                  messages: [
                      {
                          role: 'user',
                          content: [
                              { type: 'text', text: 'Can you describe this image?' },
                              { type: 'image_url', image_url: { url: imageDataUri } }
                          ]
                      }
                  ]
              });
              
              console.log(completion.choices[0].message.content);
          } catch (error) {
              console.error('Error:', error.message);
          }
          ```

          ```bash cURL theme={null}
          curl --location 'https://api.perplexity.ai/chat/completions' \
            --header 'accept: application/json' \
            --header 'content-type: application/json' \
            --header "Authorization: Bearer $PERPLEXITY_API_KEY" \
            --data '{
              "model": "sonar-pro",
              "stream": false,
              "messages": [
                {
                  "role": "user",
                  "content": [
                    {
                      "type": "text",
                      "text": "Can you describe this image?"
                    },
                    {
                      "type": "image_url",
                      "image_url": {
                        "url": "data:image/png;base64,$BASE64_ENCODED_IMAGE"
                      }
                    }
                  ]
                }
              ]
            }' | jq
          ```
        </CodeGroup>
      </Tab>

      <Tab title="HTTPS URL">
        <Info>Use this method to reference an image hosted online. Ensure the URL is publicly accessible and points directly to the image file.</Info>

        <CodeGroup>
          ```python Python theme={null}
          from perplexity import Perplexity

          client = Perplexity()

          image_https_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"

          # Analyze the image
          try:
              completion = client.chat.completions.create(
                  model="sonar-pro",
                  messages=[
                      {
                          "role": "user",
                          "content": [
                              {"type": "text", "text": "Can you describe the image at this URL?"},
                              {"type": "image_url", "image_url": {"url": image_https_url}}
                          ]
                      }
                  ]
              )
              print(completion.choices[0].message.content)
          except Exception as e:
              print(f"API Request failed: {e}")
          ```

          ```typescript TypeScript theme={null}
          import Perplexity from '@perplexity-ai/perplexity_ai';

          const client = new Perplexity();

          const imageHttpsUrl = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg";

          // Analyze the image
          const analyzeImage = async (): Promise<void> => {
              try {
                  const completion = await client.chat.completions.create({
                      model: 'sonar-pro',
                      messages: [
                          {
                              role: 'user',
                              content: [
                                  { type: 'text', text: 'Can you describe the image at this URL?' },
                                  { type: 'image_url', image_url: { url: imageHttpsUrl } }
                              ]
                          }
                      ]
                  });
                  
                  console.log(completion.choices[0].message.content);
              } catch (error) {
                  console.error('API Request failed:', error.message);
              }
          };

          analyzeImage();
          ```

          ```bash cURL theme={null}
          curl --location 'https://api.perplexity.ai/chat/completions' \
            --header "accept: application/json" \
            --header "content-type: application/json" \
            --header "Authorization: Bearer $PERPLEXITY_API_KEY" \
            --data '{
              "model": "sonar-pro",
              "stream": false,
              "messages": [
                {
                  "role": "user",
                  "content": [
                    {
                      "type": "text",
                      "text": "Can you describe the image at this URL?"
                    },
                    {
                      "type": "image_url",
                      "image_url": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
                      }
                    }
                  ]
                }
              ]
            }' | jq
          ```
        </CodeGroup>
      </Tab>
    </Tabs>
  </Tab>
</Tabs>

## Request Format

### Agentic Research API

Images must be embedded in the `input` array when using message array format. Each image should be provided using the following structure:

```json  theme={null}
{
  "role": "user",
  "content": [
    {
      "type": "input_text",
      "text": "What's in this image?"
    },
    {
      "type": "input_image",
      "image_url": "<IMAGE_URL_OR_BASE64_DATA>"
    }
  ]
}
```

The `image_url` field accepts either:

* **A URL of the image**: A publicly accessible HTTPS URL pointing directly to the image file
* **The base64 encoded image data**: A data URI in the format `data:image/{format};base64,{base64_content}`

### Chat Completions API

Images must be embedded in the `messages` array, alongside any text input. Each image should be provided using the following structure:

```json  theme={null}
{
  "type": "image_url",
  "image_url": {
    "url": "<IMAGE_URL_OR_BASE64_DATA>"
  }
}
```

The `url` field accepts either:

* **A URL of the image**: A publicly accessible HTTPS URL pointing directly to the image file
* **The base64 encoded image data**: A data URI in the format `data:image/{format};base64,{base64_content}`

## Pricing

Images are tokenized based on their pixel dimensions using the following formula:

```
tokens = (width px × height px) / 750
```

**Examples:**

* A 1024×768 image would consume: (1024 × 768) / 750 = 1,048 tokens
* A 512×512 image would consume: (512 × 512) / 750 = 349 tokens

These image tokens are then priced according to the input token pricing of the model you're using. The image tokens are added to your total token count for the request alongside any text tokens.

## Next Steps

<CardGroup cols={2}>
  <Card title="Agentic Research API Quickstart" icon="rocket" href="/docs/grounded-llm/responses/quickstart">
    Get started with the Agentic Research API
  </Card>

  <Card title="Chat Completions API Quickstart" icon="message" href="/docs/grounded-llm/chat-completions/quickstart">
    Get started with the Chat Completions API
  </Card>

  <Card title="Tools" icon="wrench" href="/docs/grounded-llm/responses/tools">
    Learn about web\_search and fetch\_url tools
  </Card>

  <Card title="Models" icon="brain" href="/docs/grounded-llm/responses/models">
    Explore available models for image analysis
  </Card>
</CardGroup>