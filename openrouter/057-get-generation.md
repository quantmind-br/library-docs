---
title: Get request & usage metadata for a generation
url: https://openrouter.ai/docs/api/api-reference/generations/get-generation.mdx
source: llms
fetched_at: 2026-02-13T15:17:56.574803-03:00
rendered_js: false
word_count: 17
summary: This document provides the OpenAPI specification for the OpenRouter API endpoint used to retrieve detailed request and usage metadata for specific AI generations. It details the necessary parameters, authentication requirements, and the comprehensive response schema including token counts, costs, and latency metrics.
tags:
    - openrouter
    - api-reference
    - generation-metadata
    - usage-tracking
    - token-usage
    - openapi-specification
category: api
---

# Get request & usage metadata for a generation

GET https://openrouter.ai/api/v1/generation

Reference: https://openrouter.ai/docs/api/api-reference/generations/get-generation

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get request & usage metadata for a generation
  version: endpoint_generations.getGeneration
paths:
  /generation:
    get:
      operationId: get-generation
      summary: Get request & usage metadata for a generation
      tags:
        - - subpackage_generations
      parameters:
        - name: id
          in: query
          required: true
          schema:
            type: string
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Returns the request metadata for this generation
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Generations_getGeneration_Response_200'
        '401':
          description: Unauthorized - Authentication required or invalid credentials
          content: {}
        '402':
          description: Payment Required - Insufficient credits or quota to complete request
          content: {}
        '404':
          description: Not Found - Generation not found
          content: {}
        '429':
          description: Too Many Requests - Rate limit exceeded
          content: {}
        '500':
          description: Internal Server Error - Unexpected server error
          content: {}
        '502':
          description: Bad Gateway - Provider/upstream API failure
          content: {}
