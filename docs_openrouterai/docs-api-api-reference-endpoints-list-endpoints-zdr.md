---
title: Preview the impact of ZDR on the available endpoints
url: https://openrouter.ai/docs/api/api-reference/endpoints/list-endpoints-zdr.mdx
source: llms
fetched_at: 2026-02-13T15:18:02.519846-03:00
rendered_js: false
word_count: 18
summary: This document specifies the OpenRouter API endpoint for previewing how Zero-Day Retention (ZDR) settings impact the availability and pricing of model endpoints.
tags:
    - openrouter
    - api-endpoints
    - zdr
    - openapi-specification
    - model-pricing
    - provider-data
category: api
---

# Preview the impact of ZDR on the available endpoints

GET https://openrouter.ai/api/v1/endpoints/zdr

Reference: https://openrouter.ai/docs/api/api-reference/endpoints/list-endpoints-zdr

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Preview the impact of ZDR on the available endpoints
  version: endpoint_endpoints.listEndpointsZdr
paths:
  /endpoints/zdr:
    get:
      operationId: list-endpoints-zdr
      summary: Preview the impact of ZDR on the available endpoints
      tags:
        - - subpackage_endpoints
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Returns a list of endpoints
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Endpoints_listEndpointsZdr_Response_200'
        '500':
          description: Internal Server Error - Unexpected server error
          content: {}
components:
  schemas:
    PublicEndpointPricingPrompt:
      type: object
      properties: {}
    PublicEndpointPricingCompletion:
      type: object
      properties: {}
    PublicEndpointPricingRequest:
      type: object
      properties: {}
    PublicEndpointPricingImage:
      type: object
      properties: {}
    PublicEndpointPricingImageToken:
      type: object
      properties: {}
    PublicEndpointPricingImageOutput:
      type: object
      properties: {}
    PublicEndpointPricingAudio:
      type: object
      properties: {}
    PublicEndpointPricingAudioOutput:
      type: object
      properties: {}
    PublicEndpointPricingInputAudioCache:
      type: object
      properties: {}
    PublicEndpointPricingWebSearch:
      type: object
      properties: {}
    PublicEndpointPricingInternalReasoning:
      type: object
      properties: {}
    PublicEndpointPricingInputCacheRead:
      type: object
      properties: {}
    PublicEndpointPricingInputCacheWrite:
      type: object
      properties: {}
    PublicEndpointPricing:
      type: object
      properties:
        prompt:
          $ref: '#/components/schemas/PublicEndpointPricingPrompt'
        completion:
          $ref: '#/components/schemas/PublicEndpointPricingCompletion'
        request:
          $ref: '#/components/schemas/PublicEndpointPricingRequest'
        image:
          $ref: '#/components/schemas/PublicEndpointPricingImage'
        image_token:
          $ref: '#/components/schemas/PublicEndpointPricingImageToken'
        image_output:
          $ref: '#/components/schemas/PublicEndpointPricingImageOutput'
        audio:
          $ref: '#/components/schemas/PublicEndpointPricingAudio'
        audio_output:
          $ref: '#/components/schemas/PublicEndpointPricingAudioOutput'
        input_audio_cache:
          $ref: '#/components/schemas/PublicEndpointPricingInputAudioCache'
        web_search:
          $ref: '#/components/schemas/PublicEndpointPricingWebSearch'
        internal_reasoning:
          $ref: '#/components/schemas/PublicEndpointPricingInternalReasoning'
        input_cache_read:
          $ref: '#/components/schemas/PublicEndpointPricingInputCacheRead'
        input_cache_write:
          $ref: '#/components/schemas/PublicEndpointPricingInputCacheWrite'
        discount:
          type: number
          format: double
      required:
        - prompt
        - completion
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
    PublicEndpointQuantization:
      type: object
      properties: {}
    Parameter:
      type: string
      enum:
        - value: temperature
        - value: top_p
        - value: top_k
        - value: min_p
        - value: top_a
        - value: frequency_penalty
        - value: presence_penalty
        - value: repetition_penalty
        - value: max_tokens
        - value: logit_bias
        - value: logprobs
        - value: top_logprobs
        - value: seed
        - value: response_format
        - value: structured_outputs
        - value: stop
        - value: tools
        - value: tool_choice
        - value: parallel_tool_calls
        - value: include_reasoning
        - value: reasoning
        - value: reasoning_effort
        - value: web_search_options
        - value: verbosity
    EndpointStatus:
      type: string
      enum:
        - value: '0'
        - value: '-1'
        - value: '-2'
        - value: '-3'
        - value: '-5'
        - value: '-10'
    PercentileStats:
      type: object
      properties:
        p50:
          type: number
          format: double
          description: Median (50th percentile)
        p75:
          type: number
          format: double
          description: 75th percentile
        p90:
          type: number
          format: double
          description: 90th percentile
        p99:
          type: number
          format: double
          description: 99th percentile
      required:
        - p50
        - p75
        - p90
        - p99
    PublicEndpointThroughputLast30M:
      type: object
      properties:
        p50:
          type: number
          format: double
          description: Median (50th percentile)
        p75:
          type: number
          format: double
          description: 75th percentile
        p90:
          type: number
          format: double
          description: 90th percentile
        p99:
          type: number
          format: double
          description: 99th percentile
      required:
        - p50
        - p75
        - p90
        - p99
    PublicEndpoint:
      type: object
      properties:
        name:
          type: string
        model_id:
          type: string
          description: The unique identifier for the model (permaslug)
        model_name:
          type: string
        context_length:
          type: number
          format: double
        pricing:
          $ref: '#/components/schemas/PublicEndpointPricing'
        provider_name:
          $ref: '#/components/schemas/ProviderName'
        tag:
          type: string
        quantization:
          $ref: '#/components/schemas/PublicEndpointQuantization'
        max_completion_tokens:
          type:
            - number
            - 'null'
          format: double
        max_prompt_tokens:
          type:
            - number
            - 'null'
          format: double
        supported_parameters:
          type: array
          items:
            $ref: '#/components/schemas/Parameter'
        status:
          $ref: '#/components/schemas/EndpointStatus'
        uptime_last_30m:
          type:
            - number
            - 'null'
          format: double
        supports_implicit_caching:
          type: boolean
        latency_last_30m:
          $ref: '#/components/schemas/PercentileStats'
        throughput_last_30m:
          $ref: '#/components/schemas/PublicEndpointThroughputLast30M'
      required:
        - name
        - model_id
        - model_name
        - context_length
        - pricing
        - provider_name
        - tag
        - quantization
        - max_completion_tokens
        - max_prompt_tokens
        - supported_parameters
        - uptime_last_30m
        - supports_implicit_caching
        - latency_last_30m
        - throughput_last_30m
    Endpoints_listEndpointsZdr_Response_200:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/PublicEndpoint'
      required:
        - data

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/endpoints/zdr"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/endpoints/zdr';
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

	url := "https://openrouter.ai/api/v1/endpoints/zdr"

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

url = URI("https://openrouter.ai/api/v1/endpoints/zdr")

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

HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/endpoints/zdr")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/endpoints/zdr', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://openrouter.ai/api/v1/endpoints/zdr");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/endpoints/zdr")! as URL,
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