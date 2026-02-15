---
title: Licenses | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/commons/apis/licenses
source: sitemap
fetched_at: 2026-02-15T09:14:47.038708-03:00
rendered_js: false
word_count: 72
summary: This document provides technical details for an API endpoint used to retrieve a list of all available licenses within the Instructure Learning Object Repository. It specifies authentication requirements via session ID and the expected response format.
tags:
    - api-endpoint
    - instructure-lor
    - licenses
    - authentication
    - session-management
    - rest-api
category: api
---

List all available licenses.

`curl -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/licenses"`

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

200

A list of available licenses

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).