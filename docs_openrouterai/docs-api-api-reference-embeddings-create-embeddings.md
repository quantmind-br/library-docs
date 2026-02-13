---
title: Submit an embedding request
url: https://openrouter.ai/docs/api/api-reference/embeddings/create-embeddings.mdx
source: llms
fetched_at: 2026-02-13T15:17:52.559332-03:00
rendered_js: false
word_count: 23
summary: This document specifies the API endpoint and request parameters for submitting text or image embedding requests through the OpenRouter platform. It provides a detailed OpenAPI schema including authentication requirements, request body properties, and possible HTTP status codes.
tags:
    - openrouter
    - embeddings
    - api-endpoint
    - vectorization
    - openapi-specification
    - machine-learning
category: api
---

# Submit an embedding request

POST https://openrouter.ai/api/v1/embeddings
Content-Type: application/json

Submits an embedding request to the embeddings router

Reference: https://openrouter.ai/docs/api/api-reference/embeddings/create-embeddings

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Submit an embedding request
  version: endpoint_embeddings.createEmbeddings
paths:
  /embeddings:
    post:
      operationId: create-embeddings
      summary: Submit an embedding request
      description: Submits an embedding request to the embeddings router
      tags:
        - - subpackage_embeddings
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Embedding response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Embeddings_createEmbeddings_Response_200'
        '400':
          description: Bad Request - Invalid request parameters or malformed input
          content: {}
        '401':
          description: Unauthorized - Authentication required or invalid credentials
          content: {}
        '402':
          description: Payment Required - Insufficient credits or quota to complete request
          content: {}
        '404':
          description: Not Found - Resource does not exist
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
        '503':
          description: Service Unavailable - Service temporarily unavailable
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                input:
                  $ref: >-
                    #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaInput
                model:
                  type: string
                encoding_format:
                  $ref: >-
                    #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaEncodingFormat
                dimensions:
                  type: integer
                user:
                  type: string
                provider:
                  $ref: '#/components/schemas/ProviderPreferences'
                input_type:
                  type: string
              required:
                - input
                - model
