---
title: Tags | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/catalog/openapi/tags
source: sitemap
fetched_at: 2026-02-15T09:04:54.725343-03:00
rendered_js: false
word_count: 142
summary: This document outlines the authentication requirements and parameter specifications for managing tags through an API, including creation, search, and deletion operations.
tags:
    - api-authentication
    - tag-management
    - rest-api
    - parameter-definitions
    - endpoint-documentation
category: api
---

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

namestringRequired

New tag name (minimum 1 and maximum 255 characters)

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

idsinteger\[]Required

Array of tag IDs to delete

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

product\_idsstringOptional

List of product ids (maximum 20 ids)

namestringOptional

Search value which will be searched in tag name and associated products names

has\_categorybooleanOptional

updated\_at\_fromstringOptional

updated\_at\_tostringOptional

created\_at\_fromstringOptional

created\_at\_tostringOptional

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

namestringRequired

Tag name (minimum 1 and maximum 255 characters)

product\_idsstringOptional

List of product ids associate to this tag

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).