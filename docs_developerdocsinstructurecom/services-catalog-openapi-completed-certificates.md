---
title: Completed Certificates | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/catalog/openapi/completed_certificates
source: sitemap
fetched_at: 2026-02-15T09:14:30.509995-03:00
rendered_js: false
word_count: 66
summary: This document specifies the authentication requirements and parameters for an API endpoint used to retrieve a list of a user's completed course certificates.
tags:
    - api-authentication
    - certificates
    - user-completions
    - endpoint-specification
category: api
---

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

only\_certificatesbooleanOptional

Indicates if the courses without certificates should be included, default is to include all courses

200

Listing user's completions with a certificate

/api/v1/completed\_certificates

200

Listing user's completions with a certificate

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).