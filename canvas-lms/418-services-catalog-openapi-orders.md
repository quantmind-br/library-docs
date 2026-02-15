---
title: Orders | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/catalog/openapi/orders
source: sitemap
fetched_at: 2026-02-15T09:10:53.884279-03:00
rendered_js: false
word_count: 89
summary: This document outlines the authentication requirements and query parameters used to retrieve and filter order data via an API.
tags:
    - api-authentication
    - query-parameters
    - canvas-api
    - data-filtering
    - order-management
category: reference
---

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

fromstringOptional

Earliest date/time to return. Suggested format YYYY-MM-DDTHH:MM:SSZ, e.g. 2018-01-01T00:00:00Z. System time zone is UTC.

tostringOptional

Latest date/time to return. See 'from' above for format.

canvas\_user\_idstringOptional

Return only orders for the specified Canvas user ID

completedstringOptional

When set, only return orders that were completed successfully

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).