---
title: Courses | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/commons/apis/courses
source: sitemap
fetched_at: 2026-02-15T09:14:38.687474-03:00
rendered_js: false
word_count: 141
summary: This document describes an API endpoint for retrieving a list of active courses associated with a user's session, specifically filtering for roles such as teachers, TAs, and designers.
tags:
    - api-endpoint
    - session-authentication
    - canvas-integration
    - course-management
    - user-enrollment
category: api
---

List courses according to your session. The courses are limited to those available to the current user (based on the active session). This endpoint is almost just a proxy for [Canvas Courses API](https://canvas.instructure.com/doc/api/courses.html#method.courses.index) except that certain filters can be applied on the list returned from Canvas. The courses are filtered to those that are not concluded and are available to content contributors, specifically, teachers, TAs, and designers.

**Example:** `curl -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/courses"`

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

200

An array of the courses the user is enrolled in

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).