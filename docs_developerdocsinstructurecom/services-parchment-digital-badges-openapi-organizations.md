---
title: Organizations | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/parchment-digital-badges/openapi/organizations
source: sitemap
fetched_at: 2026-02-15T08:56:02.324031-03:00
rendered_js: false
word_count: 109
summary: This document provides technical details for API endpoints used to retrieve a user's administrative organizations and list public issuers with support for pagination and filtering.
tags:
    - api-endpoints
    - organization-management
    - public-issuers
    - oauth2-scopes
    - rest-api
    - pagination-filtering
category: api
---

### Get a list of Organizations where the authenticated user is admin

This endpoint requires the following scopes:

- : Read organization data

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

### List public issuers for the specified organization with pagination and optional name filtering

nameQuerystring · max: 256Optional

Case-insensitive filter for the name of the issuers

numstring · max: 9223372036854776000Optional

Number of items to return per page

Example: `10`

pagestring · min: 1Optional

Index of the requested page (1-based)

Example: `1`

/v2/organizations/{id}/public-issuers

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).