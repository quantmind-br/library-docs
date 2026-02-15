---
title: Programs | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/catalog/openapi/programs
source: sitemap
fetched_at: 2026-02-15T09:05:00.236612-03:00
rendered_js: false
word_count: 157
summary: This document provides technical specifications for API endpoints used to manage programs, covering authentication requirements and actions such as archiving, reactivating, and searching.
tags:
    - api-authentication
    - program-management
    - rest-api
    - instructure-catalog
    - endpoint-reference
    - product-actions
category: api
---

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

product\_actionstringRequired

Action to perform. Possible values: archive, reactivate

product\_idsinteger\[]Required

Array of product ids to perform the action on

200

All programs have been successfully processed

422

Some programs have failed to process successfully

/api/v1/programs/archived

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

200

Getting a specific program

200

Getting a specific program

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

204

Deleting a specific program

204

Deleting a specific program

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

descriptionstringOptional

listing\_pathstringOptional

is\_enrollablestringOptional

Filter by whether the listing is currently open for enrollment (true/false)

querystringOptional

General search query (title OR description OR tags)

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).