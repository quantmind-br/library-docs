---
title: List models filtered by user provider preferences, privacy settings, and guardrails
url: https://openrouter.ai/docs/api/api-reference/models/list-models-user.mdx
source: llms
fetched_at: 2026-02-13T15:18:02.359046-03:00
rendered_js: false
word_count: 249
summary: This document describes an API endpoint for retrieving a list of AI models filtered by user-specific provider preferences, privacy configurations, and active guardrails.
tags:
    - openrouter-api
    - model-listing
    - user-preferences
    - guardrails
    - privacy-settings
    - api-reference
category: api
---

# List models filtered by user provider preferences, privacy settings, and guardrails

GET https://openrouter.ai/api/v1/models/user

List models filtered by user provider preferences, [privacy settings](https://openrouter.ai/docs/guides/privacy/logging), and [guardrails](https://openrouter.ai/docs/guides/features/guardrails). If requesting through `eu.openrouter.ai/api/v1/...` the results will be filtered to models that satisfy [EU in-region routing](https://openrouter.ai/docs/guides/privacy/logging#enterprise-eu-in-region-routing).

Reference: https://openrouter.ai/docs/api/api-reference/models/list-models-user

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: >-
    List models filtered by user provider preferences, privacy settings, and
    guardrails
  version: endpoint_models.listModelsUser
paths:
  /models/user:
    get:
      operationId: list-models-user
      summary: >-
        List models filtered by user provider preferences, privacy settings, and
        guardrails
      description: >-
        List models filtered by user provider preferences, [privacy
        settings](https://openrouter.ai/docs/guides/privacy/logging), and
        [guardrails](https://openrouter.ai/docs/guides/features/guardrails). If
        requesting through `eu.openrouter.ai/api/v1/...` the results will be
        filtered to models that satisfy [EU in-region
        routing](https://openrouter.ai/docs/guides/privacy/logging#enterprise-eu-in-region-routing).
      tags:
        - - subpackage_models
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Returns a list of models filtered by user provider preferences
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ModelsListResponse'
        '401':
          description: Unauthorized - Missing or invalid authentication
          content: {}
        '404':
          description: Not Found - No eligible endpoints found
          content: {}
        '500':
          description: Internal Server Error
          content: {}
components:
  schemas:
    PublicPricingPrompt:
      type: object
      properties: {}
    PublicPricingCompletion:
      type: object
      properties: {}
    PublicPricingRequest:
      type: object
      properties: {}
    PublicPricingImage:
      type: object
      properties: {}
    PublicPricingImageToken:
      type: object
      properties: {}
    PublicPricingImageOutput:
      type: object
      properties: {}
    PublicPricingAudio:
      type: object
      properties: {}
    PublicPricingAudioOutput:
      type: object
      properties: {}
    PublicPricingInputAudioCache:
      type: object
      properties: {}
    PublicPricingWebSearch:
      type: object
      properties: {}
    PublicPricingInternalReasoning:
      type: object
      properties: {}
    PublicPricingInputCacheRead:
      type: object
      properties: {}
    PublicPricingInputCacheWrite:
      type: object
      properties: {}
    PublicPricing:
      type: object
      properties:
        prompt:
          $ref: '#/components/schemas/PublicPricingPrompt'
        completion:
          $ref: '#/components/schemas/PublicPricingCompletion'
        request:
          $ref: '#/components/schemas/PublicPricingRequest'
        image:
          $ref: '#/components/schemas/PublicPricingImage'
        image_token:
          $ref: '#/components/schemas/PublicPricingImageToken'
        image_output:
          $ref: '#/components/schemas/PublicPricingImageOutput'
        audio:
          $ref: '#/components/schemas/PublicPricingAudio'
        audio_output:
          $ref: '#/components/schemas/PublicPricingAudioOutput'
        input_audio_cache:
          $ref: '#/components/schemas/PublicPricingInputAudioCache'
        web_search:
          $ref: '#/components/schemas/PublicPricingWebSearch'
        internal_reasoning:
          $ref: '#/components/schemas/PublicPricingInternalReasoning'
        input_cache_read:
          $ref: '#/components/schemas/PublicPricingInputCacheRead'
        input_cache_write:
          $ref: '#/components/schemas/PublicPricingInputCacheWrite'
        discount:
          type: number
          format: double
      required:
        - prompt
        - completion
    ModelGroup:
      type: string
      enum:
        - value: Router
        - value: Media
        - value: Other
        - value: GPT
        - value: Claude
        - value: Gemini
        - value: Grok
        - value: Cohere
        - value: Nova
        - value: Qwen
        - value: Yi
        - value: DeepSeek
        - value: Mistral
        - value: Llama2
        - value: Llama3
        - value: Llama4
        - value: PaLM
        - value: RWKV
        - value: Qwen3
    ModelArchitectureInstructType:
      type: string
      enum:
        - value: none
        - value: airoboros
        - value: alpaca
        - value: alpaca-modif
        - value: chatml
        - value: claude
        - value: code-llama
        - value: gemma
        - value: llama2
        - value: llama3
        - value: mistral
        - value: nemotron
        - value: neural
        - value: openchat
        - value: phi3
        - value: rwkv
        - value: vicuna
        - value: zephyr
        - value: deepseek-r1
        - value: deepseek-v3.1
        - value: qwq
        - value: qwen3
    InputModality:
      type: string
      enum:
        - value: text
        - value: image
        - value: file
        - value: audio
        - value: video
    OutputModality:
      type: string
      enum:
        - value: text
        - value: image
        - value: embeddings
        - value: audio
    ModelArchitecture:
      type: object
      properties:
        tokenizer:
          $ref: '#/components/schemas/ModelGroup'
        instruct_type:
          oneOf:
            - $ref: '#/components/schemas/ModelArchitectureInstructType'
            - type: 'null'
          description: Instruction format type
        modality:
          type:
            - string
            - 'null'
          description: Primary modality of the model
        input_modalities:
          type: array
          items:
            $ref: '#/components/schemas/InputModality'
          description: Supported input modalities
        output_modalities:
          type: array
          items:
            $ref: '#/components/schemas/OutputModality'
          description: Supported output modalities
      required:
        - modality
        - input_modalities
        - output_modalities
    TopProviderInfo:
      type: object
      properties:
        context_length:
          type:
            - number
            - 'null'
          format: double
          description: Context length from the top provider
        max_completion_tokens:
          type:
            - number
            - 'null'
          format: double
          description: Maximum completion tokens from the top provider
        is_moderated:
          type: boolean
          description: Whether the top provider moderates content
      required:
        - is_moderated
    PerRequestLimits:
      type: object
      properties:
        prompt_tokens:
          type: number
          format: double
          description: Maximum prompt tokens per request
        completion_tokens:
          type: number
          format: double
          description: Maximum completion tokens per request
      required:
        - prompt_tokens
        - completion_tokens
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
    DefaultParameters:
      type: object
      properties:
        temperature:
          type:
            - number
            - 'null'
          format: double
        top_p:
          type:
            - number
            - 'null'
          format: double
        frequency_penalty:
          type:
            - number
            - 'null'
          format: double
    Model:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for the model
        canonical_slug:
          type: string
          description: Canonical slug for the model
        hugging_face_id:
          type:
            - string
            - 'null'
          description: Hugging Face model identifier, if applicable
        name:
          type: string
          description: Display name of the model
        created:
          type: number
          format: double
          description: Unix timestamp of when the model was created
        description:
          type: string
          description: Description of the model
        pricing:
          $ref: '#/components/schemas/PublicPricing'
        context_length:
          type:
            - number
            - 'null'
          format: double
          description: Maximum context length in tokens
        architecture:
          $ref: '#/components/schemas/ModelArchitecture'
        top_provider:
          $ref: '#/components/schemas/TopProviderInfo'
        per_request_limits:
          $ref: '#/components/schemas/PerRequestLimits'
        supported_parameters:
          type: array
          items:
            $ref: '#/components/schemas/Parameter'
          description: List of supported parameters for this model
        default_parameters:
          $ref: '#/components/schemas/DefaultParameters'
        expiration_date:
          type:
            - string
            - 'null'
          description: >-
            The date after which the model may be removed. ISO 8601 date string
            (YYYY-MM-DD) or null if no expiration.
      required:
        - id
        - canonical_slug
        - name
        - created
        - pricing
        - context_length
        - architecture
        - top_provider
        - per_request_limits
        - supported_parameters
        - default_parameters
    ModelsListResponseData:
      type: array
      items:
        $ref: '#/components/schemas/Model'
    ModelsListResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/ModelsListResponseData'
      required:
        - data

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/models/user"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/models/user';
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

	url := "https://openrouter.ai/api/v1/models/user"

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

url = URI("https://openrouter.ai/api/v1/models/user")

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

HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/models/user")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/models/user', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://openrouter.ai/api/v1/models/user");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/models/user")! as URL,
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