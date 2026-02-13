---
title: Create authorization code
url: https://openrouter.ai/docs/api/api-reference/o-auth/create-auth-keys-code.mdx
source: llms
fetched_at: 2026-02-13T15:17:44.378802-03:00
rendered_js: false
word_count: 28
summary: Technical documentation for the OpenRouter API endpoint that generates authorization codes used in the PKCE flow for creating user-controlled API keys.
tags:
    - openrouter
    - oauth
    - pkce
    - authorization-code
    - api-key-generation
    - authentication
category: api
---

# Create authorization code

POST https://openrouter.ai/api/v1/auth/keys/code
Content-Type: application/json

Create an authorization code for the PKCE flow to generate a user-controlled API key

Reference: https://openrouter.ai/docs/api/api-reference/o-auth/create-auth-keys-code

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create authorization code
  version: endpoint_oAuth.createAuthKeysCode
paths:
  /auth/keys/code:
    post:
      operationId: create-auth-keys-code
      summary: Create authorization code
      description: >-
        Create an authorization code for the PKCE flow to generate a
        user-controlled API key
      tags:
        - - subpackage_oAuth
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successfully created authorization code
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OAuth_createAuthKeysCode_Response_200'
        '400':
          description: Bad Request - Invalid request parameters or malformed input
          content: {}
        '401':
          description: Unauthorized - Authentication required or invalid credentials
          content: {}
        '500':
          description: Internal Server Error - Unexpected server error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                callback_url:
                  type: string
                  format: uri
                  description: >-
                    The callback URL to redirect to after authorization. Note,
                    only https URLs on ports 443 and 3000 are allowed.
                code_challenge:
                  type: string
                  description: PKCE code challenge for enhanced security
                code_challenge_method:
                  $ref: >-
                    #/components/schemas/AuthKeysCodePostRequestBodyContentApplicationJsonSchemaCodeChallengeMethod
                  description: The method used to generate the code challenge
                limit:
                  type: number
                  format: double
                  description: Credit limit for the API key to be created
                expires_at:
                  type:
                    - string
                    - 'null'
                  format: date-time
                  description: Optional expiration time for the API key to be created
              required:
                - callback_url
components:
  schemas:
    AuthKeysCodePostRequestBodyContentApplicationJsonSchemaCodeChallengeMethod:
      type: string
      enum:
        - value: S256
        - value: plain
    AuthKeysCodePostResponsesContentApplicationJsonSchemaData:
      type: object
      properties:
        id:
          type: string
          description: The authorization code ID to use in the exchange request
        app_id:
          type: number
          format: double
          description: The application ID associated with this auth code
        created_at:
          type: string
          description: ISO 8601 timestamp of when the auth code was created
      required:
        - id
        - app_id
        - created_at
    OAuth_createAuthKeysCode_Response_200:
      type: object
      properties:
        data:
          $ref: >-
            #/components/schemas/AuthKeysCodePostResponsesContentApplicationJsonSchemaData
          description: Auth code data
      required:
        - data

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/auth/keys/code"

payload = {
    "callback_url": "https://myapp.com/auth/callback",
    "code_challenge": "E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM",
    "code_challenge_method": "S256",
    "limit": 100
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/auth/keys/code';
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{"callback_url":"https://myapp.com/auth/callback","code_challenge":"E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM","code_challenge_method":"S256","limit":100}'
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

	url := "https://openrouter.ai/api/v1/auth/keys/code"

	payload := strings.NewReader("{\n  \"callback_url\": \"https://myapp.com/auth/callback\",\n  \"code_challenge\": \"E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM\",\n  \"code_challenge_method\": \"S256\",\n  \"limit\": 100\n}")

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

url = URI("https://openrouter.ai/api/v1/auth/keys/code")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"callback_url\": \"https://myapp.com/auth/callback\",\n  \"code_challenge\": \"E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM\",\n  \"code_challenge_method\": \"S256\",\n  \"limit\": 100\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://openrouter.ai/api/v1/auth/keys/code")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"callback_url\": \"https://myapp.com/auth/callback\",\n  \"code_challenge\": \"E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM\",\n  \"code_challenge_method\": \"S256\",\n  \"limit\": 100\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://openrouter.ai/api/v1/auth/keys/code', [
  'body' => '{
  "callback_url": "https://myapp.com/auth/callback",
  "code_challenge": "E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM",
  "code_challenge_method": "S256",
  "limit": 100
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

var client = new RestClient("https://openrouter.ai/api/v1/auth/keys/code");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"callback_url\": \"https://myapp.com/auth/callback\",\n  \"code_challenge\": \"E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM\",\n  \"code_challenge_method\": \"S256\",\n  \"limit\": 100\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "callback_url": "https://myapp.com/auth/callback",
  "code_challenge": "E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM",
  "code_challenge_method": "S256",
  "limit": 100
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/auth/keys/code")! as URL,
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