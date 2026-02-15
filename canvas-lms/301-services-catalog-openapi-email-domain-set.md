---
title: Email Domain Set | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/catalog/openapi/email_domain_set
source: sitemap
fetched_at: 2026-02-15T09:10:30.94397-03:00
rendered_js: false
word_count: 142
summary: This document specifies the API endpoints for managing email domain sets, including functionality for retrieving, updating, and searching domain sets and listing associated promotions.
tags:
    - api-endpoints
    - email-domain-sets
    - rest-api
    - authentication
    - resource-management
category: api
---

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

200

Getting a specific email domain set

/api/v1/email\_domain\_sets/{id}

200

Getting a specific email domain set

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

200

Updating an email domain set

/api/v1/email\_domain\_sets/{id}

200

Updating an email domain set

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

200

List promotions by email domain set

/api/v1/email\_domain\_sets/{id}/promotions

200

List promotions by email domain set

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

searchstringOptional

A value to filter the Email Domain Sets by name

exactstringOptional

A boolean to set whether the search should only include results that match exactly

200

Listing email domain sets

/api/v1/email\_domain\_sets

200

Listing email domain sets

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).