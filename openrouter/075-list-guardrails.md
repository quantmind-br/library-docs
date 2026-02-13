---
title: List guardrails
url: https://openrouter.ai/docs/api/api-reference/guardrails/list-guardrails.mdx
source: llms
fetched_at: 2026-02-13T15:18:18.254822-03:00
rendered_js: false
word_count: 21
summary: This document provides the technical specifications and code examples for the OpenRouter API endpoint used to retrieve a list of all guardrails associated with an authenticated user. It details the required management key authentication, pagination parameters, and the structural schema of the guardrail objects.
tags:
    - openrouter-api
    - guardrails
    - api-endpoint
    - management-api
    - authentication
    - pagination
category: api
---

# List guardrails

GET https://openrouter.ai/api/v1/guardrails

List all guardrails for the authenticated user. [Management key](/docs/guides/overview/auth/management-api-keys) required.

Reference: https://openrouter.ai/docs/api/api-reference/guardrails/list-guardrails

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: List guardrails
  version: endpoint_guardrails.listGuardrails
paths:
  /guardrails:
    get:
      operationId: list-guardrails
      summary: List guardrails
      description: >-
        List all guardrails for the authenticated user. [Management
        key](/docs/guides/overview/auth/management-api-keys) required.
      tags:
        - - subpackage_guardrails
      parameters:
        - name: offset
          in: query
          description: Number of records to skip for pagination
          required: false
          schema:
            type: string
        - name: limit
          in: query
          description: Maximum number of records to return (max 100)
          required: false
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
          description: List of guardrails
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Guardrails_listGuardrails_Response_200'
        '401':
          description: Unauthorized - Missing or invalid authentication
          content: {}
        '500':
          description: Internal Server Error
          content: {}
components:
  schemas:
    GuardrailsGetResponsesContentApplicationJsonSchemaDataItemsResetInterval:
      type: string
      enum:
        - value: daily
        - value: weekly
        - value: monthly
    GuardrailsGetResponsesContentApplicationJsonSchemaDataItems:
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
                #/components/schemas/GuardrailsGetResponsesContentApplicationJsonSchemaDataItemsResetInterval
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
    Guardrails_listGuardrails_Response_200:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: >-
              #/components/schemas/GuardrailsGetResponsesContentApplicationJsonSchemaDataItems
          description: List of guardrails
        total_count:
          type: number
          format: double
          description: Total number of guardrails
      required:
        - data
        - total_count

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/guardrails"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/guardrails';
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

	url := "https://openrouter.ai/api/v1/guardrails"

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

url = URI("https://openrouter.ai/api/v1/guardrails")

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

HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/guardrails")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/guardrails', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://openrouter.ai/api/v1/guardrails");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/guardrails")! as URL,
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