components:
  schemas:
    GenerationGetResponsesContentApplicationJsonSchemaDataApiType:
      type: string
      enum:
        - value: completions
        - value: embeddings
    GenerationGetResponsesContentApplicationJsonSchemaDataProviderResponsesItemsProviderName:
      type: string
      enum:
        - value: AnyScale
        - value: Atoma
        - value: Cent-ML
        - value: CrofAI
        - value: Enfer
        - value: GoPomelo
        - value: HuggingFace
        - value: Hyperbolic 2
        - value: InoCloud
        - value: Kluster
        - value: Lambda
        - value: Lepton
        - value: Lynn 2
        - value: Lynn
        - value: Mancer
        - value: Meta
        - value: Modal
        - value: Nineteen
        - value: OctoAI
        - value: Recursal
        - value: Reflection
        - value: Replicate
        - value: SambaNova 2
        - value: SF Compute
        - value: Targon
        - value: Together 2
        - value: Ubicloud
        - value: 01.AI
        - value: AI21
        - value: AionLabs
        - value: Alibaba
        - value: Ambient
        - value: Amazon Bedrock
        - value: Amazon Nova
        - value: Anthropic
        - value: Arcee AI
        - value: AtlasCloud
        - value: Avian
        - value: Azure
        - value: BaseTen
        - value: BytePlus
        - value: Black Forest Labs
        - value: Cerebras
        - value: Chutes
        - value: Cirrascale
        - value: Clarifai
        - value: Cloudflare
        - value: Cohere
        - value: Crusoe
        - value: DeepInfra
        - value: DeepSeek
        - value: Featherless
        - value: Fireworks
        - value: Friendli
        - value: GMICloud
        - value: Google
        - value: Google AI Studio
        - value: Groq
        - value: Hyperbolic
        - value: Inception
        - value: Inceptron
        - value: InferenceNet
        - value: Infermatic
        - value: Inflection
        - value: Liquid
        - value: Mara
        - value: Mancer 2
        - value: Minimax
        - value: ModelRun
        - value: Mistral
        - value: Modular
        - value: Moonshot AI
        - value: Morph
        - value: NCompass
        - value: Nebius
        - value: NextBit
        - value: Novita
        - value: Nvidia
        - value: OpenAI
        - value: OpenInference
        - value: Parasail
        - value: Perplexity
        - value: Phala
        - value: Relace
        - value: SambaNova
        - value: Seed
        - value: SiliconFlow
        - value: Sourceful
        - value: StepFun
        - value: Stealth
        - value: StreamLake
        - value: Switchpoint
        - value: Together
        - value: Upstage
        - value: Venice
        - value: WandB
        - value: Xiaomi
        - value: xAI
        - value: Z.AI
        - value: FakeProvider
    GenerationGetResponsesContentApplicationJsonSchemaDataProviderResponsesItems:
      type: object
      properties:
        id:
          type: string
        endpoint_id:
          type: string
        model_permaslug:
          type: string
        provider_name:
          $ref: >-
            #/components/schemas/GenerationGetResponsesContentApplicationJsonSchemaDataProviderResponsesItemsProviderName
        status:
          type:
            - number
            - 'null'
          format: double
        latency:
          type: number
          format: double
        is_byok:
          type: boolean
      required:
        - status
    GenerationGetResponsesContentApplicationJsonSchemaData:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for the generation
        upstream_id:
          type:
            - string
            - 'null'
          description: Upstream provider's identifier for this generation
        total_cost:
          type: number
          format: double
          description: Total cost of the generation in USD
        cache_discount:
          type:
            - number
            - 'null'
          format: double
          description: Discount applied due to caching
        upstream_inference_cost:
          type:
            - number
            - 'null'
          format: double
          description: Cost charged by the upstream provider
        created_at:
          type: string
          description: ISO 8601 timestamp of when the generation was created
        model:
          type: string
          description: Model used for the generation
        app_id:
          type:
            - number
            - 'null'
          format: double
          description: ID of the app that made the request
        streamed:
          type:
            - boolean
            - 'null'
          description: Whether the response was streamed
        cancelled:
          type:
            - boolean
            - 'null'
          description: Whether the generation was cancelled
        provider_name:
          type:
            - string
            - 'null'
          description: Name of the provider that served the request
        latency:
          type:
            - number
            - 'null'
          format: double
          description: Total latency in milliseconds
        moderation_latency:
          type:
            - number
            - 'null'
          format: double
          description: Moderation latency in milliseconds
        generation_time:
          type:
            - number
            - 'null'
          format: double
          description: Time taken for generation in milliseconds
        finish_reason:
          type:
            - string
            - 'null'
          description: Reason the generation finished
        tokens_prompt:
          type:
            - number
            - 'null'
          format: double
          description: Number of tokens in the prompt
        tokens_completion:
          type:
            - number
            - 'null'
          format: double
          description: Number of tokens in the completion
        native_tokens_prompt:
          type:
            - number
            - 'null'
          format: double
          description: Native prompt tokens as reported by provider
        native_tokens_completion:
          type:
            - number
            - 'null'
          format: double
          description: Native completion tokens as reported by provider
        native_tokens_completion_images:
          type:
            - number
            - 'null'
          format: double
          description: Native completion image tokens as reported by provider
        native_tokens_reasoning:
          type:
            - number
            - 'null'
          format: double
          description: Native reasoning tokens as reported by provider
        native_tokens_cached:
          type:
            - number
            - 'null'
          format: double
          description: Native cached tokens as reported by provider
        num_media_prompt:
          type:
            - number
            - 'null'
          format: double
          description: Number of media items in the prompt
        num_input_audio_prompt:
          type:
            - number
            - 'null'
          format: double
          description: Number of audio inputs in the prompt
        num_media_completion:
          type:
            - number
            - 'null'
          format: double
          description: Number of media items in the completion
        num_search_results:
          type:
            - number
            - 'null'
          format: double
          description: Number of search results included
        origin:
          type: string
          description: Origin URL of the request
        usage:
          type: number
          format: double
          description: Usage amount in USD
        is_byok:
          type: boolean
          description: Whether this used bring-your-own-key
        native_finish_reason:
          type:
            - string
            - 'null'
          description: Native finish reason as reported by provider
        external_user:
          type:
            - string
            - 'null'
          description: External user identifier
        api_type:
          oneOf:
            - $ref: >-
                #/components/schemas/GenerationGetResponsesContentApplicationJsonSchemaDataApiType
            - type: 'null'
          description: Type of API used for the generation
        router:
          type:
            - string
            - 'null'
          description: Router used for the request (e.g., openrouter/auto)
        provider_responses:
          type:
            - array
            - 'null'
          items:
            $ref: >-
              #/components/schemas/GenerationGetResponsesContentApplicationJsonSchemaDataProviderResponsesItems
          description: >-
            List of provider responses for this generation, including fallback
            attempts
      required:
        - id
        - upstream_id
        - total_cost
        - cache_discount
        - upstream_inference_cost
        - created_at
        - model
        - app_id
        - streamed
        - cancelled
        - provider_name
        - latency
        - moderation_latency
        - generation_time
        - finish_reason
        - tokens_prompt
        - tokens_completion
        - native_tokens_prompt
        - native_tokens_completion
        - native_tokens_completion_images
        - native_tokens_reasoning
        - native_tokens_cached
        - num_media_prompt
        - num_input_audio_prompt
        - num_media_completion
        - num_search_results
        - origin
        - usage
        - is_byok
        - native_finish_reason
        - external_user
        - api_type
        - router
        - provider_responses
    Generations_getGeneration_Response_200:
      type: object
      properties:
        data:
          $ref: >-
            #/components/schemas/GenerationGetResponsesContentApplicationJsonSchemaData
          description: Generation data
      required:
        - data

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/generation"

querystring = {"id":"id"}

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/generation?id=id';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/generation?id=id"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/generation?id=id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/generation?id=id")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/generation?id=id', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://openrouter.ai/api/v1/generation?id=id");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/generation?id=id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```