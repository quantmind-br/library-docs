---
title: Bulk assign keys to a guardrail
url: https://openrouter.ai/docs/api/api-reference/guardrails/bulk-assign-keys-to-guardrail.mdx
source: llms
fetched_at: 2026-02-13T15:18:31.090418-03:00
rendered_js: false
word_count: 28
summary: This API reference explains how to assign multiple API keys to a specific guardrail using key hashes and provides implementation examples across several programming languages.
tags:
    - openrouter-api
    - guardrails
    - api-management
    - bulk-operations
    - authentication
category: api
---

# Bulk assign keys to a guardrail

POST https://openrouter.ai/api/v1/guardrails/{id}/assignments/keys
Content-Type: application/json

Assign multiple API keys to a specific guardrail. [Management key](/docs/guides/overview/auth/management-api-keys) required.

Reference: https://openrouter.ai/docs/api/api-reference/guardrails/bulk-assign-keys-to-guardrail

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Bulk assign keys to a guardrail
  version: endpoint_guardrails.bulkAssignKeysToGuardrail
paths:
  /guardrails/{id}/assignments/keys:
    post:
      operationId: bulk-assign-keys-to-guardrail
      summary: Bulk assign keys to a guardrail
      description: >-
        Assign multiple API keys to a specific guardrail. [Management
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
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Assignment result
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Guardrails_bulkAssignKeysToGuardrail_Response_200
        '400':
          description: Bad Request - Invalid input
          content: {}
        '401':
          description: Unauthorized - Missing or invalid authentication
          content: {}
        '404':
          description: Guardrail not found
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
                key_hashes:
                  type: array
                  items:
                    type: string
                  description: Array of API key hashes to assign to the guardrail
              required:
                - key_hashes
components:
  schemas:
    Guardrails_bulkAssignKeysToGuardrail_Response_200:
      type: object
      properties:
        assigned_count:
          type: number
          format: double
          description: Number of keys successfully assigned
      required:
        - assigned_count

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000/assignments/keys"

payload = { "key_hashes": ["c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93"] }
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000/assignments/keys';
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{"key_hashes":["c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93"]}'
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

	url := "https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000/assignments/keys"

	payload := strings.NewReader("{\n  \"key_hashes\": [\n    \"c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93\"\n  ]\n}")

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

url = URI("https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000/assignments/keys")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"key_hashes\": [\n    \"c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000/assignments/keys")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"key_hashes\": [\n    \"c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93\"\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000/assignments/keys', [
  'body' => '{
  "key_hashes": [
    "c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93"
  ]
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

var client = new RestClient("https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000/assignments/keys");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"key_hashes\": [\n    \"c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = ["key_hashes": ["c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93"]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000/assignments/keys")! as URL,
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