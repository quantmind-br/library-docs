---
title: Account Domain Lookups | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/account_domain_lookups
source: sitemap
fetched_at: 2026-02-15T09:05:35.704061-03:00
rendered_js: false
word_count: 72
summary: This document describes the Canvas LMS API endpoint for searching account domains using name or domain partial matches. It provides details on authentication scopes, request parameters, and example JSON responses.
tags:
    - canvas-lms
    - api-endpoint
    - account-search
    - domain-lookup
    - rest-api
category: api
---

## Account Domain Lookups API

`GET /api/v1/accounts/search`

**Scope:** `url:GET|/api/v1/accounts/search`

Returns a list of up to 5 matching account domains

Partial match on name / domain are supported

**Request Parameters:**

**Example Request:**

```
curlhttps://<canvas>/api/v1/accounts/search\
-G-H'Authorization: Bearer <ACCESS_TOKEN>'\
-d'name=utah'
```

**Example Response:**

```
[
{
"name":"University of Utah",
"domain":"utah.edu",
"distance":null,// distance is always nil, but preserved in the api response for backwards compatibility
"authentication_provider":"canvas",// which authentication_provider param to pass to the oauth flow; may be NULL
},
...
]
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).