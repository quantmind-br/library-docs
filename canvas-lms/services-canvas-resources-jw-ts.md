---
title: JWTs | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/jw_ts
source: sitemap
fetched_at: 2026-02-15T09:07:56.191005-03:00
rendered_js: false
word_count: 291
summary: This document details the API endpoints for generating and refreshing short-lived JSON Web Tokens used to authenticate with services in the Canvas ecosystem.
tags:
    - canvas-api
    - jwt
    - authentication
    - token-management
    - json-web-tokens
    - api-reference
category: api
---

Short term tokens useful for talking to other services in the Canvas Ecosystem. Note: JWTs have no value or use directly against the Canvas API, and expire after one hour

**A JWT object looks like:**

```
{
  // The signed, encrypted, base64 encoded JWT
  "token": "ZXlKaGJHY2lPaUprYVhJaUxDSmxibU1pT2lKQk1qVTJSME5OSW4wLi5QbnAzS1QzLUJkZ3lQZHgtLm5JT0pOV01iZmdtQ0g3WWtybjhLeHlMbW13cl9yZExXTXF3Y0IwbXkzZDd3V1NDd0JYQkV0UTRtTVNJSVRrX0FJcG0zSU1DeThMcW5NdzA0ckdHVTkweDB3MmNJbjdHeWxOUXdveU5ZZ3UwOEN4TkZteUpCeW5FVktrdU05QlRyZXZ3Y1ZTN2hvaC1WZHRqM19PR3duRm5yUVgwSFhFVFc4R28tUGxoQVUtUnhKT0pNakx1OUxYd2NDUzZsaW9ZMno5NVU3T0hLSGNpaDBmSGVjN2FzekVJT3g4NExUeHlReGxYU3BtbFZ5LVNuYWdfbVJUeU5yNHNsMmlDWFcwSzZCNDhpWHJ1clJVVm1LUkVlVTl4ZVVJcTJPaWNpSHpfemJ0X3FrMjhkdzRyajZXRnBHSlZPNWcwTlUzVHlSWk5qdHg1S2NrTjVSQjZ1X2FzWTBScjhTY2VhNFk3Y2JFX01wcm54cFZTNDFIekVVSVRNdzVMTk1GLVpQZy52LVVDTkVJYk8zQ09EVEhPRnFXLUFR"
}
```

[JwtsController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/jwts_controller.rb)

`POST /api/v1/jwts`

**Scope:** `url:POST|/api/v1/jwts`

Create a unique JWT for use with other Canvas services

Generates a different JWT each time it’s called. Each JWT expires after a short window (1 hour)

**Request Parameters:**

Adds additional data to the JWT to be used by the consuming service workflow

The type of the context to generate the JWT for, in case the workflow requires it. Case insensitive.

Allowed values: `Course`, `User`, `Account`

The id of the context to generate the JWT for, in case the workflow requires it.

The uuid of the context to generate the JWT for, in case the workflow requires it. Note that context\_id and context\_uuid are mutually exclusive. If both are provided, an error will be returned.

Defaults to true. If false, the JWT will be signed, but not encrypted, for use in downstream services. The default encrypted behaviour can be used to talk to Canvas itself.

**Example Request:**

```
curl'https://<canvas>/api/v1/jwts'\
-XPOST\
-H"Accept: application/json"\
-H'Authorization: Bearer <token>'
```

Returns a [JWT](https://developerdocs.instructure.com/services/canvas/resources/jw_ts#jwt) object.

[JwtsController#refresharrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/jwts_controller.rb)

`POST /api/v1/jwts/refresh`

**Scope:** `url:POST|/api/v1/jwts/refresh`

Refresh a JWT for use with other canvas services

Generates a different JWT each time it’s called, each one expires after a short window (1 hour).

**Request Parameters:**

An existing JWT token to be refreshed. The new token will have the same context and workflows as the existing token.

**Example Request:**

```
curl'https://<canvas>/api/v1/jwts/refresh'\
-XPOST\
-H"Accept: application/json"\
-H'Authorization: Bearer <token>'
-d'jwt=<jwt>'
```

Returns a [JWT](https://developerdocs.instructure.com/services/canvas/resources/jw_ts#jwt) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).