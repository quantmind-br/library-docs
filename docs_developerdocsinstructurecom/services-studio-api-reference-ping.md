---
title: Ping | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/studio/api-reference/ping
source: sitemap
fetched_at: 2026-02-15T09:12:35.325391-03:00
rendered_js: false
word_count: 69
summary: This document describes a diagnostic test endpoint for the Studio public API used to verify authentication and connectivity by returning a 'pong' response.
tags:
    - studio-api
    - public-api
    - authentication
    - api-testing
    - connectivity-verification
category: api
---

### Test endpoint for the Studio public API

Allows for verification of a consumer's plumbing to the public API.

AuthorizationstringRequired

200

If called with correct authentication, this API should have a text reply of 'pong'.

ResponsestringExample: `pong`

401

Authorization information is missing or invalid.

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).