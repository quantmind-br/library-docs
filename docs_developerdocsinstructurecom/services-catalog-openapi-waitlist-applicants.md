---
title: Waitlist Applicants | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/catalog/openapi/waitlist_applicants
source: sitemap
fetched_at: 2026-02-15T09:11:21.059329-03:00
rendered_js: false
word_count: 106
summary: This document outlines API authentication requirements and endpoint parameters for retrieving and deleting applicant records within a listing system.
tags:
    - api-authentication
    - applicant-management
    - endpoint-parameters
    - data-filtering
    - deletion
category: api
---

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

listing\_idstringOptional

Only include applicants for the specified listing

statusstringOptional

Only include applicants for the specified status (waitlist, accepted, declined, or expired)

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

listing\_idintegerRequired

Only delete applicants for the specified listing

canvas\_user\_idstringOptional

Only delete applicants with the specified canvas user id if specified

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

200

Getting a specific applicant record

200

Getting a specific applicant record

Last updated 6 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).