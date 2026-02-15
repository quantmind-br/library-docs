---
title: Authentication | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/parchment-digital-badges/authentication
source: sitemap
fetched_at: 2026-02-15T08:58:58.025978-03:00
rendered_js: false
word_count: 105
summary: This document explains how to authenticate requests to the Parchment Digital Badges API using bearer tokens and provides instructions for renewing expired tokens via refresh tokens.
tags:
    - authentication
    - access-tokens
    - refresh-tokens
    - api-authorization
    - bearer-auth
    - parchment-api
category: guide
---

There are two primary ways to obtain an access token:

Once you obtained an access token from the Parchment Digital Badges API domain for your region, you'll need to provide an Authorization header of type "Bearer" for all additional requests. For example:

```
curl'https://{BADGES_DOMAIN}/v2/users/self'-H"Authorization: Bearer YOURACCESSTOKEN"
```

Access tokens will expire, and if an expired token is used, a 401 status code will be returned.

The refresh token can be used to automatically renew an access token without requiring the password again. For example:

```
curl-XPOST'https://{BADGES_DOMAIN}/o/token'-d"grant_type=refresh_token&refresh_token=YOURREFRESHTOKEN"
```

Last updated 3 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).