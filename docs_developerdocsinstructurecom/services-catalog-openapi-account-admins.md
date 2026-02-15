---
title: Account Admins | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/catalog/openapi/account_admins
source: sitemap
fetched_at: 2026-02-15T08:58:26.122257-03:00
rendered_js: false
word_count: 141
summary: This document outlines the API endpoints and authentication requirements for managing account admin associations, including creating, listing, and deleting administrative roles.
tags:
    - api-documentation
    - account-admins
    - user-management
    - authentication
    - rest-api
    - canvas-lms
category: api
---

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

pageintegerOptional

Page number for pagination (defaults to 0)

searchstringOptional

Search query to filter account admins

per\_pagestringOptional

Number of results per page

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

canvas\_user\_idstringRequired

email\_addressstringRequired

Email address of the user

account\_idsstringRequired

Array of account IDs to associate with the user

201

Creating an account admin association

201

Creating an account admin association

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

account\_idintegerRequired

204

Deleting a specific account admin association

/api/v1/account\_admins/{id}/accounts/{account\_id}

204

Deleting a specific account admin association

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

204

Deleting all account admin associations

/api/v1/account\_admins/{id}

204

Deleting all account admin associations

Last updated 2 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).