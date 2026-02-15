---
title: Insights | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/studio/api-reference/insights
source: sitemap
fetched_at: 2026-02-15T09:12:35.764068-03:00
rendered_js: false
word_count: 225
summary: This document outlines API endpoints for retrieving CSV-formatted reports on media engagement metrics and detailed viewer completion data for specific perspectives.
tags:
    - api-reference
    - media-insights
    - data-export
    - analytics
    - viewer-tracking
category: api
---

### Get media insights overview for a perspective

This endpoint returns a csv file containing video views, time viewed, unique viewers and time based viewership data.

AuthorizationstringRequired

perspective\_uuidstringRequired

The ID of the perspective.

rolestring · enumOptional

A role to filter the users by. If not provided all insights data is aggregated.

Possible values:

200

Returns overview of perspective insights in a CSV.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The perspective was not found by ID.

/perspectives/{perspective\_uuid}/insights/overview

### Get all viewers' Insights data for a perspective

This endpoint returns a csv file containing user name, email, role(s), completion rate and time based completion data.

AuthorizationstringRequired

perspective\_uuidstringRequired

The ID of the perspective.

rolestring · enumOptional

A role to filter the users by. If not provided all insights data is aggregated.

Possible values:

200

Returns perspective insights for users in a CSV.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The perspective was not found by ID.

422

The provided parameters are invalid.

/perspectives/{perspective\_uuid}/insights/users

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).