components:
  schemas:
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaInputOneOf4ItemsContentItemsOneOf0Type:
      type: string
      enum:
        - value: text
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaInputOneOf4ItemsContentItems0:
      type: object
      properties:
        type:
          $ref: >-
            #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaInputOneOf4ItemsContentItemsOneOf0Type
        text:
          type: string
      required:
        - type
        - text
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaInputOneOf4ItemsContentItemsOneOf1Type:
      type: string
      enum:
        - value: image_url
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaInputOneOf4ItemsContentItemsOneOf1ImageUrl:
      type: object
      properties:
        url:
          type: string
      required:
        - url
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaInputOneOf4ItemsContentItems1:
      type: object
      properties:
        type:
          $ref: >-
            #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaInputOneOf4ItemsContentItemsOneOf1Type
        image_url:
          $ref: >-
            #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaInputOneOf4ItemsContentItemsOneOf1ImageUrl
      required:
        - type
        - image_url
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaInputOneOf4ItemsContentItems:
      oneOf:
        - $ref: >-
            #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaInputOneOf4ItemsContentItems0
        - $ref: >-
            #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaInputOneOf4ItemsContentItems1
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaInputOneOf4Items:
      type: object
      properties:
        content:
          type: array
          items:
            $ref: >-
              #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaInputOneOf4ItemsContentItems
      required:
        - content
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaInput4:
      type: array
      items:
        $ref: >-
          #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaInputOneOf4Items
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaInput:
      oneOf:
        - type: string
        - type: array
          items:
            type: string
        - type: array
          items:
            type: number
            format: double
        - type: array
          items:
            type: array
            items:
              type: number
              format: double
        - $ref: >-
            #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaInput4
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaEncodingFormat:
      type: string
      enum:
        - value: float
        - value: base64
    DataCollection:
      type: string
      enum:
        - value: deny
        - value: allow
    ProviderName:
      type: string
      enum:
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
    ProviderPreferencesOrderItems:
      oneOf:
        - $ref: '#/components/schemas/ProviderName'
        - type: string
    ProviderPreferencesOnlyItems:
      oneOf:
        - $ref: '#/components/schemas/ProviderName'
        - type: string
    ProviderPreferencesIgnoreItems:
      oneOf:
        - $ref: '#/components/schemas/ProviderName'
        - type: string
    Quantization:
      type: string
      enum:
        - value: int4
        - value: int8
        - value: fp4
        - value: fp6
        - value: fp8
        - value: fp16
        - value: bf16
        - value: fp32
        - value: unknown
    ProviderPreferencesSort:
      type: object
      properties: {}
    BigNumberUnion:
      type: string
    ProviderPreferencesMaxPriceCompletion:
      type: object
      properties: {}
    ProviderPreferencesMaxPriceImage:
      type: object
      properties: {}
    ProviderPreferencesMaxPriceAudio:
      type: object
      properties: {}
    ProviderPreferencesMaxPriceRequest:
      type: object
      properties: {}
    ProviderPreferencesMaxPrice:
      type: object
      properties:
        prompt:
          $ref: '#/components/schemas/BigNumberUnion'
        completion:
          $ref: '#/components/schemas/ProviderPreferencesMaxPriceCompletion'
        image:
          $ref: '#/components/schemas/ProviderPreferencesMaxPriceImage'
        audio:
          $ref: '#/components/schemas/ProviderPreferencesMaxPriceAudio'
        request:
          $ref: '#/components/schemas/ProviderPreferencesMaxPriceRequest'
    PercentileThroughputCutoffs:
      type: object
      properties:
        p50:
          type:
            - number
            - 'null'
          format: double
          description: Minimum p50 throughput (tokens/sec)
        p75:
          type:
            - number
            - 'null'
          format: double
          description: Minimum p75 throughput (tokens/sec)
        p90:
          type:
            - number
            - 'null'
          format: double
          description: Minimum p90 throughput (tokens/sec)
        p99:
          type:
            - number
            - 'null'
          format: double
          description: Minimum p99 throughput (tokens/sec)
    PreferredMinThroughput:
      oneOf:
        - type: number
          format: double
        - $ref: '#/components/schemas/PercentileThroughputCutoffs'
        - description: Any type
    PercentileLatencyCutoffs:
      type: object
      properties:
        p50:
          type:
            - number
            - 'null'
          format: double
          description: Maximum p50 latency (seconds)
        p75:
          type:
            - number
            - 'null'
          format: double
          description: Maximum p75 latency (seconds)
        p90:
          type:
            - number
            - 'null'
          format: double
          description: Maximum p90 latency (seconds)
        p99:
          type:
            - number
            - 'null'
          format: double
          description: Maximum p99 latency (seconds)
    PreferredMaxLatency:
      oneOf:
        - type: number
          format: double
        - $ref: '#/components/schemas/PercentileLatencyCutoffs'
        - description: Any type
    ProviderPreferences:
      type: object
      properties:
        allow_fallbacks:
          type:
            - boolean
            - 'null'
          description: >
            Whether to allow backup providers to serve requests

            - true: (default) when the primary provider (or your custom
            providers in "order") is unavailable, use the next best provider.

            - false: use only the primary/custom provider, and return the
            upstream error if it's unavailable.
        require_parameters:
          type:
            - boolean
            - 'null'
          description: >-
            Whether to filter providers to only those that support the
            parameters you've provided. If this setting is omitted or set to
            false, then providers will receive only the parameters they support,
            and ignore the rest.
        data_collection:
          $ref: '#/components/schemas/DataCollection'
        zdr:
          type:
            - boolean
            - 'null'
          description: >-
            Whether to restrict routing to only ZDR (Zero Data Retention)
            endpoints. When true, only endpoints that do not retain prompts will
            be used.
        enforce_distillable_text:
          type:
            - boolean
            - 'null'
          description: >-
            Whether to restrict routing to only models that allow text
            distillation. When true, only models where the author has allowed
            distillation will be used.
        order:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/ProviderPreferencesOrderItems'
          description: >-
            An ordered list of provider slugs. The router will attempt to use
            the first provider in the subset of this list that supports your
            requested model, and fall back to the next if it is unavailable. If
            no providers are available, the request will fail with an error
            message.
        only:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/ProviderPreferencesOnlyItems'
          description: >-
            List of provider slugs to allow. If provided, this list is merged
            with your account-wide allowed provider settings for this request.
        ignore:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/ProviderPreferencesIgnoreItems'
          description: >-
            List of provider slugs to ignore. If provided, this list is merged
            with your account-wide ignored provider settings for this request.
        quantizations:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/Quantization'
          description: A list of quantization levels to filter the provider by.
        sort:
          $ref: '#/components/schemas/ProviderPreferencesSort'
        max_price:
          $ref: '#/components/schemas/ProviderPreferencesMaxPrice'
          description: >-
            The object specifying the maximum price you want to pay for this
            request. USD price per million tokens, for prompt and completion.
        preferred_min_throughput:
          $ref: '#/components/schemas/PreferredMinThroughput'
        preferred_max_latency:
          $ref: '#/components/schemas/PreferredMaxLatency'
    EmbeddingsPostResponsesContentApplicationJsonSchemaObject:
      type: string
      enum:
        - value: list
    EmbeddingsPostResponsesContentApplicationJsonSchemaDataItemsObject:
      type: string
      enum:
        - value: embedding
    EmbeddingsPostResponsesContentApplicationJsonSchemaDataItemsEmbedding:
      oneOf:
        - type: array
          items:
            type: number
            format: double
        - type: string
    EmbeddingsPostResponsesContentApplicationJsonSchemaDataItems:
      type: object
      properties:
        object:
          $ref: >-
            #/components/schemas/EmbeddingsPostResponsesContentApplicationJsonSchemaDataItemsObject
        embedding:
          $ref: >-
            #/components/schemas/EmbeddingsPostResponsesContentApplicationJsonSchemaDataItemsEmbedding
        index:
          type: number
          format: double
      required:
        - object
        - embedding
    EmbeddingsPostResponsesContentApplicationJsonSchemaUsage:
      type: object
      properties:
        prompt_tokens:
          type: number
          format: double
        total_tokens:
          type: number
          format: double
        cost:
          type: number
          format: double
      required:
        - prompt_tokens
        - total_tokens
    Embeddings_createEmbeddings_Response_200:
      type: object
      properties:
        id:
          type: string
        object:
          $ref: >-
            #/components/schemas/EmbeddingsPostResponsesContentApplicationJsonSchemaObject
        data:
          type: array
          items:
            $ref: >-
              #/components/schemas/EmbeddingsPostResponsesContentApplicationJsonSchemaDataItems
        model:
          type: string
        usage:
          $ref: >-
            #/components/schemas/EmbeddingsPostResponsesContentApplicationJsonSchemaUsage
      required:
        - object
        - data
        - model

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/embeddings"

payload = {
    "input": "The quick brown fox jumps over the lazy dog",
    "model": "text-embedding-ada-002"
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/embeddings';
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{"input":"The quick brown fox jumps over the lazy dog","model":"text-embedding-ada-002"}'
};

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
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/embeddings"

	payload := strings.NewReader("{\n  \"input\": \"The quick brown fox jumps over the lazy dog\",\n  \"model\": \"text-embedding-ada-002\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

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

url = URI("https://openrouter.ai/api/v1/embeddings")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"input\": \"The quick brown fox jumps over the lazy dog\",\n  \"model\": \"text-embedding-ada-002\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://openrouter.ai/api/v1/embeddings")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"input\": \"The quick brown fox jumps over the lazy dog\",\n  \"model\": \"text-embedding-ada-002\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://openrouter.ai/api/v1/embeddings', [
  'body' => '{
  "input": "The quick brown fox jumps over the lazy dog",
  "model": "text-embedding-ada-002"
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://openrouter.ai/api/v1/embeddings");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"input\": \"The quick brown fox jumps over the lazy dog\",\n  \"model\": \"text-embedding-ada-002\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "input": "The quick brown fox jumps over the lazy dog",
  "model": "text-embedding-ada-002"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/embeddings")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

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