---
title: Courses | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/studio/api-reference/courses
source: sitemap
fetched_at: 2026-02-15T09:12:28.70688-03:00
rendered_js: false
word_count: 176
summary: This document outlines API endpoints for retrieving course collection details and the list of perspectives associated with a specific course ID.
tags:
    - api-endpoints
    - course-management
    - http-status-codes
    - authorization
    - data-retrieval
category: api
---

This endpoint will return the course collection information.

AuthorizationstringRequired

course\_idintegerRequired

ID of the course to get the details of.

200

After a successful request, the endpoint returns HTTP 200.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

If course is not found with the provided id, the endpoint returns HTTP 404.

### Get a list of perspectives of a course

This endpoint will return all the perspectives in a course.

AuthorizationstringRequired

course\_idintegerRequired

ID of the course to retrieve perspectives from

200

After a successful request, the endpoint returns HTTP 200.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

If course is not found with the provided id, the endpoint returns HTTP 404.

/courses/{course\_id}/perspectives

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).