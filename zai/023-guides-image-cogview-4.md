---
title: CogView-4
url: https://docs.z.ai/guides/image/cogview-4.md
source: llms
fetched_at: 2026-01-24T11:23:14.162695454-03:00
rendered_js: false
word_count: 262
summary: This document introduces CogView-4, an open-source bilingual text-to-image model by Z.AI that supports variable resolutions and prompt lengths.
tags:
    - cogview-4
    - text-to-image
    - image-generation
    - bilingual-model
    - ai-models
    - open-source
    - computer-vision
category: concept
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.z.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# CogView-4

## <Icon icon="rectangle-list" iconType="solid" color="#ffffff" size={36} />   Overview

CogView-4 is Z.AI’s first open-source text-to-image model. It has comprehensive improvements in semantic understanding, image generation quality, and the ability to generate both English and Chinese text. It supports bilingual input of any length in Chinese and English and can generate images of any resolution within a specified range.

<CardGroup cols={3}>
  <Card title="Price" icon="circle-dollar" color="#ffffff">
    \$0.01 / image
  </Card>

  <Card title="Input Modality" icon="arrow-down-right" color="#ffffff">
    Text
  </Card>

  <Card title="Output Modality" icon="arrow-down-left" color="#ffffff">
    Image
  </Card>
</CardGroup>

## <Icon icon="list" iconType="solid" color="#ffffff" size={36} />   Usage

<AccordionGroup>
  <Accordion title="Food & Beverage Promotion">
    Generates visually appealing, detailed, and realistic food images based on dish names, ingredient characteristics, and style requirements, incorporating creative text elements. Suitable for menu design, food delivery platform displays, and offline posters.
  </Accordion>

  <Accordion title="E-commerce Product Images">
    Quickly generates high-resolution product display images based on product features and selling points, adding bilingual promotional text as needed. Fits the image requirements for different product pages and campaign visuals on e-commerce platforms.
  </Accordion>

  <Accordion title="Game Asset Creation">
    Produces high-resolution, detailed character illustrations and concept art based on game worldviews and character settings, meeting the needs of multi-resolution production.
  </Accordion>

  <Accordion title="Educational Material Illustrations">
    Analyzes teaching text content and automatically generates matching illustrations and scene images, adapted to the layout and resolution requirements of various educational materials, enhancing the visualization of knowledge.
  </Accordion>

  <Accordion title="Cultural & Tourism Promotion">
    Generates promotional images in different sizes based on cultural and tourism themes, skillfully combining text with region-specific visual elements to increase the appeal of cultural and tourism marketing.
  </Accordion>
</AccordionGroup>

## <Icon icon="bars-sort" iconType="solid" color="#ffffff" size={36} />   Resources

* [API Documentation](/api-reference/image/generate-image): Learn how to call the API.

## <Icon icon="arrow-down-from-line" iconType="solid" color="#ffffff" size={36} />   Introducting CogView-4

