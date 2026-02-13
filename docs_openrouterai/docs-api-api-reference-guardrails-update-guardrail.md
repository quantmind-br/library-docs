---
title: Update a guardrail
url: https://openrouter.ai/docs/api/api-reference/guardrails/update-guardrail.mdx
source: llms
fetched_at: 2026-02-13T15:18:24.743082-03:00
rendered_js: false
word_count: 21
summary: This document provides the technical specification and code examples for updating the configuration of an existing guardrail via the OpenRouter Management API.
tags:
    - openrouter-api
    - guardrails
    - management-api
    - api-reference
    - usage-limits
    - patch-request
category: api
---

# Update a guardrail

PATCH https://openrouter.ai/api/v1/guardrails/{id}
Content-Type: application/json

Update an existing guardrail. [Management key](/docs/guides/overview/auth/management-api-keys) required.

Reference: https://openrouter.ai/docs/api/api-reference/guardrails/update-guardrail

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Update a guardrail
  version: endpoint_guardrails.updateGuardrail
paths:
  /guardrails/{id}:
    patch:
      operationId: update-guardrail
      summary: Update a guardrail
      description: >-
        Update an existing guardrail. [Management
        key](/docs/guides/overview/auth/management-api-keys) required.
      tags:
        - - subpackage_guardrails
      parameters:
        - name: id
          in: path
          description: The unique identifier of the guardrail to update
          required: true
          schema:
            type: string
            format: uuid
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Guardrail updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Guardrails_updateGuardrail_Response_200'
        '400':
          description: Bad Request - Invalid request parameters
          content: {}
        '401':
          description: Unauthorized - Missing or invalid authentication
          content: {}
        '404':
          description: Not Found - Guardrail does not exist
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
                  description: New name for the guardrail
                description:
                  type:
                    - string
                    - 'null'
                  description: New description for the guardrail
                limit_usd:
                  type:
                    - number
                    - 'null'
                  format: double
                  description: New spending limit in USD
                reset_interval:
                  oneOf:
                    - $ref: >-
                        #/components/schemas/GuardrailsIdPatchRequestBodyContentApplicationJsonSchemaResetInterval
                    - type: 'null'
                  description: Interval at which the limit resets (daily, weekly, monthly)
                allowed_providers:
                  type:
                    - array
                    - 'null'
                  items:
                    type: string
                  description: New list of allowed provider IDs
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
components:
  schemas:
    GuardrailsIdPatchRequestBodyContentApplicationJsonSchemaResetInterval:
      type: string
      enum:
        - value: daily
        - value: weekly
        - value: monthly
    GuardrailsIdPatchResponsesContentApplicationJsonSchemaDataResetInterval:
      type: string
      enum:
        - value: daily
        - value: weekly
        - value: monthly
    GuardrailsIdPatchResponsesContentApplicationJsonSchemaData:
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
                #/components/schemas/GuardrailsIdPatchResponsesContentApplicationJsonSchemaDataResetInterval
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
    Guardrails_updateGuardrail_Response_200:
      type: object
      properties:
        data:
          $ref: >-
            #/components/schemas/GuardrailsIdPatchResponsesContentApplicationJsonSchemaData
          description: The updated guardrail
      required:
        - data

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000"

payload = {
    "name": "Updated Guardrail Name",
    "description": "Updated description",
    "limit_usd": 75,
    "reset_interval": "weekly"
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.patch(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000';
const options = {
  method: 'PATCH',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{"name":"Updated Guardrail Name","description":"Updated description","limit_usd":75,"reset_interval":"weekly"}'
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

	url := "https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000"

	payload := strings.NewReader("{\n  \"name\": \"Updated Guardrail Name\",\n  \"description\": \"Updated description\",\n  \"limit_usd\": 75,\n  \"reset_interval\": \"weekly\"\n}")

	req, _ := http.NewRequest("PATCH", url, payload)

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

url = URI("https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"Updated Guardrail Name\",\n  \"description\": \"Updated description\",\n  \"limit_usd\": 75,\n  \"reset_interval\": \"weekly\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"Updated Guardrail Name\",\n  \"description\": \"Updated description\",\n  \"limit_usd\": 75,\n  \"reset_interval\": \"weekly\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000', [
  'body' => '{
  "name": "Updated Guardrail Name",
  "description": "Updated description",
  "limit_usd": 75,
  "reset_interval": "weekly"
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

var client = new RestClient("https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"Updated Guardrail Name\",\n  \"description\": \"Updated description\",\n  \"limit_usd\": 75,\n  \"reset_interval\": \"weekly\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "name": "Updated Guardrail Name",
  "description": "Updated description",
  "limit_usd": 75,
  "reset_interval": "weekly"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
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