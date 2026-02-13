---
title: List all member assignments
url: https://openrouter.ai/docs/api/api-reference/guardrails/list-member-assignments.mdx
source: llms
fetched_at: 2026-02-13T15:18:26.978074-03:00
rendered_js: false
word_count: 26
summary: This document provides the API specification and code examples for retrieving a paginated list of guardrail assignments for organization members via the OpenRouter management API.
tags:
    - openrouter-api
    - guardrails
    - member-management
    - rest-api
    - authentication
category: api
---

# List all member assignments

GET https://openrouter.ai/api/v1/guardrails/assignments/members

List all organization member guardrail assignments for the authenticated user. [Management key](/docs/guides/overview/auth/management-api-keys) required.

Reference: https://openrouter.ai/docs/api/api-reference/guardrails/list-member-assignments

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: List all member assignments
  version: endpoint_guardrails.listMemberAssignments
paths:
  /guardrails/assignments/members:
    get:
      operationId: list-member-assignments
      summary: List all member assignments
      description: >-
        List all organization member guardrail assignments for the authenticated
        user. [Management key](/docs/guides/overview/auth/management-api-keys)
        required.
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
          description: List of member assignments
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Guardrails_listMemberAssignments_Response_200
        '401':
          description: Unauthorized - Missing or invalid authentication
          content: {}
        '500':
          description: Internal Server Error
          content: {}
components:
  schemas:
    GuardrailsAssignmentsMembersGetResponsesContentApplicationJsonSchemaDataItems:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the assignment
        user_id:
          type: string
          description: Clerk user ID of the assigned member
        organization_id:
          type: string
          description: Organization ID
        guardrail_id:
          type: string
          format: uuid
          description: ID of the guardrail
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
        - user_id
        - organization_id
        - guardrail_id
        - assigned_by
        - created_at
    Guardrails_listMemberAssignments_Response_200:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: >-
              #/components/schemas/GuardrailsAssignmentsMembersGetResponsesContentApplicationJsonSchemaDataItems
          description: List of member assignments
        total_count:
          type: number
          format: double
          description: Total number of member assignments
      required:
        - data
        - total_count

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/guardrails/assignments/members"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/guardrails/assignments/members';
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

	url := "https://openrouter.ai/api/v1/guardrails/assignments/members"

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

url = URI("https://openrouter.ai/api/v1/guardrails/assignments/members")

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

HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/guardrails/assignments/members")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/guardrails/assignments/members', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://openrouter.ai/api/v1/guardrails/assignments/members");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/guardrails/assignments/members")! as URL,
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