<Steps>
  <Step title="Achieved SOTA Performance at Release" titleSize="h3">
    DPG-Bench (Dense Prompt Graph Benchmark) is a benchmark for evaluating text-to-image generation models, focusing on the model’s performance in complex semantic alignment and instruction following.

    At the time of release, CogView-4 ranked first overall in the DPG-Bench benchmark test, achieving SOTA performance among open-source text-to-image models.

    ![Description](https://cdn.bigmodel.cn/markdown/1749449849627DPG-Bench.png?attname=DPG-Bench.png)
  </Step>

  <Step title="Better Chinese Understanding and Generation" iconType="regular" stepNumber={2} titleSize="h3">
    Technically, CogView-4 replaced the English-only T5 encoder with the bilingual GLM-4 encoder and trained the model using bilingual image-text data, enabling the model to handle bilingual prompts.

    CogView-4 supports Chinese and English prompts and is especially good at understanding and following Chinese prompts, greatly lowering the prompt threshold for users. It is the first open-source text-to-image model capable of generating Chinese characters in the images, making it particularly suitable for creative needs in advertising, short videos, and other fields.
  </Step>

  <Step title="Any Resolution and Any-Length Prompts" iconType="regular" stepNumber={3} titleSize="h3">
    CogView-4 implements a mixed training paradigm of text descriptions (captions) of any length and images of any resolution. The model supports input prompts of any length and can generate images at any resolution within the supported range. This not only provides users with more creative freedom but also improves training efficiency.
  </Step>
</Steps>

## <Icon icon="objects-column" iconType="solid" color="#ffffff" size={36} />    Examples

<Tabs>
  <Tab title="Food & Beverage Promotion">
    <CardGroup cols={2}>
      <Card title="Prompt" icon="arrow-down-right">
        Close-up, commercial food photography, intense indoor lighting, extreme detail. A Christmas dinner table, a corner of the table where a long-haired orange tabby cat leans its head close to a plate, greedily sniffing the festive feast with an expression of pure delight. The table features roast chicken, plants, salad, champagne, and gold-rimmed porcelain tea sets. Afternoon sunlight bathes the cat's profile in golden light, casting a soft glow over both the food and its fur. A Christmas tree adorns the background. The image emphasizes the texture of the food and the cat's coat, featuring strong lighting and a warm, festive Christmas atmosphere.
      </Card>

      <Card title="Display" icon="arrow-down-left">
                <img src="https://mintcdn.com/zhipu-32152247/aOvZujLeW4WS84Ft/resource/cogview-1.png?fit=max&auto=format&n=aOvZujLeW4WS84Ft&q=85&s=6e96f8a615cfdd325a7abb4369d6396c" alt="Description" data-og-width="1728" width="1728" data-og-height="2304" height="2304" data-path="resource/cogview-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zhipu-32152247/aOvZujLeW4WS84Ft/resource/cogview-1.png?w=280&fit=max&auto=format&n=aOvZujLeW4WS84Ft&q=85&s=a19fc7f595290d118b94534ecc7ad544 280w, https://mintcdn.com/zhipu-32152247/aOvZujLeW4WS84Ft/resource/cogview-1.png?w=560&fit=max&auto=format&n=aOvZujLeW4WS84Ft&q=85&s=d391a485c5c270d9c6391ad33a3f2730 560w, https://mintcdn.com/zhipu-32152247/aOvZujLeW4WS84Ft/resource/cogview-1.png?w=840&fit=max&auto=format&n=aOvZujLeW4WS84Ft&q=85&s=1ade18484e7976971d65e7c43f22872b 840w, https://mintcdn.com/zhipu-32152247/aOvZujLeW4WS84Ft/resource/cogview-1.png?w=1100&fit=max&auto=format&n=aOvZujLeW4WS84Ft&q=85&s=aacbddb2a32992143fc737dba6c69676 1100w, https://mintcdn.com/zhipu-32152247/aOvZujLeW4WS84Ft/resource/cogview-1.png?w=1650&fit=max&auto=format&n=aOvZujLeW4WS84Ft&q=85&s=a453d68a5b17d6f330a9849dd020c6fa 1650w, https://mintcdn.com/zhipu-32152247/aOvZujLeW4WS84Ft/resource/cogview-1.png?w=2500&fit=max&auto=format&n=aOvZujLeW4WS84Ft&q=85&s=7446f52bcc6ce7c665f4e7da1262f9c9 2500w" />
      </Card>
    </CardGroup>
  </Tab>

  <Tab title="E-commerce Product Images">
    <CardGroup cols={2}>
      <Card title="Prompt" icon="arrow-down-right">
        Two opaque, non-reflective white milk tea cups are adorned with intricate golden patterns of varying sizes. The designs feature Christmas motifs, including reindeer and pine trees, set against a warm red background and twinkling holiday lights. Displayed within a miniature snow scene, they are illuminated by natural light.
      </Card>

      <Card title="Display" icon="arrow-down-left">
                <img src="https://mintcdn.com/zhipu-32152247/aOvZujLeW4WS84Ft/resource/cogview-2.png?fit=max&auto=format&n=aOvZujLeW4WS84Ft&q=85&s=e7b595d49b108120be3ceb86d55f17ab" alt="Description" data-og-width="880" width="880" data-og-height="1168" height="1168" data-path="resource/cogview-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zhipu-32152247/aOvZujLeW4WS84Ft/resource/cogview-2.png?w=280&fit=max&auto=format&n=aOvZujLeW4WS84Ft&q=85&s=53bc30812b67ed18daaf00a1d0730769 280w, https://mintcdn.com/zhipu-32152247/aOvZujLeW4WS84Ft/resource/cogview-2.png?w=560&fit=max&auto=format&n=aOvZujLeW4WS84Ft&q=85&s=bbc2bf99e7626f33aceedd8da23024db 560w, https://mintcdn.com/zhipu-32152247/aOvZujLeW4WS84Ft/resource/cogview-2.png?w=840&fit=max&auto=format&n=aOvZujLeW4WS84Ft&q=85&s=f4e7936b1dcf0a30396022c0d4d2348f 840w, https://mintcdn.com/zhipu-32152247/aOvZujLeW4WS84Ft/resource/cogview-2.png?w=1100&fit=max&auto=format&n=aOvZujLeW4WS84Ft&q=85&s=11313078ce6c43d276787fbf9d9e944c 1100w, https://mintcdn.com/zhipu-32152247/aOvZujLeW4WS84Ft/resource/cogview-2.png?w=1650&fit=max&auto=format&n=aOvZujLeW4WS84Ft&q=85&s=06a63565416aa7c5df3d39d907d68f4a 1650w, https://mintcdn.com/zhipu-32152247/aOvZujLeW4WS84Ft/resource/cogview-2.png?w=2500&fit=max&auto=format&n=aOvZujLeW4WS84Ft&q=85&s=04787ea69652748330ac5545c2e12407 2500w" />
      </Card>
    </CardGroup>
  </Tab>

  <Tab title="Game Asset Creation">
    <CardGroup cols={2}>
      <Card title="Prompt" icon="arrow-down-right">
        Cyberpunk samurai with a glowing katana and a robotic arm, standing in a neon-lit alley in Tokyo, rain reflecting on the wet pavement, Blade Runner aesthetic, cinematic, highly detailed, volumetric lighting -- ar 2:3.
      </Card>

      <Card title="Display" icon="arrow-down-left">
                <img src="https://mintcdn.com/zhipu-32152247/aOvZujLeW4WS84Ft/resource/cogview-3.png?fit=max&auto=format&n=aOvZujLeW4WS84Ft&q=85&s=a0afa1d589085bd9ce87d148be38a55f" alt="Description" data-og-width="2048" width="2048" data-og-height="2048" height="2048" data-path="resource/cogview-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zhipu-32152247/aOvZujLeW4WS84Ft/resource/cogview-3.png?w=280&fit=max&auto=format&n=aOvZujLeW4WS84Ft&q=85&s=96aa9afd478f344dab64b0175f77dd13 280w, https://mintcdn.com/zhipu-32152247/aOvZujLeW4WS84Ft/resource/cogview-3.png?w=560&fit=max&auto=format&n=aOvZujLeW4WS84Ft&q=85&s=8b946b544e0f338e70c8d6f11da94bf3 560w, https://mintcdn.com/zhipu-32152247/aOvZujLeW4WS84Ft/resource/cogview-3.png?w=840&fit=max&auto=format&n=aOvZujLeW4WS84Ft&q=85&s=365218e5e2483dbbadbf6a8730889507 840w, https://mintcdn.com/zhipu-32152247/aOvZujLeW4WS84Ft/resource/cogview-3.png?w=1100&fit=max&auto=format&n=aOvZujLeW4WS84Ft&q=85&s=7ed8bf693c960cb8e85b0a1586944ac0 1100w, https://mintcdn.com/zhipu-32152247/aOvZujLeW4WS84Ft/resource/cogview-3.png?w=1650&fit=max&auto=format&n=aOvZujLeW4WS84Ft&q=85&s=34c2a09edae2a2adfa3875fc3b2372d8 1650w, https://mintcdn.com/zhipu-32152247/aOvZujLeW4WS84Ft/resource/cogview-3.png?w=2500&fit=max&auto=format&n=aOvZujLeW4WS84Ft&q=85&s=44412985928b84da190b4c31fdf119d8 2500w" />
      </Card>
    </CardGroup>
  </Tab>

  <Tab title="Cultural & Tourism Promotion">
    <CardGroup cols={2}>
      <Card title="Prompt" icon="arrow-down-right">
        The dazzling nightscape of Victoria Harbour in Hong Kong employs double exposure techniques to seamlessly blend the bustling city skyline with spectacular fireworks. Multiple fireworks burst across the night sky, forming a massive heart shape perfectly superimposed at the center of the frame. The fireworks display a kaleidoscope of colors—gold, red, blue, and purple intertwine, illuminating the entire night sky. City lights twinkle in the background, with skyscraper silhouettes clearly visible. Neon lights along the streets accentuate the city's vibrant energy. The entire scene exudes a dreamlike and romantic atmosphere, immersing the viewer in the dazzling nightscape of Hong Kong.
      </Card>

      <Card title="Display" icon="arrow-down-left">
                <img src="https://mintcdn.com/zhipu-32152247/aOvZujLeW4WS84Ft/resource/cogview-4.png?fit=max&auto=format&n=aOvZujLeW4WS84Ft&q=85&s=d2148db796d13648704782164136b699" alt="Description" data-og-width="864" width="864" data-og-height="1152" height="1152" data-path="resource/cogview-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zhipu-32152247/aOvZujLeW4WS84Ft/resource/cogview-4.png?w=280&fit=max&auto=format&n=aOvZujLeW4WS84Ft&q=85&s=2626f3595bb8e6b543c860de073c9a8f 280w, https://mintcdn.com/zhipu-32152247/aOvZujLeW4WS84Ft/resource/cogview-4.png?w=560&fit=max&auto=format&n=aOvZujLeW4WS84Ft&q=85&s=94d2741f00fa9e43cdbb0fcc62767949 560w, https://mintcdn.com/zhipu-32152247/aOvZujLeW4WS84Ft/resource/cogview-4.png?w=840&fit=max&auto=format&n=aOvZujLeW4WS84Ft&q=85&s=086d8d8b9f1e9d0cbe746ef3db9e1dee 840w, https://mintcdn.com/zhipu-32152247/aOvZujLeW4WS84Ft/resource/cogview-4.png?w=1100&fit=max&auto=format&n=aOvZujLeW4WS84Ft&q=85&s=0cde8bad17b5709f82c1c49a78026986 1100w, https://mintcdn.com/zhipu-32152247/aOvZujLeW4WS84Ft/resource/cogview-4.png?w=1650&fit=max&auto=format&n=aOvZujLeW4WS84Ft&q=85&s=a617b3aa240010cab36535366adcc391 1650w, https://mintcdn.com/zhipu-32152247/aOvZujLeW4WS84Ft/resource/cogview-4.png?w=2500&fit=max&auto=format&n=aOvZujLeW4WS84Ft&q=85&s=bec67440709554e213fe1335e7db24b4 2500w" />
      </Card>
    </CardGroup>
  </Tab>
</Tabs>

## <Icon icon="rectangle-code" iconType="solid" color="#ffffff" size={36} />    Quick Start

<Tabs>
  <Tab title="cURL">
    ```
    curl --request POST \
    --url https://api.z.ai/api/paas/v4/images/generations \
    --header 'Authorization: Bearer <token>' \
    --header 'Content-Type: application/json' \
    --data '{
        "model": "cogView-4-250304",
        "prompt": "A cute little kitten sitting on a sunny windowsill, with the background of blue sky and white clouds.",
        "size": "1024x1024"
    }'
    ```
  </Tab>

  <Tab title="Python">
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

    **Call Example**

    ```python  theme={null}
    from zai import ZaiClient
    client = ZaiClient(api_key="your-api-key")
    response = client.images.generations(
    model="cogView-4-250304",
    prompt="A cute little kitten sitting on a sunny windowsill, with the background of blue sky and white clouds.",
    )
    print(response.data[0].url)
    ```
  </Tab>

  <Tab title="Java">
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

    **Call Example**

    ```java  theme={null}
    import ai.z.openapi.ZaiClient;
    import ai.z.openapi.core.Constants;
    import ai.z.openapi.service.image.CreateImageRequest;
    import ai.z.openapi.service.image.ImageResponse;

    public class CogView4Example {
    public static void main(String[] args) {
    ZaiClient client = ZaiClient.builder().ofZAI().apiKey("YOUR_API_KEY").build();
    // Create image generation request
    CreateImageRequest request = CreateImageRequest.builder()
    .model(Constants.ModelCogView4250304)
    .prompt("A cute little kitten sitting on a sunny windowsill, with the background of blue sky and white clouds.")
    .size("1024x1024")
    .build();
    ImageResponse response = client.images().createImage(request);
    System.out.println(response.getData());
    }
    }
    ```
  </Tab>
</Tabs>

<Tip>
  Please note that the output of the CogView-4 model is an image URL. You will need to download the image using this URL.
</Tip>