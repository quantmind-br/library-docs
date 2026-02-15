---
title: Outcomes | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/commons/apis/outcomes
source: sitemap
fetched_at: 2026-02-15T09:14:50.06096-03:00
rendered_js: false
word_count: 149
summary: This document describes an API endpoint for searching and retrieving academic outcomes and standards, detailing authentication requirements and search parameters.
tags:
    - academic-outcomes
    - api-endpoint
    - search-query
    - instructure-lor
    - authentication
    - pagination
category: api
---

Search academic outcomes to find standards to attach to a resource. Returns 20 outcomes at a time.

**Example:** `curl -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/outcomes/query?query=Common&authority=UT&federal=true"`

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

querystringRequired

The text to search for in the outcomes

authoritystringOptional

The comma separated authority codes for the outcomes being searched for. The authority code is the two letter state abbreviation, or "CC" for federal Common Core. Defaults to all authorities.

offsetintegerOptional

The offset the query results should start at. Used to paginate through the results. Defaults at 0.

Default: `0`

200

An array of the results of the query

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).