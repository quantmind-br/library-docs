---
title: Create a guardrail
url: https://openrouter.ai/docs/api/api-reference/guardrails/create-guardrail.mdx
source: llms
fetched_at: 2026-02-13T15:18:20.475009-03:00
rendered_js: false
word_count: 25
summary: This document provides the API specification and code examples for creating a guardrail to manage spending limits, allowed models, and data retention on OpenRouter.
tags:
    - openrouter-api
    - guardrails
    - api-reference
    - usage-limits
    - model-filtering
    - data-retention
category: api
---

# Create a guardrail

POST https://openrouter.ai/api/v1/guardrails
Content-Type: application/json

Create a new guardrail for the authenticated user. [Management key](/docs/guides/overview/auth/management-api-keys) required.

Reference: https://openrouter.ai/docs/api/api-reference/guardrails/create-guardrail

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create a guardrail
  version: endpoint_guardrails.createGuardrail
paths:
  /guardrails:
    post:
      operationId: create-guardrail
      summary: Create a guardrail
      description: >-
        Create a new guardrail for the authenticated user. [Management
        key](/docs/guides/overview/auth/management-api-keys) required.
      tags:
        - - subpackage_guardrails
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '201':
          description: Guardrail created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Guardrails_createGuardrail_Response_201'
        '400':
          description: Bad Request - Invalid request parameters
          content: {}
        '401':
          description: Unauthorized - Missing or invalid authentication
          content: {}
        '500':
          description: Internal Server Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                  description: Name for the new guardrail
                description:
                  type:
                    - string
                    - 'null'
                  description: Description of the guardrail
                limit_usd:
                  type:
                    - number
                    - 'null'
                  format: double
                  description: Spending limit in USD
                reset_interval:
                  oneOf:
                    - $ref: >-
                        #/components/schemas/GuardrailsPostRequestBodyContentApplicationJsonSchemaResetInterval
                    - type: 'null'
                  description: Interval at which the limit resets (daily, weekly, monthly)
                allowed_providers:
                  type:
                    - array
                    - 'null'
                  items:
                    type: string
                  description: List of allowed provider IDs
                allowed_models:
                  type:
                    - array
                    - 'null'
                  items:
                    type: string
                  description: Array of model identifiers (slug or canonical_slug accepted)
                enforce_zdr:
                  type:
                    - boolean
                    - 'null'
                  description: Whether to enforce zero data retention
              required:
                - name
components:
  schemas:
    GuardrailsPostRequestBodyContentApplicationJsonSchemaResetInterval:
      type: string
      enum:
        - value: daily
        - value: weekly
        - value: monthly
    GuardrailsPostResponsesContentApplicationJsonSchemaDataResetInterval:
      type: string
      enum:
        - value: daily
        - value: weekly
        - value: monthly
    GuardrailsPostResponsesContentApplicationJsonSchemaData:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the guardrail
        name:
          type: string
          description: Name of the guardrail
        description:
          type:
            - string
            - 'null'
          description: Description of the guardrail
        limit_usd:
          type:
            - number
            - 'null'
          format: double
          description: Spending limit in USD
        reset_interval:
          oneOf:
            - $ref: >-
                #/components/schemas/GuardrailsPostResponsesContentApplicationJsonSchemaDataResetInterval
            - type: 'null'
          description: Interval at which the limit resets (daily, weekly, monthly)
        allowed_providers:
          type:
            - array
            - 'null'
          items:
            type: string
          description: List of allowed provider IDs
        allowed_models:
          type:
            - array
            - 'null'
          items:
            type: string
          description: Array of model canonical_slugs (immutable identifiers)
        enforce_zdr:
          type:
            - boolean
            - 'null'
          description: Whether to enforce zero data retention
        created_at:
          type: string
          description: ISO 8601 timestamp of when the guardrail was created
        updated_at:
          type:
            - string
            - 'null'
          description: ISO 8601 timestamp of when the guardrail was last updated
      required:
        - id
        - name
        - created_at
    Guardrails_createGuardrail_Response_201:
      type: object
      properties:
        data:
          $ref: >-
            #/components/schemas/GuardrailsPostResponsesContentApplicationJsonSchemaData
          description: The created guardrail
      required:
        - data

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/guardrails"

payload = {
    "name": "My New Guardrail",
    "description": "A guardrail for limiting API usage",
    "limit_usd": 50,
    "reset_interval": "monthly",
    "allowed_providers": ["openai", "anthropic", "deepseek"],
    "allowed_models": None,
    "enforce_zdr": False
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/guardrails';
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{"name":"My New Guardrail","description":"A guardrail for limiting API usage","limit_usd":50,"reset_interval":"monthly","allowed_providers":["openai","anthropic","deepseek"],"allowed_models":null,"enforce_zdr":false}'
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

	url := "https://openrouter.ai/api/v1/guardrails"

	payload := strings.NewReader("{\n  \"name\": \"My New Guardrail\",\n  \"description\": \"A guardrail for limiting API usage\",\n  \"limit_usd\": 50,\n  \"reset_interval\": \"monthly\",\n  \"allowed_providers\": [\n    \"openai\",\n    \"anthropic\",\n    \"deepseek\"\n  ],\n  \"allowed_models\": null,\n  \"enforce_zdr\": false\n}")

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

url = URI("https://openrouter.ai/api/v1/guardrails")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"My New Guardrail\",\n  \"description\": \"A guardrail for limiting API usage\",\n  \"limit_usd\": 50,\n  \"reset_interval\": \"monthly\",\n  \"allowed_providers\": [\n    \"openai\",\n    \"anthropic\",\n    \"deepseek\"\n  ],\n  \"allowed_models\": null,\n  \"enforce_zdr\": false\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://openrouter.ai/api/v1/guardrails")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"My New Guardrail\",\n  \"description\": \"A guardrail for limiting API usage\",\n  \"limit_usd\": 50,\n  \"reset_interval\": \"monthly\",\n  \"allowed_providers\": [\n    \"openai\",\n    \"anthropic\",\n    \"deepseek\"\n  ],\n  \"allowed_models\": null,\n  \"enforce_zdr\": false\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://openrouter.ai/api/v1/guardrails', [
  'body' => '{
  "name": "My New Guardrail",
  "description": "A guardrail for limiting API usage",
  "limit_usd": 50,
  "reset_interval": "monthly",
  "allowed_providers": [
    "openai",
    "anthropic",
    "deepseek"
  ],
  "allowed_models": null,
  "enforce_zdr": false
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

var client = new RestClient("https://openrouter.ai/api/v1/guardrails");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"My New Guardrail\",\n  \"description\": \"A guardrail for limiting API usage\",\n  \"limit_usd\": 50,\n  \"reset_interval\": \"monthly\",\n  \"allowed_providers\": [\n    \"openai\",\n    \"anthropic\",\n    \"deepseek\"\n  ],\n  \"allowed_models\": null,\n  \"enforce_zdr\": false\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "name": "My New Guardrail",
  "description": "A guardrail for limiting API usage",
  "limit_usd": 50,
  "reset_interval": "monthly",
  "allowed_providers": ["openai", "anthropic", "deepseek"],
  "allowed_models": ,
  "enforce_zdr": false
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/guardrails")! as URL,
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