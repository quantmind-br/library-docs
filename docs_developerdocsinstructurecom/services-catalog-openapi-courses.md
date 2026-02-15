---
title: Courses | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/catalog/openapi/courses
source: sitemap
fetched_at: 2026-02-15T09:05:03.860949-03:00
rendered_js: false
word_count: 180
summary: This document details API endpoints for managing course listings, covering actions such as archiving, reactivating, searching, and updating course SKUs via bulk operations.
tags:
    - api-endpoints
    - course-management
    - rest-api
    - authentication
    - sku-updates
    - bulk-actions
category: api
---

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

product\_actionstringRequired

Action to perform. Possible values: archive, reactivate

product\_idsinteger\[]Required

Array of product ids to perform the action on

200

All courses have been successfully processed

422

Some courses have failed to process successfully

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

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

attachmentstring · binaryRequired

CSV containing a Catalog Course ID and Catalog Course SKU header

/api/v1/courses/update\_skus

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

200

Getting a specific course

200

Getting a specific course

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

204

Deleting a specific course

204

Deleting a specific course

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).