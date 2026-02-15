---
title: Bulk Enrollments | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/catalog/openapi/bulk_enrollments
source: sitemap
fetched_at: 2026-02-15T09:10:54.403368-03:00
rendered_js: false
word_count: 85
summary: This document outlines the API endpoints and required parameters for retrieving individual bulk enrollment records and listing enrollment history.
tags:
    - api-reference
    - bulk-enrollment
    - enrollment-history
    - canvas-api
    - authentication
category: api
---

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

200

Getting a specific bulk enrollment

/api/v1/order\_items/history/bulk\_enrollments/{id}

200

Getting a specific bulk enrollment

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

fromstringOptional

Only include bulk enrollments from this date

tostringOptional

Only include bulk enrollments to this date

canvas\_user\_idsstringOptional

Only include bulk enrollments for the specified canvas user ids

/api/v1/order\_items/history/bulk\_enrollments

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).