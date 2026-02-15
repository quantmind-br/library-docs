---
title: API Token Scopes | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/api_token_scopes
source: sitemap
fetched_at: 2026-02-15T08:57:52.838595-03:00
rendered_js: false
word_count: 127
summary: This document describes the Scopes API endpoint used to retrieve a list of available authorization scopes for developer keys and access tokens.
tags:
    - canvas-lms
    - api-scopes
    - developer-keys
    - access-tokens
    - rest-api
    - authentication
category: api
---

BETA: This API resource is not finalized, and there could be breaking changes before its final release.

API for retrieving API scopes

**A Scope object looks like:**

```
{
  // The resource the scope is associated with
"resource": "courses",
  // The localized resource name
"resource_name": "Courses",
  // The controller the scope is associated to
"controller": "courses",
  // The controller action the scope is associated to
"action": "index",
  // The HTTP verb for the scope
"verb": "GET",
  // The identifier for the scope
"scope": "url:GET|/api/v1/courses"
}
```

[ScopesApiController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/scopes_api_controller.rb)

BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.

`GET /api/v1/accounts/:account_id/scopes`

**Scope:** `url:GET|/api/v1/accounts/:account_id/scopes`

A list of scopes that can be applied to developer keys and access tokens.

**Request Parameters:**

The attribute to group the scopes by. By default no grouping is done.

Allowed values: `resource_name`

Returns a list of [Scope](https://developerdocs.instructure.com/services/canvas/resources/api_token_scopes#scope) objects.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 2 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).