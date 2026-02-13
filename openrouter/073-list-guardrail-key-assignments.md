---
title: List key assignments for a guardrail
url: https://openrouter.ai/docs/api/api-reference/guardrails/list-guardrail-key-assignments.mdx
source: llms
fetched_at: 2026-02-13T15:18:28.706422-03:00
rendered_js: false
word_count: 27
summary: This document provides the API specification and code examples for listing all API key assignments associated with a specific guardrail on OpenRouter.
tags:
    - openrouter
    - api-reference
    - guardrails
    - key-management
    - authentication
category: api
---

# List key assignments for a guardrail

GET https://openrouter.ai/api/v1/guardrails/{id}/assignments/keys

List all API key assignments for a specific guardrail. [Management key](/docs/guides/overview/auth/management-api-keys) required.

Reference: https://openrouter.ai/docs/api/api-reference/guardrails/list-guardrail-key-assignments

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: List key assignments for a guardrail
  version: endpoint_guardrails.listGuardrailKeyAssignments
paths:
  /guardrails/{id}/assignments/keys:
    get:
      operationId: list-guardrail-key-assignments
      summary: List key assignments for a guardrail
      description: >-
        List all API key assignments for a specific guardrail. [Management
        key](/docs/guides/overview/auth/management-api-keys) required.
      tags:
        - - subpackage_guardrails
      parameters:
        - name: id
          in: path
          description: The unique identifier of the guardrail
          required: true
          schema:
            type: string
            format: uuid
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
          description: List of key assignments
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Guardrails_listGuardrailKeyAssignments_Response_200
        '401':
          description: Unauthorized - Missing or invalid authentication
          content: {}
        '404':
          description: Guardrail not found
          content: {}
        '500':
          description: Internal Server Error
          content: {}
components:
  schemas:
    GuardrailsIdAssignmentsKeysGetResponsesContentApplicationJsonSchemaDataItems:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the assignment
        key_hash:
          type: string
          description: Hash of the assigned API key
        guardrail_id:
          type: string
          format: uuid
          description: ID of the guardrail
        key_name:
          type: string
          description: Name of the API key
        key_label:
          type: string
          description: Label of the API key
        assigned_by:
          type:
            - string
            - 'null'
          description: User ID of who made the assignment
        created_at:
          type: string
          description: ISO 8601 timestamp of when the assignment was created
      required:
        - id
        - key_hash
        - guardrail_id
        - key_name
        - key_label
        - assigned_by
        - created_at
    Guardrails_listGuardrailKeyAssignments_Response_200:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: >-
              #/components/schemas/GuardrailsIdAssignmentsKeysGetResponsesContentApplicationJsonSchemaDataItems
          description: List of key assignments
        total_count:
          type: number
          format: double
          description: Total number of key assignments for this guardrail
      required:
        - data
        - total_count

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000/assignments/keys"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000/assignments/keys';
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

	url := "https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000/assignments/keys"

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

url = URI("https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000/assignments/keys")

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

HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000/assignments/keys")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000/assignments/keys', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000/assignments/keys");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000/assignments/keys")! as URL,
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