---
title: List all providers
url: https://openrouter.ai/docs/api/api-reference/providers/list-providers.mdx
source: llms
fetched_at: 2026-02-13T15:18:06.956817-03:00
rendered_js: false
word_count: 12
summary: This document provides the API specification and multi-language code examples for retrieving a list of all model providers available on OpenRouter.
tags:
    - openrouter
    - api-reference
    - providers
    - http-get
    - rest-api
category: api
---

# List all providers

GET https://openrouter.ai/api/v1/providers

Reference: https://openrouter.ai/docs/api/api-reference/providers/list-providers

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: List all providers
  version: endpoint_providers.listProviders
paths:
  /providers:
    get:
      operationId: list-providers
      summary: List all providers
      tags:
        - - subpackage_providers
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Returns a list of providers
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Providers_listProviders_Response_200'
        '500':
          description: Internal Server Error - Unexpected server error
          content: {}
components:
  schemas:
    ProvidersGetResponsesContentApplicationJsonSchemaDataItems:
      type: object
      properties:
        name:
          type: string
          description: Display name of the provider
        slug:
          type: string
          description: URL-friendly identifier for the provider
        privacy_policy_url:
          type:
            - string
            - 'null'
          description: URL to the provider's privacy policy
        terms_of_service_url:
          type:
            - string
            - 'null'
          description: URL to the provider's terms of service
        status_page_url:
          type:
            - string
            - 'null'
          description: URL to the provider's status page
      required:
        - name
        - slug
        - privacy_policy_url
    Providers_listProviders_Response_200:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: >-
              #/components/schemas/ProvidersGetResponsesContentApplicationJsonSchemaDataItems
      required:
        - data

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/providers"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/providers';
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

	url := "https://openrouter.ai/api/v1/providers"

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

url = URI("https://openrouter.ai/api/v1/providers")

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

HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/providers")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/providers', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://openrouter.ai/api/v1/providers");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/providers")! as URL,
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