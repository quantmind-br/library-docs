---
title: Quick Start
url: https://docs.z.ai/guides/overview/quick-start.md
source: llms
fetched_at: 2026-01-24T11:23:21.938886269-03:00
rendered_js: false
word_count: 123
summary: This guide provides a step-by-step introduction to getting started with the Z.AI Open Platform, covering API key acquisition, model selection, and initial implementation using SDKs or HTTP requests.
tags:
    - quick-start
    - api-integration
    - z-ai-platform
    - python-sdk
    - java-sdk
    - glm-models
    - api-key
category: tutorial
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.z.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Quick Start

<Info>
  Tired of limits? GLM Coding Plan — monthly access to world-class model GLM-4.7, compatible with top coding tools like Claude Code and Cline. All from just \$3/month. [Try it now →](https://z.ai/subscribe?utm_campaign=Platform_Ops&_channel_track_key=DaprgHIc)
</Info>

<Tip>
  **Black Friday**: Enjoy 50% off your first GLM Coding Plan purchase, plus an extra 20%/30% off! [Subscribe](https://z.ai/subscribe?utm_source=z.ai\&utm_medium=link\&utm_term=glm-devpack\&utm_campaign=Platform_Ops&_channel_track_key=jFgqJREK) now.
</Tip>

## Getting Started

<Steps>
  <Step title="Get API Key">
    * Access [Z.AI Open Platform](https://z.ai/model-api), Register or Login.
    * Access [Billing Page](https://z.ai/manage-apikey/billing) to top up if needed.
    * Create an API Key in the [API Keys](https://z.ai/manage-apikey/apikey-list) management page.
    * Copy your API Key for use.
      <CardGroup cols={2}>
        <Card title="Z.AI Open Platform" icon="link" href="https://z.ai/model-api">
          Access [Z.AI Open Platform](https://z.ai/model-api), Register or Login.
        </Card>

        <Card title="API Keys Management" icon="link" href="https://z.ai/manage-apikey/apikey-list">
          Create an API Key in the [API Keys](https://z.ai/manage-apikey/apikey-list) management page.
        </Card>
      </CardGroup>
  </Step>

  <Step title="Choose Model">
    > The platform offers multiple models, and you can select the appropriate model based on your needs. For detailed model introductions, please refer to the [Models & Agents](pricing).

    <CardGroup cols={2}>
      <Card title="GLM-4.7" icon="book-open" href="/guides/llm/glm-4.7">
        Our latest flagship model, delivering open-source SOTA performance and superior Agentic Coding Experience
      </Card>

      <Card title="GLM-4.6V" icon="eyes" href="/guides/vlm/glm-4.6v">
        New multimodal model with 128K training context window and SOTA vision understanding
      </Card>

      <Card title="GLM-Image" icon="image" href="/guides/image/glm-image">
        Supports text-to-image generation, achieving open-source state-of-the-art (SOTA) in complex scenarios
      </Card>

      <Card title="CogVideoX-3" icon="video" href="/guides/video/cogvideox-3">
        New frame generation capabilities that significantly improve image stability and clarity
      </Card>
    </CardGroup>
  </Step>

  <Step title="Choose the Calling Method">
    Our platform provides various development approaches; you can select the best fit for your project needs and tech stack.

    <CardGroup cols={2}>
      <Card title="HTTP API" icon="globe" href="/guides/develop/http/introduction">
        Standard RESTful API, compatible with all programming languages.
      </Card>

      <Card title="Z.AI Python SDK" icon="python" href="/guides/develop/python/introduction">
        Official Python SDK, featuring full type hints and async support.
      </Card>

      <Card title="Z.AI Java SDK" icon="java" href="/guides/develop/java/introduction">
        Official Java SDK, designed for high concurrency and availability.
      </Card>

      <Card title="OpenAI Python SDK" icon="python" href="/guides/develop/openai/python">
        OpenAI SDK Compatibility, quickly migrating from OpenAI.
      </Card>

      <Card title="API Reference" icon="book" href="/api-reference">
        Complete API documentation with parameter descriptions.
      </Card>
    </CardGroup>
  </Step>

  <Step title="Make API Call">
    After preparing your `API Key` and selecting a model, you can start making API calls. Here are examples using `curl`, `Python SDK`, and `Java SDK`:

    <Tabs>
      <Tab title="cURL">
        <Warning>
          Note: When using the [GLM Coding Plan](/devpack/overview), you need to configure the dedicated \
          Coding endpoint - [https://api.z.ai/api/coding/paas/v4](https://api.z.ai/api/coding/paas/v4) \
          instead of the general endpoint - [https://api.z.ai/api/paas/v4](https://api.z.ai/api/paas/v4) \
          Note: The Coding API endpoint is only for Coding scenarios and is not applicable to general API scenarios. Please use them accordingly.
        </Warning>

        ```bash  theme={null}
        curl -X POST "https://api.z.ai/api/paas/v4/chat/completions" \
        -H "Content-Type: application/json" \
        -H "Accept-Language: en-US,en" \
        -H "Authorization: Bearer YOUR_API_KEY" \
        -d '{
            "model": "glm-4.7",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant."
                },
                {
                    "role": "user",
                    "content": "Hello, please introduce yourself."
                }
            ]
        }'
        ```
      </Tab>

      <Tab title="Official Python SDK">
        **Install SDK**

        ```bash  theme={null}
        # Install latest version
        pip install zai-sdk

        # Or specify version
        pip install zai-sdk==0.1.0
        ```

        **Verify Installation**

        ```python  theme={null}
        import zai
        print(zai.__version__)
        ```

        **Usage Example**

        ```python  theme={null}
        from zai import ZaiClient

        # Initialize client
        client = ZaiClient(api_key="YOUR_API_KEY")

        # Create chat completion request
        response = client.chat.completions.create(
            model="glm-4.7",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant."
                },
                {
                    "role": "user",
                    "content": "Hello, please introduce yourself."
                }
            ]
        )

        # Get response
        print(response.choices[0].message.content)
        ```
      </Tab>

      <Tab title="Official Java SDK">
        **Install SDK**

        **Maven**

        ```xml  theme={null}
        <dependency>
            <groupId>ai.z.openapi</groupId>
            <artifactId>zai-sdk</artifactId>
            <version>0.3.0</version>
        </dependency>
        ```

        **Gradle (Groovy)**

        ```groovy  theme={null}
        implementation 'ai.z.openapi:zai-sdk:0.3.0'
        ```

        **Usage Example**

        ```java  theme={null}
        import ai.z.openapi.ZaiClient;
        import ai.z.openapi.service.model.*;
        import java.util.Arrays;

        public class QuickStart {
            public static void main(String[] args) {
                // Initialize client
                ZaiClient client = ZaiClient.builder().ofZAI()
                    .apiKey("YOUR_API_KEY")
                    .build();

                // Create chat completion request
                ChatCompletionCreateParams request = ChatCompletionCreateParams.builder()
                    .model("glm-4.7")
                    .messages(Arrays.asList(
                        ChatMessage.builder()
                            .role(ChatMessageRole.USER.value())
                            .content("Hello, who are you?")
                            .build()
                    ))
                    .stream(false)
                    .build();

                // Send request
                ChatCompletionResponse response = client.chat().createChatCompletion(request);

                // Get response
                System.out.println(response.getData().getChoices().get(0).getMessage().getContent());
            }
        }
        ```
      </Tab>

      <Tab title="OpenAI Python SDK">
        **Install SDK**

        ```bash  theme={null}
        # Install or upgrade to latest version
        pip install --upgrade 'openai>=1.0'
        ```

        **Verify Installation**

        ```python  theme={null}
        python -c "import openai; print(openai.__version__)"
        ```

        **Usage Example**

        ```python  theme={null}
        from openai import OpenAI

        client = OpenAI(
            api_key="your-Z.AI-api-key",
            base_url="https://api.z.ai/api/paas/v4/"
        )

        completion = client.chat.completions.create(
            model="glm-4.7",
            messages=[
                {"role": "system", "content": "You are a smart and creative novelist"},
                {"role": "user", "content": "Please write a short fairy tale story as a fairy tale master"}
            ]
        )

        print(completion.choices[0].message.content)
        ```
      </Tab>

      <Tab title="OpenAI NodeJs SDK">
        **Install SDK**

        ```bash  theme={null}
        # Install or upgrade to latest version
        npm install openai

        # Or using yarn
        yarn add openai
        ```

        **Usage Example**

        ```javascript  theme={null}
        import OpenAI from "openai";

        const client = new OpenAI({
            apiKey: "your-Z.AI-api-key",
            baseURL: "https://api.z.ai/api/paas/v4/"
        });

        async function main() {
            const completion = await client.chat.completions.create({
                model: "glm-4.7",
                messages: [
                    { role: "system", content: "You are a helpful AI assistant." },
                    { role: "user", content: "Hello, please introduce yourself." }
                ]
            });

            console.log(completion.choices[0].message.content);
        }

        main();
        ```
      </Tab>

      <Tab title="OpenAI Java SDK">
        **Install SDK**

        **Maven**

        ```xml  theme={null}
        <dependency>
            <groupId>com.openai</groupId>
            <artifactId>openai-java</artifactId>
            <version>2.20.1</version>
        </dependency>
        ```

        **Gradle (Groovy)**

        ```groovy  theme={null}
        implementation 'com.openai:openai-java:2.20.1'
        ```

        **Usage Example**

        ```java  theme={null}
        import com.openai.client.OpenAIClient;
        import com.openai.client.okhttp.OpenAIOkHttpClient;
        import com.openai.models.chat.completions.ChatCompletion;
        import com.openai.models.chat.completions.ChatCompletionCreateParams;

        public class QuickStart {
            public static void main(String[] args) {
                // Initialize client
                OpenAIClient client = OpenAIOkHttpClient.builder()
                    .apiKey("your-Z.AI-api-key")
                    .baseUrl("https://api.z.ai/api/paas/v4/")
                    .build();

                // Create chat completion request
                ChatCompletionCreateParams params = ChatCompletionCreateParams.builder()
                    .addSystemMessage("You are a helpful AI assistant.")
                    .addUserMessage("Hello, please introduce yourself.")
                    .model("glm-4.7")
                    .build();

                // Send request and get response
                ChatCompletion chatCompletion = client.chat().completions().create(params);
                Object response = chatCompletion.choices().get(0).message().content();

                System.out.println(response);
            }
        }
        ```
      </Tab>
    </Tabs>
  </Step>
</Steps>

### Get More

<CardGroup cols={3}>
  <Card title="API Reference" icon="book" href="/api-reference">
    Access API Reference.
  </Card>

  <Card title="Python SDK" icon="python" href="https://github.com/zai-org/z-ai-sdk-python">
    Access Python SDK Github
  </Card>

  <Card title="Java SDK" icon="java" href="https://github.com/zai-org/z-ai-sdk-java">
    Access Java SDK Github
  </Card>
</CardGroup>